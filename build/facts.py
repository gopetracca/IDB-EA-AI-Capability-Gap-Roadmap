# -*- coding: utf-8 -*-
"""Load the facts and apply a scale. The only module that reads facts/.

Everything a builder needs comes through `Model`: the capability map, the
offerings and assets, the owners, the observations (rolled up where ADR-0014
says so), the source register, the obligations register and the use-case
questions.  Builders never open facts/*.json themselves, so a change to a
file's shape is absorbed here once.

Scales are discovered by listing scales/ and validated against the contract in
scales/README.md before anything is derived from them.
"""
import json, os, re, itertools, importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FACTS = os.path.join(ROOT, 'facts')
SCALES = os.path.join(ROOT, 'scales')

OBS_KEYS = ('practised', 'enabled', 'skilled', 'defined')


def _load(name):
    with open(os.path.join(FACTS, name), encoding='utf-8') as f:
        return json.load(f)


def save_facts(name, doc):
    """Write one facts file in the repository's canonical JSON form.

    The only writer of facts/ outside a human editor is `build.py ingest`, and
    it must produce the same bytes a hand edit would, so diffs stay readable.
    """
    with open(os.path.join(FACTS, name), 'w', encoding='utf-8') as f:
        f.write(json.dumps(doc, ensure_ascii=False, indent=1))


class _CapObs(dict):
    """`obs_by_cap`, with a guard on the one mistake this shape invites.

    `practised` moved to the criterion rows in ADR-0014, so it is absent here.
    The `.get(type, {}).get('value', 'unknown')` idiom used throughout the
    builders would swallow that and report `unknown` for a capability whose
    every criterion is `yes` - a wrong number in a report, with no exception and
    nothing for `build.py check` to catch, because the facts are valid and only
    the reader is wrong.  It reached a published view once; hence the guard.
    """

    def __init__(self, criterion_types):
        dict.__init__(self)
        self._crit = set(criterion_types)

    def _guard(self, key):
        if key in self._crit:
            raise KeyError(
                "%r is recorded per L3 criterion, not on the capability "
                "(ADR-0014). Use Model.values(cid)[%r] for the rolled-up value, "
                "or Model.criteria_obs(cid, %r) for the criterion rows."
                % (key, key, key))

    def __getitem__(self, key):
        self._guard(key)
        return dict.__getitem__(self, key)

    def get(self, key, default=None):
        self._guard(key)
        return dict.get(self, key, default)


class _CapObsRow(dict):
    """One capability's row map, guarding the second `.get` in the chain."""

    def __init__(self, crit):
        dict.__init__(self)
        self._crit = crit

    def _guard(self, key):
        if key in self._crit:
            raise KeyError(
                "%r is recorded per L3 criterion, not on the capability "
                "(ADR-0014). Use Model.values(cid)[%r] for the rolled-up value, "
                "or Model.criteria_obs(cid, %r) for the criterion rows."
                % (key, key, key))

    def __getitem__(self, key):
        self._guard(key)
        return dict.__getitem__(self, key)

    def get(self, key, default=None):
        self._guard(key)
        return dict.get(self, key, default)


class Model(object):
    """Every fact in the repository, joined and ready to read."""

    def __init__(self):
        c = _load('capabilities.json')
        self.domains = c['domains']
        self.capabilities = c['capabilities']
        self.by_id = {x['id']: x for x in self.capabilities}
        self.domain_by_id = {d['id']: d for d in self.domains}
        self.criterion_parent = {x['id']: cap['id'] for cap in self.capabilities
                                 for x in cap['criteria']}

        o = _load('offerings.json')
        self.offerings = o['offerings']
        self.offering_by_id = {x['id']: x for x in self.offerings}
        self.generic_assets = o['generic_assets']
        self.consumption_models = o['consumption_models']

        a = _load('assets.json')
        self.assets = a['assets']
        self.asset_by_id = {x['id']: x for x in self.assets}
        # status -> {"released": bool, "meaning": str}.  What counts as
        # released is a fact about the Bank's release process, declared once
        # here rather than hard-coded in every builder.
        self.asset_statuses = a.get('statuses', {})

        w = _load('owners.json')
        self.units = w['units']
        self.unit_by_name = {u['name']: u for u in self.units}
        self.owner_map = {m['capability']: m for m in w['mapping']}
        self.owners_source = w

        b = _load('observations.json')
        self.observation_types = b['observation_types']
        self.observation_values = b['values']
        self.observations = b['observations']

        s = _load('sources.json')
        self.sources_doc = s
        self.sources = s['sources']
        self.source_by_id = {x['id']: x for x in self.sources}
        self.source_grades = s.get('grades', {})
        self._normalize = dict(s.get('normalize', {}))
        self._normalize.update(s.get('extra_from', {}))

        ob = _load('obligations.json')
        self.obligations = ob['obligations'] if isinstance(ob, dict) else ob
        self.enablement_context = _load('enablement-context.json')
        self.questions = _load('questions.json')['questions']

        # Which observations are recorded per L3 criterion rather than per
        # capability.  Today that is `practised` alone (ADR-0014).
        self.criterion_types = [t['id'] for t in self.observation_types
                                if t.get('recorded_at') == 'criterion']

        # capability -> {observation type: row}, for capability-level types only.
        # Reading a criterion-level observation from here raises rather than
        # quietly yielding 'unknown' - see _CapObs.
        self.obs_by_cap = _CapObs(self.criterion_types)
        # capability -> {observation type: {criterion id: row}}
        self.obs_by_crit = {}
        for r in self.observations:
            if r.get('criterion'):
                (self.obs_by_crit.setdefault(r['capability'], {})
                     .setdefault(r['observation'], {})[r['criterion']]) = r
            else:
                (self.obs_by_cap.setdefault(
                    r['capability'], _CapObsRow(self.criterion_types))
                 [r['observation']]) = r

        # capability -> offerings enabling it
        self.offerings_for = {}
        for off in self.offerings:
            for cid in off['enables']:
                self.offerings_for.setdefault(cid, []).append(off)

    # ------------------------------------------------------------ assets
    def released(self, asset):
        """True if this asset's status counts as released to delivery teams."""
        if isinstance(asset, str):
            asset = self.asset_by_id[asset]
        return bool(self.asset_statuses.get(asset['status'], {}).get('released'))

    def release_count(self, offering):
        """(released, total) for an offering, derived from asset statuses."""
        ids = offering['assets']
        return sum(1 for x in ids if self.released(x)), len(ids)

    def pending_assets(self, offering=None):
        """Assets not yet released - for one offering, or across the estate."""
        ids = offering['assets'] if offering else [x['id'] for x in self.assets]
        return [self.asset_by_id[x] for x in ids if not self.released(x)]

    def offering_complete(self, offering):
        rel, tot = self.release_count(offering)
        return rel == tot

    # ------------------------------------------------------------ sources
    def resolve_source(self, citation):
        """(source record or None, locus string) for a citation string as it
        appears on a capability.  Unresolved citations return (None, '')."""
        e = self._normalize.get(citation)
        if not e:
            return None, ''
        return self.source_by_id.get(e.get('source')), e.get('locus', '') or ''

    def capability_sources(self, cid):
        """[(citation, source or None, locus)] for one capability."""
        out = []
        for s in self.by_id[cid].get('sources', []):
            src, locus = self.resolve_source(s)
            out.append((s, src, locus))
        return out

    # ------------------------------------------------------------ observations
    def criteria_obs(self, cid, otype):
        """[(criterion, row)] in taxonomy order for one capability."""
        rows = self.obs_by_crit.get(cid, {}).get(otype, {})
        return [(x, rows.get(x['id'], {}))
                for x in self.by_id.get(cid, {}).get('criteria', [])]

    def cap_obs(self, cid, otype):
        """The capability-level row for one observation type, or {}."""
        row = dict.get(self.obs_by_cap, cid, {})
        return dict.get(row, otype, {})

    def roll_up(self, cid, otype):
        """Derive one capability-level value from its L3 criterion observations.

        Strict, all-or-nothing (ADR-0014).  One weak link stops the claim: the
        same asymmetry the level ladder enforces, and what stops a capability
        reading as fully performed when a third of it has never been done.

        `unknown` drops out of the denominator rather than un-rating the whole
        capability - a reviewer who looked at four of six criteria produced real
        information.  `unknown` is never a zero, at either level.

        But `yes` requires a COMPLETE look.  An unexamined criterion cannot be
        counted as satisfied, so one `yes` with five criteria never looked at is
        `partial`, not `yes`.  Excluding `unknown` from the denominator keeps a
        partial capability ratable; letting it also unlock `yes` would let a
        single observation carry a whole capability, which is exactly the
        over-claiming ADR-0013 exists to prevent.
        """
        vals = [r.get('value', 'unknown') for _, r in self.criteria_obs(cid, otype)]
        return roll_up_values(vals)

    def values(self, cid):
        """{'practised': 'yes', ...} for one capability.

        Criterion-level observations are rolled up here, so every consumer sees
        four capability values whether or not the underlying fact is recorded at
        L2 or L3.
        """
        out = {}
        for t in self.observation_types:
            if t['id'] in self.criterion_types:
                out[t['id']] = self.roll_up(cid, t['id'])
            else:
                out[t['id']] = self.cap_obs(cid, t['id']).get('value', 'unknown')
        return out

    def rate(self, scale, cid):
        return scale.level(self.values(cid))

    def rate_all(self, scale):
        return {c['id']: self.rate(scale, c['id']) for c in self.capabilities}

    # ------------------------------------------------------------ the register's view
    def register_implies(self, cid):
        """What the offerings and asset registers, read today, would say for
        `enabled` and `defined` - the rule the 4 September 2026 seed applied.

        Used by `check` to warn when an observation taken from the register
        has drifted from it: an asset released since then makes the recorded
        `partial` stale.  It never overwrites an observation - a human answer
        stands until a human changes it.
        """
        offs = self.offerings_for.get(cid, [])
        ctx = self.enablement_context
        if offs:
            rel = sum(self.release_count(o)[0] for o in offs)
            tot = sum(self.release_count(o)[1] for o in offs)
            enabled = 'yes' if rel == tot and tot else ('partial' if rel else 'no')
        elif cid in ctx.get('realized_by_enterprise_service', {}) \
                or cid in ctx.get('purely_organizational', []):
            enabled = 'n/a'
        else:
            enabled = 'unknown'
        stds = [self.asset_by_id[a] for o in offs for a in o['assets']
                if self.asset_by_id[a]['type'] in ('Standard', 'Reference architecture')]
        if stds:
            rel = [a for a in stds if self.released(a)]
            pre = [a for a in stds if not self.released(a)]
            defined = 'yes' if rel and not pre else ('partial' if rel or pre else 'no')
        else:
            defined = 'unknown'
        return {'enabled': enabled, 'defined': defined}

    # ------------------------------------------------------------ misc
    def owner(self, cid):
        m = self.owner_map.get(cid, {})
        return m.get('unit') or '', m.get('match') or '', m.get('basis') or ''

    def sort_key(self, cid):
        return [int(n) for n in cid.split('.')]

    def capabilities_sorted(self):
        return sorted(self.capabilities, key=lambda c: self.sort_key(c['id']))


def roll_up_values(vals):
    """The ADR-0014 roll-up over a list of criterion values. Pure, so tests can
    exercise the table in the ADR directly."""
    if not vals:
        return 'unknown'
    unexamined = [v for v in vals if v in ('unknown', '')]
    applicable = [v for v in vals if v not in ('unknown', '')]
    if not applicable:
        return 'unknown'          # nobody has looked at any of them
    if all(v == 'n/a' for v in applicable):
        # every criterion that was examined is n/a; if some were never
        # looked at, that is not yet a settled 'n/a' for the capability
        return 'n/a' if not unexamined else 'unknown'
    rated = [v for v in applicable if v != 'n/a']
    if all(v == 'yes' for v in rated) and not unexamined:
        return 'yes'
    if any(v == 'yes' for v in rated) or any(v == 'partial' for v in rated):
        return 'partial'
    return 'no'


# ================================================================== scales
_SCALES = None


def load_scales(refresh=False):
    """Every scale in scales/, discovered by listing the directory.

    Cached: builders call this many times per run, and re-importing would give
    each caller a different module object for the same scale, which breaks
    identity comparisons such as `s is default`.
    """
    global _SCALES
    if _SCALES is not None and not refresh:
        return list(_SCALES)
    out = []
    for fn in sorted(os.listdir(SCALES)):
        if not fn.endswith('.py') or fn.startswith('_'):
            continue
        path = os.path.join(SCALES, fn)
        spec = importlib.util.spec_from_file_location('scale_' + fn[:-3], path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.FILE = fn
        if hasattr(mod, 'level') and hasattr(mod, 'LEVELS'):
            out.append(mod)
    _SCALES = out
    return list(out)


def default_scale():
    """The scale that declares `DEFAULT = True`. Exactly one must."""
    found = [s for s in load_scales() if getattr(s, 'DEFAULT', False)]
    if len(found) != 1:
        raise RuntimeError('exactly one scale in scales/ must set DEFAULT = True; '
                           'found %d' % len(found))
    return found[0]


OBS_VALUES = ('yes', 'partial', 'no', 'n/a', 'unknown')


def validate_scale(s):
    """Problems with one scale module against the contract in scales/README.md.

    Also runs `level()` over every combination of the five values across the
    four observations (625 cases), so a scale that crashes or returns a level
    it does not define is caught by `check` rather than halfway through a
    build.  Returns a list of strings; empty means the scale is sound.
    """
    p = []
    name = getattr(s, 'FILE', getattr(s, '__name__', '?'))
    for attr in ('NAME', 'SHORT', 'BASIS'):
        v = getattr(s, attr, None)
        if not isinstance(v, str) or not v.strip():
            p.append('%s: %s must be a non-empty string' % (name, attr))
    short = getattr(s, 'SHORT', '')
    if isinstance(short, str) and not re.fullmatch(r'[a-z0-9][a-z0-9_-]*', short or ''):
        p.append('%s: SHORT %r must be lowercase letters, digits, _ or - '
                 '(it names the output file)' % (name, short))
    levels = getattr(s, 'LEVELS', None)
    nums = []
    if not isinstance(levels, (list, tuple)) or not levels:
        p.append('%s: LEVELS must be a non-empty list of (number, name, meaning)' % name)
    else:
        for row in levels:
            if (not isinstance(row, (list, tuple)) or len(row) != 3
                    or not isinstance(row[0], int) or not isinstance(row[1], str)
                    or not isinstance(row[2], str)):
                p.append('%s: LEVELS row %r is not (int, str, str)' % (name, row))
            else:
                nums.append(row[0])
        if len(set(nums)) != len(nums):
            p.append('%s: LEVELS numbers repeat' % name)
        if nums != sorted(nums):
            p.append('%s: LEVELS must be in ascending order' % name)
    cap = getattr(s, 'DERIVABLE_MAX', None)
    if cap is not None and cap not in nums:
        p.append('%s: DERIVABLE_MAX %r is not one of the LEVELS' % (name, cap))
    if not callable(getattr(s, 'level', None)):
        p.append('%s: level(obs) must be callable' % name)
        return p
    if hasattr(s, 'note') and not callable(s.note):
        p.append('%s: note must be callable if present' % name)
    q = getattr(s, 'QUESTION', None)
    if q is not None and not isinstance(q, str):
        p.append('%s: QUESTION must be a string' % name)
    produced = set()
    for combo in itertools.product(OBS_VALUES, repeat=len(OBS_KEYS)):
        obs = dict(zip(OBS_KEYS, combo))
        try:
            r = s.level(obs)
        except Exception as e:                       # noqa: BLE001 - report, don't die
            p.append('%s: level(%r) raised %r' % (name, obs, e))
            break
        if not (isinstance(r, tuple) and len(r) == 2):
            p.append('%s: level(%r) must return (level, why), got %r' % (name, obs, r))
            break
        lv, why = r
        if lv is not None and (not isinstance(lv, int) or lv not in nums):
            p.append('%s: level(%r) returned %r, not one of LEVELS' % (name, obs, lv))
            break
        if not isinstance(why, str) or not why.strip():
            p.append('%s: level(%r) returned an empty reason' % (name, obs))
            break
        produced.add(lv)
    if cap is not None and any(x is not None and x > cap for x in produced):
        p.append('%s: level() produced a level above DERIVABLE_MAX %d' % (name, cap))
    if None not in produced:
        p.append('%s: level() never returns None - a scale must be able to say '
                 '"not rated" when nothing has been observed' % name)
    return p


def validate_scales(scales=None):
    """Contract problems across all scales, including uniqueness and the
    single-default rule."""
    scales = scales if scales is not None else load_scales()
    p = []
    for s in scales:
        p.extend(validate_scale(s))
    shorts = [getattr(s, 'SHORT', '') for s in scales]
    for sh in set(shorts):
        if shorts.count(sh) > 1:
            p.append('two scales share SHORT=%r' % sh)
    defaults = [getattr(s, 'FILE', '?') for s in scales if getattr(s, 'DEFAULT', False)]
    if len(defaults) != 1:
        p.append('exactly one scale must set DEFAULT = True; found %s'
                 % (defaults or 'none'))
    return p

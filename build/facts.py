# -*- coding: utf-8 -*-
"""Load the facts and apply a scale. The only module that reads facts/."""
import json, os, importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FACTS = os.path.join(ROOT, 'facts')
SCALES = os.path.join(ROOT, 'scales')


def _load(name):
    with open(os.path.join(FACTS, name), encoding='utf-8') as f:
        return json.load(f)


class Model(object):
    """Every fact in the repository, joined and ready to read."""

    def __init__(self):
        c = _load('capabilities.json')
        self.domains = c['domains']
        self.capabilities = c['capabilities']
        self.by_id = {x['id']: x for x in self.capabilities}
        self.domain_by_id = {d['id']: d for d in self.domains}

        o = _load('offerings.json')
        self.offerings = o['offerings']
        self.generic_assets = o['generic_assets']
        self.consumption_models = o['consumption_models']

        self.assets = _load('assets.json')['assets']
        self.asset_by_id = {a['id']: a for a in self.assets}

        w = _load('owners.json')
        self.units = w['units']
        self.owner_map = {m['capability']: m for m in w['mapping']}
        self.owners_source = w

        b = _load('observations.json')
        self.observation_types = b['observation_types']
        self.observation_values = b['values']
        self.observations = b['observations']

        # Which observations are recorded per L3 criterion rather than per
        # capability.  Today that is `practised` alone (ADR-0014).
        self.criterion_types = [t['id'] for t in self.observation_types
                                if t.get('recorded_at') == 'criterion']

        # capability -> {observation type: row}, for capability-level types only
        self.obs_by_cap = {}
        # capability -> {observation type: {criterion id: row}}
        self.obs_by_crit = {}
        for r in self.observations:
            if r.get('criterion'):
                (self.obs_by_crit.setdefault(r['capability'], {})
                     .setdefault(r['observation'], {})[r['criterion']]) = r
            else:
                self.obs_by_cap.setdefault(r['capability'], {})[r['observation']] = r

        # capability -> offerings enabling it
        self.offerings_for = {}
        for off in self.offerings:
            for cid in off['enables']:
                self.offerings_for.setdefault(cid, []).append(off)

    def criteria_obs(self, cid, otype):
        """[(criterion, row)] in taxonomy order for one capability."""
        rows = self.obs_by_crit.get(cid, {}).get(otype, {})
        return [(x, rows.get(x['id'], {}))
                for x in self.by_id.get(cid, {}).get('criteria', [])]

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
                out[t['id']] = self.obs_by_cap.get(cid, {}).get(
                    t['id'], {}).get('value', 'unknown')
        return out

    def rate(self, scale, cid):
        return scale.level(self.values(cid))

    def rate_all(self, scale):
        return {c['id']: self.rate(scale, c['id']) for c in self.capabilities}

    def owner(self, cid):
        m = self.owner_map.get(cid, {})
        return m.get('unit') or '', m.get('match') or '', m.get('basis') or ''

    def sort_key(self, cid):
        return [int(n) for n in cid.split('.')]


def load_scales():
    """Every scale in scales/, discovered by listing the directory."""
    out = []
    for fn in sorted(os.listdir(SCALES)):
        if not fn.endswith('.py') or fn.startswith('_'):
            continue
        path = os.path.join(SCALES, fn)
        spec = importlib.util.spec_from_file_location('scale_' + fn[:-3], path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if hasattr(mod, 'level') and hasattr(mod, 'LEVELS'):
            out.append(mod)
    return out


def default_scale():
    for s in load_scales():
        if getattr(s, 'SHORT', '') == 'level':
            return s
    raise RuntimeError('default scale (SHORT="level") not found in scales/')

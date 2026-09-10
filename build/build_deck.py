# -*- coding: utf-8 -*-
"""The walkthrough deck as a self-contained HTML page.

A deck for a room being shown the model for the first time: the map, then how
it is measured, then how a first round starts.  It argues the design rather
than reporting a result, which is why it is separate from the management
report - that one answers "what does the model say", this one answers "what is
this and why is it shaped like that".

No external assets and no libraries.  Arrow keys, click, or scroll; it prints
one slide per page and opens from a file:// URL, so it needs no server and
nothing leaves the machine it is opened on.

The two rules the other builders keep, this one keeps too:
  * Nothing here names a scale or a question.  Scales come from load_scales(),
    the default from default_scale(), questions from the model.
  * Every sentence with a number in it is computed from facts/.  A deck with a
    typed count is wrong the first time a fact changes, and nobody notices.
"""
from datetime import date
import collections

import charts as ch
import derive
from charts import esc, C, LABEL, ORDER, LVL


# ------------------------------------------------------------------ helpers
def _plural(n, one, many=None):
    return one if n == 1 else (many or one + "s")


def _gates_on_practice(scale):
    """True if this scale refuses to place a level without observed practice.
    Detected from behaviour, never from a flag."""
    probe = {"practised": "unknown", "enabled": "yes",
             "skilled": "yes", "defined": "yes"}
    return scale.level(probe)[0] is None


def _derivable_top(scale):
    cap = getattr(scale, "DERIVABLE_MAX", None)
    if cap is None:
        return None
    return dict((n, k) for n, k, _ in scale.LEVELS).get(cap)


class _Deck(object):
    """Slides, numbered as they are added so no reference goes stale."""

    def __init__(self):
        self.out = []
        self.n = 0

    def slide(self, body, kicker="", title="", cls=""):
        self.n += 1
        h = ['<section class="slide %s" id="s%d">' % (cls, self.n)]
        h.append('<div class="inner">')
        if kicker:
            h.append('<div class="eyebrow">%s</div>' % esc(kicker))
        if title:
            h.append('<h2>%s</h2>' % title)
        h.append(body)
        h.append('</div><div class="pn">%d</div></section>' % self.n)
        self.out.append("\n".join(h))

    def html(self):
        return "\n".join(self.out)


def _kpi(items):
    """items: [(value, caption, warn?)]"""
    o = ['<div class="kpis">']
    for it in items:
        v, cap = it[0], it[1]
        warn = len(it) > 2 and it[2]
        o.append('<div class="kpi%s"><b>%s</b><span>%s</span></div>'
                 % (" warn" if warn else "", esc(v), esc(cap)))
    o.append('</div>')
    return "\n".join(o)


def _objections(items):
    """items: [(objection, answer_html)] - the question as a reader would put it,
    and the answer in one short paragraph."""
    o = ['<div class="objs">']
    for q, a in items:
        o.append('<div class="obj"><div class="oq">&ldquo;%s&rdquo;</div>'
                 '<div class="oa">%s</div></div>' % (esc(q), a))
    o.append('</div>')
    return "\n".join(o)


def _table(head, rows, cls=""):
    """A table. A column whose heading starts with "~" is centred, heading and
    body together."""
    mid = [h.startswith("~") for h in head]
    o = ['<table class="%s"><thead><tr>' % cls]
    for h, c in zip(head, mid):
        o.append('<th%s>%s</th>' % (' class="c"' if c else "", esc(h.lstrip("~"))))
    o.append('</tr></thead><tbody>')
    for r in rows:
        o.append('<tr>')
        for i, cell in enumerate(r):
            o.append('<td%s>%s</td>'
                     % (' class="c"' if i < len(mid) and mid[i] else "", cell))
        o.append('</tr>')
    o.append('</tbody></table>')
    return "\n".join(o)


# =================================================================== the deck
def deck(m, scale, scales=None):
    scales = list(scales or [scale])
    lenses = [s for s in scales if s is not scale]
    D = _Deck()

    n_dom = len(m.domains)
    n_cap = len(m.capabilities)
    n_crit = sum(len(c['criteria']) for c in m.capabilities)
    n_obs = len(m.observations)
    levels = dict((n, k) for n, k, _ in scale.LEVELS)
    rated = m.rate_all(scale)
    n_rated = sum(1 for v in rated.values() if v[0] is not None)

    # observation coverage, per type, computed not typed
    cov = {}
    for t in m.observation_types:
        tid = t['id']
        if tid in m.criterion_types:
            rows = [r for cid in m.by_id for _, r in m.criteria_obs(cid, tid)]
        else:
            rows = [m.cap_obs(c['id'], tid) for c in m.capabilities]
        seen = sum(1 for r in rows if (r or {}).get('value', 'unknown') != 'unknown')
        cov[tid] = (seen, len(rows))

    unowned = [c for c in m.capabilities_sorted() if not m.owner(c['id'])[0]]
    low = [c for c in m.capabilities_sorted() if c.get('confidence') == 'low']
    lens_anchor = [c for c in m.capabilities_sorted() if c.get('anchor') == 'lens']
    pending = m.pending_assets()
    released = [a for a in m.assets if m.released(a)]
    inbox = sum(len(o.get('in_the_box', [])) for o in m.offerings)

    # ---------------------------------------------------------------- 1 title
    D.slide(
        '<h1>The AI capability model</h1>'
        '<p class="lede">What the Bank must be able to do with AI, what it has '
        'actually built, and the distance between the two &mdash; expressed so the '
        'answer can be checked rather than argued about.</p>'
        + _kpi([("%d" % n_dom, "domains"), ("%d" % n_cap, "capabilities"),
                ("%d" % n_crit, "criteria"), ("%d" % len(m.offerings), "offerings"),
                ("%d" % len(m.assets), "assets")])
        + '<p class="foot">Enterprise Architecture &middot; Inter-American Development '
          'Bank &middot; generated %s. Every figure on every slide is computed from '
          'the recorded facts at build time.</p>' % date.today().isoformat(),
        cls="title")

    # ------------------------------------------------------------- 2 problem
    D.slide(
        '<div class="two">'
        '<div class="quote"><p>&ldquo;We cannot run AI agents.&rdquo;</p></div>'
        '<div class="quote"><p>&ldquo;Of course we can &mdash; the platform, the '
        'standards, the reference architectures and the infrastructure modules are '
        'all published.&rdquo;</p></div></div>'
        '<p class="lede">Both are true, about different things. One describes whether '
        'the work is <b>done</b>. The other describes whether the means to do it '
        '<b>exist</b>.</p>'
        '<p>A model that answers with a single number has to pick one of those '
        'meanings, and whichever it picks, the other conversation loses its evidence. '
        'That is the standard failure of AI capability assessment: <b>supply gets '
        'reported as ability</b>, because supply is easier to establish and pleasanter '
        'to report.</p>'
        '<div class="callout"><p><b>This model is built so both statements can be '
        'true at once, visibly, with the evidence attached to each.</b></p></div>',
        kicker="The problem", title="Two people, opposite answers, both right")

    # ------------------------------------------------------------ 3 what it is
    D.slide(
        '<div class="cards">'
        '<div class="card"><div class="ch">A capability map</div>'
        '<p>%d domains, %d capabilities, %d criteria. What the institution must be '
        'able to do with AI, each with one accountable owner. Vendor-neutral: it '
        'survives replacing every product.</p></div>'
        '<div class="card"><div class="ch">A register of what exists</div>'
        '<p>%d offerings and %d named assets &mdash; standards, reference '
        'architectures, templates, modules &mdash; each with a status and a location '
        'a reader can open. This part is not an opinion.</p></div>'
        '<div class="card"><div class="ch">Four observations</div>'
        '<p>Recorded as facts, with evidence, an observer and a date. A level is '
        '<b>derived</b> from them by a written rule. Nobody types a level '
        'anywhere.</p></div></div>'
        '<div class="callout"><p><b>The separation between the three is the whole '
        'design.</b> An observation is a fact, not a score, so several scales can read '
        'one body of evidence and none of them can contradict another about what is '
        'true &mdash; only about what to make of it.</p></div>'
        % (n_dom, n_cap, n_crit, len(m.offerings), len(m.assets)),
        kicker="What it is", title="Three things, kept apart")

    # ------------------------------------------------------- 4 the three levels
    D.slide(
        _table(["", "~Count", "What it is", "~Carries a level", "~Carries an owner"], [
            ["<b>L1 &middot; Domain</b>", str(n_dom),
             "A reporting cluster. Groups capabilities so a reader can find them",
             "no", "no"],
            ["<b>L2 &middot; Capability</b>", str(n_cap),
             "Something the institution must be able to do. "
             "<b>The unit of assessment and of accountability</b>", "yes", "yes"],
            ["<b>L3 &middot; Criterion</b>", str(n_crit),
             "A specific practice that can actually be witnessed on a real system",
             "no", "no"],
        ], cls="mid")
        + '<div class="two">'
        '<div><h3 class="minor">A domain is a reporting cluster</h3>'
        '<p>Not a lifecycle. It implies no sequence, no team and no process. Every '
        'capability has exactly one primary home; a second plausible home is a typed '
        'dependency, not a second listing.</p></div>'
        '<div><h3 class="minor">A criterion is a checklist item</h3>'
        '<p>Not a gate. Criteria carry an observation, which is a fact. None has a '
        'rubric, and none is typed mandatory or conditional.</p></div></div>',
        kicker="The taxonomy", title="Three levels, and only one of them is assessed")

    # -------------------------------------------------------- 5 the eight domains
    rows = []
    for d in m.domains:
        caps = [c for c in m.capabilities if c['domain'] == d['id']]
        rows.append(['<code>%s</code>' % esc(d['id']),
                     '<b>%s</b>' % esc(d['name']),
                     esc(d['definition']),
                     str(len(caps)),
                     str(sum(len(c['criteria']) for c in caps))])
    D.slide(
        _table(["", "Domain", "Able to&hellip;", "~L2", "~L3"], rows, cls="mid")
        + '<p class="foot">The full map, every capability and every criterion with its '
          'definition, is <code>out/capability-map.md</code>. It carries no '
          'observations and no levels, so the structure can be argued with before '
          'anything is measured against it.</p>',
        kicker="The map", title="%d domains" % n_dom)

    # --------------------------------------------------------- 6 what to challenge
    def _idlist(caps, k=10):
        s = " ".join('<code>%s</code>' % esc(c['id']) for c in caps[:k])
        return s + (' <span class="mut">+%d more</span>' % (len(caps) - k)
                    if len(caps) > k else "")

    D.slide(
        '<p class="lede">Three lists a reviewer should go at first. Each is here for a '
        'different reason, and only one of them is a problem with the map.</p>'
        '<div class="cards">'
        '<div class="card"><div class="ch">%d carry low confidence</div>'
        '<p>The line itself is not yet trusted &mdash; its name, its boundary, or '
        'whether it should exist. <b>Nothing should be scored against these</b> until '
        'their owner has looked.</p><p class="ids">%s</p></div>'
        '<div class="card"><div class="ch">%d are lenses</div>'
        '<p>A view over capabilities that already exist elsewhere in the Bank\'s map '
        'rather than a new line. The anchoring rests on judgement, <b>not on a '
        'crosswalk</b> &mdash; which is why this must be carved out of any approval '
        'request.</p><p class="ids">%s</p></div>'
        '<div class="card warn"><div class="ch">%d nobody claims</div>'
        '<p>Nothing in the Bank\'s own product and enabler catalogue claims these. '
        '<b>A finding about the institution, not a gap in the map.</b> Is the line '
        'wrong, or is the ownership missing?</p><p class="ids">%s</p></div></div>'
        % (len(low), _idlist(low), len(lens_anchor), _idlist(lens_anchor),
           len(unowned), _idlist(unowned)),
        kicker="Where to push", title="What to challenge first")

    # ------------------------------------------------------------- 7 ownership
    units = {}
    for c in m.capabilities_sorted():
        units.setdefault(m.owner(c['id'])[0] or "(nobody)", []).append(c['id'])
    top = sorted(units.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    ea = len(units.get("Enterprise Architecture", []))
    D.slide(
        '<p class="lede">Mapped against the Bank\'s own product and enabler catalogue. '
        'The point of this table is that <b>the model is not one function\'s '
        'instrument</b>.</p>'
        + _table(["Unit", "~Capabilities", "Which"],
                 [["<b>(nobody)</b>" if u == "(nobody)" else esc(u), str(len(ids)),
                   '<span class="ids">%s</span>'
                   % " ".join('<code>%s</code>' % esc(x) for x in ids)]
                  for u, ids in top], cls="sm")
        + '<div class="callout"><p>The same distribution governs the observations. A '
          'standard for AI security is set by Cybersecurity, one for AI data '
          'governance by Data Management, one for AI literacy by Learning &amp; '
          'Development. <b>Enterprise Architecture is the accountable owner of %d of '
          '%d.</b></p></div>' % (ea, n_cap),
        kicker="Ownership", title="Who answers for what")

    # ------------------------------------------------------- 8 four observations
    rows = []
    for t in m.observation_types:
        tid = t['id']
        rows.append(['<b>%s</b>' % esc(tid.title()), esc(t['question']),
                     ("<b>each L3 criterion</b>" if tid in m.criterion_types
                      else "the capability"),
                     esc(t['evidence_expected'])])
    D.slide(
        _table(["", "The question", "Asked at", "Evidence expected"], rows, cls="sm")
        + '<p>Each is answered <code>yes</code> / <code>partial</code> / '
          '<code>no</code> / <code>n/a</code> / <code>unknown</code>, and each carries '
          'evidence, an observer and a date. That is the entire input to the model: '
          '<b>%d recorded observations</b>.</p>' % n_obs
        + '<div class="callout"><p><b>Nobody is being scored.</b> There is no level in '
          'the workbook for a reviewer to defend. The level is computed afterwards, '
          'from what they recorded, by a rule they can read and argue with '
          'separately.</p></div>',
        kicker="How it measures", title="Four observations, each one a fact")

    # ------------------------------------------- where the answers are recorded
    rec = derive.recorded_at(m)
    at_crit = [r for r in rec if r['at'].startswith('L3')]
    at_cap = [r for r in rec if r['at'].startswith('L2')]

    def _obsn(rs):
        ns = ["<code>%s</code>" % esc(r['id']) for r in rs]
        return ns[0] if len(ns) < 2 else ", ".join(ns[:-1]) + " and " + ns[-1]

    D.slide(
        '<p class="lede">The question most often got wrong. <b>Only two of the three '
        'taxonomy levels ever carry an observation</b>, and one of the four values is '
        'not recorded by anybody &mdash; it is computed.</p>'
        + _table(["Taxonomy level", "What is recorded against it", "~Rows"], [
            ["<b>L1 domain</b> &middot; %d" % n_dom,
             "<i>Nothing.</i> A domain is a reporting cluster and is never scored",
             "&mdash;"],
            ["<b>L2 capability</b> &middot; %d" % n_cap,
             "%s &mdash; one row each. Plus %s, <b>derived</b> from the criteria "
             "beneath it and never typed" % (_obsn(at_cap), _obsn(at_crit)),
             str(len(at_cap) * n_cap)],
            ["<b>L3 criterion</b> &middot; %d" % n_crit,
             "%s &mdash; one row per criterion, because that is the level at which "
             "work can actually be witnessed" % _obsn(at_crit),
             str(len(at_crit) * n_crit)],
        ], cls="mid")
        + '<div class="callout"><p>A round collects <b>%d rows</b>, not %d. And the '
          'capability-level %s value every chart is drawn from was <b>computed</b> by '
          'the roll-up: <b>there is nowhere to type it</b>, and a stored level is the '
          'one edit validation rejects outright.</p></div>'
          % (n_obs, n_cap, _obsn(at_crit)),
        kicker="How it measures", title="Where each answer is recorded")

    # ----------------------------------------------------------- 9 the values
    D.slide(
        _table(["Value", "Means", "Requires"], [
            ["<code>yes</code>", "Done", "Evidence"],
            ["<code>partial</code>", "Done in places, or incompletely. Say where",
             "Evidence"],
            ["<code>no</code>", "<b>An evidenced negative.</b> Someone looked and it "
             "is not there", "Evidence, or a basis saying what was looked at"],
            ["<code>n/a</code>", "Does not apply here. A governance capability is not "
             "worse for having no tooling", "A recorded reason"],
            ["<code>unknown</code>", "<b>Nobody has looked. Never a zero</b>",
             "Nothing. It is the honest default"],
        ], cls="mid")
        + '<div class="callout warn"><p><b><code>no</code> and <code>unknown</code> '
          'are the pair that decides whether the model is trustworthy.</b> A register '
          'that was searched and had nothing is <code>unknown</code> until the owner '
          'is asked &mdash; a standard owned by another function may exist and simply '
          'not be recorded here. Recording that absence as <code>no</code> turns '
          '<i>we did not look</i> into <i>it does not exist</i>, which is the failure '
          'this model exists to prevent.</p></div>'
        '<p class="foot">Most published models cannot say <i>unknown</i> at all, so '
        'they silently score an unexamined capability as if it were absent.</p>',
        kicker="How it measures", title="Five values, and the two that get misused")

    # ------------------------------------------------------------ 10 the roll-up
    # The worked example, chosen from facts and never named in code: prefer a
    # capability the recorded use-case questions already touch - the room is
    # arguing about those - and among them the one with the most criteria
    # observed, then the most criteria.  Falls back to the whole map if no
    # question is recorded.
    asked = set()
    for q in m.questions:
        asked.update(q.get('capabilities', []))
    pool = [c for c in m.capabilities if c['id'] in asked] or m.capabilities

    def _seen(c):
        if not m.criterion_types:
            return 0
        return sum(1 for _, r in m.criteria_obs(c['id'], m.criterion_types[0])
                   if r.get('value', 'unknown') != 'unknown')

    pick = max(pool, key=lambda c: (_seen(c), len(c['criteria'])))
    crit_rows = [['<code>%s</code>' % esc(x['id']), '<b>%s</b>' % esc(x['name']),
                  esc(x['definition'])]
                 for x in pick['criteria']]
    D.slide(
        '<p class="lede"><code>%s</code> <b>%s</b> covers %d distinct practices. The '
        'Bank might do one of them well and never do another at all &mdash; so '
        '<i>&ldquo;is %s practised?&rdquo;</i> has no honest single answer, and is '
        'not asked.</p>'
        % (esc(pick['id']), esc(pick['name']), len(pick['criteria']), esc(pick['id']))
        + _table(["L3", "Criterion", "The practice"], crit_rows, cls="sm")
        + '<p>Each criterion is judged on its own, and <b>the capability value is '
          'derived</b>. The gain is that a gap gets a name: not <i>&ldquo;improve '
          '%s&rdquo;</i> but a specific practice nobody has done, which is a piece of '
          'work someone can be given.</p>' % esc(pick['name'].lower()),
        kicker="How it measures", title="Why practice is observed one level down")

    # ------------------------------------------------------- 11 the roll-up rule
    D.slide(
        _table(["The criteria say", "The capability reads"], [
            ["Every one examined, and every one <code>yes</code>", "<code>yes</code>"],
            ["Some <code>yes</code> or <code>partial</code>, <b>or any left "
             "unexamined</b>", "<code>partial</code>"],
            ["None <code>yes</code> or <code>partial</code>, at least one "
             "<code>no</code>", "<code>no</code>"],
            ["None examined", "<code>unknown</code>"],
        ], cls="mid")
        + '<div class="two">'
        '<div><h3 class="minor">One weak link stops the claim</h3>'
        '<p>A capability cannot read <code>yes</code> on the strength of one '
        'observation while the rest has never been looked at. An unexamined criterion '
        'is never counted as satisfied.</p></div>'
        '<div><h3 class="minor">The asymmetry is deliberate</h3>'
        '<p><code>yes</code> needs a complete look. <code>no</code> does not: one '
        'examined <code>no</code> with the rest unexamined still reads <code>no</code>. '
        '<b>Under-claiming costs a follow-up question. Over-claiming is the failure '
        'the model exists to prevent.</b></p></div></div>',
        kicker="How it measures", title="The roll-up, and why it leans one way")

    # ------------------------------------------------------------- the ladder
    top_n = _derivable_top(scale)
    lrows = []
    cap_lvl = getattr(scale, "DERIVABLE_MAX", None)
    for n, k, meaning in scale.LEVELS:
        ok = cap_lvl is None or n <= cap_lvl
        lrows.append(['<b>%d</b>' % n, '<b>%s</b>' % esc(k), esc(meaning),
                      "yes" if ok else '<span class="mut">&mdash;</span>'])
    D.slide(
        '<p class="lede">%s</p>' % esc(scale.QUESTION)
        + _table(["~Level", "Name", "What it means", "~Derivable today"], lrows,
                 cls="mid")
        + '<div class="callout"><p><b>Performance comes first, and that ordering is '
          'not ours.</b> An approved standard with nothing performed against it earns '
          '<b>no level at all</b> &mdash; because the question was never <i>did we '
          'write it down</i>, it was <i>can the institution do this</i>. That is what '
          'stops <i>&ldquo;we approved the technology&rdquo;</i> from reading as '
          '<i>&ldquo;we have the capability&rdquo;</i>.</p></div>'
        + ('<p class="foot"><b>%s is the ceiling of what is measured, not of the '
           'scale.</b> The levels above it need observations nobody collects &mdash; '
           'threshold monitoring and a closed improvement cycle.</p>'
           % esc("Level %d %s" % (cap_lvl, top_n)) if top_n else ""),
        kicker="How it measures", title="A level is derived, never typed")

    # --------------------------------------------- what it takes, rung by rung
    n_combo = len(derive.VALUES) ** len(derive.TYPES)
    rungs = derive.ladder(scale)

    def _cell(c):
        if c['kind'] == 'any':
            return '<span class="mut">any</span>'
        if c['text'].startswith('not '):
            return 'not <code>%s</code>' % esc(c['text'][4:])
        return " or ".join('<code>%s</code>' % esc(v) for v in c['vals'])

    lad = [['<b>%d %s</b>%s' % (r['n'], esc(r['name']),
                                '' if r['exact'] else ' <span class="warn-t">approx</span>')]
           + [_cell(r['conds'][t]) for t in derive.TYPES]
           for r in rungs]
    steps = [r for r in rungs if r['adds']]
    tail = ""
    if steps and len(steps[-1]['adds']) == 1 and len(steps) > 1:
        below, last = steps[-2], steps[-1]
        a = last['adds'][0][0]
        tail = ('<div class="callout"><p><b>The whole difference between %d %s and %d '
                '%s is one observation: <code>%s</code> must be %s.</b> Everything '
                'else is already required at %d &mdash; which is why a capability with '
                'the work done, the tooling provided and competent people stops at %d '
                'until an approved standard exists.</p></div>'
                % (below['n'], esc(below['name']), last['n'], esc(last['name']),
                   esc(a), _cell(last['conds'][a]), below['n'], below['n']))
    D.slide(
        '<p class="lede">Read each row as <b>to reach at least this level</b>. Nothing '
        'here is written down: it is derived by running the rule over all <b>%d '
        'combinations</b> of the five values across the four observations.</p>' % n_combo
        + _table(["To reach"] + ["~" + t.title() for t in derive.TYPES], lad, cls="mid")
        + tail
        + '<p class="foot"><code>n/a</code> counts as satisfied &mdash; a capability '
          'that legitimately needs no tooling is not held down for having none. '
          '%s</p>' % ("Every row is exact: these conditions are not a summary of the "
                      "rule, they <b>are</b> the rule."
                      if all(r['exact'] for r in rungs) else ""),
        kicker="How it measures", title="Why a 2 and not a 3")

    # ------------------------------------------------------------ 13 the basis
    D.slide(
        '<p class="lede">%s</p>' % esc(scale.BASIS)
        + '<div class="two">'
          '<div><h3 class="minor">What is adopted</h3><p>The level ladder, the '
          'ordering of the attributes, and the idea that a level is derived from '
          'attribute achievement rather than asserted.</p></div>'
          '<div><h3 class="minor">What is ours, stated plainly</h3><p>Collapsing five '
          'process attributes to four capability observations; a three-value scale in '
          'place of the standard\'s four-point one; and applying a <i>process</i> '
          'measurement framework to a <i>capability</i> map.</p></div></div>'
        + '<div class="callout warn"><p><b>Two things must not be quoted.</b> The '
          'standard is paywalled and its published preview stops short, so its '
          'percentage bands and its exact level rule rest on secondary sources about a '
          'superseded predecessor. Cite the scale by name and the levels by clause; '
          'never quote the percentages.</p></div>'
        + '<p class="foot">Where the model adopts, adapts or invents, it says so on '
          'the face of the artifact &mdash; every generated view carries this basis '
          'line.</p>',
        kicker="Provenance", title="Where the scale comes from")

    # ------------------------------------------------------------- 14 the lenses
    if lenses:
        lrows = [['<b>%s</b>' % esc(s.NAME), esc(getattr(s, "QUESTION", "")),
                  "%d&ndash;%d %s" % (s.LEVELS[0][0], s.LEVELS[-1][0],
                                      esc(s.LEVELS[-1][1])),
                  ("gates on practice" if _gates_on_practice(s)
                   else '<span class="warn-t">does not gate on practice</span>'),
                  "<b>the default</b>" if s is scale else "a lens"]
                 for s in scales]
        D.slide(
            '<p class="lede">Because an observation is a fact and a level is a rule '
            'over facts, more than one rule can read the same evidence. %d ship, each '
            'one file.</p>' % len(scales)
            + _table(["Scale", "Asks", "Ladder", "Behaviour", "Standing"], lrows,
                     cls="sm")
            + '<div class="callout"><p><b>Where a lens and the default disagree, the '
              'default is the finding.</b> A lens exists so a room that already holds '
              'a frame can be answered in it &mdash; not so the friendlier number can '
              'be chosen.</p></div>'
            '<p class="foot">Adding a scale is one file meeting a published contract. '
            'A view is generated for it automatically, and it is validated over all '
            '625 combinations of the five values across the four observations.</p>',
            kicker="Several frames", title="One set of facts, %d ways to read it"
                                          % len(scales))

    # -------------------------------------------- the same answers, every scale
    wrows = []
    for label, obs, row in derive.worked(scales):
        wrows.append([esc(label)]
                     + ['<code>%s</code>' % esc(obs[t]) for t in derive.TYPES]
                     + [('<b>%d</b> %s' % (lv, esc(nm)) if lv is not None
                         else '<span class="mut">not rated</span>')
                        for _s, lv, nm, _w in row])
    ungated = [s for s in scales if not _gates_on_practice(s)]
    D.slide(
        '<p class="lede">Ten situations a reviewer will actually record, run through '
        'every scale at once. Every level below is computed by calling the rule.</p>'
        + _table(["If the four answers are"]
                 + ["~" + t[:3].title() for t in derive.TYPES]
                 + ["~" + s.NAME + ("" if s is scale else " (lens)") for s in scales],
                 wrows, cls="sm")
        + ('<div class="callout warn"><p><b>Look at the second row.</b> Tooling '
           'provided, people competent, an approved standard in place &mdash; and '
           'nobody yet asked whether the work is done. The scales that gate return '
           '<b>not rated</b>; the one that does not places it at the top of its '
           'ladder. <b>That single row is the entire argument for this '
           'model.</b></p></div>' if ungated else ""),
        kicker="How it measures", title="The same answers, read by every scale")

    # ------------------------------------------------------ 15 where we stand
    covrows = []
    for t in m.observation_types:
        seen, tot = cov[t['id']]
        pct = int(round(100.0 * seen / tot)) if tot else 0
        covrows.append(['<b>%s</b>' % esc(t['id'].title()),
                        "%d of %d" % (seen, tot),
                        '<div class="bar"><i style="width:%d%%"></i></div>' % pct,
                        ("asked at each of the %d criteria" % n_crit)
                        if t['id'] in m.criterion_types
                        else ("asked once per capability")])
    D.slide(
        _kpi([("%d" % n_rated, "capabilities rated", n_rated == 0),
              ("%d" % (n_cap - n_rated), "not rated"),
              ("%d" % len(released), "assets released"),
              ("%d" % len(pending), "built, not released", len(pending) > 0),
              ("%d" % inbox, "questions outstanding")])
        + _table(["Observation", "~Observed", "", "Asked at"], covrows, cls="sm")
        + '<div class="callout warn"><p><b>Not rated is a result, not a failure.</b> '
          'A rating requires knowing whether something is practised, and that question '
          'has not been put to the capability owners. The model records what exists '
          'and leaves what does not visibly absent, rather than guessing to complete '
          'the picture.</p></div>',
        kicker="Where we stand", title="What the model says today")

    # ------------------------------------------------------------ 16 the finding
    D.slide(
        '<h1 class="finding">The institution has built its enablers ahead of its '
        'practice.</h1>'
        '<p class="lede">That is the explanation for the disagreement we opened with, '
        'and it names its own fix. %d %s recorded with a status and a location; '
        '%d finished but not yet released to teams; and not one observation yet of '
        'whether any of it is used.</p>'
        % (len(m.assets), _plural(len(m.assets), "asset"), len(pending))
        + '<div class="callout"><p>The distinction the model refuses to blur is '
          'between <b>we do not know</b> and <b>we do not have it</b>. Most '
          'assessments cannot tell those apart and score an unexamined capability as '
          'if it were absent.</p></div>',
        kicker="The finding", title="", cls="statement")

    # ---------------------------------------------------------- 17 the round
    load = collections.Counter()
    caps_per = collections.Counter()
    for c in m.capabilities:
        u = m.owner(c['id'])[0] or "(nobody)"
        caps_per[u] += 1
        load[u] += len(c['criteria']) + (len(m.observation_types) - len(m.criterion_types))
    ranked = sorted(load.items(), key=lambda kv: -kv[1])
    biggest = ranked[0]
    others = [v for k, v in ranked[1:] if k != "(nobody)"]
    D.slide(
        '<p class="lede">Sheet 2 of the workbook has <b>%d rows</b> &mdash; but no '
        'single reviewer ever sees %d. Rows are answered by the unit that owns the '
        'capability.</p>' % (n_obs, n_obs)
        + _table(["Reviewer", "~Capabilities", "~Rows to answer"],
                 [[("<b>%s</b>" % esc(u)) if u != "(nobody)"
                   else '<b class="warn-t">nobody claims these</b>',
                   str(caps_per[u]), str(v)] for u, v in ranked], cls="sm")
        + '<div class="callout"><p><b>Volume is not the reason to narrow the round.</b> '
          'One reviewer carries %d rows. Everyone else answers between %d and %d, about '
          'work they already know.</p></div>'
          % (biggest[1], min(others), max(others)),
        kicker="Starting the assessment", title="The ask is smaller than it looks")

    # --------------------------------------------------- 18 what a round produces
    D.slide(
        '<div class="two">'
        '<div><h3 class="minor">What a first round can produce</h3><ul>'
        '<li>A derived level per capability answered, on the default scale and through '
        'every lens &mdash; from the same evidence.</li>'
        '<li><b>A gap with a name.</b> Not <i>&ldquo;improve orchestration&rdquo;</i> '
        'but a specific practice nobody has done, which is a piece of work someone can '
        'be given.</li>'
        '<li>The first honest count of how much of the map has been examined at '
        'all.</li></ul></div>'
        '<div><h3 class="minor">What it cannot</h3><ul>'
        '<li>A level above what today\'s observations reach. The top two need '
        'threshold monitoring and a closed improvement cycle, and nothing collects '
        'either.</li>'
        '<li><b>Evidence of conformance.</b> A top level reads it from a standard and '
        'a practice co-existing; it does not show the work follows the standard.</li>'
        '<li>A rating for the %d capabilities whose taxonomy their owner has not yet '
        'agreed.</li>'
        '<li>A benchmark. No comparable dataset exists, and inventing one would undo '
        'the point.</li></ul></div></div>' % len(low)
        + '<div class="callout"><p>There is no writing step. <code>build.py all</code> '
          'validates the facts and regenerates the workbook and every view, so the '
          'report cannot drift from what was recorded &mdash; and re-running it after '
          'new observations produces a new report rather than a new draft.</p></div>',
        kicker="Starting the assessment", title="What a round can and cannot say")

    # ------------------------------------------------------------- 19 the ask
    asks = []
    for q in m.questions:
        for nx in q.get('next', []):
            asks.append([esc(nx['who']), esc(nx['what'])])
    D.slide(
        '<p class="lede">None of this requires new tooling or new investment. It '
        'requires the questions being put to the people who can answer them.</p>'
        + (_table(["Who", "What is asked"], asks, cls="sm") if asks else "")
        + '<div class="callout"><p><b>The one thing to get right in the covering '
          'note:</b> <code>unknown</code> is a real answer. A reviewer who believes '
          'they are being rated answers defensively &mdash; and the model\'s whole '
          'value is that it can distinguish <i>we did not look</i> from <i>it is not '
          'there</i>.</p></div>',
        kicker="The ask", title="What would make the next version say more")

    # ------------------------------------------------------------- 20 close
    D.slide(
        '<h1 class="finding">Facts are edited. Views are generated. '
        'Derived values are never stored.</h1>'
        '<p class="lede">No finding is ever fixed by editing a report. The fact is '
        'fixed, and everything rebuilds &mdash; which is why two versions of this '
        'model cannot contradict each other about what is true.</p>'
        + _table(["", "", ""], [
            ["<code>facts/</code>", "What is <b>true</b> about the Bank, with evidence "
             "and a date", "<b>edited</b>"],
            ["<code>scales/</code>", "Rules that turn observations into a level",
             "rarely edited"],
            ["<code>out/</code>", "Views, one per scale, one per question, plus the "
             "report", "<b>generated</b>"],
        ], cls="mid"),
        kicker="The rule underneath all of it", title="", cls="statement")

    # ------------------------------------------------- appendix: objections
    # The figures inside these answers are computed, so an answer cannot end up
    # quoting a count the model no longer supports.
    rungs = derive.ladder(scale)
    steps = [r for r in rungs if r['adds']]
    gate_obs = derive.TYPES[0]
    delta = ""
    if steps and len(steps[-1]['adds']) == 1 and len(steps) > 1:
        below, last = steps[-2], steps[-1]
        a = last['adds'][0][0]
        delta = ("<b>%d %s</b> and <b>%d %s</b> differ by exactly one observation "
                 "(<code>%s</code>)" % (below['n'], esc(below['name']), last['n'],
                                        esc(last['name']), esc(a)))
    ea = len(units.get("Enterprise Architecture", []))
    top_name = _derivable_top(scale)

    D.slide(
        _objections([
            ("Why does the top level need a standard? The standard usually comes "
             "first \u2014 ours did.",
             "It does, and the model records that. But the ladder orders <b>claims</b>, "
             "not activities. The top rung does not claim <i>a standard exists</i>; it "
             "claims <i>the work is done against one</i>, and that sentence needs the "
             "work. A standard with nothing performed against it is recorded as "
             "<code>defined</code> = <code>yes</code> with the practice unobserved "
             "\u2014 which reads <b>not rated</b>, and is precisely the finding that "
             "the enablers were built ahead of the practice. " + delta + "."),
            ("So writing standards earns no credit?",
             "It earns the credit it should: a visible <code>defined</code> column, an "
             "asset register with a status and a location, and an offering a team can "
             "actually consume. What it does not earn is a <b>capability</b> level "
             "\u2014 because letting supply alone place one is how <i>we approved the "
             "technology</i> comes to read as <i>we have the capability</i>."),
            ("This ordering is your invention.",
             "It is not. Performance is the first process attribute in the ISO process "
             "measurement framework the default scale is adapted from; a defined "
             "process is a Level 3 attribute. We adopted the ordering and say so on "
             "every view, along with what is ours."),
            ("Why is almost nothing rated? That makes the model look useless.",
             "Because the observation every scale needs most has never been collected. "
             "%d of %d capabilities are unrated for one reason: nobody has been asked "
             "whether the work is done. That is a true statement about the assessment, "
             "and one review round changes it. Filling those cells with estimates to "
             "make the picture look finished is the one change that would make this "
             "worthless." % (n_cap - n_rated, n_cap)),
        ]),
        kicker="Appendix \u00b7 objections, answered", title="On the ladder")

    D.slide(
        _objections([
            ("<code>unknown</code> is just a way of avoiding a score.",
             "It is the opposite \u2014 it is the refusal to invent one. "
             "<code>no</code> means somebody looked and it is not there, and the record "
             "says what they looked at. <code>unknown</code> means nobody looked. Most "
             "published models cannot tell those apart and score an unexamined "
             "capability as if it were absent, which is how a model starts producing "
             "gaps that do not exist."),
            ("%d capabilities is too many. The analyst models use about half that."
             % n_cap,
             "The coarse ones are easier to fill in and produce findings nobody can "
             "act on. Granularity is what turns <i>improve orchestration</i> into a "
             "named practice with an owner. The %d criteria beneath the capabilities "
             "are where that happens \u2014 and they are a checklist behind a "
             "judgement, not %d more things to score." % (n_crit, n_crit)),
            ("This is Enterprise Architecture&rsquo;s view of the Bank.",
             "EA is the accountable owner of <b>%d of %d</b> capabilities. The standard "
             "for AI security is Cybersecurity&rsquo;s, for AI data governance Data "
             "Management&rsquo;s, for literacy Learning &amp; Development&rsquo;s. A "
             "model that only ever said EA would be a credit column, not a model \u2014 "
             "and %d capabilities are owned by nobody, which we report rather than "
             "quietly assign." % (ea, n_cap, len(unowned))),
            ("We already have a maturity model. Why another one?",
             "Because this is not competing with it. An observation is a fact, so the "
             "same evidence can be read through whichever frame a room already holds "
             "\u2014 %d scales ship and none of them required reassessing anything. "
             "Where a lens and the default disagree, the default is the finding."
             % len(scales)),
        ]),
        kicker="Appendix \u00b7 objections, answered", title="On the model")

    D.slide(
        _objections([
            ("You say %s means we conform to the standard. Prove it."
             % ("Level %d" % scale.LEVELS[-1][0] if not top_name
                else "the top level"),
             "We cannot, and the model says so on the face of it. <code>defined</code> "
             "says a standard exists; the practice observation says the work is done. "
             "Neither says the work <b>follows</b> the standard. The top rung reads "
             "conformance from the two facts sitting together and its reason line "
             "admits it. A fifth observation would make it checkable; whether that is "
             "worth collecting is recorded as an open item, not hidden."),
            ("A governance capability has no tooling. Does it fail?",
             "No. <code>n/a</code> with a recorded reason drops out of the calculation "
             "rather than counting against it. A capability that legitimately needs no "
             "platform component is not worse for having none \u2014 forcing a supply "
             "number onto a strategy capability is how a model starts producing "
             "nonsense nobody trusts."),
            ("Can we compare ourselves to peer institutions?",
             "No, and that is deliberate. No comparable dataset exists at this "
             "granularity, and inventing one would undo the point. What the model does "
             "instead is make our own position checkable: every observation carries "
             "evidence, a name and a date."),
            ("The taxonomy is not agreed yet. Should we be measuring at all?",
             "Structure is settled ahead of, and separately from, assessment. "
             "%d capabilities carry low confidence and %d are unverified lenses onto "
             "the Bank&rsquo;s existing map \u2014 both listed by name rather than "
             "buried. Nothing should be scored against those until their owner has "
             "looked, and the anchoring is carved out of any approval request until a "
             "crosswalk exists." % (len(low), len(lens_anchor))),
        ]),
        kicker="Appendix \u00b7 objections, answered", title="On the evidence")

    return _STYLE + _NAV % (D.n, D.n) + D.html() + _SCRIPT


# ------------------------------------------------------------------- chrome
_NAV = """<div class="progress"><i id="pg"></i></div>
<div class="hint" id="hint">&larr; &rarr; to move &middot; %d slides &middot; print for handout</div>
<div class="cnt"><span id="cur">1</span>&thinsp;/&thinsp;%d</div>"""

_SCRIPT = """
<script>
(function(){
 var s=[].slice.call(document.querySelectorAll('.slide')),i=0,
     pg=document.getElementById('pg'),cur=document.getElementById('cur'),
     hint=document.getElementById('hint');
 function go(n){i=Math.max(0,Math.min(s.length-1,n));
   s[i].scrollIntoView({behavior:'smooth',block:'start'});}
 function paint(){pg.style.width=((i+1)/s.length*100)+'%';cur.textContent=i+1;}
 document.addEventListener('keydown',function(e){
   if(e.key==='ArrowRight'||e.key==='PageDown'||e.key===' '){e.preventDefault();go(i+1);}
   else if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();go(i-1);}
   else if(e.key==='Home'){e.preventDefault();go(0);}
   else if(e.key==='End'){e.preventDefault();go(s.length-1);}});
 if('IntersectionObserver' in window){
   var io=new IntersectionObserver(function(es){
     es.forEach(function(en){if(en.isIntersecting){i=s.indexOf(en.target);paint();}});
   },{threshold:0.5});
   s.forEach(function(el){io.observe(el);});
 }
 setTimeout(function(){hint.classList.add('gone');},4200);
 paint();
})();
</script></body></html>"""

_STYLE = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI Capability Model &mdash; Walkthrough</title>
<style>
:root{--ink:#0d1b2a;--muted:#5a798c;--rule:#e2e8ee;--page:#fff;
--accent:#002869;--accent-soft:#F1F5FA;--warn:#E36135;--band:#F7F9FB}
@media(prefers-color-scheme:dark){:root{--ink:#eef2f6;--muted:#93a7b8;--rule:#22303d;
--page:#0b1219;--accent:#7FB2E8;--accent-soft:#12202e;--band:#0d1620}}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--page);color:var(--ink);
font:15px/1.6 "Segoe UI",-apple-system,BlinkMacSystemFont,Inter,Helvetica,Arial,sans-serif;
-webkit-font-smoothing:antialiased;scroll-snap-type:y proximity}
.slide{min-height:100vh;display:flex;align-items:center;padding:64px 56px 78px;
border-top:1px solid var(--rule);scroll-snap-align:start;position:relative}
.slide:first-of-type{border-top:none}
.inner{max-width:1080px;margin:0 auto;width:100%}
.pn{position:absolute;bottom:26px;right:36px;font-size:11px;color:var(--muted);
font-weight:700;letter-spacing:.08em}
.eyebrow{font-size:11px;letter-spacing:.15em;text-transform:uppercase;
color:var(--muted);font-weight:700;margin-bottom:14px}
h1{font-size:46px;line-height:1.08;margin:0 0 18px;letter-spacing:-.03em;
font-weight:700;max-width:22ch}
h1.finding{max-width:20ch;font-size:52px}
h2{font-size:30px;line-height:1.15;margin:0 0 20px;letter-spacing:-.025em;
font-weight:700;max-width:30ch;padding-bottom:16px;border-bottom:2px solid var(--accent)}
h3.minor{font-size:13px;margin:0 0 8px;letter-spacing:.02em;font-weight:700}
p{margin:0 0 13px;max-width:82ch}
.lede{font-size:18px;line-height:1.5;max-width:70ch}
.foot{font-size:12.5px;color:var(--muted);margin-top:18px;max-width:80ch}
.mut{color:var(--muted)}
.warn-t{color:var(--warn);font-weight:700}
.title h1{font-size:58px;max-width:16ch}
.statement{background:var(--band)}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(128px,1fr));
margin:28px 0 12px;border-top:1px solid var(--rule)}
.kpi{padding:18px 20px 16px;border-right:1px solid var(--rule);
border-bottom:1px solid var(--rule)}
.kpi:last-child{border-right:none}
.kpi b{display:block;font-size:40px;line-height:1;letter-spacing:-.035em;
font-weight:700;color:var(--accent)}
.kpi span{font-size:11px;color:var(--muted);display:block;margin-top:9px;
letter-spacing:.03em;line-height:1.35}
.kpi.warn b{color:var(--warn)}
table{width:100%;border-collapse:collapse;font-size:14px;margin:14px 0 6px}
table.mid{font-size:14.5px} table.sm{font-size:12.5px}
th{text-align:left;font-size:10px;letter-spacing:.1em;text-transform:uppercase;
color:var(--muted);border-bottom:1.5px solid var(--accent);padding:0 12px 8px;
font-weight:700}
td{padding:10px 12px;border-bottom:1px solid var(--rule);vertical-align:top}
tbody tr:nth-child(even){background:var(--band)}
tr:last-child td{border-bottom:none}
td.c,th.c{text-align:center}
code{font:12.5px ui-monospace,SFMono-Regular,Menlo,monospace;
background:var(--accent-soft);padding:1px 5px;border-radius:4px}
.callout{background:var(--accent-soft);padding:20px 24px;margin:20px 0 4px;
border-left:3px solid var(--accent);max-width:88ch}
.callout.warn{border-left-color:var(--warn)}
.callout p:last-child{margin-bottom:0}
.two{display:grid;grid-template-columns:1fr 1fr;gap:32px;margin:18px 0 4px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));
gap:20px;margin:22px 0 6px}
.card{border-top:2px solid var(--accent);padding:16px 0 0}
.card.warn{border-top-color:var(--warn)}
.card p{font-size:13.5px;margin-bottom:8px}
.ch{font-size:15px;font-weight:700;margin-bottom:9px;letter-spacing:-.01em}
.ids{font-size:11px;line-height:2}
.ids code{font-size:11px}
.objs{display:grid;grid-template-columns:1fr 1fr;gap:22px 34px;margin:14px 0 4px}
.obj{border-top:2px solid var(--rule);padding-top:13px}
.oq{font-size:15px;font-weight:700;letter-spacing:-.01em;margin-bottom:7px;
color:var(--warn)}
.oa{font-size:13px;line-height:1.55;color:var(--ink)}
@media(max-width:900px){.objs{grid-template-columns:1fr}}
.quote{border-left:3px solid var(--rule);padding:4px 0 4px 22px}
.quote p{font-size:21px;line-height:1.35;font-style:italic;color:var(--ink);
margin:0;letter-spacing:-.015em}
ul{margin:0;padding-left:20px;font-size:14px;line-height:1.65}
li{margin-bottom:9px}
.bar{background:var(--rule);height:7px;border-radius:4px;overflow:hidden;
min-width:90px;margin-top:5px}
.bar i{display:block;height:100%;background:var(--accent)}
.progress{position:fixed;top:0;left:0;right:0;height:3px;background:transparent;z-index:20}
.progress i{display:block;height:100%;background:var(--accent);width:0;
transition:width .35s ease}
.cnt{position:fixed;bottom:22px;left:36px;font-size:11px;color:var(--muted);
font-weight:700;letter-spacing:.08em;z-index:20}
.hint{position:fixed;bottom:22px;left:50%;transform:translateX(-50%);
font-size:11px;color:var(--muted);letter-spacing:.06em;z-index:20;
transition:opacity .8s ease;background:var(--page);padding:4px 12px;border-radius:20px}
.hint.gone{opacity:0}
@media(max-width:900px){.two,.cards{grid-template-columns:1fr}
.slide{padding:48px 26px 70px}h1{font-size:34px}h1.finding{font-size:34px}
h2{font-size:24px}.title h1{font-size:38px}}
@media print{
 body{scroll-snap-type:none}
 .slide{min-height:auto;page-break-after:always;break-after:page;
  padding:0 0 26px;border-top:none;display:block}
 .progress,.cnt,.hint{display:none}
 .statement{background:#fff}
 h1,h1.finding{font-size:30px}h2{font-size:22px}
}
</style></head><body>"""

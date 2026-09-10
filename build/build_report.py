# -*- coding: utf-8 -*-
"""The management report as a self-contained HTML page.

No external assets, no JavaScript libraries, no build step beyond this file.
Charts are inline SVG computed from facts/ (see charts.py), so the page cannot
drift from the model and works offline, in email, and from a file:// URL.

Design constraint that shapes everything here: THERE MAY BE NO SCORES YET.  A
heat map of 52 unrated capabilities is one flat colour, and a current-vs-target
gap chart is empty.  So this reports what is actually known - what is built,
what is owned, what is observed - and shows the absence of ratings as a finding
rather than hiding it behind an invented number.

Two rules the code keeps:
  * Nothing here names a scale.  The report argues in whichever scale is the
    default and compares every scale that ships, reading each one's NAME,
    QUESTION, LEVELS and behaviour from the module itself.
  * Every sentence that contains a number is computed from the same facts the
    chart beside it is drawn from.  Prose that would go stale when the facts
    change is generated, not typed.
"""
from datetime import date
import collections

import charts as ch
import derive
from charts import esc, C, LABEL, ORDER, LVL


# The sections of the report, in order.  Numbering and every forward reference
# ("listed in Section N") are computed from this list, so adding a section
# cannot leave a stale number behind.
SECTIONS = [
    "What this report can and cannot say",
    "What the institution has built",
    "The finding",
    "The same evidence",            # completed with ", read N ways" at render time
    "The views",
    "What needs a decision",
    "What would make the next report say more",
]


class _Sections(object):
    """Section numbering driven by SECTIONS."""

    def __init__(self):
        self.n = 0

    def next(self, title):
        self.n += 1
        expected = SECTIONS[self.n - 1]
        assert title.startswith(expected), (title, expected)
        return '<section><h2>Section %d</h2><h3>%s</h3>' % (self.n, title)

    @staticmethod
    def number_of(title):
        return SECTIONS.index(title) + 1

    def sub(self, k, title):
        return ('<h3 style="font-size:15px;margin-top:%dpx">%d.%d &nbsp;%s</h3>'
                % (8 if k == 1 else 28, self.n, k, title))


def names_gated(scales, gated):
    """The scales that do (or do not) gate on performance, named for prose."""
    ss = [s for s in scales if derive.gates_on_practice(s) is bool(gated)]
    ns = ["<b>%s</b>" % esc(s.NAME) for s in ss]
    if not ns:
        return "no scale"
    return ns[0] if len(ns) == 1 else ", ".join(ns[:-1]) + " and " + ns[-1]


def _gates_on_practice(scale):
    """Does this scale refuse to rate when practice is unobserved, however good
    the enablers look?  Read from the scale's behaviour, not from its name."""
    strong = {"practised": "unknown", "enabled": "yes", "skilled": "yes", "defined": "yes"}
    return scale.level(strong)[0] is None


def _top(scale):
    cap = getattr(scale, "DERIVABLE_MAX", None)
    return cap if cap is not None else max(n for n, _, _ in scale.LEVELS)


def _plural(n, one, many=None):
    return one if n == 1 else (many or one + "s")


def _derivable(scale):
    """The level numbers a scale can actually return, found by running it over
    every combination of observation values rather than trusting DERIVABLE_MAX."""
    import itertools
    vals = ("yes", "partial", "no", "n/a", "unknown")
    out = set()
    for combo in itertools.product(vals, repeat=4):
        lv = scale.level(dict(zip(("practised", "enabled", "skilled", "defined"), combo)))[0]
        if lv is not None:
            out.add(lv)
    return out


def _comparable(default, other):
    """Two scales' numbers can be compared one for one only when every level
    the lens can return is also a level the default can return.  A 1-5
    executive ladder against a 0-3 ladder is not - 'reads higher' would be an
    artefact of the numbering, not a disagreement about the capability."""
    return _derivable(other) <= _derivable(default)


def _agreement(m, default, other):
    """(both, agree, higher, lower) comparing one scale against the default.

    Only capabilities both scales actually RATE are compared - a not-rated is
    the absence of a placement, not a low one, and counting it as a
    disagreement would overstate how far the scales diverge.  agree/higher/
    lower are None when the ladders are not comparable (see _comparable).
    """
    both = agree = higher = lower = 0
    for c in m.capabilities:
        a = m.rate(default, c['id'])[0]
        b = m.rate(other, c['id'])[0]
        if a is None or b is None:
            continue
        both += 1
        if b == a:
            agree += 1
        elif b > a:
            higher += 1
        else:
            lower += 1
    if not _comparable(default, other):
        return both, None, None, None
    return both, agree, higher, lower


def report(m, scale, demo=False, scales=None):
    """scale: the scale the report ARGUES IN - its narrative is written against
    that ladder.  scales: every scale that ships, for the comparison section.
    Defaults to [scale] so a caller that passes one still produces a valid page.
    """
    scales = list(scales or [scale])
    if not any(s is scale for s in scales):
        same = [s for s in scales if getattr(s, "SHORT", None) == getattr(scale, "SHORT", "")]
        scale = same[0] if same else scale
        if not same:
            scales = [scale] + scales
    if demo:
        import sample
        m = sample.Demo(m, sample.sample_observations(m))
    total = len(m.capabilities)
    top = _top(scale)
    rated = {c['id']: m.rate(scale, c['id']) for c in m.capabilities}
    n_rated = sum(1 for v in rated.values() if v[0] is not None)
    pending = m.pending_assets()
    noowner = [c for c in m.capabilities if m.owner(c['id'])[1] == 'NO MATCH']
    box_total = sum(len(o['in_the_box']) for o in m.offerings)
    box_done = sum(1 for o in m.offerings for x in o['in_the_box'] if x['status'])
    obsv = {c['id']: m.values(c['id']) for c in m.capabilities}

    # count what this page actually shows: in demo mode the observations are the
    # sample ones, so reading m.observations (which passes through to the real
    # rows) would print a coverage figure that contradicts every chart beside it
    n_obs = n_known = 0
    for c in m.capabilities:
        for t in m.observation_types:
            if t['id'] in m.criterion_types:
                rows_ = [r for _x, r in m.criteria_obs(c['id'], t['id'])]
            else:
                rows_ = [m.cap_obs(c['id'], t['id'])]
            n_obs += len(rows_)
            n_known += sum(1 for r in rows_ if r.get('value', 'unknown') != 'unknown')

    S = _Sections()
    o = []
    w = o.append
    w(STYLE)

    # ---------------------------------------------------------- header
    if demo:
        w('<div class="banner">ILLUSTRATIVE &mdash; the capability map, offerings, '
          'assets and owners are real. The observations behind every chart are '
          'SAMPLE values, shown so the finished report can be reviewed before the '
          'assessment is run. This is not an assessment.</div>')
    w('<div class="wrap">')
    tag = ('<br><span style="font-size:20px;font-weight:600;color:var(--warn)">'
           'Illustrative edition</span>') if demo else ''
    w('<header><h1>AI Capability &mdash; Management Report%s</h1>'
      '<div class="sub">Inter-American Development Bank &nbsp;&#183;&nbsp; %s '
      '&nbsp;&#183;&nbsp; generated from the capability model</div></header>'
      % (tag, date.today().strftime("%d %B %Y")))

    # ---------------------------------------------------------- 1 coverage
    w(S.next('What this report can and cannot say'))
    w('<p class="lede">Read this before the findings. It states how much of the '
      'assessment has actually been done, so nothing below is read as more than it is.</p>')
    w('<div class="kpis">')
    w('<div class="kpi good"><b>%d</b><span>Platform offerings, evidenced</span></div>' % len(m.offerings))
    w('<div class="kpi good"><b>%d</b><span>Assets with a location</span></div>' % len(m.assets))
    w('<div class="kpi mid"><b>%d%%</b><span>Observations recorded</span></div>'
      % (100 * n_known // (n_obs or 1)))
    w('<div class="kpi %s"><b>%d of %d</b><span>Capabilities rated</span></div>'
      % ("warn" if n_rated == 0 else "mid", n_rated, total))
    w('</div>')
    if n_rated == 0:
        w('<div class="callout warn"><p><b>No capability is rated yet &mdash; and that is a '
          'factual statement, not a bad result.</b></p><p>A rating requires knowing whether '
          'something is actually <i>practised</i> on real AI systems. That question has not '
          'yet been put to the capability owners. What <i>has</i> been established is what '
          'the institution has <b>built</b>, and that is substantial and evidenced.</p>'
          '<p>This is the difference between <i>we do not know</i> and <i>we do not have '
          'it</i>. Most maturity assessments cannot tell those apart and score an '
          'unexamined capability as if it were absent. This one refuses to.</p></div>')
    else:
        w('<div class="callout"><p><b>%d of %d capabilities carry a rating.</b> The '
          'remainder are not zero &mdash; they are unobserved, and are shown as such '
          'throughout.</p></div>' % (n_rated, total))
    # coverage by domain - counted over the rows a reviewer actually fills in,
    # which after ADR-0014 is one per L3 criterion for `practised`
    rows = []
    for d in m.domains:
        caps = [c for c in m.capabilities if c['domain'] == d['id']]
        cnt = collections.Counter()
        ncrit = 0
        for c in caps:
            for t in m.observation_types:
                if t['id'] in m.criterion_types:
                    for _x, r_ in m.criteria_obs(c['id'], t['id']):
                        cnt["unknown" if r_.get('value', 'unknown') == 'unknown'
                            else "yes"] += 1
                        ncrit += 1
                else:
                    v = m.cap_obs(c['id'], t['id']).get('value', 'unknown')
                    cnt["unknown" if v == "unknown" else "yes"] += 1
        rows.append((ch.domain_label(d),
                     "%d capabilities · %d criteria" % (len(caps), ncrit),
                     {"yes": cnt["yes"], "unknown": cnt["unknown"]}))
    w('<h3 class="minor">How much has been observed, by domain</h3>')
    w(ch.stacked_bar(rows, keys=["yes", "unknown"]))
    w('<div class="legend"><span><i style="background:%s"></i>Observed, with evidence</span>'
      '<span><i style="background:%s"></i>Nobody has looked yet</span></div>'
      % (C["yes"], C["unknown"]))
    w('</section>')

    # ---------------------------------------------------------- 2 what exists
    w(S.next('What the institution has built'))
    w('<p>Every row is backed by a named asset with a status and a location. '
      'This is the part of the picture that is <b>not</b> an opinion.</p>')
    w(ch.progress_rows([(x['name'],) + m.release_count(x)
                        + ("enables " + ", ".join(x['enables']),)
                        for x in m.offerings]))
    ready = [x for x in m.offerings if m.offering_complete(x)]
    w('<p style="margin-top:16px"><b>%d of %d offerings are complete.</b> %s</p>'
      % (len(ready), len(m.offerings),
         ("The others are waiting on named documents or modules, listed in Section %d."
          % S.number_of("What needs a decision"))
         if len(ready) < len(m.offerings) else "Nothing is pending."))
    # enablement by domain
    w('<h3 class="minor">Can a team get the tooling? By domain</h3>')
    rows = []
    for d in m.domains:
        caps = [c for c in m.capabilities if c['domain'] == d['id']]
        rows.append((ch.domain_label(d), "",
                     dict(collections.Counter(obsv[c['id']]['enabled'] for c in caps))))
    w(ch.stacked_bar(rows))
    w(ch.legend())
    if demo:
        w('<p class="vd">Sample values in this edition; the offerings above are real.</p>')
    w('<p style="margin-top:14px"><i>Not applicable</i> is a legitimate answer, not a gap: '
      'a strategy or workforce capability is not worse for having no platform component. '
      '<i>Not observed</i> means the platform register was checked and nothing was found, '
      'and nobody has yet asked whether an enterprise service provides it. The shape to '
      'notice is that the platform and engineering domains carry the tooling, and the '
      'governance domains carry almost none.</p>')
    w('</section>')

    # ---------------------------------------------------------- 3 finding
    w(S.next('The finding'))
    w('<div class="callout"><p><b>The institution has built its enablers ahead of its '
      'practice.</b></p></div>')
    w('<p>The scale used here &mdash; <b>%s</b> &mdash; places <b>performance</b> at '
      'Level 1, <b>tooling and competent people</b> at Level 2, and <b>an approved '
      'standard, applied</b> at Level 3. Measured that way, a large part of the Level '
      '2 and Level 3 apparatus exists &mdash; platforms, standards, reference '
      'architectures, infrastructure modules &mdash; while Level 1, whether the work is '
      'actually done, %s.</p>'
      % (esc(scale.NAME),
         "has never been examined" if n_rated == 0 else
         "has been examined for %d of %d capabilities" % (n_rated, total)))
    w('<p>That is not a criticism of the build. It explains a disagreement that recurs '
      'here: one person says a capability exists, meaning the platform and the standard '
      'exist; another says it does not, meaning nothing is running on it. '
      '<b>Both are right about different things.</b> A model carrying a single number '
      'cannot show that. This one shows it as four columns.</p>')
    en = collections.Counter(v['enabled'] for v in obsv.values())
    de = collections.Counter(v['defined'] for v in obsv.values())
    sk = collections.Counter(v['skilled'] for v in obsv.values())
    pr = collections.Counter(v['practised'] for v in obsv.values())
    w('<table><thead><tr><th>What can be evidenced today</th>'
      '<th>What cannot</th></tr></thead><tbody>')
    for a, b in [
        ("%d offerings and %d assets, with locations" % (len(m.offerings), len(m.assets)),
         "Whether any of it is used in production"
         if pr['unknown'] == total else
         "Whether it is used in production: known for %d of %d capabilities"
         % (total - pr['unknown'], total)),
        ("Which capabilities have platform tooling (%d), partial tooling (%d), and where "
         "tooling does not apply (%d)" % (en['yes'], en['partial'], en['n/a']),
         "Whether tooling exists for the %d capabilities nobody has yet examined"
         % en['unknown'] if en['unknown'] else
         "Which of the %d capabilities without tooling genuinely need it" % en['no']),
        ("Which capabilities have an approved standard (%d) or one in pre-release (%d)"
         % (de['yes'], de['partial']),
         "Whether the work is done against it"),
        ("Where a standard exists in the platform register",
         "Whether the people who need the skills have them: %d of %d unobserved"
         % (sk['unknown'], total))]:
        w('<tr><td>%s</td><td style="color:var(--muted)">%s</td></tr>' % (esc(a), esc(b)))
    w('</tbody></table></section>')

    # ------------------------------------------------- 4 the same evidence,
    # read N ways.  Placed immediately after the finding because it is the
    # evidence FOR the finding, not an alternative to it.
    w(scales_section(m, scale, scales, total, demo, S))

    # ---------------------------------------------------------- 5 views
    w(S.next('The views'))
    views = []           # (title, ready:bool) - counted at the end, not typed

    def vh(title, ready, desc):
        views.append((title, ready))
        tag_ = ("READY" if not demo else "REAL DATA") if ready else \
               ("SAMPLE" if demo else "AWAITING OBSERVATIONS")
        w('<div class="viewhdr"><h4>%s</h4><span class="tag %s">%s</span></div>'
          % (esc(title), "t-real" if ready else "t-wait", tag_))
        w('<p class="vd">%s</p>' % desc)

    if demo:
        w('<p class="lede">The views this model produces, every one populated. '
          'Views marked <span class="tag t-real">REAL DATA</span> are drawn from '
          '<b>recorded facts</b> and look exactly like this today. Views marked '
          '<span class="tag t-wait">SAMPLE</span> are filled with '
          '<b>illustrative observations</b>, because the real ones have not been '
          'collected yet.</p>')
    else:
        w('<p class="lede">The views this model produces. Those marked '
          '<span class="tag t-real">READY</span> are drawn from recorded facts and are '
          'usable today. Those marked <span class="tag t-wait">AWAITING OBSERVATIONS'
          '</span> are built and will populate as answers arrive &mdash; they are '
          'shown empty rather than filled with an estimate.</p>')

    # 1 observation heat map - always drawn; in the live edition it shows what is known
    vh("Observation heat map", not demo,
       ("Every capability, every observation, on one screen. This is what the "
        "assessment looks like once the questions have been answered."
        if demo else
        "Every capability, every observation. This is the whole assessment on one "
        "screen: what is known is coloured, what nobody has looked at is pale. "
        "The pale columns are the work still to do."))
    if demo:
        views[-1] = (views[-1][0], False)
    w(ch.obs_heatmap(m))
    w(ch.legend())
    w('<p style="margin-top:14px;font-size:13.5px;color:var(--muted)">'
      'The <b>practised</b> cell is a roll-up: it is observed once per L3 criterion '
      '(%d in total) and derived here, so one weak practice inside a capability shows '
      'as <i>partial</i> rather than disappearing into an average. The other three are '
      'observed once per capability.</p>'
      % sum(len(c['criteria']) for c in m.capabilities))

    # 2 enablement by domain - real in the live edition; in the illustrative
    # edition `enabled` is sampled with everything else, so it must say so
    vh("Tooling by domain", not demo,
       "Can a delivery team get what it needs without building it? The platform and "
       "engineering domains carry the tooling; the governance domains carry almost "
       "none; People &amp; Skills is correctly not a technical question at all.")
    rows = []
    for d in m.domains:
        caps = [c for c in m.capabilities if c['domain'] == d['id']]
        rows.append((ch.domain_label(d), "", dict(collections.Counter(
            obsv[c['id']]['enabled'] for c in caps))))
    w(ch.stacked_bar(rows))
    w(ch.legend())

    # 3 accountability - REAL
    vh("Accountability spread", True,
       "Capabilities per unit, mapped against the institution's own product and "
       "enabler catalogue. The red bar is the finding.")
    w(ch.owners_chart(m))

    # 4 control exposure - REAL
    vh("Control exposure", True,
       "For each offering, whether a delivery team inherits its controls or rebuilds "
       "them. Every unanswered row is both a risk and a roadmap item.")
    w(ch.progress_rows([(x['name'],
                         sum(1 for y in x['in_the_box'] if y['status']),
                         len(x['in_the_box']), "")
                        for x in m.offerings if x['in_the_box']]))

    # 5 roadmap horizons - REAL
    vh("Roadmap horizons", True,
       "What moves now, next and later &mdash; assembled from the facts rather than "
       "from a workshop.")
    w(ch.waves_chart(m))

    # 6-10 need levels
    levels = {c['id']: rated[c['id']][0] for c in m.capabilities}
    keys = ch.level_keys(scale)
    lvl_legend = ch.legend(keys, ch.level_labels(scale), LVL)
    if demo:
        import sample
        targets = sample.sample_targets(m, levels, top)
    else:
        targets = None
    have_levels = n_rated > 0

    def vw(title, desc, chart, missing, who, extra=""):
        """A view: populated when it can be, an honest empty state otherwise."""
        vh(title, False if demo else have_levels, desc)
        if demo or have_levels:
            w(chart())
            if extra:
                w(extra)
        else:
            w(ch.empty_state(missing[0], missing[1], who))

    vw("Capability heat map",
       "All %d capabilities by their derived level &mdash; the single picture of "
       "the estate." % total,
       lambda: ch.v_heatmap(m, obsv, levels, top) + lvl_legend,
       ("Nothing to colour yet",
        "A level needs to know whether a capability is practised. That has not been "
        "asked of anyone yet, so all %d are unrated and the map would be one flat "
        "colour." % total),
       "Capability owners, one question per L3 criterion")

    def need_targets(title, desc, chart, missing_now, who):
        # targets are a decision nobody has recorded; without them these two
        # views stay empty even once levels exist
        vh(title, False, desc)
        if demo:
            w(chart())
        else:
            w(ch.empty_state(*missing_now, who))

    need_targets("Domain scorecard",
                 "Eight domains, current against target &mdash; the radar a steering "
                 "committee reads fastest.",
                 lambda: ch.v_radar(m, obsv, levels, targets, top)
                         + '<div class="legend"><span><i style="background:#002869"></i>'
                           'Current</span><span><i style="background:#E36135"></i>'
                           'Target, 12 months</span></div>',
                 ("No target state exists" if have_levels else "No current position, and no target",
                  "Needs a level per capability, and a target level per domain with a date."
                  + (" Levels exist; targets are a decision nobody has recorded yet."
                     if have_levels else " Neither exists yet.")),
                 "Capability owners, then a target-setting decision")

    vw("Built against practised",
       "The disagreement, plotted: capabilities the platform has enabled that nobody "
       "is yet doing.",
       lambda: ch.v_quadrant(m, obsv, levels),
       ("Half the axis exists",
        "Enablement is recorded for %d capabilities. Practice is recorded for "
        "none, so every point would sit on one line." % (total - en['unknown'])),
       "Capability owners",
       '<p style="margin-top:12px;font-size:13px;color:var(--muted)">Each dot is a '
       'capability. <b>Bottom-right</b> is the pattern this institution expects to '
       'find: the platform is built, the practice has not caught up.</p>')

    need_targets("Biggest gaps to target",
                 "The capabilities furthest from where they need to be, with the "
                 "accountable unit beside each.",
                 lambda: ch.v_gapbars(m, obsv, levels, targets, top),
                 ("No target state exists",
                  "A gap needs both a current level and a target. Setting targets is a "
                  "decision, not an observation, and it is worth taking after the first "
                  "real ratings rather than before."),
                 "The steering group, once ratings exist")

    vw("Level distribution",
       "How many capabilities sit at each level. A histogram is harder to argue with "
       "than an average, and this model never averages.",
       lambda: ch.v_levels(m, levels, keys) + lvl_legend,
       ("Nothing to distribute",
        "Reads the derived level. All %d are currently unrated." % total),
       "Capability owners")

    need_targets("Trajectory",
                 "Where the portfolio sits today against where the targets would put it.",
                 lambda: ch.v_trajectory(m, levels, targets, keys)
                         + '<div class="legend"><span><i style="background:#002869"></i>'
                           'Today</span><span><i style="background:#E36135"></i>'
                           'If targets are met</span></div>',
                 ("Nothing to plot",
                  "Needs both a current distribution and a target distribution."),
                 "Capability owners, then a target-setting decision")

    # the profile is drawable from whatever has been observed
    vh("Assessment profile", not demo,
       "The four observations across all %d capabilities. Shows which question is the "
       "constraint &mdash; usually practice, not tooling." % total)
    w(ch.v_profile(m, obsv) + ch.legend())
    if not demo:
        unobserved = [t['id'] for t in m.observation_types
                      if all(v[t['id']] == 'unknown' for v in obsv.values())]
        if unobserved:
            w('<p style="margin-top:10px;font-size:13px;color:var(--muted)">'
              '%s %s not been recorded for any capability yet, so %s bar%s %s entirely '
              'pale.</p>'
              % (" and ".join("<b>%s</b>" % t for t in unobserved),
                 "has" if len(unobserved) == 1 else "have",
                 "that" if len(unobserved) == 1 else "those",
                 "" if len(unobserved) == 1 else "s",
                 "is" if len(unobserved) == 1 else "are"))

    n_ready = sum(1 for _, r in views if r)
    if demo:
        w('<div class="callout warn"><p><b>Every chart marked SAMPLE is illustrative.</b> '
          'The capability map, the offerings, the assets and the owners are real; '
          'the observations are not. Answering four questions &mdash; put to the '
          'capability owners, the platform teams, the standard-setting functions and '
          'Learning &amp; Development &mdash; is what turns this into an '
          'assessment.</p></div>')
    else:
        w('<div class="callout"><p><b>%d of %d views are usable today.</b> The '
          'others are not blocked by tooling or by design &mdash; they are blocked by '
          '%s To see the whole report populated with illustrative numbers, open '
          '<code>management-report-illustrative.html</code>.</p></div>'
          % (n_ready, len(views),
             "one question that has never been put to the capability owners: "
             "<i>is this actually done, and where?</i>" if not have_levels else
             "a target state that nobody has yet decided."))
    w('</section>')

    # ---------------------------------------------------------- 6 decisions
    w(S.next('What needs a decision'))
    w(S.sub(1, 'Capabilities nobody owns'))
    w('<div class="split"><div>%s<div style="text-align:center;font-size:12px;'
      'color:var(--muted);margin-top:6px">%d of %d unowned</div></div><div>'
      % (ch.donut({"no": len(noowner), "yes": total - len(noowner)}, keys=["no", "yes"]),
         len(noowner), total))
    w('<p>These are claimed by no product or enabler in the institution\'s own catalogue. '
      'Several are governance capabilities an institution of this kind is normally '
      'expected to hold.</p>')
    w('<table><tbody>')
    for c in sorted(noowner, key=lambda x: m.sort_key(x['id'])):
        w('<tr><td><code>%s</code></td><td><b>%s</b></td>'
          '<td style="color:var(--muted)">%s</td></tr>'
          % (c['id'], esc(c['name']), esc(m.domain_by_id[c['domain']]['name'])))
    w('</tbody></table></div></div>')
    w('<p><b>Decision required:</b> assign an owner to each, or record a deliberate '
      'decision not to hold it.</p>')

    w(S.sub(2, 'Finished, but not released'))
    w('<p>%d assets exist and are not yet available to delivery teams. Each is days from '
      'being usable, and each currently holds a capability below what the underlying work '
      'would support.</p>' % len(pending))
    w('<table><thead><tr><th>Asset</th><th>What it is</th><th>Status</th></tr></thead><tbody>')
    for a in pending:
        w('<tr><td><code>%s</code></td><td>%s</td>'
          '<td><span class="pill p-mid" title="%s">%s</span></td></tr>'
          % (a['id'], esc(a['name']),
             esc(m.asset_statuses.get(a['status'], {}).get('meaning', '')),
             esc(a['status'])))
    w('</tbody></table>')
    w('<p><b>Decision required:</b> a release date for each, with a named owner.</p>')

    w(S.sub(3, 'Questions only the platform teams can answer'))
    w('<p><b>%d of %d answered.</b> These decide whether a delivery team inherits its '
      'controls or rebuilds them. Every unanswered row is an unknown; every <i>no</i> is '
      'a roadmap item, usually a cheap one, because it means extending a module rather '
      'than building a platform.</p>' % (box_done, box_total))
    w(ch.progress_rows([(x['name'],
                         sum(1 for y in x['in_the_box'] if y['status']),
                         len(x['in_the_box']), "")
                        for x in m.offerings if x['in_the_box']]))
    w('</section>')

    # ---------------------------------------------------------- 7 next
    w(S.next('What would make the next report say more'))
    w('<table><thead><tr><th>Who</th><th>What is asked of them</th>'
      '<th>What it unlocks</th></tr></thead><tbody>')
    n_undef = de['unknown']
    for who, what, why in [
        ("Capability owners",
         "For each L3 criterion under a capability they own: is this specific "
         "practice done on real AI systems, and where?",
         "Every rating in the model. Nothing can be rated without it"),
        ("Platform teams", "The %d outstanding in-the-box questions" % (box_total - box_done),
         "Whether controls are inherited or rebuilt by every team"),
        ("Cybersecurity · Data Management · Legal · HR",
         "Does an approved standard exist in your domain?",
         "%d capabilities show <i>not observed</i> only because the asset register "
         "covers platform assets" % n_undef),
        ("Learning &amp; Development", "Who is trained, and in what?",
         "Level 2 for every capability where practice exists")]:
        w('<tr><td><b>%s</b></td><td>%s</td><td style="color:var(--muted)">%s</td></tr>'
          % (who, what, why))
    w('</tbody></table>')
    w('<div class="callout"><p>None of this requires new tooling or new investment. '
      'It requires four questions put to people who already know the answers.</p></div>')
    w('</section>')

    w('<footer>Generated from the capability model &mdash; %d domains, %d capabilities, '
      '%d criteria.<br>Scale: %s. %s<br>%s</footer>'
      % (len(m.domains), total, sum(len(c['criteria']) for c in m.capabilities),
         esc(scale.NAME), esc(scale.BASIS),
         "Observations on this page are SAMPLE values and were never written to facts/."
         if demo else
         "Every figure traces to a recorded fact with evidence and a date; nothing here "
         "is estimated."))
    w('</div></body></html>')
    return "\n".join(o)


def scales_section(m, default, scales, total, demo, S):
    """The same evidence read by every scale that ships.

    Self-contained on purpose: a reader who has never opened the repository
    should finish this section knowing what a scale IS, what each one asks,
    why more than one exists, and which one to believe when they disagree.

    Every sentence with a number in it is computed from the scales' behaviour
    on the observations shown, so adding a scale or recording an observation
    cannot leave this text describing a page that no longer exists.
    """
    o = []
    w = o.append
    n = len(scales)
    words = {1: "one way", 2: "two ways", 3: "three ways", 4: "four ways", 5: "five ways"}
    w(S.next('The same evidence, read %s' % words.get(n, "%d ways" % n)))

    # ---- what a scale is
    w('<p class="lede">A <b>level</b> is never typed into this model. It is '
      '<b>derived</b> &mdash; a rule reads the four observations and returns a level '
      'and a sentence saying why. That rule is called a <b>scale</b>, and it is the '
      'only place in the model where a judgement is encoded.</p>')
    w('<p>Separating the two matters more than it sounds. <b>An observation is a fact, '
      'not a score.</b> &ldquo;The standard is pre-release&rdquo; is true whichever '
      'framework reads it. So the same body of evidence can be read by more than one '
      'scale, and the scales <b>cannot disagree about what is true</b> &mdash; only '
      'about what to make of it. Adding a scale re-rates nothing and re-interviews '
      'nobody.</p>')
    w('<p>That is why this section exists. A reader who arrives holding a different '
      'frame &mdash; a maturity ladder, an executive readiness tier &mdash; can be '
      'answered in it, without the assessment being redone and without anyone '
      'pretending the underlying evidence changed.</p>')

    # ---- where the four answers are recorded, before any rule reads them
    w(S.sub(1, 'What the rule reads, and where those answers are recorded'))
    rec = derive.recorded_at(m)
    at_crit = [r for r in rec if r['at'].startswith('L3')]
    at_cap = [r for r in rec if r['at'].startswith('L2')]
    n_crit_ = sum(len(c['criteria']) for c in m.capabilities)

    def _obs_names(rs):
        ns = ["<code>%s</code>" % esc(r['id']) for r in rs]
        return ns[0] if len(ns) < 2 else ", ".join(ns[:-1]) + " and " + ns[-1]

    w('<p>Every scale below reads the same four answers. <b>Only two of the three '
      'taxonomy levels ever carry one</b>, and one of the four is not recorded by '
      'anybody &mdash; it is computed.</p>')
    w('<table><thead><tr><th style="width:24%">Taxonomy level</th>'
      '<th>What is recorded against it</th><th class="c" style="width:12%">Rows</th>'
      '</tr></thead><tbody>')
    w('<tr><td><b>L1 domain</b> &middot; %d</td><td><i>Nothing.</i> A domain is a '
      'reporting cluster and is never scored</td><td class="c">&mdash;</td></tr>'
      % len(m.domains))
    w('<tr><td><b>L2 capability</b> &middot; %d</td><td>%s &mdash; one row each. Plus '
      '%s, <b>derived</b> from the criteria beneath it and never typed</td>'
      '<td class="c">%d</td></tr>'
      % (len(m.capabilities), _obs_names(at_cap), _obs_names(at_crit),
         len(at_cap) * len(m.capabilities)))
    w('<tr><td><b>L3 criterion</b> &middot; %d</td><td>%s &mdash; one row per '
      'criterion, because that is the level at which work can actually be '
      'witnessed</td><td class="c">%d</td></tr>'
      % (n_crit_, _obs_names(at_crit), len(at_crit) * n_crit_))
    w('</tbody></table>')
    w('<p>So a review round collects <b>%d rows</b>, not %d. The capability-level %s '
      'value every chart in this report is drawn from was <b>computed</b> by the '
      'roll-up, never entered: there is nowhere to type it, and a stored level is the '
      'one edit validation rejects outright.</p>'
      % (len(m.observations), len(m.capabilities), _obs_names(at_crit)))

    # ---- what each one asks
    w(S.sub(2, 'What each scale asks'))
    w('<table><thead><tr><th style="width:22%">Scale</th><th style="width:26%">The '
      'question it asks</th><th style="width:30%">Levels</th>'
      '<th style="width:22%">Standing</th></tr></thead><tbody>')
    for s in scales:
        names = " · ".join("%d %s" % (n_, k) for n_, k, _ in s.LEVELS)
        cap = getattr(s, "DERIVABLE_MAX", None)
        is_def = s is default
        standing = ('<b>The default.</b> The assessment itself.' if is_def
                    else 'A lens. Reporting only.')
        if cap is not None:
            standing += ' Tops out at <b>%d</b> today.' % cap
        standing += (' Gates on performance.' if _gates_on_practice(s)
                     else ' Does <b>not</b> gate on performance.')
        w('<tr><td><b>%s</b><br><span style="color:var(--muted);font-size:12px">%s</span></td>'
          '<td>%s</td><td style="font-size:12px">%s</td><td>%s</td></tr>'
          % (esc(s.NAME), esc(getattr(s, "SHORT", "")),
             esc(getattr(s, "QUESTION", None) or getattr(s, "BASIS", "")[:120]),
             esc(names), standing))
    w('</tbody></table>')

    # ---- what it takes to reach each level, derived by running the rule
    w(S.sub(3, 'What it takes to reach each level'))
    n_combo = len(derive.VALUES) ** len(derive.TYPES)
    w('<p>Nothing in the tables below is written down anywhere. Each is derived by '
      'running that scale over all <b>%d combinations</b> of the five values across '
      'the four observations, so it cannot drift from the rule it describes. Read '
      'each row as <b>to reach at least this level</b>. <code>n/a</code> counts as '
      'satisfied &mdash; a capability that legitimately needs no tooling is not held '
      'down for having none.</p>' % n_combo)
    for sc in scales:
        rungs = derive.ladder(sc)
        exact = all(r['exact'] for r in rungs)
        w('<h4 style="margin:24px 0 4px;font-size:14px">%s%s</h4>'
          % (esc(sc.NAME), '' if sc is default else
             ' <span style="color:var(--muted);font-weight:400">&mdash; a lens</span>'))
        w('<table><thead><tr><th style="width:20%">To reach</th>')
        for t in derive.TYPES:
            w('<th class="c">%s</th>' % esc(t.title()))
        w('<th class="c" style="width:12%">Combinations</th></tr></thead><tbody>')
        for r in rungs:
            w('<tr><td><b>%d %s</b>%s</td>'
              % (r['n'], esc(r['name']),
                 '' if r['exact'] else ' <span class="pill p-no">approx</span>'))
            for t in derive.TYPES:
                c = r['conds'][t]
                if c['kind'] == 'any':
                    cell = '<span style="color:var(--muted)">any</span>'
                elif c['text'].startswith('not '):
                    cell = 'not <code>%s</code>' % esc(c['text'][4:])
                else:
                    cell = " or ".join('<code>%s</code>' % esc(v) for v in c['vals'])
                w('<td class="c">%s</td>' % cell)
            w('<td class="c">%d of %d</td></tr>' % (r['combos'], n_combo))
        w('</tbody></table>')
        steps = [r for r in rungs if r['adds']]
        if exact and steps:
            bits = []
            for r in steps:
                bits.append('<b>%d %s</b> adds %s'
                            % (r['n'], esc(r['name']),
                               ", ".join('<code>%s</code>&nbsp;=&nbsp;%s'
                                         % (esc(a), " or ".join('<code>%s</code>' % esc(v)
                                            for v in r['conds'][a]['vals']))
                                         for a, _b in r['adds'])))
            w('<p class="vd">%s.</p>' % "; ".join(bits))
            last = steps[-1]
            if len(steps) > 1 and len(last['adds']) == 1:
                below = steps[-2]
                a = last['adds'][0][0]
                w('<div class="callout"><p><b>The whole difference between %d %s and '
                  '%d %s is one observation: <code>%s</code> must be %s.</b> Everything '
                  'else is already required at %d &mdash; which is why a capability '
                  'with the work done, the tooling provided and competent people stops '
                  'at %d until an approved standard exists.</p></div>'
                  % (below['n'], esc(below['name']), last['n'], esc(last['name']),
                     esc(a), " or ".join('<code>%s</code>' % esc(v)
                                         for v in last['conds'][a]['vals']),
                     below['n'], below['n']))
        elif not exact:
            w('<p class="vd">Rows marked <b>approx</b> hold for every capability at '
              'that level but do not by themselves determine it: this scale averages, '
              'and no per-observation condition describes an average. Read it in the '
              'worked table below instead.</p>')
        ur, urn = derive.unrated(sc)
        if urn:
            if ur:
                cause = "; ".join(
                    '<code>%s</code> is %s'
                    % (esc(t), " or ".join('<code>%s</code>' % esc(v) for v in vs))
                    for t, vs in ur)
                cause = 'whenever %s, whatever the others say' % cause
            else:
                cause = ('when too few dimensions have been observed to judge &mdash; '
                         'no single observation forces it')
            w('<p class="vd"><b>Not rated</b> %s: %d of %d combinations. '
              'This scale %s on performance.</p>'
              % (cause, urn, n_combo,
                 '<b>gates</b>' if derive.gates_on_practice(sc)
                 else 'does <b>not</b> gate'))

    # ---- the same answers, read by every scale at once
    w(S.sub(4, 'The same answers, read by every scale'))
    w('<p>Ten situations a reviewer will actually record, run through %s at once. '
      'Every level and every reason is computed by calling the rule, not written '
      'here.</p>' % ('both scales' if len(scales) == 2
                     else 'all %d scales' % len(scales)))
    w('<table><thead><tr><th style="width:26%">If the four answers are</th>')
    for t in derive.TYPES:
        w('<th class="c">%s</th>' % esc(t[:3].title()))
    for sc in scales:
        w('<th class="c">%s%s</th>'
          % (esc(sc.NAME), '' if sc is default else '<br><span style="font-weight:400">'
             '(lens)</span>'))
    w('</tr></thead><tbody>')
    for label, obs, row in derive.worked(scales):
        w('<tr><td>%s</td>' % esc(label))
        for t in derive.TYPES:
            w('<td class="c"><code>%s</code></td>' % esc(obs[t]))
        for _sc, lv, nm, _why in row:
            w('<td class="c">%s</td>'
              % ('<b>%d</b> %s' % (lv, esc(nm)) if lv is not None
                 else '<span style="color:var(--muted)">not rated</span>'))
        w('</tr>')
    w('</tbody></table>')
    ungated_ = [sc for sc in scales if not derive.gates_on_practice(sc)]
    if ungated_:
        w('<div class="callout warn"><p><b>Look at the second row.</b> With the '
          'tooling provided, the people competent and an approved standard in place, '
          'but nobody yet asked whether the work is actually done, %s '
          'return%s <b>not rated</b> &mdash; while %s place%s it near the top of its '
          'ladder. <b>That single row is the entire argument for this model.</b></p>'
          '</div>'
          % (names_gated(scales, True), 's' if len(scales) - len(ungated_) == 1 else '',
             names_gated(scales, False), 's' if len(ungated_) == 1 else ''))

    # ---- the comparison itself
    w(S.sub(5, 'All %d capabilities, under each scale' % total))
    rows = []
    counts_by = {}
    for s in scales:
        counts = collections.Counter(m.rate(s, c['id'])[0] for c in m.capabilities)
        counts_by[s.SHORT] = counts
        rows.append((s.NAME, getattr(s, "SHORT", ""), counts,
                     dict((n_, k) for n_, k, _ in s.LEVELS)))
    w('<p class="vd">The same %d capabilities and the same observations in every bar. '
      'Only the rule changes.</p>' % total)
    w(ch.scale_compare(rows, total))

    # ---- read the disagreement, from the numbers rather than from memory
    gated = [s for s in scales if _gates_on_practice(s)]
    ungated = [s for s in scales if not _gates_on_practice(s)]
    rated_by = {s.SHORT: total - counts_by[s.SHORT].get(None, 0) for s in scales}
    nothing = [s for s in scales if rated_by[s.SHORT] == 0]
    something = [s for s in scales if rated_by[s.SHORT] > 0]

    def names_(ss):
        ns = ["<b>%s</b>" % esc(s.NAME) for s in ss]
        return ns[0] if len(ns) == 1 else ", ".join(ns[:-1]) + " and " + ns[-1]

    if nothing and something and not demo:
        w('<div class="callout warn"><p><b>%s rate%s nothing today; %s rate%s %s.</b></p>'
          % (names_(nothing), "s" if len(nothing) == 1 else "",
             names_(something), "s" if len(something) == 1 else "",
             " and ".join("%d of %d" % (rated_by[s.SHORT], total) for s in something)))
        w('<p>That contrast <i>is</i> the finding of Section %d, shown a second way. '
          % S.number_of("The finding"))
        if gated:
            w('%s gate%s on <b>performance</b>: until someone is asked whether the work '
              'is done on real systems, %s return%s <b>not rated</b>. '
              % (names_(gated), "s" if len(gated) == 1 else "",
                 "it" if len(gated) == 1 else "they", "s" if len(gated) == 1 else ""))
        if ungated:
            w('%s do%s not gate &mdash; %s read%s whatever has been observed, so tooling '
              'and approved standards alone are enough to place a capability.</p>'
              % (names_(ungated), "es" if len(ungated) == 1 else "",
                 "it" if len(ungated) == 1 else "they", "s" if len(ungated) == 1 else ""))
            w('<p>Read %s carefully. Every level it shows rests on <b>enablers with no '
              'observed practice behind them</b>. It is exactly the reading this report '
              'exists to caution against, and it is shown here rather than hidden because '
              'someone will produce it otherwise.</p></div>'
              % ("that bar" if len(ungated) == 1 else "those bars"))
        else:
            w('</p></div>')
    elif not something and not demo:
        w('<div class="callout warn"><p><b>No scale rates anything today.</b> Every scale '
          'that ships gates on performance, and performance has not been observed for '
          'any capability.</p></div>')
    else:
        w('<div class="callout"><p><b>Where they disagree, the default scale is the '
          'finding.</b></p>')
        any_higher = False
        for s in scales:
            if s is default:
                continue
            both, agree, higher, lower = _agreement(m, default, s)
            if both == 0:
                w('<p><b>%s</b> and the default scale rate no capability in common%s.</p>'
                  % (esc(s.NAME),
                     " yet" if rated_by[s.SHORT] == 0 else ""))
                continue
            if agree is None:
                lo, hi = min(_derivable(s)), max(_derivable(s))
                dlo, dhi = min(_derivable(default)), max(_derivable(default))
                w('<p><b>%s</b> rates <b>%d</b> of the capabilities the default scale '
                  'rates, but its ladder runs %d&ndash;%d where the default runs '
                  '%d&ndash;%d today, so its numbers cannot be read against the '
                  'default\'s one for one. Compare the shape of its bar, not the '
                  'digits.</p>'
                  % (esc(s.NAME), both, lo, hi, dlo, dhi))
                continue
            any_higher = any_higher or bool(higher)
            w('<p><b>%s</b> agrees with the default scale on <b>%d of the %d</b> '
              'capabilities both scales rate%s.%s</p>'
              % (esc(s.NAME), agree, both,
                 ', reads <b>%d higher</b> and <b>%d lower</b>' % (higher, lower)
                 if (higher or lower) else '',
                 ' The remaining %d are rated by one scale and not the other.' % (total - both)
                 if total - both else ''))
        w('<p>A lens reading <i>higher</i> is the case to watch: it is a capability '
          'the Bank would be claiming on a coarser rule than the assessment applies. '
          'That is not an error &mdash; a lens is meant to be more forgiving &mdash; '
          'but it is not a reason to pick the friendlier number.</p></div>')

    # ---- the rule
    w('<p style="margin-top:18px"><b>The rule, stated once.</b> The default scale is '
      'the assessment. The others are lenses, useful for reporting into a frame a room '
      'already holds. Where a lens and the default scale disagree, <b>the default '
      'scale is the finding</b> &mdash; a lens is never the reason to claim a '
      'capability the Bank has not established.</p>')
    w('<p class="vd">Every scale is one file in <code>scales/</code>. Adding one adds '
      'a view automatically and changes no fact. The full rules, level definitions and '
      'provenance of each are in <code>scales/README.md</code>.</p>')
    w('</section>')
    return "\n".join(o)


STYLE = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI Capability &mdash; Management Report</title>
<style>
:root{--ink:#0d1b2a;--muted:#5a798c;--rule:#e2e8ee;--page:#fff;--card:#fff;
--accent:#002869;--accent-soft:#F1F5FA;--warn:#E36135;--good:#002869;--mid:#4C8CD2;
--band:#F7F9FB;--shadow:none;
--q1:#F7F9FB;--q2:#F1F5FA;--q3:#FBF3EF;--q4:#F7F9FB}
@media(prefers-color-scheme:dark){:root{--ink:#eef2f6;--muted:#93a7b8;--rule:#22303d;
--page:#0b1219;--card:#0f1822;--accent:#7FB2E8;--accent-soft:#12202e;--band:#0d1620;
--q1:#0f1822;--q2:#12202e;--q3:#1c1512;--q4:#0f1822;--shadow:none}}
*{box-sizing:border-box}
body{margin:0;background:var(--page);color:var(--ink);
font:14.5px/1.6 "Segoe UI",-apple-system,BlinkMacSystemFont,Inter,Helvetica,Arial,sans-serif;
-webkit-font-smoothing:antialiased}
.wrap{max-width:1060px;margin:0 auto;padding:0 40px 80px}
header{padding:44px 0 20px;margin-bottom:0}
.eyebrow{font-size:11px;letter-spacing:.14em;text-transform:uppercase;
color:var(--muted);font-weight:700;margin-bottom:12px}
h1{font-size:36px;line-height:1.1;margin:0 0 10px;letter-spacing:-.025em;
font-weight:700;max-width:34ch}
.sub{color:var(--muted);font-size:13px;border-top:2px solid var(--accent);
padding-top:12px;margin-top:18px}
h2{font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);
margin:0 0 6px;font-weight:700}
h3{font-size:23px;margin:0 0 16px;letter-spacing:-.02em;font-weight:700;max-width:42ch}
h3.minor{margin-top:30px;font-size:14px;max-width:none;letter-spacing:.02em}
section{background:var(--card);border:none;border-top:1px solid var(--rule);
border-radius:0;padding:40px 0 34px;margin:0}
section:first-of-type{border-top:2px solid var(--accent)}
p{margin:0 0 12px;max-width:76ch}
.lede{font-size:16.5px;line-height:1.5}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:0;
margin:24px 0 8px;border-top:1px solid var(--rule)}
.kpi{padding:18px 22px 16px;border-right:1px solid var(--rule);
border-bottom:1px solid var(--rule)}
.kpi:last-child{border-right:none}
.kpi b{display:block;font-size:34px;line-height:1;letter-spacing:-.03em;
font-weight:700;color:var(--accent)}
.kpi span{font-size:11px;color:var(--muted);display:block;margin-top:8px;
letter-spacing:.02em;line-height:1.35}
.kpi.warn b{color:var(--warn)}
.callout{background:var(--accent-soft);padding:22px 26px;margin:22px 0;
border-left:3px solid var(--accent)}
.callout.warn{border-left-color:var(--warn)}
.callout p:last-child{margin-bottom:0}
.callout b{font-size:17px;letter-spacing:-.01em}
table{width:100%;border-collapse:collapse;font-size:13px;margin:16px 0 4px}
th{text-align:left;font-size:10px;letter-spacing:.1em;text-transform:uppercase;
color:var(--muted);border-bottom:1.5px solid var(--accent);padding:0 12px 8px;
font-weight:700}
td{padding:11px 12px;border-bottom:1px solid var(--rule);vertical-align:top}
tbody tr:nth-child(even){background:var(--band)}
tr:last-child td{border-bottom:none}
td.c,th.c{text-align:center}
code{font:12.5px ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--page);
padding:1px 5px;border-radius:4px}
.chart{width:100%;height:auto;overflow:visible;margin:6px 0 2px}
.bl{font-size:12.5px;font-weight:600;fill:var(--ink)}
.bs{font-size:10.5px;fill:var(--muted)}
.bn{font-size:11px;font-weight:700;text-anchor:middle}
.bt{font-size:11.5px;fill:var(--muted);font-weight:600}
.legend{display:flex;gap:16px;flex-wrap:wrap;margin:12px 0 2px;font-size:12px;color:var(--muted)}
.legend i{display:inline-block;width:11px;height:11px;border-radius:3px;margin-right:6px;
vertical-align:-1px}
.split{display:grid;grid-template-columns:170px 1fr;gap:26px;align-items:center}
@media(max-width:640px){.split{grid-template-columns:1fr}}
.donut{width:150px;height:150px}
.pill{display:inline-block;font-size:10.5px;font-weight:700;padding:3px 9px;
letter-spacing:.04em;text-transform:uppercase}
.p-no{background:rgba(227,97,53,.14);color:#B8471F}
.p-mid{background:rgba(227,97,53,.14);color:#B8471F}
.p-yes{background:var(--accent-soft);color:var(--accent)}
.ch{font-size:9px;fill:var(--muted);font-weight:700;text-anchor:middle;
letter-spacing:.04em;text-transform:uppercase}
.dh{font-size:11px;fill:var(--accent);font-weight:700;letter-spacing:.06em;
text-transform:uppercase}
.cn{font-size:11.5px;fill:var(--ink)}
.ci{font-size:10px;fill:var(--muted);font-weight:600}
.empty{display:flex;gap:16px;align-items:flex-start;background:var(--page);
border:1px dashed var(--rule);border-radius:8px;padding:20px 22px;margin:12px 0}
.empty .ei{font-size:26px;color:var(--muted);line-height:1}
.empty b{font-size:14px}
.empty p{margin:4px 0 0;font-size:13px;color:var(--muted);max-width:64ch}
.empty p.who{margin-top:8px;font-size:12px;font-style:italic}
.waves{display:grid;grid-template-columns:repeat(auto-fit,minmax(228px,1fr));gap:16px;
margin-top:12px}
.wave{background:var(--page);border:1px solid var(--rule);border-radius:8px;padding:16px}
.wh{font-weight:700;font-size:14px;margin-bottom:2px}
.ws{font-size:11.5px;color:var(--muted);margin-bottom:10px}
.wave ul{margin:0;padding-left:16px;font-size:12.5px;line-height:1.6}
.wave li.more{color:var(--muted);list-style:none;margin-left:-16px}
.viewhdr{display:flex;justify-content:space-between;align-items:baseline;
gap:12px;margin:38px 0 6px;padding-top:26px;border-top:1px solid var(--rule)}
.viewhdr:first-of-type{border-top:none;padding-top:0;margin-top:10px}
.viewhdr h4{font-size:17px;margin:0;letter-spacing:-.015em;font-weight:700}
.tag{font-size:9.5px;font-weight:700;letter-spacing:.1em;padding:4px 10px;
white-space:nowrap;text-transform:uppercase}
.t-real{background:var(--accent);color:#fff}
.t-wait{background:transparent;color:var(--muted);box-shadow:inset 0 0 0 1px var(--rule)}
.vd{font-size:13.5px;color:var(--muted);margin:0 0 10px;max-width:78ch}
footer{color:var(--muted);font-size:12px;text-align:center;margin-top:34px;line-height:1.7}
.ax{font-size:11.5px;fill:var(--muted);font-weight:700;text-anchor:middle}
.axs{font-size:9.5px;fill:var(--muted)}
.axl{font-size:11.5px;fill:var(--muted);font-weight:600}
.axis{stroke:var(--rule);stroke-width:1.5}
.grid{fill:none;stroke:var(--rule);stroke-width:1}
.spoke{stroke:var(--rule);stroke-width:1}
.cur{fill:rgba(0,40,105,.26);stroke:#002869;stroke-width:2}
.tgt{fill:none;stroke:#E36135;stroke-width:2;stroke-dasharray:5 4}
.tl-now{fill:none;stroke:#002869;stroke-width:2.5}
.tl-then{fill:none;stroke:#E36135;stroke-width:2.5;stroke-dasharray:5 4}
.tp-now{fill:#002869} .tp-then{fill:#E36135}
.qq{font-size:11px;fill:var(--muted);font-weight:700;letter-spacing:.04em}
.wm{font-size:44px;font-weight:800;fill:var(--ink);fill-opacity:.04;
letter-spacing:.24em;pointer-events:none}
.lvn{font-size:11px;fill:var(--muted);font-weight:700}
.radar{max-width:470px;display:block;margin:0 auto}
.banner{position:sticky;top:0;z-index:9;background:var(--warn);color:#fff;
padding:10px 24px;font-size:12.5px;font-weight:600;text-align:center;
letter-spacing:.01em}
.smp{background:rgba(227,97,53,.12);padding:0 4px;border-radius:2px;
box-shadow:inset 0 -1px 0 rgba(227,97,53,.4)}
@media print{body{background:#fff}section{break-inside:avoid;box-shadow:none}
.wrap{padding:0}.banner{position:static}}
</style></head><body>"""

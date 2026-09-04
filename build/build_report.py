# -*- coding: utf-8 -*-
"""The management report as a self-contained HTML page.

No external assets, no JavaScript libraries, no build step beyond this file.
Charts are inline SVG computed from facts/, so the page cannot drift from the
model and works offline, in email, and from a file:// URL.

Design constraint that shapes everything here: THERE ARE NO SCORES YET. A heat
map of 52 unrated capabilities is one flat colour, and a current-vs-target gap
chart is empty. So this reports what is actually known - what is built, what is
owned, what is observed - and shows the absence of ratings as a finding rather
than hiding it behind an invented number.
"""
from datetime import date
import collections

C = {
    "yes": "#2f6f4e", "partial": "#c08a2e", "no": "#a33a2c",
    "n/a": "#9aa5ad", "unknown": "#dfe5ea",
}
LABEL = {"yes": "Yes", "partial": "Partial", "no": "No",
         "n/a": "Not applicable", "unknown": "Not observed"}
RELEASED = {"Published", "Published (JFrog)", "In use"}
ORDER = ["yes", "partial", "no", "n/a", "unknown"]


def _short(name):
    """Domain names, trimmed to fit the chart gutter."""
    n = name.replace("AI ", "", 1)
    return {"Governance, Risk, Security & Assurance": "Governance, Risk & Assurance"}.get(n, n)


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


# ----------------------------------------------------------------- charts
def stacked_bar(rows, width=880, rowh=30, gap=8, keys=ORDER):
    """rows: [(label, sublabel, {key: count})]. Horizontal 100% stacked bars."""
    left, right = 296, 62
    bw = width - left - right
    h = len(rows) * (rowh + gap)
    out = ['<svg viewBox="0 0 %d %d" role="img" class="chart">' % (width, h)]
    for i, (label, sub, counts) in enumerate(rows):
        y = i * (rowh + gap)
        total = sum(counts.values()) or 1
        out.append('<text x="0" y="%d" class="bl">%s</text>' % (y + 14, esc(label)))
        if sub:
            out.append('<text x="0" y="%d" class="bs">%s</text>' % (y + 26, esc(sub)))
        x = left
        for k in keys:
            n = counts.get(k, 0)
            if not n:
                continue
            w = bw * n / total
            out.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s">'
                       '<title>%s: %d</title></rect>'
                       % (x, y, w, rowh, C[k], LABEL[k], n))
            if w > 22:
                out.append('<text x="%.1f" y="%d" class="bn" fill="%s">%d</text>'
                           % (x + w / 2, y + rowh / 2 + 4,
                              "#fff" if k in ("yes", "no") else "#1a2126", n))
            x += w
        out.append('<text x="%d" y="%d" class="bt">%d</text>'
                   % (width - right + 10, y + rowh / 2 + 4, total))
    out.append("</svg>")
    return "".join(out)


def progress_rows(rows, width=880, rowh=26, gap=10):
    """rows: [(label, done, total, note)] - completeness bars."""
    left, right = 246, 88
    bw = width - left - right
    h = len(rows) * (rowh + gap)
    out = ['<svg viewBox="0 0 %d %d" role="img" class="chart">' % (width, h)]
    for i, (label, done, total, note) in enumerate(rows):
        y = i * (rowh + gap)
        frac = done / total if total else 0
        out.append('<text x="0" y="%d" class="bl">%s</text>' % (y + 13, esc(label)))
        if note:
            out.append('<text x="0" y="%d" class="bs">%s</text>' % (y + 24, esc(note)))
        out.append('<rect x="%d" y="%d" width="%d" height="%d" rx="3" fill="#e7ecf0"/>'
                   % (left, y, bw, rowh - 8))
        if frac:
            out.append('<rect x="%d" y="%d" width="%.1f" height="%d" rx="3" fill="%s"/>'
                       % (left, y, bw * frac, rowh - 8,
                          C["yes"] if frac == 1 else C["partial"]))
        out.append('<text x="%d" y="%d" class="bt">%d of %d</text>'
                   % (left + bw + 10, y + rowh / 2, done, total))
    out.append("</svg>")
    return "".join(out)


def donut(counts, size=150, keys=ORDER):
    """Single donut with a centre figure."""
    import math
    total = sum(counts.values()) or 1
    cx = cy = size / 2
    r, sw = size / 2 - 14, 22
    out = ['<svg viewBox="0 0 %d %d" class="donut" role="img">' % (size, size)]
    a = -math.pi / 2
    for k in keys:
        n = counts.get(k, 0)
        if not n:
            continue
        sweep = 2 * math.pi * n / total
        x1, y1 = cx + r * math.cos(a), cy + r * math.sin(a)
        a += sweep
        x2, y2 = cx + r * math.cos(a), cy + r * math.sin(a)
        large = 1 if sweep > math.pi else 0
        out.append('<path d="M %.2f %.2f A %.2f %.2f 0 %d 1 %.2f %.2f" fill="none" '
                   'stroke="%s" stroke-width="%d"><title>%s: %d</title></path>'
                   % (x1, y1, r, r, large, x2, y2, C[k], sw, LABEL[k], n))
    out.append("</svg>")
    return "".join(out)


def legend(keys=ORDER):
    return ('<div class="legend">' + "".join(
        '<span><i style="background:%s"></i>%s</span>' % (C[k], LABEL[k])
        for k in keys) + "</div>")


# ----------------------------------------------------------------- page
def report(m, scale):
    total = len(m.capabilities)
    rated = {c['id']: m.rate(scale, c['id']) for c in m.capabilities}
    n_rated = sum(1 for v in rated.values() if v[0] is not None)
    pending = [a for a in m.assets if a['status'] not in RELEASED]
    noowner = [c for c in m.capabilities if m.owner(c['id'])[1] == 'NO MATCH']
    box_total = sum(len(o['in_the_box']) for o in m.offerings)
    box_done = sum(1 for o in m.offerings for x in o['in_the_box'] if x['status'])
    n_obs = total * len(m.observation_types)
    n_known = sum(1 for c in m.capabilities
                  for v in m.values(c['id']).values() if v != 'unknown')

    o = []
    w = o.append
    w("""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI Capability &mdash; Management Report</title>
<style>
:root{--ink:#101619;--muted:#5d6b74;--rule:#dde3e8;--page:#f4f6f8;--card:#fff;
--accent:#12455c;--accent-soft:#e4eef3;--warn:#a33a2c;--good:#2f6f4e;--mid:#c08a2e;
--shadow:0 1px 2px rgba(16,22,25,.05),0 8px 24px rgba(16,22,25,.06)}
@media(prefers-color-scheme:dark){:root{--ink:#eef2f4;--muted:#9aa7b0;--rule:#2a3138;
--page:#0d1114;--card:#151b20;--accent:#7fb8c9;--accent-soft:#16303c;
--shadow:0 1px 2px rgba(0,0,0,.5),0 8px 24px rgba(0,0,0,.35)}}
*{box-sizing:border-box}
body{margin:0;background:var(--page);color:var(--ink);
font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Arial,sans-serif;
-webkit-font-smoothing:antialiased}
.wrap{max-width:1000px;margin:0 auto;padding:40px 24px 72px}
header{border-bottom:3px solid var(--accent);padding-bottom:18px;margin-bottom:30px}
h1{font-size:30px;line-height:1.15;margin:0 0 6px;letter-spacing:-.02em}
.sub{color:var(--muted);font-size:13.5px}
h2{font-size:12px;letter-spacing:.09em;text-transform:uppercase;color:var(--accent);
margin:0 0 4px;font-weight:700}
h3{font-size:19px;margin:0 0 14px;letter-spacing:-.01em}
section{background:var(--card);border:1px solid var(--rule);border-radius:10px;
padding:26px 28px;margin-bottom:20px;box-shadow:var(--shadow)}
p{margin:0 0 12px;max-width:76ch}
.lede{font-size:16.5px;line-height:1.5}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px;margin:18px 0 4px}
.kpi{background:var(--page);border:1px solid var(--rule);border-radius:8px;padding:14px 16px}
.kpi b{display:block;font-size:27px;line-height:1.1;letter-spacing:-.02em}
.kpi span{font-size:12px;color:var(--muted);display:block;margin-top:3px}
.kpi.warn b{color:var(--warn)} .kpi.good b{color:var(--good)} .kpi.mid b{color:var(--mid)}
.callout{border-left:4px solid var(--accent);background:var(--accent-soft);
padding:16px 20px;border-radius:0 8px 8px 0;margin:18px 0}
.callout.warn{border-left-color:var(--warn);background:rgba(163,58,44,.08)}
.callout p:last-child{margin-bottom:0}
.callout b{font-size:16px}
table{width:100%;border-collapse:collapse;font-size:13.5px;margin:14px 0 4px}
th{text-align:left;font-size:11px;letter-spacing:.06em;text-transform:uppercase;
color:var(--muted);border-bottom:2px solid var(--rule);padding:8px 10px 7px}
td{padding:9px 10px;border-bottom:1px solid var(--rule);vertical-align:top}
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
.pill{display:inline-block;font-size:11px;font-weight:700;padding:2px 8px;border-radius:20px}
.p-no{background:rgba(163,58,44,.13);color:var(--warn)}
.p-mid{background:rgba(192,138,46,.16);color:#8a6110}
.p-yes{background:rgba(47,111,78,.14);color:var(--good)}
footer{color:var(--muted);font-size:12px;text-align:center;margin-top:34px;line-height:1.7}
@media print{body{background:#fff}section{break-inside:avoid;box-shadow:none}.wrap{padding:0}}
</style></head><body><div class="wrap">""")

    # ---------------------------------------------------------- header
    w('<header><h1>AI Capability &mdash; Management Report</h1>'
      '<div class="sub">Inter-American Development Bank &nbsp;·&nbsp; %s '
      '&nbsp;·&nbsp; generated from the capability model</div></header>'
      % date.today().strftime("%d %B %Y"))

    # ---------------------------------------------------------- 1 coverage
    w('<section><h2>Section 1</h2><h3>What this report can and cannot say</h3>')
    w('<p class="lede">Read this before the findings. It states how much of the '
      'assessment has actually been done, so nothing below is read as more than it is.</p>')
    w('<div class="kpis">')
    w('<div class="kpi good"><b>%d</b><span>Platform offerings, evidenced</span></div>' % len(m.offerings))
    w('<div class="kpi good"><b>%d</b><span>Assets with a location</span></div>' % len(m.assets))
    w('<div class="kpi mid"><b>%d%%</b><span>Observations recorded</span></div>'
      % (100 * n_known // n_obs))
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
    # coverage by domain
    rows = []
    for d in m.domains:
        caps = [c for c in m.capabilities if c['domain'] == d['id']]
        cnt = collections.Counter()
        for c in caps:
            for v in m.values(c['id']).values():
                cnt["unknown" if v == "unknown" else "yes"] += 1
        rows.append(("%s · %s" % (d['id'], _short(d['name'])),
                     "%d capabilities" % len(caps),
                     {"yes": cnt["yes"], "unknown": cnt["unknown"]}))
    w('<h3 style="margin-top:26px;font-size:15px">How much has been observed, by domain</h3>')
    w(stacked_bar(rows, keys=["yes", "unknown"]))
    w('<div class="legend"><span><i style="background:%s"></i>Observed, with evidence</span>'
      '<span><i style="background:%s"></i>Nobody has looked yet</span></div>'
      % (C["yes"], C["unknown"]))
    w('</section>')

    # ---------------------------------------------------------- 2 what exists
    w('<section><h2>Section 2</h2><h3>What the institution has built</h3>')
    w('<p>Every row is backed by a named asset with a status and a location. '
      'This is the part of the picture that is <b>not</b> an opinion.</p>')
    w(progress_rows([(x['name'],
                      x['assets_released'], x['assets_total'],
                      "enables " + ", ".join(x['enables']))
                     for x in m.offerings]))
    ready = [x for x in m.offerings if x['assets_released'] == x['assets_total']]
    w('<p style="margin-top:16px"><b>%d of %d offerings are complete.</b> The others are '
      'waiting on named documents or modules, listed in section 4.</p>'
      % (len(ready), len(m.offerings)))
    # enablement by domain
    w('<h3 style="margin-top:26px;font-size:15px">Can a team get the tooling? By domain</h3>')
    rows = []
    for d in m.domains:
        caps = [c for c in m.capabilities if c['domain'] == d['id']]
        cnt = collections.Counter(m.values(c['id'])['enabled'] for c in caps)
        rows.append(("%s · %s" % (d['id'], _short(d['name'])),
                     "", dict(cnt)))
    w(stacked_bar(rows))
    w(legend())
    w('<p style="margin-top:14px"><i>Not applicable</i> is a legitimate answer, not a gap: '
      'a strategy or workforce capability is not worse for having no platform component. '
      'The shape to notice is that the platform and engineering domains carry the tooling, '
      'and the governance domains carry almost none.</p>')
    w('</section>')

    # ---------------------------------------------------------- 3 finding
    w('<section><h2>Section 3</h2><h3>The finding</h3>')
    w('<div class="callout"><p><b>The institution has built its enablers ahead of its '
      'practice.</b></p></div>')
    w('<p>The scale used here places <b>performance</b> at Level 1, <b>tooling and '
      'competent people</b> at Level 2, and <b>an approved standard, applied</b> at '
      'Level 3. Measured that way, a large part of the Level 2 and Level 3 apparatus '
      'exists &mdash; platforms, standards, reference architectures, infrastructure '
      'modules &mdash; while Level 1, whether the work is actually done, has never been '
      'examined.</p>')
    w('<p>That is not a criticism of the build. It explains a disagreement that recurs '
      'here: one person says a capability exists, meaning the platform and the standard '
      'exist; another says it does not, meaning nothing is running on it. '
      '<b>Both are right about different things.</b> A model carrying a single number '
      'cannot show that. This one shows it as four columns.</p>')
    w('<table><thead><tr><th>What can be evidenced today</th>'
      '<th>What cannot</th></tr></thead><tbody>')
    for a, b in [("%d offerings and %d assets, with locations" % (len(m.offerings), len(m.assets)),
                  "Whether any of it is used in production"),
                 ("Which capabilities have an approved standard",
                  "Whether the work is done against it"),
                 ("Which capabilities have no tooling and no reason recorded",
                  "Whether the people who need the skills have them")]:
        w('<tr><td>%s</td><td style="color:var(--muted)">%s</td></tr>' % (esc(a), esc(b)))
    w('</tbody></table></section>')

    # ---------------------------------------------------------- 4 decisions
    w('<section><h2>Section 4</h2><h3>What needs a decision</h3>')

    w('<h3 style="font-size:15px;margin-top:8px">4.1 &nbsp;Capabilities nobody owns</h3>')
    w('<div class="split"><div>%s<div style="text-align:center;font-size:12px;'
      'color:var(--muted);margin-top:6px">%d of %d unowned</div></div><div>'
      % (donut({"no": len(noowner), "yes": total - len(noowner)}, keys=["no", "yes"]),
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

    w('<h3 style="font-size:15px;margin-top:28px">4.2 &nbsp;Finished, but not released</h3>')
    w('<p>%d assets exist and are not yet available to delivery teams. Each is days from '
      'being usable, and each currently holds a capability below what the underlying work '
      'would support.</p>' % len(pending))
    w('<table><thead><tr><th>Asset</th><th>What it is</th><th>Status</th></tr></thead><tbody>')
    for a in pending:
        w('<tr><td><code>%s</code></td><td>%s</td>'
          '<td><span class="pill p-mid">%s</span></td></tr>'
          % (a['id'], esc(a['name']), esc(a['status'])))
    w('</tbody></table>')
    w('<p><b>Decision required:</b> a release date for each, with a named owner.</p>')

    w('<h3 style="font-size:15px;margin-top:28px">4.3 &nbsp;Questions only the platform '
      'teams can answer</h3>')
    w('<p><b>%d of %d answered.</b> These decide whether a delivery team inherits its '
      'controls or rebuilds them. Every unanswered row is an unknown; every <i>no</i> is '
      'a roadmap item, usually a cheap one, because it means extending a module rather '
      'than building a platform.</p>' % (box_done, box_total))
    w(progress_rows([(x['name'],
                      sum(1 for y in x['in_the_box'] if y['status']),
                      len(x['in_the_box']), "")
                     for x in m.offerings if x['in_the_box']]))
    w('</section>')

    # ---------------------------------------------------------- 5 next
    w('<section><h2>Section 5</h2><h3>What would make the next report say more</h3>')
    w('<table><thead><tr><th>Who</th><th>What is asked of them</th>'
      '<th>What it unlocks</th></tr></thead><tbody>')
    n_undef = sum(1 for c in m.capabilities if m.values(c['id'])['defined'] == 'unknown')
    for who, what, why in [
        ("Capability owners",
         "For each capability they own: is this done on real AI systems, and where?",
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
      '%d criteria.<br>Scale: %s. %s<br>Every figure traces to a recorded fact with '
      'evidence and a date; nothing here is estimated.</footer>'
      % (len(m.domains), total, sum(len(c['criteria']) for c in m.capabilities),
         esc(scale.NAME), esc(scale.BASIS)))
    w('</div></body></html>')
    return "\n".join(o)

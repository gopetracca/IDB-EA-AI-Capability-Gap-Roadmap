# -*- coding: utf-8 -*-
"""Inline-SVG chart primitives shared by the HTML report and its illustrative
edition.  One palette, one escaper, one legend - defined here and nowhere else.

Every chart takes the model (or values already read from it) and returns a
string of SVG or HTML.  Nothing here reads facts/ and nothing here knows which
scale is in use: level ranges are passed in by the caller.

Palette: a monochrome navy ramp with a single warm accent for the one thing
that needs attention.  Consultancy decks do not use traffic lights - a red/
amber/green wall reads as alarm rather than as information, and it does not
survive being printed in grey.
"""
import math
import collections

C = {
    "yes": "#002869",      # deep navy - present
    "partial": "#4C8CD2",  # mid blue - partial
    "no": "#E36135",       # the single accent - absent, and the thing to act on
    "n/a": "#C9D2DA",      # grey - does not apply
    "unknown": "#EDF1F4",  # palest - nobody has looked
}
LABEL = {"yes": "Yes", "partial": "Partial", "no": "No",
         "n/a": "Not applicable", "unknown": "Not observed"}
ORDER = ["yes", "partial", "no", "n/a", "unknown"]
# level colours: darker with height, so 'more' reads as 'further along'
LVL = {0: "#E36135", 1: "#9BB8DC", 2: "#4C8CD2", 3: "#0057AF",
       4: "#002869", 5: "#001B45", None: "#EDF1F4"}
RAMP = ["#EDF1F4", "#C6D5E6", "#8FB2D8", "#4C8CD2", "#1C5BA8", "#002869", "#001B45"]


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def short_domain(name):
    """Domain names, trimmed to fit a chart gutter."""
    n = name.replace("AI ", "", 1)
    return {"Governance, Risk, Security & Assurance":
            "Governance, Risk & Assurance"}.get(n, n)


def domain_label(d):
    return "%s · %s" % (d['id'], short_domain(d['name']))


def level_keys(scale):
    """The levels a chart should show for a scale: those it can actually derive.
    Showing levels above DERIVABLE_MAX would advertise colours the chart can
    never contain."""
    cap = getattr(scale, "DERIVABLE_MAX", None)
    return [n for n, _, _ in scale.LEVELS if cap is None or n <= cap]


def level_labels(scale):
    return dict((n, "%d %s" % (n, k)) for n, k, _ in scale.LEVELS)


def legend(keys=ORDER, labels=None, cols=None):
    labels = labels or LABEL
    cols = cols or C
    return ('<div class="legend">' + "".join(
        '<span><i style="background:%s"></i>%s</span>' % (cols[k], labels[k])
        for k in keys) + "</div>")


def wm(w, h, text="SAMPLE"):
    """Watermark behind a chart drawn from sample values."""
    return ('<text x="%d" y="%d" class="wm" text-anchor="middle">%s</text>'
             % (w / 2, h / 2 + 12, text))


def empty_state(title, missing, who):
    """Honest empty state for a view that has nothing to draw yet."""
    return ('<div class="empty"><div class="ei">&#9633;</div>'
            '<div><b>%s</b><p>%s</p><p class="who">Supplied by: %s</p></div></div>'
            % (esc(title), esc(missing), esc(who)))


# ------------------------------------------------------------- bars and rings
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


def scale_compare(rows, total, width=880, rowh=34, gap=14):
    """rows: [(scale_name, basis, {level_or_None: count}, level_names)].

    One horizontal bar per scale over the SAME capabilities, so the reader can
    see where the choice of instrument changes the answer.  Not-rated is drawn
    in the palest tone at the right, deliberately not as a zero.
    """
    left, right = 236, 74
    bw = width - left - right
    h = len(rows) * (rowh + gap)
    out = ['<svg viewBox="0 0 %d %d" role="img" class="chart">' % (width, h)]
    for i, (name, basis, counts, names) in enumerate(rows):
        y = i * (rowh + gap)
        out.append('<text x="0" y="%d" class="bl">%s</text>' % (y + 14, esc(name)))
        if basis:
            out.append('<text x="0" y="%d" class="bs">%s</text>' % (y + 26, esc(basis)))
        x = left
        keys = sorted([k for k in counts if k is not None])
        if None in counts:
            keys.append(None)
        for k in keys:
            n = counts.get(k, 0)
            if not n:
                continue
            w = bw * n / (total or 1)
            col = "#F4F6F8" if k is None else RAMP[min(k, len(RAMP) - 1)]
            lab = "Not rated" if k is None else "%d %s" % (k, names.get(k, ""))
            out.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s" '
                       'stroke="#fff" stroke-width="1"><title>%s: %d</title></rect>'
                       % (x, y, w, rowh, col, esc(lab), n))
            if w > 26:
                dark = (k is None) or k <= 2
                out.append('<text x="%.1f" y="%d" class="bn" fill="%s">%d</text>'
                           % (x + w / 2, y + rowh / 2 + 4,
                              "#1a2126" if dark else "#fff", n))
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


# ------------------------------------------------------ views from real facts
# Heat-map geometry, shared by every observation map so that the combined map
# and the one-per-observation maps render at the same text size and their
# cells line up under one another.
HM_PAD, HM_ROW, HM_GAP, HM_COL, HM_CW, HM_RIGHT = 388, 19, 3, 66, 24, 30


def _hm_width(m):
    """One viewBox width for all heat maps drawn from this model."""
    maxcrit = max(len(c['criteria']) for c in m.capabilities)
    ncols = len(m.observation_types)
    body = max(HM_COL * ncols, HM_COL + 14 + maxcrit * (HM_CW + 2))
    return HM_PAD + body + HM_RIGHT


def _hm_summary(d, caps, cells, unit):
    """The <summary> of one collapsed domain: its name, a count, and a small
    count-per-value bar.  A distribution of the cells drawn beneath it - never
    a rolled-up domain colour, which would need an average of ordinals
    (docs/the-discipline.md section 6.4)."""
    cnt = collections.Counter(cells)
    total = sum(cnt.values()) or 1
    bar = "".join('<i style="width:%.1f%%;background:%s" title="%s: %d"></i>'
                  % (100.0 * cnt[k] / total, C[k], LABEL[k], cnt[k])
                  for k in ORDER if cnt[k])
    return ('<summary><span class="hmd">%s &#183; %s</span>'
            '<span class="hms">%d capabilities%s</span>'
            '<span class="mini" title="%d %s">%s</span></summary>'
            % (d['id'], esc(short_domain(d['name'])), len(caps),
               "" if unit == "capabilities" else " &#183; %d %s" % (total, unit),
               total, unit, bar))


def _hm_title(c, t, row):
    """Tooltip for one cell: what was seen, not just the value."""
    v = row.get('value', 'unknown')
    seen = (row.get('evidence') or row.get('basis') or "").strip()
    if len(seen) > 160:
        seen = seen[:159].rstrip() + "…"
    return "%s %s &#8212; %s: %s%s" % (
        c['id'], esc(c['name']), t, LABEL[v],
        (" &#8212; " + esc(seen)) if seen else "")


def obs_heatmap(m, types=None, criteria=False):
    """Every capability by name, with its observations, one collapsible block
    per domain.

    Rows are capabilities, not a grid of ids. A 9-wide grid cannot show a name
    that averages 33 characters, and `2.3` tells a reader nothing - the point of
    a heat map is that you can see what is weak without a lookup table.

    types:    the observation types to draw as columns; default all of them,
              which is the combined map.
    criteria: for a type observed per L3 criterion, also draw one small cell
              per criterion beside the rolled-up one, so the roll-up rule
              (ADR-0014) is visible rather than hidden inside a single colour.

    Each domain is a native <details> element, so the map collapses at L1 with
    no script; the controls at the top need the two-line helper in the page
    head and do nothing without it.
    """
    types = [t['id'] for t in (types or m.observation_types)]
    W = _hm_width(m)
    pad, rowh, gap, colw, cw = HM_PAD, HM_ROW, HM_GAP, HM_COL, HM_CW
    crit_types = [t for t in types if criteria and t in m.criterion_types]
    unit = "criteria" if crit_types else "capabilities"
    rows = [(d, sorted([c for c in m.capabilities if c['domain'] == d['id']],
                       key=lambda x: m.sort_key(x['id']))) for d in m.domains]
    o = ['<div class="hm"><div class="hmctl">'
         '<button type="button" onclick="hmAll(this,true)">Expand all</button>'
         '<button type="button" onclick="hmAll(this,false)">Collapse all</button>'
         '</div>']
    # column headers, once, in an SVG of the same width so they sit over the cells
    o.append('<svg viewBox="0 0 %d 22" class="chart hmh">' % W)
    for k, t in enumerate(types):
        o.append('<text x="%.1f" y="16" class="ch">%s%s</text>'
                 % (pad + k * colw + (colw - 4) / 2, esc(t.title()),
                    " (rolled up)" if t in crit_types else ""))
    if crit_types:
        x0 = pad + len(types) * colw + 14
        maxcrit = max(len(c['criteria']) for c in m.capabilities)
        o.append('<text x="%.1f" y="16" class="ch">By L3 criterion</text>'
                 % (x0 + maxcrit * (cw + 2) / 2))
    o.append('</svg>')
    for d, caps in rows:
        cells = []
        h = len(caps) * (rowh + gap) + 6
        body = ['<svg viewBox="0 0 %d %d" class="chart">' % (W, h)]
        y = 4
        for c in caps:
            v = m.values(c['id'])
            nm = c['name']
            if len(nm) > 44:
                nm = nm[:43].rstrip(" ,&") + "…"
            body.append('<text x="14" y="%d" class="cn">%s<title>%s</title></text>'
                        % (y + 13, esc(nm), esc(c['name'])))
            body.append('<text x="%d" y="%d" class="ci" text-anchor="end">%s</text>'
                        % (pad - 14, y + 13, c['id']))
            for k, t in enumerate(types):
                x = pad + k * colw
                row = {} if t in m.criterion_types else m.cap_obs(c['id'], t)
                row = dict(row, value=v[t])
                body.append('<rect x="%.1f" y="%d" width="%d" height="%d" fill="%s">'
                            '<title>%s</title></rect>'
                            % (x, y, colw - 4, rowh, C[v[t]], _hm_title(c, t, row)))
                if t not in crit_types:
                    cells.append(v[t])
            for t in crit_types:
                x = pad + len(types) * colw + 14
                for j, (crit, row) in enumerate(m.criteria_obs(c['id'], t)):
                    cv = row.get('value', 'unknown')
                    cells.append(cv)
                    body.append('<rect x="%.1f" y="%d" width="%d" height="%d" fill="%s">'
                                '<title>%s</title></rect>'
                                % (x + j * (cw + 2), y, cw, rowh, C[cv],
                                   _hm_title(crit, t, row)))
            y += rowh + gap
        body.append('</svg>')
        o.append('<details class="dom" open>%s%s</details>'
                 % (_hm_summary(d, caps, cells, unit), "".join(body)))
    o.append('</div>')
    return "".join(o)


def owners_chart(m):
    """Accountability spread: capabilities per Bank unit. Real data."""
    cnt = collections.Counter(m.owner(c['id'])[0] or "NO OWNER"
                              for c in m.capabilities)
    rows = cnt.most_common()
    W, rowh, gap, left, right = 880, 22, 8, 268, 58
    bw = W - left - right
    mx = max(cnt.values())
    h = len(rows) * (rowh + gap)
    o = ['<svg viewBox="0 0 %d %d" class="chart">' % (W, h)]
    for i, (unit, n) in enumerate(rows):
        y = i * (rowh + gap)
        col = "#a33a2c" if unit == "NO OWNER" else "#12455c"
        o.append('<text x="0" y="%d" class="bl" fill="%s">%s</text>'
                 % (y + 14, col, esc(unit)))
        o.append('<rect x="%d" y="%d" width="%.1f" height="%d" rx="3" fill="%s" '
                 'fill-opacity="%s"/>'
                 % (left, y, bw * n / mx, rowh - 6, col,
                    "1" if unit == "NO OWNER" else ".8"))
        o.append('<text x="%.1f" y="%d" class="bt">%d</text>'
                 % (left + bw * n / mx + 8, y + rowh / 2 + 2, n))
    o.append("</svg>")
    return "".join(o)


def waves_chart(m):
    """Roadmap horizons, assembled from facts. Real data."""
    waves = [
        ("Now &mdash; this quarter", "Release what is already built",
         ["%s %s" % (a['id'], esc(a['name'])) for a in m.pending_assets()]),
        ("Next &mdash; 6 months", "Answer what comes in the box, then close the gaps",
         ["%s &mdash; %d questions" % (esc(o_['name']), len(o_['in_the_box']))
          for o_ in m.offerings if o_['in_the_box']]),
        ("Later &mdash; 12 months+", "Capabilities nobody owns today",
         ["%s %s" % (c['id'], esc(c['name'])) for c in m.capabilities
          if m.owner(c['id'])[1] == "NO MATCH"]),
    ]
    o = ['<div class="waves">']
    for title, sub, items in waves:
        o.append('<div class="wave"><div class="wh">%s</div><div class="ws">%s</div><ul>'
                 % (title, esc(sub)))
        for it in items[:8]:
            o.append("<li>%s</li>" % it)
        if len(items) > 8:
            o.append('<li class="more">+ %d more</li>' % (len(items) - 8))
        o.append("</ul></div>")
    o.append("</div>")
    return "".join(o)


# ------------------------------------------- views that need a derived level
# `levels` is {cid: level or None}; `top` is the highest level the scale can
# derive, so the axes fit the instrument rather than assuming a ladder.
def v_heatmap(m, obs, levels, top):
    """52 capabilities BY NAME, coloured by derived level."""
    rowh, gap, pad, hdr = 19, 3, 388, 30
    barw = 300
    rows = [(d, sorted([c for c in m.capabilities if c['domain'] == d['id']],
                       key=lambda x: m.sort_key(x['id']))) for d in m.domains]
    W = pad + barw + 96
    H = hdr + sum(len(c) * (rowh + gap) + 26 for _, c in rows)
    o = ['<svg viewBox="0 0 %d %d" class="chart">' % (W, H)]
    o.append('<text x="%d" y="16" class="ch">Level</text>' % (pad + 4))
    y = hdr
    for d, caps in rows:
        o.append('<text x="0" y="%d" class="dh">%s &#183; %s</text>'
                 % (y + 12, d['id'], esc(short_domain(d['name']))))
        y += 22
        for c in caps:
            lv = levels.get(c['id'])
            nm = c['name']
            if len(nm) > 44:
                nm = nm[:43].rstrip(" ,&") + "…"
            o.append('<text x="14" y="%d" class="cn">%s</text>' % (y + 13, esc(nm)))
            o.append('<text x="%d" y="%d" class="ci" text-anchor="end">%s</text>'
                     % (pad - 14, y + 13, c['id']))
            # a bar whose length is the level, so the eye reads magnitude not hue alone
            frac = 0 if lv is None else max(lv, 0.12) / float(top or 1)
            o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="#EDF1F4"/>'
                     % (pad, y, barw, rowh))
            if lv is not None:
                o.append('<rect x="%d" y="%d" width="%.1f" height="%d" fill="%s">'
                         '<title>%s %s &#8212; level %d</title></rect>'
                         % (pad, y, barw * frac, rowh, LVL[lv],
                            c['id'], esc(c['name']), lv))
                o.append('<text x="%d" y="%d" class="lvn">%d</text>'
                         % (pad + barw + 10, y + 13, lv))
            else:
                o.append('<text x="%d" y="%d" class="lvn">&#8212;</text>'
                         % (pad + barw + 10, y + 13))
            y += rowh + gap
        y += 4
    o.append(wm(W, H))
    o.append("</svg>")
    return "".join(o)


def v_radar(m, obs, levels, targets, top):
    """Domain scorecard: current vs target, one axis per domain."""
    size, cx, cy, R = 420, 210, 205, 140
    doms = m.domains
    n = len(doms)

    def pts(vals):
        p = []
        for i, v in enumerate(vals):
            a = -math.pi / 2 + 2 * math.pi * i / n
            r = R * (v / float(top or 1))
            p.append("%.1f,%.1f" % (cx + r * math.cos(a), cy + r * math.sin(a)))
        return " ".join(p)
    cur, tgt = [], []
    for d in doms:
        caps = [c for c in m.capabilities if c['domain'] == d['id']]
        lv = [levels[c['id']] for c in caps if levels.get(c['id']) is not None]
        cur.append(sum(lv) / len(lv) if lv else 0)
        tg = [targets[c['id']] for c in caps]
        tgt.append(sum(tg) / len(tg) if tg else 0)
    o = ['<svg viewBox="0 0 %d %d" class="chart radar">' % (size, size + 24)]
    for ring in range(1, (top or 1) + 1):
        o.append('<polygon points="%s" class="grid"/>' % pts([ring] * n))
    for i, d in enumerate(doms):
        a = -math.pi / 2 + 2 * math.pi * i / n
        o.append('<line x1="%d" y1="%d" x2="%.1f" y2="%.1f" class="spoke"/>'
                 % (cx, cy, cx + R * math.cos(a), cy + R * math.sin(a)))
        lx, ly = cx + (R + 26) * math.cos(a), cy + (R + 26) * math.sin(a)
        anchor = ("middle" if abs(math.cos(a)) < .3
                  else ("start" if math.cos(a) > 0 else "end"))
        o.append('<text x="%.1f" y="%.1f" class="ax" text-anchor="%s">%s</text>'
                 % (lx, ly, anchor, d['id']))
        o.append('<text x="%.1f" y="%.1f" class="axs" text-anchor="%s">%s</text>'
                 % (lx, ly + 11, anchor, esc(d['name'].replace("AI ", "", 1)[:16])))
    o.append('<polygon points="%s" class="tgt"/>' % pts(tgt))
    o.append('<polygon points="%s" class="cur"/>' % pts(cur))
    o.append(wm(size, size))
    o.append("</svg>")
    return "".join(o)


def v_quadrant(m, obs, levels):
    """Built vs done: enablement on x, practice on y."""
    W, H, pad = 620, 420, 62
    PW, PH = W - pad * 2, H - pad * 2
    # position within the plot: low / mid / high, inset so nothing touches an edge
    POS = {"no": .16, "partial": .5, "yes": .86, "n/a": .5, "unknown": .5}
    o = ['<svg viewBox="0 0 %d %d" class="chart">' % (W, H)]
    for qx, qy, fill in ((0, 0, "var(--q1)"), (1, 0, "var(--q2)"),
                         (0, 1, "var(--q3)"), (1, 1, "var(--q4)")):
        o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>'
                 % (pad + qx * PW / 2, pad + qy * PH / 2, PW / 2, PH / 2, fill))
    o.append('<text x="%.1f" y="%d" class="qq" text-anchor="middle">'
             'Practised, not enabled</text>' % (pad + PW / 4, pad - 12))
    o.append('<text x="%.1f" y="%d" class="qq" text-anchor="middle">Healthy</text>'
             % (pad + PW * 3 / 4, pad - 12))
    o.append('<text x="%.1f" y="%d" class="qq" text-anchor="middle">Neither</text>'
             % (pad + PW / 4, H - pad + 34))
    o.append('<text x="%.1f" y="%d" class="qq" text-anchor="middle">'
             'Built, not practised</text>' % (pad + PW * 3 / 4, H - pad + 34))
    # spread overlapping dots deterministically instead of randomly
    buckets = {}
    for c in m.capabilities:
        v = obs[c['id']]
        buckets.setdefault((v['enabled'], v['practised']), []).append(c)
    for (en, pr), caps in sorted(buckets.items()):
        bx = pad + POS[en] * PW
        by = H - pad - POS[pr] * PH
        n = len(caps)
        cols = max(1, int(math.ceil(math.sqrt(n))))
        for k, c in enumerate(sorted(caps, key=lambda x: m.sort_key(x['id']))):
            dx = ((k % cols) - (cols - 1) / 2) * 15
            dy = ((k // cols) - ((n - 1) // cols) / 2) * 15
            lv = levels.get(c['id'])
            o.append('<circle cx="%.1f" cy="%.1f" r="6.5" fill="%s" fill-opacity=".9" '
                     'stroke="#fff" stroke-width="1.3"><title>%s %s &#8212; '
                     'enabled %s, practised %s</title></circle>'
                     % (bx + dx, by + dy, LVL[lv], c['id'], esc(c['name']), en, pr))
    o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" class="axis"/>'
             % (pad, H - pad, W - pad, H - pad))
    o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" class="axis"/>'
             % (pad, pad, pad, H - pad))
    for i, lab in enumerate(("no", "partial", "yes")):
        o.append('<text x="%.1f" y="%d" class="axs" text-anchor="middle">%s</text>'
                 % (pad + [.16, .5, .86][i] * PW, H - pad + 16, lab))
        o.append('<text x="%d" y="%.1f" class="axs" text-anchor="end">%s</text>'
                 % (pad - 8, H - pad - [.16, .5, .86][i] * PH + 4, lab))
    o.append('<text x="%d" y="%d" class="axl" text-anchor="middle">'
             'Enabled &#8594;</text>' % (W / 2, H - 12))
    o.append('<text x="16" y="%d" class="axl" text-anchor="middle" '
             'transform="rotate(-90 16 %d)">Practised &#8594;</text>'
             % (H / 2, H / 2))
    o.append(wm(W, H))
    o.append("</svg>")
    return "".join(o)


def v_gapbars(m, obs, levels, targets, top):
    """Biggest gaps to target, ranked."""
    gaps = sorted(((targets[c['id']] - (levels.get(c['id']) or 0), c)
                   for c in m.capabilities), key=lambda t: -t[0])[:12]
    W, rowh, gap, left, right = 880, 24, 9, 300, 70
    bw = W - left - right
    h = len(gaps) * (rowh + gap)
    o = ['<svg viewBox="0 0 %d %d" class="chart">' % (W, h)]
    for i, (g, c) in enumerate(gaps):
        y = i * (rowh + gap)
        cur = levels.get(c['id']) or 0
        o.append('<text x="0" y="%d" class="bl">%s %s</text>'
                 % (y + 12, c['id'], esc(c['name'][:38])))
        o.append('<text x="0" y="%d" class="bs">%s</text>'
                 % (y + 22, esc((m.owner(c['id'])[0] or "no owner")[:36])))
        unit = bw / float(top or 1)
        # solid navy = where it is now; hatched accent = the distance to target
        o.append('<rect x="%d" y="%d" width="%.1f" height="%d" rx="3" fill="#EDF1F4"/>'
                 % (left, y, bw, rowh - 8))
        if cur:
            o.append('<rect x="%d" y="%d" width="%.1f" height="%d" rx="3" '
                     'fill="#002869"/>' % (left, y, unit * cur, rowh - 8))
        if g:
            o.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" rx="3" '
                     'fill="#E36135" fill-opacity=".28"/>'
                     % (left + unit * cur, y, unit * g, rowh - 8))
            o.append('<rect x="%.1f" y="%d" width="2" height="%d" fill="#E36135"/>'
                     % (left + unit * (cur + g) - 2, y, rowh - 8))
        o.append('<text x="%d" y="%d" class="bt">%d &#8594; %d</text>'
                 % (left + bw + 10, y + rowh / 2 - 1, cur, targets[c['id']]))
    o.append(wm(W, h))
    o.append("</svg>")
    return "".join(o)


def v_profile(m, obs):
    """Distribution of each observation across all capabilities."""
    W, rowh, gap, left, right = 880, 34, 10, 150, 66
    bw = W - left - right
    rows = []
    for t in m.observation_types:
        cnt = collections.Counter(obs[c['id']][t['id']] for c in m.capabilities)
        rows.append((t['id'].title(), dict(cnt)))
    h = len(rows) * (rowh + gap)
    o = ['<svg viewBox="0 0 %d %d" class="chart">' % (W, h)]
    for i, (label, cnt) in enumerate(rows):
        y = i * (rowh + gap)
        tot = sum(cnt.values()) or 1
        o.append('<text x="0" y="%d" class="bl">%s</text>' % (y + rowh / 2 + 4, label))
        x = left
        for k in ORDER:
            n = cnt.get(k, 0)
            if not n:
                continue
            wd = bw * n / tot
            o.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s">'
                     '<title>%s: %d</title></rect>'
                     % (x, y, wd, rowh, C[k], LABEL[k], n))
            if wd > 24:
                o.append('<text x="%.1f" y="%d" class="bn" fill="%s">%d</text>'
                         % (x + wd / 2, y + rowh / 2 + 4,
                            "#fff" if k in ("yes", "no") else "#1a2126", n))
            x += wd
        o.append('<text x="%d" y="%d" class="bt">%d</text>'
                 % (left + bw + 10, y + rowh / 2 + 4, tot))
    o.append(wm(W, h))
    o.append("</svg>")
    return "".join(o)


def v_levels(m, levels, keys):
    """How many capabilities sit at each level."""
    cnt = collections.Counter(levels.get(c['id']) for c in m.capabilities)
    W, H, pad = 560, 240, 40
    mx = max([cnt.get(k, 0) for k in keys] + [1])
    bw = (W - pad * 2) / len(keys)
    o = ['<svg viewBox="0 0 %d %d" class="chart">' % (W, H)]
    for i, k in enumerate(keys):
        n = cnt.get(k, 0)
        bh = (H - pad * 2) * n / mx
        x = pad + i * bw
        o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="5" fill="%s"/>'
                 % (x + 12, H - pad - bh, bw - 24, bh, LVL[k]))
        o.append('<text x="%.1f" y="%.1f" class="bn" fill="var(--ink)">%d</text>'
                 % (x + bw / 2, H - pad - bh - 8, n))
        o.append('<text x="%.1f" y="%d" class="ax">L%d</text>'
                 % (x + bw / 2, H - pad + 18, k))
    o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" class="axis"/>'
             % (pad, H - pad, W - pad, H - pad))
    o.append(wm(W, H))
    o.append("</svg>")
    return "".join(o)


def v_trajectory(m, levels, targets, keys):
    """Where the portfolio moves if the targets are met."""
    W, H, pad = 620, 260, 46
    now = collections.Counter(levels.get(c['id']) or 0 for c in m.capabilities)
    then = collections.Counter(targets[c['id']] for c in m.capabilities)
    mx = max(list(now.values()) + list(then.values()) + [1])
    step = (W - pad * 2) / max(len(keys) - 1, 1)

    def line(counts, cls):
        p = []
        for i, k in enumerate(keys):
            x = pad + i * step
            y = H - pad - (H - pad * 2) * counts.get(k, 0) / mx
            p.append("%.1f,%.1f" % (x, y))
        return '<polyline points="%s" class="%s"/>' % (" ".join(p), cls)
    o = ['<svg viewBox="0 0 %d %d" class="chart">' % (W, H)]
    o.append(line(now, "tl-now"))
    o.append(line(then, "tl-then"))
    for i, k in enumerate(keys):
        x = pad + i * step
        for counts, cls in ((now, "tp-now"), (then, "tp-then")):
            y = H - pad - (H - pad * 2) * counts.get(k, 0) / mx
            o.append('<circle cx="%.1f" cy="%.1f" r="4.5" class="%s"><title>'
                     'Level %d: %d</title></circle>' % (x, y, cls, k, counts.get(k, 0)))
        o.append('<text x="%.1f" y="%d" class="ax">L%d</text>' % (x, H - pad + 18, k))
    o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" class="axis"/>'
             % (pad, H - pad, W - pad, H - pad))
    o.append(wm(W, H))
    o.append("</svg>")
    return "".join(o)

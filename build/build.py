#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The only build command.

    python3 build/build.py            what the model currently says
    python3 build/build.py workbook   write out/AI-Capability-Model.xlsx
    python3 build/build.py views      write out/*.md, one per scale
    python3 build/build.py ingest     read reviewer edits back into facts/
    python3 build/build.py all        workbook + views
    python3 build/build.py check      validate facts/ and report problems

facts/ is edited. out/ is generated. `ingest` is the one path that writes to
facts/, and it only ever writes observations.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import facts as F

OUT = os.path.join(ROOT, 'out')
WORKBOOK = os.path.join(OUT, 'AI-Capability-Model.xlsx')


def _model():
    return F.Model()


# --------------------------------------------------------------- status
def cmd_status():
    m = _model()
    scales = F.load_scales()
    print("facts")
    print("  %-22s %d domains, %d capabilities, %d criteria"
          % ("capabilities.json", len(m.domains), len(m.capabilities),
             sum(len(c['criteria']) for c in m.capabilities)))
    print("  %-22s %d offerings, %d in-the-box questions"
          % ("offerings.json", len(m.offerings),
             sum(len(o['in_the_box']) for o in m.offerings)))
    print("  %-22s %d assets" % ("assets.json", len(m.assets)))
    print("  %-22s %d units, %d mapped" % ("owners.json", len(m.units),
                                           len(m.owner_map)))
    print("  %-22s %d rows" % ("observations.json", len(m.observations)))

    import collections
    print("\nobservations, by capability")
    vals = {c['id']: m.values(c['id']) for c in m.capabilities}
    for t in m.observation_types:
        c = collections.Counter(vals[x['id']][t['id']] for x in m.capabilities)
        derived = "  (derived from L3)" if t['id'] in m.criterion_types else ""
        print("  %-10s %s%s" % (t['id'], dict(sorted(c.items())), derived))

    for t in m.criterion_types:
        c = collections.Counter(
            r.get('value', 'unknown')
            for x in m.capabilities for _, r in m.criteria_obs(x['id'], t))
        n = sum(len(x['criteria']) for x in m.capabilities)
        print("\n%s, by L3 criterion (%d rows - this is what reviewers answer)"
              % (t, n))
        print("  %-10s %s" % (t, dict(sorted(c.items()))))

    print("\nscales")
    for s in scales:
        r = m.rate_all(s)
        c = collections.Counter(v[0] for v in r.values())
        pretty = {("not rated" if k is None else k): n
                  for k, n in sorted(c.items(), key=lambda kv: (kv[0] is None, kv[0]))}
        star = "  (default)" if getattr(s, 'SHORT', '') == 'level' else ""
        print("  %-22s %s%s" % (s.NAME, pretty, star))

    nomatch = [c['id'] for c in m.capabilities if m.owner(c['id'])[1] == 'NO MATCH']
    if nomatch:
        print("\n%d capabilities have no owner in the Bank's catalogue: %s"
              % (len(nomatch), ", ".join(nomatch)))


# --------------------------------------------------------------- check
def cmd_check():
    m = _model()
    problems = []
    ids = {c['id'] for c in m.capabilities}
    crit = {x['id'] for c in m.capabilities for x in c['criteria']}

    for o in m.offerings:
        for cid in o['enables']:
            if cid not in ids:
                problems.append("%s enables unknown capability %s" % (o['id'], cid))
        for a in o['assets']:
            if a not in m.asset_by_id:
                problems.append("%s references unknown asset %s" % (o['id'], a))
        for x in o['in_the_box']:
            # controls point at an L3 criterion, which resolves to its L2
            if x['capability'] not in ids and x['capability'] not in crit:
                problems.append("%s in-the-box control points at unknown subject %s"
                                % (o['id'], x['capability']))

    crit_of = {x['id']: c['id'] for c in m.capabilities for x in c['criteria']}
    for r in m.observations:
        where = "%s/%s" % (r.get('criterion') or r['capability'], r['observation'])
        if r['capability'] not in ids:
            problems.append("observation for unknown capability %s" % r['capability'])
        if r.get('criterion'):
            if r['criterion'] not in crit:
                problems.append("observation for unknown criterion %s" % r['criterion'])
            elif crit_of[r['criterion']] != r['capability']:
                problems.append("%s is recorded under %s but belongs to %s"
                                % (r['criterion'], r['capability'],
                                   crit_of[r['criterion']]))
        if r['value'] not in m.observation_values:
            problems.append("%s has invalid value %r" % (where, r['value']))
        if r['value'] == 'n/a' and not r['basis']:
            problems.append("%s is n/a with no reason" % where)
        if r['value'] in ('yes', 'partial') and not r['evidence']:
            problems.append("%s claims %s with no evidence" % (where, r['value']))

    # Capability-level observations: one row per capability per type.
    # Criterion-level observations (ADR-0014): one row per criterion.
    cap_types = {t['id'] for t in m.observation_types
                 if t['id'] not in m.criterion_types}
    for c in m.capabilities:
        got = set(m.obs_by_cap.get(c['id'], {}))
        for t in cap_types - got:
            problems.append("%s has no %s observation" % (c['id'], t))
        for t in m.criterion_types:
            rows = m.obs_by_crit.get(c['id'], {}).get(t, {})
            missing = [x['id'] for x in c['criteria'] if x['id'] not in rows]
            if missing:
                problems.append("%s has no %s observation for %d criteria (%s%s)"
                                % (c['id'], t, len(missing), ", ".join(missing[:3]),
                                   ", ..." if len(missing) > 3 else ""))

    for cid in ids:
        if cid not in m.owner_map:
            problems.append("%s is not mapped to a Bank unit" % cid)

    if problems:
        print("%d problem(s):" % len(problems))
        for p in problems:
            print("  -", p)
        return 1
    print("facts/ is consistent: %d capabilities, %d observations, %d offerings, "
          "%d assets" % (len(m.capabilities), len(m.observations),
                         len(m.offerings), len(m.assets)))
    return 0


# --------------------------------------------------------------- workbook
def cmd_workbook():
    import build_workbook
    m = _model()
    os.makedirs(OUT, exist_ok=True)
    sheets = build_workbook.build(m, F.default_scale(), WORKBOOK)
    print("wrote %s" % os.path.relpath(WORKBOOK, ROOT))
    print("  sheets: %s" % ", ".join(sheets))
    return 0


# --------------------------------------------------------------- views
def cmd_views():
    import build_views
    m = _model()
    os.makedirs(OUT, exist_ok=True)
    written = []
    for s in F.load_scales():
        path = os.path.join(OUT, 'capability-assessment-%s.md' % s.SHORT)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(build_views.capability_view(m, s))
        written.append(os.path.basename(path))
    path = os.path.join(OUT, 'management-report.md')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(build_views.management_report(m, F.default_scale()))
    written.append(os.path.basename(path))
    import build_report
    path = os.path.join(OUT, 'management-report.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(build_report.report(m, F.default_scale()))
    written.append(os.path.basename(path))
    import build_preview
    path = os.path.join(OUT, 'preview-views.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(build_preview.preview(m, F.default_scale()))
    written.append(os.path.basename(path) + '  (SAMPLE data)')
    path = os.path.join(OUT, 'agent-readiness.md')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(build_views.agent_view(m))
    written.append(os.path.basename(path))
    print("wrote %d view(s) to out/:" % len(written))
    for x in written:
        print("  -", x)
    return 0


# --------------------------------------------------------------- ingest
def cmd_ingest(path=None):
    """Read sheet 2 of a returned workbook back into facts/observations.json."""
    from openpyxl import load_workbook
    src = path or WORKBOOK
    if not os.path.exists(src):
        print("no workbook at %s - run 'workbook' first, or pass a path" % src)
        return 1
    m = _model()
    wb = load_workbook(src, read_only=True, data_only=True)
    if "2. Observations" not in wb.sheetnames:
        print("%s has no '2. Observations' sheet" % src)
        return 1
    ws = wb["2. Observations"]

    doc = json.load(open(os.path.join(F.FACTS, 'observations.json'), encoding='utf-8'))
    # key: (capability, observation, criterion or '') - criterion-level rows
    # (ADR-0014) are addressed by their criterion id
    index = {(r['capability'], r['observation'], r.get('criterion') or ''): r
             for r in doc['observations']}
    changed, unknown = 0, []
    for row in ws.iter_rows(min_row=2, values_only=True):
        if not row or not row[0]:
            continue
        # sheet 2 columns: capability, name, observation, criterion, subject,
        # question, VALUE, evidence, observed_by, date, basis
        (cid, _nm, typ, crit, _subj, _q,
         value, evidence, by, when) = (list(row) + [None] * 10)[:10]
        if typ is None:
            continue          # capability banner row, or the footer note
        key = (str(cid).strip(), str(typ).strip(),
               str(crit).strip() if crit else '')
        rec = index.get(key)
        if rec is None:
            unknown.append("/".join(x for x in key if x))
            continue
        v = (str(value).strip().lower().replace('n-a', 'n/a')
             if value is not None else 'unknown')
        if v not in doc['values']:
            unknown.append("%s/%s has value %r" % (key[0], key[1], value))
            continue
        new = {'value': v,
               'evidence': (evidence or '').strip() if evidence else '',
               'observed_by': (by or '').strip() if by else '',
               'observed_on': str(when).strip()[:10] if when else ''}
        if any(rec.get(k, '') != v_ for k, v_ in new.items()):
            rec.update(new)
            changed += 1
    with open(os.path.join(F.FACTS, 'observations.json'), 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print("ingested %s: %d observation(s) updated" % (os.path.relpath(src, ROOT), changed))
    for u in unknown[:10]:
        print("  skipped:", u)
    if len(unknown) > 10:
        print("  ... and %d more" % (len(unknown) - 10))
    if changed:
        print("now run: python3 build/build.py all")
    return 0


CMDS = {'status': cmd_status, 'check': cmd_check, 'workbook': cmd_workbook,
        'views': cmd_views, 'ingest': cmd_ingest}


def main(argv):
    if not argv:
        cmd_status()
        return 0
    cmd = argv[0]
    if cmd == 'all':
        return cmd_workbook() or cmd_views()
    if cmd == 'ingest':
        return cmd_ingest(argv[1] if len(argv) > 1 else None)
    if cmd not in CMDS:
        print(__doc__)
        print("unknown command: %s" % cmd)
        return 1
    return CMDS[cmd]() or 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

# -*- coding: utf-8 -*-
"""One-off: pull every fact out of the old scattered sources into facts/*.json.

Reads model/model3.json, model/idb-assets.json, model/idb_owners.py,
build/wb_data.py, build/wb_assets.py, build/gen_trm.py, model/sources.json,
model/obligations.json.  Writes nothing outside facts/.
"""
import json, io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def p(*a): return os.path.join(ROOT, *a)
OUT = p('facts')
os.makedirs(OUT, exist_ok=True)

def load_py(path, names):
    ns = {}
    exec(io.open(p(path), encoding='utf-8').read(), ns)
    return {n: ns[n] for n in names}

# ---------------------------------------------------------------- capabilities
M = json.load(open(p('model', 'model3.json')))
domains, caps = [], []
for d in M:
    domains.append({'id': d[0], 'name': d[1], 'definition': d[2]})
    for c in d[3]:
        caps.append({
            'id': c[0], 'domain': d[0], 'name': c[1], 'definition': c[2],
            'sources': c[3],
            'criteria': [{'id': x[0], 'name': x[1], 'definition': x[2],
                          'agentic': bool(len(x) > 3 and x[3])} for x in c[4]],
            'agentic': bool(c[5]), 'anchor': c[6],
            'proposed_owner': c[7], 'confidence': c[8],
        })
json.dump({'domains': domains, 'capabilities': caps},
          open(p('facts', 'capabilities.json'), 'w'), ensure_ascii=False, indent=1)
print('capabilities.json: %d domains, %d capabilities, %d criteria'
      % (len(domains), len(caps), sum(len(c['criteria']) for c in caps)))

# ---------------------------------------------------------------- assets
W = load_py('build/wb_assets.py', ['ASSETS', 'ASSET_LINK'])
assets = [{'id': a[1], 'type': a[0], 'name': a[2], 'status': a[3],
           'location': a[4], 'note': a[5]} for a in W['ASSETS']]
json.dump({'assets': assets}, open(p('facts', 'assets.json'), 'w'),
          ensure_ascii=False, indent=1)
print('assets.json: %d assets' % len(assets))

# ---------------------------------------------------------------- offerings
# The old REAL-001..008 rows are the offerings, merged with their asset links
# and their pattern-specific control checklists.
D = load_py('build/wb_data.py',
            ['REAL', 'CONTROLS_BY_REAL', 'GENERIC_ASSETS', 'CONSUMPTION', 'READINESS'])
ASSET_BY_ID = {a['id']: a for a in assets}
RELEASED = {'Published', 'Published (JFrog)', 'In use'}

# Group the eight realization rows into the bundles a team actually consumes.
GROUPING = [
    ('OFF-01', 'Foundry platform',        ['REAL-001']),
    ('OFF-02', 'Foundry agents',          ['REAL-002']),
    ('OFF-03', 'Custom MCP servers',      ['REAL-003']),
    ('OFF-04', 'Retrieval on AI Search',  ['REAL-004', 'REAL-005']),
    ('OFF-05', 'Document extraction',     ['REAL-006']),
    ('OFF-06', 'Approved AI tech stack',  ['REAL-007']),
    ('OFF-07', 'Agent design guidance',   ['REAL-008']),
]
REAL = {r['id']: r for r in D['REAL']}
offerings = []
for oid, name, rids in GROUPING:
    aset, caps_en, controls, notes, notprov = [], [], [], [], []
    consumption = operated = status = ''
    for rid in rids:
        r = REAL[rid]
        for aid in W['ASSET_LINK'].get(rid, []):
            if aid not in aset: aset.append(aid)
        for cid in [r['cap']] + [x.strip() for x in r['also'].split(',') if x.strip()]:
            if cid and cid not in caps_en: caps_en.append(cid)
        for nm, ref, cap, why in D['CONTROLS_BY_REAL'].get(rid, []):
            if not any(c['control'] == nm for c in controls):
                controls.append({'control': nm, 'catalog_ref': ref,
                                 'capability': cap, 'why': why, 'status': ''})
        consumption = consumption or r['consumption']
        operated = operated or r['operated']
        status = status or r['status']
        if r['note']: notes.append('%s: %s' % (rid, r['note']))
        if r['notprov']: notprov.append(r['notprov'])
    st = [ASSET_BY_ID[a]['status'] for a in aset if a in ASSET_BY_ID]
    offerings.append({
        'id': oid, 'name': name, 'was': rids,
        'assets': aset,
        'assets_released': sum(1 for s in st if s in RELEASED),
        'assets_total': len(st),
        'enables': sorted(caps_en, key=lambda x: [int(n) for n in x.split('.')]),
        'consumption': consumption, 'operated_by': operated, 'status': status,
        'not_provided': ' '.join(notprov),
        'in_the_box': controls,
        'note': ' | '.join(notes),
    })
json.dump({'generic_assets': [{'name': n, 'why': w} for n, w in D['GENERIC_ASSETS']],
           'consumption_models': [{'name': n, 'definition': d_} for n, d_ in D['CONSUMPTION']],
           'offerings': offerings},
          open(p('facts', 'offerings.json'), 'w'), ensure_ascii=False, indent=1)
print('offerings.json: %d offerings, %d in-the-box items, %d capabilities enabled'
      % (len(offerings), sum(len(o['in_the_box']) for o in offerings),
         len({c for o in offerings for c in o['enables']})))

# ---------------------------------------------------------------- owners
O = load_py('model/idb_owners.py', ['IDB_OWNERS', 'MAP', 'SOURCE_FILE', 'READ_ON'])
units = [{'name': u[0], 'function': u[1], 'family': u[2], 'lead': u[3],
          'technical_lead': u[4], 'claims': u[5]} for u in O['IDB_OWNERS']]
mapping = [{'capability': k, 'unit': v[0], 'match': v[1], 'basis': v[2]}
           for k, v in sorted(O['MAP'].items(),
                              key=lambda kv: [int(n) for n in kv[0].split('.')])]
json.dump({'source': O['SOURCE_FILE'], 'read_on': O['READ_ON'],
           'units': units, 'mapping': mapping},
          open(p('facts', 'owners.json'), 'w'), ensure_ascii=False, indent=1)
print('owners.json: %d units, %d mapped, %d NO MATCH'
      % (len(units), len(mapping), sum(1 for m in mapping if m['match'] == 'NO MATCH')))

# ---------------------------------------------------------------- realization context
src = io.open(p('build', 'gen_trm.py'), encoding='utf-8').read()
ns = {}
exec(re.search(r'^EXT = \{.*?^\}', src, re.S | re.M).group(0), ns)
exec(re.search(r'^HUMAN = \{.*?\}', src, re.S | re.M).group(0), ns)
json.dump({'realized_by_enterprise_service': ns['EXT'],
           'purely_organizational': sorted(ns['HUMAN'])},
          open(p('facts', 'enablement-context.json'), 'w'), ensure_ascii=False, indent=1)
print('enablement-context.json: %d enterprise-realized, %d organizational'
      % (len(ns['EXT']), len(ns['HUMAN'])))

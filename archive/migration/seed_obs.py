# -*- coding: utf-8 -*-
"""One-off: seed facts/observations.json.

Four observation types per capability.  Only ENABLED and DEFINED can be seeded
from evidence that already exists in the repository (the asset register).
PRACTISED and SKILLED have never been observed, so they are written as
"unknown" with no evidence - that absence is itself a finding.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def p(*a): return os.path.join(ROOT, *a)

CAPS = json.load(open(p('facts', 'capabilities.json')))['capabilities']
OFF = json.load(open(p('facts', 'offerings.json')))['offerings']
ASSETS = {a['id']: a for a in json.load(open(p('facts', 'assets.json')))['assets']}
CTX = json.load(open(p('facts', 'enablement-context.json')))
RELEASED = {'Published', 'Published (JFrog)', 'In use'}

TYPES = [
    ('practised', 'Is this done on real AI systems in production, repeatedly?',
     'Named systems or agents where it was done, and by whom'),
    ('enabled', 'Can a team get the tooling for this without building it themselves?',
     'An offering in the offerings register'),
    ('skilled', 'Do the people who must do this know how?',
     'Named practitioners, training records, or a competency statement'),
    ('defined', 'Is there a published Bank standard or method for this?',
     'The document, with a location and a date'),
]
VALUES = ['yes', 'partial', 'no', 'n/a', 'unknown']

# capability -> offerings that enable it
by_cap = {}
for o in OFF:
    for c in o['enables']:
        by_cap.setdefault(c, []).append(o)

obs = []
def add(cap, typ, value, evidence, basis):
    obs.append({'capability': cap, 'observation': typ, 'value': value,
                'evidence': evidence, 'basis': basis,
                'observed_on': '2026-09-04' if value != 'unknown' else '',
                'observed_by': 'EA, from the asset register' if value != 'unknown' else ''})

for c in CAPS:
    cid = c['id']
    offs = by_cap.get(cid, [])

    # ---- ENABLED : is there tooling, and how complete is it
    if offs:
        rel = sum(o['assets_released'] for o in offs)
        tot = sum(o['assets_total'] for o in offs)
        names = ', '.join('%s %s' % (o['id'], o['name']) for o in offs)
        aids = sorted({a for o in offs for a in o['assets']})
        val = 'yes' if rel == tot and tot else ('partial' if rel else 'no')
        add(cid, 'enabled', val, '%s (%d of %d assets released)' % (names, rel, tot),
            'Assets: ' + ', '.join(aids))
    elif cid in CTX['realized_by_enterprise_service']:
        add(cid, 'enabled', 'n/a', '',
            'Realized by an existing enterprise service: '
            + CTX['realized_by_enterprise_service'][cid])
    elif cid in CTX['purely_organizational']:
        add(cid, 'enabled', 'n/a', '',
            'Organizational capability - no technology realizes it')
    else:
        add(cid, 'enabled', 'no', '', 'No offering in the register and no reason recorded')

    # ---- DEFINED : is there a published Bank standard for this capability
    stds = []
    for o in offs:
        for aid in o['assets']:
            a = ASSETS.get(aid)
            if a and a['type'] in ('Standard', 'Reference architecture'):
                stds.append(a)
    if stds:
        rel = [a for a in stds if a['status'] in RELEASED]
        pre = [a for a in stds if a['status'] not in RELEASED]
        val = 'yes' if rel and not pre else ('partial' if rel or pre else 'no')
        ev = '; '.join('%s %s (%s)' % (a['id'], a['name'], a['status']) for a in stds)
        add(cid, 'defined', val, ev,
            'Pre-release documents hold this at partial' if pre else
            'Published standard and reference architecture')
    else:
        add(cid, 'defined', 'unknown', '',
            'No Bank standard found in the asset register - confirm none exists')

    # ---- PRACTISED and SKILLED : never observed
    add(cid, 'practised', 'unknown', '', 'Never observed. Requires the capability owner.')
    add(cid, 'skilled', 'unknown', '', 'Never observed. Requires the capability owner or L&D.')

order = {t[0]: i for i, t in enumerate(TYPES)}
obs.sort(key=lambda o: ([int(n) for n in o['capability'].split('.')], order[o['observation']]))
json.dump({'observation_types': [{'id': t, 'question': q, 'evidence_expected': e}
                                 for t, q, e in TYPES],
           'values': VALUES, 'observations': obs},
          open(p('facts', 'observations.json'), 'w'), ensure_ascii=False, indent=1)

import collections
cnt = collections.Counter((o['observation'], o['value']) for o in obs)
print('observations.json: %d rows over %d capabilities' % (len(obs), len(CAPS)))
for t, _, _ in TYPES:
    row = {v: cnt[(t, v)] for v in VALUES if cnt[(t, v)]}
    print('  %-10s %s' % (t, row))

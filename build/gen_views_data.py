# -*- coding: utf-8 -*-
"""Deterministic ILLUSTRATIVE scores for the management-views mock. Not real assessment data."""
import json, random
M = json.load(open('model3.json'))
random.seed(20260903)

# Story shape per domain: (maturity centre, readiness centre) on 1-5 / 0-5.
# Deliberately encodes the finding the real assessment is expected to surface:
# platform supply is ahead of institutional ability, governance lags both.
SHAPE = {
 'D1': (2.4, 1.2), 'D2': (2.0, 1.4), 'D3': (2.3, 2.6), 'D4': (2.6, 3.1),
 'D5': (2.7, 3.9), 'D6': (2.1, 2.4), 'D7': (1.7, 1.3), 'D8': (1.8, 0.9),
}
TARGET = {'D1':4,'D2':3,'D3':4,'D4':4,'D5':4,'D6':3,'D7':4,'D8':3}

def jitter(c, lo, hi):
    v = round(c + random.uniform(-1.35, 1.35))
    return max(lo, min(hi, v))

caps, doms = [], []
for d in M:
    did, dname = d[0], d[1]
    mc, rc = SHAPE[did]
    doms.append({'id': did, 'name': dname, 'short': dname.replace('AI ', '')})
    for l2 in d[3]:
        lid, lname, ldef, prov, l3s, agentic, anchor, owner, conf = l2
        mat = jitter(mc, 1, 5)
        rdy = jitter(rc, 0, 5)
        tgt = min(5, max(mat, TARGET[did] + random.choice([-1, 0, 0, 0, 1])))
        caps.append({
            'id': lid, 'd': did, 'n': lname, 'own': owner, 'anchor': anchor,
            'ag': agentic, 'm': mat, 'r': rdy, 't': tgt, 'n3': len(l3s),
            # trajectory: where illustrative delivery would put it
            'm6': min(5, mat + (1 if random.random() < .35 else 0)),
            'm12': min(5, mat + (1 if random.random() < .35 else 0) + (1 if random.random() < .45 else 0)),
            # evidence coverage 0-1 for the assurance view
            'ev': round(min(1.0, max(0.0, random.gauss(0.35 if did == 'D7' else 0.5, 0.22))), 2),
            'eff': random.choice(['S', 'M', 'M', 'L']),
        })

# hand-set a few so the quadrant view has real occupants in every corner
by = {c['id']: c for c in caps}
def setv(i, m=None, r=None, t=None):
    if m is not None: by[i]['m'] = m
    if r is not None: by[i]['r'] = r
    if t is not None: by[i]['t'] = max(by[i]['m'], t)
setv('5.1', m=2, r=4, t=4)      # Foundry: well packaged, institution not yet able
setv('3.6', m=2, r=4, t=4)      # retrieval: same shape
setv('4.5', m=3, r=4, t=4)      # integration/MCP: closest to healthy
setv('5.3', m=4, r=4, t=4)      # environments: the one genuinely healthy cell
setv('4.1', m=4, r=2, t=4)      # architecture governance: strong practice, little packaging
setv('3.1', m=4, r=3, t=4)      # data governance: pre-existing enterprise strength
setv('7.4', m=2, r=1, t=4)      # AI security: thin both ways
setv('7.7', m=1, r=0, t=4)      # inventory: nothing there
setv('2.3', m=3, r=1, t=4)      # product mgmt: people can do it, nothing packaged
setv('8.3', m=3, r=1, t=3)      # literacy: same
setv('1.5', m=1, r=0, t=3)      # new capability
setv('2.6', m=1, r=0, t=3)

json.dump({'domains': doms, 'caps': caps, 'target': TARGET},
          open('views_data.json', 'w'), ensure_ascii=False)
print(len(caps), 'capabilities')
import collections
print('maturity dist', sorted(collections.Counter(c['m'] for c in caps).items()))
print('readiness dist', sorted(collections.Counter(c['r'] for c in caps).items()))
print('avg gap', round(sum(c['t']-c['m'] for c in caps)/len(caps), 2))

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

        # capability -> {observation type: row}
        self.obs_by_cap = {}
        for r in self.observations:
            self.obs_by_cap.setdefault(r['capability'], {})[r['observation']] = r

        # capability -> offerings enabling it
        self.offerings_for = {}
        for off in self.offerings:
            for cid in off['enables']:
                self.offerings_for.setdefault(cid, []).append(off)

    def values(self, cid):
        """{'practised': 'yes', ...} for one capability."""
        return {t['id']: self.obs_by_cap.get(cid, {}).get(t['id'], {}).get('value', 'unknown')
                for t in self.observation_types}

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

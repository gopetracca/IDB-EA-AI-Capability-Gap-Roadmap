# The model before the refactor

Superseded by `facts/`. Kept because the conversion was mechanical and someone may want
to check it.

| File | Held | Converted to |
|---|---|---|
| `model3.json` | 8 domains, 52 capabilities, 258 criteria, as **positional arrays** — a capability was `c[7]`, a criterion `x[2]` | `facts/capabilities.json`, keyed |
| `idb-assets.json` | 20 IDB assets, 8 realizations, asset links | `facts/assets.json`, `facts/offerings.json` |
| `realization.json` | A **third, contradictory** realization register: 1 confirmed of 5 | Merged into `facts/offerings.json`; the asset-backed version won |
| `idb_owners.py` | 16 Bank units and the 52-capability mapping — **model data living in a Python file** | `facts/owners.json` |

The conversion script is `../migration-2026-09-04/extract.py`. It reads these files and
writes `facts/`, and it is reproducible.

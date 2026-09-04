# Archive

**Nothing here is current.** Kept because it is what reviewers were sent before
4 September 2026, and because the evidence in it was migrated rather than discarded.

Read [`../README.md`](../README.md) instead.

## What is here and where it went

| Directory | What it was | Where it lives now |
|---|---|---|
| `old-model/` | `model3.json`, `realization.json`, `idb-assets.json`, `idb_owners.py` | `facts/*.json` — converted from positional arrays to keyed JSON |
| `old-build/` | The six builders, `run.py`, `recalc.py`, the LibreOffice bridge | `build/build.py` — one entry point, no formulas, so no recalc |
| `reference-catalog/` | `catalog4.py` (143 entries), the TRM and views generators | Nowhere. Frozen, not maintained |
| `generated-2026-09/` | Every artifact generated before the refactor | `out/`, regenerated from `facts/` |

## Why the reference catalog was frozen

143 vendor-neutral entries — 76 services, 57 ABBs, 5 patterns, 5 standards — with typed
edges to capabilities. It is genuinely good work and it answers a question nobody at the
Bank was asking. Maintaining it against a market that renames its products twice a year
is a standing cost with no reader.

It is frozen rather than deleted: `S3.16 Hybrid Retrieval Pattern` is a properly written
pattern (problem, context, forces, solution, resulting context, rationale, known uses)
and is worth lifting if a retrieval design review ever needs one.

## The three registers that disagreed

Before the refactor, three files each claimed to be the register of what IDB provides,
and they contradicted each other:

| File | Said | Confirmed |
|---|---|---|
| `old-model/realization.json` | 1 realization, readiness 4 | 1 of 5 |
| `old-build/wb_data.py` + `old-model/idb-assets.json` | 8 realizations, 20 assets | 7 of 8 |
| `reference-catalog/mkregister.py` | A different 0–4 scale | 1 of 77 |

The generated Markdown was built from the first and the workbook from the second, so the
two main deliverables disagreed about the Bank's estate. `facts/offerings.json` merges
them, taking the asset-backed version as canonical because it is the one with evidence.

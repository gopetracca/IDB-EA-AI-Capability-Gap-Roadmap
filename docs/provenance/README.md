# Provenance

Where the model's claims come from, and whether a reviewer can open the source.

**The rule is [ADR-0010](../decisions/adr/0010-provenance-grading.md):** provenance is graded by
whether a reviewer can open it, not by prestige.

## What lives where

| | |
|---|---|
| **The rule** — grades, derivation types, locus | [ADR-0010](../decisions/adr/0010-provenance-grading.md) |
| **Why the two scales are graded as they are** | [ADR-0011](../decisions/adr/0011-scale-provenance.md) |
| **The register** — 40 sources, graded | `model/sources.json` |
| **Verification findings**, dated | `findings-YYYY-MM-DD.md` in this directory |
| **The reviewer workbook** | `out/AI-Capability-Provenance-for-review.xlsx` |

## The register is data

`model/sources.json` is edited directly. `build/prov_data.py` only loads it and exposes the tuples
the builders index positionally — if you add a field, add it to `FIELDS` in that loader too.

Rebuild after any edit:

    cd build && python run.py build_prov.py

## Findings log

| Date | Sources | Pairs | Findings | Blocking |
|---|---|---|---|---|
| [2026-09-03](findings-2026-09-03.md) | 40 | 147 | 18 | 4 |

## The one rule that catches people

> **A grade-D source cannot support a claim in anything that leaves the Bank**, whatever its
> quality.

Grade D currently covers 7 sources — the analyst model, consultancy patterns, the World Bank
slide, and the "institutional practice" placeholders. All are usable internally to check
ourselves; none is usable as evidence externally.

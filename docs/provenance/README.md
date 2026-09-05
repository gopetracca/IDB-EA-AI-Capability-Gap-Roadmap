# Provenance

Where the model's claims come from, and whether a reviewer can open the source.

**The rule is [ADR-0010](../decisions/adr/0010-provenance-grading.md):** provenance is graded by
whether a reviewer can open it, not by prestige.

## What lives where

| | |
|---|---|
| **The rule** — grades, derivation types, locus | [ADR-0010](../decisions/adr/0010-provenance-grading.md) |
| **Why the scales are graded as they are** | [ADR-0011](../decisions/adr/0011-scale-provenance.md) (survey; conclusion superseded) and [`../../scales/README.md`](../../scales/README.md) |
| **The register** — 40 sources, graded, and the table that resolves each citation | [`../../facts/sources.json`](../../facts/sources.json) |
| **The view** — grade exposure per capability, what rests on grade D, locus coverage | [`../../out/provenance.md`](../../out/provenance.md), regenerated on every build |
| **The reviewer sheet** | Sheet 8 of `out/AI-Capability-Model.xlsx` |
| **Verification findings**, dated | `findings-YYYY-MM-DD.md` in this directory |

## The register is data, and the build checks it

`facts/sources.json` is edited directly. Every string in a capability's `sources` list must
resolve through its `normalize` (or `extra_from`) table to a register entry, or
`python3 build/build.py check` fails. A source is added by verifying it first (the `citing`
skill), then adding the register entry and the citation string it normalizes.

Rebuild after any edit:

    python3 build/build.py all

## Findings log

| Date | Sources | Pairs | Findings | Blocking |
|---|---|---|---|---|
| [2026-09-03](findings-2026-09-03.md) | 40 | 147 (143 after the ADR-0009 amendment) | 18 | 4 |

## Where it stands (4 September 2026)

- **Grades:** A 10 · B 11 · C 12 · D 7.
- **10 capabilities rest partly on a grade-D source** — the analyst model (2), unattributed
  consultancy patterns (2), and "institutional practice" or an unnamed internal instrument
  (6). Listed by name in `out/provenance.md`. Each has other sources; each grade-D citation
  must be replaced or the claim restated as ours before external circulation.
- **15 of 143 citations carry a locus.** The rest say *this source informed the
  capability* without saying where. Under ADR-0010 an unpinned pair reads as *synthesized*.
- The four blocking findings of 3 September remain open: `OPEN-ITEMS.md` item 9.

## The one rule that catches people

> **A grade-D source cannot support a claim in anything that leaves the Bank**, whatever its
> quality.

Grade D currently covers 7 sources — the analyst model, consultancy patterns, the World Bank
slide's lineage, and the "institutional practice" placeholders. All are usable internally to
check ourselves; none is usable as evidence externally.

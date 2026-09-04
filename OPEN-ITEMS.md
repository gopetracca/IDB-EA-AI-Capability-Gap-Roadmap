# Open items

What is unresolved, what it blocks, and what would close it. One row per item; keep it current —
this is the list read before any approval request.

**Last reviewed:** 4 September 2026

---

## Blocks external publication

| # | Item | Detail | Closes when |
|---|---|---|---|
| 1 | **Four blocking provenance findings** | EDM Council ADAC is not a publication (4 cites) · TOGAF capability-based planning removed from the current edition · Gartner and consultancy patterns are non-public but back 4 capabilities · "Institutional practice" names no document (6 uses) | Each is re-cited to an openable source or the capability is reclassified **Synthesized**. See [`provenance/findings-2026-09-03.md`](provenance/findings-2026-09-03.md) |

## Blocks approval of ADR-0007

| # | Item | Detail | Closes when |
|---|---|---|---|
| 2 | **Control mapping** | ISO/IEC 42001 Annex A and NIST AI RMF outcomes are not mapped | The mapping exists. **Until then, carve [ADR-0007](decisions/adr/0007-anchoring-is-provisional.md) out of any approval request** |
| 3 | **Anchor crosswalk** | 14 of 52 capabilities are lenses, unverified | The Bank's existing enterprise capability map is available and crosswalked |

## Blocks mechanical scoring

| # | Item | Detail | Closes when |
|---|---|---|---|
| 4 | **Rubrics** | One worked example exists; **51 remain**. Until a capability has one, its rating is **provisional and must be labelled so** | Each L2 has a rubric |
| 5 | **L3 criteria typing** | 258 criteria are not flagged *mandatory / conditional / enhancing*, so the maturity gates ([ADR-0001](decisions/adr/0001-two-scales-never-merged.md)) cannot be evaluated mechanically | Every L3 carries a type and, where conditional, an applicability trigger |

## Blocks the gap analysis and roadmap

| # | Item | Detail | Closes when |
|---|---|---|---|
| 6 | **No target state** | Sheet `5. Gap & roadmap` computes *maturity gap* and *readiness lead*, but the target column is a reference into a column nobody has filled. Nothing in `model/` holds target maturity, horizon, sequencing or dependencies | A target-state register exists and a roadmap builder reads it. **Not yet designed — no ADR written** |

## In flight

| # | Item | Detail | Closes when |
|---|---|---|---|
| 7 | **Taxonomy validation** | The review workbook is with the capability owner. `1.5` and `2.6` carry confidence **low** | The workbook comes back and returns are applied to `model/model3.json` |
| 8 | **Provenance loci** | 147 capability-source pairs · **19** have no locus candidate · the rest carry an unverified one · **11** sources are paywalled or members-only | Each locus is checked against the source text. Paywalled ones need a licence holder |
| 9 | **Ownership model** | [ADR-0012](decisions/adr/0012-capability-ownership-model.md) is **Proposed**, recommending typed contribution columns. One `Owner` column currently conflates standard-setting with operation | The decision owner accepts, rejects, or amends it |
| 10 | **REAL-005** | Confirm whether the Azure AI Search Standard mandates ACL-trimmed, pre-ranking retrieval. **Decides the headline finding on domain D3** | Confirmed against the service documentation |
| 11 | **Agent provisioning** | 12 "what comes in the box" rows unanswered on the enablement sheet | The platform team answers them |
| 12 | **Proposed `5.5.6` Tool Traffic Mediation & Control** | The model names a runtime chokepoint for *model* traffic (`5.2.2`) but not for *tool* traffic. An MCP gateway has no single capability to be assessed against. **Not yet added** | An ADR settles whether to add it |

---

## Environment

| # | Item | Detail |
|---|---|---|
| 13 | **`recalc.py` cannot run** | LibreOffice (`soffice`) is not on `PATH`, so the mandatory zero-error recalc gate cannot be executed. `openpyxl` is only present on `python3.13`, not the default `python3` |

# Open items

What is unresolved, what it blocks, and what would close it.

**Last reviewed:** 4 September 2026, after the facts-and-scales refactor ([ADR-0013](docs/decisions/adr/0013-facts-and-scales.md))

---

## Blocks any rating at all

| # | Item | Detail | Closes when |
|---|---|---|---|
| 1 | **`practised` has never been observed** | All 52 capabilities. The default scale correctly returns *not rated* for every one, because performance is the gate for every level. This is the single highest-value gap in the model | The capability owners are asked, per capability, what is actually done on real AI systems. Record on sheet 2 |
| 2 | **`skilled` has never been observed** | All 52. Blocks Level 2 even where practice exists | L&D or the capability owner answers |

## Blocks the agent answer being complete

| # | Item | Detail | Closes when |
|---|---|---|---|
| 3 | **27 in-the-box questions unanswered** | Sheet 4. Twelve for the agent offering alone: identity, inventory registration, tracing, guardrails, injection defence, eval harness, cost tags, kill switch, credentials, network, human approval, retention | The platform team answers yes / no / partial |
| 4 | **Two documents pre-release** | Foundry Agents Standard (STD-07) and its reference architecture (RA-05). Releasing them moves `defined` from partial to yes for the agent capabilities | They are published |
| 5 | **MCP template v2 not distributed** | TPL-01 implements the superseded MCP specification; the July 2026 revision deprecated several primitives on defined timelines. v2 is built but not shared | v2 is distributed and v1 servers have a migration plan |
| 6 | **Access-trimmed retrieval unconfirmed** | Does the Azure AI Search Standard mandate ACL-trimmed, pre-ranking retrieval? Decides the headline finding on D3 | Confirmed against the service documentation and STD-04 |

## Blocks external publication

| # | Item | Detail | Closes when |
|---|---|---|---|
| 7 | **Four provenance findings** | EDM Council ADAC is not a publication (4 cites) · TOGAF capability-based planning removed from the current edition, re-cite as G193 · licensed analyst and consultancy patterns back 4 capabilities · "institutional practice" names no document (6 uses) | Each is re-cited to an openable source or reclassified. `docs/provenance/findings-2026-09-03.md`. **About a day's work** |
| 8 | **ISO/IEC 33020 not opened** | The default scale is adapted from it, but the N-P-L-F bands and the exact level rule come from secondary sources about the superseded 15504. **Do not quote them** | Someone opens the standard through the Bank's ISO subscription (CHF 181, or the subscription) |

## Blocks approval of ADR-0007

| # | Item | Detail | Closes when |
|---|---|---|---|
| 9 | **Control mapping absent** | ISO/IEC 42001 Annex A and NIST AI RMF outcomes are not mapped | The mapping exists. **Until then carve ADR-0007 out of any approval request** |
| 10 | **Anchor crosswalk** | 14 of 52 are lenses, unverified | The Bank's existing enterprise capability map is available and crosswalked |

## Findings about the Bank, not gaps in the model

| # | Item | Detail |
|---|---|---|
| 11 | **8 capabilities have no owner** | `1.5` ecosystem · `2.3` AI product management · `4.6` evaluation and testing · `6.3` drift and continuous quality · `7.2` responsible AI · `7.5` privacy · `7.6` legal · `7.9` impact assessment. Nothing in the Bank's own product and enabler catalogue claims them. **This is a finding to report, not a gap to fill** |
| 12 | **24 capabilities have no offering and no recorded reason** | `enabled: no`. Some are genuinely absent; others need an `n/a` with a reason | Walk the list once and separate the two |

## In flight

| # | Item | Detail | Closes when |
|---|---|---|---|
| 13 | **Taxonomy validation** | With the capability owner. `1.5` and `2.6` carry confidence *low* | The review comes back and is applied to `facts/capabilities.json` |
| 14 | **ADR-0012 ownership model** | **Proposed.** Its own text argues the `dependency` flag is the stronger route and needs no extension to defend | The decision owner accepts, rejects or amends |
| 15 | **Spanish explainer is stale** | `docs/analysis/como-funciona-el-modelo.md` explains the superseded two-scale model | Rewrite from `docs/how-it-works.md`, **after** the new construct survives one real conversation |
| 16 | **`5.5.6` Tool Traffic Mediation proposed** | The model names a runtime chokepoint for *model* traffic (`5.2.2`) but not for *tool* traffic. An MCP gateway has no single capability to assess against | An ADR settles whether to add it |

## Closed by the refactor

- ~~51 of 52 rubrics missing~~ — rubrics are no longer how a level is derived (ADR-0013)
- ~~258 L3 criteria not typed~~ — criteria are a checklist behind `practised`, not gates
- ~~No target state~~ — targets are target *column states* with a date, recordable now
- ~~Three registers disagree~~ — merged into `facts/offerings.json`
- ~~`recalc.py` cannot run~~ — the workbook has no formulas, so there is nothing to recalculate

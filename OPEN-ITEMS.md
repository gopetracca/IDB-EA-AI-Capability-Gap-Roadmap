# Open items

What is unresolved, what it blocks, and what would close it.

**Last reviewed:** 9 September 2026, after the D4-D6 completeness review
([ADR-0015](docs/decisions/adr/0015-extend-d4-d6-across-the-agentic-seam.md)). The
preceding review was 4 September 2026, after the facts-and-scales refactor
([ADR-0013](docs/decisions/adr/0013-facts-and-scales.md),
[ADR-0014](docs/decisions/adr/0014-practised-is-observed-at-l3.md)). Live figures are in
`out/management-report.html`; the ones here are as of this date.

---

## Blocks any rating at all

| # | Item | Detail | Closes when |
|---|---|---|---|
| 1 | **`practised` has never been observed** | All 281 criteria. The default scale and the maturity lens correctly return *not rated* for every capability, because performance is the gate for every level. This is the single highest-value gap in the model | The capability owners are asked, per criterion, what is actually done on real AI systems. Record on sheet 2 |
| 2 | **`skilled` has never been observed** | All 55. Blocks Level 2 even where practice exists | L&D or the capability owner answers |

## Blocks the agent answer being complete

| # | Item | Detail | Closes when |
|---|---|---|---|
| 3 | **27 in-the-box questions unanswered** | Sheet 4. Twelve for the agent offering alone: identity, inventory registration, tracing, guardrails, injection defence, eval harness, cost tags, kill switch, credentials, network, human approval, retention | The platform team answers yes / no / partial |
| 4 | **Two documents pre-release** | Foundry Agents Standard (STD-07) and its reference architecture (RA-05). Releasing them moves `defined` from partial to yes for the agent capabilities. `check` will advise which observations to re-take when the status changes | They are published |
| 5 | **MCP template v2 not distributed** | TPL-01 implements the superseded MCP specification; the July 2026 revision deprecated several primitives on defined timelines. v2 is built but not shared | v2 is distributed and v1 servers have a migration plan |
| 6 | **Access-trimmed retrieval unconfirmed** | Does the Azure AI Search Standard mandate ACL-trimmed, pre-ranking retrieval? Decides the headline finding on D3 | Confirmed against the service documentation and STD-04 |

## Limits of the scale

| # | Item | Detail | Closes when |
|---|---|---|---|
| 7 | **Level 3 reads conformance, it does not evidence it** | `defined` says an approved standard exists; `practised` says the work is done. Neither says the work **follows** the standard. Level 3 reads conformance from the two facts sitting together, and its reason line says so. A fifth observation — `conforms` — would make it checkable | A `conforms` observation is added, or a deliberate decision is recorded that reading it is good enough |
| 8 | **Levels 4 and 5 cannot be reached** | Defined in the default scale and the maturity lens (`DERIVABLE_MAX = 3`), but they need threshold monitoring and a closed improvement cycle, and nothing collects either. **Level 3 is the top of what is measured, not the top of what is possible** — every view says so | Observations for threshold monitoring and improvement cycles exist, or the levels are removed from the scale |

## Blocks external publication

| # | Item | Detail | Closes when |
|---|---|---|---|
| 9 | **Four provenance findings** | EDM Council ADAC is not a publication · TOGAF capability-based planning removed from the current edition, re-cite as G193 · licensed analyst and consultancy patterns back 4 capabilities · "institutional practice" and unnamed internal instruments back 6. **`out/provenance.md` now lists the 14 capabilities affected by name** (the figure was 10 in the 4 September text; the live view has said 14 since, and ADR-0015 added none) | Each is re-cited to an openable source or reclassified. `docs/provenance/findings-2026-09-03.md`. **About a day's work** |
| 10 | **ISO/IEC 33020 not opened** | The default scale is adapted from it, but the N-P-L-F bands and the exact level rule come from secondary sources about the superseded 15504. **Do not quote them** | Someone opens the standard through the Bank's ISO subscription (CHF 181, or the subscription) |
| 11 | **144 of 162 citations have no locus** | A citation without a clause, section or control says *this source informed the capability* without saying where. Under ADR-0010 an unpinned pair reads as *synthesized*. Two were pinned on 5 September 2026 (7.2 to NIST AI RMF GOVERN 1.2, verified against the primary text; 7.3 to ISO/IEC 23894 6.4.2, its title and location confirmed against the publisher's preview, its body still unopened) | Loci pinned for the sources a reviewer can open; the paywalled ones need a licence holder |

## Blocks approval of ADR-0007

| # | Item | Detail | Closes when |
|---|---|---|---|
| 12 | **Control mapping absent** | ISO/IEC 42001 Annex A and NIST AI RMF outcomes are not mapped | The mapping exists. **Until then carve ADR-0007 out of any approval request** |
| 13 | **Anchor crosswalk** | 14 of 55 are lenses, unverified | The Bank's existing enterprise capability map is available and crosswalked |

## Findings about the Bank, not gaps in the model

| # | Item | Detail |
|---|---|---|
| 14 | **9 capabilities have no owner** | `1.5` ecosystem · `2.3` AI product management · `4.6` evaluation and testing · `6.3` drift and continuous quality · `6.7` human oversight operations · `7.2` responsible AI · `7.5` privacy · `7.6` legal · `7.9` impact assessment. Nothing in the Bank's own product and enabler catalogue claims them. **This is a finding to report, not a gap to fill.** `6.7` was added on 9 September 2026 (ADR-0015) already knowing nobody would claim it |
| 15 | **26 capabilities: tooling never examined** | No platform offering, and nobody has asked whether an enterprise service or a GRC platform provides it. Recorded as `enabled: unknown` since 4 September 2026 (ADR-0013 Amendment 2); `5.7` and `6.7` joined them on 9 September 2026 (ADR-0015); they were `no` before, which the executive lens scored as zeros. The owner separates *no tooling exists* (`no`, evidenced) from *none is needed* (`n/a`, with the reason in `facts/enablement-context.json`) |

## In flight

| # | Item | Detail | Closes when |
|---|---|---|---|
| 16 | **Taxonomy validation** | With the capability owner. `1.5`, `2.6` and — since ADR-0015 — `5.7`, `5.8` and `6.7` carry confidence *low*. Five of 55 | The review comes back and is applied to `facts/capabilities.json` |
| 17 | **ADR-0012 ownership model** | **Proposed.** Its own text argues the `dependency` flag is the stronger route and needs no extension to defend | The decision owner accepts, rejects or amends |
| 18 | **Spanish explainer is stale** | `docs/analysis/como-funciona-el-modelo.md` explains the superseded two-scale model; it now carries a banner saying so | Rewrite from `docs/how-it-works.md`, **after** the new construct survives one real conversation |
| 20 | **Offering notes use the superseded vocabulary** | The `note` field on each offering in `facts/offerings.json` is the migration note from the realization register and still says *"readiness 3, not 4"*, *"the step to 4"*. Shown on sheet 3. Kept as history, labelled as such | The seven notes are rewritten in the current vocabulary (pending assets, in-the-box gaps) |
| 21 | **Six obligations re-homed, pending Legal** | Six statutory references pointed at services in the frozen reference catalog. Re-homed on 4 September 2026 to the parent capability of the criteria the catalog linked them to; `subject` names the former service id | Legal confirms the placement along with applicability (ADR-0008) |
| 22 | **2.2 enabled by a guidance offering** | `2.2 AI Use-Case Feasibility & Qualification` was listed as purely organizational and is also enabled by OFF-07 (the agent decision tree). The context entry was removed; the observation (`yes`, evidenced) stands | The owner confirms a decision aid counts as tooling for 2.2, or `enabled` becomes `n/a` again |

## Closed by the refactor and the review

- ~~51 of 52 rubrics missing~~ — rubrics are no longer how a level is derived (ADR-0013)
- ~~258 L3 criteria not typed~~ — criteria are a checklist behind `practised`, not gates
- ~~No target state~~ — targets are target *column states* with a date, recordable now
- ~~Three registers disagree~~ — merged into `facts/offerings.json`
- ~~`recalc.py` cannot run~~ — the workbook has no formulas, so there is nothing to recalculate
- ~~Release counts typed on offerings~~ — derived from asset statuses; `check` rejects them stored (4 Sept 2026)
- ~~Source register not load-bearing~~ — every citation must resolve; `out/provenance.md` and sheet 8 report it (4 Sept 2026)
- ~~Agent one-pager hard-coded in a builder~~ — generated from `facts/questions.json`; a second question is one more entry (4 Sept 2026)
- ~~`5.5.6` Tool Traffic Mediation undecided~~ — decided as a **capability**, `5.7 AI Runtime Mediation & Egress Control`, not a criterion of `5.5` (ADR-0015, 9 September 2026). A catalog is a design-time inventory; a gateway stands in the path of a call, and the two have different owners
- ~~Nothing tested~~ — 39 tests cover the roll-up table, the ladder, the scale contract, ingest round trip and that builds never write to `facts/` (4 Sept 2026)

# Open items

What is unresolved, what it blocks, and what would close it.

**Last reviewed:** 10 September 2026, after the D4 and D5 review rounds were transcribed
([ADR-0016](docs/decisions/adr/0016-d4-criteria-refinements-from-the-first-review-round.md),
[ADR-0017](docs/decisions/adr/0017-carve-out-experimentation-and-rehome-shared-agent-assets.md))
and `5.9`'s criteria were completed ([ADR-0018](docs/decisions/adr/0018-complete-the-criteria-of-ai-experimentation.md)).
The preceding review was 9 September 2026, after the D4-D6 completeness review
([ADR-0015](docs/decisions/adr/0015-extend-d4-d6-across-the-agentic-seam.md)). The
preceding review was 4 September 2026, after the facts-and-scales refactor
([ADR-0013](docs/decisions/adr/0013-facts-and-scales.md),
[ADR-0014](docs/decisions/adr/0014-practised-is-observed-at-l3.md)). Live figures are in
`out/management-report.html`; the ones here are as of this date.

---

## Blocks any rating at all

| # | Item | Detail | Closes when |
|---|---|---|---|
| 1 | **`practised` observed on 47 of 287 criteria** | D4 was walked through on 9 September 2026 (ADR-0016) and D5 on 10 September (ADR-0017). Ten capabilities are rated, all at Level 1. **The other 240 criteria and 46 capabilities are untouched**, including all of D1, D2, D3, D6, D7 and D8. Performance is the gate for every level, so this remains the single highest-value gap | The remaining capability owners are asked, per criterion, what is actually done on real AI systems. Record on sheet 2 |
| 2 | **`skilled` has never been observed** | All 56, and it is now the binding constraint. **`5.3` rolls up to `practised: yes` with `enabled: yes` and `defined: yes` — competence is the only thing between it and Level 3.** No other capability in the model is that close | L&D or the capability owner answers. **Start with `5.3`** |

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
| 14 | **9 capabilities have no owner** | `1.5` ecosystem · `2.3` AI product management · `5.5` tool and connector catalog · `6.3` drift and continuous quality · `6.7` human oversight operations · `7.2` responsible AI · `7.5` privacy · `7.6` legal · `7.9` impact assessment. Nothing in the Bank's own product and enabler catalogue claims them. **This is a finding to report, not a gap to fill.** `6.7` was added on 9 September 2026 (ADR-0015) already knowing nobody would claim it. `4.6` left this list on 9 September 2026 when the EA workshop gave evaluation and testing to the AI enabler; `5.5` joined it on 10 September when the meeting withdrew the AI enabler as its owner — a red-flagged doubt, not a settled finding |
| 15 | **26 capabilities: tooling never examined** | No platform offering, and nobody has asked whether an enterprise service or a GRC platform provides it. Recorded as `enabled: unknown` since 4 September 2026 (ADR-0013 Amendment 2); `5.7` and `6.7` joined them on 9 September 2026 (ADR-0015); they were `no` before, which the executive lens scored as zeros. The owner separates *no tooling exists* (`no`, evidenced) from *none is needed* (`n/a`, with the reason in `facts/enablement-context.json`) |

## In flight

| # | Item | Detail | Closes when |
|---|---|---|---|
| 16 | **Taxonomy validation** | With the capability owner. `1.5`, `2.6` and — since ADR-0015 — `5.7`, `5.8` and `6.7` carry confidence *low*. Five of 55 | The review comes back and is applied to `facts/capabilities.json` |
| 17 | **ADR-0012 ownership model** | **Proposed.** Its own text argues the `dependency` flag is the stronger route and needs no extension to defend | The decision owner accepts, rejects or amends |
| 28 | **`5.9 AI Experimentation` has no evidence** | Added 10 September 2026 (ADR-0017), `confidence: low`, owner Emerging Tech by inference — the meeting wrote "Tech Lab", which is not a unit in the catalogue, and its note was "ASK tech lab". The definition was restated the same day to say what it is for (ADR-0017 Amendment 1) and four criteria were added — access, emerging-service access, data admission and egress, time-boxing and teardown (ADR-0018). None of the five has been seen by the Tech Lab | The Tech Lab confirms, amends or strikes the capability and its criteria |
| 29 | **Three D5 judgements contradict the asset register** | `5.5 enabled: no` against OFF-03 at 4 of 7 released (partial) · `5.8 enabled: yes` against OFF-02 at 6 of 8 released (partial), where the meeting's own criterion notes say "missing prod" · `5.5` and `5.6` `defined` moved back to `unknown` while published standards stay in the evidence field. Each row states the disagreement in its `basis`; nothing was overwritten | The owners reconcile the register against what they see |
| 30 | **Four rows flagged red — "Doubts. Needs Karla"** | `5.1`, `5.4`, `5.5` and `5.6.4`, the meeting's own colour convention. `5.4 defined: n/a` carries no reason, only the routing note "Send to Edgares?" | Karla is asked |
| 31 | **`5.7` ownership unsettled** | Flagged amber — "we dont know what to do with this" — with the note "Might be the control plane v99". `facts/owners.json` still records the AI enabler from ADR-0015; the meeting's sheet said Unknown, on a row it pasted rather than assessed, so nothing was changed | The capability is validated or retired |
| 18 | **Spanish explainer is stale** | `docs/analysis/como-funciona-el-modelo.md` explains the superseded two-scale model; it now carries a banner saying so | Rewrite from `docs/how-it-works.md`, **after** the new construct survives one real conversation |
| 19 | **Three owner changes cannot be recorded** | The EA workshop named `4.5` → *Product Teams*, `4.7` → *Core Platforms + Product Teams* and `5.1` → *Enablers*. None is a unit in the Bank's 16-unit catalogue that `facts/owners.json` reads, and the schema holds one unit per capability. `4.4` → Enterprise Architecture and `4.6` → Artificial Intelligence were applied; these three were not | ADR-0012 is decided, or the catalogue read is extended to name product teams |
| 23 | **Six rows carry a value with no reason** | `4.3.4`, `4.3.5` (covered by the 4.3 blanket rationale), `4.4.2`, `4.6.2`, `4.6.4` marked `n/a` and `4.7.2` marked `partial`, all with nothing written beside them on the sheet. Each row says so in its own `basis` rather than being filled in. The reverse also happened once: `5.1.2` Landing Zone & Baseline Provisioning carries the note *"Terraform modules"* and no value, so it stays `unknown` | The capability owner supplies the reason, or the value drops back to `unknown` |
| 24 | **`4.6` `enabled`/`defined` recorded as `no`, arguably `unknown`** | The workshop wrote `no`, but its own note says *"the eval framework from ai product, unknown status"*. Under ADR-0013 Amendment 2 an unresolved register answer is `unexamined`, not an evidenced negative. Recorded as written, with the tension stated in the basis | The AI enabler confirms whether that framework exists and what it covers |
| 25 | **`4.4` `enabled: n/a` contradicts OFF-02** | The workshop marked the tooling not applicable; `OFF-02 Foundry agents` enables the capability. `check` raises this as its one standing advisory | The owner says whether agent design genuinely needs no tooling, or the value moves |
| 26 | ~~**Should `4.3` be reframed around skills, plugins and hooks?**~~ | **Closed 10 September 2026 by ADR-0017.** The shared repository of skills, hooks and rules is `5.6.4`, re-scoped. A production agent's own skills were already covered by `5.5`, `4.4` and `5.8.1`. `4.3` itself stays `n/a` and is not reframed | Closed |
| 27 | **ADR-0015's new criteria were never put to the workshop** | `4.5.6` agent-to-agent interoperability and `4.6.6`–`4.6.8` trajectory evaluation, simulation testing and judge governance were added the day after the workbook was generated. They are `unknown`, and under ADR-0014 an unexamined criterion holds its capability at `partial` — so `4.5` and `4.6` cannot read `yes` until they are asked | A short follow-up pass with the same owners |
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

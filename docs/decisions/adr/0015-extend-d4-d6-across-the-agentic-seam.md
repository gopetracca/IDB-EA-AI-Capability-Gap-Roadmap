---
id: ADR-0015
title: Extend D4-D6 across the agentic seam
status: Accepted
date: 2026-09-09
depends_on: [ADR-0009, ADR-0010, ADR-0013, ADR-0014]
---

# ADR-0015 · Extend D4-D6 across the agentic seam

## Status

**Accepted** — 9 September 2026. Extends the taxonomy. Reverses nothing.

Closes `OPEN-ITEMS` #19, which proposed criterion `5.5.6 Tool Traffic Mediation`, by
deciding it differently: as a capability, not a criterion. §"Options considered" says why.

## Context

A completeness review of domains D4, D5 and D6
([`docs/analysis/d4-d6-completeness-review.md`](../../analysis/d4-d6-completeness-review.md))
tested the three domains four ways: a lifecycle sweep, a failure-mode sweep, an external
sweep against published models, and an internal consistency sweep over the `agentic` flag.

The first three found no missing job in the conventional AI build-run-operate lifecycle.
Every capability named by IBM's Generative AI Capability Model — the most detailed public
technical model — has a home here, usually at finer resolution.

The fourth sweep found the pattern the other three had been converging on. Counted from
`facts/capabilities.json` as it stood:

| Where agents are… | Capability | Agentic criteria |
|---|---|---|
| designed | 4.4 | 6 of 6 |
| catalogued | 5.5 | 5 of 5 |
| evaluated | 4.6 | **0 of 5** |
| released | 4.7 | **0 of 5** |
| quality-managed in production | 6.3 | **0 of 5** |
| hosted and executed | — | **no capability** |
| mediated at runtime | — | **no capability** |
| humanly supervised, day to day | — | **no capability** |

D5 held 29 criteria. Five were agentic and all five sat in one capability; provisioning,
model access, environments, compute and developer experience held 24 criteria and no
agentic criterion between them.

The model was agent-aware at design time and at inventory time, and agent-blind at
build-verify time, at runtime and at run-quality time. Three failures had no landing site
at all: an agent released after passing every response-quality gate that then takes a
correct-looking eleven-step tool sequence whose seventh step writes to a system of record;
a tool that returns injected instructions or personal data that enter context unexamined;
and an approval queue that backs up until reviewers clear it in bulk, with every individual
control on paper satisfied.

None of this was a gap in the *conventional* lifecycle. It was one seam.

## Decision

**Three capabilities are added, and eight criteria are added to existing capabilities.**

| New capability | Names |
|---|---|
| **5.7 AI Runtime Mediation & Egress Control** | The runtime chokepoint for *tool and agent* traffic, which 5.2.2 already is for *model* traffic — including what leaves through a tool call |
| **5.8 AI Agent Runtime & Execution Environment** | Where an agent executes, sandboxes generated code, keeps state, and is bounded |
| **6.7 Human Oversight Operations** | Running the oversight that 2.5 designs and 7.2.3 requires, at the volume production produces |

| Existing capability | Gains |
|---|---|
| 4.5 Integration & Tool Enablement | 4.5.6 Agent-to-Agent Interoperability |
| 4.6 AI Evaluation & Testing | 4.6.6 Agent Trajectory & Tool-Use Evaluation · 4.6.7 Simulation & Scenario-Based Testing · 4.6.8 Evaluator Validation & Judge Governance |
| 6.1 AI Deployment & Serving Operations | 6.1.6 Agent Fleet & Version Operations · 6.1.7 Provider Failover & Degraded-Mode Operation |
| 6.3 Continuous Evaluation, Drift & Quality Management | 6.3.6 Guardrail Effectiveness Monitoring & Tuning |
| 6.5 AI Cost Management | 6.5.5 Energy & Carbon Accounting for AI |

**The extension is additive.** No id is reused, renumbered or retired. Every existing
observation row, ADR reference and generated view keeps its meaning.

**The three new capabilities carry `confidence: low`** until their owners validate them,
under ADR-0009. **All 23 new criteria carry `practised: unknown`**, and the three new
capabilities carry `enabled` / `skilled` / `defined` at whatever the register and the
evidence actually support — `unknown` where nobody has looked (ADR-0013 Amendment 2).
Nothing here rates anything. It names things that can now be rated.

**A capability is warranted only where three things coincide**: a distinct accountable
owner, a failure with no current landing site, and no adequate home in an existing
capability. Where fewer than three coincide, it is a criterion. Where none does, it is an
offering or a use-case question, and it belongs in `facts/offerings.json` or
`facts/questions.json`, not here. This test is what kept the addition to three.

## Options considered

| Option | For | Against |
|---|---|---|
| **A — Three capabilities and eight criteria** *(chosen)* | Each new capability has a distinct owner in the Bank's own catalogue, a failure with no landing site, and no adequate home. Additive, so nothing renumbers | Takes the model to 55 capabilities and five `confidence: low` entries into the ADR-0009 validation round |
| B — Criteria only, no new capabilities | Cheapest. Keeps 52 | Buries a runtime control plane inside a design-time catalog capability, and buries the human-oversight run function inside a design capability. Neither could then be owned or funded separately — the objection §3.1 of the Gartner comparison makes against Gartner's own resolution |
| C — `5.5.6 Tool Traffic Mediation` as a criterion, per `OPEN-ITEMS` #19 | Already proposed and understood | A catalog is a design-time inventory; a gateway stands in the path of a call. In the Bank's catalogue the AI enabler claims *"AI Gateway"* while 5.5 maps to Integration Platform. Two jobs, two owners. A criterion inside someone else's capability cannot be funded |
| D — 5.7 and 5.8 merged into one platform capability | They are often bought as one product | Two owners: the AI enabler claims the gateway, Cloud and Infrastructure owns runtime and compute. The model's first rule is one accountable owner |
| E — Wait for a published capability model to name these | Maximum external authority | None exists at this resolution and none is coming. IBM's is ~40 boxes over the same ground. Waiting means the Bank has no place to record the three failures above |
| F — Add modality and task capabilities (speech-to-text, OCR, translation, …) | A leadership audience asks for a service menu | Rejected. These are **offerings**, not capabilities (`docs/glossary.md`): no distinct owner, failures already landing on 3.5.2, 3.3.1, 4.6.1, 2.5.2 and 6.3.1, and naming one forces about twenty siblings all rated by the same question — which is 5.1.1 asked twenty times. The service menu is `facts/offerings.json` plus a `facts/questions.json` entry |

## Consequences

**What becomes true.**

- D4-D6 goes from 19 capabilities / 95 criteria to **22 / 118**; the model from 52 / 258 to
  **55 / 281**. Agentic criteria in D4-D6 go from 19 to 34.
- `facts/observations.json` gains **32 rows** — 23 `practised` at criterion level, 9 at
  capability level — taking it from 414 to **446**.
- D5 stops being a domain with no agentic criteria outside one capability.
- The three failures named in Context now each land on a capability someone can be asked
  about.

**What becomes harder.**

- **Five capabilities carry `confidence: low`** into the ADR-0009 validation round — 1.5,
  2.6 and now 5.7, 5.8 and 6.7. The taxonomy review is now unambiguously the critical path.
- **6.7 is expected to return `NO MATCH` on ownership**, taking unowned capabilities from
  8 to 9. That is a finding about the Bank, not a defect in the model (`OPEN-ITEMS` #14),
  but it is an uncomfortable pairing: a new capability that nobody claims. It is recorded
  rather than avoided.
- **Two more capabilities recorded as `enabled: unknown`** — 5.7 and 6.7 — taking
  `OPEN-ITEMS` #15 from 24 to 26.
- The first `practised` round is 23 questions longer.

**What had to change as a result.**

- `facts/sources.json` gained five entries and eleven `normalize` mappings, and S31b's date
  was corrected — IMDA updated the agentic framework on 20 May 2026, after it was
  registered (ADR-0010, supersession).
- `facts/owners.json` gained three mapping rows; `facts/offerings.json` points OFF-02 at
  5.8.
- `OPEN-ITEMS` #19 closes. `CLAUDE.md` §1 counts change.
- Nothing in `build/` or `scales/` changed. The extension needed no code, which is the
  design working: a capability is data.

## Open

- **ADR-0009 validation of 5.7, 5.8 and 6.7.** They are named on the evidence in §8 of the
  review, not on an owner's confirmation. Until that comes back they are proposals wearing
  the right file format.
- **Whether 5.7 and 5.8 stay separate.** Option D is reversible in one direction only: if
  the Bank decides one team owns both, merging is easy; splitting later is not.
- **Whether 6.7 belongs in D6 at all.** It is placed there because the model separates
  design (D2, D4) from run (D6) from govern (D7) everywhere else. A reviewer may reasonably
  read it as belonging with 7.2.3. If so, that is a new ADR, not an edit to this one.
- **`3.5.6 Extraction & Transcription Fidelity`** was identified by the same review and is
  **not** added here: it is in domain D3, outside the scope reviewed. The evidence for it is
  that OFF-05 had to hang its extraction-confidence control on the generic 4.6.1 because no
  specific criterion exists.
- **NIST SP 800-218A** is now cited on 4.7 and 7.4. It was already the right source for
  both and was simply absent from the register.

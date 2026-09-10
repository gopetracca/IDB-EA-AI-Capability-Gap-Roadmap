# Are domains 4, 5 and 6 complete?

**A completeness review of AI Solution Engineering, AI Platform & Infrastructure and
AI Operations & Reliability, and the end state proposed for them**

Inter-American Development Bank · Enterprise Architecture
Version 1.1 · 9 September 2026 · **Applied** — [ADR-0015](../decisions/adr/0015-extend-d4-d6-across-the-agentic-seam.md)

> **Status, 9 September 2026: built.** Everything §6 proposes is now in `facts/`, recorded as
> a decision by [ADR-0015](../decisions/adr/0015-extend-d4-d6-across-the-agentic-seam.md). The
> model is **55 capabilities / 281 criteria / 446 observations**. `check` and 45 tests pass;
> `out/` is regenerated, workbook included. The three new capabilities carry
> `confidence: low` pending ADR-0009 validation, and `6.7` came back `NO MATCH` on ownership
> exactly as §7 predicted, taking unowned capabilities from 8 to 9.
>
> This document is kept as the analysis that produced the decision — the four sweeps, the
> rejected options and the verification boundary — not as a to-do list. §11 records what was
> done, in the order it was done.

---

## 1. The short answer

**Coverage of the conventional AI build-run-operate lifecycle is complete.** Across four
sweeps I could not find a job in engineering, platform provision or operations that D4-D6
fails to name somewhere. Compared against the most detailed public technical model — IBM's
Generative AI Capability Model, re-read on 9 September 2026 — every box IBM names has a home
in ours, usually at finer resolution.

**The incompleteness is real but it is not spread evenly. It is concentrated in one seam.**

> The model knows how to **design** an agent (4.4, six criteria, all agentic) and how to
> **inventory** one (7.7). It does not know how to **test** one, **where it runs**, **what
> mediates what it reaches**, or **how the humans supervising it are operated**.

That is not an impression. It falls out of the facts already in the repository:

| Where agents are… | Capability | Agentic criteria |
|---|---|---|
| **designed** | 4.4 Agent & Workflow Orchestration Design | **6 of 6** |
| **catalogued** | 5.5 Tool & Connector Catalog Management | **5 of 5** |
| integrated | 4.5 Integration & Tool Enablement | 3 of 5 |
| observed | 6.2 AI Monitoring & Observability | 2 of 5 |
| deployed | 6.1 AI Deployment & Serving Operations | 1 of 5 |
| contained | 6.4 AI Incident & Problem Management | 1 of 5 |
| **evaluated** | 4.6 AI Evaluation & Testing | **0 of 5** |
| **released** | 4.7 AI Release & Change Management | **0 of 5** |
| **quality-managed in production** | 6.3 Continuous Evaluation, Drift & Quality | **0 of 5** |
| **hosted and executed** | — | **no capability exists** |
| **mediated at runtime** | — | **no capability exists** |
| **humanly supervised, day to day** | — | **no capability exists** |

D5 carries 29 criteria. Five are agentic and all five sit in one capability. The other five
platform capabilities — provisioning, model access, environments, compute, developer
experience — hold **24 criteria and not one agentic criterion between them**. A platform
domain with no agentic criteria in it cannot be assessed on the workload the Bank is
actually about to run.

**The proposal: three new capabilities, eight new criteria on existing ones, fifteen on the
new ones.** D4-D6 goes from **19 capabilities / 95 criteria** to **22 / 118**; the model from
**52 / 258** to **55 / 281**. No renumbering — every addition is additive, so no existing id,
observation or ADR reference moves.

And on the premise behind the request: *"in an ideal world the capabilities would be backed
by a framework, but there seems to be nothing."* Half right, and the wrong half matters.
**No published capability model exists at this resolution** — that part is true and will stay
true. **Framework backing for the individual capabilities does exist**, more of it than the
current source register uses. §8 names it.

---

## 2. How completeness was tested

Four sweeps, deliberately different in kind, so that a gap has to survive all four to count.

**(a) Lifecycle sweep.** Walk an AI system from architecture decision to decommissioning and
ask, at each step, *which capability is rated when this is done badly?* Any step with no
answer is a candidate.

**(b) Failure sweep.** The method §3.3 of the Gartner comparison used: list plausible
failures and check each lands on a nameable, ownable capability. A failure with no landing
site is a gap; a failure that lands on three capabilities at once is a boundary problem.

**(c) External sweep.** IBM Generative AI Capability Model · CNCF cloud-native AI platform
material · enterprise MCP-gateway architectures (Kong, Tyk, Microsoft APIM, Google Agent
Gateway) · CSA agentic identity and registry work · OWASP GenAI Security Project agentic
guidance and the new Agent Control Standard · the A2A protocol · ISO/IEC test and quality
standards for AI · NIST SP 800-218A · Green Software Foundation SCI. What each names that we
do not.

**(d) Internal consistency sweep.** The distribution of the `agentic` flag across D4-D6,
computed from `facts/capabilities.json`.

Sweep (d) produced the table in §1 in about a second, and it turned out to be the same
finding sweeps (a)-(c) were converging on from three other directions. That agreement is why
this review recommends three capabilities rather than a longer list: the gaps that survive
all four sweeps are few, and they are all on one seam.

---

## 3. What is already strong, and should not be touched

Worth stating plainly, because a gap review that lists only gaps misrepresents the model.

- **4.1** carries ABB stewardship (4.1.6) and solution conformance certification (4.1.7).
  Most published models stop at "design and architect AI". These two are what make an
  architecture claim checkable.
- **4.3 Prompt & Context Engineering** exists as a first-class capability with versioning and
  a registry. IBM holds prompt work as three sub-items under model customization; treating
  prompts as controlled artifacts with a lifecycle is ahead of the published field.
- **5.2 Model Access & Traffic Management** names a *runtime chokepoint* — 5.2.2 — for model
  traffic. That single design move is what makes G2 below identifiable at all: the model
  already knows what a chokepoint capability looks like, it just has only one of the two it
  needs.
- **6.2.3 Agent Action & Tool-Call Observability** and **6.4.2 Containment & Kill-Switch
  Execution** are the two agentic criteria most often absent elsewhere. Both are here.
- **6.5.3 Unit Economics & Cost-per-Outcome** is the right shape — per outcome, not per
  month — and it is why G8 below is one criterion rather than a capability.
- **6.6** retires systems *with their evidence*, which almost nothing published does.

Cross-checked against IBM's categories: GenAI Operations, Model Hub, Model Hosting, Model
Customization, Model Monitoring and the Agentic AI grouping (routing and orchestration, tool
management and tool calling) all map onto existing capabilities. Two IBM items map only to
*design-time* capabilities of ours and have no runtime home — *conversational memory* and
*dynamic function generation*. Both fall inside G3.

---

## 4. The gaps

Eight, ordered by severity. Severity is judged on three things: whether a plausible failure
has no landing site, whether the missing thing has a distinct accountable owner, and whether
the Bank is exposed to it inside twelve months.

### G1 — Agents are never evaluated · **High** · 4.6

**Missing.** 4.6 has five criteria and none is agentic. Every one of them evaluates a
*response*: metrics, golden datasets, an automated harness, human review, acceptance testing.
None evaluates a *trajectory* — did the agent choose the right tool, pass the right
arguments, recover from a failed call, stop when it should have stopped, and complete the
task without taking an action nobody asked for.

**The failure with no landing site.** An agent passes every response-quality gate, is
released, and in production takes a correct-looking sequence of eleven tool calls, the
seventh of which writes to a system of record. Nothing in 4.6 would have caught it, and
today nothing in the model is rated down for it. 4.4.6 designs the stopping condition;
nothing tests that it holds.

**Backed by.** ISO/IEC TR 29119-11:2020 on testing AI-based systems, whose central subject is
the test-oracle problem and non-determinism — exactly the reason trajectory evaluation cannot
be a golden-dataset exercise. IMDA's Model AI Governance Framework for Agentic AI, technical
controls dimension. OWASP GenAI Security Project's agentic red-teaming taxonomy. ISO/IEC
25059:2023 for the quality-characteristic vocabulary.

**Proposed.** Three criteria on 4.6 — see §6.

### G2 — Tool and agent traffic has no runtime chokepoint · **High** · new capability

**Missing.** 5.2.2 routes *model* traffic through a controlled point that can observe and
enforce. There is no equivalent for *tool* traffic. 5.5 is a **catalog** — a design-time
inventory of what exists, approved, scoped and versioned. A catalog does not sit in the path
of a call. When an agent invokes a tool at 03:00, no capability in the model is accountable
for what mediated it.

This is `OPEN-ITEMS.md` #19, which proposed it as criterion **5.5.6**. **This review
recommends promoting it to a capability instead**, for the model's own first reason: one
accountable owner. In the Bank's catalogue the AI enabler claims *"AI Gateway"*; 5.5 maps to
Integration Platform. Cataloguing a tool and standing in the path of its invocation are two
jobs, two skill sets and two reporting lines. A criterion buried in someone else's capability
cannot be funded.

**The failure with no landing site.** A tool returns a document containing injected
instructions, or returns 400 rows of personal data that the agent then places in its context
and paraphrases into a reply. Egress — what leaves through a tool call — is not named
anywhere in the model. 7.4.3 detects injection as a security control; nothing provides the
place where the inspection happens.

**Backed by.** Convergent enterprise architecture rather than a standard: MCP gateways from
Kong, Tyk, Microsoft (APIM) and Google (Agent Gateway) all describe the same shape — a
control plane distributing policy, data-plane instances enforcing authentication,
authorization, routing, rate limiting and **outbound payload filtering before context
hydration**. The OWASP Agent Control Standard, donated to the OWASP GenAI Security Project
and announced 1 September 2026, is explicitly about extending agentic guidance "toward
practical runtime enforcement". IBM names *Tool Management and Tool Calling* under Agentic
AI. This is grade-B backing, and it is unanimous.

**Proposed.** New capability **5.7 AI Runtime Mediation & Egress Control**.

### G3 — Agents have nowhere to run · **High** · new capability

**Missing.** D5 provisions platform services (5.1), environments and workspaces for *teams*
(5.3), and compute (5.4). None of them is the runtime an agent executes in. There is no
capability for: the hosting substrate for a long-running agent, the sandbox in which
model-generated code or computer-use actions execute, the store that holds agent memory
between turns, or the resource and blast-radius limit that stops a looping agent from
consuming a quota.

4.4.4 *designs* what an agent retains and who else can see it. Nothing *provides* the store
that enforces it. That is the exact pattern of a design capability with no platform
counterpart — the same pattern G2 shows for traffic.

**The failure with no landing site.** An agent generates and executes code that reads the
filesystem of the host it runs on; or two teams' agents share a memory store and one reads
the other's context. Today the closest capability is 5.3.2 workspace tenancy, which is about
*people's* workspaces, and rating it would be wrong.

**Backed by.** OWASP *Securing Agentic Applications Guide 1.0*. CNCF cloud-native AI platform
material on multi-model isolation and multi-tenant governance in shared clusters. IBM's
*dynamic function generation* and *conversational memory*, both of which imply a runtime the
Bank does not currently name. Vendor sandbox patterns (agent evaluation sandboxes routing
traffic through a separate instance before production).

**Proposed.** New capability **5.8 AI Agent Runtime & Execution Environment**.

### G4 — Nobody operates the humans in the loop · **High** · new capability

**Missing.** 2.5 *designs* oversight and intervention. 7.2.3 *enforces* human agency as a
governance control. Neither *runs* the oversight function: the approval queue, its depth and
latency, the service level on a human decision, reviewer competence and rotation, the
override rate, and automation bias when a reviewer has approved 200 identical items.

The model already separates design (D2, D4) from run (D6) from govern (D7) everywhere else —
4.4 designs the agent, 6.1 runs it, 7.7 governs it. Oversight is the one control where the
run column is empty.

**The failure with no landing site.** The queue backs up, reviewers approve in bulk to clear
it, and every individual control on paper was satisfied. There is no capability whose rating
would fall.

**Backed by.** EU AI Act Article 14 (human oversight — understand, intervene, override) read
with Article 72 (post-market monitoring), where **operator override rate is treated as a
leading indicator of performance degradation** — a directly measurable criterion the model
currently has nowhere to record. IMDA's framework names *meaningful human accountability* as
one of four dimensions and added automation bias in its May 2026 update. ISO/IEC 42001 and
the GAO Accountability Framework both carry monitoring obligations of this shape.

**Proposed.** New capability **6.7 Human Oversight Operations**.

### G5 — Agent-to-agent interoperability is unnamed · **Medium** · 4.5

**Missing.** 4.5.3 exposes institutional capability to AI clients through "the prevailing open
tool-interface standard" — MCP. Agent-to-agent is a different plane: publishing a description
of what an agent can do, discovering another agent's, negotiating a task through a lifecycle,
and carrying identity across an organisational boundary. 4.5.4 carries the acting user's
identity to a system of record; it does not carry it to another agent.

**Backed by.** The A2A protocol, specification version **1.0.0**, governed by the Agentic AI
Foundation after Google's 2025 donation to the Linux Foundation. Agent Cards as signed
discovery metadata, a defined task lifecycle, standard enterprise auth schemes. This is a
real, versioned, openly readable specification — the same character as MCP, already source
S33 at grade A.

**Proposed.** Criterion **4.5.6**.

### G6 — Agents are deployed one at a time, and run as a fleet · **Medium** · 6.1

**Missing.** 6.1.1 deploys a model or agent. Nothing operates *many* of them: pinned versions
across a fleet, coordinated rollout when a shared model or tool moves underneath them,
behavioural regression when a dependency changes, and the drift in an agent's behaviour that
follows from a provider's model update rather than from its own release. 5.2.5 absorbs
provider-side version change at the access layer; 6.3 detects drift in outputs. Neither
operates the fleet.

Related and cheap: **model provider failover**. 6.1.4 commits to availability; 5.2.5 controls
which versions remain reachable. Failing over to a second provider under a defined
degradation policy is named by neither.

**Backed by.** CSA research on the enterprise agent-registry gap (no authoritative record of
which agents exist, what they may do, or whether runtime behaviour matches what was
approved). IMDA's May 2026 update on multi-agent systems and third-party agents. ITIL 4 for
the fleet-versus-instance distinction.

**Proposed.** Criteria **6.1.6** and **6.1.7**.

### G7 — Guardrails are designed and provided, never measured · **Medium** · 6.3

**Missing.** 4.4.5 designs the hard limits; 7.4.6 provides output filtering and content
safety as a security control. Nothing measures whether the guardrails are working in
production: block rate, false positives that make the system unusable, false negatives found
after the fact, and change control when a threshold is tuned. 6.3 measures the *system's*
quality; the guardrail is the part of the system whose failure is silent in both directions.

**Backed by.** NIST AI RMF Measure function. OWASP GenAI Security Project. ISO/IEC 42001
performance evaluation.

**Proposed.** Criterion **6.3.6**.

### G8 — AI consumption is counted in money and not in energy · **Medium-low** · 6.5

**Missing.** 6.5 meters consumption, attributes it, forecasts it and expresses it per
outcome. 7.2.5 makes environmental and social responsibility a governance obligation. Nothing
connects them: no capability produces the number 7.2.5 would need.

Cheap to close, and unusually well-shaped: 6.5.3 already expresses cost per outcome, and the
Software Carbon Intensity specification is a rate per functional unit. A token is a natural
functional unit. This is one criterion in an existing capability with an existing owner.

**Backed by.** Green Software Foundation SCI specification, adopted as **ISO/IEC
21031:2024**. The GSF specification is openly readable; the ISO adoption is paywalled — cite
the former, note the latter.

**Proposed.** Criterion **6.5.5**.

---

## 5. What is deliberately *not* proposed

A completeness review that adds everything it notices produces a taxonomy nobody can assess.
The bar applied here: a new capability needs **a distinct accountable owner**, **a failure
with no current landing site**, and **no adequate home in an existing capability**. All three,
or it is a criterion. All three plus real scope, or it is nothing.

| Considered | Verdict |
|---|---|
| **Secure SDLC for AI** as a capability | No. 4.7.1 (build and CI) and 7.4.2 (model and supply-chain integrity) hold it between them. **But cite NIST SP 800-218A on both** — it is grade A, free, and directly on point |
| **Vector / retrieval infrastructure** as a D5 capability | No. 3.6.1 Retrieval Service Provision already provides it, and 3.7.3 owns the index lifecycle |
| **Model optimization and efficiency engineering** (quantization, distillation, caching) | No. 6.5.4 holds the cost route and 4.1.4 the latency route. Revisit only if self-hosted open-weight serving becomes material |
| **LLM-as-judge governance** | Criterion, not capability — 4.6.8. Real, but it is a property of the evaluation harness |
| **AI-assisted software engineering** (coding assistants in the Bank's own SDLC) | **Not a gap — a scope question, and it should be settled explicitly.** The model has no home for provenance of AI-generated code, licence exposure, or review standards for it. It is arguably a use case like any other; it is arguably an engineering capability. Either answer is defensible; having no answer is not. Worth its own short ADR |
| **Post-market monitoring plan** as a distinct capability | No. 6.3 covers the substance; the *plan* as an artifact is a criterion of 7.6.4 if the Bank ever falls in scope |
| **AI service desk / end-user support** | No. 8.4.3 and 6.4 hold it |

---

## 6. The proposed end state

### D4 — AI Solution Engineering · 7 capabilities (unchanged) · 38 → 42 criteria

| Capability | Change |
|---|---|
| 4.1 AI Architecture Management & Solution Governance | — |
| 4.2 Model Selection, Customization & Tuning | — |
| 4.3 Prompt & Context Engineering | — |
| 4.4 Agent & Workflow Orchestration Design | — |
| **4.5 Integration & Tool Enablement** | **+ 4.5.6 Agent-to-Agent Interoperability** ▸*agentic* — publish and consume agent descriptions, negotiate a task through a defined lifecycle, and carry identity and authorization across an agent boundary |
| **4.6 AI Evaluation & Testing** | **+ 4.6.6 Agent Trajectory & Tool-Use Evaluation** ▸*agentic* — evaluate the path taken, not only the answer returned: tool selection, argument correctness, failure recovery, termination and task completion<br>**+ 4.6.7 Simulation & Scenario-Based Testing** ▸*agentic* — exercise the system against simulated users, environments and adversarial inputs before it can reach a system of record<br>**+ 4.6.8 Evaluator Validation & Judge Governance** — where a model does the grading, validate the grader against human judgement and monitor the grader's own drift |
| 4.7 AI Release & Change Management | — |

### D5 — AI Platform & Infrastructure · 6 → 8 capabilities · 29 → 39 criteria

| Capability | Change |
|---|---|
| 5.1-5.4, 5.6 | — |
| 5.5 Tool & Connector Catalog Management | — (the proposed 5.5.6 moves out and becomes 5.7.1) |
| **5.7 AI Runtime Mediation & Egress Control** *(new)* | *Able to stand in the path of every tool and agent call, and to control what goes out through it.*<br>Proposed owner: **AI Platform Owner** · Bank unit: **Artificial Intelligence** (claims *AI Gateway*) · anchor `new` · confidence `low` · agentic |
| | 5.7.1 Tool Traffic Mediation ▸*agentic* — route every tool invocation through a controlled point that can observe, authorize and refuse |
| | 5.7.2 Outbound Content & Data Egress Control ▸*agentic* — inspect what a tool returns before it enters context, and what a call carries out of the institution |
| | 5.7.3 Runtime Policy Distribution & Enforcement ▸*agentic* — distribute policy from one control plane and enforce it at every data-plane instance |
| | 5.7.4 Invocation Rate, Budget & Loop Enforcement ▸*agentic* — enforce per-agent call budgets and stop runaway invocation at the mediation point rather than in the agent's own code |
| | 5.7.5 Mediation Telemetry Hand-off ▸*agentic* — emit from the mediation point the record 6.2.3 and 7.8.2 depend on |
| **5.8 AI Agent Runtime & Execution Environment** *(new)* | *Able to give agents a governed place to execute, remember and be bounded.*<br>Proposed owner: **AI Platform Owner**, with a Cloud Platform dependency · Bank unit: **Artificial Intelligence** + **Cloud and Infrastructure** — *confirm* · anchor `new` · confidence `low` · agentic |
| | 5.8.1 Agent Hosting & Execution Runtime ▸*agentic* — provide the managed substrate an agent executes in |
| | 5.8.2 Code & Computer-Use Sandboxing ▸*agentic* — execute model-generated code and computer-use actions in an isolated, disposable environment |
| | 5.8.3 Agent Memory & State Infrastructure ▸*agentic* — provide the store that enforces what 4.4.4 designed: retention, isolation, and who else can read it |
| | 5.8.4 Long-Running Task & Scheduling Support ▸*agentic* — support work that outlives a request, including resumption and cancellation |
| | 5.8.5 Runtime Resource & Blast-Radius Limits ▸*agentic* — bound what a single agent execution can consume and reach |

### D6 — AI Operations & Reliability · 6 → 7 capabilities · 28 → 37 criteria

| Capability | Change |
|---|---|
| **6.1 AI Deployment & Serving Operations** | **+ 6.1.6 Agent Fleet & Version Operations** ▸*agentic* — operate many agents as a fleet: pinned versions, coordinated rollout, and detection of behavioural change caused by a dependency moving rather than by a release<br>**+ 6.1.7 Provider Failover & Degraded-Mode Operation** — fail over between model providers, or degrade deliberately, under a defined and exercised policy |
| 6.2 AI Monitoring & Observability | — |
| **6.3 Continuous Evaluation, Drift & Quality Management** | **+ 6.3.6 Guardrail Effectiveness Monitoring & Tuning** — measure block rate, false positives and after-the-fact false negatives, and change-control every threshold adjustment |
| 6.4 AI Incident & Problem Management | — |
| **6.5 AI Cost Management** | **+ 6.5.5 Energy & Carbon Accounting for AI** — express AI consumption per functional unit in energy and carbon, not only in money, and give 7.2.5 a number |
| 6.6 AI Asset Retirement & Evidence Preservation | — |
| **6.7 Human Oversight Operations** *(new)* | *Able to run the human supervision that 2.5 designed and 7.2.3 requires, at the volume production produces.*<br>Proposed owner: **AI Operations Owner**, jointly with the business process owner · Bank unit: **no claimant — expect a NO MATCH** · anchor `new` · confidence `low` · agentic |
| | 6.7.1 Review & Approval Queue Operation ▸*agentic* — run the queue an agent's actions wait in, with defined routing and coverage |
| | 6.7.2 Oversight Service Levels & Throughput Management — commit to and meet a latency and coverage standard for human decisions |
| | 6.7.3 Override & Intervention Rate Monitoring — monitor how often humans override, and treat a falling rate as a signal rather than as success |
| | 6.7.4 Reviewer Competence, Rotation & Automation-Bias Control — keep the reviewer capable of dissent |
| | 6.7.5 Oversight Evidence Capture — record the human decision so 7.8.2 can produce it later |

### Totals

| | Now | Proposed |
|---|---|---|
| D4-D6 capabilities | 19 | **22** |
| D4-D6 criteria | 95 | **118** |
| D4-D6 agentic criteria | 19 | **34** |
| Model total capabilities | 52 | **55** |
| Model total criteria | 258 | **281** |

No id changes. No renumbering. Every existing observation row stays valid.

---

## 7. What building it would change elsewhere

| Area | Effect |
|---|---|
| **ADRs** | One ADR to extend the taxonomy during ADR-0009 validation. It should also record the promotion of `OPEN-ITEMS` #19 from criterion 5.5.6 to capability 5.7, and why (one accountable owner). Optionally a second, short, on the AI-assisted-software-engineering scope question |
| **`OPEN-ITEMS.md` #19** | Closes — resolved as a capability, not a criterion |
| **`facts/observations.json`** | +23 `practised` rows (one per new criterion) and +9 capability-level rows (3 × 3 new capabilities) = **32 new rows, all `unknown`**. No level moves: every capability is unrated today because `practised` has never been observed |
| **`facts/owners.json`** | Three new mapping rows. 5.7 maps **Direct** to the AI enabler, which already claims *"AI Gateway"*. 5.8 is likely a split — confirm before recording. **6.7 will almost certainly be a NO MATCH**, taking the unowned count from 8 to 9. That is a finding to report, not a gap to fill |
| **`facts/offerings.json`** | The AI enabler claims an AI Gateway and **no offering in the register represents it**. That gap is worth chasing regardless of this proposal. OFF-02 *Foundry agents* would newly enable 5.8 |
| **`facts/sources.json`** | Six to eight new entries (§8), plus one correction: **S31b is out of date** |
| **`out/`** | Everything rebuilds. `out/capability-map.md`, the workbook, all three scale views, `out/provenance.md` and both reports carry new counts |
| **Review round** | The 32 new rows are 32 new questions on sheet 2. Worth timing with the first `practised` round rather than sending a second workbook |

---

## 8. What actually backs this — the premise, corrected

**There is no capability model at this resolution, and there will not be one.** IBM's is the
closest public technical model and it is roughly forty boxes over ground we cover with about
a hundred criteria; it is coarser than ours by design, exactly as the Gartner model is. That
part of the premise is correct and it is not a weakness — §3 of
`capability-model-comparison.md` already argues why.

**But "backed by a framework" and "traceable to a published capability model" are not the
same test**, and by the first test the position is much better than it was even a year ago.
Every proposal in §6 has something openable behind it:

| Proposal | Backing | Grade | Character |
|---|---|---|---|
| 4.6.6-4.6.8 agent evaluation | ISO/IEC TR 29119-11:2020 · ISO/IEC 25059:2023 · IMDA MGF for Agentic AI · OWASP agentic red-teaming taxonomy | C / C / A / A | Standards + framework |
| 4.5.6 agent-to-agent | **A2A specification v1.0.0**, Agentic AI Foundation | A/B | Protocol specification |
| 5.7 runtime mediation | OWASP **Agent Control Standard** (Sept 2026) · convergent MCP-gateway architectures (Kong, Tyk, Microsoft APIM, Google Agent Gateway) · IBM *Tool Management and Tool Calling* | A / B / B | Emerging standard + unanimous industry practice |
| 5.8 agent runtime | OWASP *Securing Agentic Applications Guide 1.0* · CNCF cloud-native AI platform material · IBM *dynamic function generation*, *conversational memory* | A / B / B | Practitioner guidance |
| 6.7 human oversight ops | **EU AI Act Art. 14 with Art. 72** (override rate as degradation indicator) · IMDA MGF, human accountability dimension · ISO/IEC 42001 · GAO framework | A / A / C / A | Regulation + framework |
| 6.1.6-6.1.7 fleet & failover | CSA agent-registry research · IMDA May 2026 multi-agent update · ITIL 4 | B / A / C | Research + framework |
| 6.3.6 guardrail effectiveness | NIST AI RMF **Measure** · OWASP GenAI Security Project · ISO/IEC 42001 | A / A / C | Framework |
| 6.5.5 energy & carbon | **GSF Software Carbon Intensity**, adopted as ISO/IEC 21031:2024 | A (GSF) / C (ISO) | Standard |
| *(not proposed, but cite it)* secure AI SDLC | **NIST SP 800-218A**, SSDF Community Profile for generative AI, 26 July 2024, free | A | Standard |

Four of these are candidates for the source register that are **openly available and dated** —
A2A, NIST SP 800-218A, the GSF SCI specification, and the CSA AI Controls Matrix. Under
ADR-0010 that is the grade that matters, and adding them would improve the register's grade
profile rather than dilute it.

**One correction the register needs anyway.** `facts/sources.json` carries **S31b IMDA
Agentic AI Framework at 2026-01-22**. IMDA published an **update dated 20 May 2026**
incorporating industry feedback on multi-agent systems, third-party agents and automation
bias. Under the `citing` skill's supersession rule this is a live finding independent of
whether anything in this proposal is built.

---

## 9. The verification boundary

Per the `citing` skill: what was actually opened on 9 September 2026, and what was not.

**Publisher page or official announcement opened; existence, title and date confirmed;
document body not opened:** ISO/IEC TR 29119-11:2020 (`iso.org`, Technical Report,
paywalled) · ISO/IEC 25059:2023 (`iso.org`; note **ISO/IEC DIS 25059** is in ballot, so a
revision is in flight) · ISO/IEC 21031:2024 (`iso.org`, paywalled) · NIST SP 800-218A
(`csrc.nist.gov`, final 26 July 2024, free PDF) · OWASP Agent Control Standard announcement
(`genai.owasp.org`, 1 September 2026) · IMDA factsheet (update dated 20 May 2026, page last
updated 21 May 2026) · IBM Generative AI Capability Model (`ibm.com/architectures`, page
states last updated 30 April 2025).

**Specification page opened directly:** A2A — the page states *Latest Released Version
1.0.0* and governance by the **Agentic AI Foundation**.

**Read in secondary summary only — treat as unverified until opened:** the A2A v1.0 release
date of 12 March 2026 · the CSA AI Controls Matrix figures (v1.1, 18 domains, 247 control
objectives — sources disagree between 243 and 247) · the internal structure and control set
of the OWASP Agent Control Standard, which the announcement does not give · OpenTelemetry
GenAI semantic conventions, reported as still **Development** status and **not stable**,
which is why 6.2 is left unchanged and no criterion here depends on them · EU AI Act
Articles 14 and 72, read through commentary rather than the Official Journal text.

**Not verified at all, and not relied on:** any claim about what a paywalled ISO clause
*says*, as opposed to that it exists and what it is titled.

Nothing in this document reproduces licensed analyst material, and nothing in it rests on a
grade-D source.

---

## 10. What is still open in the proposal itself

Three judgements a reviewer may take differently, stated so they are heard from us first.

1. **5.7 and 5.8 as two capabilities, or one.** They are often bought as one product. They
   are separated here because the Bank's own catalogue separates them — the AI enabler claims
   the AI Gateway, Cloud and Infrastructure owns runtime and compute — and because the model's
   first rule is one accountable owner. If the Bank decides one team owns both, merge them and
   drop to seven D5 capabilities.
2. **6.7 may read as a duplicate of 2.5 and 7.2.3.** It is not — design, enforce and run are
   already separated everywhere else in the model — but it is the addition most likely to be
   challenged, and it is also the one most likely to come back **NO MATCH** on ownership. That
   combination is uncomfortable and should be said out loud in the ADR.
3. **All three new capabilities would carry `confidence: low`** under ADR-0009, alongside 1.5
   and 2.6. That is five low-confidence capabilities out of 55 going into a validation round.
   Acceptable, but it makes the taxonomy review the critical path.

---

## 11. How it was built

Done on 9 September 2026 in this order, because `check` must pass at every step.

1. **ADR first.** `docs/decisions/adr/` — extend the taxonomy, promote #19 from criterion to
   capability, record the two-versus-one judgement. Use the `decisions` skill.
2. **Sources before capabilities.** Add the new entries to `facts/sources.json` with grades
   and `normalize` mappings, and correct S31b's date. `check` fails on a citation string that
   does not resolve, so the capabilities cannot land first. Use the `citing` skill.
3. **`facts/capabilities.json`** — 3 capabilities, 23 criteria, each with `sources`, `anchor`,
   `confidence: low`, `proposed_owner`, and `agentic` where it applies.
4. **`facts/observations.json`** — 32 new rows, all `unknown`, no evidence, no basis.
5. **`facts/owners.json`** — three mapping rows; expect 6.7 to be NO MATCH.
6. **`facts/offerings.json`** — point OFF-02 at 5.8; open the question of the missing AI
   Gateway offering.
7. `uv run python build/build.py check && uv run python build/build.py test`, then
   `... build.py all`.
8. **Update `OPEN-ITEMS.md`** — close #19, and add the unowned count moving from 8 to 9.

**Outcome.** `facts/` is consistent: 55 capabilities, 446 observations, 7 offerings, 20 assets,
45 sources, 1 question; 3 scales sound. 45 tests pass. Ten views and the workbook regenerated.
Nothing in `build/` or `scales/` changed — the extension needed no code, which is the design
working: a capability is data.

Two things were deliberately left undone. **`3.5.6 Extraction & Transcription Fidelity`** is
in domain D3, outside the scope reviewed, and is recorded as open in ADR-0015. **The missing
AI Gateway offering** — the AI enabler's catalogue claims one and `facts/offerings.json` has
no entry for it — is now visible as the reason `5.7` reads `enabled: unknown`, which is the
right way for it to surface.

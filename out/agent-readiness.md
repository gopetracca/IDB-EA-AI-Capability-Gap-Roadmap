# Can the Bank run AI agents?

**IDB Enterprise Architecture** · generated 2026-09-04

Short answer: **the Bank can provision and build agents to a published standard today. What it cannot yet do is operate them as an institution.** Both halves of that sentence are evidenced below.

---

## What exists, with the evidence

| Layer | What exists | Assets released | The whole distance to the next step |
|---|---|:-:|---|
| **Foundry platform** | STD-03, RA-02, IAC-04, IAC-05 | 4 of 4 | Nothing. A per-use-case runtime is correctly packaged here. |
| **Foundry agents** | STD-03, STD-07, RA-02, RA-05, IAC-04, IAC-05, IAC-02, STD-06 | 6 of 8 | Release two documents: the Foundry Agents Standard and its reference architecture. |
| **Custom MCP servers** | STD-02, RA-01, TPL-01, TPL-02, IAC-02, IAC-01, IAC-03 | 4 of 7 | Distribute template v2 and migrate v1 servers inside the July 2026 spec window. |
| **Agent design guidance** | STD-06 | 1 of 1 | Nothing pending. |

## What comes in the box

The twelve questions that decide whether an agent inherits its controls or every team rebuilds them. **0 of 12 answered.**

| Control | Status | Capability | Why it matters |
|---|:-:|:-:|---|
| Distinct workload identity per instance, not a shared service principal | **unanswered** | `7.4.4` | A shared service principal makes every agent's actions indistinguishable. Nothing downstream can attribute or revoke. |
| Automatic registration in the AI system / agent inventory | **unanswered** | `7.7.2` | An inventory that depends on teams remembering to register is not an inventory. |
| Tracing and tool-call logging enabled by default | **unanswered** | `6.2.2` | If it is not on by default it will not be there when you need to explain what an agent did. |
| Content filtering and safety controls on by default | **unanswered** | `7.4.6` | Opt-in safety is the control that is missing exactly when it is needed. |
| Prompt-injection defence configured | **unanswered** | `7.4.3` | Content the agent reads can instruct it. Prompt design alone does not stop this at run time. |
| Evaluation harness scaffolded in the template | **unanswered** | `4.6.3` | Without a harness in the template, evaluation happens once at launch and never again. |
| Cost attribution tags applied automatically | **unanswered** | `6.5.1` | Untagged consumption cannot be attributed, forecast or stopped. |
| A tested way to stop it and revoke its access | **unanswered** | `6.4.2` | An untested kill switch is an assumption, not a control. |
| Credential issuance and rotation handled by the platform | **unanswered** | `5.2.4` | Credentials created by hand are credentials nobody rotates. |
| Network isolation and private connectivity baseline | **unanswered** | `5.3.3` | Isolation applied per team is isolation applied inconsistently. |
| A hook for human approval of consequential actions | **unanswered** | `2.5.2` | Oversight designed into the platform is exercised; oversight written into policy is not. |
| Interaction log retention configured to policy | **unanswered** | `3.1.4` | Interaction logs are evidence. Retention set per project is evidence you cannot rely on. |

**What the platform never provides:** The agent itself: business rules, grounding data, evaluation criteria, human oversight design. Those remain with the delivery team.

---

## The capabilities this actually touches

"Can we build agents?" is not one question. It is these, with these owners.

| ID | Capability | Owner | Practised | Enabled | Skilled | Defined |
|---|---|---|:-:|:-:|:-:|:-:|
| `4.4` | Agent & Workflow Orchestration Design | Artificial Intelligence | ? | part | ? | part |
| `5.1` | AI Platform Service Provisioning | Artificial Intelligence | ? | part | ? | part |
| `5.5` | Tool & Connector Catalog Management | Artificial Intelligence | ? | part | ? | yes |
| `7.7` | AI System & Agent Inventory Management | Artificial Intelligence | ? | no | ? | ? |
| `2.5` | Human-AI Interaction & Oversight Design | People Experience - IBT | ? | yes | ? | yes |
| `4.5` | Integration & Tool Enablement | Core Platforms | ? | part | ? | yes |
| `7.4` | AI Security & Resilience | Cybersecurity | ? | no | ? | ? |
| `8.3` | AI Literacy & Awareness | Emerging Tech | ? | n-a | ? | ? |

---

## What this means

The enablers were built before the practice. In the terms of the scale this model uses, the Bank has assembled its **Level 2 and Level 3 enablers** — the tooling and the standards — while **Level 1, the practice itself, has never been observed**. That is precisely the complaint, stated in a way that names the fix.

| Who | What they do next |
|---|---|
| Platform team | Answer the twelve in-the-box questions. Release the two pre-release documents. Distribute template v2. |
| Product teams | Build against the standard, so there is practice to observe. |
| EA | Observe it. Record `practised` with named systems. |
| People | 8.3 literacy and 8.2 skills: no observation exists yet. |


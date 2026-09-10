# Can the Bank run AI agents?

**Inter-American Development Bank** · generated 2026-09-09

The claim being answered: *"We cannot run AI agents."*

Short answer: **The Bank can provision and build agents to a published standard today. What it cannot yet do is operate them as an institution. The enablers were built before the practice: the tooling and the standards exist, and whether the work is done on real systems has never been observed.**

*Finding recorded by EA on 2026-09-04. Everything below it is derived from the recorded facts and regenerates as they change.*

---

## What exists, with the evidence

| Offering | What exists | Assets released | The whole distance to complete |
|---|---|:-:|---|
| **Foundry platform** | STD-03, RA-02, IAC-04, IAC-05 | 4 of 4 | Nothing pending. |
| **Foundry agents** | STD-03, STD-07, RA-02, RA-05, IAC-04, IAC-05, IAC-02, STD-06 | 6 of 8 | Release STD-07 Foundry Agents Standard (Pre-release); RA-05 Foundry Agents Reference Architecture (Pre-release). |
| **Custom MCP servers** | STD-02, RA-01, TPL-01, TPL-02, IAC-02, IAC-01, IAC-03 | 4 of 7 | Release TPL-02 MCP Server Template v2 (C# / .NET) (Built, not yet distributed); IAC-01 Container App Environment (In review by DX); IAC-03 Container Registry (In review by DX). |
| **Agent design guidance** | STD-06 | 1 of 1 | Nothing pending. |

## What comes in the box

The 18 questions that decide whether a team inherits its controls or rebuilds them. **0 of 18 answered.**

| Offering | Control | Status | Capability | Why it matters |
|---|---|:-:|:-:|---|
| Foundry agents | Distinct workload identity per instance, not a shared service principal | **unanswered** | `7.4.4` | A shared service principal makes every agent's actions indistinguishable. Nothing downstream can attribute or revoke. |
| Foundry agents | Automatic registration in the AI system / agent inventory | **unanswered** | `7.7.2` | An inventory that depends on teams remembering to register is not an inventory. |
| Foundry agents | Tracing and tool-call logging enabled by default | **unanswered** | `6.2.2` | If it is not on by default it will not be there when you need to explain what an agent did. |
| Foundry agents | Content filtering and safety controls on by default | **unanswered** | `7.4.6` | Opt-in safety is the control that is missing exactly when it is needed. |
| Foundry agents | Prompt-injection defence configured | **unanswered** | `7.4.3` | Content the agent reads can instruct it. Prompt design alone does not stop this at run time. |
| Foundry agents | Evaluation harness scaffolded in the template | **unanswered** | `4.6.3` | Without a harness in the template, evaluation happens once at launch and never again. |
| Foundry agents | Cost attribution tags applied automatically | **unanswered** | `6.5.1` | Untagged consumption cannot be attributed, forecast or stopped. |
| Foundry agents | A tested way to stop it and revoke its access | **unanswered** | `6.4.2` | An untested kill switch is an assumption, not a control. |
| Foundry agents | Credential issuance and rotation handled by the platform | **unanswered** | `5.2.4` | Credentials created by hand are credentials nobody rotates. |
| Foundry agents | Network isolation and private connectivity baseline | **unanswered** | `5.3.3` | Isolation applied per team is isolation applied inconsistently. |
| Foundry agents | A hook for human approval of consequential actions | **unanswered** | `2.5.2` | Oversight designed into the platform is exercised; oversight written into policy is not. |
| Foundry agents | Interaction log retention configured to policy | **unanswered** | `3.1.4` | Interaction logs are evidence. Retention set per project is evidence you cannot rely on. |
| Custom MCP servers | Server registered in an approved-server registry before any client may call it | **unanswered** | `5.5.2` | A public registry entry is not enterprise approval. Discovery and approval are different registers. |
| Custom MCP servers | Acting user's identity propagated on-behalf-of to the system of record | **unanswered** | `4.5.4` | Without it every action looks like the service account and the audit trail names the wrong actor. |
| Custom MCP servers | Tool scopes issued at least privilege | **unanswered** | `5.5.3` | A tool that can do more than its purpose is the confused-deputy path. |
| Custom MCP servers | Traffic passes a gateway or policy enforcement point | **unanswered** | `7.4.5` | Per-server enforcement is enforcement that varies by team. |
| Custom MCP servers | Protocol revision pinned, with a migration plan for the July 2026 spec | **unanswered** | `5.5.5` | Roots, Sampling, Logging, RFC 7591 dynamic client registration and legacy HTTP+SSE are deprecated on defined timelines. Template v1 predates this. |
| Custom MCP servers | Tool calls audited with arguments and effect | **unanswered** | `6.2.3` | You cannot explain what an agent did without the call record. |

**What Foundry agents never provides:** The agent itself: business rules, grounding data, evaluation criteria, human oversight design. Those remain with the delivery team.

---

## The capabilities this actually touches

"Can the Bank run AI agents" is not one question. It is these, with these owners.

| ID | Capability | Owner | Practised | Enabled | Skilled | Defined |
|---|---|---|:-:|:-:|:-:|:-:|
| `4.4` | Agent & Workflow Orchestration Design | Artificial Intelligence | ? | part | ? | part |
| `5.1` | AI Platform Service Provisioning | Artificial Intelligence | ? | part | ? | part |
| `5.5` | Tool & Connector Catalog Management | Artificial Intelligence | ? | part | ? | yes |
| `7.7` | AI System & Agent Inventory Management | Artificial Intelligence | ? | ? | ? | ? |
| `2.5` | Human-AI Interaction & Oversight Design | People Experience - IBT | ? | yes | ? | yes |
| `4.5` | Integration & Tool Enablement | Core Platforms | ? | part | ? | yes |
| `7.4` | AI Security & Resilience | Cybersecurity | ? | ? | ? | ? |
| `8.3` | AI Literacy & Awareness | Emerging Tech | ? | n-a | ? | ? |

The in-the-box controls above also reach 7 further capabilities: `3.1`, `4.6`, `5.2`, `5.3`, `6.2`, `6.4`, `6.5`.

---

## What this means

| Who | What they do next |
|---|---|
| Platform team | Answer the in-the-box questions. Release the pre-release documents. Distribute template v2 and plan the v1 migration inside the MCP specification window. |
| Product teams | Build against the standard, so there is practice to observe. |
| Capability owners | Confirm what is actually practised, criterion by criterion, with named systems. |
| Cybersecurity, Data Management, Legal | Confirm whether an approved standard exists in their own domain. |
| Learning & Development | 8.3 literacy and 8.2 skills: no observation exists yet. |


# The capability map

**Inter-American Development Bank** · the taxonomy alone · generated 2026-09-09

> This page is the **map**, not the assessment. It carries no observations, no scale and no levels — nothing here says how good the Bank is at anything. It exists so the taxonomy can be argued with on its own terms before anything is measured against it ([ADR-0009](../docs/decisions/adr/0009-taxonomy-validated-before-scoring.md)). For what has been observed, see [`capability-assessment-level.md`](capability-assessment-level.md).

## The three levels

| | Count | What it is | Carries a level? | Carries an owner? |
|---|:-:|---|:-:|:-:|
| **L1 · Domain** | 8 | A reporting cluster. Groups capabilities so a reader can find them | no | no |
| **L2 · Capability** | 52 | Something the institution must be able to do. **The unit of assessment and of accountability** | yes | yes |
| **L3 · Criterion** | 258 | A specific practice that can actually be witnessed on a real system | no | no |

A domain is a **reporting cluster, not a lifecycle** — it does not imply a sequence, a team or a process ([ADR-0006](../docs/decisions/adr/0006-single-primary-home.md)). Every capability has exactly one primary home; where it plausibly belongs in two, one is chosen and the other relationship is expressed as a dependency rather than a second listing.

A capability is stated so that it **survives replacing every vendor**. If a line would have to be rewritten because a product was swapped, it is not a capability — it is an offering, and it lives in [`facts/offerings.json`](../facts/offerings.json) instead.

Criteria are the **checklist behind a judgement, not gates**. They are where *practised* is observed, because that is the level at which work is actually witnessed; the capability's value is derived from them ([ADR-0014](../docs/decisions/adr/0014-practised-is-observed-at-l3.md)). No criterion carries a level of its own.

## The eight domains

| | Domain | What it means | L2 | L3 |
|---|---|---|:-:|:-:|
| `D1` | **AI Strategy & Value Management** | Able to set direction for AI and convert it into measurable institutional value. | 5 | 26 |
| `D2` | **AI Demand & Solution Shaping** | Able to find, qualify and shape AI opportunities into deliverable, adoptable solutions. | 6 | 30 |
| `D3` | **Data & Knowledge Management** | Able to supply trusted, governed data and knowledge to AI systems. | 7 | 33 |
| `D4` | **AI Solution Engineering** | Able to design, build, customize and validate AI solutions to a defined standard. | 7 | 38 |
| `D5` | **AI Platform & Infrastructure** | Able to provide and sustain the technical means to build and run AI. | 6 | 29 |
| `D6` | **AI Operations & Reliability** | Able to run AI in production dependably, observably and affordably. | 6 | 28 |
| `D7` | **AI Governance, Risk, Security & Assurance** | Able to direct, control, protect and evidence the trustworthy use of AI. | 9 | 49 |
| `D8` | **AI People, Skills & Adoption** | Able to build and sustain the human side of AI: who does it, who can, and who will. | 6 | 25 |
| | | **Total** | **52** | **258** |

## How to read the tables below

| Column | What it tells you |
|---|---|
| **Owner** | The unit in the Bank's own product and enabler catalogue that claims this. **none** means nothing in the catalogue claims it — a finding, not a blank |
| **Anchor** | How this capability relates to the Bank's existing enterprise capability map. Provisional until a crosswalk exists ([ADR-0007](../docs/decisions/adr/0007-anchoring-is-provisional.md)) |
| **Conf.** | How confident we are in the line itself — its name, boundary and definition. `low` means it needs its owner's eyes before anything is scored against it |
| **L3** | How many criteria sit behind it |

**Anchor** takes three values:

| Anchor | Means | Count |
|---|---|:-:|
| `specialization` | An AI-specific narrowing of a capability the Bank already has. Should map onto an existing line | 18 |
| `new` | Genuinely new with AI. No existing line to map onto | 20 |
| `lens` | A view over capabilities that already exist elsewhere. **Unverified — these are the ones to challenge** | 14 |

---

## The map

### D1 · AI Strategy & Value Management

*Able to set direction for AI and convert it into measurable institutional value.*

| ID | Capability | Able to… | Owner | Anchor | Conf. | L3 |
|---|---|---|---|---|---|:-:|
| `1.1` | **AI Vision & Strategy Definition** | establish and maintain a stated institutional position on AI and keep it current. | Artificial Intelligence | new | medium | 5 |
| `1.2` | **AI Portfolio & Investment Management** | decide which AI work is funded, in what order, and when it stops. | Strategic Portfolio Management | lens | high | 5 |
| `1.3` | **Value Realization & Performance Reporting** | prove what AI actually delivered, to the standard a governing body accepts. | Strategic Portfolio Management | lens | high | 5 |
| `1.4` | **AI Sourcing & Partner Strategy** | decide what is built, bought or partnered, and to stay able to change that decision. | Strategic Resource Management | specialization | medium | 5 |
| `1.5` | **AI Ecosystem & Alliance Management** | hold external AI relationships that are not supplier contracts, and to stay operable when the ecosystem around them changes. | **none** | new | low | 6 |

<details><summary><code>1.1</code> AI Vision & Strategy Definition — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `1.1.1` | **AI Ambition & Positioning** | Define what role AI plays in the institutional mandate and how far the organization intends to go. |
| `1.1.2` | **AI Strategy Formulation & Refresh** | Produce and periodically revise an endorsed AI strategy with explicit scope and stated exclusions. |
| `1.1.3` | **Strategic Alignment to Institutional Priorities** | Trace every AI objective to a corporate goal, sector strategy or country program. |
| `1.1.4` | **AI Principles & Ethical Positioning** | Set the non-negotiable commitments that constrain all downstream AI decisions. |
| `1.1.5` | **Horizon Scanning & Technology Foresight** | Track emerging AI capability and judge what it changes for the institution. |

</details>

<details><summary><code>1.2</code> AI Portfolio & Investment Management — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `1.2.1` | **AI Investment Case Development** | Build comparable business cases stating cost, benefit and risk on a common basis. |
| `1.2.2` | **Portfolio Prioritization & Sequencing** | Rank and stage the AI portfolio against delivery capacity, risk appetite and dependency. |
| `1.2.3` | **Funding & Budget Allocation** | Route funds to AI work through a mechanism that survives audit and annual planning. |
| `1.2.4` | **Portfolio Balance & Exposure Management** | Keep the mix of experimental, scaling and production AI within stated tolerance. |
| `1.2.5` | **Stage-Gate & Investment Review** | Decide continuation, pivot or termination at defined decision points on recorded criteria. |

</details>

<details><summary><code>1.3</code> Value Realization & Performance Reporting — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `1.3.1` | **Benefit Definition & Baselining** | State expected benefit in measurable terms before build, with a recorded pre-intervention baseline. |
| `1.3.2` | **Value Tracking & Attribution** | Measure realized benefit and attribute it defensibly to the AI intervention rather than to trend. |
| `1.3.3` | **AI Performance Metrics & KPI Management** | Maintain the indicator set that describes AI performance institution-wide. |
| `1.3.4` | **Executive & Board Reporting** | Report AI status, risk and value to governing bodies at their cadence and in their language. |
| `1.3.5` | **Post-Implementation Review** | Assess delivered outcomes against the approved case and feed findings back into prioritization. |

</details>

<details><summary><code>1.4</code> AI Sourcing & Partner Strategy — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `1.4.1` | **Build / Buy / Partner Decisioning** | Choose the sourcing route per capability with recorded rationale and revisit triggers. |
| `1.4.2` | **AI Vendor & Model Provider Evaluation** | Assess providers on capability, trustworthiness, transparency and cost of exit. |
| `1.4.3` | **Contractual Safeguards & AI Clauses** | Secure rights covering data use, IP, indemnity, audit access and notification of model change. |
| `1.4.4` | **Concentration & Exit Risk Management** | Limit dependence on any single provider and keep a tested, costed exit path. |
| `1.4.5` | **Supplier Performance & Assurance Monitoring** | Monitor contracted providers against their obligations and assurance commitments for the life of the relationship. |

</details>

<details><summary><code>1.5</code> AI Ecosystem & Alliance Management — 6 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `1.5.1` | **Partnership Portfolio Definition** | Decide which external relationships the institution needs in order to hold AI capability it will not build itself. |
| `1.5.2` | **Research & Academic Collaboration** | Operate collaborations whose output is knowledge, method or evidence rather than a delivered system. |
| `1.5.3` | **Peer & Multilateral Cooperation** | Exchange AI practice, assets and evidence with counterpart institutions under agreed terms. |
| `1.5.4` | **Insourcing / Outsourcing Posture Management** | Set and periodically revisit which AI work is held internally and which is placed outside. |
| `1.5.5` | **Ecosystem Dependency & Continuity Management** | Track aggregate dependency across the external AI ecosystem and stay able to operate when a member changes, merges or exits. |
| `1.5.6` | **Partnership Value & Obligation Tracking** | Monitor what each relationship returns against what it obliges the institution to do. |

</details>

### D2 · AI Demand & Solution Shaping

*Able to find, qualify and shape AI opportunities into deliverable, adoptable solutions.*

| ID | Capability | Able to… | Owner | Anchor | Conf. | L3 |
|---|---|---|---|---|---|:-:|
| `2.1` | **Use Case Discovery & Intake** | surface candidate AI work and admit it through one controlled front door. | Artificial Intelligence | lens | high | 4 |
| `2.2` | **AI Use-Case Feasibility & Qualification** | judge, before build, whether a use case is technically and operationally deliverable and worth doing. | Enterprise Architecture | new | medium | 4 |
| `2.3` | **AI Product Management** | own an AI capability as a product across its life, not as a project that ends. | **none** | specialization | medium | 5 |
| `2.4` | **Business Process & Service Redesign** | change how work is actually done, not merely to add a model to an unchanged process. | Digital Transformation | specialization | medium | 6 |
| `2.5` | **Human-AI Interaction & Oversight Design** | design the human's role in the system, rather than assert oversight in policy alone. | People Experience - IBT | new | low | 6 |
| `2.6` | **AI Innovation & Incubation** | turn an untested AI idea into evidence, and evidence into either a funded product or a cheap, recorded stop. | Emerging Tech | new | low | 5 |

<details><summary><code>2.1</code> Use Case Discovery & Intake — 4 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `2.1.1` | **Opportunity Identification & Ideation** | Actively generate candidate use cases from business need rather than waiting for requests. |
| `2.1.2` | **Demand Intake & Triage** | Operate a single intake route that classifies and routes every AI request. |
| `2.1.3` | **Use Case Registration & Classification** | Record each candidate against a common taxonomy before any build effort begins. |
| `2.1.4` | **Duplicate & Reuse Screening** | Detect that a request is already solved, in flight, or satisfiable by an existing asset. |

</details>

<details><summary><code>2.2</code> AI Use-Case Feasibility & Qualification — 4 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `2.2.1` | **Technical & Data Feasibility Assessment** | Judge whether the data, models and integration required actually exist and are obtainable. |
| `2.2.2` | **Cost, Effort & Capacity Feasibility** | Estimate build and run cost, effort and the specialist capacity a use case would consume. |
| `2.2.3` | **Operational & Adoption Feasibility** | Judge whether the receiving business area can absorb, operate and sustain the change. |
| `2.2.4` | **Go / No-Go Determination** | Make and record a proceed decision with named accountability and stated conditions. |

</details>

<details><summary><code>2.3</code> AI Product Management — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `2.3.1` | **AI Product Definition & Roadmapping** | Define the product, its users, its boundary and its forward path. |
| `2.3.2` | **Requirements & Acceptance Criteria Management** | Express what good looks like precisely enough to be tested against. |
| `2.3.3` | **User Research & Feedback Integration** | Learn from actual use and feed it back into the product. |
| `2.3.4` | **Backlog & Release Planning** | Sequence work and commit to releases against capacity. |
| `2.3.5` | **Product Performance Ownership** | Hold a named owner accountable for the product's outcomes in production. |

</details>

<details><summary><code>2.4</code> Business Process & Service Redesign — 6 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `2.4.1` | **Process Analysis & AI Fit Assessment** | Understand the current process well enough to know where AI changes it. |
| `2.4.2` | **Target Process & Task Redesign** | Design the intended process, including what stops being done. |
| `2.4.3` | **Human / Machine Task Allocation** | Decide explicitly which tasks move, which stay, and which become supervisory. |
| `2.4.4` | **Control Point Redesign** | Relocate or rebuild the controls that the old process embedded in human steps. |
| `2.4.5` | **Service Model & Service Level Redefinition** | Restate the service promise once AI changes what is deliverable. |
| `2.4.6` | **Language Coverage & Service Equity** | Determine which languages an AI-delivered service must support, and at what measured quality, across the institution's countries. |

</details>

<details><summary><code>2.5</code> Human-AI Interaction & Oversight Design — 6 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `2.5.1` | **Autonomy & Interaction Pattern Determination** | Set and record, per system, the interaction pattern and how much an AI system or agent may do without human confirmation. |
| `2.5.2` | **Human Oversight & Intervention Design** | Design the specific point, information and control through which a human can intervene. |
| `2.5.3` | **Explanation & Disclosure Design** | Design what the system tells its user about what it is and how it reached an output. |
| `2.5.4` | **Escalation & Handover Design** | Design the path by which work returns to a human, with sufficient context to act. |
| `2.5.5` | **Oversight Competence & Workload Design** | Ensure the person assigned oversight has the time, information, training and authority to actually exercise it. |
| `2.5.6` | **Accessible & Inclusive Interaction Design** | Design AI-delivered interaction to be usable with assistive technology and across literacy and channel constraints. |

</details>

<details><summary><code>2.6</code> AI Innovation & Incubation — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `2.6.1` | **Idea Capture & Innovation Sourcing** | Collect candidate AI ideas from staff, partners and technology watch outside the formal demand route. |
| `2.6.2` | **Sandboxed Experimentation** | Run time-boxed experiments in an environment where failure is contained and permitted. |
| `2.6.3` | **Innovation Portfolio & Scaling Decisions** | Hold the set of live experiments within capacity and decide which of them scale. |
| `2.6.4` | **Experiment-to-Product Transition** | Move a proven experiment onto the funded delivery route, or record why it stops. |
| `2.6.5` | **Controlled Failure & Learning Capture** | Permit experiments to fail and extract reusable learning from the failure. |

</details>

### D3 · Data & Knowledge Management

*Able to supply trusted, governed data and knowledge to AI systems.*

| ID | Capability | Able to… | Owner | Anchor | Conf. | L3 |
|---|---|---|---|---|---|:-:|
| `3.1` | **Data Governance & Stewardship for AI** | say who owns each data asset, who may use it, and under what conditions. | Data Management | specialization | high | 5 |
| `3.2` | **Data Sourcing, Licensing & Provenance** | demonstrate lawful, documented origin for every dataset an AI system uses. | Data Management | specialization | high | 5 |
| `3.3` | **Data Quality & Preparation for AI** | make data fit for the specific AI purpose and to prove it was fit. | Data Management | specialization | medium | 5 |
| `3.4` | **Metadata, Lineage & Cataloging for AI** | find data, understand what it means, and trace where it went. | Data Management | specialization | high | 4 |
| `3.5` | **Knowledge Corpus & Content Management** | curate the document and content estate that grounded AI depends on. | Core Platforms | new | medium | 5 |
| `3.6` | **Knowledge Access & Retrieval** | return the right knowledge to the right requester, with its provenance intact. | Artificial Intelligence | new | low | 5 |
| `3.7` | **Derived Representation Management** | manage derived representations of data as governed assets in their own right. | Artificial Intelligence | new | low | 4 |

<details><summary><code>3.1</code> Data Governance & Stewardship for AI — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `3.1.1` | **Data Ownership & Stewardship Assignment** | Name an accountable owner and an operating steward for each data asset used by AI. |
| `3.1.2` | **Data Classification & Sensitivity Labeling** | Apply a consistent sensitivity classification that downstream controls can act on. |
| `3.1.3` | **Data Access Policy & Entitlement Management** | Define and enforce who may access which data, for which purpose. |
| `3.1.4` | **Data Retention & Records Management** | Apply retention and disposal rules to AI inputs, outputs and interaction records. |
| `3.1.5` | **Cross-Border Data Transfer Control** | Determine and enforce which jurisdictions the institution's data may be transferred to and processed in. |

</details>

<details><summary><code>3.2</code> Data Sourcing, Licensing & Provenance — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `3.2.1` | **Data Acquisition & Onboarding** | Bring external and internal data into the estate through a controlled route. |
| `3.2.2` | **Licensing & Permitted-Use Verification** | Confirm and record that intended AI use is permitted by the source's terms. |
| `3.2.3` | **Provenance & Chain-of-Custody Recording** | Record where data came from and every transformation applied to it. |
| `3.2.4` | **Consent & Purpose Limitation Management** | Track the basis on which data was collected and confine use to it. |
| `3.2.5` | **Synthetic Data Generation & Control** | Produce and govern synthetic data, including disclosure of its synthetic nature. |

</details>

<details><summary><code>3.3</code> Data Quality & Preparation for AI — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `3.3.1` | **Data Profiling & Quality Assessment** | Measure completeness, accuracy, timeliness and consistency against stated thresholds. |
| `3.3.2` | **Data Cleansing & Remediation** | Correct defects at source where possible, and record what was corrected downstream. |
| `3.3.3` | **Representativeness & Bias Screening** | Test datasets for gaps and skews relative to the affected population. |
| `3.3.4` | **Labeling & Annotation Management** | Produce, quality-check and version human and machine labels. |
| `3.3.5` | **Dataset Versioning & Snapshotting** | Freeze and identify the exact dataset a model or evaluation used. |

</details>

<details><summary><code>3.4</code> Metadata, Lineage & Cataloging for AI — 4 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `3.4.1` | **Data Catalog Management** | Maintain a searchable inventory of data assets with their attributes. |
| `3.4.2` | **Business Glossary & Semantic Definition** | Hold one agreed definition per business term that data assets bind to. |
| `3.4.3` | **Lineage Capture & Traceability** | Trace a model output back through transformations to source records. |
| `3.4.4` | **Data Product Publication** | Publish curated, contracted datasets that consumers can depend on. |

</details>

<details><summary><code>3.5</code> Knowledge Corpus & Content Management — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `3.5.1` | **Corpus Definition & Curation** | Decide what belongs in a knowledge corpus and what is deliberately excluded. |
| `3.5.2` | **Content Ingestion & Normalization** | Bring heterogeneous content into a consistent, machine-usable form. |
| `3.5.3` | **Content Segmentation Design** | Choose and apply segmentation that preserves meaning and citability. |
| `3.5.4` | **Corpus Freshness & Refresh Management** | Keep the corpus current and know how stale any part of it is. |
| `3.5.5` | **Authoritative Source Designation** | Declare which source wins when two documents disagree. |

</details>

<details><summary><code>3.6</code> Knowledge Access & Retrieval — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `3.6.1` | **Retrieval Service Provision** | Provide governed retrieval over institutional content — by meaning, by term, or both — as a reusable service. |
| `3.6.2` | **Access-Trimmed Retrieval Enforcement** | Enforce, at retrieval time, the entitlements determined in 3.1.3, so a requester sees only what they may see. |
| `3.6.3` | **Retrieval Quality Evaluation & Tuning** | Measure and improve retrieval precision and recall against a known set. |
| `3.6.4` | **Multi-Source Federation & Ranking** | Retrieve across several repositories and rank the combined result coherently. |
| `3.6.5` | **Citation, Grounding & Traceability** | Return every answer with the source it rests on, resolvable by the reader. |

</details>

<details><summary><code>3.7</code> Derived Representation Management — 4 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `3.7.1` | **Feature Engineering & Store Management** | Produce, share and reuse engineered features under version control. |
| `3.7.2` | **Embedding Model Selection & Versioning** | Choose embedding models deliberately and record which version produced which index. |
| `3.7.3` | **Index Lifecycle & Re-embedding** | Rebuild and migrate indexes when content or embedding models change. |
| `3.7.4` | **Derived Representation Governance** | Apply access, retention and residency controls to vector representations. |

</details>

### D4 · AI Solution Engineering

*Able to design, build, customize and validate AI solutions to a defined standard.*

| ID | Capability | Able to… | Owner | Anchor | Conf. | L3 |
|---|---|---|---|---|---|:-:|
| `4.1` | **AI Architecture Management & Solution Governance** | set, steward and enforce the architecture that AI solutions are built to. | Enterprise Architecture | lens | medium | 7 |
| `4.2` | **Model Selection, Customization & Tuning** | choose and adapt models on evidence, and to record what was done. | Artificial Intelligence | new | medium | 5 |
| `4.3` | **Prompt & Context Engineering** | treat prompts and context assembly as versioned, tested engineering artifacts. | Artificial Intelligence | new | medium | 5 |
| `4.4` | **Agent & Workflow Orchestration Design** | design what an agent may pursue, how it plans, and where it must stop. | Artificial Intelligence | new | low | 6 |
| `4.5` | **Integration & Tool Enablement** | give AI systems safe, governed reach into institutional systems. | Core Platforms | new | medium | 5 |
| `4.6` | **AI Evaluation & Testing** | state, before release, what the system does and does not do reliably. | **none** | new | medium | 5 |
| `4.7` | **AI Release & Change Management** | move AI change into production under control and to reverse it. | Core Platforms | lens | high | 5 |

<details><summary><code>4.1</code> AI Architecture Management & Solution Governance — 7 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `4.1.1` | **Solution Pattern Selection** | Choose the architecture building block that realizes the required capability. |
| `4.1.2` | **Reference Architecture Compliance** | Build to published reference architectures and detect deviation. |
| `4.1.3` | **Architecture Decision Recording** | Record significant decisions with alternatives and consequences. |
| `4.1.4` | **Non-Functional Requirement Design** | Design explicitly for latency, cost, availability, and degradation behavior. |
| `4.1.5` | **Architecture Review & Dispensation** | Review designs and grant time-boxed exceptions with recorded conditions. |
| `4.1.6` | **ABB & Pattern Stewardship** | Define, version and retire the institution's logical building blocks and the patterns that compose them. |
| `4.1.7` | **Solution Conformance Certification** | Certify that a concrete solution conforms to the building blocks and controls it claims, and record the deviations. |

</details>

<details><summary><code>4.2</code> Model Selection, Customization & Tuning — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `4.2.1` | **Model Selection for Use Case** | Select a model from within the cleared set against task-specific criteria and evidence. |
| `4.2.2` | **Fine-Tuning & Adaptation** | Adapt models to institutional context under controlled, repeatable procedure. |
| `4.2.3` | **Model Training & Experimentation** | Run and track experiments so results are reproducible. |
| `4.2.4` | **Model Documentation & Disclosure Production** | Produce model cards covering intended use, limits, data and evaluation results. |
| `4.2.5` | **Model Versioning & Registration** | Register every model version as an identifiable, ownable asset. |

</details>

<details><summary><code>4.3</code> Prompt & Context Engineering — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `4.3.1` | **Prompt Design & Templating** | Design prompts as reusable, parameterized templates rather than embedded strings. |
| `4.3.2` | **Prompt Versioning & Registry** | Version, review and register prompts as controlled artifacts. |
| `4.3.3` | **Context Assembly & Window Management** | Assemble context deliberately and manage what is included, ordered and dropped. |
| `4.3.4` | **Grounding Strategy Design** | Decide what the model is permitted to answer from, and enforce it. |
| `4.3.5` | **Prompt & Context Boundary Design** | Construct prompt and context boundaries that constrain what untrusted content can instruct. |

</details>

<details><summary><code>4.4</code> Agent & Workflow Orchestration Design — 6 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `4.4.1` | **Agent Specification & Goal Definition** | State an agent's objective, scope and prohibited actions before it is built. |
| `4.4.2` | **Task Decomposition & Planning Design** | Design how an agent breaks work down and selects its next step. |
| `4.4.3` | **Multi-Agent Coordination Design** | Design how agents delegate, communicate and resolve conflict. |
| `4.4.4` | **Agent Memory & State Design** | Design what an agent retains, for how long, and who else can see it. |
| `4.4.5` | **Guardrail & Constraint Design** | Encode hard limits an agent cannot argue its way past. |
| `4.4.6` | **Termination & Loop Control Design** | Design stopping conditions, budgets and loop detection. |

</details>

<details><summary><code>4.5</code> Integration & Tool Enablement — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `4.5.1` | **API & System Integration Design** | Design integration to institutional systems with contracts and error semantics. |
| `4.5.2` | **Tool & Function Definition** | Define the callable actions exposed to a model, with typed inputs and stated effects. |
| `4.5.3` | **Capability Exposure to AI Clients** | Expose institutional capability to AI clients through the prevailing open tool-interface standard. |
| `4.5.4` | **Identity Propagation & Delegated Access** | Carry the acting user's identity through to the system of record. |
| `4.5.5` | **Legacy & Core System Adaptation** | Reach systems that were never designed to be called by an AI client. |

</details>

<details><summary><code>4.6</code> AI Evaluation & Testing — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `4.6.1` | **Evaluation Criteria & Metric Definition** | Define the metrics that constitute acceptable performance for this use case. |
| `4.6.2` | **Golden Dataset & Test Set Management** | Build and maintain representative evaluation sets with known-correct answers. |
| `4.6.3` | **Automated Evaluation Harness Operation** | Run evaluations repeatably as part of the delivery pipeline. |
| `4.6.4` | **Human Review & Expert Evaluation** | Obtain qualified human judgement where automated metrics are insufficient. |
| `4.6.5` | **Pre-Deployment Acceptance Testing** | Test against acceptance criteria and record the result as release evidence. |

</details>

<details><summary><code>4.7</code> AI Release & Change Management — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `4.7.1` | **Build & Continuous Integration** | Build AI artifacts through an automated, auditable pipeline. |
| `4.7.2` | **Promotion & Environment Progression** | Move artifacts through environments under defined entry and exit criteria. |
| `4.7.3` | **Change Approval & Release Authorization** | Authorise AI change through a route proportionate to its risk tier. |
| `4.7.4` | **Rollback & Release Reversal** | Return a deployed AI system to a previously accepted release. |
| `4.7.5` | **Release Documentation & Evidence Capture** | Capture at release the evidence that later assurance work will need. |

</details>

### D5 · AI Platform & Infrastructure

*Able to provide and sustain the technical means to build and run AI.*

| ID | Capability | Able to… | Owner | Anchor | Conf. | L3 |
|---|---|---|---|---|---|:-:|
| `5.1` | **AI Platform Service Provisioning** | offer AI platform services as a governed, supported institutional service. | Artificial Intelligence | specialization | medium | 5 |
| `5.2` | **Model Access & Traffic Management** | control which models the institution may call, through one governed path. | Artificial Intelligence | new | low | 5 |
| `5.3` | **AI Environment & Workspace Management** | give teams isolated places to work without weakening controls. | Cloud and Infrastructure | lens | medium | 4 |
| `5.4` | **AI Compute & Capacity Management** | secure and allocate the compute that AI work requires. | Cloud and Infrastructure | specialization | medium | 5 |
| `5.5` | **Tool & Connector Catalog Management** | control what actions AI systems can reach, as a governed inventory. | Artificial Intelligence | new | low | 5 |
| `5.6` | **AI Developer Experience & Reuse Assets** | make the compliant path the easiest path for delivery teams. | Core Platforms | specialization | medium | 5 |

<details><summary><code>5.1</code> AI Platform Service Provisioning — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `5.1.1` | **Platform Service Catalog Management** | Publish what AI platform services exist, their terms and how to obtain them. |
| `5.1.2` | **Landing Zone & Baseline Provisioning** | Provision AI environments from a compliant baseline rather than by hand. |
| `5.1.3` | **Platform Configuration & Policy Enforcement** | Enforce configuration standards technically, not by instruction. |
| `5.1.4` | **Platform Service Level Commitment** | Commit to and meet service levels for the shared AI platform services the institution offers. |
| `5.1.5` | **Platform Upgrade & Deprecation Management** | Move consumers across platform versions without stranding them. |

</details>

<details><summary><code>5.2</code> Model Access & Traffic Management — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `5.2.1` | **Model Clearance & Approved Model List** | Assess candidate models against institutional criteria, record the clearance decision and its conditions, and maintain the approved list. |
| `5.2.2` | **Model Traffic Control & Routing** | Route all model traffic through a controlled point that can observe and enforce. |
| `5.2.3` | **Quota, Throttling & Rate Management** | Allocate and enforce consumption limits per consumer. |
| `5.2.4` | **Model Provider Credential Management** | Issue, rotate and revoke the credentials used to reach model providers and platform services. Agent identity is 7.4.4. |
| `5.2.5` | **Model Version Availability & Provider Change Control** | Control which model versions remain reachable and absorb provider-side version change without breaking consumers. |

</details>

<details><summary><code>5.3</code> AI Environment & Workspace Management — 4 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `5.3.1` | **Experimentation Environment Provision** | Provide safe environments for experimentation with clear data rules. |
| `5.3.2` | **Workspace Tenancy & Isolation** | Define and enforce the tenancy and isolation topology between team workspaces. |
| `5.3.3` | **Network & Private Connectivity Control** | Control network reachability of AI services and keep traffic private where required. |
| `5.3.4` | **Environment Data Segregation** | Prevent production data from reaching environments not cleared for it. |

</details>

<details><summary><code>5.4</code> AI Compute & Capacity Management — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `5.4.1` | **Compute Provisioning & Scheduling** | Make compute available to workloads on a predictable basis. |
| `5.4.2` | **Capacity Planning & Forecasting** | Forecast demand far enough ahead to secure supply. |
| `5.4.3` | **Accelerator & Quota Allocation** | Allocate scarce accelerator capacity against portfolio priority. |
| `5.4.4` | **Workload Placement & Residency Enforcement** | Place workloads in locations that enforce the transfer and residency decisions taken in 3.1.5. |
| `5.4.5` | **Edge & Disconnected Operation** | Run AI where connectivity, latency or residency prevents central serving, including fully offline. |

</details>

<details><summary><code>5.5</code> Tool & Connector Catalog Management — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `5.5.1` | **Tool & Connector Catalog Management** | Maintain the inventory of actions and connectors available to AI systems. |
| `5.5.2` | **Tool Source Registration & Approval** | Register and approve any source of callable tools before an AI client may reach it. |
| `5.5.3` | **Tool Permission & Scope Governance** | Set and enforce the scope each tool grants, at least privilege. |
| `5.5.4` | **Third-Party Tool Vetting** | Assess externally supplied tools and connectors before admission. |
| `5.5.5` | **Tool Version & Deprecation Control** | Manage tool change so agent behavior does not silently shift. |

</details>

<details><summary><code>5.6</code> AI Developer Experience & Reuse Assets — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `5.6.1` | **Reference Implementation & Template Provision** | Publish working templates that already embed required controls. |
| `5.6.2` | **SDK, Library & Component Curation** | Curate the approved libraries and shared components teams should build on. |
| `5.6.3` | **Self-Service Onboarding** | Let a team start correctly without a bespoke engagement. |
| `5.6.4` | **Inner-Source & Asset Reuse** | Make internally built assets discoverable and reusable across the institution. |
| `5.6.5` | **Developer Documentation & Support** | Document the platform to the standard its users actually need. |

</details>

### D6 · AI Operations & Reliability

*Able to run AI in production dependably, observably and affordably.*

| ID | Capability | Able to… | Owner | Anchor | Conf. | L3 |
|---|---|---|---|---|---|:-:|
| `6.1` | **AI Deployment & Serving Operations** | place AI systems into production and keep them serving. | Artificial Intelligence | specialization | medium | 5 |
| `6.2` | **AI Monitoring & Observability** | see what an AI system did, in enough detail to explain it afterwards. | Cloud and Infrastructure | specialization | medium | 5 |
| `6.3` | **Continuous Evaluation, Drift & Quality Management** | know that a system still performs as it did at release. | **none** | new | medium | 5 |
| `6.4` | **AI Incident & Problem Management** | stop AI harm quickly and account for it afterwards. | Service Delivery | lens | high | 5 |
| `6.5` | **AI Cost Management** | know what AI costs, per unit of value, and to control it. | Cloud and Infrastructure | lens | high | 4 |
| `6.6` | **AI Asset Retirement & Evidence Preservation** | retire AI systems deliberately, with their evidence preserved. | Service Delivery | lens | high | 4 |

<details><summary><code>6.1</code> AI Deployment & Serving Operations — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `6.1.1` | **Model & Agent Deployment** | Deploy models and agents into production through a controlled mechanism. |
| `6.1.2` | **Inference Serving & Scaling** | Serve inference at required throughput and scale it with demand. |
| `6.1.3` | **Configuration & Feature Flag Control** | Change runtime behavior safely without redeployment. |
| `6.1.4` | **System Availability & Continuity Management** | Meet availability and continuity commitments for individual AI systems in production. |
| `6.1.5` | **Operational Readiness & Handover** | Hand over to operations with documented procedures before go-live. |

</details>

<details><summary><code>6.2</code> AI Monitoring & Observability — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `6.2.1` | **Telemetry Instrumentation & Collection** | Instrument AI systems to emit the signals operations and assurance need. |
| `6.2.2` | **Trace & Interaction Logging** | Record prompts, context, outputs and decisions to a defined retention standard. |
| `6.2.3` | **Agent Action & Tool-Call Observability** | See every action an agent took, with what arguments and to what effect. |
| `6.2.4` | **Alerting & Threshold Management** | Detect abnormal behavior and raise it to someone who can act. |
| `6.2.5` | **Operational Dashboarding** | Present operational state to the people accountable for it. |

</details>

<details><summary><code>6.3</code> Continuous Evaluation, Drift & Quality Management — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `6.3.1` | **Production Output Quality Monitoring** | Measure output quality on live traffic, not only on test sets. |
| `6.3.2` | **Data & Concept Drift Detection** | Detect when inputs or the world have moved away from training conditions. |
| `6.3.3` | **Bias & Fairness Monitoring in Production** | Monitor outcome disparities on live populations over time. |
| `6.3.4` | **Feedback Capture & Ground-Truth Collection** | Capture corrections and outcomes to build evolving ground truth. |
| `6.3.5` | **Retraining & Refresh Triggering** | Trigger retraining or refresh on defined conditions rather than on schedule alone. |

</details>

<details><summary><code>6.4</code> AI Incident & Problem Management — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `6.4.1` | **AI Incident Detection & Classification** | Recognise an AI incident as distinct from a conventional IT incident. |
| `6.4.2` | **Containment & Kill-Switch Execution** | Stop a model or agent immediately, at any hour, with a tested mechanism. |
| `6.4.3` | **Root Cause Analysis** | Establish why an AI system behaved as it did, including at the data and prompt level. |
| `6.4.4` | **Regulatory & Stakeholder Notification** | Notify the parties an incident obliges the institution to notify, within the deadline. |
| `6.4.5` | **Corrective Action & Lessons Learned** | Close findings and feed them back into design and control. |

</details>

<details><summary><code>6.5</code> AI Cost Management — 4 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `6.5.1` | **Consumption Metering & Attribution** | Attribute token, compute and storage consumption to an owner. |
| `6.5.2` | **Cost Forecasting & Budget Control** | Forecast AI spend and stop it exceeding authorization. |
| `6.5.3` | **Unit Economics & Cost-per-Outcome** | Express cost per transaction, per document or per outcome, not per month. |
| `6.5.4` | **Optimization & Rightsizing** | Reduce cost through model, caching and routing choices without losing quality. |

</details>

<details><summary><code>6.6</code> AI Asset Retirement & Evidence Preservation — 4 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `6.6.1` | **Periodic Recertification & Review** | Re-confirm at defined intervals that a system should remain in service. |
| `6.6.2` | **Deprecation & Sunset Planning** | Plan and communicate withdrawal before it happens. |
| `6.6.3` | **Decommissioning & Data Disposition** | Remove the system and dispose of its data under retention rules. |
| `6.6.4` | **Archive & Evidence Preservation** | Preserve the records that assurance and legal obligations require after retirement. |

</details>

### D7 · AI Governance, Risk, Security & Assurance

*Able to direct, control, protect and evidence the trustworthy use of AI.*

| ID | Capability | Able to… | Owner | Anchor | Conf. | L3 |
|---|---|---|---|---|---|:-:|
| `7.1` | **AI Policy, Standards & Management System** | operate a functioning management system for AI, not a policy document. | Artificial Intelligence | specialization | medium | 6 |
| `7.2` | **Responsible & Trustworthy AI Practice** | make the institution's stated AI principles operative in delivered systems. | **none** | new | medium | 5 |
| `7.3` | **AI Risk Management** | identify, treat and monitor AI risk within a stated appetite. | Risk, Audit & Compliance | specialization | high | 6 |
| `7.4` | **AI Security & Resilience** | defend AI systems against attack, including attacks that use the AI itself. | Cybersecurity | new | medium | 7 |
| `7.5` | **Privacy & Data Protection for AI** | use personal data in AI without breaching the institution's obligations. | **none** | specialization | high | 5 |
| `7.6` | **Legal, Regulatory & Contractual Compliance for AI** | know which obligations bind the institution and to demonstrate compliance. | **none** | specialization | medium | 6 |
| `7.7` | **AI System & Agent Inventory Management** | state, at any moment, every AI system and agent in operation and who owns it. | Artificial Intelligence | new | low | 5 |
| `7.8` | **AI Assurance & Evidence Management** | produce and retain evidence about AI that an independent reviewer can rely on. Independent assessment of that evidence is Internal Audit's, not this capability's. | IT Risk (Compliance) | specialization | medium | 4 |
| `7.9` | **AI Impact Assessment & Risk Classification** | determine, independently of the team proposing a use case, what impact it may have and what risk tier it belongs to. | **none** | specialization | low | 5 |

<details><summary><code>7.1</code> AI Policy, Standards & Management System — 6 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `7.1.1` | **AI Management System Operation** | Operate the AIMS itself — scope, objectives, reviews, continual improvement. |
| `7.1.2` | **AI Policy Development & Maintenance** | Issue and maintain the institutional AI policy set. |
| `7.1.3` | **Standards & Technical Guideline Issuance** | Translate policy into standards a delivery team can actually build to. |
| `7.1.4` | **Governance Body & Decision Rights Operation** | Run the forums that decide AI matters, with defined authority. |
| `7.1.5` | **Exception & Dispensation Management** | Grant, time-box and track departures from standard. |
| `7.1.6` | **Conformance Monitoring** | Detect where practice has diverged from policy without waiting for audit. |

</details>

<details><summary><code>7.2</code> Responsible & Trustworthy AI Practice — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `7.2.1` | **Fairness Standard Setting & Adjudication** | Set the fairness standard per use case, adjudicate measured disparity against it, and mandate remediation. Measurement is 6.3.3. |
| `7.2.2` | **Transparency & Explainability Provision** | Provide explanation proportionate to the decision's consequence. |
| `7.2.3` | **Human Agency & Oversight Enforcement** | Verify that designed oversight is actually exercised in operation. |
| `7.2.4` | **Contestability & Redress Handling** | Give affected people a route to challenge an AI-influenced outcome. |
| `7.2.5` | **Environmental & Social Responsibility** | Account for the environmental and social footprint of AI use. |

</details>

<details><summary><code>7.3</code> AI Risk Management — 6 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `7.3.1` | **AI Risk Identification & Taxonomy** | Maintain a common taxonomy of AI risks the institution recognizes. |
| `7.3.2` | **Risk Assessment & Scoring** | Assess AI risks consistently enough to compare them across the portfolio. |
| `7.3.3` | **Control Design & Treatment Planning** | Design proportionate controls and record accepted residual risk. |
| `7.3.4` | **Risk Appetite & Tolerance Setting** | State how much AI risk the institution will carry, by category. |
| `7.3.5` | **Risk Monitoring & Reporting** | Track risk position over time and report it to accountable bodies. |
| `7.3.6` | **Independent Model Risk Validation** | Validate consequential models independently of the team that built them. |

</details>

<details><summary><code>7.4</code> AI Security & Resilience — 7 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `7.4.1` | **AI Threat Modeling** | Model threats specific to AI systems, not only to their hosting infrastructure. |
| `7.4.2` | **Model & Supply Chain Integrity** | Verify the provenance and integrity of models, weights and dependencies. |
| `7.4.3` | **Injection & Jailbreak Detection and Response** | Detect subversion attempts in live traffic and respond to them. |
| `7.4.4` | **Agent Identity & Credential Lifecycle** | Issue, sponsor, rotate and revoke a distinct identity per agent, rather than a shared service account. |
| `7.4.5` | **Runtime Authorization & Action Control** | Authorise each consequential action at the moment it is attempted. |
| `7.4.6` | **Output Filtering & Content Safety** | Prevent unsafe or disclosing output from reaching its recipient. |
| `7.4.7` | **Adversarial & Red-Team Testing** | Actively attempt to make AI systems fail or misbehave, before release and on a recurring basis thereafter. |

</details>

<details><summary><code>7.5</code> Privacy & Data Protection for AI — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `7.5.1` | **Privacy Impact Assessment for AI** | Assess privacy impact where AI processing introduces new exposure. |
| `7.5.2` | **Personal Data Minimization & Masking** | Reduce personal data to what the purpose requires before it reaches a model. |
| `7.5.3` | **Data Subject Rights Handling** | Answer access, correction and objection requests where AI is involved. |
| `7.5.4` | **Confidentiality & Non-Disclosure Control** | Prevent confidential material leaving through model providers or outputs. |
| `7.5.5` | **Training-Data Privacy Controls** | Control whether institutional data may be used to train provider models. |

</details>

<details><summary><code>7.6</code> Legal, Regulatory & Contractual Compliance for AI — 6 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `7.6.1` | **Regulatory Horizon Monitoring** | Track AI regulation across the jurisdictions the institution operates in. |
| `7.6.2` | **Applicability & Obligation Mapping** | Determine which obligations apply to which AI system, and record why. |
| `7.6.3` | **Intellectual Property & Copyright Control** | Manage IP exposure in both training inputs and generated outputs. |
| `7.6.4` | **Records, Disclosure & Registration Obligations** | Meet registration, logging and disclosure duties on time. |
| `7.6.5` | **Institutional Legal Status Determination** | Determine, as a prerequisite to any obligation mapping, how the institution's international legal status affects which AI regimes apply. Not a maturity dimension — a legal determination that exists or does not. |
| `7.6.6` | **Regulatory Role Determination** | Establish whether the institution acts as provider, deployer or distributor for each AI system, as the prerequisite to obligation mapping. |

</details>

<details><summary><code>7.7</code> AI System & Agent Inventory Management — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `7.7.1` | **AI System Registration** | Register every AI system before it reaches production, with mandatory attributes. |
| `7.7.2` | **Agent Registration & Attribute Recording** | Record each agent in the inventory with its owner, purpose, scope and identity reference. |
| `7.7.3` | **Ownership & Accountability Recording** | Record a named accountable individual for every registered AI system and keep it current as people and teams change. |
| `7.7.4` | **Shadow AI Discovery** | Find AI in use that was never registered. |
| `7.7.5` | **Inventory Completeness Assurance** | Test that the inventory is actually complete rather than assumed to be. |

</details>

<details><summary><code>7.8</code> AI Assurance & Evidence Management — 4 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `7.8.1` | **Control Testing & Assurance Planning** | Plan and perform first- and second-line testing of AI controls on a risk basis. |
| `7.8.2` | **Evidence Management & Audit Trail** | Retain evidence in a form an auditor can rely on, without reconstruction. |
| `7.8.3` | **External Certification & Attestation** | Obtain and maintain external certification where it is required or valuable. |
| `7.8.4` | **Finding Remediation Tracking** | Close audit and assurance findings and evidence the closure. |

</details>

<details><summary><code>7.9</code> AI Impact Assessment & Risk Classification — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `7.9.1` | **AI System Impact Assessment** | Conduct the structured impact assessment on affected individuals and groups per ISO/IEC 42005. |
| `7.9.2` | **Rights Impact Assessment Determination** | Determine whether a fundamental-rights impact assessment is required for a use case, and conduct it where it is. |
| `7.9.3` | **Risk Classification & Tiering** | Assign each use case to a risk tier that determines the controls it must carry. |
| `7.9.4` | **Classification Review & Reclassification** | Re-examine impact and risk tier when purpose, data, autonomy or affected population materially change. |
| `7.9.5` | **Independent Challenge of First-Line Classification** | Challenge and, where warranted, overturn a proposing team's own assessment of impact or risk tier. |

</details>

### D8 · AI People, Skills & Adoption

*Able to build and sustain the human side of AI: who does it, who can, and who will.*

| ID | Capability | Able to… | Owner | Anchor | Conf. | L3 |
|---|---|---|---|---|---|:-:|
| `8.1` | **AI Operating Model & Decision Rights** | say who decides what about AI, and who does the work. | Strategic Portfolio Management | lens | high | 4 |
| `8.2` | **AI Skills & Specialist Capability Building** | grow and retain the specialist skill the portfolio depends on. | Strategic Resource Management | lens | high | 4 |
| `8.3` | **AI Literacy & Awareness** | ensure everyone who uses or is affected by AI understands enough to act safely. | Emerging Tech | new | medium | 4 |
| `8.4` | **AI Adoption, Enablement & Support** | convert delivered AI capability into actual, sustained use. | Artificial Intelligence | lens | high | 5 |
| `8.5` | **AI Change Management & Workforce Transition** | carry the workforce through the change AI causes. | Digital Transformation | lens | high | 5 |
| `8.6` | **AI Community & Reuse Culture** | make institutional learning about AI compound rather than repeat. | Emerging Tech | lens | high | 3 |

<details><summary><code>8.1</code> AI Operating Model & Decision Rights — 4 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `8.1.1` | **Operating Model Design** | Choose and maintain the centralized, federated or hybrid model for AI work. |
| `8.1.2` | **Role & Responsibility Definition** | Define the AI roles the institution needs and what each is accountable for. |
| `8.1.3` | **Decision Rights & Escalation Paths** | State who may decide what, and where a disagreement goes. |
| `8.1.4` | **Capacity & Resourcing Management** | Match available skilled capacity to the committed portfolio. |

</details>

<details><summary><code>8.2</code> AI Skills & Specialist Capability Building — 4 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `8.2.1` | **Skills Taxonomy & Assessment** | Define the AI skills required and assess where the institution stands. |
| `8.2.2` | **Training & Certification Delivery** | Deliver structured learning against identified gaps. |
| `8.2.3` | **Recruitment & Talent Acquisition** | Acquire skills the institution cannot build in time. |
| `8.2.4` | **Career Pathways & Retention** | Give AI practitioners a reason to stay. |

</details>

<details><summary><code>8.3</code> AI Literacy & Awareness — 4 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `8.3.1` | **Baseline AI Literacy Delivery** | Deliver a common minimum level of AI understanding across the institution. |
| `8.3.2` | **Role-Specific Awareness** | Give each role the specific understanding its AI exposure requires. |
| `8.3.3` | **Acceptable Use Communication** | Make clear, in practical terms, what staff may and may not do with AI. |
| `8.3.4` | **Literacy Coverage Evidence** | Evidence who has received what AI training, to the standard the institution's own policy sets. |

</details>

<details><summary><code>8.4</code> AI Adoption, Enablement & Support — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `8.4.1` | **Adoption Planning & Targeting** | Plan adoption deliberately rather than assuming availability creates use. |
| `8.4.2` | **User Onboarding & Enablement** | Bring new users to competent use quickly. |
| `8.4.3` | **User Support Provision** | Answer users when AI behaves unexpectedly. |
| `8.4.4` | **Adoption Measurement** | Measure real usage and depth of use, not licenses issued. |
| `8.4.5` | **Champion Network Operation** | Sustain distributed advocates who carry adoption locally. |

</details>

<details><summary><code>8.5</code> AI Change Management & Workforce Transition — 5 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `8.5.1` | **Change Impact Assessment** | Assess what AI changes for specific roles and teams before it lands. |
| `8.5.2` | **Stakeholder Engagement & Communication** | Engage those affected early enough to influence the design. |
| `8.5.3` | **Workforce Transition & Redeployment** | Move people whose work changes into work that is needed. |
| `8.5.4` | **Staff Consultation & Representation** | Consult staff representation where AI changes conditions of work. |
| `8.5.5` | **Trust & Resistance Management** | Address well-founded concern rather than treating it as an obstacle. |

</details>

<details><summary><code>8.6</code> AI Community & Reuse Culture — 3 criteria</summary>

| L3 | Criterion | The practice |
|---|---|---|
| `8.6.1` | **Practitioner Community Operation** | Sustain a working community across organizational boundaries. |
| `8.6.2` | **Knowledge Sharing & Documentation** | Capture what was learned in a form others can find and use. |
| `8.6.3` | **Reuse Incentives & Recognition** | Make reuse and contribution visibly worth doing. |

</details>

---

## What to challenge first

The three lists a reviewer should go at, and why each one is here.

### 10 capabilities carry low confidence

The line itself is not yet trusted — its name, its boundary or whether it should exist at all. Nothing should be scored against these until their owner has looked.

| ID | Capability | Owner |
|---|---|---|
| `1.5` | AI Ecosystem & Alliance Management | **none** |
| `2.5` | Human-AI Interaction & Oversight Design | People Experience - IBT |
| `2.6` | AI Innovation & Incubation | Emerging Tech |
| `3.6` | Knowledge Access & Retrieval | Artificial Intelligence |
| `3.7` | Derived Representation Management | Artificial Intelligence |
| `4.4` | Agent & Workflow Orchestration Design | Artificial Intelligence |
| `5.2` | Model Access & Traffic Management | Artificial Intelligence |
| `5.5` | Tool & Connector Catalog Management | Artificial Intelligence |
| `7.7` | AI System & Agent Inventory Management | Artificial Intelligence |
| `7.9` | AI Impact Assessment & Risk Classification | **none** |

### 14 capabilities are lenses over existing ones

Each is a view over capabilities that already exist somewhere in the Bank's map rather than a new line of its own. The anchoring is **unverified**: it rests on judgement, not on a crosswalk against the Bank's enterprise capability map. This is why [ADR-0007](../docs/decisions/adr/0007-anchoring-is-provisional.md) must be carved out of any approval request until that crosswalk exists.

| ID | Capability | Owner |
|---|---|---|
| `1.2` | AI Portfolio & Investment Management | Strategic Portfolio Management |
| `1.3` | Value Realization & Performance Reporting | Strategic Portfolio Management |
| `2.1` | Use Case Discovery & Intake | Artificial Intelligence |
| `4.1` | AI Architecture Management & Solution Governance | Enterprise Architecture |
| `4.7` | AI Release & Change Management | Core Platforms |
| `5.3` | AI Environment & Workspace Management | Cloud and Infrastructure |
| `6.4` | AI Incident & Problem Management | Service Delivery |
| `6.5` | AI Cost Management | Cloud and Infrastructure |
| `6.6` | AI Asset Retirement & Evidence Preservation | Service Delivery |
| `8.1` | AI Operating Model & Decision Rights | Strategic Portfolio Management |
| `8.2` | AI Skills & Specialist Capability Building | Strategic Resource Management |
| `8.4` | AI Adoption, Enablement & Support | Artificial Intelligence |
| `8.5` | AI Change Management & Workforce Transition | Digital Transformation |
| `8.6` | AI Community & Reuse Culture | Emerging Tech |

### 8 capabilities nobody claims

Nothing in the Bank's own product and enabler catalogue claims these. **This is a finding about the institution, not a gap in the map.** The question for the room is whether the line is wrong or the ownership is missing.

| ID | Capability | Domain | Proposed owner |
|---|---|---|---|
| `1.5` | AI Ecosystem & Alliance Management | AI Strategy & Value Management | Chief AI Officer |
| `2.3` | AI Product Management | AI Demand & Solution Shaping | AI Product Owner |
| `4.6` | AI Evaluation & Testing | AI Solution Engineering | Quality Engineering Owner |
| `6.3` | Continuous Evaluation, Drift & Quality Management | AI Operations & Reliability | AI Product Operations Owner |
| `7.2` | Responsible & Trustworthy AI Practice | AI Governance, Risk, Security & Assurance | Responsible AI Owner |
| `7.5` | Privacy & Data Protection for AI | AI Governance, Risk, Security & Assurance | Privacy Officer |
| `7.6` | Legal, Regulatory & Contractual Compliance for AI | AI Governance, Risk, Security & Assurance | General Counsel |
| `7.9` | AI Impact Assessment & Risk Classification | AI Governance, Risk, Security & Assurance | AI Risk & Governance Owner |

---

## Who owns the map

Mapped against the Bank's own product and enabler catalogue. The point of this table is that **the model is not one function's instrument**: the unit that answers for a capability is usually not Architecture.

| Unit | Capabilities | Which |
|---|:-:|---|
| Artificial Intelligence | 14 | `1.1` `2.1` `3.6` `3.7` `4.2` `4.3` `4.4` `5.1` `5.2` `5.5` `6.1` `7.1` `7.7` `8.4` |
| **(nobody)** | 8 | `1.5` `2.3` `4.6` `6.3` `7.2` `7.5` `7.6` `7.9` |
| Cloud and Infrastructure | 4 | `5.3` `5.4` `6.2` `6.5` |
| Core Platforms | 4 | `3.5` `4.5` `4.7` `5.6` |
| Data Management | 4 | `3.1` `3.2` `3.3` `3.4` |
| Emerging Tech | 3 | `2.6` `8.3` `8.6` |
| Strategic Portfolio Management | 3 | `1.2` `1.3` `8.1` |
| Digital Transformation | 2 | `2.4` `8.5` |
| Enterprise Architecture | 2 | `2.2` `4.1` |
| Service Delivery | 2 | `6.4` `6.6` |
| Strategic Resource Management | 2 | `1.4` `8.2` |
| Cybersecurity | 1 | `7.4` |
| IT Risk (Compliance) | 1 | `7.8` |
| People Experience - IBT | 1 | `2.5` |
| Risk, Audit & Compliance | 1 | `7.3` |

---

## What is new because of agents

7 of 52 capabilities and 30 of 258 criteria are marked as arising from agentic AI rather than from analytics or from generative AI used as a tool. They are flagged because they are the newest part of the map and therefore the least settled.

| ID | Capability | Domain |
|---|---|---|
| `2.5` | **Human-AI Interaction & Oversight Design** | AI Demand & Solution Shaping |
| `4.4` | **Agent & Workflow Orchestration Design** | AI Solution Engineering |
| `4.5` | **Integration & Tool Enablement** | AI Solution Engineering |
| `5.5` | **Tool & Connector Catalog Management** | AI Platform & Infrastructure |
| `7.4` | **AI Security & Resilience** | AI Governance, Risk, Security & Assurance |
| `7.7` | **AI System & Agent Inventory Management** | AI Governance, Risk, Security & Assurance |
| `7.9` | **AI Impact Assessment & Risk Classification** | AI Governance, Risk, Security & Assurance |

<details><summary>30 agentic criteria</summary>

| L3 | Criterion | Under |
|---|---|---|
| `2.5.1` | Autonomy & Interaction Pattern Determination | `2.5` Human-AI Interaction & Oversight Design |
| `2.5.2` | Human Oversight & Intervention Design | `2.5` Human-AI Interaction & Oversight Design |
| `2.5.4` | Escalation & Handover Design | `2.5` Human-AI Interaction & Oversight Design |
| `2.5.5` | Oversight Competence & Workload Design | `2.5` Human-AI Interaction & Oversight Design |
| `4.3.5` | Prompt & Context Boundary Design | `4.3` Prompt & Context Engineering |
| `4.4.1` | Agent Specification & Goal Definition | `4.4` Agent & Workflow Orchestration Design |
| `4.4.2` | Task Decomposition & Planning Design | `4.4` Agent & Workflow Orchestration Design |
| `4.4.3` | Multi-Agent Coordination Design | `4.4` Agent & Workflow Orchestration Design |
| `4.4.4` | Agent Memory & State Design | `4.4` Agent & Workflow Orchestration Design |
| `4.4.5` | Guardrail & Constraint Design | `4.4` Agent & Workflow Orchestration Design |
| `4.4.6` | Termination & Loop Control Design | `4.4` Agent & Workflow Orchestration Design |
| `4.5.2` | Tool & Function Definition | `4.5` Integration & Tool Enablement |
| `4.5.3` | Capability Exposure to AI Clients | `4.5` Integration & Tool Enablement |
| `4.5.4` | Identity Propagation & Delegated Access | `4.5` Integration & Tool Enablement |
| `5.5.1` | Tool & Connector Catalog Management | `5.5` Tool & Connector Catalog Management |
| `5.5.2` | Tool Source Registration & Approval | `5.5` Tool & Connector Catalog Management |
| `5.5.3` | Tool Permission & Scope Governance | `5.5` Tool & Connector Catalog Management |
| `5.5.4` | Third-Party Tool Vetting | `5.5` Tool & Connector Catalog Management |
| `5.5.5` | Tool Version & Deprecation Control | `5.5` Tool & Connector Catalog Management |
| `6.1.1` | Model & Agent Deployment | `6.1` AI Deployment & Serving Operations |
| `6.2.2` | Trace & Interaction Logging | `6.2` AI Monitoring & Observability |
| `6.2.3` | Agent Action & Tool-Call Observability | `6.2` AI Monitoring & Observability |
| `6.4.2` | Containment & Kill-Switch Execution | `6.4` AI Incident & Problem Management |
| `7.2.3` | Human Agency & Oversight Enforcement | `7.2` Responsible & Trustworthy AI Practice |
| `7.4.3` | Injection & Jailbreak Detection and Response | `7.4` AI Security & Resilience |
| `7.4.4` | Agent Identity & Credential Lifecycle | `7.4` AI Security & Resilience |
| `7.4.5` | Runtime Authorization & Action Control | `7.4` AI Security & Resilience |
| `7.7.1` | AI System Registration | `7.7` AI System & Agent Inventory Management |
| `7.7.2` | Agent Registration & Attribute Recording | `7.7` AI System & Agent Inventory Management |
| `7.9.5` | Independent Challenge of First-Line Classification | `7.9` AI Impact Assessment & Risk Classification |

</details>

---

## Where this map came from

Each capability cites the published frameworks its line was drawn from. Those citations are graded by whether a reviewer can open them, and the grading — with the capabilities that rest on a source a reviewer cannot open — is in [`provenance.md`](provenance.md). The map is **not** an adoption of any one framework: no published model has this shape, and the lines that are ours say so.


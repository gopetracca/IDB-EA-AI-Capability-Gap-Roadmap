# Capability assessment — Executive readiness

**Inter-American Development Bank** · generated 2026-09-10 · scale `exec` · **a lens, not the assessment**

> **The question this scale asks:** How much of what we said we would do actually exists?
>
> Our own coarse roll-up for executive reporting. Reads the same observations as the default scale. Not adopted from any published model.
>
> A LENS for executive reporting, not the assessment. It averages, which the default scale deliberately does not: a capability can look adequate here while the default scale holds it at Level 1 because nothing is performed. Where they disagree, the default scale is the finding.

The taxonomy has three levels: **8 domains (L1)**, a reporting cluster that is never scored; **56 capabilities (L2)** — the unit that carries a level and an accountable owner; and **283 criteria (L3)** — the specific practices that can actually be witnessed. *Practised* is observed once per criterion and the capability value is **derived** from those observations, never typed: it reads `yes` only when every criterion was examined and every one passed (ADR-0014). Criteria carry no level of their own. They are listed per capability in section *By domain* below, and each has a row on sheet 2 of the workbook.

| | |
|---|---|
| Domains (L1) | 8 |
| Capabilities (L2) | 56 |
| Criteria (L3) | 283 |
| Rated | 15 |
| Not rated | 41 |
| Offerings | 7 |
| Assets | 20 |

---

## The scale

| Level | Name | Meaning | Derivable today |
|---|---|---|:-:|
| **1** | Planning | Considered. Little or nothing exists yet. | yes |
| **2** | Experimenting | Something exists, in pieces, not joined up. | yes |
| **3** | Stabilizing | It exists and is used, with gaps. | yes |
| **4** | Scaling | It exists, is used, and is supported across the institution. | yes |
| **5** | Leading | Relied upon, measured and improved. | yes |

## The four observations

| Observation | The question | Asked at | Evidence expected |
|---|---|---|---|
| **Practised** | Is this specific practice done on real AI systems in production, repeatedly? | each L3 criterion | Named AI systems or agents where this criterion was done, and by whom |
| **Enabled** | Can a team get the tooling for this without building it themselves? | the capability | An offering in the offerings register, or the enterprise service that provides it |
| **Skilled** | Do the people who must do this know how? | the capability | Named practitioners, training records, or a competency statement |
| **Defined** | Is there an approved institutional standard, policy or method for this? Set by whoever owns the subject - the platform team, Cybersecurity, Data Management, Legal, HR or EA. | the capability | The document, its owner, its location and a date |

Values: `yes` · `partial` · `no` · `n/a` (with a reason) · `unknown` (nobody has looked — never a zero).

### Where each observation is recorded

This is the question most often got wrong. **Only two of the three taxonomy levels ever carry an observation**, and one value on this page is not recorded by anybody — it is computed.

| Taxonomy level | What is recorded against it | Rows |
|---|---|:-:|
| **L1 domain** (8) | *Nothing.* A domain is a reporting cluster and is never scored | — |
| **L2 capability** (56) | `enabled`, `skilled`, `defined` — one row each. Plus `practised`, **derived** from the criteria below it and never typed | 168 |
| **L3 criterion** (283) | `practised` — one row per criterion | 283 |

So a reviewer answers **451 rows**, not 56: `enabled`, `skilled`, `defined` once per capability, and `practised` once per criterion. The capability's `practised` value shown in the tables below was computed by the roll-up (ADR-0014); **there is nowhere to type it, and typing one is the one edit `check` rejects outright.**

---

## How this scale places a level

Nothing below is typed. It is derived by running this scale over all **625 combinations** of the five values across the four observations, so it cannot disagree with the rule it describes.

| To reach | **Practised** | **Enabled** | **Skilled** | **Defined** | Reaches |
|---|---|---|---|---|:-:|
| **1 Planning** ⚠ | *any* | *any* | *any* | *any* | 513 of 625 |
| **2 Experimenting** ⚠ | *any* | *any* | *any* | *any* | 480 of 625 |
| **3 Stabilizing** ⚠ | *any* | *any* | *any* | *any* | 330 of 625 |
| **4 Scaling** ⚠ | *any* | *any* | *any* | *any* | 119 of 625 |
| **5 Leading** ⚠ | `yes` or `n/a` or `unknown` | `yes` or `n/a` or `unknown` | `yes` or `n/a` or `unknown` | `yes` or `n/a` or `unknown` | 33 of 625 |

*Read each row as **to reach at least this level**.* `n/a` counts as satisfied: a capability that legitimately needs no tooling is not held down for having none.

Rows marked ⚠ are true of every capability at that level but do **not** by themselves determine it: this scale does something no per-observation condition can express. Read the worked examples below instead.

### When it returns *not rated*

No single observation forces it: this scale declines to place a level when too few dimensions have been observed to judge. That is **112 of 625 combinations**.

Not rated is a result, not a zero: the evidence needed to place the capability has never been gathered.

This scale **does not gate** on performance: it will place a level from the enablers alone, which is why it is a lens and not the assessment.

### Worked: what a set of answers produces

Ten situations a reviewer will actually record, run through this scale. Every level and every reason below is computed, not written.

| If the four answers are | Practised | Enabled | Skilled | Defined | Then | Because |
|---|---|---|---|---|---|---|
| Nobody has looked yet | `unknown` | `unknown` | `unknown` | `unknown` | *not rated* | Not rated: nothing has been observed |
| The enablers exist, but nobody has asked whether the work is done | `unknown` | `yes` | `yes` | `yes` | **5 Leading** | 3 of 3 observed dimensions achieved; practised not observed |
| Someone looked: it is not done, though the enablers exist | `no` | `yes` | `yes` | `yes` | **4 Scaling** | 3 of 4 observed dimensions achieved |
| Done on some systems, nothing else observed | `partial` | `unknown` | `unknown` | `unknown` | *not rated* | Not rated: only 1 of 4 dimensions observed (practised) - too few to average without one cell carrying the whole claim |
| Done everywhere, but no tooling is provided | `yes` | `no` | `yes` | `yes` | **4 Scaling** | 3 of 4 observed dimensions achieved |
| Done everywhere, tooled, but competence not evidenced | `yes` | `yes` | `unknown` | `yes` | **5 Leading** | 3 of 3 observed dimensions achieved; skilled not observed |
| Done everywhere, tooled and staffed, no standard recorded | `yes` | `yes` | `yes` | `unknown` | **5 Leading** | 3 of 3 observed dimensions achieved; defined not observed |
| Done everywhere, tooled and staffed, standard pre-release | `yes` | `yes` | `yes` | `partial` | **4 Scaling** | 4 of 4 observed dimensions achieved |
| Done everywhere, tooled and staffed, approved standard | `yes` | `yes` | `yes` | `yes` | **5 Leading** | 4 of 4 observed dimensions achieved |
| Done everywhere and staffed; no tooling is needed here | `yes` | `n/a` | `yes` | `yes` | **5 Leading** | 3 of 3 observed dimensions achieved; enabled not applicable |

---

## By domain

### D1 · AI Strategy & Value Management

*Able to set direction for AI and convert it into measurable institutional value.*

| ID | Capability | Owner | Pra | Ena | Ski | Def | Level | Why |
|---|---|---|:-:|:-:|:-:|:-:|:-:|---|
| `1.1` | AI Vision & Strategy Definition | Artificial Intelligence | ? | n-a | ? | ? | *not rated* | Not rated: nothing has been observed |
| `1.2` | AI Portfolio & Investment Management | Strategic Portfolio Management | ? | n-a | ? | ? | *not rated* | Not rated: nothing has been observed |
| `1.3` | Value Realization & Performance Reporting | Strategic Portfolio Management | ? | n-a | ? | ? | *not rated* | Not rated: nothing has been observed |
| `1.4` | AI Sourcing & Partner Strategy | Strategic Resource Management | ? | n-a | ? | ? | *not rated* | Not rated: nothing has been observed |
| `1.5` | AI Ecosystem & Alliance Management | **none** | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |

<details><summary><code>1.1</code> AI Vision & Strategy Definition — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `1.1.1` | **AI Ambition & Positioning** | Define what role AI plays in the institutional mandate and how far the organization intends to go. | ? |  |
| `1.1.2` | **AI Strategy Formulation & Refresh** | Produce and periodically revise an endorsed AI strategy with explicit scope and stated exclusions. | ? |  |
| `1.1.3` | **Strategic Alignment to Institutional Priorities** | Trace every AI objective to a corporate goal, sector strategy or country program. | ? |  |
| `1.1.4` | **AI Principles & Ethical Positioning** | Set the non-negotiable commitments that constrain all downstream AI decisions. | ? |  |
| `1.1.5` | **Horizon Scanning & Technology Foresight** | Track emerging AI capability and judge what it changes for the institution. | ? |  |

</details>

<details><summary><code>1.2</code> AI Portfolio & Investment Management — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `1.2.1` | **AI Investment Case Development** | Build comparable business cases stating cost, benefit and risk on a common basis. | ? |  |
| `1.2.2` | **Portfolio Prioritization & Sequencing** | Rank and stage the AI portfolio against delivery capacity, risk appetite and dependency. | ? |  |
| `1.2.3` | **Funding & Budget Allocation** | Route funds to AI work through a mechanism that survives audit and annual planning. | ? |  |
| `1.2.4` | **Portfolio Balance & Exposure Management** | Keep the mix of experimental, scaling and production AI within stated tolerance. | ? |  |
| `1.2.5` | **Stage-Gate & Investment Review** | Decide continuation, pivot or termination at defined decision points on recorded criteria. | ? |  |

</details>

<details><summary><code>1.3</code> Value Realization & Performance Reporting — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `1.3.1` | **Benefit Definition & Baselining** | State expected benefit in measurable terms before build, with a recorded pre-intervention baseline. | ? |  |
| `1.3.2` | **Value Tracking & Attribution** | Measure realized benefit and attribute it defensibly to the AI intervention rather than to trend. | ? |  |
| `1.3.3` | **AI Performance Metrics & KPI Management** | Maintain the indicator set that describes AI performance institution-wide. | ? |  |
| `1.3.4` | **Executive & Board Reporting** | Report AI status, risk and value to governing bodies at their cadence and in their language. | ? |  |
| `1.3.5` | **Post-Implementation Review** | Assess delivered outcomes against the approved case and feed findings back into prioritization. | ? |  |

</details>

<details><summary><code>1.4</code> AI Sourcing & Partner Strategy — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `1.4.1` | **Build / Buy / Partner Decisioning** | Choose the sourcing route per capability with recorded rationale and revisit triggers. | ? |  |
| `1.4.2` | **AI Vendor & Model Provider Evaluation** | Assess providers on capability, trustworthiness, transparency and cost of exit. | ? |  |
| `1.4.3` | **Contractual Safeguards & AI Clauses** | Secure rights covering data use, IP, indemnity, audit access and notification of model change. | ? |  |
| `1.4.4` | **Concentration & Exit Risk Management** | Limit dependence on any single provider and keep a tested, costed exit path. | ? |  |
| `1.4.5` | **Supplier Performance & Assurance Monitoring** | Monitor contracted providers against their obligations and assurance commitments for the life of the relationship. | ? |  |

</details>

<details><summary><code>1.5</code> AI Ecosystem & Alliance Management — 6 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `1.5.1` | **Partnership Portfolio Definition** | Decide which external relationships the institution needs in order to hold AI capability it will not build itself. | ? |  |
| `1.5.2` | **Research & Academic Collaboration** | Operate collaborations whose output is knowledge, method or evidence rather than a delivered system. | ? |  |
| `1.5.3` | **Peer & Multilateral Cooperation** | Exchange AI practice, assets and evidence with counterpart institutions under agreed terms. | ? |  |
| `1.5.4` | **Insourcing / Outsourcing Posture Management** | Set and periodically revisit which AI work is held internally and which is placed outside. | ? |  |
| `1.5.5` | **Ecosystem Dependency & Continuity Management** | Track aggregate dependency across the external AI ecosystem and stay able to operate when a member changes, merges or exits. | ? |  |
| `1.5.6` | **Partnership Value & Obligation Tracking** | Monitor what each relationship returns against what it obliges the institution to do. | ? |  |

</details>

### D2 · AI Demand & Solution Shaping

*Able to find, qualify and shape AI opportunities into deliverable, adoptable solutions.*

| ID | Capability | Owner | Pra | Ena | Ski | Def | Level | Why |
|---|---|---|:-:|:-:|:-:|:-:|:-:|---|
| `2.1` | Use Case Discovery & Intake | Artificial Intelligence | ? | n-a | ? | ? | *not rated* | Not rated: nothing has been observed |
| `2.2` | AI Use-Case Feasibility & Qualification | Enterprise Architecture | ? | yes | ? | yes | **5** Leading | 2 of 2 observed dimensions achieved; practised, skilled not observed |
| `2.3` | AI Product Management | **none** | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |
| `2.4` | Business Process & Service Redesign | Digital Transformation | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |
| `2.5` | Human-AI Interaction & Oversight Design | People Experience - IBT | ? | yes | ? | yes | **5** Leading | 2 of 2 observed dimensions achieved; practised, skilled not observed |
| `2.6` | AI Innovation & Incubation | Emerging Tech | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |

<details><summary><code>2.1</code> Use Case Discovery & Intake — 4 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `2.1.1` | **Opportunity Identification & Ideation** | Actively generate candidate use cases from business need rather than waiting for requests. | ? |  |
| `2.1.2` | **Demand Intake & Triage** | Operate a single intake route that classifies and routes every AI request. | ? |  |
| `2.1.3` | **Use Case Registration & Classification** | Record each candidate against a common taxonomy before any build effort begins. | ? |  |
| `2.1.4` | **Duplicate & Reuse Screening** | Detect that a request is already solved, in flight, or satisfiable by an existing asset. | ? |  |

</details>

<details><summary><code>2.2</code> AI Use-Case Feasibility & Qualification — 4 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `2.2.1` | **Technical & Data Feasibility Assessment** | Judge whether the data, models and integration required actually exist and are obtainable. | ? |  |
| `2.2.2` | **Cost, Effort & Capacity Feasibility** | Estimate build and run cost, effort and the specialist capacity a use case would consume. | ? |  |
| `2.2.3` | **Operational & Adoption Feasibility** | Judge whether the receiving business area can absorb, operate and sustain the change. | ? |  |
| `2.2.4` | **Go / No-Go Determination** | Make and record a proceed decision with named accountability and stated conditions. | ? |  |

</details>

<details><summary><code>2.3</code> AI Product Management — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `2.3.1` | **AI Product Definition & Roadmapping** | Define the product, its users, its boundary and its forward path. | ? |  |
| `2.3.2` | **Requirements & Acceptance Criteria Management** | Express what good looks like precisely enough to be tested against. | ? |  |
| `2.3.3` | **User Research & Feedback Integration** | Learn from actual use and feed it back into the product. | ? |  |
| `2.3.4` | **Backlog & Release Planning** | Sequence work and commit to releases against capacity. | ? |  |
| `2.3.5` | **Product Performance Ownership** | Hold a named owner accountable for the product's outcomes in production. | ? |  |

</details>

<details><summary><code>2.4</code> Business Process & Service Redesign — 6 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `2.4.1` | **Process Analysis & AI Fit Assessment** | Understand the current process well enough to know where AI changes it. | ? |  |
| `2.4.2` | **Target Process & Task Redesign** | Design the intended process, including what stops being done. | ? |  |
| `2.4.3` | **Human / Machine Task Allocation** | Decide explicitly which tasks move, which stay, and which become supervisory. | ? |  |
| `2.4.4` | **Control Point Redesign** | Relocate or rebuild the controls that the old process embedded in human steps. | ? |  |
| `2.4.5` | **Service Model & Service Level Redefinition** | Restate the service promise once AI changes what is deliverable. | ? |  |
| `2.4.6` | **Language Coverage & Service Equity** | Determine which languages an AI-delivered service must support, and at what measured quality, across the institution's countries. | ? |  |

</details>

<details><summary><code>2.5</code> Human-AI Interaction & Oversight Design — 6 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `2.5.1` | **Autonomy & Interaction Pattern Determination** | Set and record, per system, the interaction pattern and how much an AI system or agent may do without human confirmation. | ? |  |
| `2.5.2` | **Human Oversight & Intervention Design** | Design the specific point, information and control through which a human can intervene. | ? |  |
| `2.5.3` | **Explanation & Disclosure Design** | Design what the system tells its user about what it is and how it reached an output. | ? |  |
| `2.5.4` | **Escalation & Handover Design** | Design the path by which work returns to a human, with sufficient context to act. | ? |  |
| `2.5.5` | **Oversight Competence & Workload Design** | Ensure the person assigned oversight has the time, information, training and authority to actually exercise it. | ? |  |
| `2.5.6` | **Accessible & Inclusive Interaction Design** | Design AI-delivered interaction to be usable with assistive technology and across literacy and channel constraints. | ? |  |

</details>

<details><summary><code>2.6</code> AI Innovation & Incubation — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `2.6.1` | **Idea Capture & Innovation Sourcing** | Collect candidate AI ideas from staff, partners and technology watch outside the formal demand route. | ? |  |
| `2.6.2` | **Sandboxed Experimentation** | Run time-boxed experiments in an environment where failure is contained and permitted. | ? |  |
| `2.6.3` | **Innovation Portfolio & Scaling Decisions** | Hold the set of live experiments within capacity and decide which of them scale. | ? |  |
| `2.6.4` | **Experiment-to-Product Transition** | Move a proven experiment onto the funded delivery route, or record why it stops. | ? |  |
| `2.6.5` | **Controlled Failure & Learning Capture** | Permit experiments to fail and extract reusable learning from the failure. | ? |  |

</details>

### D3 · Data & Knowledge Management

*Able to supply trusted, governed data and knowledge to AI systems.*

| ID | Capability | Owner | Pra | Ena | Ski | Def | Level | Why |
|---|---|---|:-:|:-:|:-:|:-:|:-:|---|
| `3.1` | Data Governance & Stewardship for AI | Data Management | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |
| `3.2` | Data Sourcing, Licensing & Provenance | Data Management | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |
| `3.3` | Data Quality & Preparation for AI | Data Management | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |
| `3.4` | Metadata, Lineage & Cataloging for AI | Data Management | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |
| `3.5` | Knowledge Corpus & Content Management | Core Platforms | ? | yes | ? | yes | **5** Leading | 2 of 2 observed dimensions achieved; practised, skilled not observed |
| `3.6` | Knowledge Access & Retrieval | Artificial Intelligence | ? | yes | ? | yes | **5** Leading | 2 of 2 observed dimensions achieved; practised, skilled not observed |
| `3.7` | Derived Representation Management | Artificial Intelligence | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |

<details><summary><code>3.1</code> Data Governance & Stewardship for AI — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `3.1.1` | **Data Ownership & Stewardship Assignment** | Name an accountable owner and an operating steward for each data asset used by AI. | ? |  |
| `3.1.2` | **Data Classification & Sensitivity Labeling** | Apply a consistent sensitivity classification that downstream controls can act on. | ? |  |
| `3.1.3` | **Data Access Policy & Entitlement Management** | Define and enforce who may access which data, for which purpose. | ? |  |
| `3.1.4` | **Data Retention & Records Management** | Apply retention and disposal rules to AI inputs, outputs and interaction records. | ? |  |
| `3.1.5` | **Cross-Border Data Transfer Control** | Determine and enforce which jurisdictions the institution's data may be transferred to and processed in. | ? |  |

</details>

<details><summary><code>3.2</code> Data Sourcing, Licensing & Provenance — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `3.2.1` | **Data Acquisition & Onboarding** | Bring external and internal data into the estate through a controlled route. | ? |  |
| `3.2.2` | **Licensing & Permitted-Use Verification** | Confirm and record that intended AI use is permitted by the source's terms. | ? |  |
| `3.2.3` | **Provenance & Chain-of-Custody Recording** | Record where data came from and every transformation applied to it. | ? |  |
| `3.2.4` | **Consent & Purpose Limitation Management** | Track the basis on which data was collected and confine use to it. | ? |  |
| `3.2.5` | **Synthetic Data Generation & Control** | Produce and govern synthetic data, including disclosure of its synthetic nature. | ? |  |

</details>

<details><summary><code>3.3</code> Data Quality & Preparation for AI — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `3.3.1` | **Data Profiling & Quality Assessment** | Measure completeness, accuracy, timeliness and consistency against stated thresholds. | ? |  |
| `3.3.2` | **Data Cleansing & Remediation** | Correct defects at source where possible, and record what was corrected downstream. | ? |  |
| `3.3.3` | **Representativeness & Bias Screening** | Test datasets for gaps and skews relative to the affected population. | ? |  |
| `3.3.4` | **Labeling & Annotation Management** | Produce, quality-check and version human and machine labels. | ? |  |
| `3.3.5` | **Dataset Versioning & Snapshotting** | Freeze and identify the exact dataset a model or evaluation used. | ? |  |

</details>

<details><summary><code>3.4</code> Metadata, Lineage & Cataloging for AI — 4 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `3.4.1` | **Data Catalog Management** | Maintain a searchable inventory of data assets with their attributes. | ? |  |
| `3.4.2` | **Business Glossary & Semantic Definition** | Hold one agreed definition per business term that data assets bind to. | ? |  |
| `3.4.3` | **Lineage Capture & Traceability** | Trace a model output back through transformations to source records. | ? |  |
| `3.4.4` | **Data Product Publication** | Publish curated, contracted datasets that consumers can depend on. | ? |  |

</details>

<details><summary><code>3.5</code> Knowledge Corpus & Content Management — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `3.5.1` | **Corpus Definition & Curation** | Decide what belongs in a knowledge corpus and what is deliberately excluded. | ? |  |
| `3.5.2` | **Content Ingestion & Normalization** | Bring heterogeneous content into a consistent, machine-usable form. | ? |  |
| `3.5.3` | **Content Segmentation Design** | Choose and apply segmentation that preserves meaning and citability. | ? |  |
| `3.5.4` | **Corpus Freshness & Refresh Management** | Keep the corpus current and know how stale any part of it is. | ? |  |
| `3.5.5` | **Authoritative Source Designation** | Declare which source wins when two documents disagree. | ? |  |

</details>

<details><summary><code>3.6</code> Knowledge Access & Retrieval — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `3.6.1` | **Retrieval Service Provision** | Provide governed retrieval over institutional content — by meaning, by term, or both — as a reusable service. | ? |  |
| `3.6.2` | **Access-Trimmed Retrieval Enforcement** | Enforce, at retrieval time, the entitlements determined in 3.1.3, so a requester sees only what they may see. | ? |  |
| `3.6.3` | **Retrieval Quality Evaluation & Tuning** | Measure and improve retrieval precision and recall against a known set. | ? |  |
| `3.6.4` | **Multi-Source Federation & Ranking** | Retrieve across several repositories and rank the combined result coherently. | ? |  |
| `3.6.5` | **Citation, Grounding & Traceability** | Return every answer with the source it rests on, resolvable by the reader. | ? |  |

</details>

<details><summary><code>3.7</code> Derived Representation Management — 4 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `3.7.1` | **Feature Engineering & Store Management** | Produce, share and reuse engineered features under version control. | ? |  |
| `3.7.2` | **Embedding Model Selection & Versioning** | Choose embedding models deliberately and record which version produced which index. | ? |  |
| `3.7.3` | **Index Lifecycle & Re-embedding** | Rebuild and migrate indexes when content or embedding models change. | ? |  |
| `3.7.4` | **Derived Representation Governance** | Apply access, retention and residency controls to vector representations. | ? |  |

</details>

### D4 · AI Solution Engineering

*Able to design, build, customize and validate AI solutions to a defined standard.*

| ID | Capability | Owner | Pra | Ena | Ski | Def | Level | Why |
|---|---|---|:-:|:-:|:-:|:-:|:-:|---|
| `4.1` | AI Architecture Management & Solution Governance | Enterprise Architecture | part | yes | ? | yes | **4** Scaling | 2 of 3 observed dimensions achieved; skilled not observed |
| `4.2` | Model Selection, Customization & Tuning | Artificial Intelligence | part | part | ? | no | **2** Experimenting | 1 of 3 observed dimensions achieved; skilled not observed |
| `4.3` | Prompt & Context Engineering | Artificial Intelligence | n-a | n-a | ? | n-a | *not rated* | Not rated: nothing has been observed |
| `4.4` | Agent & Workflow Orchestration Design | Enterprise Architecture | part | n-a | ? | part | **3** Stabilizing | 1 of 2 observed dimensions achieved; skilled not observed; enabled not applicable |
| `4.5` | Integration & Tool Enablement | Core Platforms | part | part | ? | yes | **3** Stabilizing | 2 of 3 observed dimensions achieved; skilled not observed |
| `4.6` | AI Evaluation & Testing | Artificial Intelligence | part | no | ? | no | **2** Experimenting | 0 of 3 observed dimensions achieved; skilled not observed |
| `4.7` | AI Release & Change Management | Core Platforms | part | part | ? | yes | **3** Stabilizing | 2 of 3 observed dimensions achieved; skilled not observed |

<details><summary><code>4.1</code> AI Architecture Management & Solution Governance — 7 L3 criteria, 7 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `4.1.1` | **Solution Pattern Selection** | Choose the architecture building block that realizes the required capability. | yes | EA codesigns enterprise solutions with product teams, also defines reference architectures/ decission trees, , etc. |
| `4.1.2` | **Reference Architecture Compliance** | Build to published reference architectures and detect deviation. | part | practiced es partial porque no hay casos de uso en produccion. El primer agente enterprise va a ser el de KNP |
| `4.1.3` | **Architecture Decision Recording** | Record significant decisions with alternatives and consequences. | yes | ADR. Los poroductos ya trabajan con ADR, cada uno documenta en diferentes lugares. EA, también tiene ADRs y se documentan en sharepoint. |
| `4.1.4` | **Non-Functional Requirement Design** | Design explicitly for latency, cost, availability, degradation behavior and any other non-functional requirement the solution carries. | yes | EA co-design enterprise solutions with product teams and non-functional requirements is lwasy taken into account. |
| `4.1.5` | **Architecture Review & Dispensation** | Review designs and grant time-boxed exceptions with recorded conditions. | yes | Architecture reviews from EA, part of the PRAC process. |
| `4.1.6` | **ABB & Pattern Stewardship** | Define, version and retire the institution's logical building blocks and the patterns that compose them. | yes | EA works on standards/reference architectures/reusable patterns, etc. |
| `4.1.7` | **Solution Conformance Certification** | Certify that a concrete solution conforms to the building blocks and controls it claims, and record the deviations. | yes | El PRAC. |

</details>

<details><summary><code>4.2</code> Model Selection, Customization & Tuning — 5 L3 criteria, 5 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `4.2.1` | **Model Selection for Use Case** | Select a model from within the cleared set against task-specific criteria and evidence. | yes | only azure openai allowed for now. There is not formal EA or AI Enabler standard. TODO: who should write this down? |
| `4.2.2` | **Fine-Tuning & Adaptation** | Adapt models to institutional context under controlled, repeatable procedure. | no |  |
| `4.2.3` | **Model Training & Experimentation** | Run and track experiments so results are reproducible. | no |  |
| `4.2.4` | **Model Documentation & Disclosure Production** | Produce model cards covering intended use, limits, data and evaluation results. | n-a |  |
| `4.2.5` | **Model Versioning & Registration** | Register every model version as an identifiable, ownable asset. | yes | Teams can deploy their own models in their own Foundry, OR, they can consume the models via the AI Gateway provided by AI Enabler. |

</details>

<details><summary><code>4.3</code> Prompt & Context Engineering — 5 L3 criteria, 5 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `4.3.1` | **Prompt Design & Templating** | Design prompts as reusable, parameterized templates rather than embedded strings. | n-a |  |
| `4.3.2` | **Prompt Versioning & Registry** | Version, review and register prompts as controlled artifacts. | n-a |  |
| `4.3.3` | **Context Assembly & Window Management** | Assemble context deliberately and manage what is included, ordered and dropped. | n-a |  |
| `4.3.4` | **Grounding Strategy Design** | Decide what the model is permitted to answer from, and enforce it. | n-a |  |
| `4.3.5` | **Prompt & Context Boundary Design** | Construct prompt and context boundaries that constrain what untrusted content can instruct. | n-a |  |

</details>

<details><summary><code>4.4</code> Agent & Workflow Orchestration Design — 6 L3 criteria, 2 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `4.4.1` | **Agent Specification & Goal Definition** | State an agent's objective, scope and prohibited actions before it is built. | part | Example: Katia's project preparation project. Defined. We might use that example to replicate what it's done for others. |
| `4.4.2` | **Task Decomposition & Planning Design** | Design how an agent breaks work down and selects its next step. | n-a |  |
| `4.4.3` | **Multi-Agent Coordination Design** | Design how agents delegate, communicate and resolve conflict. | ? |  |
| `4.4.4` | **Agent Memory & State Design** | Design what an agent retains, for how long, and who else can see it. | ? |  |
| `4.4.5` | **Guardrail & Constraint Design** | Encode hard limits an agent cannot argue its way past. | ? |  |
| `4.4.6` | **Termination & Loop Control Design** | Design stopping conditions, budgets and loop detection. | ? |  |

</details>

<details><summary><code>4.5</code> Integration & Tool Enablement — 6 L3 criteria, 5 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `4.5.1` | **MCP & System Integration Design** | Design integration to institutional systems with contracts and error semantics. | part | MCP servers on their way to production. And, agent-mcp integration defined. |
| `4.5.2` | **MCP Tool & Function Definition** | Define the callable actions exposed to a model, with typed inputs and stated effects. | part | We are not in prod yet, (ops mcp servers), we have the standards for MCP and agent. |
| `4.5.3` | **Capability Exposure to AI Clients** | Expose institutional capability to AI clients through the prevailing open tool-interface standard. | part | We use APIM as mcp gateway for now. All partial because systems not yet in prod. No responsible for APIM mcp configurations today. |
| `4.5.4` | **Identity Propagation & Delegated Access** | Carry the acting user's identity through to the system of record. | part | Depends on the system supporting delegated access. |
| `4.5.5` | **Legacy & Core System Adaptation** | Reach systems that were never designed to be called by an AI client. | part | Example: convergence was not built for AI clients, but with a custom enterprise mcp server, we can consume its data. |
| `4.5.6` | **Agent-to-Agent Interoperability** | Publish and consume agent descriptions, negotiate a task through a defined lifecycle, and carry identity and authorization across an agent boundary. | ? |  |

</details>

<details><summary><code>4.6</code> AI Evaluation & Testing — 8 L3 criteria, 3 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `4.6.1` | **Evaluation Criteria & Metric Definition** | Define the metrics that constitute acceptable performance for this use case. | part | KNP agent and MVP tested foundry evaluation framework. We also have the eval framework from ai product, unknown status |
| `4.6.2` | **Golden Dataset & Test Set Management** | Build and maintain representative evaluation sets with known-correct answers. | n-a |  |
| `4.6.3` | **Automated Evaluation Harness Operation** | Run evaluations repeatably as part of the delivery pipeline. | ? |  |
| `4.6.4` | **Human Review & Expert Evaluation** | Obtain qualified human judgement where automated metrics are insufficient. | n-a |  |
| `4.6.5` | **Pre-Deployment Acceptance Testing** | Test against acceptance criteria and record the result as release evidence. | ? |  |
| `4.6.6` | **Agent Trajectory & Tool-Use Evaluation** | Evaluate the path taken, not only the answer returned: tool selection, argument correctness, recovery from a failed call, termination and task completion. | ? |  |
| `4.6.7` | **Simulation & Scenario-Based Testing** | Exercise the system against simulated users, environments and adversarial inputs before it can reach a system of record. | ? |  |
| `4.6.8` | **Evaluator Validation & Judge Governance** | Where a model does the grading, validate the grader against human judgement and monitor the grader's own drift. | ? |  |

</details>

<details><summary><code>4.7</code> AI Release & Change Management — 6 L3 criteria, 5 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `4.7.1` | **Build & Continuous Integration** | Build AI artifacts through an automated, auditable pipeline. | part | MVP has a CICD for deploying agents in foundry. Missing definition on Container registry in case we use hosted agents |
| `4.7.2` | **Promotion & Environment Progression** | Move artifacts through environments under defined entry and exit criteria. | part | Not recorded on the sheet. Graded partial at the EA workshop, 9 September 2026 alongside 4.7.1, 4.7.3 and 4.7.4 as part of the Bank's standard SDLC; no system was named. EVIDENCE PENDING from the capability owner. |
| `4.7.3` | **Change Approval & Release Authorization** | Authorise AI change through a route proportionate to its risk tier. | part | Same SDLC. |
| `4.7.4` | **Rollback & Release Reversal** | Return a deployed AI system to a previously accepted release. | part | Can rollback to previous artifact  (container or jfrog artifact) |
| `4.7.5` | **Release Documentation** | Document at release what changed and what was deployed. | yes | Same SDLC. GitHub gives this out of the box when creating a release. |
| `4.7.6` | **Evidence Capture** | Capture at release the evidence that later assurance work will need. | ? |  |

</details>

### D5 · AI Platform & Infrastructure

*Able to provide and sustain the technical means to build and run AI.*

| ID | Capability | Owner | Pra | Ena | Ski | Def | Level | Why |
|---|---|---|:-:|:-:|:-:|:-:|:-:|---|
| `5.1` | AI Platform Service Provisioning | Artificial Intelligence | ? | part | ? | part | **3** Stabilizing | 1 of 2 observed dimensions achieved; practised, skilled not observed |
| `5.2` | Model Access & Traffic Management | Artificial Intelligence | part | yes | ? | yes | **4** Scaling | 2 of 3 observed dimensions achieved; skilled not observed |
| `5.3` | AI Environment & Workspace Management | Core Platforms | yes | yes | ? | yes | **5** Leading | 3 of 3 observed dimensions achieved; skilled not observed |
| `5.4` | AI Compute & Capacity Management | Cloud and Infrastructure | ? | yes | ? | n-a | *not rated* | Not rated: only 1 of 4 dimensions observed (enabled) - too few to average without one cell carrying the whole claim |
| `5.5` | Tool & Connector Catalog Management | **none** | ? | no | ? | ? | *not rated* | Not rated: only 1 of 4 dimensions observed (enabled) - too few to average without one cell carrying the whole claim |
| `5.6` | AI Developer Experience & Reuse Assets | Core Platforms | part | part | ? | ? | **3** Stabilizing | 1 of 2 observed dimensions achieved; defined, skilled not observed |
| `5.7` | AI Runtime Mediation & Egress Control | Artificial Intelligence | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |
| `5.8` | AI Agent Runtime & Execution Environment | Artificial Intelligence | part | yes | ? | part | **3** Stabilizing | 2 of 3 observed dimensions achieved; skilled not observed |
| `5.9` | AI Experimentation | Emerging Tech | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |

<details><summary><code>5.1</code> AI Platform Service Provisioning — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `5.1.1` | **Platform Service Catalog Management** | Publish what AI platform services exist, their terms and how to obtain them. | ? |  |
| `5.1.2` | **Landing Zone & Baseline Provisioning** | Provision AI environments from a compliant baseline rather than by hand. | ? |  |
| `5.1.3` | **Platform Configuration & Policy Enforcement** | Enforce configuration standards technically, not by instruction. | ? |  |
| `5.1.4` | **Platform Service Level Commitment** | Commit to and meet service levels for the shared AI platform services the institution offers. | ? |  |
| `5.1.5` | **Platform Upgrade & Deprecation Management** | Move consumers across platform versions without stranding them. | ? |  |

</details>

<details><summary><code>5.2</code> Model Access & Traffic Management — 5 L3 criteria, 4 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `5.2.1` | **Model Clearance & Approved Model List** | Assess candidate models against institutional criteria, record the clearance decision and its conditions, and maintain the approved list. | yes | Not recorded on the sheet. Graded yes at the EA meeting of 10 September 2026 with the rest of 5.2. EVIDENCE PENDING from the capability owner. |
| `5.2.2` | **Model Traffic Control & Routing** | Route all model traffic through a controlled point that can observe and enforce. | yes | Not all models will be exposed via an AI Gateway. Only the shared ones (shared capability). Individual teams can deploy their own models. |
| `5.2.3` | **Quota, Throttling & Rate Management** | Allocate and enforce consumption limits per consumer. | yes | Not recorded on the sheet. Graded yes at the EA meeting of 10 September 2026 with the rest of 5.2. EVIDENCE PENDING from the capability owner. |
| `5.2.4` | **Model Provider Credential Management** | Issue, rotate and revoke the credentials used to reach model providers and platform services. Agent identity is 7.4.4. | yes | Not recorded on the sheet. Graded yes at the EA meeting of 10 September 2026 with the rest of 5.2. EVIDENCE PENDING from the capability owner. |
| `5.2.5` | **Model Version Availability & Provider Change Control** | Control which model versions remain reachable and absorb provider-side version change without breaking consumers. | ? |  |

</details>

<details><summary><code>5.3</code> AI Environment & Workspace Management — 4 L3 criteria, 4 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `5.3.1` | **Environment Provision** | Provide the environments delivery teams build AI in - development, test and production - with clear data rules. | yes | Requires: subscription, RG, netowkring, subnets, connectivity, AI resources. The terraform modules to deploy foundry accounts and Foundry projects were built by EA. |
| `5.3.2` | **Workspace Tenancy & Isolation** | Define and enforce the tenancy and isolation topology between team workspaces. | yes | azure sub, rg, + foundry account with projects. Foundry account can be owned or shared, the logical isolation is with foundry projects. |
| `5.3.3` | **Network & Private Connectivity Control** | Control network reachability of AI services and keep traffic private where required. | yes | Foundry in private network mode, plus, traffic control at the subnet level possible. |
| `5.3.4` | **Environment Data Segregation** | Prevent production data from reaching environments not cleared for it. | yes | Applies the same type of controls that we currently have for applications? Roles, permissions, etc. |

</details>

<details><summary><code>5.4</code> AI Compute & Capacity Management — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `5.4.1` | **Compute Provisioning & Scheduling** | Make compute available to workloads on a predictable basis. | ? |  |
| `5.4.2` | **Capacity Planning & Forecasting** | Forecast demand far enough ahead to secure supply. | ? |  |
| `5.4.3` | **Accelerator & Quota Allocation** | Allocate scarce accelerator capacity against portfolio priority. | ? |  |
| `5.4.4` | **Workload Placement & Residency Enforcement** | Place workloads in locations that enforce the transfer and residency decisions taken in 3.1.5. | ? |  |
| `5.4.5` | **Edge & Disconnected Operation** | Run AI where connectivity, latency or residency prevents central serving, including fully offline. | ? |  |

</details>

<details><summary><code>5.5</code> Tool & Connector Catalog Management — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `5.5.1` | **Tool & Connector Catalog Management** | Maintain the inventory of actions and connectors available to AI systems. | ? |  |
| `5.5.2` | **Tool Source Registration & Approval** | Register and approve any source of callable tools before an AI client may reach it. | ? |  |
| `5.5.3` | **Tool Permission & Scope Governance** | Set and enforce the scope each tool grants, at least privilege. | ? |  |
| `5.5.4` | **Third-Party Tool Vetting** | Assess externally supplied tools and connectors before admission. | ? |  |
| `5.5.5` | **Tool Version & Deprecation Control** | Manage tool change so agent behavior does not silently shift. | ? |  |

</details>

<details><summary><code>5.6</code> AI Developer Experience & Reuse Assets — 5 L3 criteria, 4 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `5.6.1` | **Reference Implementation & Template Provision** | Publish working templates that already embed required controls. | part | Template available for MCP server. Template of hosted agent in progress. Missing CICD (GitHub actions) - Shared with DX platform team. |
| `5.6.2` | **SDK, Library & Component Curation** | Curate the approved libraries and shared components teams should build on. | n-a |  |
| `5.6.3` | **Self-Service Onboarding** | Let a team start correctly without a bespoke engagement. | no |  |
| `5.6.4` | **Shared Agent Skill & Extension Repository** | Maintain a curated, shared repository of the skills, hooks and rules that agents draw on, discoverable and reusable across the institution. | ? |  |
| `5.6.5` | **Developer Documentation & Support** | Document the platform to the standard its users actually need. | part | Doc per product line. Standards serve as the basis, then we need runbooks, product documentation, solution documentation, etc? |

</details>

<details><summary><code>5.7</code> AI Runtime Mediation & Egress Control — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `5.7.1` | **Tool Traffic Mediation** | Route every tool invocation through a controlled point that can observe, authorize and refuse. | ? |  |
| `5.7.2` | **Outbound Content & Data Egress Control** | Inspect what a tool returns before it enters context, and what a call carries out of the institution. | ? |  |
| `5.7.3` | **Runtime Policy Distribution & Enforcement** | Distribute policy from one control plane and enforce it at every data-plane instance. | ? |  |
| `5.7.4` | **Invocation Rate, Budget & Loop Enforcement** | Enforce per-agent call budgets and stop runaway invocation at the mediation point rather than in the agent's own code. | ? |  |
| `5.7.5` | **Mediation Telemetry Hand-off** | Emit from the mediation point the record that 6.2.3 and 7.8.2 depend on. | ? |  |

</details>

<details><summary><code>5.8</code> AI Agent Runtime & Execution Environment — 5 L3 criteria, 3 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `5.8.1` | **Agent Hosting & Execution Runtime** | Provide the managed substrate an agent executes in. | part | Foundry Agents, missing prod |
| `5.8.2` | **Code & Computer-Use Sandboxing** | Execute model-generated code and computer-use actions in an isolated, disposable environment. | no |  |
| `5.8.3` | **Agent Memory & State Infrastructure** | Provide the store that enforces what 4.4.4 designed: retention, isolation, and who else can read it. | part | It is there, missing prod. |
| `5.8.4` | **Long-Running Task & Scheduling Support** | Support work that outlives a request, including resumption and cancellation. | ? |  |
| `5.8.5` | **Runtime Resource & Blast-Radius Limits** | Bound what a single agent execution can consume and reach. | ? |  |

</details>

<details><summary><code>5.9</code> AI Experimentation — 1 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `5.9.1` | **Isolated Experimentation Environment Provision** | Provide an experimentation environment that is fully isolated from institutional systems and data. | ? |  |

</details>

### D6 · AI Operations & Reliability

*Able to run AI in production dependably, observably and affordably.*

| ID | Capability | Owner | Pra | Ena | Ski | Def | Level | Why |
|---|---|---|:-:|:-:|:-:|:-:|:-:|---|
| `6.1` | AI Deployment & Serving Operations | Artificial Intelligence | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |
| `6.2` | AI Monitoring & Observability | Cloud and Infrastructure | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |
| `6.3` | Continuous Evaluation, Drift & Quality Management | **none** | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |
| `6.4` | AI Incident & Problem Management | Service Delivery | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |
| `6.5` | AI Cost Management | Cloud and Infrastructure | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |
| `6.6` | AI Asset Retirement & Evidence Preservation | Service Delivery | ? | n-a | ? | ? | *not rated* | Not rated: nothing has been observed |
| `6.7` | Human Oversight Operations | **none** | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |

<details><summary><code>6.1</code> AI Deployment & Serving Operations — 7 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `6.1.1` | **Model & Agent Deployment** | Deploy models and agents into production through a controlled mechanism. | ? |  |
| `6.1.2` | **Inference Serving & Scaling** | Serve inference at required throughput and scale it with demand. | ? |  |
| `6.1.3` | **Configuration & Feature Flag Control** | Change runtime behavior safely without redeployment. | ? |  |
| `6.1.4` | **System Availability & Continuity Management** | Meet availability and continuity commitments for individual AI systems in production. | ? |  |
| `6.1.5` | **Operational Readiness & Handover** | Hand over to operations with documented procedures before go-live. | ? |  |
| `6.1.6` | **Agent Fleet & Version Operations** | Operate many agents as a fleet: pinned versions, coordinated rollout, and detection of behavioural change caused by a dependency moving rather than by a release. | ? |  |
| `6.1.7` | **Provider Failover & Degraded-Mode Operation** | Fail over between model providers, or degrade deliberately, under a policy that is defined and exercised. | ? |  |

</details>

<details><summary><code>6.2</code> AI Monitoring & Observability — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `6.2.1` | **Telemetry Instrumentation & Collection** | Instrument AI systems to emit the signals operations and assurance need. | ? |  |
| `6.2.2` | **Trace & Interaction Logging** | Record prompts, context, outputs and decisions to a defined retention standard. | ? |  |
| `6.2.3` | **Agent Action & Tool-Call Observability** | See every action an agent took, with what arguments and to what effect. | ? |  |
| `6.2.4` | **Alerting & Threshold Management** | Detect abnormal behavior and raise it to someone who can act. | ? |  |
| `6.2.5` | **Operational Dashboarding** | Present operational state to the people accountable for it. | ? |  |

</details>

<details><summary><code>6.3</code> Continuous Evaluation, Drift & Quality Management — 6 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `6.3.1` | **Production Output Quality Monitoring** | Measure output quality on live traffic, not only on test sets. | ? |  |
| `6.3.2` | **Data & Concept Drift Detection** | Detect when inputs or the world have moved away from training conditions. | ? |  |
| `6.3.3` | **Bias & Fairness Monitoring in Production** | Monitor outcome disparities on live populations over time. | ? |  |
| `6.3.4` | **Feedback Capture & Ground-Truth Collection** | Capture corrections and outcomes to build evolving ground truth. | ? |  |
| `6.3.5` | **Retraining & Refresh Triggering** | Trigger retraining or refresh on defined conditions rather than on schedule alone. | ? |  |
| `6.3.6` | **Guardrail Effectiveness Monitoring & Tuning** | Measure block rate, false positives and after-the-fact false negatives, and change-control every threshold adjustment. | ? |  |

</details>

<details><summary><code>6.4</code> AI Incident & Problem Management — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `6.4.1` | **AI Incident Detection & Classification** | Recognise an AI incident as distinct from a conventional IT incident. | ? |  |
| `6.4.2` | **Containment & Kill-Switch Execution** | Stop a model or agent immediately, at any hour, with a tested mechanism. | ? |  |
| `6.4.3` | **Root Cause Analysis** | Establish why an AI system behaved as it did, including at the data and prompt level. | ? |  |
| `6.4.4` | **Regulatory & Stakeholder Notification** | Notify the parties an incident obliges the institution to notify, within the deadline. | ? |  |
| `6.4.5` | **Corrective Action & Lessons Learned** | Close findings and feed them back into design and control. | ? |  |

</details>

<details><summary><code>6.5</code> AI Cost Management — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `6.5.1` | **Consumption Metering & Attribution** | Attribute token, compute and storage consumption to an owner. | ? |  |
| `6.5.2` | **Cost Forecasting & Budget Control** | Forecast AI spend and stop it exceeding authorization. | ? |  |
| `6.5.3` | **Unit Economics & Cost-per-Outcome** | Express cost per transaction, per document or per outcome, not per month. | ? |  |
| `6.5.4` | **Optimization & Rightsizing** | Reduce cost through model, caching and routing choices without losing quality. | ? |  |
| `6.5.5` | **Energy & Carbon Accounting for AI** | Express AI consumption per functional unit in energy and carbon, not only in money. | ? |  |

</details>

<details><summary><code>6.6</code> AI Asset Retirement & Evidence Preservation — 4 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `6.6.1` | **Periodic Recertification & Review** | Re-confirm at defined intervals that a system should remain in service. | ? |  |
| `6.6.2` | **Deprecation & Sunset Planning** | Plan and communicate withdrawal before it happens. | ? |  |
| `6.6.3` | **Decommissioning & Data Disposition** | Remove the system and dispose of its data under retention rules. | ? |  |
| `6.6.4` | **Archive & Evidence Preservation** | Preserve the records that assurance and legal obligations require after retirement. | ? |  |

</details>

<details><summary><code>6.7</code> Human Oversight Operations — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `6.7.1` | **Review & Approval Queue Operation** | Run the queue an agent's actions wait in, with defined routing and coverage. | ? |  |
| `6.7.2` | **Oversight Service Levels & Throughput Management** | Commit to and meet a latency and coverage standard for human decisions. | ? |  |
| `6.7.3` | **Override & Intervention Rate Monitoring** | Monitor how often humans override, and treat a falling rate as a signal rather than as success. | ? |  |
| `6.7.4` | **Reviewer Competence, Rotation & Automation-Bias Control** | Keep the reviewer capable of dissent. | ? |  |
| `6.7.5` | **Oversight Evidence Capture** | Record the human decision so that 7.8.2 can produce it later. | ? |  |

</details>

### D7 · AI Governance, Risk, Security & Assurance

*Able to direct, control, protect and evidence the trustworthy use of AI.*

| ID | Capability | Owner | Pra | Ena | Ski | Def | Level | Why |
|---|---|---|:-:|:-:|:-:|:-:|:-:|---|
| `7.1` | AI Policy, Standards & Management System | Artificial Intelligence | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |
| `7.2` | Responsible & Trustworthy AI Practice | **none** | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |
| `7.3` | AI Risk Management | Risk, Audit & Compliance | ? | n-a | ? | ? | *not rated* | Not rated: nothing has been observed |
| `7.4` | AI Security & Resilience | Cybersecurity | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |
| `7.5` | Privacy & Data Protection for AI | **none** | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |
| `7.6` | Legal, Regulatory & Contractual Compliance for AI | **none** | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |
| `7.7` | AI System & Agent Inventory Management | Artificial Intelligence | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |
| `7.8` | AI Assurance & Evidence Management | IT Risk (Compliance) | ? | ? | ? | ? | *not rated* | Not rated: nothing has been observed |
| `7.9` | AI Impact Assessment & Risk Classification | **none** | ? | n-a | ? | ? | *not rated* | Not rated: nothing has been observed |

<details><summary><code>7.1</code> AI Policy, Standards & Management System — 6 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `7.1.1` | **AI Management System Operation** | Operate the AIMS itself — scope, objectives, reviews, continual improvement. | ? |  |
| `7.1.2` | **AI Policy Development & Maintenance** | Issue and maintain the institutional AI policy set. | ? |  |
| `7.1.3` | **Standards & Technical Guideline Issuance** | Translate policy into standards a delivery team can actually build to. | ? |  |
| `7.1.4` | **Governance Body & Decision Rights Operation** | Run the forums that decide AI matters, with defined authority. | ? |  |
| `7.1.5` | **Exception & Dispensation Management** | Grant, time-box and track departures from standard. | ? |  |
| `7.1.6` | **Conformance Monitoring** | Detect where practice has diverged from policy without waiting for audit. | ? |  |

</details>

<details><summary><code>7.2</code> Responsible & Trustworthy AI Practice — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `7.2.1` | **Fairness Standard Setting & Adjudication** | Set the fairness standard per use case, adjudicate measured disparity against it, and mandate remediation. Measurement is 6.3.3. | ? |  |
| `7.2.2` | **Transparency & Explainability Provision** | Provide explanation proportionate to the decision's consequence. | ? |  |
| `7.2.3` | **Human Agency & Oversight Enforcement** | Verify that designed oversight is actually exercised in operation. | ? |  |
| `7.2.4` | **Contestability & Redress Handling** | Give affected people a route to challenge an AI-influenced outcome. | ? |  |
| `7.2.5` | **Environmental & Social Responsibility** | Account for the environmental and social footprint of AI use. | ? |  |

</details>

<details><summary><code>7.3</code> AI Risk Management — 6 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `7.3.1` | **AI Risk Identification & Taxonomy** | Maintain a common taxonomy of AI risks the institution recognizes. | ? |  |
| `7.3.2` | **Risk Assessment & Scoring** | Assess AI risks consistently enough to compare them across the portfolio. | ? |  |
| `7.3.3` | **Control Design & Treatment Planning** | Design proportionate controls and record accepted residual risk. | ? |  |
| `7.3.4` | **Risk Appetite & Tolerance Setting** | State how much AI risk the institution will carry, by category. | ? |  |
| `7.3.5` | **Risk Monitoring & Reporting** | Track risk position over time and report it to accountable bodies. | ? |  |
| `7.3.6` | **Independent Model Risk Validation** | Validate consequential models independently of the team that built them. | ? |  |

</details>

<details><summary><code>7.4</code> AI Security & Resilience — 7 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `7.4.1` | **AI Threat Modeling** | Model threats specific to AI systems, not only to their hosting infrastructure. | ? |  |
| `7.4.2` | **Model & Supply Chain Integrity** | Verify the provenance and integrity of models, weights and dependencies. | ? |  |
| `7.4.3` | **Injection & Jailbreak Detection and Response** | Detect subversion attempts in live traffic and respond to them. | ? |  |
| `7.4.4` | **Agent Identity & Credential Lifecycle** | Issue, sponsor, rotate and revoke a distinct identity per agent, rather than a shared service account. | ? |  |
| `7.4.5` | **Runtime Authorization & Action Control** | Authorise each consequential action at the moment it is attempted. | ? |  |
| `7.4.6` | **Output Filtering & Content Safety** | Prevent unsafe or disclosing output from reaching its recipient. | ? |  |
| `7.4.7` | **Adversarial & Red-Team Testing** | Actively attempt to make AI systems fail or misbehave, before release and on a recurring basis thereafter. | ? |  |

</details>

<details><summary><code>7.5</code> Privacy & Data Protection for AI — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `7.5.1` | **Privacy Impact Assessment for AI** | Assess privacy impact where AI processing introduces new exposure. | ? |  |
| `7.5.2` | **Personal Data Minimization & Masking** | Reduce personal data to what the purpose requires before it reaches a model. | ? |  |
| `7.5.3` | **Data Subject Rights Handling** | Answer access, correction and objection requests where AI is involved. | ? |  |
| `7.5.4` | **Confidentiality & Non-Disclosure Control** | Prevent confidential material leaving through model providers or outputs. | ? |  |
| `7.5.5` | **Training-Data Privacy Controls** | Control whether institutional data may be used to train provider models. | ? |  |

</details>

<details><summary><code>7.6</code> Legal, Regulatory & Contractual Compliance for AI — 6 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `7.6.1` | **Regulatory Horizon Monitoring** | Track AI regulation across the jurisdictions the institution operates in. | ? |  |
| `7.6.2` | **Applicability & Obligation Mapping** | Determine which obligations apply to which AI system, and record why. | ? |  |
| `7.6.3` | **Intellectual Property & Copyright Control** | Manage IP exposure in both training inputs and generated outputs. | ? |  |
| `7.6.4` | **Records, Disclosure & Registration Obligations** | Meet registration, logging and disclosure duties on time. | ? |  |
| `7.6.5` | **Institutional Legal Status Determination** | Determine, as a prerequisite to any obligation mapping, how the institution's international legal status affects which AI regimes apply. Not a maturity dimension — a legal determination that exists or does not. | ? |  |
| `7.6.6` | **Regulatory Role Determination** | Establish whether the institution acts as provider, deployer or distributor for each AI system, as the prerequisite to obligation mapping. | ? |  |

</details>

<details><summary><code>7.7</code> AI System & Agent Inventory Management — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `7.7.1` | **AI System Registration** | Register every AI system before it reaches production, with mandatory attributes. | ? |  |
| `7.7.2` | **Agent Registration & Attribute Recording** | Record each agent in the inventory with its owner, purpose, scope and identity reference. | ? |  |
| `7.7.3` | **Ownership & Accountability Recording** | Record a named accountable individual for every registered AI system and keep it current as people and teams change. | ? |  |
| `7.7.4` | **Shadow AI Discovery** | Find AI in use that was never registered. | ? |  |
| `7.7.5` | **Inventory Completeness Assurance** | Test that the inventory is actually complete rather than assumed to be. | ? |  |

</details>

<details><summary><code>7.8</code> AI Assurance & Evidence Management — 4 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `7.8.1` | **Control Testing & Assurance Planning** | Plan and perform first- and second-line testing of AI controls on a risk basis. | ? |  |
| `7.8.2` | **Evidence Management & Audit Trail** | Retain evidence in a form an auditor can rely on, without reconstruction. | ? |  |
| `7.8.3` | **External Certification & Attestation** | Obtain and maintain external certification where it is required or valuable. | ? |  |
| `7.8.4` | **Finding Remediation Tracking** | Close audit and assurance findings and evidence the closure. | ? |  |

</details>

<details><summary><code>7.9</code> AI Impact Assessment & Risk Classification — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `7.9.1` | **AI System Impact Assessment** | Conduct the structured impact assessment on affected individuals and groups per ISO/IEC 42005. | ? |  |
| `7.9.2` | **Rights Impact Assessment Determination** | Determine whether a fundamental-rights impact assessment is required for a use case, and conduct it where it is. | ? |  |
| `7.9.3` | **Risk Classification & Tiering** | Assign each use case to a risk tier that determines the controls it must carry. | ? |  |
| `7.9.4` | **Classification Review & Reclassification** | Re-examine impact and risk tier when purpose, data, autonomy or affected population materially change. | ? |  |
| `7.9.5` | **Independent Challenge of First-Line Classification** | Challenge and, where warranted, overturn a proposing team's own assessment of impact or risk tier. | ? |  |

</details>

### D8 · AI People, Skills & Adoption

*Able to build and sustain the human side of AI: who does it, who can, and who will.*

| ID | Capability | Owner | Pra | Ena | Ski | Def | Level | Why |
|---|---|---|:-:|:-:|:-:|:-:|:-:|---|
| `8.1` | AI Operating Model & Decision Rights | Strategic Portfolio Management | ? | n-a | ? | ? | *not rated* | Not rated: nothing has been observed |
| `8.2` | AI Skills & Specialist Capability Building | Strategic Resource Management | ? | n-a | ? | ? | *not rated* | Not rated: nothing has been observed |
| `8.3` | AI Literacy & Awareness | Emerging Tech | ? | n-a | ? | ? | *not rated* | Not rated: nothing has been observed |
| `8.4` | AI Adoption, Enablement & Support | Artificial Intelligence | ? | n-a | ? | ? | *not rated* | Not rated: nothing has been observed |
| `8.5` | AI Change Management & Workforce Transition | Digital Transformation | ? | n-a | ? | ? | *not rated* | Not rated: nothing has been observed |
| `8.6` | AI Community & Reuse Culture | Emerging Tech | ? | n-a | ? | ? | *not rated* | Not rated: nothing has been observed |

<details><summary><code>8.1</code> AI Operating Model & Decision Rights — 4 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `8.1.1` | **Operating Model Design** | Choose and maintain the centralized, federated or hybrid model for AI work. | ? |  |
| `8.1.2` | **Role & Responsibility Definition** | Define the AI roles the institution needs and what each is accountable for. | ? |  |
| `8.1.3` | **Decision Rights & Escalation Paths** | State who may decide what, and where a disagreement goes. | ? |  |
| `8.1.4` | **Capacity & Resourcing Management** | Match available skilled capacity to the committed portfolio. | ? |  |

</details>

<details><summary><code>8.2</code> AI Skills & Specialist Capability Building — 4 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `8.2.1` | **Skills Taxonomy & Assessment** | Define the AI skills required and assess where the institution stands. | ? |  |
| `8.2.2` | **Training & Certification Delivery** | Deliver structured learning against identified gaps. | ? |  |
| `8.2.3` | **Recruitment & Talent Acquisition** | Acquire skills the institution cannot build in time. | ? |  |
| `8.2.4` | **Career Pathways & Retention** | Give AI practitioners a reason to stay. | ? |  |

</details>

<details><summary><code>8.3</code> AI Literacy & Awareness — 4 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `8.3.1` | **Baseline AI Literacy Delivery** | Deliver a common minimum level of AI understanding across the institution. | ? |  |
| `8.3.2` | **Role-Specific Awareness** | Give each role the specific understanding its AI exposure requires. | ? |  |
| `8.3.3` | **Acceptable Use Communication** | Make clear, in practical terms, what staff may and may not do with AI. | ? |  |
| `8.3.4` | **Literacy Coverage Evidence** | Evidence who has received what AI training, to the standard the institution's own policy sets. | ? |  |

</details>

<details><summary><code>8.4</code> AI Adoption, Enablement & Support — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `8.4.1` | **Adoption Planning & Targeting** | Plan adoption deliberately rather than assuming availability creates use. | ? |  |
| `8.4.2` | **User Onboarding & Enablement** | Bring new users to competent use quickly. | ? |  |
| `8.4.3` | **User Support Provision** | Answer users when AI behaves unexpectedly. | ? |  |
| `8.4.4` | **Adoption Measurement** | Measure real usage and depth of use, not licenses issued. | ? |  |
| `8.4.5` | **Champion Network Operation** | Sustain distributed advocates who carry adoption locally. | ? |  |

</details>

<details><summary><code>8.5</code> AI Change Management & Workforce Transition — 5 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `8.5.1` | **Change Impact Assessment** | Assess what AI changes for specific roles and teams before it lands. | ? |  |
| `8.5.2` | **Stakeholder Engagement & Communication** | Engage those affected early enough to influence the design. | ? |  |
| `8.5.3` | **Workforce Transition & Redeployment** | Move people whose work changes into work that is needed. | ? |  |
| `8.5.4` | **Staff Consultation & Representation** | Consult staff representation where AI changes conditions of work. | ? |  |
| `8.5.5` | **Trust & Resistance Management** | Address well-founded concern rather than treating it as an obstacle. | ? |  |

</details>

<details><summary><code>8.6</code> AI Community & Reuse Culture — 3 L3 criteria, 0 observed</summary>

| L3 | Criterion | What it means | Practised | Evidence |
|---|---|---|:-:|---|
| `8.6.1` | **Practitioner Community Operation** | Sustain a working community across organizational boundaries. | ? |  |
| `8.6.2` | **Knowledge Sharing & Documentation** | Capture what was learned in a form others can find and use. | ? |  |
| `8.6.3` | **Reuse Incentives & Recognition** | Make reuse and contribution visibly worth doing. | ? |  |

</details>

---

## What the Bank has built

| Offering | What a team gets | Assets released | Enables |
|---|---|:-:|---|
| **Foundry platform** | Building blocks | 4 of 4 | `5.1`, `5.3`, `5.4` |
| **Foundry agents** | Building blocks | 6 of 8 | `4.4`, `5.1`, `5.6`, `5.8` |
| **Custom MCP servers** | Reference implementation | 4 of 7 | `4.5`, `5.5` |
| **Retrieval on AI Search** | Building blocks | 3 of 3 | `3.6` |
| **Document extraction** | Guidance | 2 of 2 | `3.5` |
| **Approved AI tech stack** | Guidance | 1 of 1 | `4.1`, `5.2` |
| **Agent design guidance** | Guidance | 1 of 1 | `2.2`, `2.5` |


# Enterprise AI Capability Model

**Reference model v0.1** · vendor-neutral composite · generated 2026-09-04

One capability tree covering what the institution must be able to do with AI, decomposed to a level where maturity can be scored against evidence. Lifecycle, risk controls, platform realization and agentic scope attach as overlays, never as branches of the tree.

| | |
|---|---|
| L1 domains | 8 |
| L2 capabilities (the scored unit) | 52 |
| L3 assessment units | 258 |
| L2 capabilities carrying agentic scope | 12 |

---

## 1. How to read this

| Level | What it is | What you do with it |
|---|---|---|
| **L1** | Domain. Covers the space; there are eight and they are mutually exclusive. | Never scored. Averaging a domain hides the one capability that is failing. |
| **L2** | A capability coherent enough to have one accountable owner. | **This is the scored unit.** Current and target maturity, 1–5. |
| **L3** | The assessment unit — where evidence actually exists. | Defines the scope of its L2 and tells you what evidence to gather. Score at L3 only in domains on the critical path. |

The **⬥** marker denotes agentic-AI scope. It is a tag across the tree, not a domain — a separate agentic branch would break mutual exclusivity and date the model within eighteen months.

## 2. The meta-model

### Why one tree and not eight

Every published AI framework is a *different dimension*, not a competing map. AWS CAF-AI is an organizational perspective. IBM's model is platform realization. ISO/IEC 5338 is lifecycle. NIST AI RMF is risk. MITRE is a scoring scale. Merging them into one hierarchy produces a tree that mixes abilities, phases, assets and products — which is why most enterprise AI capability maps fail their first architecture review.

This model keeps a single capability spine. Everything else is an overlay joined by a cross-mapping matrix:

| Overlay | Source | How it attaches |
|---|---|---|
| Lifecycle | ISO/IEC 5338 | A value stream cross-mapped to capabilities |
| Risk & controls | ISO/IEC 42001, NIST AI RMF | Requirements mapped onto capabilities |
| Maturity | MITRE-style 1–5 scale | An attribute on the capability node |
| Realization | Platform and product catalogs | Matrix A and Matrix B, below |
| Agentic scope | IMDA, SAP, Salesforce | A tag (⬥) across the tree |
| Organization | Operating model | Owner attribute on the capability node |

### Capability, pattern, product

The commonest modelling error is wiring a capability straight to a product. Three tiers, and the middle one is the one that gets skipped:

| Tier | What it is | Clock | Example |
|---|---|---|---|
| **Capability** | What the organization is able to do. Survives replacing every vendor. | 5–10 years | `3.6` Knowledge Access & Retrieval |
| **ABB** | Architecture Building Block — one of several competing logical patterns. Vendor-neutral. | 2–5 years | Vector Index & Similarity Search · Lexical + Rerank · Graph Traversal · Hybrid |
| **SBB** | Solution Building Block — the product you run. Has a SKU, a version, a contract. | quarterly | Azure AI Search · pgvector · Cosmos DB vector |

The relationship is many-to-many in **both** directions: one capability realized by several patterns; one pattern by several products; and one product realizing several capabilities. A two-tier model cannot express the third case without duplicating the product under four capabilities — and it is exactly that case (three products realizing one pattern) that surfaces a rationalization finding no maturity questionnaire would ever produce.

Only the **capability** tier appears in this document. Matrix A (capability × ABB) and Matrix B (ABB × SBB) are deliberately separate artifacts, because they change on different clocks. Keeping them in one document is what causes a roadmap to be invalidated by a licensing decision.

### Design rules

1. **The ability test.** *“The organization is able to ___”* must read naturally, and the node must be scorable 1–5 with evidence and an accountable owner. *“We have Databricks”* fails. *“MLOps”* fails as an ambiguous blob — decompose it.
2. **Appears exactly once.** If a capability seems to belong in two places, either it is two distinct capabilities or the parent is wrong. Cross-cutting concerns are handled by overlays, never by duplication.
3. **Stop at L3.** L1 covers the space. L2 is coherent enough to have one owner. L3 is where evidence exists. L4 only where a specific area genuinely needs it.
4. **Score at L2, decompose to L3 on the critical path.** 52 scores is a workshop series; 258 is a survey nobody finishes. Never score L1.

### The fourth overlay: lines of defence

Several capabilities look like duplicates until you know this axis. Designing a prompt boundary (`4.3.5`) and defending one at run time (`7.4.3`) are different capabilities with different owners, different evidence and different failure modes. So are placing a workload (`5.4.4`) and deciding where data may go (`3.1.5`). The model separates **design-time** (D2, D4), **run-time** (D5, D6) and **assurance-time** (D7) — and where a pair could not be separated on that axis it was collapsed to one node.

### How an L2 score is derived from L3 evidence

Without this rule the gap arithmetic is arithmetic performed on opinion.

1. **Weakest link — mandatory for D7 and any capability supporting a risk-tiered use case.** The L2 score may not exceed the lowest scored L3 beneath it.
2. **Median elsewhere**, with an explicit written justification for any override, recorded on the capability.
3. **Never score L1.**
4. An L2 scored with no L3 evidence recorded is marked *unevidenced* and excluded from the heat map, rather than shown as a number.

### Repository anchoring — read before loading this into an EA repository

Every capability carries an anchor class, because a third of this tree would otherwise duplicate capabilities the institution already has.

| Class | Count | What to do with it |
|---|---:|---|
| **New** | 20 | No existing enterprise capability covers it. Record as a new node with a new owner. |
| **Specialization** | 18 | An AI-specific specialization of an existing capability. Keep as its own node, linked to the parent. |
| **Lens** | 14 | **Should not become a separate node.** Record as an AI view on the existing capability, keeping its existing owner. |

Loading the 14 lenses as new nodes is how an institution ends up with two change-management capabilities, two owners and two maturity scores that disagree.

### Where the shape came from, stated plainly

The **L1 partition follows AWS CAF-AI's perspectives**, deliberately, with Security folded into Governance and three domains inserted in the middle. Per-capability provenance records where the *content* came from; it cannot record where the *shape* came from, so it is recorded here. The largest single content source is ISO/IEC 42001. D2, D3 and D4 have no CAF analogue and derive from IBM's GenAI capability model and ISO/IEC 5338.

### What this model does not yet do

- **No control mapping.** ISO/IEC 42001 Annex A and the NIST AI RMF functions are not mapped onto capabilities. Until they are, D7's claim to coverage is an assertion, and **D7 should be carved out of any approval request**.
- **No per-capability rubrics.** One generic 1–5 scale covers all 50.
- **Legal applicability is undetermined.** See section 10.
- **The scale is CMMI-derived**, not a MITRE artifact. It is a generic maturity scale and is described as one.

## 3. Domain index

| ID | Domain | Able to… | L2 | L3 | ⬥ | Lens |
|---|---|---|---:|---:|:-:|---:|
| **D1** | [AI Strategy & Value Management](#d1--ai-strategy--value-management) | set direction for AI and convert it into measurable institutional value | 5 | 26 |  | 2 |
| **D2** | [AI Demand & Solution Shaping](#d2--ai-demand--solution-shaping) | find, qualify and shape AI opportunities into deliverable, adoptable solutions | 6 | 30 | 1 | 1 |
| **D3** | [Data & Knowledge Management](#d3--data--knowledge-management) | supply trusted, governed data and knowledge to AI systems | 7 | 33 |  |  |
| **D4** | [AI Solution Engineering](#d4--ai-solution-engineering) | design, build, customize and validate AI solutions to a defined standard | 7 | 38 | 3 | 2 |
| **D5** | [AI Platform & Infrastructure](#d5--ai-platform--infrastructure) | provide and sustain the technical means to build and run AI | 6 | 29 | 1 | 1 |
| **D6** | [AI Operations & Reliability](#d6--ai-operations--reliability) | run AI in production dependably, observably and affordably | 6 | 28 | 3 | 3 |
| **D7** | [AI Governance, Risk, Security & Assurance](#d7--ai-governance-risk-security--assurance) | direct, control, protect and evidence the trustworthy use of AI | 9 | 49 | 4 |  |
| **D8** | [AI People, Skills & Adoption](#d8--ai-people-skills--adoption) | build and sustain the human side of AI: who does it, who can, and who will | 6 | 25 |  | 5 |

---

## 4. The model

### D1 · AI Strategy & Value Management

*Able to set direction for AI and convert it into measurable institutional value.*

| ID | Assessment subject | Proposed owner | Anchor | Conf. | Criteria | Primary provenance |
|---|---|---|---|---|---:|---|
| `1.1` | **AI Vision & Strategy Definition** | Chief AI Officer | New | medium | 5 | AWS CAF-AI - Business perspective · ISO/IEC 38507 · MITRE AI Maturity Model |
| `1.2` | **AI Portfolio & Investment Management** | Enterprise Portfolio Owner | **Lens** | high | 5 | AWS CAF-AI · Gartner (analyst, non-public) · TOGAF (capability-based planning) |
| `1.3` | **Value Realization & Performance Reporting** | Strategy Performance Owner | **Lens** | high | 5 | WEF AI-First Operating System · MIT CISR · GAO AI Accountability Framework |
| `1.4` | **AI Sourcing & Partner Strategy** | Chief Procurement Officer | Spec. | medium | 5 | ISO/IEC 42001 - third-party control · AWS CAF-AI |
| `1.5` | **AI Ecosystem & Alliance Management** | Chief AI Officer | New | low | 6 | ISO/IEC 42001 - context and interested parties · The Open Group Open Agile Architecture · Institutional practice |

#### 1.1 AI Vision & Strategy Definition

Able to establish and maintain a stated institutional position on AI and keep it current.

| L3 | Assessment unit | Definition |
|---|---|---|
| `1.1.1` | AI Ambition & Positioning | Define what role AI plays in the institutional mandate and how far the organization intends to go. |
| `1.1.2` | AI Strategy Formulation & Refresh | Produce and periodically revise an endorsed AI strategy with explicit scope and stated exclusions. |
| `1.1.3` | Strategic Alignment to Institutional Priorities | Trace every AI objective to a corporate goal, sector strategy or country program. |
| `1.1.4` | AI Principles & Ethical Positioning | Set the non-negotiable commitments that constrain all downstream AI decisions. |
| `1.1.5` | Horizon Scanning & Technology Foresight | Track emerging AI capability and judge what it changes for the institution. |

#### 1.2 AI Portfolio & Investment Management

Able to decide which AI work is funded, in what order, and when it stops.

| L3 | Assessment unit | Definition |
|---|---|---|
| `1.2.1` | AI Investment Case Development | Build comparable business cases stating cost, benefit and risk on a common basis. |
| `1.2.2` | Portfolio Prioritization & Sequencing | Rank and stage the AI portfolio against delivery capacity, risk appetite and dependency. |
| `1.2.3` | Funding & Budget Allocation | Route funds to AI work through a mechanism that survives audit and annual planning. |
| `1.2.4` | Portfolio Balance & Exposure Management | Keep the mix of experimental, scaling and production AI within stated tolerance. |
| `1.2.5` | Stage-Gate & Investment Review | Decide continuation, pivot or termination at defined decision points on recorded criteria. |

#### 1.3 Value Realization & Performance Reporting

Able to prove what AI actually delivered, to the standard a governing body accepts.

| L3 | Assessment unit | Definition |
|---|---|---|
| `1.3.1` | Benefit Definition & Baselining | State expected benefit in measurable terms before build, with a recorded pre-intervention baseline. |
| `1.3.2` | Value Tracking & Attribution | Measure realized benefit and attribute it defensibly to the AI intervention rather than to trend. |
| `1.3.3` | AI Performance Metrics & KPI Management | Maintain the indicator set that describes AI performance institution-wide. |
| `1.3.4` | Executive & Board Reporting | Report AI status, risk and value to governing bodies at their cadence and in their language. |
| `1.3.5` | Post-Implementation Review | Assess delivered outcomes against the approved case and feed findings back into prioritization. |

#### 1.4 AI Sourcing & Partner Strategy

Able to decide what is built, bought or partnered, and to stay able to change that decision.

| L3 | Assessment unit | Definition |
|---|---|---|
| `1.4.1` | Build / Buy / Partner Decisioning | Choose the sourcing route per capability with recorded rationale and revisit triggers. |
| `1.4.2` | AI Vendor & Model Provider Evaluation | Assess providers on capability, trustworthiness, transparency and cost of exit. |
| `1.4.3` | Contractual Safeguards & AI Clauses | Secure rights covering data use, IP, indemnity, audit access and notification of model change. |
| `1.4.4` | Concentration & Exit Risk Management | Limit dependence on any single provider and keep a tested, costed exit path. |
| `1.4.5` | Supplier Performance & Assurance Monitoring | Monitor contracted providers against their obligations and assurance commitments for the life of the relationship. |

#### 1.5 AI Ecosystem & Alliance Management

Able to hold external AI relationships that are not supplier contracts, and to stay operable when the ecosystem around them changes.

| L3 | Assessment unit | Definition |
|---|---|---|
| `1.5.1` | Partnership Portfolio Definition | Decide which external relationships the institution needs in order to hold AI capability it will not build itself. |
| `1.5.2` | Research & Academic Collaboration | Operate collaborations whose output is knowledge, method or evidence rather than a delivered system. |
| `1.5.3` | Peer & Multilateral Cooperation | Exchange AI practice, assets and evidence with counterpart institutions under agreed terms. |
| `1.5.4` | Insourcing / Outsourcing Posture Management | Set and periodically revisit which AI work is held internally and which is placed outside. |
| `1.5.5` | Ecosystem Dependency & Continuity Management | Track aggregate dependency across the external AI ecosystem and stay able to operate when a member changes, merges or exits. |
| `1.5.6` | Partnership Value & Obligation Tracking | Monitor what each relationship returns against what it obliges the institution to do. |


### D2 · AI Demand & Solution Shaping

*Able to find, qualify and shape AI opportunities into deliverable, adoptable solutions.*

| ID | Assessment subject | Proposed owner | Anchor | Conf. | Criteria | Primary provenance |
|---|---|---|---|---|---:|---|
| `2.1` | **Use Case Discovery & Intake** | Demand Management Owner | **Lens** | high | 4 | AWS CAF-AI · Google AI Adoption Framework |
| `2.2` | **AI Use-Case Feasibility & Qualification** | AI Product Owner | New | medium | 4 | IBM Generative AI Capability Model · AWS CAF-AI - Business perspective · The Open Group TOGAF |
| `2.3` | **AI Product Management** | AI Product Owner | Spec. | medium | 5 | WEF AI-First Operating System · The Open Group IT4IT · The Open Group Open Agile Architecture |
| `2.4` | **Business Process & Service Redesign** | Business Process Owner | Spec. | medium | 6 | WEF AI-First Operating System · Consultancy transformation patterns (non-public) · The Open Group Open Agile Architecture |
| `2.5` | **Human-AI Interaction & Oversight Design** ⬥ | Product Design Owner | New | low | 6 | IMDA Model AI Governance Framework · ISO/IEC 42001 |
| `2.6` | **AI Innovation & Incubation** | AI CoE Owner | New | low | 5 | Google AI Adoption Framework · AWS CAF-AI · Institutional practice |

#### 2.1 Use Case Discovery & Intake

Able to surface candidate AI work and admit it through one controlled front door.

| L3 | Assessment unit | Definition |
|---|---|---|
| `2.1.1` | Opportunity Identification & Ideation | Actively generate candidate use cases from business need rather than waiting for requests. |
| `2.1.2` | Demand Intake & Triage | Operate a single intake route that classifies and routes every AI request. |
| `2.1.3` | Use Case Registration & Classification | Record each candidate against a common taxonomy before any build effort begins. |
| `2.1.4` | Duplicate & Reuse Screening | Detect that a request is already solved, in flight, or satisfiable by an existing asset. |

#### 2.2 AI Use-Case Feasibility & Qualification

Able to judge, before build, whether a use case is technically and operationally deliverable and worth doing.

| L3 | Assessment unit | Definition |
|---|---|---|
| `2.2.1` | Technical & Data Feasibility Assessment | Judge whether the data, models and integration required actually exist and are obtainable. |
| `2.2.2` | Cost, Effort & Capacity Feasibility | Estimate build and run cost, effort and the specialist capacity a use case would consume. |
| `2.2.3` | Operational & Adoption Feasibility | Judge whether the receiving business area can absorb, operate and sustain the change. |
| `2.2.4` | Go / No-Go Determination | Make and record a proceed decision with named accountability and stated conditions. |

#### 2.3 AI Product Management

Able to own an AI capability as a product across its life, not as a project that ends.

| L3 | Assessment unit | Definition |
|---|---|---|
| `2.3.1` | AI Product Definition & Roadmapping | Define the product, its users, its boundary and its forward path. |
| `2.3.2` | Requirements & Acceptance Criteria Management | Express what good looks like precisely enough to be tested against. |
| `2.3.3` | User Research & Feedback Integration | Learn from actual use and feed it back into the product. |
| `2.3.4` | Backlog & Release Planning | Sequence work and commit to releases against capacity. |
| `2.3.5` | Product Performance Ownership | Hold a named owner accountable for the product's outcomes in production. |

#### 2.4 Business Process & Service Redesign

Able to change how work is actually done, not merely to add a model to an unchanged process.

| L3 | Assessment unit | Definition |
|---|---|---|
| `2.4.1` | Process Analysis & AI Fit Assessment | Understand the current process well enough to know where AI changes it. |
| `2.4.2` | Target Process & Task Redesign | Design the intended process, including what stops being done. |
| `2.4.3` | Human / Machine Task Allocation | Decide explicitly which tasks move, which stay, and which become supervisory. |
| `2.4.4` | Control Point Redesign | Relocate or rebuild the controls that the old process embedded in human steps. |
| `2.4.5` | Service Model & Service Level Redefinition | Restate the service promise once AI changes what is deliverable. |
| `2.4.6` | Language Coverage & Service Equity | Determine which languages an AI-delivered service must support, and at what measured quality, across the institution's countries. |

#### 2.5 Human-AI Interaction & Oversight Design ⬥

Able to design the human's role in the system, rather than assert oversight in policy alone.

| L3 | Assessment unit | Definition |
|---|---|---|
| `2.5.1` | Autonomy & Interaction Pattern Determination ⬥ | Set and record, per system, the interaction pattern and how much an AI system or agent may do without human confirmation. |
| `2.5.2` | Human Oversight & Intervention Design ⬥ | Design the specific point, information and control through which a human can intervene. |
| `2.5.3` | Explanation & Disclosure Design | Design what the system tells its user about what it is and how it reached an output. |
| `2.5.4` | Escalation & Handover Design ⬥ | Design the path by which work returns to a human, with sufficient context to act. |
| `2.5.5` | Oversight Competence & Workload Design ⬥ | Ensure the person assigned oversight has the time, information, training and authority to actually exercise it. |
| `2.5.6` | Accessible & Inclusive Interaction Design | Design AI-delivered interaction to be usable with assistive technology and across literacy and channel constraints. |

#### 2.6 AI Innovation & Incubation

Able to turn an untested AI idea into evidence, and evidence into either a funded product or a cheap, recorded stop.

| L3 | Assessment unit | Definition |
|---|---|---|
| `2.6.1` | Idea Capture & Innovation Sourcing | Collect candidate AI ideas from staff, partners and technology watch outside the formal demand route. |
| `2.6.2` | Sandboxed Experimentation | Run time-boxed experiments in an environment where failure is contained and permitted. |
| `2.6.3` | Innovation Portfolio & Scaling Decisions | Hold the set of live experiments within capacity and decide which of them scale. |
| `2.6.4` | Experiment-to-Product Transition | Move a proven experiment onto the funded delivery route, or record why it stops. |
| `2.6.5` | Controlled Failure & Learning Capture | Permit experiments to fail and extract reusable learning from the failure. |


### D3 · Data & Knowledge Management

*Able to supply trusted, governed data and knowledge to AI systems.*

| ID | Assessment subject | Proposed owner | Anchor | Conf. | Criteria | Primary provenance |
|---|---|---|---|---|---:|---|
| `3.1` | **Data Governance & Stewardship for AI** | Chief Data Officer | Spec. | high | 5 | EDM Council DCAM/ADAC · ISO/IEC 42001 |
| `3.2` | **Data Sourcing, Licensing & Provenance** | Chief Data Officer | Spec. | high | 5 | NIST AI RMF - Map · EDM Council DCAM/ADAC |
| `3.3` | **Data Quality & Preparation for AI** | Data Product Owner | Spec. | medium | 5 | ISO/IEC 5338 · EDM Council DCAM/ADAC |
| `3.4` | **Metadata, Lineage & Cataloging for AI** | Data Governance Owner | Spec. | high | 4 | EDM Council DCAM/ADAC · ISO/IEC 5338 |
| `3.5` | **Knowledge Corpus & Content Management** | Knowledge Management Owner | New | medium | 5 | IBM GenAI Capability Model |
| `3.6` | **Knowledge Access & Retrieval** | Knowledge Platform Owner | New | low | 5 | IBM GenAI Capability Model · NIST AI 600-1 Generative AI Profile |
| `3.7` | **Derived Representation Management** | Data/ML Platform Owner | New | low | 4 | IBM GenAI Capability Model · ISO/IEC 5338 |

#### 3.1 Data Governance & Stewardship for AI

Able to say who owns each data asset, who may use it, and under what conditions.

| L3 | Assessment unit | Definition |
|---|---|---|
| `3.1.1` | Data Ownership & Stewardship Assignment | Name an accountable owner and an operating steward for each data asset used by AI. |
| `3.1.2` | Data Classification & Sensitivity Labeling | Apply a consistent sensitivity classification that downstream controls can act on. |
| `3.1.3` | Data Access Policy & Entitlement Management | Define and enforce who may access which data, for which purpose. |
| `3.1.4` | Data Retention & Records Management | Apply retention and disposal rules to AI inputs, outputs and interaction records. |
| `3.1.5` | Cross-Border Data Transfer Control | Determine and enforce which jurisdictions the institution's data may be transferred to and processed in. |

#### 3.2 Data Sourcing, Licensing & Provenance

Able to demonstrate lawful, documented origin for every dataset an AI system uses.

| L3 | Assessment unit | Definition |
|---|---|---|
| `3.2.1` | Data Acquisition & Onboarding | Bring external and internal data into the estate through a controlled route. |
| `3.2.2` | Licensing & Permitted-Use Verification | Confirm and record that intended AI use is permitted by the source's terms. |
| `3.2.3` | Provenance & Chain-of-Custody Recording | Record where data came from and every transformation applied to it. |
| `3.2.4` | Consent & Purpose Limitation Management | Track the basis on which data was collected and confine use to it. |
| `3.2.5` | Synthetic Data Generation & Control | Produce and govern synthetic data, including disclosure of its synthetic nature. |

#### 3.3 Data Quality & Preparation for AI

Able to make data fit for the specific AI purpose and to prove it was fit.

| L3 | Assessment unit | Definition |
|---|---|---|
| `3.3.1` | Data Profiling & Quality Assessment | Measure completeness, accuracy, timeliness and consistency against stated thresholds. |
| `3.3.2` | Data Cleansing & Remediation | Correct defects at source where possible, and record what was corrected downstream. |
| `3.3.3` | Representativeness & Bias Screening | Test datasets for gaps and skews relative to the affected population. |
| `3.3.4` | Labeling & Annotation Management | Produce, quality-check and version human and machine labels. |
| `3.3.5` | Dataset Versioning & Snapshotting | Freeze and identify the exact dataset a model or evaluation used. |

#### 3.4 Metadata, Lineage & Cataloging for AI

Able to find data, understand what it means, and trace where it went.

| L3 | Assessment unit | Definition |
|---|---|---|
| `3.4.1` | Data Catalog Management | Maintain a searchable inventory of data assets with their attributes. |
| `3.4.2` | Business Glossary & Semantic Definition | Hold one agreed definition per business term that data assets bind to. |
| `3.4.3` | Lineage Capture & Traceability | Trace a model output back through transformations to source records. |
| `3.4.4` | Data Product Publication | Publish curated, contracted datasets that consumers can depend on. |

#### 3.5 Knowledge Corpus & Content Management

Able to curate the document and content estate that grounded AI depends on.

| L3 | Assessment unit | Definition |
|---|---|---|
| `3.5.1` | Corpus Definition & Curation | Decide what belongs in a knowledge corpus and what is deliberately excluded. |
| `3.5.2` | Content Ingestion & Normalization | Bring heterogeneous content into a consistent, machine-usable form. |
| `3.5.3` | Content Segmentation Design | Choose and apply segmentation that preserves meaning and citability. |
| `3.5.4` | Corpus Freshness & Refresh Management | Keep the corpus current and know how stale any part of it is. |
| `3.5.5` | Authoritative Source Designation | Declare which source wins when two documents disagree. |

#### 3.6 Knowledge Access & Retrieval

Able to return the right knowledge to the right requester, with its provenance intact.

| L3 | Assessment unit | Definition |
|---|---|---|
| `3.6.1` | Retrieval Service Provision | Provide governed retrieval over institutional content — by meaning, by term, or both — as a reusable service. |
| `3.6.2` | Access-Trimmed Retrieval Enforcement | Enforce, at retrieval time, the entitlements determined in 3.1.3, so a requester sees only what they may see. |
| `3.6.3` | Retrieval Quality Evaluation & Tuning | Measure and improve retrieval precision and recall against a known set. |
| `3.6.4` | Multi-Source Federation & Ranking | Retrieve across several repositories and rank the combined result coherently. |
| `3.6.5` | Citation, Grounding & Traceability | Return every answer with the source it rests on, resolvable by the reader. |

#### 3.7 Derived Representation Management

Able to manage derived representations of data as governed assets in their own right.

| L3 | Assessment unit | Definition |
|---|---|---|
| `3.7.1` | Feature Engineering & Store Management | Produce, share and reuse engineered features under version control. |
| `3.7.2` | Embedding Model Selection & Versioning | Choose embedding models deliberately and record which version produced which index. |
| `3.7.3` | Index Lifecycle & Re-embedding | Rebuild and migrate indexes when content or embedding models change. |
| `3.7.4` | Derived Representation Governance | Apply access, retention and residency controls to vector representations. |


### D4 · AI Solution Engineering

*Able to design, build, customize and validate AI solutions to a defined standard.*

| ID | Assessment subject | Proposed owner | Anchor | Conf. | Criteria | Primary provenance |
|---|---|---|---|---|---:|---|
| `4.1` | **AI Architecture Management & Solution Governance** | Chief Enterprise Architect | **Lens** | medium | 7 | The Open Group TOGAF · SAP AI-native North Star architecture · NVIDIA Enterprise AI Factory |
| `4.2` | **Model Selection, Customization & Tuning** | AI Engineering Owner | New | medium | 5 | IBM GenAI Capability Model · ISO/IEC 5338 · NIST AI 600-1 Generative AI Profile |
| `4.3` | **Prompt & Context Engineering** ⬥ | AI Engineering Owner | New | medium | 5 | IBM GenAI Capability Model · NIST AI 600-1 Generative AI Profile · OWASP GenAI Security Project |
| `4.4` | **Agent & Workflow Orchestration Design** ⬥ | AI Engineering Owner | New | low | 6 | Salesforce Agent Development Lifecycle · SAP AI-native North Star architecture · IBM Generative AI Capability Model · IMDA Model AI Governance Framework |
| `4.5` | **Integration & Tool Enablement** ⬥ | Integration Architecture Owner | New | medium | 5 | IBM Generative AI Capability Model · Model Context Protocol specification · SAP AI-native North Star architecture · IMDA Model AI Governance Framework |
| `4.6` | **AI Evaluation & Testing** | Quality Engineering Owner | New | medium | 5 | NIST AI 600-1 Generative AI Profile · ISO/IEC 5338 |
| `4.7` | **AI Release & Change Management** | DevSecOps Owner | **Lens** | high | 5 | ITIL 4 · The Open Group IT4IT · ISO/IEC 5338 |

#### 4.1 AI Architecture Management & Solution Governance

Able to set, steward and enforce the architecture that AI solutions are built to.

| L3 | Assessment unit | Definition |
|---|---|---|
| `4.1.1` | Solution Pattern Selection | Choose the architecture building block that realizes the required capability. |
| `4.1.2` | Reference Architecture Compliance | Build to published reference architectures and detect deviation. |
| `4.1.3` | Architecture Decision Recording | Record significant decisions with alternatives and consequences. |
| `4.1.4` | Non-Functional Requirement Design | Design explicitly for latency, cost, availability, and degradation behavior. |
| `4.1.5` | Architecture Review & Dispensation | Review designs and grant time-boxed exceptions with recorded conditions. |
| `4.1.6` | ABB & Pattern Stewardship | Define, version and retire the institution's logical building blocks and the patterns that compose them. |
| `4.1.7` | Solution Conformance Certification | Certify that a concrete solution conforms to the building blocks and controls it claims, and record the deviations. |

#### 4.2 Model Selection, Customization & Tuning

Able to choose and adapt models on evidence, and to record what was done.

| L3 | Assessment unit | Definition |
|---|---|---|
| `4.2.1` | Model Selection for Use Case | Select a model from within the cleared set against task-specific criteria and evidence. |
| `4.2.2` | Fine-Tuning & Adaptation | Adapt models to institutional context under controlled, repeatable procedure. |
| `4.2.3` | Model Training & Experimentation | Run and track experiments so results are reproducible. |
| `4.2.4` | Model Documentation & Disclosure Production | Produce model cards covering intended use, limits, data and evaluation results. |
| `4.2.5` | Model Versioning & Registration | Register every model version as an identifiable, ownable asset. |

#### 4.3 Prompt & Context Engineering ⬥

Able to treat prompts and context assembly as versioned, tested engineering artifacts.

| L3 | Assessment unit | Definition |
|---|---|---|
| `4.3.1` | Prompt Design & Templating | Design prompts as reusable, parameterized templates rather than embedded strings. |
| `4.3.2` | Prompt Versioning & Registry | Version, review and register prompts as controlled artifacts. |
| `4.3.3` | Context Assembly & Window Management | Assemble context deliberately and manage what is included, ordered and dropped. |
| `4.3.4` | Grounding Strategy Design | Decide what the model is permitted to answer from, and enforce it. |
| `4.3.5` | Prompt & Context Boundary Design ⬥ | Construct prompt and context boundaries that constrain what untrusted content can instruct. |

#### 4.4 Agent & Workflow Orchestration Design ⬥

Able to design what an agent may pursue, how it plans, and where it must stop.

| L3 | Assessment unit | Definition |
|---|---|---|
| `4.4.1` | Agent Specification & Goal Definition ⬥ | State an agent's objective, scope and prohibited actions before it is built. |
| `4.4.2` | Task Decomposition & Planning Design ⬥ | Design how an agent breaks work down and selects its next step. |
| `4.4.3` | Multi-Agent Coordination Design ⬥ | Design how agents delegate, communicate and resolve conflict. |
| `4.4.4` | Agent Memory & State Design ⬥ | Design what an agent retains, for how long, and who else can see it. |
| `4.4.5` | Guardrail & Constraint Design ⬥ | Encode hard limits an agent cannot argue its way past. |
| `4.4.6` | Termination & Loop Control Design ⬥ | Design stopping conditions, budgets and loop detection. |

#### 4.5 Integration & Tool Enablement ⬥

Able to give AI systems safe, governed reach into institutional systems.

| L3 | Assessment unit | Definition |
|---|---|---|
| `4.5.1` | API & System Integration Design | Design integration to institutional systems with contracts and error semantics. |
| `4.5.2` | Tool & Function Definition ⬥ | Define the callable actions exposed to a model, with typed inputs and stated effects. |
| `4.5.3` | Capability Exposure to AI Clients ⬥ | Expose institutional capability to AI clients through the prevailing open tool-interface standard. |
| `4.5.4` | Identity Propagation & Delegated Access ⬥ | Carry the acting user's identity through to the system of record. |
| `4.5.5` | Legacy & Core System Adaptation | Reach systems that were never designed to be called by an AI client. |

#### 4.6 AI Evaluation & Testing

Able to state, before release, what the system does and does not do reliably.

| L3 | Assessment unit | Definition |
|---|---|---|
| `4.6.1` | Evaluation Criteria & Metric Definition | Define the metrics that constitute acceptable performance for this use case. |
| `4.6.2` | Golden Dataset & Test Set Management | Build and maintain representative evaluation sets with known-correct answers. |
| `4.6.3` | Automated Evaluation Harness Operation | Run evaluations repeatably as part of the delivery pipeline. |
| `4.6.4` | Human Review & Expert Evaluation | Obtain qualified human judgement where automated metrics are insufficient. |
| `4.6.5` | Pre-Deployment Acceptance Testing | Test against acceptance criteria and record the result as release evidence. |

#### 4.7 AI Release & Change Management

Able to move AI change into production under control and to reverse it.

| L3 | Assessment unit | Definition |
|---|---|---|
| `4.7.1` | Build & Continuous Integration | Build AI artifacts through an automated, auditable pipeline. |
| `4.7.2` | Promotion & Environment Progression | Move artifacts through environments under defined entry and exit criteria. |
| `4.7.3` | Change Approval & Release Authorization | Authorise AI change through a route proportionate to its risk tier. |
| `4.7.4` | Rollback & Release Reversal | Return a deployed AI system to a previously accepted release. |
| `4.7.5` | Release Documentation & Evidence Capture | Capture at release the evidence that later assurance work will need. |


### D5 · AI Platform & Infrastructure

*Able to provide and sustain the technical means to build and run AI.*

| ID | Assessment subject | Proposed owner | Anchor | Conf. | Criteria | Primary provenance |
|---|---|---|---|---|---:|---|
| `5.1` | **AI Platform Service Provisioning** | AI Platform Owner | Spec. | medium | 5 | AWS CAF-AI - Platform perspective · Microsoft Cloud Adoption Framework for AI · NVIDIA Enterprise AI Factory |
| `5.2` | **Model Access & Traffic Management** | AI Platform Owner | New | low | 5 | IBM Generative AI Capability Model · Microsoft Cloud Adoption Framework for AI · ISO/IEC 42001 |
| `5.3` | **AI Environment & Workspace Management** | Cloud Platform Owner | **Lens** | medium | 4 | Microsoft Cloud Adoption Framework for AI · ISO/IEC 27001 |
| `5.4` | **AI Compute & Capacity Management** | Infrastructure Platform Owner | Spec. | medium | 5 | NVIDIA Enterprise AI Factory · Microsoft Cloud Adoption Framework for AI · FinOps Foundation |
| `5.5` | **Tool & Connector Catalog Management** ⬥ | Integration Platform Owner | New | low | 5 | SAP AI-native North Star architecture · IMDA Model AI Governance Framework · Model Context Protocol specification |
| `5.6` | **AI Developer Experience & Reuse Assets** | Developer Platform Owner | Spec. | medium | 5 | The Open Group IT4IT · The Open Group Open Agile Architecture · AWS CAF-AI |

#### 5.1 AI Platform Service Provisioning

Able to offer AI platform services as a governed, supported institutional service.

| L3 | Assessment unit | Definition |
|---|---|---|
| `5.1.1` | Platform Service Catalog Management | Publish what AI platform services exist, their terms and how to obtain them. |
| `5.1.2` | Landing Zone & Baseline Provisioning | Provision AI environments from a compliant baseline rather than by hand. |
| `5.1.3` | Platform Configuration & Policy Enforcement | Enforce configuration standards technically, not by instruction. |
| `5.1.4` | Platform Service Level Commitment | Commit to and meet service levels for the shared AI platform services the institution offers. |
| `5.1.5` | Platform Upgrade & Deprecation Management | Move consumers across platform versions without stranding them. |

#### 5.2 Model Access & Traffic Management

Able to control which models the institution may call, through one governed path.

| L3 | Assessment unit | Definition |
|---|---|---|
| `5.2.1` | Model Clearance & Approved Model List | Assess candidate models against institutional criteria, record the clearance decision and its conditions, and maintain the approved list. |
| `5.2.2` | Model Traffic Control & Routing | Route all model traffic through a controlled point that can observe and enforce. |
| `5.2.3` | Quota, Throttling & Rate Management | Allocate and enforce consumption limits per consumer. |
| `5.2.4` | Model Provider Credential Management | Issue, rotate and revoke the credentials used to reach model providers and platform services. Agent identity is 7.4.4. |
| `5.2.5` | Model Version Availability & Provider Change Control | Control which model versions remain reachable and absorb provider-side version change without breaking consumers. |

#### 5.3 AI Environment & Workspace Management

Able to give teams isolated places to work without weakening controls.

| L3 | Assessment unit | Definition |
|---|---|---|
| `5.3.1` | Experimentation Environment Provision | Provide safe environments for experimentation with clear data rules. |
| `5.3.2` | Workspace Tenancy & Isolation | Define and enforce the tenancy and isolation topology between team workspaces. |
| `5.3.3` | Network & Private Connectivity Control | Control network reachability of AI services and keep traffic private where required. |
| `5.3.4` | Environment Data Segregation | Prevent production data from reaching environments not cleared for it. |

#### 5.4 AI Compute & Capacity Management

Able to secure and allocate the compute that AI work requires.

| L3 | Assessment unit | Definition |
|---|---|---|
| `5.4.1` | Compute Provisioning & Scheduling | Make compute available to workloads on a predictable basis. |
| `5.4.2` | Capacity Planning & Forecasting | Forecast demand far enough ahead to secure supply. |
| `5.4.3` | Accelerator & Quota Allocation | Allocate scarce accelerator capacity against portfolio priority. |
| `5.4.4` | Workload Placement & Residency Enforcement | Place workloads in locations that enforce the transfer and residency decisions taken in 3.1.5. |
| `5.4.5` | Edge & Disconnected Operation | Run AI where connectivity, latency or residency prevents central serving, including fully offline. |

#### 5.5 Tool & Connector Catalog Management ⬥

Able to control what actions AI systems can reach, as a governed inventory.

| L3 | Assessment unit | Definition |
|---|---|---|
| `5.5.1` | Tool & Connector Catalog Management ⬥ | Maintain the inventory of actions and connectors available to AI systems. |
| `5.5.2` | Tool Source Registration & Approval ⬥ | Register and approve any source of callable tools before an AI client may reach it. |
| `5.5.3` | Tool Permission & Scope Governance ⬥ | Set and enforce the scope each tool grants, at least privilege. |
| `5.5.4` | Third-Party Tool Vetting ⬥ | Assess externally supplied tools and connectors before admission. |
| `5.5.5` | Tool Version & Deprecation Control ⬥ | Manage tool change so agent behavior does not silently shift. |

#### 5.6 AI Developer Experience & Reuse Assets

Able to make the compliant path the easiest path for delivery teams.

| L3 | Assessment unit | Definition |
|---|---|---|
| `5.6.1` | Reference Implementation & Template Provision | Publish working templates that already embed required controls. |
| `5.6.2` | SDK, Library & Component Curation | Curate the approved libraries and shared components teams should build on. |
| `5.6.3` | Self-Service Onboarding | Let a team start correctly without a bespoke engagement. |
| `5.6.4` | Inner-Source & Asset Reuse | Make internally built assets discoverable and reusable across the institution. |
| `5.6.5` | Developer Documentation & Support | Document the platform to the standard its users actually need. |


### D6 · AI Operations & Reliability

*Able to run AI in production dependably, observably and affordably.*

| ID | Assessment subject | Proposed owner | Anchor | Conf. | Criteria | Primary provenance |
|---|---|---|---|---|---:|---|
| `6.1` | **AI Deployment & Serving Operations** ⬥ | AI Operations Owner | Spec. | medium | 5 | IBM Generative AI Capability Model · ITIL 4 · ISO/IEC 5338 |
| `6.2` | **AI Monitoring & Observability** ⬥ | AI SRE Owner | Spec. | medium | 5 | IBM Generative AI Capability Model · NVIDIA Enterprise AI Factory · NIST AI RMF - Measure |
| `6.3` | **Continuous Evaluation, Drift & Quality Management** | AI Product Operations Owner | New | medium | 5 | NIST AI RMF - Measure · ISO/IEC 5338 |
| `6.4` | **AI Incident & Problem Management** ⬥ | Service Operations Owner | **Lens** | high | 5 | ISO/IEC 42001 · NIST AI RMF - Manage · ITIL 4 |
| `6.5` | **AI Cost Management** | FinOps Owner | **Lens** | high | 4 | FinOps Foundation · Microsoft Cloud Adoption Framework for AI · Gartner (analyst, non-public) |
| `6.6` | **AI Asset Retirement & Evidence Preservation** | Asset Management Owner | **Lens** | high | 4 | ISO/IEC 5338 - retirement processes · ISO/IEC 42001 · GAO AI Accountability Framework |

#### 6.1 AI Deployment & Serving Operations ⬥

Able to place AI systems into production and keep them serving.

| L3 | Assessment unit | Definition |
|---|---|---|
| `6.1.1` | Model & Agent Deployment ⬥ | Deploy models and agents into production through a controlled mechanism. |
| `6.1.2` | Inference Serving & Scaling | Serve inference at required throughput and scale it with demand. |
| `6.1.3` | Configuration & Feature Flag Control | Change runtime behavior safely without redeployment. |
| `6.1.4` | System Availability & Continuity Management | Meet availability and continuity commitments for individual AI systems in production. |
| `6.1.5` | Operational Readiness & Handover | Hand over to operations with documented procedures before go-live. |

#### 6.2 AI Monitoring & Observability ⬥

Able to see what an AI system did, in enough detail to explain it afterwards.

| L3 | Assessment unit | Definition |
|---|---|---|
| `6.2.1` | Telemetry Instrumentation & Collection | Instrument AI systems to emit the signals operations and assurance need. |
| `6.2.2` | Trace & Interaction Logging ⬥ | Record prompts, context, outputs and decisions to a defined retention standard. |
| `6.2.3` | Agent Action & Tool-Call Observability ⬥ | See every action an agent took, with what arguments and to what effect. |
| `6.2.4` | Alerting & Threshold Management | Detect abnormal behavior and raise it to someone who can act. |
| `6.2.5` | Operational Dashboarding | Present operational state to the people accountable for it. |

#### 6.3 Continuous Evaluation, Drift & Quality Management

Able to know that a system still performs as it did at release.

| L3 | Assessment unit | Definition |
|---|---|---|
| `6.3.1` | Production Output Quality Monitoring | Measure output quality on live traffic, not only on test sets. |
| `6.3.2` | Data & Concept Drift Detection | Detect when inputs or the world have moved away from training conditions. |
| `6.3.3` | Bias & Fairness Monitoring in Production | Monitor outcome disparities on live populations over time. |
| `6.3.4` | Feedback Capture & Ground-Truth Collection | Capture corrections and outcomes to build evolving ground truth. |
| `6.3.5` | Retraining & Refresh Triggering | Trigger retraining or refresh on defined conditions rather than on schedule alone. |

#### 6.4 AI Incident & Problem Management ⬥

Able to stop AI harm quickly and account for it afterwards.

| L3 | Assessment unit | Definition |
|---|---|---|
| `6.4.1` | AI Incident Detection & Classification | Recognise an AI incident as distinct from a conventional IT incident. |
| `6.4.2` | Containment & Kill-Switch Execution ⬥ | Stop a model or agent immediately, at any hour, with a tested mechanism. |
| `6.4.3` | Root Cause Analysis | Establish why an AI system behaved as it did, including at the data and prompt level. |
| `6.4.4` | Regulatory & Stakeholder Notification | Notify the parties an incident obliges the institution to notify, within the deadline. |
| `6.4.5` | Corrective Action & Lessons Learned | Close findings and feed them back into design and control. |

#### 6.5 AI Cost Management

Able to know what AI costs, per unit of value, and to control it.

| L3 | Assessment unit | Definition |
|---|---|---|
| `6.5.1` | Consumption Metering & Attribution | Attribute token, compute and storage consumption to an owner. |
| `6.5.2` | Cost Forecasting & Budget Control | Forecast AI spend and stop it exceeding authorization. |
| `6.5.3` | Unit Economics & Cost-per-Outcome | Express cost per transaction, per document or per outcome, not per month. |
| `6.5.4` | Optimization & Rightsizing | Reduce cost through model, caching and routing choices without losing quality. |

#### 6.6 AI Asset Retirement & Evidence Preservation

Able to retire AI systems deliberately, with their evidence preserved.

| L3 | Assessment unit | Definition |
|---|---|---|
| `6.6.1` | Periodic Recertification & Review | Re-confirm at defined intervals that a system should remain in service. |
| `6.6.2` | Deprecation & Sunset Planning | Plan and communicate withdrawal before it happens. |
| `6.6.3` | Decommissioning & Data Disposition | Remove the system and dispose of its data under retention rules. |
| `6.6.4` | Archive & Evidence Preservation | Preserve the records that assurance and legal obligations require after retirement. |


### D7 · AI Governance, Risk, Security & Assurance

*Able to direct, control, protect and evidence the trustworthy use of AI.*

| ID | Assessment subject | Proposed owner | Anchor | Conf. | Criteria | Primary provenance |
|---|---|---|---|---|---:|---|
| `7.1` | **AI Policy, Standards & Management System** | AI Management System Owner | Spec. | medium | 6 | ISO/IEC 42001 - AI management system · ISO/IEC 38507 · GAO AI Accountability Framework |
| `7.2` | **Responsible & Trustworthy AI Practice** ⬥ | Responsible AI Owner | New | medium | 5 | NIST AI RMF - Govern · OECD AI Principles · ISO/IEC 42001 |
| `7.3` | **AI Risk Management** | Enterprise Risk Owner | Spec. | high | 6 | NIST AI RMF · ISO/IEC 23894 · ISO/IEC 42005 |
| `7.4` | **AI Security & Resilience** ⬥ | Chief Information Security Officer | New | medium | 7 | OWASP GenAI Security Project · ISO/IEC 27001 · IMDA Model AI Governance Framework · NIST AI RMF |
| `7.5` | **Privacy & Data Protection for AI** | Privacy Officer | Spec. | high | 5 | ISO/IEC 27701 · ISO/IEC 42001 · Institutional data protection framework |
| `7.6` | **Legal, Regulatory & Contractual Compliance for AI** | General Counsel | Spec. | medium | 6 | ISO/IEC 42001 · Institutional legal framework |
| `7.7` | **AI System & Agent Inventory Management** ⬥ | AI Governance Owner | New | low | 5 | ISO/IEC 42001 · GAO AI Accountability Framework |
| `7.8` | **AI Assurance & Evidence Management** | Second-Line Assurance Owner | Spec. | medium | 4 | GAO AI Accountability Framework · ISO/IEC 42001 · Institutional internal audit standards |
| `7.9` | **AI Impact Assessment & Risk Classification** ⬥ | AI Risk & Governance Owner | Spec. | low | 5 | ISO/IEC 42005 · ISO/IEC 23894 · NIST AI RMF - Map · IIA Three Lines Model |

#### 7.1 AI Policy, Standards & Management System

Able to operate a functioning management system for AI, not a policy document.

| L3 | Assessment unit | Definition |
|---|---|---|
| `7.1.1` | AI Management System Operation | Operate the AIMS itself — scope, objectives, reviews, continual improvement. |
| `7.1.2` | AI Policy Development & Maintenance | Issue and maintain the institutional AI policy set. |
| `7.1.3` | Standards & Technical Guideline Issuance | Translate policy into standards a delivery team can actually build to. |
| `7.1.4` | Governance Body & Decision Rights Operation | Run the forums that decide AI matters, with defined authority. |
| `7.1.5` | Exception & Dispensation Management | Grant, time-box and track departures from standard. |
| `7.1.6` | Conformance Monitoring | Detect where practice has diverged from policy without waiting for audit. |

#### 7.2 Responsible & Trustworthy AI Practice ⬥

Able to make the institution's stated AI principles operative in delivered systems.

| L3 | Assessment unit | Definition |
|---|---|---|
| `7.2.1` | Fairness Standard Setting & Adjudication | Set the fairness standard per use case, adjudicate measured disparity against it, and mandate remediation. Measurement is 6.3.3. |
| `7.2.2` | Transparency & Explainability Provision | Provide explanation proportionate to the decision's consequence. |
| `7.2.3` | Human Agency & Oversight Enforcement ⬥ | Verify that designed oversight is actually exercised in operation. |
| `7.2.4` | Contestability & Redress Handling | Give affected people a route to challenge an AI-influenced outcome. |
| `7.2.5` | Environmental & Social Responsibility | Account for the environmental and social footprint of AI use. |

#### 7.3 AI Risk Management

Able to identify, treat and monitor AI risk within a stated appetite.

| L3 | Assessment unit | Definition |
|---|---|---|
| `7.3.1` | AI Risk Identification & Taxonomy | Maintain a common taxonomy of AI risks the institution recognizes. |
| `7.3.2` | Risk Assessment & Scoring | Assess AI risks consistently enough to compare them across the portfolio. |
| `7.3.3` | Control Design & Treatment Planning | Design proportionate controls and record accepted residual risk. |
| `7.3.4` | Risk Appetite & Tolerance Setting | State how much AI risk the institution will carry, by category. |
| `7.3.5` | Risk Monitoring & Reporting | Track risk position over time and report it to accountable bodies. |
| `7.3.6` | Independent Model Risk Validation | Validate consequential models independently of the team that built them. |

#### 7.4 AI Security & Resilience ⬥

Able to defend AI systems against attack, including attacks that use the AI itself.

| L3 | Assessment unit | Definition |
|---|---|---|
| `7.4.1` | AI Threat Modeling | Model threats specific to AI systems, not only to their hosting infrastructure. |
| `7.4.2` | Model & Supply Chain Integrity | Verify the provenance and integrity of models, weights and dependencies. |
| `7.4.3` | Injection & Jailbreak Detection and Response ⬥ | Detect subversion attempts in live traffic and respond to them. |
| `7.4.4` | Agent Identity & Credential Lifecycle ⬥ | Issue, sponsor, rotate and revoke a distinct identity per agent, rather than a shared service account. |
| `7.4.5` | Runtime Authorization & Action Control ⬥ | Authorise each consequential action at the moment it is attempted. |
| `7.4.6` | Output Filtering & Content Safety | Prevent unsafe or disclosing output from reaching its recipient. |
| `7.4.7` | Adversarial & Red-Team Testing | Actively attempt to make AI systems fail or misbehave, before release and on a recurring basis thereafter. |

#### 7.5 Privacy & Data Protection for AI

Able to use personal data in AI without breaching the institution's obligations.

| L3 | Assessment unit | Definition |
|---|---|---|
| `7.5.1` | Privacy Impact Assessment for AI | Assess privacy impact where AI processing introduces new exposure. |
| `7.5.2` | Personal Data Minimization & Masking | Reduce personal data to what the purpose requires before it reaches a model. |
| `7.5.3` | Data Subject Rights Handling | Answer access, correction and objection requests where AI is involved. |
| `7.5.4` | Confidentiality & Non-Disclosure Control | Prevent confidential material leaving through model providers or outputs. |
| `7.5.5` | Training-Data Privacy Controls | Control whether institutional data may be used to train provider models. |

#### 7.6 Legal, Regulatory & Contractual Compliance for AI

Able to know which obligations bind the institution and to demonstrate compliance.

| L3 | Assessment unit | Definition |
|---|---|---|
| `7.6.1` | Regulatory Horizon Monitoring | Track AI regulation across the jurisdictions the institution operates in. |
| `7.6.2` | Applicability & Obligation Mapping | Determine which obligations apply to which AI system, and record why. |
| `7.6.3` | Intellectual Property & Copyright Control | Manage IP exposure in both training inputs and generated outputs. |
| `7.6.4` | Records, Disclosure & Registration Obligations | Meet registration, logging and disclosure duties on time. |
| `7.6.5` | Institutional Legal Status Determination | Determine, as a prerequisite to any obligation mapping, how the institution's international legal status affects which AI regimes apply. Not a maturity dimension — a legal determination that exists or does not. |
| `7.6.6` | Regulatory Role Determination | Establish whether the institution acts as provider, deployer or distributor for each AI system, as the prerequisite to obligation mapping. |

#### 7.7 AI System & Agent Inventory Management ⬥

Able to state, at any moment, every AI system and agent in operation and who owns it.

| L3 | Assessment unit | Definition |
|---|---|---|
| `7.7.1` | AI System Registration ⬥ | Register every AI system before it reaches production, with mandatory attributes. |
| `7.7.2` | Agent Registration & Attribute Recording ⬥ | Record each agent in the inventory with its owner, purpose, scope and identity reference. |
| `7.7.3` | Ownership & Accountability Recording | Record a named accountable individual for every registered AI system and keep it current as people and teams change. |
| `7.7.4` | Shadow AI Discovery | Find AI in use that was never registered. |
| `7.7.5` | Inventory Completeness Assurance | Test that the inventory is actually complete rather than assumed to be. |

#### 7.8 AI Assurance & Evidence Management

Able to produce and retain evidence about AI that an independent reviewer can rely on. Independent assessment of that evidence is Internal Audit's, not this capability's.

| L3 | Assessment unit | Definition |
|---|---|---|
| `7.8.1` | Control Testing & Assurance Planning | Plan and perform first- and second-line testing of AI controls on a risk basis. |
| `7.8.2` | Evidence Management & Audit Trail | Retain evidence in a form an auditor can rely on, without reconstruction. |
| `7.8.3` | External Certification & Attestation | Obtain and maintain external certification where it is required or valuable. |
| `7.8.4` | Finding Remediation Tracking | Close audit and assurance findings and evidence the closure. |

#### 7.9 AI Impact Assessment & Risk Classification ⬥

Able to determine, independently of the team proposing a use case, what impact it may have and what risk tier it belongs to.

| L3 | Assessment unit | Definition |
|---|---|---|
| `7.9.1` | AI System Impact Assessment | Conduct the structured impact assessment on affected individuals and groups per ISO/IEC 42005. |
| `7.9.2` | Rights Impact Assessment Determination | Determine whether a fundamental-rights impact assessment is required for a use case, and conduct it where it is. |
| `7.9.3` | Risk Classification & Tiering | Assign each use case to a risk tier that determines the controls it must carry. |
| `7.9.4` | Classification Review & Reclassification | Re-examine impact and risk tier when purpose, data, autonomy or affected population materially change. |
| `7.9.5` | Independent Challenge of First-Line Classification ⬥ | Challenge and, where warranted, overturn a proposing team's own assessment of impact or risk tier. |


### D8 · AI People, Skills & Adoption

*Able to build and sustain the human side of AI: who does it, who can, and who will.*

| ID | Assessment subject | Proposed owner | Anchor | Conf. | Criteria | Primary provenance |
|---|---|---|---|---|---:|---|
| `8.1` | **AI Operating Model & Decision Rights** | Chief AI Officer | **Lens** | high | 4 | WEF AI-First Operating System · MITRE AI Maturity Model · ISO/IEC 38507 |
| `8.2` | **AI Skills & Specialist Capability Building** | Chief Human Resources Officer | **Lens** | high | 4 | AWS CAF-AI - People perspective · WEF AI-First Operating System · Google AI Adoption Framework |
| `8.3` | **AI Literacy & Awareness** | Learning & Development Owner | New | medium | 4 | ISO/IEC 42001 · OECD AI Principles |
| `8.4` | **AI Adoption, Enablement & Support** | Change Enablement Owner | **Lens** | high | 5 | Google AI Adoption Framework · AWS CAF-AI · WEF AI-First Operating System |
| `8.5` | **AI Change Management & Workforce Transition** | Chief Human Resources Officer | **Lens** | high | 5 | WEF AI-First Operating System · Consultancy transformation patterns (non-public) · OECD AI Principles |
| `8.6` | **AI Community & Reuse Culture** | AI CoE Owner | **Lens** | high | 3 | The Open Group Open Agile Architecture · AWS CAF-AI · Institutional practice |

#### 8.1 AI Operating Model & Decision Rights

Able to say who decides what about AI, and who does the work.

| L3 | Assessment unit | Definition |
|---|---|---|
| `8.1.1` | Operating Model Design | Choose and maintain the centralized, federated or hybrid model for AI work. |
| `8.1.2` | Role & Responsibility Definition | Define the AI roles the institution needs and what each is accountable for. |
| `8.1.3` | Decision Rights & Escalation Paths | State who may decide what, and where a disagreement goes. |
| `8.1.4` | Capacity & Resourcing Management | Match available skilled capacity to the committed portfolio. |

#### 8.2 AI Skills & Specialist Capability Building

Able to grow and retain the specialist skill the portfolio depends on.

| L3 | Assessment unit | Definition |
|---|---|---|
| `8.2.1` | Skills Taxonomy & Assessment | Define the AI skills required and assess where the institution stands. |
| `8.2.2` | Training & Certification Delivery | Deliver structured learning against identified gaps. |
| `8.2.3` | Recruitment & Talent Acquisition | Acquire skills the institution cannot build in time. |
| `8.2.4` | Career Pathways & Retention | Give AI practitioners a reason to stay. |

#### 8.3 AI Literacy & Awareness

Able to ensure everyone who uses or is affected by AI understands enough to act safely.

| L3 | Assessment unit | Definition |
|---|---|---|
| `8.3.1` | Baseline AI Literacy Delivery | Deliver a common minimum level of AI understanding across the institution. |
| `8.3.2` | Role-Specific Awareness | Give each role the specific understanding its AI exposure requires. |
| `8.3.3` | Acceptable Use Communication | Make clear, in practical terms, what staff may and may not do with AI. |
| `8.3.4` | Literacy Coverage Evidence | Evidence who has received what AI training, to the standard the institution's own policy sets. |

#### 8.4 AI Adoption, Enablement & Support

Able to convert delivered AI capability into actual, sustained use.

| L3 | Assessment unit | Definition |
|---|---|---|
| `8.4.1` | Adoption Planning & Targeting | Plan adoption deliberately rather than assuming availability creates use. |
| `8.4.2` | User Onboarding & Enablement | Bring new users to competent use quickly. |
| `8.4.3` | User Support Provision | Answer users when AI behaves unexpectedly. |
| `8.4.4` | Adoption Measurement | Measure real usage and depth of use, not licenses issued. |
| `8.4.5` | Champion Network Operation | Sustain distributed advocates who carry adoption locally. |

#### 8.5 AI Change Management & Workforce Transition

Able to carry the workforce through the change AI causes.

| L3 | Assessment unit | Definition |
|---|---|---|
| `8.5.1` | Change Impact Assessment | Assess what AI changes for specific roles and teams before it lands. |
| `8.5.2` | Stakeholder Engagement & Communication | Engage those affected early enough to influence the design. |
| `8.5.3` | Workforce Transition & Redeployment | Move people whose work changes into work that is needed. |
| `8.5.4` | Staff Consultation & Representation | Consult staff representation where AI changes conditions of work. |
| `8.5.5` | Trust & Resistance Management | Address well-founded concern rather than treating it as an obstacle. |

#### 8.6 AI Community & Reuse Culture

Able to make institutional learning about AI compound rather than repeat.

| L3 | Assessment unit | Definition |
|---|---|---|
| `8.6.1` | Practitioner Community Operation | Sustain a working community across organizational boundaries. |
| `8.6.2` | Knowledge Sharing & Documentation | Capture what was learned in a form others can find and use. |
| `8.6.3` | Reuse Incentives & Recognition | Make reuse and contribution visibly worth doing. |

---

## 5. Maturity scale

| Level | Name | Definition | Evidence you would expect to find |
|:-:|---|---|---|
| **0** | Absent | Applicability confirmed and a documented inquiry finds no operating instance of the ability. | A positive absence finding — not simply the lack of a search. |
| **1** | Initial | Verified isolated execution that relies on individuals and is not repeatable. | Evidence of isolated execution; no common method. |
| **2** | Repeatable | Repeatable within named local scopes over a defined period. | Repeated execution, local ownership, specified coverage. |
| **3** | Defined | An approved common method and roles are applied across the required scope. | A published standard, a coverage rule, sampled conformance. |
| **4** | Managed | Thresholds, exceptions and corrective actions operate over a defined period. | Monitoring with thresholds, control tests, retained evidence. |
| **5** | Adaptive | At least one completed evidence-driven improvement cycle produced a verified outcome. | Trend, action, verified benefit, external comparison. |

**States — not levels. They never enter arithmetic.**

| State | Meaning |
|:-:|---|
| **NE** | Applicable, but evidence is insufficient to rate. Appears in the completeness view. |
| **UC** | Applicability or legal status under clarification. An active decision gap with an owner and a due date. |
| **NA** | Formally not applicable, with approver, rationale, effective date and expiry. |

Absence of evidence is not evidence of absence. `0` means a documented inquiry positively established that the ability does not operate; where that inquiry has not happened the honest answer is `NE` or `UC`.

### How a rating is derived — gated, not averaged

1. The rating is the **highest level for which every applicable mandatory criterion at that level and at all lower levels** is satisfied by valid evidence.
2. Alternative routes are expressed as approved AND/OR gate logic. Enhancing criteria never compensate for an unmet mandatory gate.
3. Conditional criteria enter the gate only when a pre-approved trigger is true; applicability is settled and versioned before evidence is examined.
4. Only a **predeclared essential control** may cap maturity. Other failed controls create conformance gaps and affect assurance rather than silently lowering the organizational rating.
5. **Never rate L1.** Domains are reporting containers.

Every result belongs to an **assessment context** — organizational boundary, as-of date, assessor, rubric version, and in a full implementation jurisdiction, use-case class, risk tier and autonomy level. **Local ratings are not averaged into an enterprise rating**; enterprise maturity is assessed separately against enterprise coverage criteria, and local results are reported as a distribution.

Rate **current** against evidence that exists today, not intent. Set **target** at the level the institution's risk appetite requires — not every subject needs a 5.

**Priority is a governed decision, not a subtraction.** A three-level gap can be low priority and a one-level gap can be urgent. Subjects fall into categorical lanes — *Mandatory/urgent*, *Foundational/enabling*, *Value-led*, *Deferred/monitor*, plus *Blocked* for `NE` and `UC` — and a Priority Decision record capturing outcome contribution, deadline, residual risk, dependency, capacity and sponsor settles each one. Never subtract ordinal levels to estimate effort or benefit.

## 6. Provenance index

Which published framework each capability was normalized from. This is not an endorsement of that framework's wording, and no vendor term is carried into the taxonomy itself. Use it to answer *“where did this come from”* in architecture and audit review.

| Source | Capabilities |
|---|---|
| ISO/IEC 42001 | `2.5`, `3.1`, `5.2`, `6.4`, `6.6`, `7.2`, `7.5`, `7.6`, `7.7`, `7.8`, `8.3` |
| ISO/IEC 5338 | `3.3`, `3.4`, `3.7`, `4.2`, `4.6`, `4.7`, `6.1`, `6.3` |
| AWS CAF-AI | `1.2`, `1.4`, `2.1`, `2.6`, `5.6`, `8.4`, `8.6` |
| WEF AI-First Operating System | `1.3`, `2.3`, `2.4`, `8.1`, `8.2`, `8.4`, `8.5` |
| IBM Generative AI Capability Model | `2.2`, `4.4`, `4.5`, `5.2`, `6.1`, `6.2` |
| GAO AI Accountability Framework | `1.3`, `6.6`, `7.1`, `7.7`, `7.8` |
| IBM GenAI Capability Model | `3.5`, `3.6`, `3.7`, `4.2`, `4.3` |
| IMDA Model AI Governance Framework | `2.5`, `4.4`, `4.5`, `5.5`, `7.4` |
| Microsoft Cloud Adoption Framework for AI | `5.1`, `5.2`, `5.3`, `5.4`, `6.5` |
| The Open Group Open Agile Architecture | `1.5`, `2.3`, `2.4`, `5.6`, `8.6` |
| EDM Council DCAM/ADAC | `3.1`, `3.2`, `3.3`, `3.4` |
| Google AI Adoption Framework | `2.1`, `2.6`, `8.2`, `8.4` |
| NIST AI 600-1 Generative AI Profile | `3.6`, `4.2`, `4.3`, `4.6` |
| NVIDIA Enterprise AI Factory | `4.1`, `5.1`, `5.4`, `6.2` |
| SAP AI-native North Star architecture | `4.1`, `4.4`, `4.5`, `5.5` |
| ISO/IEC 38507 | `1.1`, `7.1`, `8.1` |
| ITIL 4 | `4.7`, `6.1`, `6.4` |
| Institutional practice | `1.5`, `2.6`, `8.6` |
| OECD AI Principles | `7.2`, `8.3`, `8.5` |
| The Open Group IT4IT | `2.3`, `4.7`, `5.6` |
| AWS CAF-AI - Business perspective | `1.1`, `2.2` |
| Consultancy transformation patterns (non-public) | `2.4`, `8.5` |
| FinOps Foundation | `5.4`, `6.5` |
| Gartner (analyst, non-public) | `1.2`, `6.5` |
| ISO/IEC 23894 | `7.3`, `7.9` |
| ISO/IEC 27001 | `5.3`, `7.4` |
| ISO/IEC 42005 | `7.3`, `7.9` |
| MITRE AI Maturity Model | `1.1`, `8.1` |
| Model Context Protocol specification | `4.5`, `5.5` |
| NIST AI RMF | `7.3`, `7.4` |
| NIST AI RMF - Map | `3.2`, `7.9` |
| NIST AI RMF - Measure | `6.2`, `6.3` |
| OWASP GenAI Security Project | `4.3`, `7.4` |
| The Open Group TOGAF | `2.2`, `4.1` |
| AWS CAF-AI - People perspective | `8.2` |
| AWS CAF-AI - Platform perspective | `5.1` |
| IIA Three Lines Model | `7.9` |
| ISO/IEC 27701 | `7.5` |
| ISO/IEC 42001 - AI management system | `7.1` |
| ISO/IEC 42001 - context and interested parties | `1.5` |
| ISO/IEC 42001 - third-party control | `1.4` |
| ISO/IEC 5338 - retirement processes | `6.6` |
| Institutional data protection framework | `7.5` |
| Institutional internal audit standards | `7.8` |
| Institutional legal framework | `7.6` |
| MIT CISR | `1.3` |
| NIST AI RMF - Govern | `7.2` |
| NIST AI RMF - Manage | `6.4` |
| Salesforce Agent Development Lifecycle | `4.4` |
| TOGAF (capability-based planning) | `1.2` |

## 7. AI reference catalog — services, building blocks, patterns, standards

What *could* exist in the AI domain, vendor-neutral and stable. **Nothing here is a capability and nothing here is a product.** 143 entries across 10 groups, 214 typed edges. Four kinds:

| Kind | Meaning | Test | Count |
|---|---|---|---:|
| **SVC** | Service type — something a consumer calls | Can someone call it and get a result? | 76 |
| **ABB** | Logical building block | Is it a piece *inside* an architecture? | 57 |
| **PAT** | Pattern — a governed arrangement of blocks | Does it have forces and a resulting context? | 5 |
| **STD** | Open standard or protocol profile | Is it a specification someone else maintains? | 5 |

Entries marked *either* are genuinely ambiguous: OCR is an ABB when you are designing a document pipeline and a Service when someone exposes an endpoint. Same concept, two registers — not a conflict.

Read this layer with the tier table in section 2 in mind. A service here is expected to be replaced on a 2-5 year clock without the capability model changing.

| ID | Service group | Services | Primary provenance |
|---|---|---:|---|
| **S1** | Content & Perception | 19 | Hugging Face task taxonomy (CV / audio / NLP / multimodal) · ISO/IEC 22989 cl.9 Fields of AI · OECD Classification Framework (Task & Output) |
| **S2** | Generation & Synthesis | 10 | Hugging Face task taxonomy (generation tasks) · OpenTelemetry GenAI semconv (gen_ai.operation.name = chat) · IBM GenAI Capability Model |
| **S3** | Retrieval & Knowledge | 16 | Azure AI Search (BM25 / HNSW / RRF / semantic ranker / agentic retrieval) · AWS Bedrock Knowledge Bases · Google RAG Engine (Gemini Enterprise Agent Platform) |
| **S4** | Reasoning, Prediction & Decision | 10 | ISO/IEC 23053 cl.6.2 (regression, classification, clustering, anomaly detection, dimensionality reduction) · Hugging Face (tabular tasks) · OpenTelemetry GenAI semconv (plan) |
| **S5** | Agent & Orchestration | 15 | MCP specification 2026-07-28 (Agentic AI Foundation / Linux Foundation) · A2A specification 1.0.0 (AAIF) · OpenTelemetry GenAI semconv (invoke_agent, execute_tool, invoke_workflow, create_agent) |
| **S6** | Integration, Gateway & Registry | 15 | MCP specification 2026-07-28 and the official MCP Registry (v0.1, AAIF Registry Working Group) · Azure API Management AI gateway + Azure API Center · Google Agent Gateway / Agent Registry / Skill Registry |
| **S7** | Guardrail, Safety & Assurance | 14 | OWASP Top 10 for LLM Applications (2026) · OWASP Top 10 for Agentic Applications 2026 (ASI01-ASI10) · Azure Content Safety (Prompt Shields, groundedness, protected material, task adherence) |
| **S8** | Model, Data & Experiment | 24 | LF AI & Data Landscape categories (Model, Data, Machine Learning, Deep Learning, Trusted & Responsible AI) · IBM GenAI Capability Model (Model Hub, Model Hosting, Model Customization) · ISO/IEC 23053 cl.8 ML pipeline stages |
| **S9** | Observability, Operations & Cost | 15 | OpenTelemetry GenAI semantic conventions (Development status, semconv-genai repo, v1.42.0) · IBM Model Monitoring · AWS Bedrock observability and cost-optimization categories |
| **S10** | Standards & Protocol Profiles | 5 | Model Context Protocol specification · A2A specification · OpenTelemetry GenAI semantic conventions |

### S1 · Content & Perception

*Turn unstructured input — documents, speech, images, video, text — into structured, machine-usable meaning.*

Group provenance: Hugging Face task taxonomy (CV / audio / NLP / multimodal) · ISO/IEC 22989 cl.9 Fields of AI · OECD Classification Framework (Task & Output) · Microsoft Foundry Tools · AWS pretrained AI services · Google Document AI

| ID | Entry | Kind | Definition | Typed edges | Flags |
|---|---|---|---|---|---|
| `S1.1` | **Optical Character Recognition** | **SVC** | Extract machine-readable text from scanned or photographed documents. | `3.5.2` required-enabler |  |
| `S1.2` | **Document Layout & Structure Analysis** | **SVC** | Recover reading order, sections, headings and hierarchy from a document. | `3.5.2` required-enabler, `3.5.3` required-enabler |  |
| `S1.3` | **Form & Key-Value Extraction** | **SVC** | Extract labelled field values from structured and semi-structured forms. | `3.5.2` required-enabler |  |
| `S1.4` | **Table Extraction** | **SVC** | Recover tabular structure and cell values from documents. | `3.5.2` required-enabler |  |
| `S1.5` | **Document Classification & Splitting** | **SVC** | Assign document type and divide multi-document files into constituent parts. | `3.5.1` required-enabler, `3.5.2` required-enabler |  |
| `S1.6` | **Handwriting Recognition** | **SVC** | Read handwritten content from documents and images. | `3.5.2` required-enabler |  |
| `S1.7` | **Speech-to-Text** | **SVC** | Transcribe spoken audio into text. | `3.5.2` required-enabler |  |
| `S1.8` | **Speaker Diarization & Recognition** | **SVC** | Separate and identify speakers within an audio stream. | — | ⚑ regulatory |
| `S1.9` | **Audio Classification** | **SVC** | Classify non-speech audio content and events. | — |  |
| `S1.10` | **Image Classification & Tagging** | **SVC** | Assign labels and tags to image content. | — |  |
| `S1.11` | **Object Detection & Segmentation** | **SVC** | Locate and delineate objects within images and video. | — |  |
| `S1.12` | **Face Detection & Recognition** | **SVC** | Detect and match human faces. | — | ⚑ regulatory |
| `S1.13` | **Video Analysis & Indexing** | **SVC** | Extract structure, entities and events from video. | `3.5.2` required-enabler |  |
| `S1.14` | **Named Entity Recognition** | **SVC** | Identify and type entities within text. | `3.5.2` required-enabler |  |
| `S1.15` | **Text Classification & Sentiment** | **SVC** | Assign categories, intent or sentiment to text. | — |  |
| `S1.16` | **Sensitive Data Detection** | **SVC** | Classifies spans of text, audio or image content as personal or sensitive and emits typed span annotations. | `3.1.2` required-enabler, `7.5.2` required-enabler | ⚑ regulatory |
| `S1.17` | **Language Identification** | **SVC** | Determine the natural language of a text or audio input. | — |  |
| `S1.18` | **Machine Translation** | **SVC** | Translate content between natural languages. | `2.4.6` required-enabler |  |
| `S1.19` | **Composite Content Understanding Pattern** | **PAT** | Composition pattern: chains extraction, transcription and generation services to emit records against a declared schema. | `3.5.2` required-enabler, `3.5.3` required-enabler | *either* |

### S2 · Generation & Synthesis

*Produce new content — text, structured data, code, speech, image, video — from a model.*

Group provenance: Hugging Face task taxonomy (generation tasks) · OpenTelemetry GenAI semconv (gen_ai.operation.name = chat) · IBM GenAI Capability Model · OECD Classification Framework (generative configuration)

| ID | Entry | Kind | Definition | Typed edges | Flags |
|---|---|---|---|---|---|
| `S2.1` | **Text Generation & Completion** | **SVC** | Generate free-form text from a prompt and supplied context. | `4.3.3` required-enabler |  |
| `S2.2` | **Conversational Response Generation** | **SVC** | Sustain multi-turn dialogue with state across turns. | — |  |
| `S2.3` | **Summarization** | **SVC** | Condense longer content while preserving stated meaning. | — |  |
| `S2.4` | **Rewriting, Style & Tone Transfer** | **SVC** | Restate content in a different register, format or reading level. | `2.5.6` required-enabler |  |
| `S2.5` | **Structured & Schema-Constrained Output** | **SVC** | Constrain generation to a declared schema so output is machine-consumable. | `4.5.2` required-enabler, `4.3.1` required-enabler |  |
| `S2.6` | **Code Generation & Transformation** | **SVC** | Generate, translate or refactor source code. | — |  |
| `S2.7` | **Text-to-Speech & Voice Synthesis** | **SVC** | Render text as spoken audio, optionally in a specified voice. | `2.5.6` required-enabler | ⚑ regulatory |
| `S2.8` | **Image Generation & Editing** | **SVC** | Generate or modify images from text or image input. | — | ⚑ regulatory |
| `S2.9` | **Video & Animation Generation** | **SVC** | Generate or transform moving image content. | — | ⚑ regulatory |
| `S2.10` | **Synthetic Data Generation** | **SVC** | Produce artificial data that preserves the statistical shape of real data. | `3.2.5` required-enabler |  |

### S3 · Retrieval & Knowledge

*Find, rank and ground content so that generation and decisions rest on identifiable sources.*

Group provenance: Azure AI Search (BM25 / HNSW / RRF / semantic ranker / agentic retrieval) · AWS Bedrock Knowledge Bases · Google RAG Engine (Gemini Enterprise Agent Platform) · Hugging Face (sentence-similarity, feature-extraction, text-ranking) · OpenTelemetry GenAI semconv (retrieval, embeddings) · IBM GenAI Capability Model

| ID | Entry | Kind | Definition | Typed edges | Flags |
|---|---|---|---|---|---|
| `S3.1` | **Lexical Search** | **SVC** | Retrieve by literal term match and term-frequency scoring. | `3.6.1` optional-enabler, `3.6.4` optional-enabler |  |
| `S3.2` | **Vector Similarity Search** | **SVC** | Retrieve by proximity in embedding space rather than term match. | `3.6.1` optional-enabler | *either* |
| `S3.3` | **Rank Fusion Service** | **SVC** | Combines several ranked result sets into one ordered list by a declared fusion function. | `3.6.4` optional-enabler |  |
| `S3.4` | **Semantic Reranking** | **SVC** | Re-order a candidate set with a model that scores relevance directly. | `3.6.1` optional-enabler, `3.6.3` required-enabler | *either* |
| `S3.5` | **Query Understanding, Rewriting & Decomposition** | **SVC** | Interpret and restructure a request before retrieval, including breaking it into subqueries. | `3.6.1` optional-enabler, `3.6.4` optional-enabler | ⬥ agentic |
| `S3.6` | **Content Chunking & Segmentation** | **ABB** | Divide source content into retrievable units that preserve meaning and citability. | `3.5.3` required-enabler |  |
| `S3.7` | **Embedding Generation** | **ABB** | Produce vector representations of content for similarity operations. | `3.7.2` required-enabler |  |
| `S3.8` | **Vector Index Management** | **ABB** | Builds, refreshes, compacts and migrates vector indexes, including re-embedding on model or content change. | `3.7.3` required-enabler, `3.7.4` required-enabler |  |
| `S3.9` | **Knowledge Graph Construction & Traversal** | **ABB** | Represent entities and relationships explicitly and query across them. | `3.4.2` required-enabler, `3.6.1` optional-enabler |  |
| `S3.10` | **Access-Trimmed Retrieval** | **ABB** | Applies the requester's entitlement set as a filter at query time, before ranking, so non-entitled documents never enter the result set. | `3.6.2` required-enabler | ⚑ regulatory |
| `S3.11` | **Federated & Multi-Source Retrieval** | **ABB** | Issues subqueries to several indexed and live repositories in parallel and merges their results into one ranked list. | `3.6.4` optional-enabler |  |
| `S3.12` | **Grounding, Citation & Attribution** | **SVC** | Bind generated statements to resolvable sources. | `3.6.5` required-enabler, `7.2.2` required-enabler |  |
| `S3.13` | **Agentic Retrieval Pattern** | **PAT** | Plan, execute and refine multiple retrieval passes autonomously. | `3.6.1` optional-enabler, `4.4.2` required-enabler | ⬥ agentic |
| `S3.14` | **Recommendation & Similarity Matching** | **SVC** | Surface related items on learned similarity or behavior. | `3.6.4` optional-enabler |  |
| `S3.15` | **Governed Corpus Serving** | **SVC** | Serves a curated corpus behind a stable addressable endpoint with its own access policy, freshness state and version. | `3.5.1` required-enabler, `3.5.4` required-enabler, `3.5.5` required-enabler | *either* |
| `S3.16` | **Hybrid Retrieval Pattern** | **PAT** | Composes Lexical Retrieval, Vector Retrieval and Rank Fusion, optionally with Semantic Reranking, over one corpus. | `3.6.1` optional-enabler, `3.6.4` optional-enabler |  |

### S4 · Reasoning, Prediction & Decision

*Produce a judgement, forecast, score or plan rather than content.*

Group provenance: ISO/IEC 23053 cl.6.2 (regression, classification, clustering, anomaly detection, dimensionality reduction) · Hugging Face (tabular tasks) · OpenTelemetry GenAI semconv (plan) · AWS Bedrock Automated Reasoning

| ID | Entry | Kind | Definition | Typed edges | Flags |
|---|---|---|---|---|---|
| `S4.1` | **Classification & Scoring** | **SVC** | Assign a class or score to a case using a trained model. | — |  |
| `S4.2` | **Regression & Estimation** | **SVC** | Predict a continuous value from input features. | — |  |
| `S4.3` | **Time-Series Forecasting** | **SVC** | Project a series forward from historical observations. | — |  |
| `S4.4` | **Anomaly & Outlier Detection** | **SVC** | Identify observations that depart from expected behavior. | `6.2.4` required-enabler, `6.3.2` required-enabler |  |
| `S4.5` | **Clustering & Segmentation** | **SVC** | Group cases by similarity without predefined labels. | — |  |
| `S4.6` | **Optimization & Allocation** | **SVC** | Select the best option under stated constraints and objectives. | — |  |
| `S4.7` | **Rules & Policy Decisioning** | **SVC** | Apply deterministic rules, alone or combined with a model. | `2.4.4` required-enabler, `7.1.6` required-enabler |  |
| `S4.8` | **Planning & Task Decomposition** | **SVC** | Break a goal into an ordered set of executable steps. | `4.4.2` required-enabler | ⬥ agentic |
| `S4.9` | **Model-Based Evaluation** | **SVC** | Use a model to score the output of another model against criteria. | `4.6.3` required-enabler, `6.3.1` evidence-provider |  |
| `S4.10` | **Formal & Verifiable Reasoning Checks** | **SVC** | Verify an output against formally expressed rules rather than by classifier judgement. | `4.6.5` required-enabler, `7.2.2` evidence-provider |  |

### S5 · Agent & Orchestration

*Let a system pursue a goal across multiple steps, calling tools and other agents, with state and stopping conditions.*

Group provenance: MCP specification 2026-07-28 (Agentic AI Foundation / Linux Foundation) · A2A specification 1.0.0 (AAIF) · OpenTelemetry GenAI semconv (invoke_agent, execute_tool, invoke_workflow, create_agent) · IBM GenAI Capability Model (Agentic AI: routing & orchestration, tool management) · SAP AI-native North Star (agentic orchestration, harness engineering) · Salesforce Agent Development Lifecycle · CSA MAESTRO (Agent Frameworks layer)

| ID | Entry | Kind | Definition | Typed edges | Flags |
|---|---|---|---|---|---|
| `S5.1` | **Agent Runtime & Execution** | **SVC** | Host and execute an agent's reasoning-action loop under supervision. | `6.1.1` required-enabler, `4.4.1` required-enabler | ⬥ agentic *either* |
| `S5.2` | **Agent Definition & Declarative Specification** | **ABB** | Express an agent's goal, scope, tools and limits as a versioned artifact. | `4.4.1` required-enabler, `7.7.2` required-enabler | ⬥ agentic |
| `S5.3` | **Tool & Function Calling** | **SVC** | Let a model invoke a declared, typed capability and consume its result. | `4.5.2` required-enabler, `4.4.1` required-enabler | ⬥ agentic *either* |
| `S5.4` | **Agent Orchestrator Runtime** | **ABB** | Executes a coordination topology over several agents, routing work and consolidating results. | `4.4.3` required-enabler | ⬥ agentic |
| `S5.5` | **Agent-to-Agent Interoperability** | **ABB** | Let agents from different owners discover and transact with one another. | `4.4.3` required-enabler, `4.5.4` required-enabler | ⬥ agentic |
| `S5.6` | **Deterministic Workflow Orchestration** | **ABB** | Run a fixed sequence of steps where autonomy is not wanted. | `4.4.6` required-enabler, `2.4.2` required-enabler |  |
| `S5.7` | **Session & Short-Term Memory** | **ABB** | Retain state within a single interaction or task. | `4.4.4` required-enabler | ⬥ agentic |
| `S5.8` | **Persistent & Long-Term Memory** | **ABB** | Retain state across sessions, with retention and visibility rules. | `4.4.4` required-enabler, `3.1.4` required-enabler | ⬥ agentic |
| `S5.9` | **Context Assembly & Management** | **ABB** | Select, order and budget what enters the model's context window. | `4.3.3` required-enabler | ⬥ agentic |
| `S5.10` | **Human-in-the-Loop Interrupt & Approval** | **SVC** | Route a decision or action to a person before it takes effect. | `2.5.2` required-enabler, `2.5.4` required-enabler, `7.2.3` required-enabler | ⬥ agentic |
| `S5.11` | **Task State & Long-Running Job Management** | **ABB** | Track work that outlives a single request, including resumption and cancellation. | `4.4.6` required-enabler, `6.1.1` required-enabler | ⬥ agentic |
| `S5.12` | **Sandboxed Code Execution** | **SVC** | Execute generated code in an isolated environment with bounded effect. | `4.4.5` required-enabler, `7.4.5` required-enabler | ⬥ agentic |
| `S5.13` | **Termination, Budget & Loop Control** | **ABB** | Stop an agent on cost, time, step-count or repetition conditions. | `4.4.6` required-enabler, `6.5.1` operational-support | ⬥ agentic |
| `S5.14` | **Agent Skill Packaging & Distribution** | **ABB** | Package reusable agent competence for discovery and reuse. | `5.6.4` required-enabler, `5.5.1` required-enabler | ⬥ agentic |
| `S5.15` | **Multi-Agent Coordination Patterns** | **PAT** | Named topologies for agent collaboration: supervisor/worker, handoff, sequential, concurrent fan-out, group, hierarchical, reviewer/debate and event-driven. | `4.4.3` required-enabler | ⬥ agentic |

### S6 · Integration, Gateway & Registry

*Broker every call between AI systems and the institution's systems, under one governed, discoverable path.*

Group provenance: MCP specification 2026-07-28 and the official MCP Registry (v0.1, AAIF Registry Working Group) · Azure API Management AI gateway + Azure API Center · Google Agent Gateway / Agent Registry / Skill Registry · AWS Bedrock AgentCore Gateway · SAP MCP Gateway and Agent Gateway · Microsoft Entra Agent ID · CSA Agentic Identity Governance Framework v1 (draft white paper) · OpenID Foundation AI Identity Management CG (pre-standard) · IETF agent-identity Internet-Drafts (individual, not adopted)

| ID | Entry | Kind | Definition | Typed edges | Flags |
|---|---|---|---|---|---|
| `S6.1` | **Model Gateway & Unified Inference API** | **SVC** | Front several model providers behind one governed endpoint and schema. | `5.2.2` required-enabler, `5.2.1` required-enabler | *either* |
| `S6.2` | **Model Routing & Fallback** | **ABB** | Direct each request to an appropriate model on cost, capability or availability. | `5.2.2` required-enabler, `5.2.5` required-enabler, `6.5.4` operational-support |  |
| `S6.3` | **MCP Server Adapter** | **ABB** | Expose an institutional capability to AI clients as an MCP server. | `4.5.3` required-enabler, `4.5.5` required-enabler | ⬥ agentic |
| `S6.4` | **MCP Client Adapter** | **ABB** | Consume external MCP servers from an institutional AI client. | `4.5.3` required-enabler, `5.5.4` required-enabler | ⬥ agentic |
| `S6.5` | **MCP Gateway** | **SVC** | Terminates tool-protocol traffic at a policy enforcement point and forwards to approved backends. | `5.2.2` required-enabler, `5.5.3` required-enabler, `7.4.5` control-enforcer | ⬥ agentic *either* |
| `S6.6` | **Approved Tool & Server Registry** | **ABB** | Holds the institution's approved tool servers and their approval state; distinct from any public registry. | `5.5.1` required-enabler, `5.5.2` required-enabler | ⬥ agentic *either* |
| `S6.7` | **Third-Party Connector Integration** | **ABB** | Reach external SaaS and partner systems through governed connectors. | `4.5.1` required-enabler, `5.5.4` required-enabler | ⬥ agentic |
| `S6.8` | **Identity Propagation & Delegated Authorization** | **SVC** | Exchanges the calling user's token for a downstream credential carrying that user's identity and scoped consent. | `4.5.4` required-enabler, `7.4.5` control-enforcer | ⬥ agentic *either* |
| `S6.9` | **Agent Identity & Credential Issuance** | **ABB** | Give each agent a distinct, sponsored, revocable identity. | `7.4.4` control-enforcer, `7.7.2` control-enforcer | ⬥ agentic *either* |
| `S6.10` | **Rate Limiting, Quota & Throttling** | **ABB** | Bound consumption per consumer, per model and per tool. | `5.2.3` required-enabler, `6.5.2` required-enabler |  |
| `S6.11` | **Semantic & Prompt Caching** | **ABB** | Reuse prior results to cut latency and cost. | `6.5.4` operational-support, `5.2.2` required-enabler |  |
| `S6.12` | **Event & Message Integration** | **ABB** | Trigger AI work from, and emit results to, institutional event streams. | `4.5.1` required-enabler |  |
| `S6.13` | **Business Capability API Exposure** | **ABB** | Publish institutional business functions as callable, contracted APIs for AI to use. | `4.5.1` required-enabler, `4.5.5` required-enabler |  |
| `S6.14` | **Brokered External Federation Pattern** | **PAT** | Composes Gateway, Registry, Delegated Authorization, Runtime Action Policy and Audit ABBs to admit third-party tool servers across a trust boundary. | `5.5.3` required-enabler, `7.4.5` control-enforcer | ⬥ agentic |
| `S6.15` | **Agent & Skill Discovery Catalog** | **ABB** | Publishes discoverable agent and skill descriptors for internal consumers, separate from the approval registry. | `7.7.2` control-enforcer, `5.6.4` required-enabler | ⬥ agentic |

### S7 · Guardrail, Safety & Assurance

*Constrain what goes into and comes out of an AI system, and what an agent is permitted to do at runtime.*

Group provenance: OWASP Top 10 for LLM Applications (2026) · OWASP Top 10 for Agentic Applications 2026 (ASI01-ASI10) · Azure Content Safety (Prompt Shields, groundedness, protected material, task adherence) · AWS Bedrock Guardrails and Automated Reasoning checks · C2PA specification 2.4 (incl. AI/ML guidance) · NIST AI 600-1 Generative AI Profile · CSA MAESTRO

| ID | Entry | Kind | Definition | Typed edges | Flags |
|---|---|---|---|---|---|
| `S7.1` | **Input Content Filtering** | **SVC** | Screen incoming content for harmful or disallowed material before it reaches a model. | `7.4.6` control-enforcer, `7.2.1` control-enforcer |  |
| `S7.2` | **Output Content Filtering** | **SVC** | Screen generated content before it reaches its recipient. | `7.4.6` control-enforcer |  |
| `S7.3` | **Sensitive Data Redaction & Masking** | **SVC** | Transforms detected sensitive spans by masking, tokenizing or removing them before storage or transmission. | `7.5.2` control-enforcer, `7.5.4` control-enforcer, `3.1.2` control-enforcer | ⚑ regulatory |
| `S7.4` | **Prompt Injection & Jailbreak Detection** | **SVC** | Detect attempts to subvert instructions, directly or through retrieved content. | `7.4.3` control-enforcer | ⬥ agentic |
| `S7.5` | **Groundedness & Hallucination Detection** | **SVC** | Test whether an assertion is supported by the supplied source material. | `6.3.1` evidence-provider, `3.6.5` required-enabler | *either* |
| `S7.6` | **Topic & Scope Enforcement** | **SVC** | Keep a system inside its declared purpose and refuse out-of-scope requests. | `7.1.6` control-enforcer, `4.4.5` control-enforcer |  |
| `S7.7` | **Protected Material & IP Leakage Detection** | **SVC** | Detect reproduction of copyrighted or protected content in output. | `7.6.3` control-enforcer, `7.5.4` control-enforcer | ⚑ regulatory |
| `S7.8` | **Agent Action & Task Adherence Monitoring** | **SVC** | Detect tool calls and actions that are misaligned, premature or outside the agent's remit. | `7.2.3` control-enforcer, `6.2.3` control-enforcer | ⬥ agentic |
| `S7.9` | **Runtime Action Authorization & Gating** | **ABB** | Decide, at the moment of the call, whether an agent may perform a consequential action. | `7.4.5` control-enforcer, `4.4.5` control-enforcer | ⬥ agentic *either* |
| `S7.10` | **Output Provenance & Watermarking** | **ABB** | Mark generated content so downstream consumers can establish origin. | `7.2.2` control-enforcer, `7.6.4` control-enforcer | ⚑ regulatory |
| `S7.11` | **Abuse & Unbounded-Consumption Detection** | **ABB** | Detect misuse patterns and runaway resource consumption. | `7.4.7` control-enforcer, `6.5.1` operational-support | ⬥ agentic |
| `S7.12` | **AI-Channel Data Loss Prevention** | **ABB** | Inspects prompts, tool arguments and outputs against classification labels and blocks or quarantines transfers that breach policy. | `7.5.4` control-enforcer, `7.4.6` control-enforcer | ⚑ regulatory |
| `S7.13` | **Emergency Stop & Capability Revocation** | **SVC** | Halts inference and agent execution and revokes agent credentials and tool grants across the fleet, from a single tested trigger. | `6.4.2` control-enforcer, `7.4.4` control-enforcer, `5.5.3` control-enforcer | ⬥ agentic *either* |
| `S7.14` | **Adversarial Test Harness** | **SVC** | Runs curated attack suites against a deployed system and records outcomes as reproducible evidence. | `7.4.7` evidence-provider, `7.4.1` operational-support | ⬥ agentic |

### S8 · Model, Data & Experiment

*The substrate every other service depends on: models, data, features, prompts and the machinery to train, register and evaluate them.*

Group provenance: LF AI & Data Landscape categories (Model, Data, Machine Learning, Deep Learning, Trusted & Responsible AI) · IBM GenAI Capability Model (Model Hub, Model Hosting, Model Customization) · ISO/IEC 23053 cl.8 ML pipeline stages · NVIDIA Enterprise AI Factory software stack · Databricks platform components · CD Foundation MLOps SIG

| ID | Entry | Kind | Definition | Typed edges | Flags |
|---|---|---|---|---|---|
| `S8.1` | **Model Catalog & Marketplace** | **ABB** | Publish the models available to the institution and the terms of their use. | `5.2.1` required-enabler, `4.2.1` required-enabler |  |
| `S8.2` | **Model Registry & Versioning** | **ABB** | Stores model artifacts with immutable version identifiers, lineage pointers and stage labels, and serves them to deployment. | `4.2.5` required-enabler |  |
| `S8.3` | **Model Serving & Inference Runtime** | **SVC** | Host models and serve inference at required throughput. | `6.1.2` required-enabler, `5.1.1` required-enabler | *either* |
| `S8.4` | **Batch & Asynchronous Inference** | **SVC** | Process large volumes offline where latency is not the constraint. | `6.1.2` required-enabler, `6.5.4` optional-enabler |  |
| `S8.5` | **Fine-Tuning & Adaptation** | **SVC** | Adapt a base model to institutional context and task. | `4.2.2` optional-enabler | *either* |
| `S8.6` | **Model Distillation & Compression** | **SVC** | Produce a smaller, cheaper model that preserves acceptable behavior. | `6.5.4` optional-enabler, `4.2.2` optional-enabler |  |
| `S8.7` | **Training & Distributed Compute** | **ABB** | Train models at scale across accelerated infrastructure. | `4.2.3` required-enabler, `5.4.1` required-enabler |  |
| `S8.8` | **Experiment Tracking** | **ABB** | Record runs, parameters and results so work is reproducible. | `4.2.3` required-enabler |  |
| `S8.9` | **Feature Store** | **ABB** | Computes, stores and serves engineered features to training and inference with point-in-time correctness. | `3.7.1` required-enabler |  |
| `S8.10` | **Prompt Registry & Versioning** | **ABB** | Manage prompts as controlled, reviewable, versioned artifacts. | `4.3.2` required-enabler |  |
| `S8.11` | **Dataset & Corpus Management** | **ABB** | Version, snapshot and govern the datasets models and evaluations use. | `3.3.5` required-enabler, `3.5.1` required-enabler |  |
| `S8.12` | **Data Labeling & Annotation** | **ABB** | Produce and quality-check labels, human or machine generated. | `3.3.4` required-enabler |  |
| `S8.13` | **Data Pipeline & Transformation** | **ABB** | Move and reshape data into the form AI workloads require. | `3.3.2` required-enabler, `3.2.1` required-enabler |  |
| `S8.14` | **Metadata, Catalog & Lineage** | **ABB** | Record what data exists, what it means and where it went. | `3.4.1` required-enabler, `3.4.3` required-enabler, `3.4.2` required-enabler |  |
| `S8.15` | **Evaluation Harness & Benchmarking** | **SVC** | Run repeatable evaluations against defined criteria and test sets. | `4.6.2` required-enabler, `4.6.3` required-enabler | *either* |
| `S8.16` | **Edge & On-Device Inference** | **SVC** | Packages and executes models on local or embedded hardware with intermittent or no connection to a central service. | `5.4.5` required-enabler, `6.1.2` required-enabler |  |
| `S8.17` | **Sovereign & Isolated Deployment** | **ABB** | Run AI wholly within a defined jurisdiction or disconnected boundary. | `3.1.5` required-enabler, `5.4.4` required-enabler | ⚑ regulatory |
| `S8.18` | **Model & Artifact Integrity Verification** | **SVC** | Signs, attests and verifies model weights, containers and dependencies at registration and again at load. | `7.4.2` required-enabler, `4.2.5` operational-support |  |
| `S8.19` | **Subject Data Location & Purge** | **SVC** | Locates a data subject's records across indexes, embeddings, caches and derived artifacts and removes them verifiably. | `7.5.3` required-enabler, `3.1.4` required-enabler | ⚑ regulatory |
| `S8.20` | **Isolated Workspace & Network Provisioning** | **ABB** | Provisions tenant-isolated workspaces with private connectivity and enforced data-segregation boundaries. | `5.3.2` required-enabler, `5.3.3` required-enabler, `5.3.4` required-enabler |  |
| `S8.21` | **Model Documentation Generation** | **SVC** | Produces and publishes model and system documentation from registry, evaluation and lineage metadata. | `4.2.4` required-enabler, `7.2.2` evidence-provider |  |
| `S8.22` | **Permitted-Use & Consent Metadata** | **ABB** | Records licensing terms, permitted-use scope and consent basis as machine-checkable metadata enforced at access time. | `3.2.2` required-enabler, `3.2.4` required-enabler | ⚑ regulatory |
| `S8.23` | **Architecture Repository & Decision Records** | **ABB** | Stores capabilities, building blocks, patterns, solutions and dated architecture decisions with their relationships. | `4.1.3` required-enabler, `4.1.6` required-enabler |  |
| `S8.24` | **Conformance Test Harness** | **SVC** | Executes declared conformance tests against a solution and records pass/fail as reusable evidence. | `4.1.7` evidence-provider, `4.6.3` operational-support | *either* |

### S9 · Observability, Operations & Cost

*See what AI systems did, prove it afterwards, and know what it cost.*

Group provenance: OpenTelemetry GenAI semantic conventions (Development status, semconv-genai repo, v1.42.0) · IBM Model Monitoring · AWS Bedrock observability and cost-optimization categories · Microsoft Foundry Control Plane · Databricks Data Quality Monitoring · GAO AI Accountability Framework

| ID | Entry | Kind | Definition | Typed edges | Flags |
|---|---|---|---|---|---|
| `S9.1` | **Trace Instrumentation & Context Propagation** | **ABB** | Emits spans and propagates correlation context across model, retrieval, tool, agent and workflow calls. | `6.2.1` operational-support, `6.2.2` operational-support | ⬥ agentic *either* |
| `S9.2` | **Interaction & Prompt Logging** | **ABB** | Persists prompt, context, output and decision records to a retention-managed store, with configurable field-level redaction. | `6.2.2` operational-support, `7.8.2` evidence-provider | ⚑ regulatory |
| `S9.3` | **Agent Action & Tool-Call Auditing** | **ABB** | Emits and stores a structured record of each agent action - tool invoked, arguments, result, actor - queryable after the fact. | `6.2.3` operational-support, `7.8.2` evidence-provider | ⬥ agentic |
| `S9.4` | **Token & Consumption Metering** | **ABB** | Counts tokens, accelerator-seconds and storage per call and tags each measurement with consumer, model and workload. | `6.5.1` operational-support |  |
| `S9.5` | **Cost Attribution & Showback** | **ABB** | Attribute AI consumption to an accountable owner and budget. | `6.5.1` operational-support, `6.5.3` operational-support |  |
| `S9.6` | **Production Evaluation & Online Scoring** | **SVC** | Evaluate live output quality continuously, not only pre-release. | `6.3.1` evidence-provider, `4.6.3` operational-support | *either* |
| `S9.7` | **Drift Detection** | **SVC** | Detect divergence of inputs or relationships from training conditions. | `6.3.2` evidence-provider |  |
| `S9.8` | **Bias & Fairness Monitoring** | **SVC** | Monitor outcome disparities across affected groups over time. | `6.3.3` evidence-provider, `7.2.1` evidence-provider | ⚑ regulatory |
| `S9.9` | **Feedback Capture** | **ABB** | Captures explicit and implicit user corrections and downstream outcomes, and writes them to a labeled store for reuse. | `6.3.4` evidence-provider, `2.3.3` operational-support |  |
| `S9.10` | **Alerting & Service Level Management** | **ABB** | Evaluates telemetry streams against configured thresholds and routes notifications to on-call recipients and dashboards. | `6.2.4` operational-support, `6.1.4` operational-support |  |
| `S9.11` | **Fleet & Agent Inventory Telemetry** | **ABB** | Know what agents and AI systems are actually running, right now. | `7.7.4` required-enabler, `7.7.5` evidence-provider | ⬥ agentic |
| `S9.12` | **Immutable Audit Trail** | **ABB** | Retain tamper-evident evidence an auditor can rely on. | `7.8.2` evidence-provider, `7.8.1` evidence-provider | ⚑ regulatory |
| `S9.13` | **Energy & Emissions Metering** | **ABB** | Attributes energy consumption and estimated emissions to workloads, models and consumers alongside cost. | `7.2.5` evidence-provider, `6.5.1` operational-support |  |
| `S9.14` | **Telemetry Collection Pipeline** | **ABB** | Receives, batches, transforms and routes telemetry, applying sampling and redaction policy in transit. | `6.2.1` operational-support |  |
| `S9.15` | **Protected Telemetry & Evidence Store** | **ABB** | Retains telemetry and assessment evidence under access control, retention policy and tamper-evidence. | `7.8.2` evidence-provider, `6.2.2` operational-support | ⚑ regulatory |

### S10 · Standards & Protocol Profiles

*Open specifications the building blocks conform to. A standard is not a building block; ABBs reference a pinned profile of one.*

Group provenance: Model Context Protocol specification · A2A specification · OpenTelemetry GenAI semantic conventions · C2PA specification · IETF OAuth 2.0

| ID | Entry | Kind | Definition | Typed edges | Flags |
|---|---|---|---|---|---|
| `S10.1` | **MCP Enterprise Client Profile** | **STD** | Pinned profile of the Model Context Protocol: revision, transports, primitives in use and deprecation dates carried. | — |  |
| `S10.2` | **A2A Interoperability Profile** | **STD** | Pinned profile of the Agent-to-Agent protocol: Agent Card fields, task states, bindings and signature verification. | — |  |
| `S10.3` | **GenAI Telemetry Convention Profile** | **STD** | Pinned commit of the GenAI semantic conventions, with per-convention stability recorded. | — |  |
| `S10.4` | **Content Provenance Profile** | **STD** | Pinned C2PA profile covering assertions, digital source types and validation. | — |  |
| `S10.5` | **Delegated Authorization Profile** | **STD** | Pinned OAuth 2.0 / OIDC profile for on-behalf-of exchange, audience restriction and least privilege. | — |  |

---

## 8. Matrix A — subject × catalog group

The join between the two models. **The blanks are the finding, and they come in three kinds.** Some capabilities are realized by existing non-AI enterprise services (ENT). Others are purely organizational and no technology realizes them (HUM). A blank that is neither would be a genuine gap.

| Capability | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | Σ | Blank reason |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **D1 · AI Strategy & Value Management** | | | | | | | | | | | | |
| `1.1` AI Vision & Strategy Definition |  |  |  |  |  |  |  |  |  |  |  | **HUM** — organizational capability |
| `1.2` AI Portfolio & Investment Management |  |  |  |  |  |  |  |  |  |  |  | **ENT** — Enterprise portfolio and investment management |
| `1.3` Value Realization & Performance Reporting |  |  |  |  |  |  |  |  |  |  |  | **ENT** — Benefits realization and performance reporting tooling |
| `1.4` AI Sourcing & Partner Strategy |  |  |  |  |  |  |  |  |  |  |  | **ENT** — Procurement and vendor management systems |
| `1.5` AI Ecosystem & Alliance Management |  |  |  |  |  |  |  |  |  |  |  | **UNEXPLAINED — review** |
| **D2 · AI Demand & Solution Shaping** | | | | | | | | | | | | |
| `2.1` Use Case Discovery & Intake |  |  |  |  |  |  |  |  |  |  |  | **ENT** — Demand management / ITSM intake |
| `2.2` AI Use-Case Feasibility & Qualification |  |  |  |  |  |  |  |  |  |  |  | **HUM** — organizational capability |
| `2.3` AI Product Management |  |  |  |  |  |  |  |  |  |  |  | control / evidence support only — the ability itself is organizational |
| `2.4` Business Process & Service Redesign | 1 |  |  | 1 | 1 |  |  |  |  |  | 3 |  |
| `2.5` Human-AI Interaction & Oversight Design |  | 2 |  |  | 1 |  |  |  |  |  | 3 |  |
| `2.6` AI Innovation & Incubation |  |  |  |  |  |  |  |  |  |  |  | **UNEXPLAINED — review** |
| **D3 · Data & Knowledge Management** | | | | | | | | | | | | |
| `3.1` Data Governance & Stewardship for AI | 1 |  |  |  | 1 |  |  | 2 |  |  | 4 |  |
| `3.2` Data Sourcing, Licensing & Provenance |  | 1 |  |  |  |  |  | 2 |  |  | 3 |  |
| `3.3` Data Quality & Preparation for AI |  |  |  |  |  |  |  | 3 |  |  | 3 |  |
| `3.4` Metadata, Lineage & Cataloging for AI |  |  | 1 |  |  |  |  | 1 |  |  | 2 |  |
| `3.5` Knowledge Corpus & Content Management | 10 |  | 2 |  |  |  |  | 1 |  |  | 13 |  |
| `3.6` Knowledge Access & Retrieval |  |  | 12 |  |  |  | 1 |  |  |  | 13 |  |
| `3.7` Derived Representation Management |  |  | 2 |  |  |  |  | 1 |  |  | 3 |  |
| **D4 · AI Solution Engineering** | | | | | | | | | | | | |
| `4.1` AI Architecture Management & Solution Governance |  |  |  |  |  |  |  | 1 |  |  | 1 |  |
| `4.2` Model Selection, Customization & Tuning |  |  |  |  |  |  |  | 7 |  |  | 7 |  |
| `4.3` Prompt & Context Engineering |  | 2 |  |  | 1 |  |  | 1 |  |  | 4 |  |
| `4.4` Agent & Workflow Orchestration Design |  |  | 1 | 1 | 12 |  |  |  |  |  | 14 |  |
| `4.5` Integration & Tool Enablement |  | 1 |  |  | 2 | 6 |  |  |  |  | 9 |  |
| `4.6` AI Evaluation & Testing |  |  |  | 2 |  |  |  | 1 |  |  | 3 |  |
| `4.7` AI Release & Change Management |  |  |  |  |  |  |  |  |  |  |  | **ENT** — CI/CD pipeline and change management tooling |
| **D5 · AI Platform & Infrastructure** | | | | | | | | | | | | |
| `5.1` AI Platform Service Provisioning |  |  |  |  |  |  |  | 1 |  |  | 1 |  |
| `5.2` Model Access & Traffic Management |  |  |  |  |  | 5 |  | 1 |  |  | 6 |  |
| `5.3` AI Environment & Workspace Management |  |  |  |  |  |  |  | 1 |  |  | 1 |  |
| `5.4` AI Compute & Capacity Management |  |  |  |  |  |  |  | 3 |  |  | 3 |  |
| `5.5` Tool & Connector Catalog Management |  |  |  |  | 1 | 5 |  |  |  |  | 6 |  |
| `5.6` AI Developer Experience & Reuse Assets |  |  |  |  | 1 | 1 |  |  |  |  | 2 |  |
| **D6 · AI Operations & Reliability** | | | | | | | | | | | | |
| `6.1` AI Deployment & Serving Operations |  |  |  |  | 2 |  |  | 3 |  |  | 5 |  |
| `6.2` AI Monitoring & Observability |  |  |  | 1 |  |  |  |  |  |  | 1 |  |
| `6.3` Continuous Evaluation, Drift & Quality Management |  |  |  | 1 |  |  |  |  |  |  | 1 |  |
| `6.4` AI Incident & Problem Management |  |  |  |  |  |  |  |  |  |  |  | control / evidence support only — the ability itself is organizational |
| `6.5` AI Cost Management |  |  |  |  |  | 1 |  | 2 |  |  | 3 |  |
| `6.6` AI Asset Retirement & Evidence Preservation |  |  |  |  |  |  |  |  |  |  |  | **ENT** — CMDB and IT asset management |
| **D7 · AI Governance, Risk, Security & Assurance** | | | | | | | | | | | | |
| `7.1` AI Policy, Standards & Management System |  |  |  | 1 |  |  |  |  |  |  | 1 |  |
| `7.2` Responsible & Trustworthy AI Practice |  |  | 1 |  | 1 |  |  |  |  |  | 2 |  |
| `7.3` AI Risk Management |  |  |  |  |  |  |  |  |  |  |  | **ENT** — Enterprise GRC platform |
| `7.4` AI Security & Resilience |  |  |  |  | 1 |  |  | 1 |  |  | 2 |  |
| `7.5` Privacy & Data Protection for AI | 1 |  |  |  |  |  |  | 1 |  |  | 2 |  |
| `7.6` Legal, Regulatory & Contractual Compliance for AI |  |  |  |  |  |  |  |  |  |  |  | control / evidence support only — the ability itself is organizational |
| `7.7` AI System & Agent Inventory Management |  |  |  |  | 1 |  |  |  | 1 |  | 2 |  |
| `7.8` AI Assurance & Evidence Management |  |  |  |  |  |  |  |  |  |  |  | control / evidence support only — the ability itself is organizational |
| `7.9` AI Impact Assessment & Risk Classification |  |  |  |  |  |  |  |  |  |  |  | **ENT** — GRC assessment and workflow tooling |
| **D8 · AI People, Skills & Adoption** | | | | | | | | | | | | |
| `8.1` AI Operating Model & Decision Rights |  |  |  |  |  |  |  |  |  |  |  | **HUM** — organizational capability |
| `8.2` AI Skills & Specialist Capability Building |  |  |  |  |  |  |  |  |  |  |  | **ENT** — Learning management system |
| `8.3` AI Literacy & Awareness |  |  |  |  |  |  |  |  |  |  |  | **ENT** — Learning management system |
| `8.4` AI Adoption, Enablement & Support |  |  |  |  |  |  |  |  |  |  |  | **ENT** — Service desk and adoption analytics |
| `8.5` AI Change Management & Workforce Transition |  |  |  |  |  |  |  |  |  |  |  | **HUM** — organizational capability |
| `8.6` AI Community & Reuse Culture |  |  |  |  |  |  |  |  |  |  |  | **ENT** — Collaboration and knowledge platform |

Unexplained blanks: **1.5, 2.6**.

## 9. What backs the reference catalog

Assessed rather than asserted. The honest finding: **no standards body publishes a functional taxonomy of AI services.** ISO/IEC 42001, 5338, 23894 and the NIST AI RMF — the backbone of the capability model — contain none. Verified September 2026.

| Source | What it actually gives | Status | Backing | Caveat |
|---|---|---|---|---|
| Hugging Face task taxonomy | 47 named ML tasks across 6 modality groups (CV, NLP, audio, multimodal, tabular, RL) | Live, community-maintained | **strong** | De facto industry taxonomy. Not versioned or dated — cite as convention, not standard. |
| LF AI & Data Landscape | 13 technical categories with subcategories (Machine Learning, Deep Learning, Data, Model, Trusted & Responsible AI, Security & Privacy…) | Maintained YAML source, Linux Foundation | **strong** | The most formally maintained open technical classification of AI/ML tooling. |
| MCP specification 2026-07-28 | Primitives (Resources, Prompts, Tools, Elicitation), transports, official Registry v0.1 | Current; governed by the Agentic AI Foundation under the Linux Foundation | **strong** | Roots, Sampling and Logging deprecated in this release; protocol went stateless. Anything citing the 2025 spec is stale. |
| A2A specification 1.0.0 | Agent Card, Task lifecycle (7 states), Message, Part, Artifact; JSON-RPC / gRPC / REST bindings | Current; moved to AAIF August 2026 | **strong** | Transferred Google → Linux Foundation → AAIF. Now governed alongside MCP. |
| OWASP Top 10 for LLM Applications 2026 | LLM01–LLM10, v2.0 | Published ~March 2026 | **strong** | Materially different from the 2023 list — item names and ordering both changed. |
| OWASP Top 10 for Agentic Applications 2026 | ASI01–ASI10 (Goal Hijack, Tool Misuse, Identity & Privilege Abuse, Memory Poisoning, Rogue Agents…) | Published December 2025 | **strong** | The first enumerated agentic threat taxonomy from a recognised body. |
| C2PA specification 2.4 | Content Credentials, digital source types for AI output, data-mining assertions | Current | **strong** | Backs output provenance and training-data opt-out signalling. |
| IBM Generative AI Capability Model | 7 L1 categories decomposed to L2/L3 (Model Hub, Model Hosting, Agentic AI, GenAI Governance, Security Management…) | IBM Architecture Center, current Jan 2026 | **strong** | The strongest single vendor-published capability decomposition. Structurally vendor-neutral in its naming. |
| SAP AI-native North Star | 4 layers; named MCP Gateway, Agent Gateway, harness engineering, context engineering | Published June 2026 | **strong** | Freshest enterprise architecture naming concrete MCP/A2A gateway roles rather than gesturing at interoperability. |
| OpenTelemetry GenAI semantic conventions | Operation taxonomy: chat, embeddings, execute_tool, invoke_agent, invoke_workflow, create_agent, retrieval, plan | Development status — not stable; separate repo since June 2026 | partial | An operation taxonomy in all but name, and the closest thing to a neutral vocabulary for agent observability. Attribute names are still changing. |
| ISO/IEC 23053:2022 | ML task examples (regression, classification, clustering, anomaly detection, dimensionality reduction) + 6 pipeline stages | Current | partial | The task list is explicitly non-exhaustive and illustrative. Do not present it as a controlled taxonomy. |
| ISO/IEC 22989:2022 | Clause 9 “Fields of AI”: computer vision, NLP, data mining, planning, knowledge processing | Current | partial | Terminology entries in prose, not a normative classification table. |
| OECD Framework for the Classification of AI Systems | 5 dimensions; the Task & Output dimension names core application areas and autonomy levels | Published 2022, no revision found | partial | A policy classification tool, not an engineering catalog — but the most developed formal task dimension available. |
| Australia DTA technical standard for government use of AI | 8 lifecycle stages, 42 numbered compliance statements | Current, architecture.digital.gov.au | **strong** | The strongest public-sector precedent found. Lifecycle-shaped, directly adaptable. |
| Gartner AI TRiSM | Concept: continuous embedded governance across the lifecycle | Primary document June 2026, paywalled | weak | Pillar list is not stable across public sources — at least four different structures are attributed to it. Cite the functional intent, never a specific pillar list. |
| Agent identity standards | CSA Agent Identity Governance Framework v1; OpenID Foundation AI Identity CG; several individual IETF drafts | Pre-consensus | weak | No ratified standard exists. Microsoft Entra Agent ID is the most productised implementation, not a standard. Cite as emerging. |
| ISO/IEC 42001, 42005, 5338, 23894 | Management system, impact assessment, lifecycle processes, risk guidance | Current | **not a taxonomy** | Contain no functional or service taxonomy. They back the capability model's governance domains, not this layer. Confirmed by structure. |
| NIST AI RMF and AI 600-1 | Govern/Map/Measure/Manage; 12 GenAI risk categories | Current | **not a taxonomy** | Risk and harm taxonomies, not functional ones. No enumeration of AI system task types. |
| ISO/IEC TR 24030:2024 | 81 use cases across 18 application domains | 2nd edition, April 2024 | **not a taxonomy** | Taxonomises application domains and deployment models, not AI functions. A plausible-looking source that does not actually back a service catalog. |
| The Open Group | — | No AI reference model published | **not a taxonomy** | IT4IT 3.0 contains zero mentions of AI/ML/GenAI. The AI Initiatives page states intent with no deliverable. ArchiMate 4 shipped May 2026 — AI-specific elements unverified. |
| Papers with Code | — | Discontinued (2025) | **not a taxonomy** | No longer maintained. Do not cite as a current task ontology. |
| Banks and development banks | — | Nothing published | **not a taxonomy** | World Bank, IMF, JPMorgan, Capital One, DBS, ING: no reusable AI capability model or technical reference architecture found. Trade-press write-ups are not citable artifacts. |

### Currency corrections verified September 2026

| Area | What changed | Consequence |
|---|---|---|
| Microsoft | Azure AI Foundry → Microsoft Foundry. “Azure” dropped from the brand. “Azure AI services” → “Foundry Tools” — Vision, Speech, Language, Document Intelligence are all now Foundry Tools. | Any internal material still saying “Azure AI Studio” or “Azure AI services” is stale. New named components: Foundry IQ (managed knowledge layer), Foundry Control Plane (cross-agent observability and runtime control), Foundry Local (on-device). |
| Microsoft | Retired Foundry Tools: Anomaly Detector, Content Moderator, LUIS, Metrics Advisor, Personalizer, QnA Maker. | Superseded — Content Moderator by Content Safety. Do not put any of these in a target architecture. |
| Microsoft | Entra Agent ID is GA: agent identity blueprints, per-instance identities, human sponsors, lifecycle governance, native OAuth 2.0 / MCP / A2A support. | The most mature agent-identity implementation of the three hyperscalers. Directly realizes capability 7.4.4 and 7.7.2. |
| AWS | July 2026 retirement wave. Bedrock Agents (“Classic”), Amazon Kendra, Amazon Q Business and ~10 SageMaker AI features moved to maintenance mode. | Successors: Bedrock AgentCore, Bedrock Knowledge Bases, Amazon Quick Suite. SageMaker renamed SageMaker AI. |
| Google | Agentspace → Gemini Enterprise. Vertex AI Agent Builder absorbed into the Gemini Enterprise Agent Platform; docs now redirect. | Any taxonomy with “Vertex AI” as the top-level Google node is already out of date. New: Agent Registry, Agent Gateway, Skill Registry. |
| Protocols | MCP and A2A now share a governance home — the Agentic AI Foundation, a Linux Foundation body, 250+ members including AWS, Anthropic, Google, Microsoft, OpenAI. | This materially strengthens the case for building on MCP/A2A rather than a proprietary integration pattern. It is no longer single-vendor. |
| Protocols | MCP went stateless in the 2026-07-28 revision. Roots, Sampling and Logging deprecated with a 12-month offramp; legacy HTTP+SSE transport deprecated. | Anything built against the 2025 spec needs a migration plan inside 12 months. |

## 10. Obligations register — held outside the model, owned by Legal

Statutory references were **removed from capability provenance** and are held here. Nothing in this model asserts that any regulation binds the institution. Capability `7.6.5` is the prerequisite legal determination — a legal opinion that either exists or does not, not a maturity dimension.

Two cautions on the entries below, both material:

- **Articles 49, 72 and 73 are provider obligations.** On every use case contemplated here the institution would be a *deployer*. Capability `7.6.6` (Regulatory Role Determination) is the control that establishes which.
- **Article 49 is not authority for an internal asset inventory.** It governs registration in the EU database. Capability `7.7` is defensible on management grounds alone and should be justified that way.

| Applies to | Name | Instrument | Subject |
|---|---|---|---|
| `7.6` | Legal, Regulatory & Contractual Compliance for AI | EU AI Act | Provider / deployer role determination (see 7.6.6) |
| `2.2` | Feasibility & Impact Assessment | EU AI Act | Fundamental rights impact assessment |
| `2.5` | Human-AI Interaction & Oversight Design | EU AI Act Art. 14 | Human oversight |
| `3.1` | Data Governance & Stewardship for AI | EU AI Act Art. 10 | Data and data governance |
| `3.2` | Data Sourcing, Licensing & Provenance | EU AI Act Art. 10 | Data and data governance |
| `3.3` | Data Quality & Preparation | EU AI Act Art. 10 | Data and data governance |
| `4.6` | Evaluation & Testing | EU AI Act Art. 15 | Accuracy, robustness, cybersecurity |
| `6.3` | Continuous Evaluation, Drift & Quality Management | EU AI Act Art. 72 | Post-market monitoring - PROVIDER obligation |
| `6.4` | AI Incident & Problem Management | EU AI Act Art. 73 | Serious incident reporting - PROVIDER obligation |
| `7.6` | Legal, Regulatory & Contractual Compliance | EU AI Act | General |
| `7.7` | AI System & Agent Inventory Management | EU AI Act Art. 49 | Registration - PROVIDER and public-authority deployer only |
| `8.3` | AI Literacy & Awareness | EU AI Act Art. 4 | AI literacy |
| `service:S1.12` | Face Detection & Recognition | EU AI Act Annex III (biometric identification) | — |
| `service:S5.10` | Human-in-the-Loop Interrupt & Approval | EU AI Act Art. 14 | — |
| `service:S7.10` | Output Provenance & Watermarking | EU AI Act Art. 50 | — |
| `service:S9.2` | Interaction & Prompt Logging | EU AI Act Art. 12 (logging) | — |
| `service:S9.6` | Production Evaluation & Online Scoring | EU AI Act Art. 72 (post-market monitoring) | — |
| `service:S9.11` | Fleet & Agent Inventory Telemetry | EU AI Act Art. 49 | — |

**Status of every row above: candidate — applicability not determined.**

## 11. Realization catalog — readiness, and why it is not maturity

The reference catalog above says what *could* exist. This register says what IDB provides today. Confusing the two is how "we approved the technology" becomes "we have the capability".

A service's **state** is a structural fact, not a rating — it depends on which objects exist and who operates the instances, so it can be read off by inspection.

| Readiness | Meaning | Evidence that establishes it |
|:-:|---|---|
| **0 · Not available** | No supported realization. | - |
| **1 · Available or project-proven** | The technology exists and can do it, or one team built it and it works. Not separable from their application, not reusable. | The application, or the vendor capability |
| **2 · Approved** | Cleared for enterprise use. Each team assembles the solution itself. | The approval record |
| **3 · Standardized** | A published standard and an architecture pattern or reference architecture exist. | The standard - the pattern document |
| **4 · Industrialized** | Reusable building blocks: IaC, security baseline, observability, CI/CD, implementation guidance, support model. Teams self-serve a compliant instance and operate it. | The module or template repository - a team that used it |
| **5 · Productized** | An exposed endpoint with a contract. Consumers call it; the platform operates it. | The endpoint - its service levels - its operational owner - its consumers |

Two questions decide every row: **is there a reusable solution building block, separable from any one application?** (2 vs 3), and **who operates the instances?** (3 vs 4).

### Realizations

One row per capability x pattern x technology. A technology appears on as many rows as it realizes patterns — that is correct, and a two-tier model cannot express it.

| ID | Capability | Pattern | Technology | Readiness | Consumption | Status |
|---|---|---|---|:-:|---|---|
| `REAL-001` | `5.1` | Internal Foundry deployment standard + agent build standard | Microsoft Foundry | **4** Industrialized | Building blocks | Approved |
| `REAL-101` *(illustrative)* | `3.6` | S3.16 Hybrid Retrieval Pattern | Azure AI Search | — | — | — |
| `REAL-102` *(illustrative)* | `3.6` | S3.2 Vector Similarity Search | Azure AI Search | — | — | — |
| `REAL-103` *(illustrative)* | `3.6` | S3.2 Vector Similarity Search | PostgreSQL + pgvector | — | — | — |
| `REAL-104` *(illustrative)* | `3.6` | S3.10 Access-Trimmed Retrieval | — | **0** Not available | — | Not available |

- **`REAL-001`** — Readiness 4 is arguably the correct TARGET here, not a way-station: agents are per-use-case by nature. The improvement path is enriching what comes in the box, not moving to 5.
- **`REAL-101`** — ILLUSTRATIVE - confirm before use.
- **`REAL-102`** — ILLUSTRATIVE - confirm before use.
- **`REAL-103`** — ILLUSTRATIVE - confirm before use.
- **`REAL-104`** — THE ROW THAT MATTERS. Nothing enforces entitlements at query time. This is why capability 3.6 can sit at maturity 2 while its headline realization sits at readiness 4. Rows at readiness 0 are the roadmap, and they are the reason the two scales stay separate.

### Consumption model

What the consuming team still has to build. Recorded on the realization, not the capability. **This is the column that settles the recurring argument** — *"a capability means I don't have to build it"* — without redefining the word capability. That belief is about consumption model; record it as one and the argument stops being definitional.

| Model | Meaning |
|---|---|
| **Guidance** | EA tells you how to build it. |
| **Building blocks** | Reusable modules and components are provided. |
| **Reference implementation** | A working implementation exists and can be adapted. |
| **Managed platform** | The platform provides the underlying infrastructure; the consumer configures on top. |
| **Service / API** | The consumer calls it and gets a result. |

### Enablement evidence

Generic assets — standard, pattern document, reference architecture, IaC, CI/CD, security baseline, observability, runbook, support model — mostly tick together and carry little information once a realization reaches readiness 4. **The pattern-specific controls are the ones that stay unticked, and the reason to read the list at all.** An inherited control that cannot be skipped is stronger evidence than a procurement approval.

**REAL-001**

| Control | Reference block | Capability | Why it matters |
|---|---|---|---|
| Distinct workload identity per instance, not a shared service principal | `S6.9` | `7.4.4` | A shared service principal makes every agent's actions indistinguishable. Nothing downstream can attribute or revoke. |
| Automatic registration in the AI system / agent inventory | `S6.6` | `7.7.2` | An inventory that depends on teams remembering to register is not an inventory. |
| Tracing and tool-call logging enabled by default | `S9.1` | `6.2.2` | If it is not on by default it will not be there when you need to explain what an agent did. |
| Content filtering and safety controls on by default | `S7.1` | `7.4.6` | Opt-in safety is the control that is missing exactly when it is needed. |
| Prompt-injection defence configured | `S7.4` | `7.4.3` | Content the agent reads can instruct it. Prompt design alone does not stop this at run time. |
| Evaluation harness scaffolded in the template | `S8.15` | `4.6.3` | Without a harness in the template, evaluation happens once at launch and never again. |
| Cost attribution tags applied automatically | `S9.4` | `6.5.1` | Untagged consumption cannot be attributed, forecast or stopped. |
| A tested way to stop it and revoke its access | `S7.13` | `6.4.2` | An untested kill switch is an assumption, not a control. |
| Credential issuance and rotation handled by the platform | `S6.9` | `5.2.4` | Credentials created by hand are credentials nobody rotates. |
| Network isolation and private connectivity baseline | `S8.20` | `5.3.3` | Isolation applied per team is isolation applied inconsistently. |
| A hook for human approval of consequential actions | `S5.10` | `2.5.2` | Oversight designed into the platform is exercised; oversight written into policy is not. |
| Interaction log retention configured to policy | `S9.2` | `3.1.4` | Interaction logs are evidence. Retention set per project is evidence you cannot rely on. |

**REAL-101**

| Control | Reference block | Capability | Why it matters |
|---|---|---|---|
| Entitlement enforced at query time, before ranking | `S3.10` | `3.6.2` | Filtering a ranked list after the fact both leaks and distorts relevance. The filter must precede ranking. |
| Citations resolvable to source, version and location | `S3.12` | `3.6.5` | A citation that cannot be opened is decoration. It also does not prove the statement is true. |
| Retrieval quality measured against a benchmark | `S8.15` | `3.6.3` | Relevance that is never measured degrades silently as the corpus changes. |
| Re-embedding runbook for model change | `S3.8` | `3.7.3` | Changing the embedding model invalidates the index. Without a runbook this is an outage. |
| Index residency and access controls enforced | `S3.8` | `3.1.5` | A vector index is a copy of the source content, and inherits its residency obligations. |

**REAL-103**

| Control | Reference block | Capability | Why it matters |
|---|---|---|---|
| Entitlement enforced at query time, before ranking | `S3.10` | `3.6.2` | Filtering a ranked list after the fact both leaks and distorts relevance. The filter must precede ranking. |
| Citations resolvable to source, version and location | `S3.12` | `3.6.5` | A citation that cannot be opened is decoration. It also does not prove the statement is true. |
| Retrieval quality measured against a benchmark | `S8.15` | `3.6.3` | Relevance that is never measured degrades silently as the corpus changes. |
| Re-embedding runbook for model change | `S3.8` | `3.7.3` | Changing the embedding model invalidates the index. Without a runbook this is an outage. |
| Index residency and access controls enforced | `S3.8` | `3.1.5` | A vector index is a copy of the source content, and inherits its residency obligations. |

The workbook carries 76 further candidate realizations generated from the reference catalog, each awaiting a readiness level. That list is the survey: mark the ones that matter, leave the rest. **An unmarked row is an unanswered question, not a zero.**

## 12. Open items

| # | Item | Note |
|---|---|---|
| 1 | Matrix A — subject × catalog | **Done** — section 8. |
| 2 | Matrix B — service × product | The product mapping against the actual Azure estate. Not started. |
| 3 | Lifecycle value stream | ISO/IEC 5338 stages cross-mapped to L2 capabilities. Not started. |
| 4 | Control mapping | ISO 42001 Annex A and NIST AI RMF functions mapped onto capabilities. Not started. |
| 5 | Anchor points | Where these capabilities specialize the existing enterprise business capability model. Deferred — model built greenfield. |
| 6 | L2 boundary review | D7 at 8 L2s, and the D2/D4 split, are the two decisions most likely to be challenged in review. |

---

*Generated from the same source data as the published capability register. Edit the source, not this file.*

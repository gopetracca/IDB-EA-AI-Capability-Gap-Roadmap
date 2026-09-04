# Our AI capability model and the Gartner model

**How the two relate, and why ours carries more technical capability**

Inter-American Development Bank · Enterprise Architecture
Version 1.0 · 4 September 2026

> **Internal use only.** The Gartner capability model referenced here (Tier 1 and Tier 2,
> June 2026) is subscription-licensed. It may be used inside the Bank under our own
> subscription. Its capability names and descriptions must not be reproduced in material that
> circulates to vendors, partners or the public. Nothing from it has been carried into the IDB
> model's source list — every source cited in our model is one a reviewer can open.

---

## 1. The short answer

The two models are not competitors and they are not versions of each other. They answer different
questions for different rooms.

| | Gartner model | IDB model |
|---|---|---|
| Built for | The board conversation — *is our AI programme sound?* | The delivery and assurance conversation — *can we run this system, and prove it?* |
| Shape | 7 Tier-1 × 25 Tier-2 | 8 domains × 52 capabilities × 258 criteria |
| Tier-2 written as | Verb phrases — *Deploy, operate and scale AI* | Noun capabilities — *AI Deployment & Serving Operations* |
| Depth in technology | 5 of 25 (8 counting the data block) | 26 of 52 (D3-D6) |
| Depth in governance and control | 3 of 25 | 9 of 52 |
| Answers "who owns this?" | Not reliably | By design — one accountable owner per capability |
| Answers "what is the evidence?" | Not addressed | The whole point of the third level |

**Their 25 sit almost exactly between our 8 domains and our 52 capabilities.** That is a useful
property, not a conflict: it means Gartner's model works as an *intermediate reporting lens* over
ours. If a Board member has seen the Gartner picture, we can report our assessment in their frame
without changing a single rating.

---

## 2. The crosswalk

Every one of Gartner's 25 Tier-2 capabilities has a home in our model. The mapping is not
one-to-one in either direction — theirs are broader, ours are more numerous.

### Gartner Tier-1 → our domains

| Gartner Tier 1 | Our domain |
|---|---|
| AI strategy | D1 AI Strategy & Value Management |
| AI value | D1, and D2 AI Demand & Solution Shaping |
| AI organization | D8 AI People, Skills & Adoption, and D1 (sourcing, ecosystem) |
| AI people and culture | D8 |
| AI governance | D7 AI Governance, Risk, Security & Assurance |
| AI engineering | D4 AI Solution Engineering, D5 AI Platform & Infrastructure, D6 AI Operations & Reliability |
| AI data | D3 Data & Knowledge Management |

### Gartner Tier-2 → our capabilities

| Gartner Tier 2 capability | Maps to | Notes |
|---|---|---|
| Monitor and interpret AI trends | 1.1 (via 1.1.5 Horizon Scanning & Technology Foresight) | We hold it one level lower |
| Develop and rationalize the AI vision | 1.1 AI Vision & Strategy Definition | Direct |
| Develop and refine the AI strategy | 1.1 | Direct |
| Develop and coordinate the AI roadmap | 1.2 AI Portfolio & Investment Management | Roadmap sits with sequencing for us |
| Promote AI-driven innovation | **2.6 AI Innovation & Incubation** | **Added because of this comparison** |
| Manage the AI use-case portfolio | 1.2 + 2.1 Use Case Discovery & Intake | We split the funnel from the portfolio |
| Manage AI value propositions | 1.3 Value Realization & Performance Reporting | Direct |
| Develop the AI product portfolio | 2.3 AI Product Management | Direct |
| Develop external AI partnerships | **1.5 AI Ecosystem & Alliance Management** | **Added because of this comparison** |
| Manage the AI ecosystem | **1.5** | **Added because of this comparison** |
| Evolve the internal operating model | 8.1 AI Operating Model & Decision Rights | Direct |
| Manage AI-related change and culture | 8.5 + 8.6 | We separate transition from community |
| Evolve AI-related roles and staffing | 8.2 + 8.1 | |
| Deliver AI training and literacy | 8.3 + 8.4 | We separate literacy from ongoing support |
| Evolve AI policies and controls | 7.1 + 7.2 | Their single box is our management system plus responsible-AI practice |
| Develop AI governance teams and roles | 8.1 + 7.1 | |
| Monitor AI and enforce policies | 7.8 + 7.3 | |
| Design and architect AI | 4.1 AI Architecture Management & Solution Governance | Direct |
| Develop, test and integrate AI | 4.2 + 4.3 + 4.5 + 4.6, and 3.6 + 3.7 for the "ground and contextualize" part | **Four to six of ours in one of theirs** |
| Deploy, operate and scale AI | 4.7 + 5.4 + 6.1 + 6.2 + 6.3, and 7.4 for the security part | **Six of ours in one of theirs** |
| Manage AI platform and infrastructure | 5.1 + 5.2 + 5.3 + 5.5 + 5.6 | **Five of ours in one of theirs** |
| Manage AI engineering | 8.2 + 8.1 | Staffing and coordination, not engineering itself |
| Acquire and prepare AI data | 3.2 + 3.3 + 3.5 | |
| Manage and govern AI data | 3.1 + 3.4 | |
| Analyze AI data | — | Analytics and BI; deliberately outside our AI scope |

### What we carry that their model does not

Twenty-one of our fifty-two capabilities have no counterpart in the Gartner model. They fall into
three groups.

**Governance, risk and assurance depth (7 capabilities)** — 7.3 AI Risk Management ·
7.4 AI Security & Resilience · 7.5 Privacy & Data Protection for AI · 7.6 Legal, Regulatory &
Contractual Compliance for AI · 7.7 AI System & Agent Inventory Management · 7.8 AI Assurance &
Evidence Management · 7.9 AI Impact Assessment & Risk Classification. Gartner compresses all of
this into three governance verbs.

**The generative and agentic layer (7 capabilities)** — 3.5 Knowledge Corpus & Content
Management · 3.6 Knowledge Access & Retrieval · 3.7 Derived Representation Management ·
4.3 Prompt & Context Engineering · 4.4 Agent & Workflow Orchestration Design · 5.2 Model Access &
Traffic Management · 5.5 Tool & Connector Catalog Management. None of these existed as capabilities
in any pre-2023 model, and Gartner's data block is still shaped around acquire / govern / analyze.

**Delivery and operations discipline (7 capabilities)** — 1.4 AI Sourcing & Partner Strategy ·
2.2 AI Use-Case Feasibility & Qualification · 2.4 Business Process & Service Redesign ·
2.5 Human-AI Interaction & Oversight Design · 6.4 AI Incident & Problem Management ·
6.5 AI Cost Management · 6.6 AI Asset Retirement & Evidence Preservation.

One inconsistency worth knowing about: **FinOps appears on Gartner's own AI roadmap slide but not
in their capability model.** We hold it as 6.5.

### What their model prompted us to add

The comparison was not one-way. Two capabilities were added to our model as a direct result:

- **1.5 AI Ecosystem & Alliance Management.** Our 1.4 was procurement-shaped throughout —
  build/buy/partner, vendor evaluation, contract clauses, exit risk. It had nowhere to put academic
  collaborations, multilateral cooperation or peer-institution exchange, none of which are supplier
  relationships. For a development bank that was a real hole.
- **2.6 AI Innovation & Incubation.** Experimentation existed only as an L3 under community culture,
  with no owner and nothing to assess.

---

## 3. Why our model carries more technical capability

This is the question that will be asked, usually as *"isn't 52 too many?"* or *"Gartner manages
with 25 — why do we need more?"* Eight answers, in the order they tend to land.

### 3.1 A capability you cannot assign is a heading, not a capability

Our first design rule is that every capability has **one accountable owner**. Test Gartner's
*Deploy, operate and scale AI* against it. In our model that single box spans release management
(4.7), capacity (5.4), serving operations (6.1), monitoring (6.2), continuous evaluation (6.3) and
security (7.4) — six different owners in six different reporting lines.

Ask one person to accept accountability for that box and they will decline, correctly. Ask six
people and nobody is accountable. The box cannot be rated, cannot be owned, and cannot be funded.

### 3.2 At their resolution, every honest answer is "partially"

A gap analysis has to produce sentences someone can act on. At Gartner's granularity, our answer to
*"how mature is Deploy, operate and scale AI?"* is "partially" — because we are genuinely strong at
some of it and absent at other parts of it. That is not a finding; it is a shrug.

At our granularity the same reality reads: *"Foundry is industrialised and approved for general
use, but access-trimmed retrieval has never been standardised, and there is no inventory of
deployed agents."* Three sentences, three owners, three roadmap items.

### 3.3 The incidents live in the technical capabilities

Every plausible AI failure at the Bank is technical in origin, and each one lands on a capability
that Gartner's model does not have:

| What goes wrong | Lands on |
|---|---|
| A retrieval answer includes a document the asker was not cleared to see | 3.6 Knowledge Access & Retrieval |
| An agent takes an action nobody authorised | 4.4 + 2.5 + 7.7 |
| A prompt-injected document changes what a system does | 7.4 + 4.3 |
| A model version changes and output quality silently degrades | 6.3 + 4.7 |
| Nobody can say how many AI systems are running in production | 7.7 AI System & Agent Inventory Management |
| We cannot show an auditor the evidence behind a claim | 7.8 AI Assurance & Evidence Management |

A model with no capability for the thing that fails cannot produce a roadmap that prevents it.

### 3.4 Generative and agentic AI created capabilities that older models do not contain

Gartner's *Develop, test and integrate AI* description passes over grounding and contextualisation
in a subordinate clause. At the Bank, "grounding" is not a verb inside a bullet. It is a **corpus**
that somebody curates and retires, an **index** with a refresh cadence, an **access-trimming rule**
that has to be enforced before ranking rather than after, an **embedding lifecycle** that has to be
re-run when the model changes, and an **evaluation harness** that proves it still returns the right
document. Those are five different jobs with at least three different owners.

The same holds for agents. Their data block — acquire and prepare, manage and govern, analyze — is
a pre-generative shape. It has no place for a knowledge corpus, for retrieval, or for derived
representations, because when that shape was set those things were not enterprise capabilities.

### 3.5 Without a capability name, architecture questions become procurement questions

If the model has no *Knowledge Access & Retrieval*, the conversation is "should we buy Azure AI
Search?" — and the answer is a purchase order. With the capability named, Azure AI Search becomes
**one realization of it**, and the question becomes the right one: does what we have deliver
access-trimmed retrieval to the standard we need, and what else could?

This is exactly the vendor neutrality we are required to hold. It is not achievable at 25
capabilities, because at that resolution the product *is* the capability.

### 3.6 The second and third lines need something to attach to

Cybersecurity attaches controls to 7.4. Legal attaches obligations to 7.6. Data Governance attaches
stewardship to 3.1 and licensing to 3.2. Privacy attaches DPIAs to 7.5. Internal Audit attaches
evidence to 7.8. Each of them needs a named, owned capability to point at.

Gartner offers them *Evolve AI policies and controls* and *Monitor AI and enforce policies*. Two
boxes for five functions, with no evidence hooks. That model cannot survive an audit because it was
never built to; ours has to.

### 3.7 The technical layer is the only part that moves this year

Strategy and culture capabilities move on a five-to-ten-year clock. Platform readiness moves
quarterly. A roadmap assembled only from strategy capabilities has nothing to deliver in the first
two quarters, which is precisely when it has to show progress.

### 3.8 The good news only exists at the technical layer

The Bank's own brief was to show what is already approved for general use — *"so that we see we are
not that bad."* That story cannot be told against a box called *Manage AI platform and
infrastructure*; it is too coarse to be either good news or bad. It can be told against
5.1 Platform Service Provisioning at readiness 4, 4.5 Integration & Tool Enablement at readiness 4,
and 3.6 Knowledge Access & Retrieval at readiness 4 — capability by capability, each with a named
thing behind it that someone can already use. Coverage is only countable, and only defensible, at
this resolution.

---

## 4. The objections, answered

**"Fifty-two is too many to assess."**
It is not the reporting tier. The **8 domains** are what leadership sees. The **52 capabilities**
are the working tier, where ownership and rating happen. The **258 criteria** are not reporting
units at all — they are the evidence questions behind a rating. And if an audience arrives already
familiar with the Gartner picture, we can report our ratings through their 25 without re-rating
anything.

**"This is over-engineering."**
The cost of too much resolution is a longer assessment. The cost of too little is a roadmap that
cannot be sequenced, a gap analysis nobody can own, and a governance domain that fails its first
audit. Those are not symmetric risks.

**"Gartner is the industry standard — why deviate?"**
We have not deviated; we have gone deeper in the two places where a development bank cannot afford
their compression. Their model is excellent for what it is for, and we should keep using it for
that: it is the right shape for a board slide and a useful outside check on our own completeness —
it is how we found the two capabilities we were missing. It is not built to sequence delivery or to
survive Internal Audit.

**"Are we sure the extra capabilities are real?"**
Every one of them carries named sources a reviewer can open, and a separate provenance register now
records the edition, date, access route and evidence grade of each. Where a capability is our own
synthesis rather than something a published model names — which is true of most of the agentic and
retrieval layer, because nothing published names them yet — it says so explicitly rather than
borrowing authority it does not have.

---

## 5. How to use both

| Situation | Use |
|---|---|
| Board or senior leadership briefing | The 8 domains, or Gartner's 25 as the lens if that is the frame they know |
| Assigning accountability | The 52 capabilities. Nothing coarser works |
| Building the roadmap | The 52, sequenced by the enabler dependencies between them |
| Cyber, Legal, Data Governance, Privacy, Internal Audit | D7's nine capabilities plus D3's seven, with evidence |
| Checking our own completeness | Gartner's model, and the other external models in the source register — as a challenge, not a source |
| Anything that leaves the Bank | Our model only. Gartner material stays internal |

---

## 6. What is still open

Three things a reviewer will find if they look, so they are better heard from us:

- **The capability taxonomy is out for validation.** 1.5 and 2.6 are new and carry low confidence
  until that comes back.
- **Provenance is pinned at source level, not clause level.** The register records edition, date and
  access for all 40 sources; 19 of 147 capability-to-source citations still have no locus, and
  eleven sources are paywalled or members-only.
- **D7 is not yet control-mapped.** ISO/IEC 42001 Annex A and NIST AI RMF outcomes are not mapped to
  our governance capabilities. That domain should be carved out of any approval request until they
  are.

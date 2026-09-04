# Where maturity and readiness come from

**The options surveyed, the decision taken, and how it is implemented**

Inter-American Development Bank · Enterprise Architecture
Version 2.0 · 4 September 2026 · supersedes v1.0 of the same date

**Status:** supporting record for **D1 · Two scales, never merged**
(`decisions/meta-model-decisions.md`). D1 states the rule. This states what was available to
adopt, what we adopted, what we built, and where a reviewer will push.

> **Internal use only.** §2.4 and §3.4 quote from non-public material — a World Bank slide marked
> *Official Use Only*, and subscription-licensed analyst content. Neither may be reproduced in a
> deliverable that leaves the Bank. Strip those subsections before any external circulation.

---

## 1. The short answer

**Maturity was adopted. Readiness was built.** That asymmetry is real, and stating it is a
stronger position than concealing it.

| | Maturity 1–5 | Readiness 0–5 |
|---|---|---|
| Options available | Several, all converging on the same CMMI shape | **None that measure what we needed** |
| What we did | Adopted the shape, added the gate and the states | Constructed it |
| Derivation type (D10) | **Adopted** | **Synthesized** |
| Attaches to | A **capability** (L2) | A **realization** (capability × pattern × technology) |
| Owner · clock | Capability owner · 5–10 years | Platform · quarterly |
| Defensible as | An instance of a very well-established scale | Our own construction, stated as such |

D10 supplies the reason to prefer the honest label: *assembled by us is a stronger position with
Internal Audit than a citation that does not resolve.*

---

## 2. Maturity — the options

### 2.1 What was available

All the credible candidates converge on the same five-stage CMMI arc. The choice was never
*which shape*; it was *which instrument to name*.

| Option | What it is | Grade | Why not adopted wholesale |
|---|---|---|---|
| **S29 MITRE AI Maturity Model** | 6 pillars, 20 dimensions, 5 levels — *Initial / Adopted / Defined / Managed / Optimized* | **B** | Pre-dates the generative-AI wave (its own register caution). Sound as a scale reference, not as current AI guidance |
| **S12 AWS CAF-AI** | 6 perspectives + adoption playbook | **C** | **Flagged "for historical reference only" by AWS.** Our most-used vendor capability source; must be cited as a February 2024 artifact |
| **S30 MIT CISR** briefing | 4 stages — *Experiment and Prepare → Become AI Future Ready* | **B** | Research briefing, not an assessment instrument. No evidence gates |
| **S01 ISO/IEC 42001** | AI management system | **C** | **Carries no scale at all** — conformance, not maturity. Paywalled |
| **S08 NIST AI RMF** | GOVERN / MAP / MEASURE / MANAGE | **A** | Outcomes, not levels. Not a maturity instrument |
| CMMI itself | The origin | — | Generic; no AI content. Would need the whole AI layer built anyway |

**The finding:** maturity was a solved problem. Five stages, *Initial → Optimizing*, is the
industry consensus and nobody disputes it.

### 2.2 What we adopted

The **shape** — 1–5, evidence-gated, ordinal — with the lineage stated:
SEI Capability Maturity Model → CMMI → effectively every capability maturity instrument since.

### 2.3 What we added

Two things, and both are ours:

**The gate.** Most published maturity models describe levels narratively and leave the rater to
judge. Ours is mechanical:

> The rating is the highest level for which every applicable mandatory criterion at that level
> **and all lower levels** is met by valid evidence.

No averaging, no partial credit. This is what makes 258 L3 criteria load-bearing rather than
decorative, and it is why `CLAUDE.md` forbids averaging an ordinal score.

**The states 0 / NE / UC / NA.** Most models lack these, and an assessment that cannot distinguish
*absent* from *not evidenced* from *not applicable* will silently score an unassessed capability
as 1. `NE` exists to prevent exactly that.

### 2.4 Peer comparator — the World Bank slide

> **Source.** World Bank Group · Information and Technology Solutions (ITS), deck footer
> *"ITS | AI Readiness of WB Data"*, slide 10, **Official Use Only**. A shared slide, not a
> publication. **Evidence grade D** — non-public, no edition, no date, no retrievable URL.
> Not in the source register; cannot support any claim that leaves the Bank.

**It is a maturity model, despite the filing.** `notes/Readiness levels.md` filed it as
*"readiness levels - World Bank"*. The slide is titled **"Maturity Model"** and its levels are
1 Initial · 2 Emerging · 3 Consolidating · 4 Integrating · 5 Optimizing — CMMI, essentially
unmodified. The word *readiness* in the deck title names the **subject** (the AI-readiness of the
data estate), not a readiness scale. The note has been corrected.

Its lower band carries four **"Dimensions of AI-Ready Data Culture"** — **People · Process ·
Technology · Data**. Their provenance is unremarkable: People-Process-Technology is the oldest
partition in IT management (Leavitt's 1965 organizational diamond, by way of ITIL's four
dimensions and every transformation framework since), with **Data** added as a fourth and stated
as dependent on the other three. The slide claims nothing more, and nothing more should be read in.

**Why we did not adopt the four dimensions:**

| | World Bank slide | Our model |
|---|---|---|
| Scope | The **data estate**'s AI-readiness | The **whole AI capability surface**, 8 domains |
| Structure | 4 dimensions × 5 levels | 52 capabilities × 5 levels, plus readiness on realizations |
| Assessment unit | A dimension — *"People"* | A capability — *4.4 Agent & Workflow Orchestration Design* |
| Ownership | Not assignable — nobody owns "Process" | One accountable owner per capability, by design |
| Evidence | Narrative level descriptions | 258 L3 criteria, gated |

**The decisive objection is ownership.** Rating *"People: 3"* produces a number no individual can
be asked to move — the same argument made against coarse tiers in
`notes/Capability-Model-Comparison-and-Rationale.md` §3.1: *a capability you cannot assign is a
heading, not a capability.*

**What it is good for.** Two things, both real:

- **Corroboration of the maturity shape.** An independent MDB landing on the same five-stage arc.
  Grade D, so modest — but it corroborates the borrowed half, which was never in dispute.
- **A reporting lens held in reserve.** If a World Bank counterpart or an MDB forum arrives with
  this frame, we report into it without re-rating anything:

  | WB dimension | Our primary home |
  |---|---|
  | People | **D8** (8.1–8.6) |
  | Process | **D2** and **D7** |
  | Technology | **D4 · D5 · D6** |
  | Data | **D3** (3.1–3.7) |

  A presentation device, not a structural claim.

---

## 3. Readiness — the options

### 3.1 What was available

Nothing that measures what we needed. This is the substantive finding of the whole document, and
it survived a deliberate search of the source register.

| Option | What it measures | Why it does not fit |
|---|---|---|
| **NASA TRL** (1974; ISO 16290:2013) | How proven a **technology** is in its operating environment | A property of the technology, not of our packaging of it. See §3.2 |
| **S21 TOGAF G193** capability-based planning | — | Separates a capability from its realizing building blocks, then **assigns no scale to either**. The ontology without the measurement |
| **S23 IT4IT 3.0.1** · **S24 ITIL 4** | Service capability vs service offering | Right instinct, wrong shape: IT-service-shaped, not AI-shaped. ITIL 4 is grade C and partly superseded — ITIL 5 announced January 2026 |
| Vendor "platform readiness" checklists | Supply only | Marketing instruments. No institutional dimension |
| **The World Bank slide** | Maturity (§2.4) | Not a readiness scale at all, despite how it was filed |

**Nothing in our possession carries a supply-side scale.** Not "nothing published" — nothing at all.

### 3.2 Why TRL is a relative, not a parent

TRL is the nearest thing and the one a reviewer will reach for, so the distinction has to be exact.

TRL measures how proven a technology is in its environment — component in the lab, prototype in
relevant environment, flight-proven. Ours measures **how well the enterprise has packaged
something for internal reuse.** The gap is visible level by level:

| Level | The question it asks | TRL equivalent? |
|---|---|---|
| 0–1 | Does it exist / has anyone made it work? | Roughly, yes |
| 2 Approved | Has our governance cleared it? | **No** |
| 3 Standardized | Is there a published standard and a pattern? | **No** |
| 4 Industrialized | Is there a reusable block separable from any one application? | **No** |
| 5 Productized | **Who operates the instances?** | **No** |

Levels 2 through 5 are enterprise-architecture supply questions. TRL has no concept of them,
because TRL was never asking about an institution.

### 3.3 What we built

A 0–5 structural scale, read off by inspection rather than assessed. From D2, **two questions
settle every row**:

1. **Is there a reusable building block separable from any one application?** → settles 2 vs 3–4
2. **Who operates the instances?** → settles 4 vs 5

A scale two questions can settle is one a reviewer applies without training. That was the design
goal, and it is the argument for building rather than bending TRL to a purpose it was not built for.

### 3.4 Why it had to be built now

Before generative AI, supply and capability tracked each other closely enough that one number
mostly worked. **Foundry is why they stopped.**

A platform can be genuinely well-packaged — **REAL-001, readiness 4**: Terraform modules, security
baseline, CI/CD, a team self-serves a compliant instance — while the institution has **no standard
for how an agent's stopping conditions are designed** (`4.4`, maturity 2). That combination is now
common, and it is invisible to any model carrying one number.

---

## 4. The decision

**Two scales. Never merged.** Three independent reasons, in ascending order of how hard they are
to argue with.

### 4.1 Different owners, different clocks

| | Maturity | Readiness |
|---|---|---|
| Asks | Can the institution *do* this, to what standard, with what evidence? | Has the enterprise *packaged* this well enough to consume? |
| Owner | The accountable capability owner | The platform |
| Clock | 5–10 years | Quarterly |

A single number has to pick an owner and a refresh cycle. Whichever it picks, the other
conversation loses its instrument.

### 4.2 The collapse fails in a predictable direction

It is never symmetric. **Supply masquerades as capability**, not the reverse.

> *"Semantic retrieval: 4, via Azure AI Search."*

True about supply — and it has silently answered a question nobody asked. Nobody ever accidentally
reports maturity when they meant readiness: supply is the number that is easy to establish and
pleasant to report. This is why D1 ends **both numbers or neither**.

### 4.3 They do not attach to the same object

The structural reason, and the one that ends the argument.

Maturity attaches to a **capability**. Readiness attaches to a **realization** — the triple
*capability × pattern × technology*. One capability carries several: `REAL-101` and `REAL-102` are
both `cap: 3.6`, different patterns, independent readiness values.

One number per capability has **nowhere to put that**. A single scale is not merely less
informative — it is not well-formed against the object model (D4, D5).

---

## 5. How it is implemented

Where each decision above actually lives, so a reviewer can check it rather than take it on trust.

| Decision | Implementation | Where |
|---|---|---|
| Maturity on the capability | Sheet 1 col. K (now) and L (target); validation `1,2,3,4,5,0,NE,UC,NA` | `build/build_wb.py` |
| Readiness on the realization | Sheet 2 col. H, per realization record | `model/realization.json` |
| Never write readiness into the capability catalog | Sheet 1 col. M is a **formula**, locked, pulling the best readiness from sheet 2 | `SUMPRODUCT(MAX(...))`, sheet 1 |
| The gap is the finding | Sheet 1 col. N — *"Gap: why maturity trails"* — free text, required where M > K | Sheet 1 |
| Readiness backed by evidence, not assertion | Sheet 2 col. I *"Evidence-implied"* — a formula deriving the level from the enablement assets actually recorded on sheet 3 | Sheet 2 |
| The gate, not an average | Rubric sheet: level × criterion × mandatory/conditional/enhancing, plus **caps maturity** | Sheet 11 |
| What supply does not provide | `notprov` on each realization record | `model/realization.json` |
| Consumption model is recorded, not argued | Field on the realization (D3) | `model/realization.json` |
| Illustrative vs confirmed | `conf: true/false` — **1 of 5 realizations is confirmed** | `model/realization.json` |

**Two implementation facts worth knowing before quoting any number:**

- Column M is **locked and formula-driven** precisely so nobody can type a readiness value into
  the capability catalog. The D1 rule is enforced by the workbook, not by discipline.
- Readiness is **cross-checked**: sheet 2 carries both the asserted level (col. H) and an
  *evidence-implied* level derived from the enablement assets on sheet 3 (col. I). A divergence
  between them is a claim the assets do not support — the readiness-side equivalent of the
  maturity gate.
- **The gate cannot yet be evaluated mechanically.** The 258 L3 criteria are not typed
  mandatory / conditional / enhancing, and one rubric of 52 exists. Until then maturity is
  expert judgement using the L3s as a checklist, and **every rating is provisional and must be
  labelled so.**

---

## 6. The objections, answered

**"This isn't a standard. You made up half of it."**
Half is accurate, and it is the half we say is ours. Maturity is CMMI-lineage and cited. Readiness
is our construction, recorded as Synthesized under D10, defined by two questions any reviewer can
apply. The alternative was to cite TRL for a scale that measures something TRL does not measure —
the exact failure mode D10 exists to prevent.

**"Why not just use MITRE's maturity model and stop?"**
We use its scale shape. It carries no readiness dimension, and its own register entry notes it
pre-dates the generative-AI wave. It cannot express *the platform is industrialized and the
institution still cannot design an agent* — our most common real finding.

**"Isn't readiness just TRL?"**
No. TRL asks how proven a technology is in its environment; readiness asks how well **we** have
packaged it for **our** reuse. Levels 2 through 5 have no TRL equivalent (§3.2).

**"Two numbers is twice the assessment work."**
No. Readiness is read off by inspection — two questions, structural, no evidence gathering. The
cost sits almost entirely in maturity, which a one-scale model would have required anyway.

**"The gap between the numbers looks like an inconsistency."**
It is the finding, and the reason both numbers exist. Sheet 1 column N exists to make someone
write down *why* maturity trails readiness; `notprov` records the same thing on the supply side.

**"The World Bank uses four dimensions — why don't we?"**
Different scope and a different assessment unit (§2.4). Theirs assesses the data estate; ours
assesses the AI capability surface. Their dimensions are not assignable to an owner. We can report
*into* their four whenever it is useful, without re-rating anything.

---

## 7. Where a reviewer will push, and what we owe

Stated plainly so it is not discovered.

- **Readiness has thinner grounding than the taxonomy.** Every L2 carries named sources; the
  readiness scale carries none. This is where a challenge starts, and the word **"Custom"** in
  `notes/Readiness levels.md` is where they will point. The answer is §3.1 — the search was done
  and there was nothing to adopt — plus §3.3, the two-question test.

- **Settled by inspection, not by preference.** An earlier draft offered a choice: defend
  readiness as synthesized, or obtain the World Bank scale's documentation and cite it.
  **That second option does not exist** — the slide is a maturity model. We defend readiness as
  synthesized-by-design, which is what D10 prescribes regardless.

- **Do not let the analyst crosswalk carry this.** `notes/Interesting stuff.md` shows five of
  seven Tier-1 rows mapping cleanly to our domains. That is genuine evidence the **partition** is
  not idiosyncratic. It says nothing about the two-scale decision. One piece of evidence, two
  different claims — keep them apart.

- **Maturity's own sources are ageing.** S29 pre-dates generative AI; S12 is flagged historical by
  its own publisher; S24 is partly superseded. Not fatal — the scale shape is disputed nowhere —
  but a deliverable leaning on them as *current AI guidance* rather than as *maturity-scale
  precedent* overstates them.

- **The gate is not yet mechanical.** L3 typing and 51 rubrics are outstanding (§5). Anyone
  quoting a maturity rating today is quoting a provisional number.

---

## See also

- `decisions/meta-model-decisions.md` — **D1** (the rule), **D2** (the readiness levels),
  **D5** (two registers), **D10** (evidence grades and derivation types)
- `notes/Readiness levels.md` — the level table, the evidence that establishes each, and the
  corrected World Bank filing
- `notes/Como-funciona-el-modelo-explicado.md` — §1, §6 and §7: the same argument for a
  non-specialist audience, with the worked example
- `notes/Capability-Model-Comparison-and-Rationale.md` — §3.1, the ownership argument against
  coarse assessment units
- `build/prov_data.py` — the verified source register: S01, S08, S12, S21, S23, S24, S29, S30

---
id: ADR-0012
alias: D11-candidate
title: How to record who owns a capability
status: Proposed
date: 2026-09-04
decision_owner: Gabriel Petracca (EA)
recommended_option: B — typed contribution columns
depends_on: [ADR-0004, ADR-0006]
---

# ADR-0012 · How to record who owns a capability

> **Status: PROPOSED — not decided.** Raised 4 September 2026.
> Decision owner: Gabriel Petracca (EA).
> Recommended option: **B — typed contribution columns**.
>
> Previously `notes/OPEN-capability-ownership-model.md`. Moved into the ADR sequence because it is
> a decision awaiting a call, not a note.

---

## The problem

The capability model records exactly one `Owner` per capability. After mapping all 52 against the
Bank's own product and enabler catalogue, the AI enabler carries 14 and Enterprise Architecture
carries 2 — which reads as though EA contributes almost nothing.

That is not what happens. EA writes the reference architectures, the standards, the ABB/SBB
definitions and the Terraform module specifications that the AI enabler and the platform teams
build against. The model has no place to record that, so it disappears.

Stated neutrally, without reference to any team: **one column can only answer one question, and the
question it currently answers is "who runs it".** At least three distinct accountabilities exist per
capability — who answers for the outcome, who sets the standard the solution must satisfy, and who
builds and operates it.

## Why it matters

1. The owner view is currently read as a contribution view, and it is not one.
2. The concentration finding (14 of 52 on one enabler) may be an artefact of the column, not a fact
   about the Bank.
3. The operating-model conversation on sheet 3 of the taxonomy workbook cannot be had properly
   while "owner" conflates standard-setting with operation.

## Options

### A — Leave it as is
One owner, meaning the accountable party. EA's contribution is recorded only through the enterprise
asset register (20 assets: 7 standards, 5 reference architectures, 2 templates, 6 IaC modules).

*For:* nothing to build, no extension to defend, single-accountability stays unambiguous.
*Against:* the asset register is not connected to the capability rows, so nobody reading the map
sees it. The concentration finding stays misleading.

### B — Typed contribution columns  *(recommended)*
Keep **Accountable** as exactly one, and add **Sets the standard** and **Delivers & operates**.
Record as a sparse list — (capability, unit, contribution type) — and generate the matrix as a view
rather than materialising 52 x 16 = 832 cells.

Deliberately excluded: a "consulted" or "consumed by" column. Those get sprayed across every row,
are then ignored, and corrode trust in the whole artefact.

*For:* answers the real question, makes EA's role visible as a fact rather than a claim, and turns
sheet 3 into a usable operating-model discussion.
*Against:* it is an extension — see the precedent section. Needs discipline to stay honest.

### C — BIZBOK capability instances
Instead of typing the relationship, instantiate the capability per business unit: one "Knowledge
Access & Retrieval" capability with several implementations, one per unit that performs it.

*For:* it is what BIZBOK actually prescribes, so no extension to defend.
*Against:* multiplies the model across 52 capabilities and 16 units, which makes the heat map
unreadable and the assessment unusable — and it still does not say *how* each unit contributes, it
only produces more rows.

**Record C as a considered rejection, not an oversight.** Someone will ask.

## What the frameworks actually do

Checked 4 September 2026. The split has two halves and they are not equally defensible.

**The single-accountable half is squarely standard and quotable.**
COBIT 2019: *"Accountable (A) roles carry overall accountability. As a principle, accountability
cannot be shared."* — ISACA, *COBIT 2019 Framework: Governance and Management Objectives*, 2018.
Paywalled (ISACA members / purchase). Note ISACA has said an update to COBIT is planned, so this
citation may age.

**Several units against one capability is also standard.**
- TOGAF Series Guide **G211**, *Business Capabilities, Version 2*, April 2022: *"multiple business
  entities may share the delivery of a particular business capability."* Openly readable at
  pubs.opengroup.org. (Supersedes G189. **G190 is Information Mapping** — not this.)
- TOGAF Series Guide **G206**, *Organization Mapping*, April 2022 — describes a many-to-many mapping
  between organisation units and capabilities. Open.
- **BIZBOK** organisation cross-mapping — *Business Architecture Metamodel Guide V3.0*, Business
  Architecture Guild, September 2024, section 5.4.1. The Metamodel Guide is open; BIZBOK itself
  (v15, April 2026) is members-only.
- **DoDAF CV-5**, *Capability to Organizational Development Mapping* — DoDAF 2.02 Change 1. Open.
  Note DoDAF 2.02 dates from 2010 and has had no substantive revision since; describe it as
  "current release, unchanged since 2010" rather than actively maintained.

**Typing the contribution is where we would be extending.**
No capability-modelling framework provides a vocabulary for *sets the standard* vs *operates* vs
*consumes*.
- ArchiMate collapses them on purpose: the Assignment relationship is defined as *"the allocation of
  responsibility, performance of behavior, storage, or execution."* — The Open Group, *ArchiMate 3.2
  Specification* (C221), section 5. Open at pubs.opengroup.org. Its strategy-layer chapter defines
  no capability-owner relationship at all.
- BIZBOK's cross-mapping, G206 and CV-5 are all untyped.
- ArchiMate section 15, *Language Customization Mechanisms*, explicitly sanctions specialising
  relationships and adding attributes — so the extension is within the standard's own rules.

**But typed multi-party contribution is well established in the governance literature.**
- **Bain RAPID** — Recommend / Agree / Perform / Input / Decide. "Agree" is a veto held by a
  standard-setter, a near-exact analogue of the proposed column. Rogers & Blenko, *"Who Has the D?"*,
  Harvard Business Review, January 2006 (R0601D). HBR paywalled; free summary on bain.com.
- **IIA Three Lines Model** — first line operates, second line sets standards and monitors, third
  line assures, all against the same subject matter. Structurally identical to what is proposed.
  Cite the **Statement of Position, 8 July 2026** (five principles), not the superseded 2020 paper.
  Free.
- **NIST AI RMF GOVERN 2.1** requires roles and responsibilities to be *documented and clear*, but
  prescribes no taxonomy. **ISO/IEC 42001** clause 5.3 and Annex A.3 require roles and
  responsibilities to be assigned and communicated, but do not require R and A to be recorded
  separately. Both are requirements to do this at all, not prescriptions of shape.

*Not usable:* RASCI and DACI are real in practice but have no owning body and no canonical
definition — do not cite them as framework precedent. APQC PCF and IT4IT do not address ownership.
No citable Gartner or Forrester convention was found.

## The position statement, if B is chosen

> We apply COBIT 2019's single-accountability principle to the capability-to-organisation
> cross-mapping that BIZBOK, TOGAF G206/G211 and DoDAF CV-5 all recognise, and type the
> contributions in the manner of Bain's RAPID and the IIA Three Lines Model. ArchiMate section 15
> (Language Customization Mechanisms) sanctions this kind of specialisation.

Honest about which part is ours. **Do not write that any named framework prescribes a
standard-setter / operator split against a capability.** None does.

## Design cautions if B is chosen

1. **Enforce single-A in the builder**, as a validation rule — not as a convention in a guidance
   note. A-proliferation is the commonest way these matrices die: every unit that cares lobbies for
   an A and the principle erodes silently.
2. **Define the terms and give worked examples where they differ.** Accountable = answerable for the
   outcome, holds the standard, arbitrates disputes. Delivers = performs and operates. Without
   examples people collapse them back within a month — ArchiMate's own definition shows how natural
   that collapse is.
3. **Keep it sparse.** Most capabilities should touch three to five units, not sixteen. If more than
   a fifth of the grid is populated, nobody can read a row.
4. **Map to units by mandate, not by current name**, and hold one authoritative organisation list to
   join against. A reorg otherwise invalidates a large share of the mapping overnight.
5. **Require that the accountable party holds something** — budget, standard-setting authority, or
   escalation rights — and record which. Accountability without authority is a name on a page.

## The larger point, which stands regardless

The underlying complaint — *"they should be able to handle all the AI work, but we are the ones who
define the reference architectures and standards"* — is a **maturity finding**, not an ownership
problem. A capability whose accountable owner cannot discharge it without another team doing the
definitional work is not at a high maturity level, whatever the org chart says.

That is the stronger position, and it does not depend on this decision:
- Owner stays the accountable party.
- The maturity rating reflects that they cannot currently discharge it alone.
- Evidence points at the EA-authored asset that is carrying it.
- The roadmap item is: transfer from EA-dependent to owner-operated.

"We do a lot" is unverifiable and invites argument. "Here are N capabilities whose current maturity
depends on assets EA produced, with the evidence, and here is what it takes for the owner to stand
alone" is a finding nobody can dismiss.

**Consider adding a `dependency` flag independently of this decision:** *can the accountable owner
discharge this today without EA?* Yes / No / Partly. That column is the roadmap, and it needs no
extension to defend.

## Still pending on the merits, separate from this decision

Five owner assignments look wrong against EA's own entry in the product catalogue, which claims
*"Technology Strategy — defining how technology supports bank objectives and how technological
assets should be used. This includes defining guidelines for buy vs. build decisions, creating
long-term strategies (target architecture)"* and *"Software Architecture"*:

| Capability | Currently assigned | Should be |
|---|---|---|
| `1.4` AI Sourcing & Partner Strategy | Strategic Resource Management | EA sets build/buy guidance — the catalogue says so explicitly |
| `4.5` Integration & Tool Enablement | Core Platforms | EA sets the integration architecture |
| `4.7` AI Release & Change Management | Core Platforms | EA sets the architecture gates |
| `5.6` AI Developer Experience & Reuse Assets | Core Platforms | EA authors the templates and reference implementations |
| `7.1` AI Policy, Standards & Management System | Artificial Intelligence (partial) | EA co-owns the standards half |

These are corrections to make whether or not the column split happens.

## What is needed to decide

- Whether the extra columns are worth defending in review, or whether the maturity-finding route
  alone is enough.
- Whether the taxonomy reviewers would fill three owner columns or ignore two of them.
- Confirmation that the standard-setter column would carry Cybersecurity, Data Management and Cloud
  as well as EA. **If it only ever says EA, it is a credit column, not a model** — and once a
  reviewer notices that, the map loses its authority, including the parts that matter.

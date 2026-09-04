# Enterprise AI Capability Model — settled meta-model decisions

**Status:** adopted in v0.5 · 2 September 2026 · supersedes earlier drafts
**Scope:** how the model is structured. Not the content of the model itself.

These decisions exist because the standards do not settle them. TOGAF does not prescribe the
ordering of capability, pattern and building block — Pattern is not even a formal entity in the
content metamodel, and the text says patterns identify combinations of "ABBs *and/or* SBBs". No
amount of further reading resolves this. It is settled by decision and recorded here.

---

## D1 · Two scales, never merged

A **capability** carries **maturity**. A **realization** carries **readiness**.

| | Maturity | Readiness |
|---|---|---|
| Attaches to | An L2 capability | A realization (capability × pattern × technology) |
| Asks | Is the institution *able to do this*, to what standard, with what evidence? | Has the enterprise *packaged this well enough to consume*? |
| Scale | 1–5, evidence-gated, plus states 0 / NE / UC / NA | 0–5, structural, read off by inspection |
| Owner | The accountable capability owner | The platform |
| Clock | 5–10 years | Quarterly |

**The gap between them is the finding.** A capability can be readiness 4 and maturity 2 — the
product is well packaged and the institution still cannot do the thing to the standard it needs.
That combination is common and invisible to any model carrying only one number.

**Provenance of the two scales — maturity adopted, readiness synthesized — is recorded separately
in `decisions/two-scales-provenance.md`, together with the answer to "is this standard?"**

**Never write a readiness level into the capability catalog.** "Semantic retrieval: readiness 4
via Azure AI Search" is a true statement about supply that silently substitutes for the maturity
question. Both numbers or neither.

## D2 · Readiness levels

0 Not available · 1 Available or project-proven · 2 Approved · 3 Standardized ·
4 Industrialized · 5 Productized

Two questions settle every row: **is there a reusable building block separable from any one
application?** (2 vs 3–4) and **who operates the instances?** (4 vs 5).

Level 5 is not the target everywhere. Agent runtimes are per-use-case by nature; 4 is the correct
destination and the improvement path is enriching what comes in the box.

## D3 · Consumption model is a recorded fact, not a definition

Guidance · Building blocks · Reference implementation · Managed platform · Service/API.

Recorded on the realization, not the capability. This settles the recurring disagreement —
*"a capability means I don't have to build it"* — without redefining the word capability. That
belief is about consumption model. Record it as one and the argument stops being definitional.

## D4 · Objects

Capability → Pattern → ABB → SBB, plus **Service** for exposed consumable behavior. Technology
offering and deployed instance are fields on the SBB record, not model objects — TOGAF defines no
"product" concept, so this is a stated local convention.

Corrections carried in: an SBB **may be procured or developed** (TOGAF §33.2.4) — in-house
Terraform modules are an SBB. A **pattern is not a name**: TOGAF requires problem, context,
forces, solution, resulting context, rationale and known uses. A capability **may be an ability
not yet possessed** — ArchiMate covers "current *and desired*" abilities.

## D5 · Two registers, kept apart

**Reference catalog** — what could exist in the AI domain. Vendor-neutral, stable.
**Realization catalog** — what this institution actually provides. Specific, quarterly.

Confusing the two is how "we approved the technology" becomes "we have the capability".

## D6 · Single primary home, not mutual exclusivity

The eight domains are reporting clusters, not a sequential lifecycle and not proof of ontological
exclusivity. Every subject has exactly one `primary_domain` and may carry typed links to others.

## D7 · Repository anchoring is provisional

Every capability carries New / Specialization / Lens with a confidence. **Lens means do not create
a node** — keep the existing enterprise capability and attach an AI assessment profile. 14 of 50
are lenses; loading them as new nodes produces two change-management capabilities with two owners.

Unverified until the institution's existing capability map is crosswalked.

## D8 · Statutory references live outside the model

Held in a Legal-owned obligations register, all marked *candidate — applicability not determined*.
`7.6.6 Regulatory Role Determination` is the prerequisite. EU AI Act Articles 49, 72 and 73 are
**provider** obligations; on the use cases contemplated here the institution would be a deployer.

## D9 · The taxonomy is validated by the owner before anything is scored against it

Structure is settled separately from, and ahead of, assessment. A taxonomy-only workbook
(`AI-Capability-Taxonomy-for-review.xlsx` — domains, L2, L3, owner, anchor, sources, plus a
Decision column) goes to the capability owner first. Maturity, readiness, realizations and
evidence are withheld from it deliberately: a reviewer shown a score argues the score and stops
reading the structure.

**Change of 3 September 2026, from a comparison against an external analyst capability model:**

- **Added `1.5 AI Ecosystem & Alliance Management` (D1, 6 L3).** `1.4 AI Sourcing & Partner
  Strategy` was procurement-shaped throughout — build/buy/partner, vendor evaluation, contract
  clauses, concentration risk, supplier assurance. It had no home for academic collaborations,
  multilateral cooperation or peer-institution exchange, none of which are supplier
  relationships. `1.4` keeps per-supplier concentration and exit (`1.4.4`); `1.5` holds
  aggregate ecosystem dependency (`1.5.5`). That boundary is flagged for the owner to confirm.
- **Added `2.6 AI Innovation & Incubation` (D2, 5 L3).** Experimentation existed only as
  `8.6.4 Experimentation & Learning Culture` — an L3 under community culture, with no owner and
  nothing to assess. Innovation is an accountable capability: capture, sandbox, portfolio,
  transition to funded delivery, learning from controlled failure. Placement in D2 is a
  judgement (incubation feeds demand); D1 and D8 are defensible alternatives.
- **Removed `8.6.4`**, absorbed into `2.6.5`. `8.6` now carries 3 L3.

Model is now **8 domains / 52 L2 / 258 L3**.

**Licensing constraint on the comparison.** The analyst model that surfaced these two gaps is
subscription-licensed. It is usable internally under the institution's subscription and must not
be cited or paraphrased in deliverables that circulate externally. It is therefore **not** listed
in any capability's sources — every source in the model is one a reviewer can open. Any
Tier-1/Tier-2 crosswalk belongs in an internal-only sheet citing the document number alone.

## D10 · Provenance is graded by whether a reviewer can open it, not by prestige

Every source carries an **evidence grade**: **A** openly available, dated, versioned, from a
standards body or public authority · **B** openly available and dated but vendor-published or
non-normative · **C** available but undated, superseded, publisher-flagged historical, or
paywalled · **D** non-public, or not a publication at all. A grade-D source cannot support a
claim in anything that leaves the Bank, whatever its quality.

Each capability-source pair also carries a **derivation type** — Adopted, Adapted, Corroborating,
Synthesized, Institutional, Unsupported — and a **locus**, the specific part of the source relied
on. A capability whose locus is never pinned is reclassified **Synthesized** rather than left
claiming a source it cannot point into: assembled by us is a stronger position with Internal Audit
than a citation that does not resolve.

**Re-verification of 3 September 2026** normalised 50 citation strings into 40 canonical sources
and produced 18 findings. Four block publication:

- **EDM Council ADAC is not a publication.** It is a workgroup, absent from EDM Council's own
  Frameworks page. Cited four times. Remove; substitute CDMC if an open data-controls reference is
  needed.
- **TOGAF capability-based planning was removed from the current edition.** Chapter 28 of 9.2 was
  deliberately dropped in the 10th Edition. Re-cite as Series Guide **G193** (Capability-Based
  Planning), or **G211** (Business Capabilities, Version 2, April 2022, superseding G189) for
  business capabilities. **G190 is Information Mapping** — an earlier draft of this note had that
  number wrong.
- **Non-public sources cannot carry evidence.** Gartner (subscription) and unattributed
  "consultancy transformation patterns" together back four capabilities.
- **"Institutional practice" names no document.** Six uses. Each must become a named internal
  policy or standard with an owner and a date — Data Governance, Legal and Internal Audit each own
  one.

Also carried in: the IIA Three Lines Model 2020 paper was superseded on 8 July 2026 (five
principles, not six); ISO/IEC 27701:2019 clause references no longer resolve against the 2025
second edition; the correct NIST AI RMF locus form is `GOVERN 1.1`, not `GOVERN-1.1`; AWS flags
CAF-AI "for historical reference only"; the IMDA framework name is ambiguous across three
documents; MIT CISR is a research centre, not a citable artifact; and MCP revision 2026-07-28 is a
breaking change that invalidates architecture text written against 2025-11-25.

Standing rule: **cite by name, never by number**, for any list whose numbering changes between
editions (the OWASP Top 10 above all).

---

## Known open items

- **Rubrics** — one worked example exists; 51 remain. Until a capability has one, its rating is
  provisional and must be labelled so.
- **Criteria typing** — L3 criteria are not yet flagged mandatory / conditional / enhancing, so
  the maturity gates cannot be evaluated mechanically.
- **Control mapping** — ISO/IEC 42001 Annex A and NIST AI RMF outcomes are not mapped. **Carve D7
  out of any approval request until they are.**
- **Anchor crosswalk** — blocked on access to the existing enterprise capability map.
- **Provenance ledger** — the source register now pins edition, date, URL, access and evidence
  grade (D10). What remains is the **locus**: 147 capability-source pairs, of which 19 have no
  candidate at all and the rest carry an unverified one. Eleven sources are paywalled or
  members-only, so pinning them needs a licence holder.
- **Taxonomy validation** — the review workbook is with the capability owner; `1.5` and `2.6`
  carry confidence *low* until it comes back.

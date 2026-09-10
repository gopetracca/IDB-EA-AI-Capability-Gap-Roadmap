# What is settled

The rules that govern this model, in current vocabulary, each with the decision that
settles it. **This page is a digest, not a decision.** Where it and an ADR disagree, the
ADR wins; the binding records and their statuses are in
[`decisions/README.md`](decisions/README.md).

It exists so that *"is this settled, and by what?"* is one page rather than fourteen
files — three of which describe a model that no longer runs.

---

## The short version

| | |
|---|---|
| **Five rules that decide everything else** | Facts are separate from judgement · a level is never typed · `unknown` is never a zero · performance comes first · `out/` is generated |
| **Governing decision** | [ADR-0013](decisions/adr/0013-facts-and-scales.md), amended twice, itself amended by [ADR-0014](decisions/adr/0014-practised-is-observed-at-l3.md) |
| **Retired** | ADR-0001, ADR-0002, ADR-0003 — the two-scale model. Kept, unedited, with banners |
| **Not yet accepted** | ADR-0012 (ownership), Proposed |
| **Accepted but carrying a condition** | ADR-0007 — **carve out of any approval request** until a control mapping exists |

---

## 1 · The structure of the model

**The taxonomy has three levels, and only one of them is assessed.**
L1 domains cluster for reporting; L2 capabilities carry a level and an owner; L3 criteria
are the practices that can be witnessed. Criteria carry no level of their own.
→ [ADR-0006](decisions/adr/0006-single-primary-home.md), [ADR-0014](decisions/adr/0014-practised-is-observed-at-l3.md)

**A domain is a reporting cluster, not a lifecycle.**
It implies no sequence, no team and no process. Every capability has exactly one primary
home; a second plausible home is expressed as a typed link, not a second listing.
→ [ADR-0006](decisions/adr/0006-single-primary-home.md)

**A capability is vendor-neutral.**
If a line would have to be rewritten because a product changed, it is not a capability. What
a team can actually get is an **offering**, recorded separately.
→ [ADR-0004](decisions/adr/0004-objects.md), as amended by [ADR-0013](decisions/adr/0013-facts-and-scales.md)

**Every capability declares how it anchors to the Bank's existing map** — `specialization`,
`new` or `lens` — with a confidence. **`lens` means do not create a node**: keep the
existing enterprise capability and attach an AI assessment profile to it.
→ [ADR-0007](decisions/adr/0007-anchoring-is-provisional.md)

> ⚠ **The anchoring is provisional and unverified.** It rests on judgement, not on a
> crosswalk against the Bank's enterprise capability map, and 14 of 52 are lenses.
> ADR-0007 must be **carved out of any approval request** until ISO/IEC 42001 Annex A and
> NIST AI RMF outcomes are mapped. See [OPEN-ITEMS](../OPEN-ITEMS.md) #12–13.

**Structure is settled ahead of, and separately from, assessment.**
A reviewer shown a score argues the score and stops reading the structure. So the taxonomy
goes out for validation with no maturity, no levels and no evidence attached. New
capabilities carry `confidence: low` until their owner validates them.
→ [ADR-0009](decisions/adr/0009-taxonomy-validated-before-scoring.md)

**Statutory references live outside the model**, in a Legal-owned obligations register, all
marked *candidate — applicability not determined*. Architecture does not decide what law
applies.
→ [ADR-0008](decisions/adr/0008-statutory-references-outside-the-model.md)

**Who owns a capability is recorded against the Bank's own catalogue, and the ownership
*model* is not yet decided.** ADR-0012 is **Proposed**, and its own text argues the
dependency flag is the stronger route.
→ [ADR-0012](decisions/adr/0012-capability-ownership-model.md) — *awaiting a call*

---

## 2 · How the model measures

**Separate what is true from what we make of it.** This is the decision the whole model
rests on.

```
facts/    what is TRUE about the Bank, with evidence and a date   ← edited
scales/   rules that turn observations into a level                ← rarely edited
out/      views, one per scale, one per question, plus the report  ← generated
```

→ [ADR-0013](decisions/adr/0013-facts-and-scales.md)

**An observation is a fact, not a score.** *"The Foundry Agents Standard is pre-release"* is
true whichever framework reads it. That is what makes several scales possible over one body
of evidence without reassessing anything.
→ [ADR-0013](decisions/adr/0013-facts-and-scales.md) §1

**Four observations, five values.** `practised` · `enabled` · `skilled` · `defined`, each
`yes` / `partial` / `no` / `n/a` / `unknown`, each with evidence, an observer and a date.
→ [ADR-0013](decisions/adr/0013-facts-and-scales.md) §1

**`practised` is observed at L3 and derived at L2. Never typed.**
The other three stay at L2 — tooling, people and standards do not decompose per criterion
in a way a reviewer could answer. The roll-up is strict and asymmetric: `yes` only if every
criterion was examined and every one passed; **an unexamined criterion is never counted as
satisfied.** Under-claiming costs a follow-up question; over-claiming is the failure the
model exists to prevent.
→ [ADR-0014](decisions/adr/0014-practised-is-observed-at-l3.md)

**`defined` asks whether an approved institutional standard exists — not whether
Architecture wrote it.** The standard-setter is Cybersecurity for AI security, Data
Management for AI data governance, Legal for regulatory obligations, L&D for literacy, the
platform teams for their platforms. Architecture is the accountable owner of 2 of 52.
→ [ADR-0013 Amendment 1](decisions/adr/0013-facts-and-scales.md#amendment-1--4-september-2026)

**`no` is an evidenced negative; `unknown` means nobody has looked.**
An absence in a register that covers only platform assets is *not* a `no` — an enterprise
service may provide the tooling and nobody has asked. 24 `enabled` rows were corrected from
`no` to `unknown` on this basis on 4 September 2026, and `check` now enforces it.
→ [ADR-0013 Amendment 2](decisions/adr/0013-facts-and-scales.md#amendment-2--4-september-2026)

**A level is never typed. It is always derived**, by a rule in `scales/` that can be argued
with separately from the facts it reads. `check` fails if a derived value is found stored.
→ [ADR-0013](decisions/adr/0013-facts-and-scales.md) §2

**Performance comes first.** An approved standard with nothing performed against it earns
**no level at all**. That ordering is ISO/IEC 33020's, not ours, and it is what stops *"we
approved the technology"* from reading as *"we have the capability"*.
→ [ADR-0013](decisions/adr/0013-facts-and-scales.md) §3, [`../scales/README.md`](../scales/README.md)

**More than one scale may read the same facts, and one of them is the default.**
Lenses exist so a room that already holds a frame can be answered in it. **Where a lens and
the default disagree, the default is the finding.**
→ [ADR-0013](decisions/adr/0013-facts-and-scales.md) §2

**Not rated is a result, not a zero.** A scale must be able to return *not rated*, and the
views draw it in the palest tone rather than as 0.
→ [`../scales/README.md`](../scales/README.md), the scale contract

---

## 3 · How the model handles evidence

**Every source is graded by whether a reviewer can open it** — A open and normative, B open
but vendor or non-normative, C paywalled or superseded, D non-public or not a publication.
**A grade-D source cannot support a claim that leaves the Bank**, whatever its quality.
→ [ADR-0010](decisions/adr/0010-provenance-grading.md)

**Every citation carries a derivation type and a locus.** A capability whose locus is never
pinned is reclassified *Synthesized* rather than left claiming a source it cannot point
into. *Assembled by us* is a stronger position with Internal Audit than a citation that does
not resolve.
→ [ADR-0010](decisions/adr/0010-provenance-grading.md)

**Say which half is borrowed.** Where the model adopts, adapts or invents, it says so on the
face of the artifact. The default scale's `BASIS` states what is ISO/IEC 33020's and what is
ours.
→ [ADR-0010](decisions/adr/0010-provenance-grading.md), [ADR-0011](decisions/adr/0011-scale-provenance.md)

> ⚠ **Two things must not be written down.** ISO/IEC 33020:2019 is paywalled and its
> published preview stops before clause 5.3, so the **N-P-L-F percentage bands** and the
> **exact capability level rule** rest on secondary sources about the superseded ISO/IEC
> 15504. Cite the scale by name and levels by clause; **never quote the percentages**.
> → [`../scales/README.md`](../scales/README.md), [OPEN-ITEMS](../OPEN-ITEMS.md) #10

---

## 4 · What was decided, then reversed

Three decisions are superseded. They are kept **unedited, with banners**, because an ADR is
never rewritten to reverse itself — the record of what was believed and why is the point.

| Retired | It said | What replaced it | Why |
|---|---|---|---|
| [ADR-0001](decisions/adr/0001-two-scales-never-merged.md) | A capability carries **maturity**, a realization carries **readiness**, and the two are never merged | One derived level plus four visible columns | The distinction was real but could not be held in a room, and it needed 52 rubrics and 258 typed criteria that were never going to be written |
| [ADR-0002](decisions/adr/0002-readiness-levels.md) | Readiness 0–5, read off by inspection | The `enabled` observation | Supply now cannot produce a level on its own, which is the fact ADR-0001 was protecting — held structurally instead of by convention |
| [ADR-0003](decisions/adr/0003-consumption-model-is-recorded.md) | Consumption model scored on the realization | A recorded fact on the offering | It was never a judgement |

**The old model was right about one thing, and the new one keeps it.** ADR-0001 existed to
stop supply being reported as ability. ADR-0013 achieves the same end structurally:
`enabled` contributes nothing without `practised`.

> **Do not restart the rubric workstream.** It is the single most likely thing to be
> re-proposed by someone who read an old document. Criteria are the checklist behind a
> `practised` judgement, not gates. → [ADR-0013](decisions/adr/0013-facts-and-scales.md)

---

## 5 · What is not settled

| | What is open | Blocks |
|---|---|---|
| [ADR-0007](decisions/adr/0007-anchoring-is-provisional.md) | The crosswalk to the Bank's enterprise capability map does not exist. 14 of 52 are unverified lenses | **Approval.** Carve it out |
| [ADR-0012](decisions/adr/0012-capability-ownership-model.md) | **Proposed.** How to record contribution where more than one unit is involved | Nothing today; the owner mapping stands |
| [ADR-0009](decisions/adr/0009-taxonomy-validated-before-scoring.md) | Taxonomy validation is in flight; 10 capabilities carry `confidence: low` | Scoring those lines |
| Level 3 | Reads conformance from a standard and a practice co-existing. It does not evidence that the work **follows** the standard. A fifth observation would fix it | Nothing today; the reason line admits it |
| Levels 4–5 | Defined but not derivable — nothing collects threshold monitoring or a closed improvement cycle | Nothing. **Level 3 is the top of what is measured, not of the scale** |

The full list, with what would close each, is [`../OPEN-ITEMS.md`](../OPEN-ITEMS.md).

---

## 6 · Working rules that follow from all of this

These are not decisions in their own right; they are what the decisions above require in
practice. The enforcement is in `build/build.py check` and `tests/`.

| Rule | Enforced by |
|---|---|
| `facts/` is edited; `out/` is generated. Never fix a finding by editing a view | Convention, and `out/` is overwritten every build |
| Derived values are never stored — release counts, capability `practised`, levels | `check` fails |
| `yes` and `partial` require evidence; `no` requires evidence or a basis; `n/a` requires a reason | `check` fails |
| Every citation must resolve in the source register | `check` fails |
| Every scale must meet the contract, over all 625 observation combinations | `check` fails |
| No builder may name a scale or a question | A test fails |
| Sample data never reaches `facts/` | A test fails on the facts digest |
| No formulas in the workbook — every derived value is computed in Python and written as a value | By construction; there is no recalc step |
| An ADR is never edited to reverse itself | [`decisions/README.md`](decisions/README.md) |

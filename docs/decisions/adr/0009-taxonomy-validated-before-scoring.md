---
id: ADR-0009
alias: D9
title: The taxonomy is validated by the owner before anything is scored against it
status: Accepted
date: 2026-09-02
amended: 2026-09-03
depends_on: [ADR-0006]
---

# ADR-0009 · The taxonomy is validated before anything is scored against it

> **Alias `D9`.**

## Status

**Accepted** 2 September 2026 · **amended** 3 September 2026 (see Amendment 1).

## Decision

Structure is settled **separately from, and ahead of, assessment**.

A taxonomy-only workbook (`AI-Capability-Taxonomy-for-review.xlsx` — domains, L2, L3, owner,
anchor, sources, plus a Decision column) goes to the capability owner first.

Maturity, readiness, realizations and evidence are **withheld from it deliberately**: a reviewer
shown a score argues the score and stops reading the structure.

---

## Amendment 1 — 3 September 2026

From a comparison against an external analyst capability model. Evidence base:
`analysis/capability-model-comparison.md`.

- **Added `1.5 AI Ecosystem & Alliance Management` (D1, 6 L3).** `1.4 AI Sourcing & Partner
  Strategy` was procurement-shaped throughout — build/buy/partner, vendor evaluation, contract
  clauses, concentration risk, supplier assurance. It had no home for academic collaborations,
  multilateral cooperation or peer-institution exchange, none of which are supplier
  relationships. `1.4` keeps per-supplier concentration and exit (`1.4.4`); `1.5` holds aggregate
  ecosystem dependency (`1.5.5`). **That boundary is flagged for the owner to confirm.**
- **Added `2.6 AI Innovation & Incubation` (D2, 5 L3).** Experimentation existed only as
  `8.6.4 Experimentation & Learning Culture` — an L3 under community culture, with no owner and
  nothing to assess. Innovation is an accountable capability: capture, sandbox, portfolio,
  transition to funded delivery, learning from controlled failure. Placement in D2 is a
  judgement (incubation feeds demand); D1 and D8 are defensible alternatives.
- **Removed `8.6.4`**, absorbed into `2.6.5`. `8.6` now carries 3 L3.

Model is now **8 domains / 52 L2 / 258 L3**.

### Licensing constraint on the comparison

The analyst model that surfaced these two gaps is **subscription-licensed**. It is usable
internally under the institution's subscription and **must not be cited or paraphrased in
deliverables that circulate externally**. It is therefore **not** listed in any capability's
sources — every source in the model is one a reviewer can open. Any Tier-1/Tier-2 crosswalk
belongs in an internal-only sheet citing the document number alone.

## Open

`1.5` and `2.6` carry confidence **low** until the review workbook comes back from the capability
owner.

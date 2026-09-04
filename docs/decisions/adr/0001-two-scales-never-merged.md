---
id: ADR-0001
alias: D1
title: Two scales, never merged
status: Superseded
date: 2026-09-02
supersedes: []
superseded_by: [ADR-0013]
informs: [ADR-0002, ADR-0003, ADR-0011]
---

> ## ⚠ SUPERSEDED by [ADR-0013](0013-facts-and-scales.md) — 4 September 2026
>
> The two-scale model is replaced by four recorded observations and one derived level. ADR-0013 §4 states where this record was right (supply and ability are different questions; the collapse fails asymmetrically) and where it was wrong (that they must therefore be reported as two numbers).
>
> This record is kept unedited: an ADR is never rewritten to reverse itself. Read it as
> the account of what was believed on 2 September 2026 and why. For how the model works
> now, see [ADR-0013](0013-facts-and-scales.md) and [`../../how-it-works.md`](../../how-it-works.md).


# ADR-0001 · Two scales, never merged

> **Alias `D1`.** Referenced as D1 in `CLAUDE.md`, the build scripts and the review workbooks.
> Both identifiers name this record.

## Status

**Accepted** — adopted in v0.5, 2 September 2026. Supersedes earlier drafts.

## Context

The standards do not settle how ability and supply relate. A model carrying one number per
capability has to pick which question that number answers, and the choice is invisible to
everyone downstream of it.

## Decision

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

**Never write a readiness level into the capability catalog.** "Semantic retrieval: readiness 4
via Azure AI Search" is a true statement about supply that silently substitutes for the maturity
question. **Both numbers or neither.**

## Consequences

- Sheet 1 column N exists specifically to make someone write down *why* maturity trails readiness.
- `REAL-001`'s `notprov` field records the same idea on the supply side.
- Assessment cost sits almost entirely in maturity; readiness is read by inspection.

## Provenance

Maturity is **adopted** (CMMI lineage), readiness is **synthesized** (no parent). That asymmetry
is stated rather than left to be discovered — see **ADR-0011 · Provenance of the two scales**,
which also answers *"is this standard?"* and handles the World Bank comparator.

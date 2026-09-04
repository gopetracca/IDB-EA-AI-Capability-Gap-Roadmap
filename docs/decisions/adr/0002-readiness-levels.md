---
id: ADR-0002
alias: D2
title: Readiness levels
status: Superseded
date: 2026-09-02
supersedes: []
superseded_by: [ADR-0013]
informs: [ADR-0003]
depends_on: [ADR-0001]
---

> ## ⚠ SUPERSEDED by [ADR-0013](0013-facts-and-scales.md) — 4 September 2026
>
> Readiness is no longer a scale. It is the in-the-box checklist on an offering, counted. The two questions that settled every row survive as two items on that checklist.
>
> This record is kept unedited: an ADR is never rewritten to reverse itself. Read it as
> the account of what was believed on 2 September 2026 and why. For how the model works
> now, see [ADR-0013](0013-facts-and-scales.md) and [`../../how-it-works.md`](../../how-it-works.md).


# ADR-0002 · Readiness levels

> **Alias `D2`.**

## Status

**Accepted** — 2 September 2026.

## Decision

0 Not available · 1 Available or project-proven · 2 Approved · 3 Standardized ·
4 Industrialized · 5 Productized

Two questions settle every row:

1. **Is there a reusable building block separable from any one application?** → settles 2 vs 3–4
2. **Who operates the instances?** → settles 4 vs 5

A scale two questions can settle is a scale a reviewer can apply without training. That was the
design goal, and it is the argument for having built one rather than adapting TRL (ADR-0011 §3).

## Consequences

**Level 5 is not the target everywhere.** Agent runtimes are per-use-case by nature; 4 is the
correct destination and the improvement path is enriching what comes in the box.

## Where the levels live

Canonical definitions with evidence expectations: `model/realization.json` → `readiness[]`.

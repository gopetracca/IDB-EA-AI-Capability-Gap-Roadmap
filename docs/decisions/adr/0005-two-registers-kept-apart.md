---
id: ADR-0005
alias: D5
title: Two registers, kept apart
status: Accepted
date: 2026-09-02
depends_on: [ADR-0004]
---

> **Amended by [ADR-0013](0013-facts-and-scales.md) — 4 September 2026.** The decision
> stands: what *could* exist and what the Bank *does* provide are never confused. The
> realization catalog is replaced by the offerings register, `facts/offerings.json`; the
> reference catalog is frozen in `archive/reference-catalog/` and no longer maintained.

# ADR-0005 · Two registers, kept apart

> **Alias `D5`.**

## Status

**Accepted** — 2 September 2026.

## Decision

**Reference catalog** — what could exist in the AI domain. Vendor-neutral, stable.
**Realization catalog** — what this institution actually provides. Specific, quarterly.

## Consequences

Confusing the two is how *"we approved the technology"* becomes *"we have the capability"*.

## Where they live

Reference catalog: `model/catalog4.py` (143 entries — 76 services, 57 ABBs, 5 patterns,
5 standards). Realization catalog: `model/realization.json`.

> *Location note, 4 September 2026:* the reference catalog is now
> `archive/reference-catalog/catalog4.py`, frozen; the realization catalog became
> `facts/offerings.json` (ADR-0013 §3).

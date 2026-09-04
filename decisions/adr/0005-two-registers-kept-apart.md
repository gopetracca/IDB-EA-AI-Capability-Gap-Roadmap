---
id: ADR-0005
alias: D5
title: Two registers, kept apart
status: Accepted
date: 2026-09-02
depends_on: [ADR-0004]
---

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

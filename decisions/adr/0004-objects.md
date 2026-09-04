---
id: ADR-0004
alias: D4
title: Objects — capability, pattern, ABB, SBB, service
status: Accepted
date: 2026-09-02
depends_on: []
---

# ADR-0004 · Objects

> **Alias `D4`.**

## Status

**Accepted** — 2 September 2026.

## Context

TOGAF does not prescribe the ordering of capability, pattern and building block. Pattern is not
even a formal entity in the content metamodel, and the text says patterns identify combinations of
ABBs *and/or* SBBs. No amount of further reading resolves this. It is settled by decision.

## Decision

**Capability → Pattern → ABB → SBB**, plus **Service** for exposed consumable behavior.

Technology offering and deployed instance are **fields on the SBB record**, not model objects —
TOGAF defines no "product" concept, so this is a stated local convention.

## Corrections carried in

- An SBB **may be procured or developed** (TOGAF §33.2.4) — in-house Terraform modules are SBBs.
- A **pattern is not a name.** TOGAF requires problem, context, forces, solution, resulting
  context, rationale and known uses.
- A capability **may be an ability not yet possessed** — ArchiMate covers "current *and desired*"
  abilities.

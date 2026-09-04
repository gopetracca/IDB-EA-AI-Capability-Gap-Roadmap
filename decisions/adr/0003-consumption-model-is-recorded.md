---
id: ADR-0003
alias: D3
title: Consumption model is a recorded fact, not a definition
status: Accepted
date: 2026-09-02
depends_on: [ADR-0001, ADR-0002]
---

# ADR-0003 · Consumption model is a recorded fact, not a definition

> **Alias `D3`.**

## Status

**Accepted** — 2 September 2026.

## Context

A recurring disagreement: *"a capability means I don't have to build it."* Argued as a definition,
it never resolves.

## Decision

Guidance · Building blocks · Reference implementation · Managed platform · Service/API.

Recorded **on the realization, not the capability**.

## Consequences

This settles the recurring disagreement **without redefining the word capability**. That belief is
about consumption model. Record it as one and the argument stops being definitional.

## Where it lives

`model/realization.json` → `consumption[]`.

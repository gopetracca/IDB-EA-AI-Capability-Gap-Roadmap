---
id: ADR-0003
alias: D3
title: Consumption model is a recorded fact, not a definition
status: Superseded
superseded_by: [ADR-0013]
date: 2026-09-02
depends_on: [ADR-0001, ADR-0002]
---

> ## ⚠ SUPERSEDED by [ADR-0013](0013-facts-and-scales.md) — 4 September 2026
>
> The consumption model is now a plain field on the offering record. The insight — that the recurring argument is about consumption, not about the word 'capability' — is carried forward intact.
>
> This record is kept unedited: an ADR is never rewritten to reverse itself. Read it as
> the account of what was believed on 2 September 2026 and why. For how the model works
> now, see [ADR-0013](0013-facts-and-scales.md) and [`../../how-it-works.md`](../../how-it-works.md).


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

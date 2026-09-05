---
id: ADR-0008
alias: D8
title: Statutory references live outside the model
status: Accepted
date: 2026-09-02
owner: Legal
---

# ADR-0008 · Statutory references live outside the model

> **Alias `D8`.**

## Status

**Accepted** — 2 September 2026.

## Decision

Statutory references are held in a **Legal-owned obligations register**, all marked
*candidate — applicability not determined*.

`7.6.6 Regulatory Role Determination` is the prerequisite.

## Note carried in

EU AI Act Articles 49, 72 and 73 are **provider** obligations. On the use cases contemplated here
the institution would be a **deployer**.

## Where it lives

`model/obligations.json` — 18 statutory references, all candidate.

> *Location note, 4 September 2026:* now `facts/obligations.json`, read by the build and
> shown on sheet 9 of the workbook and in `out/provenance.md`. Six of the 18 had pointed at
> service ids in the frozen reference catalog rather than at capabilities; they were re-homed
> to the parent capability of the criteria the catalog linked them to (the `subject` names
> the former service id). The re-homing is mechanical; applicability remains for Legal.

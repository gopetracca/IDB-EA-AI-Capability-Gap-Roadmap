---
id: ADR-0006
alias: D6
title: Single primary home, not mutual exclusivity
status: Accepted
date: 2026-09-02
depends_on: []
---

# ADR-0006 · Single primary home, not mutual exclusivity

> **Alias `D6`.**

## Status

**Accepted** — 2 September 2026.

## Decision

The eight domains are **reporting clusters** — not a sequential lifecycle, and not proof of
ontological exclusivity. Every subject has exactly one `primary_domain` and may carry typed links
to others.

## Consequences

Alternative partitions (an analyst model's tiers, the World Bank's four dimensions) can be
reported as **lenses over the same ratings**, with no re-rating. See ADR-0011 §5.3.

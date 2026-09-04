---
id: ADR-0007
alias: D7
title: Repository anchoring is provisional
status: Accepted
date: 2026-09-02
open_items: [anchor-crosswalk, control-mapping]
---

# ADR-0007 · Repository anchoring is provisional

> **Alias `D7`.**

## Status

**Accepted, with a live constraint** — 2 September 2026.

## Decision

Every capability carries **New / Specialization / Lens** with a confidence.

**Lens means do not create a node** — keep the existing enterprise capability and attach an AI
assessment profile.

## Consequences

14 of 52 are lenses. Loading them as new nodes produces two change-management capabilities with
two owners.

## Open — blocks approval

- **Anchor crosswalk** unverified until the institution's existing capability map is available.
- **Control mapping** — ISO/IEC 42001 Annex A and NIST AI RMF outcomes are not mapped.
  **Carve this ADR out of any approval request until they are.**

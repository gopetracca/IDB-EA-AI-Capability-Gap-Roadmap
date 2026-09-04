---
id: ADR-0010
alias: D10
title: Provenance is graded by whether a reviewer can open it, not by prestige
status: Accepted
date: 2026-09-02
amended: 2026-09-03
informs: [ADR-0011]
---

# ADR-0010 · Provenance is graded by whether a reviewer can open it

> **Alias `D10`.**

## Status

**Accepted** 2 September 2026 · re-verification of 3 September 2026 recorded in
`provenance/findings-2026-09-03.md`.

## Decision — evidence grade

Every source carries an **evidence grade**:

| Grade | Meaning |
|---|---|
| **A** | Openly available, dated, versioned, from a standards body or public authority |
| **B** | Openly available and dated, but vendor-published or non-normative |
| **C** | Available but undated, superseded, publisher-flagged historical, or paywalled |
| **D** | Non-public, or not a publication at all |

> **A grade-D source cannot support a claim in anything that leaves the Bank**, whatever its
> quality.

## Decision — derivation type and locus

Each capability-source pair also carries a **derivation type** — Adopted, Adapted, Corroborating,
Synthesized, Institutional, Unsupported — and a **locus**, the specific part of the source relied
on.

A capability whose locus is never pinned is **reclassified Synthesized** rather than left claiming
a source it cannot point into.

> *Assembled by us* is a stronger position with Internal Audit than a citation that does not
> resolve.

## Standing rules

- **Cite by name, never by number**, for any list whose numbering changes between editions — the
  OWASP Top 10 above all.
- **NIST AI RMF locus form is `GOVERN 1.1`** — function, space, category.subcategory. Not
  hyphenated. The hyphenated form belongs to AI 600-1 action ids (`GV-1.1-001`).
- **Do not invent a clause number.** If a locus cannot be verified against the source text, mark
  it unverified or reclassify the capability as Synthesized.

## Where the register lives

`model/sources.json` — 40 canonical sources with edition, date, access, URL and grade.
`model/citations.json` — 147 capability-source pairs with derivation type and locus.

Findings from re-verification: `provenance/findings-2026-09-03.md`.

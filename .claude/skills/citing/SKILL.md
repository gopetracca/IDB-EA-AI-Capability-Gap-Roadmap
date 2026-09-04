---
name: citing
description: Use before citing, quoting, paraphrasing or attributing any external standard, framework, analyst model or clause number in this repository — ISO, NIST, TOGAF, COBIT, OWASP, MCP, vendor documentation or licensed analyst material. Also use when deciding whether something may leave the Bank. Enforces verify-before-writing and the A-D evidence grades.
---

# Citing something in this repository

The governing rule is ADR-0010: **provenance is graded by whether a reviewer can
open it, not by prestige.**

## Verify before you write it down

Do not cite from memory. This has produced wrong attributions in this repository
before — the process attribute that carries competence, which standard COBIT 2019
builds on, and which clause names a rating scale were each wrong when written
from memory and each corrected by opening the source.

Before any citation, one of:

- Fetch the source and read the relevant part.
- Find the publisher's own page for edition, date and status.
- If neither is possible, **say it is unverified in the text itself.**

Secondary sources establish that a claim exists, not that it is true. A summary
of a paywalled standard is evidence about the summary.

## Grades

| Grade | Meaning |
|---|---|
| **A** | Openly available, dated, versioned, standards body or public authority |
| **B** | Openly available and dated, but vendor-published or non-normative |
| **C** | Available but undated, superseded, publisher-flagged historical, or paywalled |
| **D** | Non-public, or not a publication at all |

> **A grade-D source cannot support a claim in anything that leaves the Bank**,
> whatever its quality.

## Standing rules

- **Cite by name, never by number**, for any list that renumbers between
  editions. The OWASP Top 10 above all.
- **NIST AI RMF locus form is `GOVERN 1.1`** — function, space,
  category.subcategory. Not hyphenated; the hyphenated form belongs to AI 600-1
  action ids (`GV-1.1-001`).
- **Do not invent a clause number.** If a locus cannot be verified against the
  source text, mark it unverified or say the content is ours. *Assembled by us*
  is a stronger position with Internal Audit than a citation that does not
  resolve.
- **Check for supersession.** Several sources here were superseded after being
  cited: ISO/IEC 27701 restructured, the IIA Three Lines Model reissued, the MCP
  specification revised with breaking changes, AWS CAF-AI flagged historical by
  its own publisher.

## Currently unverified in this repository

**ISO/IEC 33020:2019** backs the default scale. Its published preview stops
before clause 5.3, so two things rest on secondary sources about the *superseded*
ISO/IEC 15504 and **must not be quoted**:

- the N-P-L-F percentage bands (0–15 / >15–50 / >50–85 / >85–100)
- the exact capability level rule

Verified from the preview and safe to cite: the six-point scale 0 Incomplete →
5 Innovating, the process attribute ids and names, PA 2.1's resource and
competence outcomes, and that the second edition cancels and replaces the 2015
edition. See `scales/README.md`.

## Licensed and non-public material

- **Licensed analyst material** is usable inside the Bank, never reproduced
  externally, and never listed as a source in `facts/sources.json`. Any
  crosswalk lives in an internal-only artifact citing the document number alone.
- **The World Bank slide** is a maturity model, not a readiness scale, marked
  Official Use Only. Grade D. Never cite outside the Bank.
- **Everything in `docs/notes/`** is grade D and internal only.

## Before anything circulates externally

Check it carries no grade-D support, no licensed analyst wording, no World Bank
slide content, and nothing from `docs/notes/`. Four known provenance findings are
open in `OPEN-ITEMS.md` and block external publication until closed.

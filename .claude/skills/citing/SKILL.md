---
name: citing
description: Use before citing, quoting, paraphrasing or attributing any external standard, framework, analyst model or clause number in this repository — ISO, NIST, TOGAF, COBIT, OWASP, MCP, vendor documentation or licensed analyst material — including adding a source to the register, pinning a locus, or deciding whether something may leave the Bank.
---

# Citing something in this repository

The governing rule is ADR-0010: **provenance is graded by whether a reviewer can open it,
not by prestige.** The register is `facts/sources.json`; the live view of what rests on
what is `out/provenance.md`; sheet 8 of the workbook shows the register to a reviewer.

## Verify before you write it down

Do not cite from memory. This has produced wrong attributions in this repository before —
the process attribute that carries competence, which standard COBIT 2019 builds on, and
which clause names a rating scale were each wrong when written from memory and each
corrected by opening the source.

Before any citation, one of:

- Fetch the source and read the relevant part.
- Find the publisher's own page for edition, date and status.
- If neither is possible, **say it is unverified in the text itself** — in the register's
  `caution` field, in the locus string, and in your reply.

Secondary sources establish that a claim exists, not that it is true. A summary of a
paywalled standard is evidence about the summary. A clause number that "mirrors" another
standard's structure is a guess until the text is opened.

## Grades

| Grade | Meaning |
|---|---|
| **A** | Openly available, dated, versioned, standards body or public authority |
| **B** | Openly available and dated, but vendor-published or non-normative |
| **C** | Available but undated, superseded, publisher-flagged historical, or paywalled |
| **D** | Non-public, or not a publication at all |

> **A grade-D source cannot support a claim in anything that leaves the Bank**,
> whatever its quality. `out/provenance.md` names the capabilities that currently rest
> partly on one; today there are 10.

## Where a citation lives, mechanically

- A capability cites a **string** in its `sources` list (`facts/capabilities.json`).
- `facts/sources.json` → `normalize` maps that string to `{"source": "Sxx", "locus": "..."}`.
  `check` fails if a string does not resolve, so add the `normalize` entry when you add the
  string.
- A **locus** is the clause, section, control or category relied on, in the source's own
  `locus_form` (`GOVERN 1.1`, `A.5`, `6.4.2 Risk identification`). Empty means *not yet
  pinned*; most are, and an unpinned pair reads as *synthesized* under ADR-0010.
- **To pin a locus for one capability**, give that capability a more specific citation
  string — `"<short> - <topic>"`, e.g. `"ISO/IEC 23894 - risk identification"` — and add a
  `normalize` entry mapping it to the source and the locus. Do **not** put a locus on the
  bare string (`"ISO/IEC 23894"`): several capabilities share it and would all inherit a
  clause that may not be theirs. Follow the existing entries
  (`"ISO/IEC 5338 - retirement processes"`, `"ISO/IEC 42001 - AI management system"`).
- **Check the premise first.** If asked to pin a locus for a source the capability does not
  cite, say so and offer the choice (add the citation, or pin it on the capability that does
  cite it) rather than inventing a citation.
- **A locus can be partly verified — record the boundary, not just the fact.** Confirming a
  clause's *number and title* against a publisher's own table of contents is real
  verification of that much; it is not verification of what the clause *says*. Pin the locus
  either way (the register records where the citation points, not that its content was
  read), but the source's `caution` must say exactly how far the check went and that the
  body was not opened — do not let a partial check read as a full one, and do not paraphrase
  or reconstruct the unopened content from what a similar clause elsewhere might say.
- Record what you verified and what you could not in the source's `caution`, dated. If the
  work is substantial enough to want a narrative record, add a dated entry to
  `docs/provenance/findings-YYYY-MM-DD.md`, matching `findings-2026-09-03.md`, and add it to
  the findings log table in `docs/provenance/README.md`.
- Then `uv run python build/build.py check && uv run python build/build.py all`. The live counts
  are in `out/provenance.md`; dated figures in `OPEN-ITEMS.md` and `docs/provenance/` are
  snapshots and need not be chased.

## Standing rules

- **Cite by name, never by number**, for any list that renumbers between editions. The
  OWASP Top 10 above all.
- **NIST AI RMF locus form is `GOVERN 1.1`** — function, space, category.subcategory. Not
  hyphenated; the hyphenated form belongs to AI 600-1 action ids (`GV-1.1-001`).
- **Do not invent a clause number.** If a locus cannot be verified against the source text,
  mark it unverified or say the content is ours. *Assembled by us* is a stronger position
  with Internal Audit than a citation that does not resolve.
- **Check for supersession.** Several sources here were superseded after being cited:
  ISO/IEC 27701 restructured, the IIA Three Lines Model reissued, the MCP specification
  revised with breaking changes, AWS CAF-AI flagged historical by its own publisher.

## Currently unverified in this repository

**ISO/IEC 33020:2019** backs the default scale. Its published preview stops before clause
5.3, so two things rest on secondary sources about the *superseded* ISO/IEC 15504 and
**must not be quoted**:

- the N-P-L-F percentage bands (0–15 / >15–50 / >50–85 / >85–100)
- the exact capability level rule

Verified from the preview and safe to cite: the six-point scale 0 Incomplete →
5 Innovating, the process attribute ids and names, PA 2.1's resource and competence
outcomes, and that the second edition cancels and replaces the 2015 edition. See
`scales/README.md`.

## Licensed and non-public material

- **Licensed analyst material** is usable inside the Bank, never reproduced externally, and
  never listed as a source in `facts/sources.json`. Any crosswalk lives in an internal-only
  artifact citing the document number alone.
- **The World Bank slide** is a maturity model, not a readiness scale, marked Official Use
  Only. Grade D. Never cite outside the Bank. The maturity lens's level names are the
  generic CMM vocabulary and must never be attributed to that slide.
- **Everything in `docs/notes/`** is grade D and internal only.

## Before anything circulates externally

Check `out/provenance.md`: it carries no grade-D support, no licensed analyst wording, no
World Bank slide content, and nothing from `docs/notes/`. Four known provenance findings are
open in `OPEN-ITEMS.md` and block external publication until closed.

# Decisions

Architecture Decision Records for the AI capability model. **One decision per file**, numbered
`ADR-NNNN`, never renumbered once issued.

These records govern *how the model is structured*. They are not the content of the model itself —
that lives in `facts/` (schemas in [`../../facts/README.md`](../../facts/README.md)).

## Why these exist

The standards do not settle them. TOGAF does not prescribe the ordering of capability, pattern and
building block; Pattern is not even a formal entity in the content metamodel. No amount of further
reading resolves it. It is settled by decision and recorded here.

---

## Index

> ### ⚠ Read ADR-0013 first
>
> **[ADR-0013 · Facts and scales are separated](adr/0013-facts-and-scales.md)** supersedes
> ADR-0001, ADR-0002 and ADR-0003, and amends ADR-0004 and ADR-0005.
> It is itself amended by **[ADR-0014](adr/0014-practised-is-observed-at-l3.md)**, which moves the `practised` observation down to L3. The two-scale model
> (maturity on a capability, readiness on a realization) is no longer how this model works.
> Those records are kept, unedited, as the account of what was believed and why.

| ADR | Title | Status | Date |
|---|---|---|---|
| [ADR-0001](adr/0001-two-scales-never-merged.md) | Two scales, never merged | ~~Superseded~~ by ADR-0013 | 2026-09-02 |
| [ADR-0002](adr/0002-readiness-levels.md) | Readiness levels | ~~Superseded~~ by ADR-0013 | 2026-09-02 |
| [ADR-0003](adr/0003-consumption-model-is-recorded.md) | Consumption model is a recorded fact | ~~Superseded~~ by ADR-0013 | 2026-09-02 |
| [ADR-0004](adr/0004-objects.md) | Objects — capability, pattern, ABB, SBB, service | Accepted, amended by ADR-0013 | 2026-09-02 |
| [ADR-0005](adr/0005-two-registers-kept-apart.md) | Two registers, kept apart | Accepted, amended by ADR-0013 | 2026-09-02 |
| [ADR-0006](adr/0006-single-primary-home.md) | Single primary home, not mutual exclusivity | Accepted | 2026-09-02 |
| [ADR-0007](adr/0007-anchoring-is-provisional.md) | Repository anchoring is provisional | Accepted ⚠ | 2026-09-02 |
| [ADR-0008](adr/0008-statutory-references-outside-the-model.md) | Statutory references live outside the model | Accepted | 2026-09-02 |
| [ADR-0009](adr/0009-taxonomy-validated-before-scoring.md) | Taxonomy validated before scoring | Accepted, amended | 2026-09-03 |
| [ADR-0010](adr/0010-provenance-grading.md) | Provenance graded by whether a reviewer can open it | Accepted | 2026-09-02 |
| [ADR-0011](adr/0011-scale-provenance.md) | Provenance of the two scales | Accepted | 2026-09-04 |
| [ADR-0012](adr/0012-capability-ownership-model.md) | How to record who owns a capability | **Proposed** | 2026-09-04 |
| [ADR-0013](adr/0013-facts-and-scales.md) | **Facts and scales are separated** | **Accepted**, amended twice | 2026-09-04 |
| [ADR-0014](adr/0014-practised-is-observed-at-l3.md) | **Practised is observed at L3 and derived at L2** | **Accepted** | 2026-09-04 |
| [ADR-0015](adr/0015-extend-d4-d6-across-the-agentic-seam.md) | **Extend D4-D6 across the agentic seam** | **Accepted** | 2026-09-09 |

⚠ **ADR-0007 must be carved out of any approval request** until ISO/IEC 42001 Annex A and NIST AI
RMF outcomes are mapped.

---

## Alias table — the old D-numbers

The accepted decisions were originally issued as `D1`–`D10` in a single file. Those identifiers
appear throughout `CLAUDE.md`, the build scripts, the review workbooks and material already sent
to reviewers. **Both identifiers name the same record.**

| Old | New | | Old | New |
|---|---|---|---|---|
| D1 | ADR-0001 | | D6 | ADR-0006 |
| D2 | ADR-0002 | | D7 | ADR-0007 |
| D3 | ADR-0003 | | D8 | ADR-0008 |
| D4 | ADR-0004 | | D9 | ADR-0009 |
| D5 | ADR-0005 | | D10 | ADR-0010 |

> ### ⚠ `D1`–`D8` are ambiguous in this repository
>
> They are **also** the eight domain identifiers (`D3` = Data, `D8` = People & Culture). Which one
> is meant is nearly always clear from context, but when writing new text prefer **`ADR-0001`** for
> a decision and **`domain D3`** for a domain. Never rewrite a `D`-number mechanically.

---

## Status vocabulary

| Status | Meaning |
|---|---|
| **Proposed** | Argued and written up, awaiting a call from the decision owner |
| **Accepted** | Settled. Binding on the model and the builders |
| **Superseded** | Replaced. Kept, never deleted — `superseded_by` names the replacement |

An ADR is **never edited to reverse itself**. A reversal is a new ADR that supersedes it. Dated
amendments that refine a decision without reversing it are added as `## Amendment N` sections
(see ADR-0009, ADR-0013). When a file an ADR points at moves, the record gets a dated
*location note* under the pointer rather than a silent rewrite — the pointer is a fact about
the repository, not part of the decision.

## Adding one

Copy `TEMPLATE.md`, take the next free number, fill the frontmatter, add a row to the index above.

## The originals

The single files this ADR set was split out of are in
[`../../archive/pre-adr-originals/`](../../archive/pre-adr-originals/README.md).
Nothing there is current.

## Canonical location

**This directory is canonical.** The claude.ai Project doc `claude/meta-model-decisions.md` is a
mirror; update it after a decision settles here.

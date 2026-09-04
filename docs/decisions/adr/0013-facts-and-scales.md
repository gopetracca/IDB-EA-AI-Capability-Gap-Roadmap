---
id: ADR-0013
title: Facts and scales are separated; one derived level replaces the two scales
status: Accepted
date: 2026-09-04
supersedes: [ADR-0001, ADR-0002, ADR-0003]
amends: [ADR-0004, ADR-0005]
depends_on: [ADR-0010]
---

# ADR-0013 · Facts and scales are separated

## Status

**Accepted** — 4 September 2026. Supersedes **ADR-0001** (two scales, never merged),
**ADR-0002** (readiness levels) and **ADR-0003** (consumption model is recorded).

Per the standing rule, those ADRs are not edited. They stand as the record of what was
believed, and §4 below states where each was right.

## Context

The model carried two scales: **maturity** on a capability (1–5, evidence-gated) and
**readiness** on a realization (0–5, structural). ADR-0001 forbade merging them.

Three things went wrong, and only the third is fatal.

1. **The instrument could not be operated.** Evidence-gated maturity needs 52 rubrics
   and 258 criteria typed mandatory / conditional / enhancing. One rubric existed. For
   one part-time person the remaining 51 were never going to be written, so every rating
   would have stayed provisional indefinitely.
2. **The distinction could not be held.** Two abstract nouns, two 0–5 scales, the same
   heat colours, adjacent columns. Colleagues read them as two opinions about one thing.
   The author reported not holding it under pressure either.
3. **The judgement was fused into the model.** Because the scale was the schema,
   changing our mind about measurement meant migrating the model and re-rating. There
   was no way to report the same evidence two ways, and no way to correct a scale
   without invalidating what had been collected.

A fourth problem was structural: **readiness did not apply to most capabilities.** Of
52, roughly a dozen are realized by existing enterprise services and four are purely
organizational. The workbook nonetheless computed a best-readiness column for all 52,
showing blank for about thirty — which every reader interprets as zero.

## Decision

**Separate what is true from what we make of it.**

### 1 · Facts

`facts/` holds only things that are true about the Bank, each with evidence and a date.
The capability map, the offerings, the assets, the owners, and the **observations**.

Four observations per capability, valued `yes` / `partial` / `no` / `n/a` / `unknown`:

| Observation | The question |
|---|---|
| **Practised** | Is this done on real AI systems in production, repeatedly? |
| **Enabled** | Can a team get the tooling without building it themselves? |
| **Skilled** | Do the people who must do this know how? |
| **Defined** | Is there a published Bank standard or method? |

`n/a` requires a recorded reason. `unknown` means nobody has looked and is **never**
treated as zero.

### 2 · Scales

`scales/` holds rules that read observations and return a level. Each is one small file.
Adding one changes nothing else in the repository.

The **default** is `capability_level.py`, adapted from **ISO/IEC 33020:2019**:
0 Incomplete → 5 Innovating, with performance at Level 1, resources and competence at
Level 2, and a defined process at Level 3.

**A level is never typed. It is always derived.**

### 3 · Offerings replace realizations

The realization triple (capability × pattern × technology) produced four rows for one
story. The object a team consumes — and the object the room asks about — is a **bundle**:
standard, reference architecture, modules, templates, and what comes in the box.

Readiness ceases to be a scale. It is the in-the-box checklist, counted.

## Consequences

- **Supply cannot masquerade as ability** — the fact ADR-0001 existed to protect — but
  now structurally rather than by convention. `enabled` contributes nothing without
  `practised`, so *"semantic retrieval: 4, via Azure AI Search"* cannot be written.
- **The rubric workstream is closed.** The 258 criteria become the checklist behind a
  `practised` judgement, never gates. 51 unwritten rubrics stop blocking anything.
- **The consumption model becomes a field on the offering** rather than a decision. It
  is recorded and is no longer a scale-shaped concept competing with readiness.
- **Correcting a scale costs one file.** The level ladder was wrong twice during its own
  design before the ISO text corrected it; each fix was a two-line edit.
- **More cells to fill:** four observations rather than one rating, about 160 live after
  `n/a` drops out. Each is a yes-or-no with obvious evidence rather than a rubric
  judgement, and the argument moves to the column, which is where it belongs.
- **Two scales can show different numbers.** Mitigation: one default everywhere, others
  labelled lenses and offered only when a room arrives holding that frame.

## Where ADR-0001 was right, and where it was wrong

**Right, and carried forward:** supply and ability are different questions; the collapse
fails asymmetrically, with supply masquerading as ability and never the reverse; and
*"both numbers or neither"* correctly identified that a single ungated number hides the
distinction.

**Wrong:** the conclusion that the two must therefore be *reported* as two numbers. A
single **gated** number does not collapse them — it orders them, and shows the
underlying facts as columns beside it. ADR-0011 §4.2's argument holds against an
unstructured number and does not hold against a gated one.

**Wrong, and consequentially:** ADR-0001 §4.3 argued the scales cannot merge because
they attach to different objects. True, and the reason readiness is now a property of
the **offering** rather than a second scale on the capability. That fixes the object
model rather than requiring two scales on the capability.

**ADR-0011 survives as history.** Its account of what was surveyed and what was found is
accurate and worth keeping. Its conclusion is superseded by this record. Its warning that
*assembled by us is a stronger position than a citation that does not resolve* now cuts
the other way: the default scale is **adapted from a current ISO standard**, which is a
stronger position than the synthesized readiness scale ever had.

## Provenance

Under ADR-0010:

- **Adapted** — the level ladder, the attribute ordering, and derivation-from-attributes,
  from ISO/IEC 33020:2019 (grade **C**, paywalled).
- **Ours** — four observations rather than five process attributes; three values rather
  than the standard's four-point N-P-L-F; applying a *process* measurement framework to
  a *capability* map.
- **Not verified** — the N-P-L-F percentage bands and the exact level rule. The published
  preview stops before clause 5.3. **Do not quote them** until the standard is opened
  through the Bank's ISO subscription. See `scales/README.md`.

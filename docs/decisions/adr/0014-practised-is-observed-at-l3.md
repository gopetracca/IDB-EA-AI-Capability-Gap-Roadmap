---
id: ADR-0014
title: Practised is observed at L3 and derived at L2
status: Accepted
date: 2026-09-04
amends: [ADR-0013]
depends_on: [ADR-0013, ADR-0009]
---

# ADR-0014 · Practised is observed at L3 and derived at L2

## Status

**Accepted** — 4 September 2026. Amends **ADR-0013**; reverses nothing in it.

ADR-0013 stands as written. This record closes a hole it left open, using the
mechanism ADR-0013 itself established: a level is never typed, it is derived.

## Context

ADR-0013 closed the rubric workstream and made the 258 L3 criteria *"the checklist
behind a `practised` judgement, never gates."* That was right — 51 unwritten rubrics
were never going to be written, and they were blocking every rating.

But closing the rubric workstream removed L3 from the **instrument** as well as from
the **scale**. What remained was a reference list. Three consequences, observed when
the workbook was read as an operator would read it:

1. **No step uses the criteria.** Sheet 6 lists all 258. Sheet 2 is where a reviewer
   works, and it never mentions them. The checklist behind the judgement is never
   handed to the person making the judgement.
2. **`practised` is the one judgement still typed.** Every other number in the model
   is derived. `practised` is a hand-typed verdict, and the model's central rule —
   *facts, not scores* — does not reach it.
3. **The L2 question is not answerable as posed.** `4.4 Agent & Workflow
   Orchestration Design` covers six distinct practices. The Bank plausibly does
   guardrails and never does loop control. *"Is 4.4 practised?"* has no honest
   single answer, and `partial` absorbs the question rather than recording it.

The evidence already collected proves the point. ADR-0013's own worked example records
*"4 agents built on Foundry; 1 has written guardrails"* against `4.4`. That is a fact
about criterion **4.4.5**. It was written at L2 because the schema had nowhere else to
put it, and the information about *which* of the six was seen is lost on arrival.

**The observable reality is at L3. The accountable unit is at L2.** The model had no
step connecting them.

## Decision

**`practised` is observed per L3 criterion. The L2 `practised` value is derived from
those observations and is never typed.**

Nothing else changes. Specifically, and deliberately:

- **The other three observations stay at L2.** `enabled`, `skilled` and `defined` are
  properties of tooling, people and standards, which do not decompose per criterion in
  any way a reviewer could answer. Only `practised` asks about work that is witnessed.
- **Criteria still carry no level of their own.** They carry an observation, which is
  a fact. They are still not gates in the ADR-0013 sense: no criterion has a rubric,
  and none is typed mandatory / conditional / enhancing. The rubric workstream stays
  closed.
- **The level ladder is untouched.** `scales/capability_level.py` continues to read
  four L2 values. It does not know criteria exist.

### The roll-up rule

Strict, all-or-nothing, with `unknown` excluded from the denominator:

| L3 criterion observations | L2 `practised` |
|---|---|
| Every applicable criterion `yes` | `yes` |
| At least one `yes`, and any criterion `partial` or `no` | `partial` |
| No criterion `yes`, at least one `no` | `no` |
| Every applicable criterion `unknown` | `unknown` — nobody has looked |
| Every applicable criterion `n/a` | `n/a` — needs a reason, per ADR-0013 |

Two properties this rule was chosen for:

- **One weak link stops the claim.** This is the same asymmetry the level ladder
  already enforces: it is what stops a capability reading as fully performed when a
  third of it has never been done. A majority rule would let `4.4` read `yes` with
  loop control absent, which is the over-claiming ADR-0013 exists to prevent.
- **A partly-examined capability is still ratable.** `unknown` criteria drop out
  rather than un-rating the whole L2. A reviewer who has looked at four of six
  criteria has produced real information, and the model records it. The alternative —
  any `unknown` blocks the L2 — makes the instrument unusable in a first round, where
  most criteria are unexamined by definition.

`unknown` remains never a zero, at both levels.

### What this costs

- **258 observation rows replace 52.** The count is the honest one: it is how many
  distinct things the taxonomy claims the Bank does. A reviewer answers only for the
  capabilities they own, which is how the round was always going to be run.
- **A reviewer sees more cells.** They also see, for the first time, *what they are
  being asked about* — a named practice with a definition, rather than an abstract
  capability name. This is expected to make the round faster per answer, not slower,
  though that is a prediction and not yet evidence.

## Consequences

- **`practised` becomes a finding rather than a feeling.** *"4.4 is partial"* becomes
  *"4.4.1 and 4.4.5 yes, 4.4.3 and 4.4.6 no, 4.4.2 partial, 4.4.4 unexamined."* The
  argument moves to the criterion, which is where it can be settled by looking.
- **Sheet 6 stops being an appendix.** The criteria become the rows a reviewer fills
  in, which is what ADR-0013 always said they were for.
- **The gap register gets finer.** A roadmap item can name the criterion that is
  missing rather than the capability that is partial. `4.4.6 Termination & Loop
  Control` is an actionable piece of work; *"improve agent orchestration"* is not.
- **The model says the same thing at both levels**, because one is computed from the
  other. There is no longer a place where L2 and L3 can disagree.
- **`facts/observations.json` changes shape.** Existing L2 `practised` rows are
  replaced by criterion rows. Because every current `practised` value is `unknown`
  with no evidence, **no recorded evidence is lost in the migration** — this is the
  cheapest moment in the model's life to make this change, and that is part of why it
  is being made now.
- **ADR-0009 still holds.** Criteria carry the same provisional standing as the
  capabilities above them; observing against them is not validation of them.

## What was considered and rejected

**Leave it, and hand reviewers the criteria as a separate interview guide.** Cheapest,
and keeps the workbook a pure L2 instrument. Rejected because it leaves `practised` as
the one typed judgement in a model whose whole claim is that judgements are derived,
and because a guide nobody is required to open is a guide nobody opens.

**A free-text column on the L2 `practised` row listing criteria observed.** Cheap, no
schema change. Rejected because `check` cannot validate free text, and because it
records the reviewer's summary of what they saw rather than what they saw.

**Reopen the rubrics — type each criterion mandatory / conditional / enhancing.** This
is what ADR-0013 closed, and closing it was correct. An observation is not a rubric: it
records whether a thing is done, not how much it is worth. Nothing here reopens that.

**Decompose all four observations to L3.** Rejected: `enabled`, `skilled` and `defined`
have no per-criterion answer a reviewer could give, and asking for one would produce
1,032 rows of mostly-invented distinctions.

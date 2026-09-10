---
id: ADR-0017
title: Carve out experimentation, and re-home shared agent assets
status: Accepted
date: 2026-09-10
decision_owner: Gabriel Petracca, Enterprise Architecture
supersedes: []
superseded_by: []
depends_on: [ADR-0009, ADR-0010, ADR-0013, ADR-0014, ADR-0015, ADR-0016]
---

# ADR-0017 · Carve out experimentation, and re-home shared agent assets

## Status

**Accepted** — 10 September 2026. Adds one capability and re-scopes two criteria.
Reverses nothing. Nothing is renumbered.

## Context

The D5 walkthrough of 10 September 2026 graded the platform domain and, in doing so, hit
three places where the taxonomy did not match how the Bank organizes the work. The workbook
is kept unedited at
[`review/2026-09-10-ea-meeting.xlsx`](../../../review/2026-09-10-ea-meeting.xlsx).

**Experimentation was a criterion inside environment management, and it does not belong
there.** `5.3.1 Experimentation Environment Provision` sat under `5.3 AI Environment &
Workspace Management`, whose other four criteria — tenancy, network, data segregation — are
about the environments delivery teams build in. The meeting graded all four `yes` and could
evidence them precisely: Foundry in private network mode, logical isolation through Foundry
projects, Terraform modules for Foundry accounts built by EA, Core Platforms creating
subscriptions and subnets. Experimentation is a different job with a different owner (the
Tech Lab), a different risk posture (total isolation), and — unlike the rest of `5.3` — no
evidence at all. Graded inside `5.3` it would have been carried by four `yes` answers about
something else.

**Shared agent assets had no home, and the nearest criterion was being deleted.** The
meeting first drafted a criterion `4.4.7 Agent Skills`, and a floating row reading *"Shared
AI tools, skills, etc. — where?"*. Pulling that apart gave two different things:

| | Where it lives |
|---|---|
| A production agent having skills — a Foundry-deployed agent's callable actions | **Already in the model.** `5.5` is the governed inventory (registration, scope, vetting, version control), `4.4` designs what the agent may pursue, `5.8.1` is the runtime it executes in. The AI enabler's catalogue entry already claims *"Agent Skill Admin"* |
| A **shared institutional repository** of skills, hooks and rules that agents draw on — chiefly coding agents and desktop AI clients | **Nowhere**, except `5.6.4 Inner-Source & Asset Reuse`, which the same meeting marked *REMOVE* |

`5.6.4` was written as classic inner-source: shared internal code, discoverable and
reusable. That framing is what the meeting rejected. But the need it was written to cover
did not go away — it changed shape. The reusable institutional asset for agent work is a
skill, a hook, a rule, not a library.

**Two definitions arrived that were not authored in the meeting.** `5.7` and `5.8` were
pasted into the sheet from ADR-0015's drafting, in a different voice from the `Able to…`
form the other 53 capabilities use.

## Decision

**One capability is added. Two criteria are re-scoped. One drafted criterion is rejected.**

| | |
|---|---|
| **`5.9 AI Experimentation`** (new) | *Able to try AI in isolation, without exposing institutional systems or data.* One criterion: `5.9.1 Isolated Experimentation Environment Provision` — *Provide an experimentation environment that is fully isolated from institutional systems and data.* Owner: Emerging Tech. `confidence: low`, `anchor: new` (ADR-0009) |
| **`5.3.1`** re-scoped | `Experimentation Environment Provision` → **`Environment Provision`**: *Provide the environments delivery teams build AI in — development, test and production — with clear data rules.* Experimentation leaves `5.3` for `5.9` |
| **`5.6.4`** replaced | `Inner-Source & Asset Reuse` → **`Shared Agent Skill & Extension Repository`**: *Maintain a curated, shared repository of the skills, hooks and rules that agents draw on, discoverable and reusable across the institution.* Same number, current subject |
| **`4.4.7 Agent Skills`** | **Not added.** It conflated the two things above. Its production half is already covered three times over; its institutional half is `5.6.4` |
| **`5.7` and `5.8` definitions** | **Unchanged.** ADR-0015's wording stands. The sheet's variants were pasted for context, not authored |

A capability is warranted where a distinct owner, a failure with no landing site, and no
adequate existing home **all three** coincide (ADR-0015). `5.9` meets all three: the Tech
Lab owns it, an uncontained experiment reaching institutional data lands nowhere else, and
`5.3` is now explicitly about delivery environments. `4.4.7` met none of them.

D5 goes from 8 capabilities to 9; the model goes from 55 to 56, and from 282 criteria
to 283.

## Options considered

| Option | For | Against |
|---|---|---|
| A — `5.9` as a capability, `5.6.4` replaced, `4.4.7` dropped (**chosen**) | Puts each of the two "skills" conversations where its owner can answer for it; keeps experimentation from being carried by four unrelated `yes` answers | Adds a capability with one criterion and no evidence — it will read *not rated* for some time |
| B — Keep experimentation as `5.3.1` | No taxonomy change | `5.3` rolls up to `yes` on four evidenced criteria; an unevidenced fifth would drag a real result down, or be quietly ignored. Different owner, different risk posture |
| C — Add `5.6.6` and keep `5.6.4` | Preserves classic inner-source as a separate question | Two criteria competing for one practice, one of which the meeting had already marked for removal |
| D — Delete `5.6.4` outright, as the sheet said | Simplest reading of the instruction | Loses the need along with the framing. The row was also flagged red — *doubts, needs Karla* — so deletion would act on an instruction the meeting itself was unsure of |
| E — Keep `4.4.7 Agent Skills` | Matches what was typed in the room | Conflates a runtime property of a deployed agent with an institutional asset register. The decision owner asked for these conversations to be separated |

## Consequences

- `facts/capabilities.json`: one capability, one new criterion, two re-scoped criteria.
- `facts/observations.json` gains four rows for `5.9` — one `practised` at `5.9.1` plus
  `enabled`, `skilled`, `defined` — all `unknown`. The meeting's note was *"ASK tech lab"*.
- `facts/owners.json` gains `5.9` → Emerging Tech, `match: Inferred`. The meeting wrote
  *Tech Lab*, which is not a unit in the Bank's catalogue; Emerging Tech is the unit that
  carries that work.
- **`5.6.4`'s observation stays `unknown`.** The criterion number is reused for a new
  subject, so the grade that was never given against the old subject is not carried over.
- `5.3` rolls up to `practised: yes` — the first capability in the model to do so — and is
  held at Level 1 only because `skilled` has never been observed anywhere.
- The **`agentic` flag** is `true` on `5.6.4` in its new form, where it was `false` as
  inner-source. `5.9` is `false`.

## Open

- **`5.9` has one criterion.** Isolation is the only aspect the meeting named. Whether it
  needs criteria for what may enter an experiment, how results graduate to delivery, and
  when an experiment must stop is unresolved, and is a question for the Tech Lab.
- **Who owns `5.7`** is unsettled. The meeting flagged it amber — *"we dont know what to do
  with this"* — with the note *"Might be the control plane v99"*. `facts/owners.json` still
  records the AI enabler from ADR-0015; the meeting's sheet said *Unknown*, on a row it had
  pasted rather than assessed, so nothing is changed here.
- **`5.5`'s ownership was withdrawn** at the same meeting — *"Needs clarification. Who owns
  it, who operates it, who monitors, etc."* — which is recorded as a fact, not decided here.

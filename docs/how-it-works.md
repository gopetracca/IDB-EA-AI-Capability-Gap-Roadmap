# How this model works

Ten minutes. No jargon. If you read one thing, read this.

*Orientation, not normative. The binding records are in [`decisions/`](decisions/README.md).*

---

## 1. The problem it solves

Someone says: **"we don't have the capability to run AI agents."**

Someone else says: **"yes we do — the standards, the reference architectures and the
infrastructure modules are all published."**

Both are telling the truth about different things, and no single number can hold both.
A model that answers with one score has to pick which truth to tell.

The same argument recurs about retrieval, about data governance, about AI security. It is
never really about agents.

## 2. The move: separate facts from judgement

Most maturity models fuse the two. You read a paragraph describing "Level 3" and decide
whether your organisation feels like that. The judgement is baked into the instrument,
so changing your mind about measurement means reassessing everything.

This model splits them.

| | What it is | Example |
|---|---|---|
| **Fact** | Something true about the Bank, with evidence and a date | *The Foundry Agents Standard is pre-release* |
| **Scale** | A rule that reads facts and produces a level | *No practice, no level* |
| **View** | A rendering of one scale over the map | The assessment page, the agent one-pager |

A fact is true whichever framework reads it. So you can run several scales over the same
evidence, and they cannot disagree about what is true — only about what to make of it.

## 3. The four observations

Four questions, each answered `yes` / `partial` / `no` / `n/a` / `unknown`, each with
evidence and a name attached.

| | The question | Asked at | Who usually answers |
|---|---|---|---|
| **Practised** | Is this specific practice done on real AI systems in production, repeatedly? | **each L3 criterion** | The capability owner |
| **Enabled** | Can a team get the tooling without building it themselves? | the L2 capability | The platform team |
| **Skilled** | Do the people who must do this know how? | the L2 capability | The owner, or L&D |
| **Defined** | Is there an approved institutional standard, policy or method? | the L2 capability | Whoever owns the subject: the platform team, Cybersecurity, Data Management, Legal, HR, EA |

### Where each one is recorded, and the one you cannot record

Only two of the three taxonomy levels ever carry an observation, and one of the four
values is not entered by anybody:

| Taxonomy level | What is recorded against it | Rows |
|---|---|:-:|
| **L1 domain** | *Nothing.* A domain is a reporting cluster and is never scored | — |
| **L2 capability** | `enabled`, `skilled`, `defined` — one row each. Plus `practised`, **derived** from the criteria beneath it | 156 |
| **L3 criterion** | `practised` — one row per criterion | 258 |

That is why a review round collects **414 rows, not 52**. And it is why there is nowhere
in the workbook to type a capability's `practised` value or its level: both are computed,
and `check` fails if it finds either stored. See
[`../out/capability-map.md`](../out/capability-map.md) for the three levels themselves.

### Why `practised` is asked lower down

*4.4 Agent & Workflow Orchestration Design* covers six distinct practices — goal
definition, task decomposition, multi-agent coordination, memory design, guardrails,
termination control. The Bank might do guardrails well and never do loop control at all.

*"Is 4.4 practised?"* has no honest single answer. So it is not asked. Each of the six
criteria is judged on its own, and **the capability's value is derived** (ADR-0014):

| The criteria say | The capability reads |
|---|---|
| every one examined, every one `yes` | `yes` |
| some `yes` or `partial`, or any left unexamined | `partial` |
| none `yes` or `partial`, at least one `no` | `no` |
| none examined | `unknown` |

One weak link stops the claim, and an unexamined criterion is never counted as
satisfied — so a capability cannot read `yes` on the strength of one observation while
the rest has never been looked at.

The gain is that a gap gets a name. *"4.4 is partial"* becomes *"termination and loop
control has never been done"*, which is a piece of work someone can be given.

Three values carry weight people usually miss:

- **`no` is an evidenced negative.** Someone looked and it is not there, and the record
  says what they looked at. A register that was searched and had nothing is **not** a
  `no` until the owner has been asked whether something outside the register provides it.
- **`n/a` needs a reason.** *"No platform component exists for AI strategy"* is a
  legitimate n/a. It drops out of the calculation rather than counting as a failure —
  a governance capability is not worse for having no tooling.
- **`unknown` is an honest answer and is never a zero.** It means nobody has looked.
  Most published models cannot say this, so they silently score an unexamined capability
  as if it were absent.

## 4. How the level is computed

You never type a level. The default scale derives it, and the order is what matters:

| Level | Name | What it takes |
|---|---|---|
| 0 | Incomplete | Not performed |
| 1 | Performed | It is done on real systems |
| 2 | Managed | Done, **and** tooling provided, **and** competent people |
| 3 | Established | All of that, **and** done against an approved institutional standard |
| 4 | Predictable | Measured against thresholds — **not derivable today** |
| 5 | Innovating | An improvement cycle closed — **not derivable today** |

### Why one capability is a 2 and another a 3

Read the exact conditions off the generated table, not off this page. Every view carries
a **How this scale places a level** section, derived by running the rule over all 625
combinations of the five values across the four observations — so it cannot drift from
the code the way a paragraph can:

| Where | What it shows |
|---|---|
| [`../out/capability-assessment-level.md`](../out/capability-assessment-level.md) | The default scale's ladder, what each step up costs, and ten worked situations |
| [`../out/capability-assessment-exec.md`](../out/capability-assessment-exec.md), [`-maturity.md`](../out/capability-assessment-maturity.md) | The same, for each lens |
| [`../out/management-report.html`](../out/management-report.html) §4 | All scales side by side, plus the same answers read by every scale at once |

The table reads **cumulatively** — each row is *what it takes to reach at least this
level*. Two things surprise people:

- **`n/a` counts as satisfied.** A capability that legitimately needs no tooling is not
  held down for having none. It drops out; it does not fail.
- **The step from 2 to 3 is a single observation.** Everything Level 3 asks for is
  already required at Level 2 except one thing: `defined` must be `yes`. So a capability
  where the work is done, the tooling is provided and the people are competent sits at
  **2 Managed** until an approved institutional standard exists — and moves to
  **3 Established** the day it does, with no other change. That is the single most common
  question about this model, and that is the whole answer.

The step from 1 to 2 is the wider one: it needs `practised` to go from `partial` to
`yes` — every criterion examined and every one passed — *and* tooling, *and* competence.
Most capabilities that stall will stall there.

### The objection you will get: "but the standard came first"

It usually does — the standard is often written before anything is built. So why does the
top level require it, as if it were last?

**Because the ladder orders claims, not activities.** Each level is a strictly stronger
statement than the one below:

| Level | The claim being made |
|---|---|
| 1 Performed | "We do this." |
| 2 Managed | "We do this, repeatably, with tooling and competent people." |
| 3 Established | "We do this, repeatably, **against an approved institutional standard**." |

Level 3 does not claim *a standard exists*. It claims *the work is done to the standard* —
and that sentence needs the work. A driving manual existing does not mean anyone in the
building can drive.

So writing the standard first does not make a capability Level 3 early. It makes `defined`
read `yes` while `practised` is still `unknown` — which the model records exactly, and
reports as **not rated**. That combination is not the model withholding credit; it *is* the
Bank's headline finding, in one line: **the enablers were built ahead of the practice.** If
`defined` alone could place a level, that finding would be invisible.

The credit for standard-first work is recorded — just not in the level. It is the `defined`
column, the asset register with statuses and locations, and the offerings view.

**And the ordering is not ours.** Performance is the Level 1 process attribute in the
standard the scale is adapted from; a defined process is a Level 3 attribute. See
[`where-the-scales-come-from.md`](where-the-scales-come-from.md) §2.

> The rest of the objections a room will raise — and the answers, with live figures — are
> the appendix of [`../out/walkthrough.html`](../out/walkthrough.html).

**Level 3 is the ceiling of what this model measures, not the ceiling of the scale.**
Levels 4 and 5 need observations nobody collects — threshold monitoring and a closed
improvement cycle. A capability at 3 is at the top of what is being asked about.

**And Level 3 is read, not proved.** `defined` says a standard exists; `practised` says
the work is done. Neither says the work *follows* the standard. Level 3 infers
conformance from the two facts co-existing, and its reason line admits it. A fifth
observation would fix that; whether it is worth collecting is an open question.

**Performance comes first.** This is the whole design. An approved standard with nothing
performed against it earns **no level at all** — because the question was never
*"did we write it down?"*, it was *"can the institution do this?"*

That ordering is not ours. It is ISO/IEC 33020's, the ISO process measurement framework:
performance at Level 1, resources and competence at Level 2, a defined process at
Level 3. See [`../scales/README.md`](../scales/README.md) for what we adopted, what is
ours, and what is not yet verified.

### The worked example

**4.4 Agent & Workflow Orchestration Design** — *able to design what an agent may
pursue, how it plans, and where it must stop.*

Practised, judged criterion by criterion:

| L3 criterion | Value | Evidence |
|---|---|---|
| 4.4.1 Agent Specification & Goal Definition | yes | Specs written for all 4 Foundry agents |
| 4.4.2 Task Decomposition & Planning Design | partial | Only the retrieval agent has a designed plan |
| 4.4.3 Multi-Agent Coordination Design | no | No multi-agent work attempted |
| 4.4.4 Agent Memory & State Design | unknown | Nobody has looked |
| 4.4.5 Guardrail & Constraint Design | partial | Guardrails on 1 of 4 agents |
| 4.4.6 Termination & Loop Control Design | no | No budget or loop control anywhere |

Which derives the capability's four values:

| Observation | Value | Evidence |
|---|---|---|
| Practised | **partial** (derived) | 1 of 6 criteria done, 2 partial, 2 not done, 1 unexamined |
| Enabled | partial | Foundry agents offering, 6 of 8 assets released |
| Skilled | unknown | Nobody has looked |
| Defined | partial | Foundry Agents Standard is **pre-release** |

**Level 1 — Performed.** *"Performed on some AI systems but not repeatably."*

And the sentence that lands in the room: *the platform is strong, the standard is nearly
there, and the practice is thin. The fix is not to buy anything — it is to release two
documents and build the next agent against them.*

Note what the criterion rows add: the roadmap item is no longer *"improve agent
orchestration"*. It is **multi-agent coordination and termination control** — two named
practices nobody has done — **guardrails on the other three agents**, and **agent memory
design**, which nobody has yet looked at.

### Standards are not one function's job

`defined` asks whether an approved standard exists — not whether Architecture wrote it.
Across the 52 capabilities the standard-setter is Cybersecurity for AI security, Data
Management for AI data governance, Legal for regulatory obligations, HR and Learning &
Development for literacy and skills, the platform teams for their own platforms, and
Architecture for architecture. Of 52 capabilities, Architecture is the accountable owner
of two.

Where `defined` currently reads `unknown` — 39 of 52 — it means the asset register covers
AI platform assets only, so a standard owned by another function may well exist and simply
not be recorded here. Those are questions to ask, not gaps to assume.

### Why the roll-up is asymmetric

`yes` needs a complete look: every criterion examined and every one passed. `no` does
not: one examined `no` with the rest unexamined still reads `no`. That is deliberate.
Under-claiming costs a follow-up question; over-claiming is the failure this model exists
to prevent, so the rule leans one way. The record is
[ADR-0014](decisions/adr/0014-practised-is-observed-at-l3.md).

## 5. What a capability is, and what it is not

A **capability** is something the Bank must be able to do, with one accountable owner.
It survives replacing every vendor. `3.6 Knowledge Access & Retrieval` is a capability.

An **offering** is what a delivery team can actually get today: a bundle of standard,
reference architecture, Terraform modules and templates, with someone operating it.
*Retrieval on AI Search* is an offering.

**"Can we build agents?" is not a capability question.** It touches at least eight
capabilities with different owners. That is why the honest answer is a table, not a
number — and why [`../out/agent-readiness.md`](../out/agent-readiness.md) exists.

### Not every capability has an offering, and that is correct

Of 52 capabilities, 12 are realised by enterprise services the Bank already runs and 3 are
purely organisational; for those, `enabled` is `n/a` with the reason recorded in
`facts/enablement-context.json`, and the level rests on the other three observations. A
further 24 have no platform offering and have not yet been examined by their owner: they
read `unknown`, not `no`, until someone says whether an enterprise service or a GRC
platform provides the tooling, or whether none is needed.

Forcing a supply number onto a strategy capability is how a model starts producing
nonsense that nobody trusts. Recording an unexamined absence as a zero is the other way.

## 6. Several scales, one set of facts

Because an observation is a fact and a level is a rule over facts, more than one rule can
read the same evidence. Three ship, each one file in `scales/`:

| Scale | Asks | Standing |
|---|---|---|
| Capability level | Has the institution established this practice? | **The default.** The assessment |
| Executive readiness | How much of what we said we would do exists? | A lens. Averages, deliberately, and says so |
| Institutional maturity | How far has the practice spread beyond the people doing it? | A lens. Same performance gate as the default |

The report shows all three over the same 52 capabilities. **Where a lens and the default
disagree, the default is the finding.** A lens exists so a room that already holds a frame
can be answered in it, not so the friendlier number can be chosen.

## 7. What replaced what

Earlier versions carried **two scales** — maturity on a capability, readiness on a
realization — that were never to be merged. The distinction was real, but it could not
be held in a room, and it required 52 rubrics and 258 typed criteria that were never
going to be written.

This model keeps the fact that distinction was protecting, structurally instead of by
convention: **supply alone cannot produce a level**, because `enabled` contributes
nothing without `practised`. What was two numbers is now one derived level and four
visible columns, and the columns are where the argument belongs.

See [ADR-0013](decisions/adr/0013-facts-and-scales.md).

## 8. Doing something with it

| To… | Do |
|---|---|
| Read the map | `out/capability-assessment-level.md`, or sheet 1 of the workbook |
| Record what you learned | Sheet 2 of the workbook, then `build.py ingest` |
| Ask the platform team something | Sheet 4, *In the box* — 27 questions, each a roadmap item |
| Brief a committee | `out/management-report.html`; `out/capability-assessment-exec.md` for the coarser lens |
| Answer the agent claim | `out/agent-readiness.md` — generated from `facts/questions.json` |
| Answer a new *"can we do X?"* | Add an entry to `facts/questions.json`; a page appears on the next build |
| Check what may leave the Bank | `out/provenance.md` |

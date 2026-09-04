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

A fact is true whichever framework reads it. So you can run two scales over the same
evidence, and they cannot disagree about what is true — only about what to make of it.

## 3. The four observations

Per capability, four questions. Each answered `yes` / `partial` / `no` / `n/a` / `unknown`,
each with evidence and a name attached.

| | The question | Who usually answers |
|---|---|---|
| **Practised** | Is this done on real AI systems in production, repeatedly? **Asked once per L3 criterion** (ADR-0014) | The capability owner |
| **Enabled** | Can a team get the tooling without building it themselves? | The platform team |
| **Skilled** | Do the people who must do this know how? | The owner, or L&D |
| **Defined** | Is there an approved institutional standard, policy or method? | Whoever owns the subject: the platform team, Cybersecurity, Data Management, Legal, HR, EA |

Two values carry weight people usually miss:

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

| Observation | Value | Evidence |
|---|---|---|
| Practised | partial | 4 agents built on Foundry; 1 has written guardrails |
| Enabled | partial | Foundry agents offering, 6 of 8 assets released |
| Skilled | unknown | Nobody has looked |
| Defined | partial | Foundry Agents Standard is **pre-release** |

**Level 1 — Performed.** *"Performed on some AI systems but not repeatably."*

And the sentence that lands in the room: *the platform is strong, the standard is nearly
there, and the practice is thin. The fix is not to buy anything — it is to release two
documents and build the next agent against them.*

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

### Practised is asked at L3, and derived at L2

The other three observations are properties of tooling, people and standards, and are
answered once per capability. `practised` is different: *"is 4.4 Agent & Workflow
Orchestration Design practised?"* covers six distinct practices, and the Bank plausibly
does some and not others. So it is asked once per **criterion** — a named practice with
a definition, answerable by looking — and the capability value is rolled up from those
answers.

The rule is strict: every applicable criterion `yes` gives `yes`; any weak link gives
`partial`; `unknown` criteria drop out rather than un-rating the whole capability. One
weak link stops the claim, which is the same asymmetry the level ladder enforces.

That turns *"4.4 is partial"* into *"4.4.1 and 4.4.6 yes, 4.4.5 no, three unexamined"* —
and the roadmap item becomes a named practice rather than a vague improvement.
See [ADR-0014](decisions/adr/0014-practised-is-observed-at-l3.md).

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

Of 52 capabilities: about a dozen are realised by enterprise services the Bank already
runs, four are purely organisational, and the rest are governance and practice
capabilities where tooling is at most a form in a GRC system. For all of these, `enabled`
is `n/a` with a reason, and the level rests on the other three observations.

Forcing a supply number onto a strategy capability is how a model starts producing
nonsense that nobody trusts.

## 6. What replaced what

Earlier versions carried **two scales** — maturity on a capability, readiness on a
realization — that were never to be merged. The distinction was real, but it could not
be held in a room, and it required 52 rubrics and 258 typed criteria that were never
going to be written.

This model keeps the fact that distinction was protecting, structurally instead of by
convention: **supply alone cannot produce a level**, because `enabled` contributes
nothing without `practised`. What was two numbers is now one derived level and four
visible columns, and the columns are where the argument belongs.

See [ADR-0013](decisions/adr/0013-facts-and-scales.md).

## 7. Doing something with it

| To… | Do |
|---|---|
| Read the map | `out/capability-assessment-level.md`, or sheet 1 of the workbook |
| Record what you learned | Sheet 2 of the workbook, then `build.py ingest` |
| Ask the platform team something | Sheet 4, *In the box* — 27 questions, each a roadmap item |
| Brief a committee | `out/capability-assessment-exec.md` — the coarser lens |
| Answer the agent claim | `out/agent-readiness.md` |

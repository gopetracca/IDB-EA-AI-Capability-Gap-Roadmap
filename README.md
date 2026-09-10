# Enterprise AI Capability Model

**Inter-American Development Bank**

A model of what the institution must be able to do with AI, what it has actually built,
and the distance between the two — expressed so that the answer can be checked rather
than argued about.

| | |
|---|---|
| **The walkthrough** | [`out/walkthrough.html`](out/walkthrough.html) — the deck: map, observations, scale, first round. Open in a browser, arrow keys |
| **The map** | [`out/capability-map.md`](out/capability-map.md) — the taxonomy alone: 8 domains, 52 capabilities, 258 criteria, no scores attached |
| **The report** | [`out/management-report.html`](out/management-report.html) — open in a browser |
| **What it will look like** | [`out/management-report-illustrative.html`](out/management-report-illustrative.html) — the same report, every chart populated with **sample observations** |
| **The worked example** | [`out/agent-readiness.md`](out/agent-readiness.md) — *"can we run AI agents?"* |
| **The detail** | [`out/capability-assessment-level.md`](out/capability-assessment-level.md) — all 52 capabilities, 258 criteria, with what has been observed |
| **Where the map comes from** | [`out/provenance.md`](out/provenance.md) — sources by grade, and what cannot leave the Bank |
| **All the documentation** | [`docs/README.md`](docs/README.md) — **start here**, it says what to read in what order |
| **How it works inside** | [`docs/how-it-works.md`](docs/how-it-works.md) |
| **How to start assessing** | [`docs/first-round.md`](docs/first-round.md) |

---

## 1 · The problem this exists to solve

Inside the institution, two people say opposite things about the same capability.

> *"We cannot run AI agents."*
>
> *"Of course we can — the platform, the standards, the reference architectures and the
> infrastructure modules are all published."*

Both are telling the truth, about different things. One is describing whether the work is
**done**; the other is describing whether the means to do it **exist**. A model that
answers with a single number has to pick one of those meanings, and whichever it picks,
the other conversation loses its evidence.

That disagreement is not unique to agents, and it is not unique to this institution. It
is the standard failure of AI capability assessment: **supply gets reported as ability**,
because supply is the easier thing to establish and the more pleasant thing to report.

This model is built so that both statements can be true at once, visibly, with the
evidence attached to each.

## 2 · What it is

Three things, and the separation between them is the whole design.

**A capability map.** 8 domains, 52 capabilities, 258 criteria. What the institution must
be able to do with AI, stated so that each capability has one accountable owner. It is
vendor-neutral and survives replacing every product.

**A register of what exists.** 7 platform offerings and 20 named assets — standards,
reference architectures, templates, infrastructure modules — each with a status and a
location a reader can open. This is the part that is not an opinion.

**Four observations**, each recorded as a fact with evidence and a date. Three are asked
once per capability; **practised is asked once per L3 criterion**, because that is the
level at which work is actually witnessed, and the capability value is derived from
those answers rather than typed:

| | The question | Typically answered by |
|---|---|---|
| **Practised** *(per criterion)* | Is this specific practice done on real AI systems, repeatedly? | The capability owner |
| **Enabled** | Can a team get the tooling without building it themselves? | The platform team providing it |
| **Skilled** | Do the people who must do this know how? | The owner, or Learning & Development |
| **Defined** | Is there an approved institutional standard, policy or method? | Whoever owns the subject |

**Nobody types a level.** A level is derived from the four observations by a rule that is
written down and can be argued with separately from the facts it reads. Three such rules
ship: the default scale, adapted from ISO/IEC 33020, and two lenses for rooms that already
hold an executive or a maturity frame. Where a lens and the default disagree, the default
is the finding.

### Who this is a model of

Every function that touches AI, not one of them. Of the 52 capabilities, the AI platform
team owns 14, Data Management 4, Cloud and Infrastructure 4, Core Platforms 4, Strategic
Portfolio Management 3, Enterprise Architecture 2, and Cybersecurity, Legal, HR, Risk,
Audit and others hold the rest. **Eight are owned by nobody**, which is itself one of the
findings.

The same distribution applies to the observations. A standard for AI security is set by
Cybersecurity, one for AI data governance by Data Management, one for AI literacy by
Learning & Development. Architecture sets some and not most.

## 3 · What it is for

| Question | Where it is answered |
|---|---|
| Are we ready to do *X* with AI? | The four observations for the capabilities *X* touches |
| Why do people disagree about whether we have a capability? | The columns separate *built* from *done* |
| What should we fund next? | Capabilities with no tooling and no reason recorded; assets finished but unreleased |
| Who owns this? | The owner mapping, against the institution's own catalogue |
| What do we tell an auditor? | Every observation carries evidence, a source and a date |
| Are we behind? | Only where an observation says so. Elsewhere the model says *unknown* rather than guessing |
| Can we say this outside the Bank? | The provenance view: which capabilities rest on a source a reviewer cannot open |

## 4 · How it relates to what exists in the market

Three families of instrument exist, and this model is deliberately none of them.

**Analyst maturity assessments** (the major research firms) are self-assessed
questionnaires producing a current and target score per capability, benchmarked against
peers. They are excellent at executive framing and peer comparison, and they are
licensed, coarse — typically around 25 capabilities — and thin underneath: the score
rests on a judgement made in twenty minutes, with no evidence recorded and nothing an
auditor can follow.

**Cloud provider adoption frameworks** (the hyperscalers) are structured to sell and
sequence adoption of a particular platform. Useful checklists, not neutral, and they
cannot describe a capability that no product realises.

**Process assessment standards** (the ISO/IEC 330xx family, and CMMI before it) are the
opposite: rigorous, evidence-gated, ordered so that performance precedes definition — and
built for software *processes*, with no AI content at all.

**This model takes the measurement discipline from the third and applies it to a
capability map built for AI.** Its default scale is adapted from ISO/IEC 33020, which is
where the ordering comes from: a published standard with nothing performed against it
earns no level, because the question was never *did we write it down*.

What it adds that none of them has: **the facts are separate from the judgement.** An
observation such as *"the agents standard is pre-release"* is true whichever framework
reads it. So the same evidence can be reported through a different frame — including an
analyst frame, if that is what a committee already knows — without reassessing anything
and without the two versions being able to contradict each other on the facts.

What it does not do: benchmark against peers. No comparable dataset exists, and inventing
one would undo the point.

## 5 · What the model says today

**No capability is rated**, and the report says so on its first page. A rating requires
knowing whether something is *practised*, and that question has not yet been put to the
capability owners.

What is established is substantial and evidenced (figures as of 4 September 2026; the
report carries the live ones):

| | |
|---|---|
| Platform offerings with named assets behind them | 7 |
| Assets recorded with status and location | 20 |
| Assets finished but not yet released to teams | 5 |
| Capabilities nobody in the institution's catalogue claims | 8 |
| Questions outstanding for the platform teams | 27 |
| Capabilities where nobody has yet asked whether tooling exists | 24 |

The finding those support: **the institution has built its enablers ahead of its
practice.** That is the explanation for the disagreement in section 1, and it names its
own fix.

The distinction the model refuses to blur is between *we do not know* and *we do not have
it*. Most assessments cannot tell those apart and score an unexamined capability as if it
were absent. This model records `no` only as an evidenced negative; a register that was
searched and had nothing stays `unknown` until the owner is asked.

## 6 · How a report is produced

There is no writing step. The report is generated from the recorded facts, so it cannot
drift from them, and re-running it after new observations produces a new report rather
than a new draft.

```
facts          →   scale          →   report
what is true       how we judge       what we tell people
```

1. Someone answers a question — a capability owner, a platform team, Cybersecurity.
2. The answer is recorded as an observation, with evidence, a name and a date.
3. `uv run python build/build.py all` validates the facts, then regenerates the workbook and
   every view. Nothing is built from facts that fail validation.

Recording happens in a workbook: send it, the reviewer fills in the yellow cells, it comes
back, and one command reads it in. Full instructions in
[`docs/using-the-model.md`](docs/using-the-model.md).

**Four questions would change what the next report can say**, and none requires new
tooling or new investment:

| Who | What is asked |
|---|---|
| Capability owners | Is this done on real AI systems, and where? |
| Platform teams | The 27 in-the-box control questions |
| Cybersecurity, Data Management, Legal, HR | Does an approved standard exist in your domain? |
| Learning & Development | Who is trained, and in what? |

## 7 · Layout

| Directory | What it is |
|---|---|
| [`facts/`](facts/README.md) | The model. What is true, with evidence and dates. Schemas in its README |
| [`scales/`](scales/README.md) | Rules that turn observations into a level. The contract a scale must keep |
| [`out/`](out/README.md) | Generated reports, views and the workbook. Never edited |
| [`build/`](build/README.md) | Seven modules. One command |
| [`tests/`](tests/) | The rules the documentation promises, as tests |
| [`docs/`](docs/README.md) | Explanations, decisions, provenance, analysis. Its README is the reading path |
| [`review/`](review/README.md) | Returned workbooks, dated, never edited |
| [`archive/`](archive/README.md) | Superseded work, kept and explained |

**The one rule:** `facts/` is edited, `out/` is generated. A finding is never fixed by
editing a report. Derived values — release counts, the capability's *practised*, every
level — are computed, never stored.

## 8 · Handling

- Licensed analyst material is usable internally, never reproduced externally, and never
  cited as a source here.
- Sources are graded by whether a reviewer can open them. The lowest grade cannot support
  a claim that leaves the institution.
- Where something is our own construction rather than an adopted standard, it says so.
  See [`scales/README.md`](scales/README.md).

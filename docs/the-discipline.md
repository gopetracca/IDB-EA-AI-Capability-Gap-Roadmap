# The discipline behind the model

**Capability modelling, maturity assessment and heat maps — the theory, the lineage, and
how to defend what we built.**

Inter-American Development Bank · Enterprise Architecture
Written 9 September 2026 · hand-written, so its figures are a snapshot; the live ones are
in [`../out/`](../out/README.md)

> ### ⚠ Handling
>
> This page names paywalled standards, describes the shape of licensed analyst
> instruments, and quotes this repository's own handling rules. Before any of it
> circulates outside the Bank, read §16. Three rules bind everywhere in it: **do not quote
> ISO/IEC 33020's N-P-L-F percentage bands or its exact capability level rule**; **do not
> attribute the maturity ladder to any institution's model**; **do not reproduce licensed
> analyst wording**.

---

## How to read this

This is a primer, not a specification. It exists so that you can hold a room against
someone who has done thirty of these engagements, and so that when you are challenged you
answer from the theory rather than from the artifact.

It is in three parts, and they are meant to be read in order once and then used out of
order forever.

| | | Read it when |
|---|---|---|
| **Part I** | §1-§7 — the field: where capability thinking comes from, how maturity assessment became a discipline, the measurement theory underneath it, and what AI changed | You are ramping up, or someone has asked a *why is it done this way* question |
| **Part II** | §8-§9 — the market: the three families of instrument, and how a consulting engagement actually runs | You are being compared to an analyst model, or you are about to sit opposite one |
| **Part III** | §10-§16 — ours: every design decision with its warrant, the objection drill, and what we concede | You are presenting, defending, or being audited |

Nothing here is binding. The binding records are the ADRs in
[`decisions/`](decisions/README.md). Where this page and an ADR differ, the ADR is right.
Where this page and a generated view differ, the view is right.

---
---

# Part I — The field

---

## 1. Where capability thinking comes from

### 1.1 The problem it was invented to solve

Every large organisation has the same recurring failure: it plans by **what it owns**
(systems, teams, budgets, vendors) and then discovers it cannot say **what it can do**.
The two are not the same, and the gap between them is where transformation programmes die.

Ask *"can we run AI agents?"* of an organisation that plans by ownership, and the answers
that come back are a platform name, a team name and a budget line. None of them answers
the question. The question is about **ability**, and ability is not a possession.

Capability thinking is the response: introduce a layer of description that names abilities
directly, holds still while everything underneath it churns, and can be planned against.

### 1.2 The lineage, briefly

The idea has two origins that converged.

**Defence planning.** Post-Cold-War defence ministries faced an adversary they could no
longer name, which broke a planning method built on *threat-based* planning — size your
forces against a specific opponent. The replacement was **capability-based planning**: state
the effects you must be able to achieve, under stated conditions, to a stated standard, and
then work out what force mix delivers them. The vocabulary of *capability*, *capability gap*
and *capability increment* comes from there, and it carries an assumption worth keeping: a
capability is defined by an **outcome under conditions**, not by an asset.

**Enterprise architecture.** The same idea arrived in business architecture through the
1990s and 2000s and became formalised in the 2010s. The Open Group publishes it as TOGAF
Series Guides — **G193** *Capability-Based Planning: Supporting Project/Portfolio and
Digital Capabilities Mapping Using the TOGAF® and ArchiMate® Standards* (16 July 2019),
**G211** *Business Capabilities* (Version 2, superseding G189) and **G233** *Business
Capability Planning* (11 April 2023, part of the TOGAF Standard 10th Edition). The Business
Architecture Guild's BIZBOK carries a parallel treatment. Our register records the TOGAF
Standard as **S20** and the capability-based planning guide as **S21**, both grade B.

> **The one-sentence version to say out loud:** *capability-based planning was invented
> because you cannot plan against an adversary, or a technology, that you cannot name in
> advance — so you plan against the abilities you must have either way.* That is exactly
> the position an institution is in with AI.

### 1.3 The stability argument — why the layer earns its keep

A capability layer is worth maintaining only if it is **more stable than the things it
describes**. This is the whole justification, and it is the answer to *"why not just list
our systems?"*

| Layer | Half-life | Changes when |
|---|---|---|
| Product / vendor | 1-3 years | Procurement, market, a licence renegotiation |
| System / application | 3-7 years | A replacement programme |
| Process | 5-10 years | A reorganisation or a redesign |
| **Capability** | **10-20 years** | **The mission changes** |
| Organisation chart | 1-3 years | A new executive |

*Knowledge Access & Retrieval* was a capability before anyone had heard of a vector index
and will still be one after vector indexes are unfashionable. **Azure AI Search is a
realisation of it.** If the map named the product, the map would have to be rewritten on a
procurement cycle, and every historical assessment would become uncomparable.

This is also the answer to the vendor-neutrality obligation a public institution carries.
A capability map lets you ask *does what we have deliver access-trimmed retrieval to the
standard we need, and what else could?* — a design question. Without it, the same
conversation is *should we buy this product?* — a procurement question with one supplier in
the room.

### 1.4 The four things a capability is not

Most bad capability maps are a different thing wearing the word.

| Not a… | Tell | Why it fails |
|---|---|---|
| **Organisation unit** | Boxes match the org chart; renaming a department renames the map | Re-orgs invalidate the assessment. And it hides capabilities nobody owns — which are the findings you most need |
| **Process** | Boxes are verb phrases in sequence: *intake → build → deploy* | A process is *one way* of delivering a capability. Naming the process freezes the design |
| **System or product** | Boxes are product names, or thin abstractions over them | The map becomes a licence inventory, and the ability to say "we could do this differently" is gone |
| **Project or programme** | Boxes are things currently being funded | The map ends when the funding does; capabilities you are *not* investing in disappear, which is the opposite of a gap analysis |

Our own guard against the first is **ADR-0006**: the 8 domains are declared *reporting
clusters, not a lifecycle*. That ADR exists because the pull toward a lifecycle is
constant — someone always wants D2 to come before D4 — and a lifecycle map cannot express
the fact that governance runs alongside everything.

### 1.5 The three tests a capability line must pass

Use these when someone proposes a new box. They are the practical form of everything above,
and they are the same three that **ADR-0015** applies:

1. **The owner test.** Can one accountable person be named who would accept being rated on
   it? If the honest answer needs six names, it is a heading, not a capability.
2. **The vendor test.** Does the sentence survive replacing every product involved? If it
   does not, you have named a realisation.
3. **The landing test.** Is there a plausible failure that would land here and nowhere
   else? If every failure you can imagine lands somewhere that already exists, you have a
   criterion, not a capability.

**All three must coincide.** ADR-0015 states this explicitly, and it is what stopped the
agentic review from adding a dozen capabilities where three were warranted. Where only one
or two hold, the right answer is a **criterion** (a witnessable practice under an existing
capability), an **offering** (something the platform provides), or a **question** (a
recorded *can we do X?*). Modalities — speech-to-text, OCR, translation — fail the owner
test and the landing test, and are recorded as offerings.

---

## 2. How a capability map is built, and how it goes wrong

### 2.1 The decomposition rules

A map is a tree, and the tree has to obey rules or it becomes an argument.

**MECE — mutually exclusive, collectively exhaustive.** The convention comes out of
McKinsey and is attributed to **Barbara Minto**, who developed it while at the firm; in the
firm's own alumni interview she claims the coinage and traces the underlying idea to
Aristotle. *Mutually exclusive*: no ability appears in two boxes, because if it does, two
owners will each assume the other has it. *Collectively exhaustive*: at each level, the
children fully account for the parent, because a decomposition with a hole produces a
roadmap with a hole.

In practice MECE is an aspiration at L1 and a discipline at L2. Domains overlap at the
edges — AI security genuinely touches engineering — and the honest response is to place
each ability in **one primary home** and cross-reference, rather than to duplicate. That is
our ADR-0006 rule.

**Levelling — each level answers a different question.** This is the part most maps get
wrong, and it is where our design is unusually strict:

| Level | Answers | Reader | Carries |
|---|---|---|---|
| **L1 domain** | *Where do I look?* | Leadership. 8 boxes fit on a slide | Nothing. Never scored |
| **L2 capability** | *Who owns this, and is it established?* | The working tier | The four observations, and the level |
| **L3 criterion** | *What exactly would I go and look at?* | The assessor and the owner | `practised`, and nothing else |

A level that answers two questions at once is the commonest structural defect. If L2 boxes
are sometimes broad themes and sometimes specific practices, no rating at L2 means anything,
because the boxes are not comparable.

### 2.2 Granularity — the question you will be asked most

*"Isn't 55 too many?"* is the standard challenge, and the standard bad answer is to defend
the number. Defend the **tests** instead; the number is a consequence.

Granularity is right when:

- **Every box passes the owner test.** This sets the *floor* on granularity. If a box needs
  six owners, split it. This single rule does most of the work.
- **The answer to "is this established?" is not always "partially".** This is the *ceiling*
  test in reverse. If every honest answer at your resolution is *partially*, the resolution
  is too coarse to produce a finding. *"Partially"* is not a finding; it is a shrug.
- **A gap can be stated as a sentence someone can be given.** *"Improve agent
  orchestration"* is not fundable. *"Termination and loop control has never been done"* is.
- **A box does not need a paragraph to be understood by its owner.** If it does, it is two
  capabilities.

The shapes that recur across published models — roughly **6-10 at L1, 40-70 at L2, and
200-350 at L3** — are not a convention anyone agreed. They are what the owner test and the
one-slide constraint produce independently in most large organisations. Ours lands at
**8 / 55 / 281**. Analyst models land near **7 / 25** because they are optimised for a
board conversation, where the owner test is not applied.

### 2.3 The anchoring problem

A new capability map almost never lands on empty ground. The institution has an existing
enterprise capability map, and the new one has to be related to it or it will be rejected as
a parallel universe.

Three relationships are possible, and ours are recorded as the `anchor` field:

| Anchor | Means |
|---|---|
| `specialization` | This is the AI-specific form of a capability the Bank already names |
| `new` | The Bank's map has no counterpart; this is genuinely new ground |
| `lens` | This cuts across several existing capabilities rather than sitting under one |

**Ours are provisional and say so** — that is **ADR-0007**, and 14 of 55 are `lens`, the
weakest and least verified relationship. The ADR's own instruction is to **carve anchoring
out of any approval request** until a control mapping exists. Volunteering that is
disarming; being caught on it is not.

### 2.4 Confidence in the *line*, not in the Bank

A distinction almost no published model makes, and one of the better things in ours.

**ADR-0009** says the taxonomy is validated *before* anything is scored against it, and
each capability carries a `confidence` field. That field is **a measure of the map, not of
the institution**: it says how much we trust this line's name, boundary and definition.
The three capabilities ADR-0015 added carry `confidence: low` because they are new and have
not survived a challenge round yet.

Keeping the two separate matters because otherwise every conversation about *"is this box
right?"* becomes a conversation about *"are we bad at this?"*, and the second one is much
harder to have honestly.

### 2.5 The six ways a capability map goes wrong

Recognise these on sight. Five of the six are visible in maps you will be shown.

| Failure | What it looks like | What it costs |
|---|---|---|
| **The org mirror** | L1 domains match departments | Dies at the next re-org; unowned capabilities are invisible |
| **The product mirror** | Boxes are platforms with the vendor name filed off | Every architecture question becomes procurement |
| **Verb soup** | Every box is a verb phrase — *deploy, operate and scale AI* | Verb phrases hide multiplicity. One verb, six owners |
| **Orphan boxes** | Boxes nobody will accept | The rating is uncontested because nobody contests it, and unfundable |
| **Level drift** | L2 boxes at wildly different resolutions | Ratings not comparable; the heat map is meaningless |
| **Taxonomy theatre** | A beautiful map, never assessed | The commonest of all. A map with no observations is a diagram |

We carry a structural guard against the last one: **not rated is a result**, printed on the
first page of the report, rather than an empty map quietly rendered as a good one.

---

## 3. Maturity assessment: the lineage

You will be asked *"where does your scale come from?"*, and the answer needs to start
further back than our repository.

### 3.1 The chain, with dates

| When | What | Why it matters here |
|---|---|---|
| **1979** | **Philip Crosby**, *Quality Is Free* — the **Quality Management Maturity Grid**: five stages (Uncertainty · Awakening · Enlightenment · Wisdom · Certainty) across six management dimensions | The origin of the whole convention. Five stages, and — importantly — **stages assessed across several dimensions**, which is the shape every model since has copied |
| **1989** | **Watts Humphrey**, *Managing the Software Process* | Carried Crosby's grid into software process |
| **1991** | **SEI Capability Maturity Model v1.0** (Carnegie Mellon; Paulk, Curtis, Chrissis) — five levels: Initial · Repeatable · Defined · Managed · Optimizing | The model everyone means when they say "maturity level". v1.1 followed in 1993 |
| **1998-2004** | **ISO/IEC 15504** (*SPICE*) — process assessment as an international standard | Where the *process attribute* idea and the continuous representation were standardised |
| **2000s** | **CMMI** — CMM Integration, merging several CMMs | Introduced the distinction in §3.2, which people conflate constantly |
| **2015** | **ISO/IEC 33001:2015** supersedes 15504-1; the **330xx family** replaces the 155xx family | 15504 is **withdrawn**. Citing it as current is a tell that someone is working from memory |
| **2019-11** | **ISO/IEC 33020:2019**, second edition — the process **measurement** framework; cancels and replaces the 2015 edition | **What our default scale is adapted from** |
| **2023-04** | **CMMI V3.0**, published by the CMMI Institute, part of **ISACA** | CMMI is no longer an SEI product. Saying "the SEI's CMMI" dates you by a decade |

Two of these are load-bearing for us and worth memorising exactly: **ISO/IEC 15504 is
withdrawn and superseded by the 330xx family**, and **the standard we adapted is
ISO/IEC 33020:2019, second edition.**

### 3.2 The distinction everyone conflates: capability level vs maturity level

In CMMI these are two different instruments, and confusing them is the fastest way to lose
credibility with anyone who knows the field.

| | Rates | Range | Answers |
|---|---|---|---|
| **Capability level** | **One** process area / practice area | 0-3 in CMMI V3.0 | *How well do we do this particular thing?* |
| **Maturity level** | A defined **group** of practice areas, for an organisational unit | 0-5 | *What stage is this organisation at, overall?* |

These correspond to the two **representations**:

- **Continuous** — improve the handful of areas the business actually cares about, each on
  its own capability level. Comparison between organisations is area by area.
- **Staged** — a prescribed grouping and ordering; you achieve maturity levels in sequence.
  This is what a customer or a contract demands when it says "we require a CMMI Level 3
  supplier".

**Ours is a continuous-style instrument.** We rate each capability independently, on its own
level, with no organisation-wide roll-up and no prescribed ordering. There is **no
institutional maturity level** in our default scale, deliberately — because a single number
for "the Bank's AI maturity" would be an average over 55 ordinals, which §4.2 explains is a
category error, and because it would hide exactly the variation the roadmap needs.

> **When someone asks "so what level is the Bank at?"**, the answer is: *that question has
> no form in this model. We rate capabilities, not the institution. Here are the 55, and
> here is where the mass sits.* Then show the distribution. If they insist on one number,
> the executive lens exists for that room — and it says on its face that it averages.

### 3.3 What a process attribute is, and why the ordering is the interesting part

ISO/IEC 33020 measures a process not by asking *"are you level 3?"* but by asking whether
specific **process attributes** are achieved, and then deriving a level from which
attributes hold. The attributes are ordered:

| Level | Attribute | In plain words |
|---|---|---|
| 1 | **PA 1.1** Process performance | The process purpose is achieved |
| 2 | **PA 2.1** Performance management — including that resources are determined, provided and maintained, and that persons performing it are competent | Someone provides the means and the people are capable |
| 2 | PA 2.2 Work product management | |
| 3 | **PA 3.1** Process definition, **PA 3.2** Process deployment | A standard process exists and is deployed |
| 4 | Quantitative measurement | Measured against thresholds |
| 5 | Innovation | An improvement cycle closes |

**The ordering is the borrowing that matters.** Performance is Level 1. A defined process
is Level 3. So a published standard with nothing performed against it earns **no level at
all**.

That is counter-intuitive to almost everyone in a room, because the standard usually *is*
written first. §11.4 has the full answer; the short one is that the ladder orders **claims**,
not activities, and *"we do this against an approved standard"* is a strictly stronger claim
than *"we do this"* — and it needs the doing.

This ordering is also the single most useful thing about borrowing from a process
assessment standard rather than inventing a ladder. It is what stops *"we approved the
technology"* from reading as *"we have the capability"*, and it is the reason the Bank's
headline finding — **the enablers were built ahead of the practice** — is even expressible.

### 3.4 What a *rating* formally requires

Worth knowing because it is what an ISO assessor would ask, and because it marks the
boundary of what we claim.

A conformant process assessment under the 330xx family involves a **defined assessment
process**, a **competent assessor**, a **documented process assessment model**, an
**evidence base** with a defined sampling approach, and **recorded ratings with
traceability**. It produces a rated process profile that can be compared and, in some
schemes, certified.

**We are not doing that, and must never say we are.** We have adapted the measurement
framework's ladder and ordering into an instrument of our own. The honest sentence is in
[`where-the-scales-come-from.md`](where-the-scales-come-from.md) §7 and is worth learning
close to verbatim:

> *Nothing here claims to be an ISO assessment, and no capability is rated against a clause
> we have not opened.*

What we do have that a typical maturity assessment does not: **every rating traces to an
observation with evidence, an observer and a date**, and the rule that turns observations
into a level is code that runs over all 625 value combinations and is tested. That is a real
assurance position, just not a certified one.

### 3.5 The one thing you must not quote

**ISO/IEC 33020:2019 is paywalled (grade C), and its published preview stops before clause
5.3.** Two things therefore rest on secondary sources describing the *superseded* ISO/IEC
15504 and **must not be quoted**:

- the **N-P-L-F percentage bands**
- the **exact capability level rule**

Verified from the preview and safe to cite: the six-point scale 0 Incomplete → 5
Innovating, the process attribute identifiers and names, PA 2.1's resource and competence
outcomes, and that the second edition cancels and replaces the 2015 edition.

**Cite the scale by name, and the levels by clause. Never the percentages.** Closing this
needs someone to open the standard through the Bank's ISO subscription —
[OPEN-ITEMS](../OPEN-ITEMS.md) #10.

---

## 4. The measurement theory consultants skip

This section is why you will win arguments. Almost nobody selling a maturity assessment can
have this conversation.

### 4.1 Stevens' scale types

**S. S. Stevens, "On the Theory of Scales of Measurement", *Science* 103 (2684), 677-680,
1946.** Four scale types, each permitting different operations:

| Scale | You may say | You may compute | Example |
|---|---|---|---|
| **Nominal** | *same / different* | Mode, counts | Owner name, domain |
| **Ordinal** | *more / less* | Median, percentile, counts per level | **Maturity levels. Ours.** |
| **Interval** | *how much more* | Mean, standard deviation | Temperature in °C |
| **Ratio** | *how many times more* | All arithmetic | Cost, headcount |

**A maturity level is ordinal.** Level 3 is higher than Level 2. It is *not* one unit above
it, it is *not* 1.5 times Level 2, and the distance from 1 to 2 is not the distance from 2
to 3. In our default scale the 1→2 step requires three observations to move and the 2→3
step requires one — the rungs are visibly unequal, which is a concrete demonstration that
the numbers are ranks wearing digits.

Stevens' framework has been criticised and extended since 1946, and it is not a law of
nature. But it is the shared vocabulary, and the specific error it names is the one that
matters here.

### 4.2 Why averaging ordinals is a category error

*"What's our average maturity?"* is asked in every one of these meetings. The mean of
Level 2 and Level 4 is not Level 3, because the arithmetic requires interval distances that
an ordinal scale does not have. Worse, the average is **not actionable**: nothing anyone can
be given follows from 2.7.

Three failure modes follow from averaging:

- **It manufactures precision.** 2.7 implies a resolution the evidence cannot support.
- **It hides the distribution.** *Two at 3 and two at 1* averages the same as *four at 2*,
  and they are completely different institutional situations with completely different
  roadmaps.
- **It rewards breadth over depth.** Raising four capabilities from 1 to 2 moves the
  average as much as raising two from 1 to 3, though the second may be the only one that
  changes what the institution can do.

**So `capability_level.py` does not average, and `check` would not care if it did — the
discipline is ours to keep.** Report the **distribution**: how many at each level, and where
the mass sits.

**And yet our executive lens averages.** Deliberately. Here is why that is defensible and
not hypocrisy, in the form you should say it:

> *Averaging ordinals is formally wrong, and the default scale does not do it. The
> executive lens does, on purpose, because the question that room is asking — "how much of
> what we said we would do actually exists?" — is a question about proportion, and
> proportion is what an average expresses. The lens says on the face of every view that it
> averages and that it does not gate on performance. Where it disagrees with the default,
> the default is the finding.*

Two guards make that survivable, and both are worth knowing:

- **`n/a` and `unknown` drop out of the denominator** rather than counting as zeros.
- **A floor**: below two *scored* dimensions it declines to rate at all, because a fraction
  computed from one cell is not an average. Before that floor existed, a single `yes`
  produced a reported Level 5. That is a good story to tell, because it demonstrates that
  the failure mode is real and that we found it in our own instrument.

### 4.3 Missing data — the error that makes most assessments untrustworthy

This is the strongest single idea in our model and the one to lead with.

Most maturity instruments have **four states** — some variant of *no · partial · yes · n/a*
— and no way to say *nobody has looked*. Faced with an unexamined capability, the assessor
must pick one, and the pick is almost always the lowest. **The unexamined and the absent
become indistinguishable**, and the resulting picture systematically overstates how much is
known and how bad things are.

In survey methodology this is **treating missing data as a zero**, and the resulting
distortion is a **non-response bias**. It is not a subtle statistical point; it is the
difference between *we have a problem here* and *we have not asked here yet*, which are
different work items for different people.

Our five values exist to prevent it:

| Value | Means | Needs |
|---|---|---|
| `yes` | Done | Evidence |
| `partial` | Done in places, or incompletely — say where | Evidence |
| `no` | **An evidenced negative.** Someone looked and it is not there | Evidence, or a basis saying what was looked at |
| `n/a` | Does not apply here | A reason; for `enabled`, an entry in `enablement-context.json` |
| `unknown` | **Nobody has looked. Never a zero** | Nothing. It is the honest default |

**`no` and `unknown` are the pair that decides whether the model is trustworthy.** A
register that was searched and had nothing is `unknown` until the owner is asked, because a
standard owned by another function may exist and simply not be recorded here. Recording
that absence as `no` turns *we did not look* into *it does not exist*. That is
**ADR-0013 Amendment 2**, and we applied it to ourselves: **24 `enabled` rows were corrected
from `no` to `unknown` on 4 September 2026.** Say that out loud when you are challenged on
rigour — an instrument that has corrected itself against its own rule is a stronger claim
than one that has never been tested.

`n/a` carries the other half: a governance capability is not worse for having no tooling.
It drops out of the calculation rather than counting as a failure. **15 of 55 `enabled`
rows are `n/a` today**, each with a recorded reason.

### 4.4 Construct validity and reliability, at working depth

Two terms from measurement science that let you name what is wrong with a competing
instrument.

**Construct validity — does the instrument measure the thing it claims to measure?** A
questionnaire that asks *"do you have an AI strategy?"* measures whether a document exists.
It does not measure whether the institution can act strategically about AI. Most maturity
questionnaires have weak construct validity in exactly this direction: they measure
**artifacts** and report **abilities**.

Our answer is the four-observation split. `defined` measures the artifact, honestly and
separately; `practised` measures the doing; and the scale refuses to let the first stand in
for the second. **The construct being measured is named on the tin, per column.**

**Reliability — would two competent observers, working independently, record the same
thing?** This is where self-assessment instruments are weakest, and where you should press
when shown one. Ask: *what stops two people answering this differently?*

Our answers, and their limits:

| Device | What it buys | Its limit |
|---|---|---|
| **L3 criteria** | Two people arguing about *"is 4.4 practised?"* have no shared referent. Arguing about *"has termination and loop control been done?"* almost always converges | 281 criteria is a lot of asking |
| **Evidence required for every non-`unknown` value** | Disagreement becomes a comparison of evidence, not of impressions | Evidence quality is not itself graded |
| **`unknown` available** | Nobody is forced to invent an answer, which is the largest source of noise | |
| **Derived levels** | Two people cannot disagree about the level if they agree about the facts, because the level is code | They can still disagree about the rule — which is the argument we *want*, and it happens in one file |

**What we do not have** is a second observer. Every observation today has one, and
**inter-rater reliability has never been measured**. Concede this before it is found
(§13).

**Self-assessment bias** is the third term. Owners asked to rate themselves inflate,
predictably and without dishonesty, because they know the good instances and are less aware
of the tail. Every device above is a partial defence: evidence is harder to inflate than an
opinion, criterion-level questions are harder to answer generously than capability-level
ones, and the roll-up (§4.5) is built to lean the other way.

### 4.5 Asymmetry, on purpose

This is a design decision people often miss, and it is a good one to volunteer.

Our capability-level `practised` is **derived** from its criteria, and the rule is
deliberately not symmetric:

| The criteria say | The capability reads |
|---|---|
| Every one examined, every one `yes` | `yes` |
| Some `yes`/`partial`, **or any left unexamined** | `partial` |
| None `yes`/`partial`, at least one `no` | `no` |
| None examined | `unknown` |

`yes` requires a **complete** look. `no` does not: one examined `no` with the rest
unexamined still reads `no`.

**The justification is a cost argument, not a statistical one.** Under-claiming costs a
follow-up question. Over-claiming costs an incident, an audit finding, or a decision made on
a capability the institution does not have. Those are not symmetric risks, so the rule
should not be symmetric either. The record is **ADR-0014**.

The phrase to use: **one weak link stops the claim, and an unexamined criterion is never
counted as satisfied.**

### 4.6 Evidence-gating changes what kind of instrument you have

A last framing that is worth having ready, because it reframes the whole comparison in
Part II.

There are two species of maturity instrument:

| | **Rubric instruments** | **Evidence-gated instruments** |
|---|---|---|
| How a level is set | Read the paragraph describing Level 3, decide whether it feels like you | Record what is true; a rule derives the level |
| Judgement lives | Inside the instrument, fused with the description | In one file, separable from the facts |
| Changing your mind about measurement | Reassess everything | Change the rule and rebuild. **No fact changes** |
| Two frames at once | Impossible — the frames disagree about the evidence | Routine — same facts, different rule |
| Audit trail | The assessor's judgement | Observation → evidence → observer → date |
| Cost | Hours | Weeks |

Most published models — and every analyst self-assessment — are rubric instruments. Ours is
evidence-gated. **That is the single structural difference from which almost every other
difference follows**, including the ones people complain about (it takes longer; most of it
is `unknown` today).

---

## 5. Gap analysis, target state and roadmapping

A capability assessment that stops at "here is where we are" has done half a job. The other
half has its own theory, and its own standard mistakes.

### 5.1 Current, target, gap

The classic triptych. Two of the three are usually done badly.

**Current state** is the assessment. Ours.

**Target state** is where most assessments quietly fail: they set every capability's target
to the top of the scale. That is wrong on three counts.

- **It is unaffordable**, so it is ignored, so the whole artifact loses force.
- **It is incorrect.** Not every capability should be Level 3. A capability that is rarely
  exercised, low-consequence and cheap to redo does not warrant an approved institutional
  standard and the conformance overhead that comes with it.
- **It removes the only interesting decision.** Choosing which capabilities warrant
  investment *is* the strategy. A target state of "all 5s" is the absence of a strategy
  wearing its clothes.

**Target-setting should be driven by criticality**, and criticality has recognisable inputs:
regulatory exposure, consequence of failure, frequency of exercise, degree of
irreversibility, and how many other capabilities depend on it. In our model these are not
yet recorded — a target-state layer does not exist, which is a real limitation to concede
(§13).

**Gap** is then the *distance between current and target*, per capability — not the
distance from the top of the scale. This distinction is worth being pedantic about, because
"gap to Level 3" and "gap to target" produce different roadmaps and only one of them is a
plan.

### 5.2 Gap, finding, recommendation — three different objects

Sloppiness here is why assessment decks fail to produce action.

| | Is | Example |
|---|---|---|
| **Gap** | A measured distance | *4.4 is at Level 1; the target is 3* |
| **Finding** | An interpretation of one or more gaps, with a cause | *The enablers were built ahead of the practice* |
| **Recommendation** | A piece of work with an owner and a cost | *Release STD-07 and RA-05; build the next agent against them* |

An assessment produces gaps automatically. **Findings require a human**, and are the actual
professional contribution. Recommendations require the finding plus knowledge of what the
institution can absorb.

The best test of a finding is that **it names its own fix**. *"The enablers were built
ahead of the practice"* does: it says stop building enablers, start practising. *"AI
maturity is low"* does not.

### 5.3 Sequencing — dependencies, not levels

The naive roadmap sorts by gap size and funds the biggest gaps first. This is almost always
wrong, because capabilities are not independent.

The right first cut is **enabler dependency**: which capabilities must move before others
*can* move. If retrieval evaluation cannot be done until an evaluation harness exists, no
amount of funding on the first moves it. In our model, this is what the offerings and
assets registers give you — a capability whose enabling assets are *finished but unreleased*
is a cheap move; a capability with no offering at all is an expensive one.

Second cut: **cheapness of the observation**. Where the model says `unknown`, the next step
costs a conversation, not a programme. Our current position is an extreme case of this —
see §5.4.

Third cut: **criticality**, per §5.1.

A useful and slightly contrarian point for the room: **the technical layer is the only part
that moves inside a year.** Strategy and culture capabilities move on a five-to-ten-year
clock. A roadmap assembled only from strategy capabilities has nothing to deliver in the
first two quarters, which is exactly when it must show progress.

### 5.4 The cheapest roadmap item is a question

Our model today says **`practised` is `unknown` for all 281 criteria**, and therefore every
one of the 55 capabilities is **not rated** under the default scale and the maturity lens.

That is not a failure of the model; it is the model refusing to guess. And it makes the
first roadmap trivially cheap to state:

| Who | What is asked | What it unlocks |
|---|---|---|
| Capability owners | Per criterion: is this done on real AI systems, and where? | Every level. Nothing rates without it |
| Platform teams | The 27 in-the-box questions | The agent answer, and most of `enabled` |
| Cybersecurity, Data Management, Legal, HR | Does an approved standard exist in your domain? | `defined`, currently `unknown` for 41 of 55 |
| Learning & Development | Who is trained, and in what? | `skilled`, currently `unknown` for all 55 |

**None of it requires new tooling or new investment.** That is the strongest thing you can
say about a roadmap, and it is true of ours because we have not yet spent the cheap moves.

---

## 6. Heat maps and the visual grammar

A heat map is the artifact everyone remembers from the deck, which makes it the artifact
most likely to be wrong in a way nobody notices.

### 6.1 What a heat map is actually for

**Pattern-finding across a portfolio.** It answers *where is the mass, and where are the
outliers* at a glance, over more items than a table can hold. It is a **scanning** tool.

It is **not** a precision tool. A reader cannot recover a value from a colour with any
accuracy, and should not be asked to. The moment a decision needs an exact value, the heat
map has done its job and a table should take over. **Every heat map should therefore have a
table behind it**, and in our reports it does.

### 6.2 The encoding rules

Two rules carry most of the quality.

**One variable per visual channel.** Colour carries level. Position carries taxonomy.
Something else — a hatch, a border, an explicit tone — carries *not rated*. The moment
colour carries two things (say, level *and* confidence) the map becomes unreadable and
readers invent a decoding rule of their own.

**Ordinal data takes a sequential palette.** Levels are ranks, so the palette must be
perceptually ordered: light → dark in a single hue ramp, so that *more colour = more level*
without a legend. Specifically:

- **Never a rainbow palette for ordinal data.** Spectral hue order is not perceived as
  magnitude, it is not monotonic in lightness, and it fabricates category boundaries at hue
  transitions that do not exist in the data.
- **Diverging palettes are for diverging data** — data with a meaningful midpoint you move
  either side of, such as *gap to target*. A maturity level has no meaningful midpoint, so
  a diverging palette on levels invents one.
- **Vary lightness, not just hue.** Lightness is the channel that survives greyscale
  printing and the commonest forms of colour vision deficiency.

### 6.3 Red-amber-green, and why it is worse than it looks

RAG is the default in institutional reporting, and it has four problems worth being able to
name:

1. **Red and green are the classic confusion pair.** Deuteranomaly and protanomaly are the
   commonest colour vision deficiencies, and both affect exactly this pair. A meaningful
   fraction of any large audience cannot reliably separate your two most important
   categories.
2. **RAG encodes judgement, not measurement.** Red means *bad*. But a Level 1 capability
   that is *supposed* to be Level 1 is not bad; it is on target. RAG cannot express "low and
   correct", which is a real and common state.
3. **It collapses to three buckets**, discarding resolution you paid for.
4. **It has no colour for "we have not looked."** Which is our single most common state, and
   the one whose distinctness the whole model depends on.

If an institution requires RAG, the survivable form is: use it for **gap to target**, where
*bad* is genuinely meaningful; keep a sequential ramp for level; and give *not assessed* its
own visually distinct treatment that is not a shade of red.

### 6.4 The four ways a heat map lies

Learn these as a checklist and run it over any heat map you are shown, including ours.

**1. Aggregation across unlike units.** A domain-level colour computed from its
capabilities' levels requires a roll-up rule, and any such rule is a judgement — usually an
average, which §4.2 forbids for ordinals. *Two at 3 and two at 1* and *four at 2* produce
the same domain colour and are entirely different situations. **If a domain is coloured, ask
what rule coloured it.** Ours does not roll up levels into domains; domains are reporting
clusters and are never scored (ADR-0006), and that is not an accident.

**2. Missing data drawn as bad.** The most consequential lie, and almost always
unintentional. If `unknown` renders in the same palette as a low level, the map says *we are
weak here* when the facts say *we have not looked here*. **Our views draw not-rated in the
palest tone rather than as 0**, and the report says on its first page that nothing is rated.

**3. False precision by cell size.** Equal-sized cells imply equal importance. A capability
that is existential and one that is marginal occupy the same square, and readers read area
as weight. There is no clean fix without a criticality measure; the honest mitigation is to
say so.

**4. The sea of red.** When most of the map is one colour, the map stops informing and
starts demoralising, and the reliable audience response is to reject the instrument rather
than the finding. If everything is red, the target state is probably wrong (§5.1) or the
resolution is wrong (§2.2). A map where everything looks the same is a map that has failed,
whichever direction it fails in.

### 6.5 When not to use one

| Instead of a heat map | Use | Because |
|---|---|---|
| Comparing values precisely | A sorted bar or dot plot | Position beats colour for accuracy, by a wide margin |
| Current vs target | A bullet chart, or a dumbbell | Two positions on one axis; the gap is the visible thing |
| A distribution over levels | A simple count-per-level bar | It is the honest replacement for "the average" |
| Fewer than ~20 items | A table | A heat map's value is scanning many; below that a table is strictly better |
| Change over time | Small multiples | Colour change between two maps is nearly impossible to read |

### 6.6 What our reports do, and what to say about it

Worth knowing so you can answer *"why does your heat map look like that?"*:

- **Not rated is drawn in the palest tone**, never as zero, and the report's first page says
  no capability is rated.
- **Domains are not coloured by a roll-up**, because scoring a reporting cluster would
  require averaging ordinals.
- **Every chart is generated from the facts.** There is no writing step, so a chart cannot
  drift from the numbers behind it. *"Prose with a number in it is generated, never typed"*
  is a repository rule with a test behind it.
- **The illustrative report exists** —
  [`../out/management-report-illustrative.html`](../out/management-report-illustrative.html)
  — the same report with **sample observations substituted in memory**, so you can show what
  a populated assessment looks like without inventing facts. A test checks that the facts
  digest is unchanged by building it. Sample data never reaches `facts/`. This is a good
  thing to demonstrate: it answers *"what will this look like when it's done?"* without
  anyone having to pretend.

---

## 7. The AI overlay: why the old maps do not fit

### 7.1 What generative and agentic AI actually added

The honest answer is not *"everything is different now"*. Most of a pre-2023 analytics
capability map still holds. But three genuinely new things appeared, and each of them
creates capabilities that older maps have no box for.

**Grounding became an enterprise capability, not a feature.** In a pre-generative model,
"data" decomposes into acquire · govern · analyse. Grounding does not fit any of the three.
It is a **corpus** someone curates and retires, an **index** with a refresh cadence, an
**access-trimming rule** enforced before ranking rather than after, an **embedding
lifecycle** that must be re-run when the model changes, and an **evaluation harness** that
proves it still returns the right document. Five jobs, at least three owners. In our map that
is `3.5` Knowledge Corpus & Content Management, `3.6` Knowledge Access & Retrieval and
`3.7` Derived Representation Management, plus `4.3` Prompt & Context Engineering.

**The interface became non-deterministic.** Testing, release and monitoring all change
character when the same input can produce different output and quality can degrade silently
because a model version changed underneath you. That is `6.3` continuous evaluation and
`4.7` release management doing work that traditional equivalents do not.

**Agents made the system an actor.** This is the largest shift, and the one our
**ADR-0015** addressed. Once software pursues a goal, chooses tools and takes actions, three
things need somewhere to land that a pre-agentic map does not provide: **what the thing is
allowed to do at runtime** (`5.7` runtime mediation and egress control), **where it runs**
(`5.8` agent runtime and execution environment), and **who is watching and can stop it**
(`6.7` human oversight operations). ADR-0015 added exactly those three, plus 8 criteria on
existing capabilities, and applied the three tests from §1.5 to refuse the rest.

Note that **`6.7` has no owner by design.** Human oversight *operations* — someone actually
on shift, able to intervene — has no home in the Bank's catalogue today. Naming a capability
that nobody owns is precisely how a capability map earns its keep, and it is why the owner
test must be *"can one person be named"*, not *"is one person already named"*.

### 7.2 The instruments that exist, and what each is for

You will be asked which frameworks we align to. This is the map of the territory. Editions
and dates below are as recorded in our own register, `facts/sources.json`, which is graded
and dated — cite from there, not from memory.

| Instrument | What it is | Use it for |
|---|---|---|
| **NIST AI RMF 1.0** (NIST AI 100-1, 26 Jan 2023) — GOVERN · MAP · MEASURE · MANAGE | A voluntary risk management framework, function/category/subcategory structured | The common language for AI risk in the US federal orbit. **Locus form is `GOVERN 1.1`** — not hyphenated |
| **NIST AI 600-1** (26 Jul 2024) | The Generative AI Profile of the RMF | Generative-specific risks. Its **action ids** *are* hyphenated (`GV-1.1-001`) — this is the trap |
| **ISO/IEC 42001:2023** | An AI **management system** standard, certifiable, with an Annex A of controls | The auditable governance spine. Structurally the ISO 27001 pattern applied to AI |
| **ISO/IEC 23894:2023** | Guidance on AI **risk management** | Risk process detail; complements 42001 |
| **ISO/IEC 42005:2025** | AI system **impact assessment** | Impact assessment method |
| **ISO/IEC 5338:2023** | AI system **life cycle processes** | Engineering process vocabulary |
| **OWASP GenAI Security Project** | The Top 10 for LLM Applications | Concrete attack classes. **Cite by name, never by number** — the list renumbers between editions |
| **EU AI Act** — Regulation (EU) 2024/1689, in force 1 August 2024 | Binding law, risk-tiered, extraterritorial in reach, applying in phases | The shape most regulation is converging on. **Legal owns this**, not Architecture — ADR-0008 |
| **CMMI V3.0** (ISACA, April 2023), **ISO/IEC 33020:2019** | Process assessment and measurement | The measurement discipline. Not AI content |
| **TOGAF** G193 / G211 / G233 | Capability-based planning and business capabilities | The method for the map itself |

Two rules apply to all of them and you should say them before anyone asks:

- **Alignment is not conformance.** We cite these as sources that informed capability lines.
  We are not certified against any of them, and **D7 is not yet control-mapped** —
  ISO/IEC 42001 Annex A and NIST AI RMF outcomes are not mapped to our governance
  capabilities. That domain should be carved out of any approval request until they are
  (OPEN-ITEMS #12).
- **Statutory references are Legal-owned and all candidate** (ADR-0008). We hold 18
  candidate obligations, and *candidate* is doing real work in that sentence: Architecture
  does not get to decide what the Bank is legally obliged to do. Also note that AI Act
  timelines have been amended since adoption; treat any date you have not confirmed with
  Legal as unverified.

### 7.3 Why a general capability map cannot simply be reused

Three structural reasons, useful when someone asks why the Bank's existing enterprise
capability map is not enough:

1. **The failure modes are new and land nowhere.** A retrieval answer including a document
   the asker was not cleared to see; an agent taking an unauthorised action; a
   prompt-injected document changing what a system does; a model version silently degrading
   output. **A map with no capability for the thing that fails cannot produce a roadmap that
   prevents it.**
2. **The ownership pattern is unusual.** AI capability is unusually distributed — of our 55,
   Architecture is the accountable owner of **two**. Standards for AI security belong to
   Cybersecurity, AI data governance to Data Management, literacy to L&D. A map built by one
   function for one function will quietly assign everything to that function and be wrong.
3. **The cadence is different.** Platform readiness moves quarterly; an enterprise
   capability map is maintained annually at best.

---
---

# Part II — The market

---

## 8. The three families of instrument

Everything you will be compared to is one of three things. Know what each optimises for and
you can be generous about them and still hold your position.

### 8.1 Analyst maturity assessments

**What they are.** A licensed capability model — typically two tiers, around 25 capabilities
at the lower one, written as verb phrases — plus a self-assessed questionnaire producing a
current and target score per capability, benchmarked against a peer set.

**What they are genuinely good at**, and you should say so first:

- **Executive framing.** The vocabulary is tested on hundreds of boards. It lands.
- **Peer comparison.** They have a dataset nobody else has. *"You are behind your peers on
  X"* is a sentence only they can say.
- **Speed.** Days, not months.
- **Completeness challenge.** Reading someone else's model against yours finds your holes.
  Ours found two — `1.5` AI Ecosystem & Alliance Management and `2.6` AI Innovation &
  Incubation were added as a direct result of that comparison. Volunteer this: *the model we
  are being compared to is a model we used, and it improved ours.*

**What they cost you:**

- **Coarse.** ~25 capabilities is a board resolution, not an ownership resolution. A single
  box like *deploy, operate and scale AI* spans six of our capabilities in six reporting
  lines. Nobody can be accountable for it, so it cannot be funded or fixed.
- **Thin underneath.** The score rests on a judgement made in a workshop, with no evidence
  recorded. There is nothing an auditor can follow.
- **Licensed.** The capability names and descriptions cannot be reproduced in anything that
  leaves the institution — which means the model cannot be the basis of anything you publish,
  and cannot be cited as a source.
- **No missing-data state.** Unexamined and absent collapse together (§4.3).

**Our position on them, stated fairly:** they are the right shape for a board slide and a
useful outside check on completeness. They are not built to sequence delivery or to survive
Internal Audit. The internal-only comparison is
[`analysis/capability-model-comparison.md`](analysis/capability-model-comparison.md) —
**internal use only**, and its subject's capability names must not be reproduced externally.

### 8.2 Cloud provider adoption frameworks

**What they are.** Structured guidance for adopting AI on a particular platform, organised
by perspective or phase. Our register holds several, graded B or C.

**Good for:** concrete checklists, especially operational ones; naming things you forgot;
and being free.

**What they cost:** they are **structured to sell and sequence adoption of one platform**.
That is not a criticism of their honesty, it is their purpose. Two consequences: they cannot
describe a capability that no product of theirs realises, and their granularity follows their
product boundaries rather than your ownership boundaries.

One is worth knowing about specifically: **AWS CAF-AI has been flagged historical by its own
publisher.** Frameworks in this family go stale silently, which is why our register records
edition, date and access route rather than just a name.

### 8.3 Process assessment standards

**What they are.** The ISO/IEC 330xx family and CMMI (§3). Rigorous, evidence-gated, with a
formal definition of what a rating requires and an ordering in which performance precedes
definition.

**Good for:** measurement discipline; defensibility; an audit trail; and an ordering that
resists the *"we approved the technology"* failure.

**What they cost:** they are built for software **processes** and contain **no AI content at
all**. You cannot assess AI capability with them; you can only assess processes.

### 8.4 Where ours sits, in one paragraph

Learn this shape; it is the answer to *"so what is yours, then?"*

> **We took the measurement discipline from the third family and applied it to a capability
> map built for AI.** The default scale is adapted from ISO/IEC 33020:2019, which is where
> the ordering comes from — a published standard with nothing performed against it earns no
> level. What none of the three has is the separation of **facts from judgement**: an
> observation like *"the agents standard is pre-release"* is true whichever framework reads
> it, so the same evidence can be reported through a different frame — including an analyst
> frame, if that is what the room knows — without reassessing anything, and without the two
> versions being able to contradict each other on the facts. What we deliberately do not do
> is benchmark against peers: no comparable dataset exists, and inventing one would undo the
> point.

---

## 9. How consultants actually run this, and how to hold your own

You said you do not have the consultant profile. Most of what that profile consists of is
four habits and a structure. None of it is mysterious, and you already have the harder half —
the substance.

### 9.1 The engagement shape

A capability assessment engagement, at any of the large firms, runs the same five steps:

1. **Frame.** Agree the question, the scope, the audience and what a decision at the end
   looks like. Underrated; it is where the engagement is won or lost.
2. **Model.** Adopt or adapt a capability model. Rarely built from scratch — usually a
   proprietary model lightly tailored.
3. **Assess.** Workshops and interviews, current and target per capability. Typically two to
   four weeks.
4. **Synthesise.** Gaps → findings → recommendations → a sequenced roadmap with an
   indicative cost and benefit. **This is where most of the value actually is.**
5. **Land.** The readout. Rehearsed, structured answer-first, with a small number of
   messages.

Compare honestly: **we are far stronger at 2 and at the evidence base under 3, and we have
not yet done 4 and 5**, because `practised` has never been observed. That is a fair
statement of where we are, and it is also the argument for spending the cheap moves in §5.4.

### 9.2 Answer first — the Minto pyramid

**Barbara Minto**, an ex-McKinsey consultant, formalised this as the *Pyramid Principle*
(published in the mid-to-late 1980s; sources differ between 1985 and 1987, so do not state a
year unless you have checked it). The rule:

> **State the answer first. Then the small number of reasons it is true. Then the evidence
> under each.**

Not: background, then method, then analysis, then — on slide 40 — the conclusion. The
executive read is top-down and stops early, so a bottom-up structure delivers the point to a
room that has already stopped listening.

Applied to ours, the top of the pyramid is one sentence:

> **The institution has built its enablers ahead of its practice.**

Then three supports: the assets exist and are recorded, with 5 finished but not released;
nobody has yet been asked whether the work is done, so nothing is rated; and the fix is
cheap — release two documents and ask four groups of people four questions.

Then the evidence under each. That is the whole deck.

### 9.3 The "so what" test

Every statement in an assessment gets asked *so what?* until it terminates in something
someone can do. Run it on your own material before someone runs it on you.

| Statement | So what? | Terminates? |
|---|---|---|
| *AI maturity is Level 2* | …so we are mid-pack? | No. Dead end |
| *39 of 55 `defined` values are unknown* | …so we do not know what standards exist outside the AI platform | Getting there |
| *…because the asset register covers AI platform assets only* | …so ask Cyber, Data Management, Legal and L&D what they have already approved | **Yes.** Four conversations, four owners |

Notice that the terminating statement is **cheap**. Findings that terminate in *"a
three-year programme"* are usually findings that have not been thought through to the point
where they are useful.

### 9.4 MECE, in practice

§2.1 has the theory. The practical use is as a **challenge tool**: when shown a
decomposition, test for overlap (*"which of these two owns prompt injection?"*) and for
holes (*"where does an agent taking an unauthorised action land?"*). Both questions are
short, sound naive, and reliably find real defects. They are also exactly the questions that
will be asked of you, which is why §2.5 and §13 exist.

### 9.5 Reading the room

Four people are typically present, and they are asking different questions. Answering the
wrong one is how a good assessment fails its readout.

| Who | Actually asking | Give them |
|---|---|---|
| **The executive sponsor** | *Am I exposed? What do I say upward?* | The one-sentence finding, and the cheapest credible next step |
| **The platform owner** | *Is this fair to my team?* | The `enabled` column and the asset register. **Their work is visible and separately credited** — this is what defuses the fight |
| **The risk / audit function** | *Can I rely on this?* | Evidence per observation, dates, observers; the provenance grading; what you concede |
| **The peer architect** | *Is the model right?* | The three tests, ADR-0015's discipline, and the invitation to challenge lines |

The platform-owner case is worth dwelling on, because it is the one that goes wrong. A
maturity assessment that returns *not rated* to a team that has built and shipped a great
deal reads as an insult. The defence is structural and you should lead with it: **`enabled`
and `defined` record their work as facts with evidence, and are reported separately and
prominently. The level withholds nothing from them; it is measuring a different sentence.**

### 9.6 Five questions that expose a thin assessment

Ask these when you are shown someone else's. They also tell you what you will be asked.

1. **"What does this instrument do when nobody has looked?"** If there is no state for it,
   the picture systematically confuses unexamined with absent.
2. **"What evidence sits behind this rating, and who recorded it, and when?"** If the answer
   is a workshop, the rating is an impression.
3. **"Would two people have answered this the same way?"** Reliability. Usually unmeasured,
   including in ours.
4. **"Who owns this box?"** If the answer needs more than one name, the box cannot be acted
   on.
5. **"What would change this rating?"** If the answer is not a specific, checkable fact, the
   rating is not connected to reality.

---
---

# Part III — Defending ours

---

## 10. The framework in one page

The claim chain, in order. If you can reproduce this from memory you can defend the model.

1. **Two people disagree about the same capability**, and both are telling the truth — one
   about whether the work is *done*, the other about whether the *means* exist. Any model
   that answers with one number must discard one of them.
2. **So we record facts, not scores.** Four observations per capability, each `yes` /
   `partial` / `no` / `n/a` / `unknown`, each with evidence, an observer and a date. An
   observation is true whichever framework reads it.
3. **`practised` is asked at L3**, per criterion, because that is the level at which work
   can actually be witnessed; the capability's value is **derived** from its criteria, never
   typed (ADR-0014).
4. **A level is a rule over facts**, in one file, arguable separately from the facts it
   reads. Nobody types a level anywhere, and `check` fails if a derived value is found
   stored.
5. **The default rule is adapted from ISO/IEC 33020:2019**, and it takes the standard's
   ordering: performance at Level 1, resources and competence at Level 2, a defined process
   at Level 3. **A standard with nothing performed against it earns no level.**
6. **Other rules may read the same facts.** Two lenses ship. Where a lens and the default
   disagree, **the default is the finding**.
7. **`facts/` is edited; `out/` is generated.** No finding is ever fixed by editing a view.
   Prose with a number in it is generated, never typed, and there are tests behind that.
8. **Provenance is graded by whether a reviewer can open the source**, not by prestige
   (ADR-0010), and a grade-D source cannot support a claim that leaves the Bank.
9. **Therefore: today nothing is rated**, because `practised` has never been observed — and
   the report says so on its first page rather than papering over it.

**The finding that falls out**: *the institution has built its enablers ahead of its
practice.* Enablers exist and are recorded; practice has not been examined. That sentence
names its own fix.

### The live position, 9 September 2026

Snapshot; the live figures are in [`../out/`](../out/README.md).

| | |
|---|---|
| Domains · capabilities · criteria | 8 · 55 · 281 |
| Observations recorded | 446 (281 criterion-level `practised`, plus 3 × 55) |
| `practised` | **`unknown` on all 281 criteria** |
| `skilled` | `unknown` on all 55 |
| `enabled` | 8 `yes` · 6 `partial` · 15 `n/a` · 26 `unknown` |
| `defined` | 10 `yes` · 4 `partial` · 41 `unknown` |
| Default scale | **not rated: 55 of 55** |
| Maturity lens | not rated: 55 of 55 (same performance gate) |
| Executive lens | 8 at 5 · 2 at 4 · 4 at 3 · 41 not rated — **entirely on enablers, with no observed practice behind them** |
| Offerings · assets | 7 · 20 (15 released) |
| Owners | 16 units, 55 mapped; **9 capabilities with no owner** — 1.5, 2.3, 4.6, 6.3, 6.7, 7.2, 7.5, 7.6, 7.9 |
| Sources | 45 — grade A 13 · B 11 · C 14 · D 7 |
| Capabilities resting partly on grade D | 14 |

---

## 11. Every design decision, with its warrant

Each of these will be questioned. Each has a reason that is not *"we preferred it"*.

### 11.1 Facts, scales and views are separate directories

**Decision.** `facts/` holds what is true, with evidence and a date. `scales/` holds rules
that turn observations into levels. `out/` holds generated views. Derived values are never
stored, and `check` fails if one is found stored.

**Warrant.** It is what makes several frames possible over one body of evidence without
reassessing anything (§4.6). It also means changing our mind about measurement changes no
fact — which is the difference between an instrument you can improve and one you can only
replace. **ADR-0013**, the ADR that governs the model.

**The consequence to own:** it is more work than a spreadsheet, and it requires that nobody
ever fixes a number by editing a view. That discipline is enforced by tests, not by good
intentions.

### 11.2 Four observations, not one score

**Decision.** `practised` · `enabled` · `skilled` · `defined`.

**Warrant.** These are the four things people are actually arguing about when they disagree
about a capability, and each has a different natural owner — which means each is answerable
by someone who actually knows. They map onto ISO/IEC 33020's process attributes (§3.3),
which is what gives the ladder its ordering.

**Why not more?** Because every additional observation multiplies the review burden by 55
and the combination space by five. The one we know is missing is `conforms` (§13).

### 11.3 `practised` is observed at L3 and derived at L2

**Decision.** ADR-0014.

**Warrant.** *"Is 4.4 practised?"* has no honest single answer, because 4.4 covers six
distinct practices and the Bank might do guardrails well and never do loop control at all.
Asking at the criterion improves **reliability** (two people converge on a specific
practice; they do not converge on a broad one) and it makes gaps **nameable** — the roadmap
item stops being *"improve agent orchestration"* and becomes *"termination and loop control
has never been done"*, which is a piece of work someone can be given.

**The consequence to own:** a review round is 446 rows, not 55. That is the price, and it is
the main thing a reviewer will push back on.

### 11.4 Performance gates every level

**Decision.** No `practised`, no level — however good the other three look.

**Warrant, and the objection.** *"But the standard came first"* — it usually did. The answer
is that **the ladder orders claims, not activities**:

| Level | The claim |
|---|---|
| 1 Performed | "We do this." |
| 2 Managed | "We do this, repeatably, with tooling and competent people." |
| 3 Established | "We do this, repeatably, **against an approved institutional standard**." |

Level 3 does not claim *a standard exists*. It claims *the work is done to the standard* —
and that sentence needs the work. **A driving manual existing does not mean anyone in the
building can drive.**

Writing the standard first does not make a capability Level 3 early. It makes `defined` read
`yes` while `practised` is `unknown` — which the model records exactly and reports as *not
rated*. **That combination is not the model withholding credit; it is the Bank's headline
finding in one line.** If `defined` alone could place a level, that finding would be
invisible.

**And the ordering is not ours** — it is the standard's (§3.3), which is the strongest
single sentence in the defence.

### 11.5 The roll-up is asymmetric

Covered at §4.5. **Under-claiming costs a follow-up question; over-claiming costs an
incident or an audit finding. The risks are not symmetric, so the rule is not.**

### 11.6 `unknown` is a first-class value

Covered at §4.3. The proof that we hold ourselves to it: **24 `enabled` rows corrected from
`no` to `unknown` on 4 September 2026** under ADR-0013 Amendment 2.

### 11.7 Lenses exist, and the default wins

**Decision.** Three scales ship. The executive lens averages and does not gate on
performance; the maturity lens uses conventional CMM-shaped level names but applies the same
performance gate as the default. **Where a lens and the default disagree, the default is the
finding.**

**Warrant.** A room that already holds a frame can be answered in that frame without the
assessment being redone and without anyone pretending the evidence changed. That is the
payoff of §4.6, made concrete.

**The discipline that makes it honest:** a lens exists so a room can be answered, **not so
the friendlier number can be chosen**. Say that sentence out loud when you show the
executive lens, and note that every level it currently shows rests on enablers with no
observed practice behind them.

**The maturity lens deliberately does not behave like a maturity model.** Maturity ladders
are conventionally the forgiving instrument — they rate the enablers when practice is
unobserved. Ours applies the same performance gate as the default, because rating the
enablers alone is precisely how *"we approved the technology"* comes to read as *"we have
the capability"*.

### 11.8 Provenance is graded by openability, not prestige

**Decision.** ADR-0010. Grade A (open, dated, standards body) → grade D (non-public, or not a
publication at all). **A grade-D source cannot support a claim that leaves the Bank,
whatever its quality.**

**Warrant.** The test that matters for a claim leaving the institution is *can the reviewer
check it?* Prestige does not answer that; a licence does. This also makes a genuinely
awkward position visible rather than hidden: **14 of our capabilities currently rest partly
on grade D**, and `out/provenance.md` names them.

**Two consequences worth stating before someone finds them:** the register records edition,
date and access route for all 45 sources, and **most citations still have no pinned locus** —
a citation without a clause says *this source informed the capability* without saying where
(OPEN-ITEMS #11).

### 11.9 Scales are not in the source register

**Decision.** `facts/sources.json` does not contain ISO/IEC 33020. Each scale carries its
own `BASIS` (what is adopted, what is ours) and `CAUTION` (how far anyone actually opened
the source), and both are shown on **every** view that uses the scale.

**Warrant.** **A source is something we cite; a scale is something we wrote.** Putting the
scale in the register would imply the ladder is a citation, when it is a rule of ours that
happens to be adapted from one. Keeping `CAUTION` on the scale rather than in a README means
the caveat travels with the claim into every view — so the thing that must not be quoted is
attached to the thing a reader might quote.

### 11.10 Nothing in the build names a scale or a question

**Decision.** Scales are discovered by listing `scales/`; questions come from
`facts/questions.json`. A test fails if a builder names one.

**Warrant.** It is what makes *"add a scale, get a view"* and *"add a question, get a page"*
true rather than aspirational, and it stops the report from acquiring hard-coded knowledge
of the assessment — which is how generated artifacts start drifting from their facts.

---

## 12. The objection drill

The objection, what is really being asked, the answer, and what to point at. Learn the
italic sentences.

### On size and effort

**1. "Fifty-five is too many."**
*Really asking: this will take forever, and I do not have the people.*
The 8 domains are the reporting tier; the 55 are the working tier where ownership and rating
happen; the 281 criteria are not reporting units at all — they are the evidence questions
behind a rating. **The number is a consequence of the owner test, not a target.** *If a box
needs six owners it cannot be rated, owned or funded, so we split it — and 55 is where that
rule stopped.*
→ §2.2, [`analysis/capability-model-comparison.md`](analysis/capability-model-comparison.md) §4

**2. "The analyst model manages with 25."**
*Really asking: are you over-engineering, or are they wrong?*
Neither. **They are optimised for a board conversation, where the owner test is not
applied.** Their single box *deploy, operate and scale AI* spans six of our capabilities in
six reporting lines. And *if a committee already knows their 25, we can report our ratings
through their frame without re-rating anything* — that is exactly what the facts/scales
split buys.
→ §8.1, §11.1

**3. "This is over-engineering."**
*Really asking: justify the cost.*
**The costs are not symmetric.** Too much resolution costs a longer assessment. Too little
costs a roadmap that cannot be sequenced, a gap analysis nobody can own, and a governance
domain that fails its first audit.

**4. "How long does a round take?"**
446 rows, but they are not one person's work: `practised` is the capability owners,
`enabled` is the platform teams, `defined` is whoever owns the subject, `skilled` is L&D.
The workbook is sent, the yellow cells are filled in, it comes back, one command reads it in.
**Nothing requires new tooling or new investment.**
→ [`first-round.md`](first-round.md), [`using-the-model.md`](using-the-model.md)

### On the result

**5. "Nothing is rated. What use is this?"**
*Really asking: you have spent months and produced no score.*
This is the objection to welcome. **Not rated is a result, and it is the honest one.** A
rating requires knowing whether something is *practised*, and that question has not yet been
put to the capability owners. Most instruments would have scored those capabilities anyway,
by treating unexamined as absent — which would have produced a confident picture that was
wrong. *What we have instead is a complete, evidenced inventory of what exists, a named list
of exactly which questions would change the picture, and the four groups of people who can
answer them.*
→ §4.3, §5.4

**6. "So what level is the Bank at?"**
**That question has no form in this model.** We rate capabilities, not the institution,
because a single number would be an average over 55 ordinals and would hide exactly the
variation the roadmap needs. Show the distribution. If the room insists, the executive lens
exists for it — and it says on its face that it averages and does not gate on performance.
→ §3.2, §4.2

**7. "Can we just average the domains for the slide?"**
No, and the reason is short: **levels are ranks, not quantities.** *Two at 3 and two at 1
averages the same as four at 2, and those are completely different situations with
completely different roadmaps.* Offer the count-per-level bar instead; it fits the same slide
and says more.
→ §4.2, §6.4

**8. "Everything is unknown — that just means you have not done the work."**
Partly true, and worth conceding plainly: **the work that has not been done is asking the
owners, and that is the next step, not a defect in the instrument.** What has been done is
the map, the register of what exists, the measurement rule and the evidence discipline.
*The alternative was to guess, and a guessed baseline is worse than no baseline because
people plan against it.*

### On the scale

**9. "The standard came first — why doesn't that count?"**
The single most common question. **The ladder orders claims, not activities.** Level 3
claims *the work is done to the standard*, not *a standard exists*. A driving manual
existing does not mean anyone in the building can drive. **And the ordering is the
standard's, not ours.**
→ §11.4, §3.3

**10. "Who approved this scale? Is it standard?"**
Learn this close to verbatim: *The capability map is ours, drawn from published frameworks
that are cited and graded. The measurement scale is adapted from ISO/IEC 33020:2019, the ISO
process measurement framework — we took its ladder and, more importantly, its ordering, in
which performance precedes definition. What is ours is stated on the face of every view:
four observations in place of five process attributes, three values in place of its four,
and a simplified rule. Nothing here claims to be an ISO assessment, and no capability is
rated against a clause we have not opened.*
→ [`where-the-scales-come-from.md`](where-the-scales-come-from.md) §7

**11. "Why is this one a 2 and that one a 3?"**
Never answer from memory. **Every view carries a *How this scale places a level* table**,
derived by running the rule over all 625 value combinations, so it cannot drift from the
code. The short answer: **the step from 2 to 3 is a single observation** — everything Level
3 asks is already required at Level 2 except that `defined` must be `yes`.
→ [`../out/capability-assessment-level.md`](../out/capability-assessment-level.md)

**12. "Your Level 3 doesn't prove conformance."**
**Correct, and we say so ourselves.** `defined` says a standard exists; `practised` says the
work is done. Neither says the work *follows* the standard. Level 3 reads conformance from
the two facts sitting together, and its reason line admits it. A fifth observation —
`conforms` — would make it checkable; whether it is worth collecting is open.
→ OPEN-ITEMS #7

**13. "Why does it stop at 3?"**
Levels 4 and 5 are defined in the scale but **need observations nobody collects** —
threshold monitoring and a closed improvement cycle. `DERIVABLE_MAX = 3` declares that
ceiling on every view, **so a capability at 3 does not quietly read as "the best there
is."** Level 3 is the ceiling of what is measured, not of the scale.
→ OPEN-ITEMS #8

**14. "Your maturity ladder looks like one I have seen before."**
Handle carefully. **Initial and Optimizing are CMM/CMMI levels 1 and 5 (SEI, 1991) —
public, citable, and the origin of the whole convention. The middle-band words are generic
vocabulary that recurs across many published maturity models; no model owns them.** The
recognition is the convention, not a lineage. **Never attribute the ladder to any particular
institution's model** — doing so would rest a claim on a non-public artifact.
→ §16, [`where-the-scales-come-from.md`](where-the-scales-come-from.md) §3.1

**15. "Your executive lens contradicts your default."**
It does, and that is designed. It averages and does not gate on performance, which is why it
can show levels today when the default cannot. **Every level it shows rests on enablers with
no observed practice behind them, and it says so on its face. Where a lens and the default
disagree, the default is the finding.**
→ §11.7

### On the map

**16. "Who owns 6.7? Nobody. So why is it there?"**
**By design.** Human oversight *operations* has no home in the Bank's catalogue today, and
naming a capability that nobody owns is precisely how a capability map earns its keep. The
owner test is *can one person be named*, not *is one already named*. **Nine of 55 are
unowned, and that is one of the findings.**
→ §7.1, ADR-0015

**17. "Are the extra capabilities real, or did you invent them?"**
Every one carries named sources a reviewer can open, and a provenance register records the
edition, date, access route and grade of each. **Where a capability is our own synthesis
rather than something a published model names — true of most of the agentic and retrieval
layer, because nothing published names them yet — it says so, rather than borrowing
authority it does not have.**
→ [`../out/provenance.md`](../out/provenance.md)

**18. "Why not use the Bank's existing capability map?"**
We anchor to it — every capability records whether it is a `specialization`, `new`, or a
`lens` over it. But three things do not carry over: the new failure modes have nowhere to
land, the ownership pattern is unusually distributed (Architecture owns 2 of 55), and the
cadence is quarterly, not annual. **And our anchoring is provisional and says so** — 14 of
55 are lenses, and ADR-0007 should be carved out of any approval request until a control
mapping exists.
→ §7.3, §2.3

**19. "Why is speech-to-text not a capability?"**
Modalities are **offerings**. They fail the owner test and the landing test: no distinct
owner, and no failure that lands there and nowhere else. This is ADR-0015's rule — a
capability is warranted only where a distinct owner, a failure with no landing site, and no
adequate existing home **all three** coincide.

### On trust

**20. "What stops an owner over-claiming?"**
Four things, and the honest limit. Evidence is required for every non-`unknown` value.
Questions are asked at the criterion, where generosity is harder. The roll-up is asymmetric —
one weak link stops the claim, and an unexamined criterion is never counted as satisfied.
And the level is derived, so nobody can type a favourable one. **What we do not have is a
second observer, and inter-rater reliability has never been measured.**
→ §4.4, §4.5, §13

**21. "Can I see the underlying data?"**
Yes — that is the point. Every observation carries evidence, an observer and a date; the
source register carries edition, date, access route and grade; the workbook shows the
register to a reviewer on sheet 8. **What may leave the Bank is a separate question**, and
`out/provenance.md` answers it.

**22. "This is just a spreadsheet with extra steps."**
The spreadsheet is an input and output format, not the model. **The model is that facts are
edited and views are generated; that no derived value is ever stored; that the rule turning
observations into levels is code, tested over all 625 combinations; and that prose with a
number in it is generated rather than typed.** *There is no writing step, so a report cannot
drift from its facts — re-running after new observations produces a new report, not a new
draft.*

---

## 13. What we concede, first and unprompted

Conceding before you are caught is the strongest defensive move available, and it is also
just honest. Each of these is already recorded in [`../OPEN-ITEMS.md`](../OPEN-ITEMS.md) —
volunteer them, and say where they are written down.

| Concession | The honest statement |
|---|---|
| **Nothing is rated** | `practised` has never been observed on any of 281 criteria. The default scale and the maturity lens correctly return *not rated* for all 55. This is the single highest-value gap, and it is a conversation, not a programme (#1, #2) |
| **Level 3 reads conformance, it does not evidence it** | Neither observation says the work *follows* the standard. A fifth observation would fix it (#7) |
| **Levels 4 and 5 are unreachable** | Defined but not derivable; `DERIVABLE_MAX` declares it on every view (#8) |
| **No peer benchmark, and there will not be one** | No comparable dataset exists. Inventing one would undo the point. If the room needs peer comparison, an analyst instrument is the right tool and we should say so |
| **Inter-rater reliability is unmeasured** | Every observation has one observer. We have devices that should improve agreement (§4.4) and no measurement that they do |
| **No target state** | We record current state only. Criticality is not modelled, so "gap to target" cannot be computed — only "gap to Level 3", which is not the same thing (§5.1) |
| **Anchoring is provisional** | 14 of 55 are `lens`, unverified. **Carve ADR-0007 out of any approval request** until control mapping exists (#12, #13) |
| **D7 is not control-mapped** | ISO/IEC 42001 Annex A and NIST AI RMF outcomes are not mapped to our governance capabilities (#12) |
| **Most citations have no pinned locus** | A citation without a clause says *this source informed the capability* without saying where; under ADR-0010 an unpinned pair reads as *synthesized* (#11) |
| **14 capabilities rest partly on grade D** | Named in `out/provenance.md`. They cannot support anything that leaves the Bank until re-cited (#9) |
| **ISO/IEC 33020 has not been opened** | Adapted from its published preview. The percentage bands and the exact level rule **must not be quoted** (#10) |
| **The ownership ADR is still Proposed** | ADR-0012's own text says the dependency flag is the stronger route |
| **Parts of `docs/` lag `facts/`** | Several hand-written documents still say 52 capabilities and 258 criteria; the live model is 55 and 281 after ADR-0015. **Generated views are always right; hand-written prose is a snapshot** |

The framing to use, once, at the start of a hostile review:

> *Here is what this model does not do, before you find it. It does not rate anything today,
> because we have not asked the owners. It does not prove conformance, only reads it. It
> does not benchmark against peers, and it never will. And fourteen capabilities rest partly
> on sources you could not open, which are named. Everything else, you can check.*

---

## 14. Vocabulary you must not fumble

These are the words that cause the arguments. The full reference is
[`glossary.md`](glossary.md); these are the ones that will catch you.

| Say | Not | Because |
|---|---|---|
| **Capability** (L2) | Offering, product, team, project | A capability survives replacing every vendor. An offering realises capabilities; it is not one |
| **Criterion** (L3) | Sub-capability | A criterion is a witnessable practice. It carries no level of its own |
| **Observation** | Score, rating | An observation is a fact with evidence, an observer and a date |
| **Level** | Score, maturity | A level is a scale's output over four observations. **Always derived, never typed** |
| **Not rated** | Level 0, zero, low | Not rated means the evidence to place it has never been gathered. Level 0 Incomplete is an evidenced statement that it is not performed |
| **`unknown`** | `no` | `unknown` means nobody has looked. `no` means someone looked and it is not there |
| **Lens** | Alternative assessment | Where a lens and the default disagree, the default is the finding |
| **Taxonomy level** (`L3`) | Capability level (`Level 3`) | Two different things. A position in the map, versus what a scale returns. **Say "L3 criterion" and "Level 3 Established" and never abbreviate either** |
| **Adapted from ISO/IEC 33020** | Based on ISO, ISO-compliant, ISO-aligned | *Adapted* is the ADR-0010 derivation type and it is precise. The others imply conformance we do not claim |
| **Domain** (L1) | Lifecycle, phase, stage | ADR-0006: reporting clusters, not a sequence. Domains are never scored |
| **Candidate obligation** | Requirement | Statutory references are Legal-owned and all candidate (ADR-0008) |

**"Readiness" has three senses and one of them is retired.** *Executive readiness* is a
lens. `out/agent-readiness.md` is a use-case page, named for its question. **Readiness 0-5
on a realization is retired** (ADR-0002, superseded by ADR-0013). If someone asks *"what
readiness is retrieval?"*, the honest answer is that **the question no longer has a form** —
supply is now the `enabled` column and cannot produce a level on its own.

**Digits are not comparable across scales.** The executive lens runs 1-5; the default derives
0-3 today. A 4 there is not "better" than a 3 here. The report compares the maturity lens
level for level because every level it can return is one the default can return, and refuses
to compare the executive one's digits.

---

## 15. Reading list

Ordered by what it will do for you, with the grade of each so you know what can be quoted.

**Inside this repository, in this order**

| | |
|---|---|
| [`how-it-works.md`](how-it-works.md) | The design in ten minutes. If you read one, this one |
| [`../out/capability-map.md`](../out/capability-map.md) | The taxonomy alone. **Generated — never hand-write the map** |
| [`glossary.md`](glossary.md) | The vocabulary, and the four words that mean more than one thing |
| [`where-the-scales-come-from.md`](where-the-scales-come-from.md) | Provenance of the instrument. **Read before defending a level to anyone** |
| [`what-is-settled.md`](what-is-settled.md) | The rules in force, and the three that were reversed |
| [`decisions/adr/0013-facts-and-scales.md`](decisions/adr/0013-facts-and-scales.md) | The ADR that governs the model |
| [`decisions/adr/0014-practised-is-observed-at-l3.md`](decisions/adr/0014-practised-is-observed-at-l3.md) · [`0015`](decisions/adr/0015-extend-d4-d6-across-the-agentic-seam.md) | Why `practised` is at L3; the agentic seam and the three tests |
| [`analysis/capability-model-comparison.md`](analysis/capability-model-comparison.md) | The analyst comparison. **Internal use only** |
| [`../OPEN-ITEMS.md`](../OPEN-ITEMS.md) | What is unresolved. Read before any review |

**Outside — the theory**

| Grade | | |
|---|---|---|
| **A** | **S. S. Stevens**, "On the Theory of Scales of Measurement", *Science* 103 (2684), 677-680, 1946 | Four pages. The foundation of §4.1-§4.2 |
| **A** | **NIST AI RMF 1.0** (NIST AI 100-1, 26 Jan 2023) and the **Generative AI Profile** (NIST AI 600-1, 26 Jul 2024) | Free, open, current. The common language for AI risk. Locus form `GOVERN 1.1` |
| **B** | **CMMI V3.0** (CMMI Institute / ISACA, April 2023) | For the capability-vs-maturity-level distinction and the two representations (§3.2) |
| **B** | **TOGAF Series Guides** — G193 capability-based planning (16 Jul 2019), G211 business capabilities, G233 business capability planning (11 Apr 2023) | The method for building the map itself |
| **C** | **ISO/IEC 33020:2019** | What our scale is adapted from. **Paywalled; the preview stops before clause 5.3.** Opening it closes OPEN-ITEMS #10 |
| **C** | **ISO/IEC 42001:2023** (with Annex A) and **ISO/IEC 23894:2023** | The governance spine and AI risk guidance. Paywalled |
| — | **Philip Crosby**, *Quality Is Free* (1979); **Watts Humphrey**, *Managing the Software Process* (1989) | Historical. Read the QMMG description; it is the origin of the whole convention (§3.1) |
| — | **Barbara Minto**, *The Pyramid Principle* | For §9.2. **Publication year is inconsistently reported (1985 / 1987) — do not state one unless you have checked** |

**A note on how to read a standard you are about to cite.** The `citing` skill in this
repository states the rule and it is the right habit generally: **do not cite from memory.**
Fetch the source and read the relevant part, or find the publisher's own page for edition,
date and status — and if neither is possible, **say it is unverified in the text itself**.
A secondary source establishes that a claim exists, not that it is true. A clause number
that "mirrors" another standard's structure is a guess until the text is opened. This
repository has been wrong from memory before — about which process attribute carries
competence, about which standard COBIT 2019 builds on, and about which clause names a
rating scale — and each was corrected by opening the source.

---

## 16. Handling — before any of this leaves the Bank

| Check | Why |
|---|---|
| **No ISO/IEC 33020 percentage bands or exact level rule quoted** | Unverified, and sourced from a superseded predecessor (§3.5) |
| **The maturity ladder is not attributed to any institution's model** | It is the generic convention. Attributing it would rest a claim on a non-public artifact |
| **No licensed analyst wording, capability names or descriptions anywhere** | Usable inside the Bank under our subscription; never reproduced externally; never listed as a source |
| **Nothing from `docs/notes/`** | Grade D, internal only |
| **ADR-0011 §2.4 and §3.4 stripped** | They discuss the non-public comparator |
| **[`../out/provenance.md`](../out/provenance.md) checked for grade-D support** | 14 capabilities currently rest partly on one. A grade-D source cannot support a claim that leaves the Bank, whatever its quality |
| **Cite by name, never by number** | For any list that renumbers between editions — the OWASP Top 10 above all |
| **`GOVERN 1.1`, not hyphenated** | The hyphenated form belongs to AI 600-1 action ids (`GV-1.1-001`) |
| **Four provenance findings still open** | They block external publication until closed (OPEN-ITEMS #9). **About a day's work** |

**ISO/IEC 33020 itself is grade C, not D.** It is a real, citable, current standard — a
reviewer simply needs a licence to open it. Citing it by name is fine. Quoting what we have
not read is not.

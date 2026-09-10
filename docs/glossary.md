# Vocabulary

Every term this model uses, what it means here, and — for the four words that mean more
than one thing — which sense is meant where.

*Reference, not normative. The binding records are in [`decisions/`](decisions/README.md);
the narrative is [`how-it-works.md`](how-it-works.md).*

---

## 1. The words that carry the model

| Term | In this model it means | It is **not** |
|---|---|---|
| **Domain** (L1) | A reporting cluster. Groups capabilities so a reader can find them | A lifecycle, a team, a process or a sequence (ADR-0006) |
| **Capability** (L2) | Something the institution must be able to do with AI, with one accountable owner. Survives replacing every vendor. **The unit that carries a level** | A product, a platform, a team or a project |
| **Criterion** (L3) | A specific practice that can actually be witnessed on a real system. Where *practised* is observed | A gate, a score, or something that carries a level of its own |
| **Offering** | What a delivery team can get today: a bundle of standard, reference architecture, modules and templates, with someone operating it | A capability. An offering realises capabilities; it is not one |
| **Asset** | One named artifact inside an offering — a standard, a reference architecture, a Terraform module, a template — with a status | Evidence that the thing is *done* |
| **Observation** | One recorded fact about the Bank, with evidence, an observer and a date | A score, a rating or a judgement |
| **Scale** | A rule that reads observations and returns a level. The only place a judgement is encoded | Part of the facts. Changing a scale changes no fact |
| **Lens** | A scale that is **not** the default. Exists so a room that already holds a frame can be answered in it | An alternative assessment. Where a lens and the default disagree, **the default is the finding** |
| **Level** | The output of a scale over one capability's four observations. Always derived, never typed | Something anyone writes down anywhere |
| **View** | A generated rendering of the facts, optionally through one scale | A document anyone edits |
| **Question** | A recorded *"can we do X?"*, naming the capabilities and offerings it touches | A capability. Use cases are not capabilities |
| **Anchor** | How a capability relates to the Bank's **existing** enterprise capability map: `specialization`, `new` or `lens` | Verified. It is provisional until a crosswalk exists (ADR-0007) |
| **Confidence** | How much we trust the *line itself* — its name, boundary and definition | A measure of the Bank. It is a measure of the map |

## 2. The four observations

Four questions, each answered `yes` / `partial` / `no` / `n/a` / `unknown`, each with
evidence and a name attached. Three are asked once per capability; **practised is asked
once per L3 criterion** and the capability value is derived (ADR-0014).

| | The question | Asked at | Answered by |
|---|---|---|---|
| **Practised** | Is this practice done on real AI systems, repeatedly? | each criterion | The capability owner |
| **Enabled** | Can a team get the tooling without building it themselves? | the capability | The platform team |
| **Skilled** | Do the people who must do this know how? | the capability | The owner, or L&D |
| **Defined** | Is there an approved institutional standard, policy or method? | the capability | Whoever owns the subject |

### The five values, and the two that get misused

| Value | Means | Requires |
|---|---|---|
| `yes` | Done | Evidence |
| `partial` | Done in places, or incompletely. Say where | Evidence |
| `no` | **An evidenced negative.** Someone looked and it is not there | Evidence, or a basis saying what was looked at |
| `n/a` | Does not apply here | A reason; for `enabled`, an entry in `enablement-context.json` |
| `unknown` | **Nobody has looked. Never a zero** | Nothing. It is the honest default |

**`no` and `unknown` are the pair that decides whether the model is trustworthy.** A
register that was searched and had nothing is `unknown` until the owner is asked, because
a standard owned by another function may exist and simply not be recorded here
(ADR-0013 Amendment 2). Recording that absence as `no` turns *we did not look* into
*it does not exist*, which is the failure this model exists to prevent.

**`n/a` is not a failure.** A governance capability is not worse for having no tooling. It
drops out of the calculation rather than counting against the capability.

### From four answers to a level

**A level is the highest rung whose conditions all four observations satisfy.** Nobody
types it. The conditions are published per scale in the *How this scale places a level*
table on every generated view, derived by running the rule over all 625 value
combinations — so they cannot drift from the code:

- **`n/a` counts as satisfied.** It drops out; it does not fail.
- **`unknown` on `practised` means not rated** on the default scale and the maturity lens,
  however good the other three look. The executive lens does not gate that way, which is
  why it is a lens.
- **The step from 2 to 3 is one observation:** `defined` must be `yes`.

The worked table beneath it shows ten sets of answers and what each produces.

---

## 3. The four words that mean more than one thing

These are the ones that cause the arguments. Each has a live sense and, in three cases, a
retired one still visible in the repository.

### "Readiness" — three senses, one of them retired

| Where you see it | What it means there | Standing |
|---|---|---|
| **Executive readiness** (`scales/executive.py`) | A **lens**: *how much of what we said we would do actually exists?* Averages across capabilities, deliberately, and says so on every view | **Live.** A lens, never the assessment |
| **`out/agent-readiness.md`** | A **use-case page**: the answer to one recorded question, *"can we run AI agents?"*. Named for its question, not for a scale | **Live.** One page per entry in `facts/questions.json` |
| **Readiness 0–5 on a realization** | The retired second scale: a 0–5 level carried by a *realization* alongside a maturity level on the capability | **Retired** (ADR-0002, superseded by ADR-0013) |

The retired sense is still readable in two places, both labelled: the `note` field on each
offering in `facts/offerings.json`, kept as migration history (OPEN-ITEMS #20), and
`archive/`. **If someone in a meeting says "what readiness is retrieval?", the honest
answer is that the question no longer has a form** — supply is now the `enabled` column and
cannot produce a level on its own.

### "Maturity" — two senses

| Where you see it | What it means there | Standing |
|---|---|---|
| **Institutional maturity** (`scales/maturity.py`) | A **lens**: *how far has the practice spread beyond the people doing it?* Applies the same performance gate as the default | **Live.** A lens |
| **Maturity on a capability, 1–5** | The retired first scale, paired with readiness above | **Retired** (ADR-0001, superseded by ADR-0013) |

The maturity lens uses the conventional CMM-shaped ladder — Initial · Emerging ·
Consolidating · Integrating · Optimizing. **Those names are the generic convention and must
never be attributed to any particular institution's model**, least of all the grade-D slide
in `docs/notes/` (CLAUDE.md §4, ADR-0011 §2.4).

### "Level" — two senses

**A taxonomy level** (L1 domain, L2 capability, L3 criterion) is a position in the map. **A
capability level** (0–5) is what a scale returns. `L3` and `Level 3` are different things
and are written differently for that reason: *L3 criterion*, *Level 3 Established*.

### "D1"–"D8" — two senses

They are **both** the eight domain identifiers (`D3` = Data & Knowledge Management) and the
old identifiers for the first eight decisions (`D3` = ADR-0003). In new text write
**`ADR-0003`** for a decision and **`domain D3`** for a domain, and never rewrite a
D-number mechanically. The alias table is in
[`decisions/README.md`](decisions/README.md).

---

## 4. Terms that are retired

Nothing below is how the model works today. They are listed because they appear in
`archive/`, in material already sent to reviewers, and in the offering notes.

| Retired term | What it was | What replaced it | Record |
|---|---|---|---|
| **Realization** | The thing that carried a readiness level | **Offering**, which carries assets with statuses and no level of its own | ADR-0013 |
| **Readiness level (0–5)** | Supply, scored | The `enabled` observation, which contributes nothing without `practised` | ADR-0013 |
| **Maturity level (1–5) on a capability** | The typed capability score | A **derived** level from four observations | ADR-0013 |
| **Rubric** | A per-capability paragraph to be written for each level. 52 of them, 51 never written | Nothing. A level is derived from observations, not matched against prose | ADR-0013 |
| **Typed L3 criteria** | 258 criteria as scoring gates | Criteria as the **checklist behind a `practised` judgement** | ADR-0013, ADR-0014 |
| **Consumption model as a scored property** | A scored attribute of a realization | A recorded fact on the offering | ADR-0003, superseded |
| **The three registers** | Three disagreeing lists of what exists | One `facts/offerings.json` | ADR-0013 |

> **Do not restart the rubric workstream.** It is the single most likely thing to be
> re-proposed by someone who read an old document, and it is closed.

---

## 5. Words used precisely, that sound casual

| Word | Read it as |
|---|---|
| **Fact** | Something true about the Bank, with evidence and a date, that is true whichever framework reads it |
| **Derived** | Computed by a rule at build time and never stored. `check` fails if a derived value is found in `facts/` |
| **Not rated** | A **result**, not a zero. The evidence needed to place this capability has never been gathered |
| **Evidenced** | A named system, document, person or register a reviewer could go and look at |
| **Released** | An asset whose status counts as available to delivery teams. Which statuses count is declared once, in `facts/assets.json` |
| **Pending** | Built but not released. *Pre-release*, *in review* and *built, not yet distributed* all mean **one release away**, which is a more useful statement than "exists" |
| **Grade A–D** | How openable a source is by a reviewer, not how good it is. **Grade D cannot support a claim that leaves the Bank** (ADR-0010) |
| **Locus** | The clause, section or control a citation points at. A citation with no locus says *this informed the capability* without saying where |
| **Illustrative** | The report with **invented** observations, for agreeing the approach. Never for reporting. It carries a banner, a per-view badge and a watermark |
| **Advisory** | A `check` finding that does not fail the build — usually a fact that may have gone stale |

---

## 6. Where each term is defined for real

| For | Go to |
|---|---|
| The map, and every capability and criterion in it | [`../out/capability-map.md`](../out/capability-map.md) |
| The shape of every file in `facts/` | [`../facts/README.md`](../facts/README.md) |
| The contract a scale must keep, and what is adopted vs ours | [`../scales/README.md`](../scales/README.md) |
| Why the model is shaped this way | [`how-it-works.md`](how-it-works.md) |
| What is settled, and by which decision | [`what-is-settled.md`](what-is-settled.md) |
| How to run it | [`using-the-model.md`](using-the-model.md) |

# Documentation

Everything written about the model, and the order to read it in.

The repository holds three kinds of writing, and confusing them is the main way people get
lost:

| | | |
|---|---|---|
| **Explanations** | `docs/` | Why the model is shaped this way, and how to run it. Written by hand |
| **Decisions** | `docs/decisions/` | What was settled, when, and what was rejected. **Binding**. Never edited to reverse itself |
| **Views** | `out/` | What the model currently says. **Generated** — never edited, always regenerable |

If a document and a view disagree, the view is right: it was built from the facts this
morning. If a document and an ADR disagree, the ADR is right.

---

## Read in this order

### If you have ten minutes

1. [`../README.md`](../README.md) — what this is and the problem it solves
2. [`how-it-works.md`](how-it-works.md) — **the one to read if you read one thing.** Facts
   versus judgement, the four observations, how a level is derived

### If you are about to present it

3. [`../out/walkthrough.html`](../out/walkthrough.html) — **the deck.** The slides, in order:
   the problem, the map, what to challenge, the four observations, the scale, and how a
   first round starts. Open it in a browser; arrow keys move, and it prints one slide per
   page as a handout. Generated, so its figures cannot go stale
4. [`../out/capability-map.md`](../out/capability-map.md) — the taxonomy alone: 8 domains,
   52 capabilities, 258 criteria, with no observations and no levels attached. What to
   challenge, and who owns what
5. [`glossary.md`](glossary.md) — every term, and the four words that mean more than one
   thing. **Read the "readiness" entry before anyone asks**
6. [`what-is-settled.md`](what-is-settled.md) — the rules in force, each with the decision
   that settles it, and the three that were reversed
7. [`first-round.md`](first-round.md) — how to get from *nothing is rated* to a first
   defensible picture, and what a round can and cannot produce

### If you are running a round

8. [`using-the-model.md`](using-the-model.md) — the operating manual: commands, the
   workbook, ingest, and the mistakes that will bite you
9. [`../facts/README.md`](../facts/README.md) — the shape of every file you might edit

### If you are changing how it measures

**[`where-the-scales-come-from.md`](where-the-scales-come-from.md)** — the provenance of the measurement instrument: what each ladder was adapted from, what is ours, what has **not** been verified, and what was retired. Read it before defending a level to anyone.

10. [`../scales/README.md`](../scales/README.md) — the contract a scale must keep, what is
   adopted from ISO/IEC 33020 and what is ours, **and the two things that must not be
   quoted**

11. [`decisions/README.md`](decisions/README.md) — the ADR index, statuses, and how to
    record a new one
12. [`../build/README.md`](../build/README.md) — the modules and what each writes

---

## By question

| You want to know | Go to |
|---|---|
| What the 52 capabilities actually are | [`../out/capability-map.md`](../out/capability-map.md) |
| Something I can put on screen | [`../out/walkthrough.html`](../out/walkthrough.html) |
| **Why is this one a 2 and that one a 3?** | [`how-it-works.md`](how-it-works.md) §4, then the **How this scale places a level** table in any [`../out/capability-assessment-*.md`](../out/capability-assessment-level.md) |
| **Where do I record `practised`, `skilled`…?** | [`how-it-works.md`](how-it-works.md) §3 — `practised` at L3, the other three at L2, nothing at L1 |
| **How do I get a level out of four answers?** | The **Worked** table in any capability view; all scales at once in [`../out/management-report.html`](../out/management-report.html) §4 |
| Why a capability isn't rated | [`how-it-works.md`](how-it-works.md) §4 — performance is the gate |
| What `unknown` means, and why it isn't zero | [`glossary.md`](glossary.md) §2 |
| Whether "readiness" is still a thing | [`glossary.md`](glossary.md) §3 — three senses, one retired |
| Which ADR settles X | [`what-is-settled.md`](what-is-settled.md) |
| Whether a decision can be reopened | [`decisions/README.md`](decisions/README.md) — status vocabulary |
| How to start assessing | [`first-round.md`](first-round.md) |
| How to record an answer | [`using-the-model.md`](using-the-model.md) |
| What may leave the Bank | [`../out/provenance.md`](../out/provenance.md), and CLAUDE.md §8 |
| What is still open | [`../OPEN-ITEMS.md`](../OPEN-ITEMS.md) |
| **Where our scales and levels come from** | [`where-the-scales-come-from.md`](where-the-scales-come-from.md), and [`../out/provenance.md`](../out/provenance.md) §"The measurement instrument" |
| Whether a level is *standard* | [`where-the-scales-come-from.md`](where-the-scales-come-from.md) §7 |
| What must not be quoted from ISO/IEC 33020 | [`where-the-scales-come-from.md`](where-the-scales-come-from.md) §2.3 |
| Why we didn't just buy an analyst assessment | [`../README.md`](../README.md) §4, [`analysis/capability-model-comparison.md`](analysis/capability-model-comparison.md) |

---

## What is in here

| | |
|---|---|
| [`how-it-works.md`](how-it-works.md) | The design, explained without jargon. Orientation, not normative |
| [`glossary.md`](glossary.md) | Vocabulary. Live terms, retired terms, and the ambiguous four |
| [`what-is-settled.md`](what-is-settled.md) | The rules in force, digested from the ADRs. A digest, not a decision |
| [`first-round.md`](first-round.md) | The plan for getting the first observations in |
| [`where-the-scales-come-from.md`](where-the-scales-come-from.md) | Provenance of the measurement instrument. **Carries handling rules** |
| [`using-the-model.md`](using-the-model.md) | The operating manual |
| [`decisions/`](decisions/README.md) | The ADRs. **Binding.** ADR-0013 governs; read it first |
| [`provenance/`](provenance/README.md) | Where the map came from, and the findings against it |
| [`analysis/`](analysis/) | Background: comparison to market instruments, comparator scales |
| [`notes/`](notes/) | Working notes. **Never leaves the Bank** — see CLAUDE.md §8 |

### Two documents that are deliberately stale

| | |
|---|---|
| [`analysis/como-funciona-el-modelo.md`](analysis/como-funciona-el-modelo.md) | Explains the **superseded** two-scale model, in Spanish. Carries a banner saying so. To be rewritten from `how-it-works.md` once the current construct has survived a real conversation ([OPEN-ITEMS](../OPEN-ITEMS.md) #18) |
| [`../archive/`](../archive/README.md) | History. **Nothing there is current** |

---

## Conventions

- **Point at files; do not paste model content into chat or into slides.** A pasted number
  is stale the moment a fact changes.
- **Prose with a number in it is generated**, not typed — in `out/` absolutely, and as far
  as possible here. Where a hand-written document quotes a figure it says as of when.
- **`facts/` is edited. `out/` is generated. Derived values are never stored.** No finding
  is ever fixed by editing a view.

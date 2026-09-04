# Enterprise AI Capability Model

**IDB Enterprise Architecture** · what the Bank must be able to do with AI, what it has
built, and the distance between them.

---

## Four questions, four answers

| If you want to know… | Open |
|---|---|
| **What must the Bank be able to do?** | [`out/capability-assessment-level.md`](out/capability-assessment-level.md) — 8 domains, 52 capabilities |
| **What has the Bank actually built?** | Sheet 3 of the workbook, or [`facts/offerings.json`](facts/offerings.json) — 7 offerings, 20 assets |
| **Can we run AI agents?** | [`out/agent-readiness.md`](out/agent-readiness.md) — the one-pager |
| **How does any of this work?** | [`docs/how-it-works.md`](docs/how-it-works.md) — ten minutes, no jargon |

---

## The idea in one picture

```
facts/            what is TRUE about the Bank        ← you edit this
  capabilities      the map: 8 domains, 52 capabilities, 258 criteria
  offerings         what a delivery team can actually get today
  assets            the 20 standards, architectures, templates and modules
  observations      four observations per capability, each with evidence
  owners            which Bank unit owns what

scales/           rules that turn facts into a LEVEL  ← rarely changes
  capability_level  the default. Adapted from ISO/IEC 33020
  executive         a coarser lens for a steering committee

out/              VIEWS, one per scale                ← never edit, always generated
```

**An observation is a fact, not a score.** *"The Foundry Agents Standard is pre-release"*
is true whichever framework reads it. Because the facts are separate from the scales,
you can measure the same evidence two ways without reassessing anything — and two scales
can never disagree about the evidence, only about what to make of it.

---

## The four observations

You never type a level. You record four things per capability, each with evidence, and
the level is computed.

| | The question |
|---|---|
| **Practised** | Is this done on real AI systems in production, repeatedly? |
| **Enabled** | Can a team get the tooling for this without building it themselves? |
| **Skilled** | Do the people who must do this know how? |
| **Defined** | Is there a published Bank standard or method for this? |

Values: `yes` · `partial` · `no` · `n/a` (needs a reason) · `unknown` (nobody has
looked — **never** a zero).

> **Performance comes first.** A published standard with nothing performed against it
> earns **no level at all**. That ordering is ISO/IEC 33020's, not ours, and it is what
> stops *"we approved the technology"* from reading as *"we have the capability"*.

---

## Working with it

Everything runs through one command. Requires Python 3 and `openpyxl`.

```bash
python3 build/build.py            # what the model currently says
python3 build/build.py check      # validate facts/, report problems
python3 build/build.py all        # rebuild the workbook and every view
python3 build/build.py ingest     # read reviewer edits back into facts/
```

### The review loop

1. `python3 build/build.py workbook` → `out/AI-Capability-Model.xlsx`
2. Send it. **One reviewer at a time** — Excel does not merge.
3. They fill the yellow cells on sheet **2. Observations**.
4. `python3 build/build.py ingest path/to/returned.xlsx`
5. `python3 build/build.py all`, then commit.

The workbook has **no formulas**. Every derived number is computed in Python and written
as a value, so it opens identically in Excel, LibreOffice and a browser, and there is no
recalculation step to get wrong.

---

## The one rule

> **`facts/` is edited. `out/` is generated.**

Never fix a finding by editing a workbook or a view. Fix the fact and rebuild. `ingest`
is the only path that writes to `facts/`, and it only ever writes observations.

---

## Layout

| Directory | What it is | Edited? |
|---|---|---|
| [`facts/`](facts/) | **The model.** Five registers, plain keyed JSON | ✏️ |
| [`scales/`](scales/README.md) | Rules that turn observations into a level | ✏️ rarely |
| [`build/`](build/) | Four files. `build.py` is the only entry point | ✏️ |
| [`docs/`](docs/) | Everything a human reads — explainer, ADRs, analysis | ✏️ |
| [`sources/`](sources/) · [`review/`](review/) | Documents obtained · reviewer returns | 📥 |
| `out/` | **Generated.** Never edit | 🚫 |
| [`archive/`](archive/README.md) | Superseded. Kept, never deleted | 🗄️ |

---

## Where the work stands

**Nothing is rated yet, and the model says so.** Every capability is `not rated` under
the default scale, because `practised` has never been observed for any of them. What
*is* recorded is real: 20 named assets with status and location, 7 offerings, 27
in-the-box control questions, and an owner mapping against the Bank's own catalogue that
finds **8 capabilities nobody claims**.

That is the honest state, and it is the point of the design: what exists is evidenced,
what does not is visibly absent rather than silently scored.

See [`OPEN-ITEMS.md`](OPEN-ITEMS.md) for what is unresolved and what it blocks.

---

## Handling rules

- **Grade D sources cannot support a claim that leaves the Bank.** Licensed analyst
  material stays internal and is never listed as a source.
- **Cite by name, never by number**, for any list that renumbers between editions.
- **Do not invent a clause number.** Mark it unverified or say it is ours.
- **Do not quote ISO/IEC 33020's percentage bands** until someone opens the standard —
  see [`scales/README.md`](scales/README.md).

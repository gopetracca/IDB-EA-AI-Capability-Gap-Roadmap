# Using the model

The operating manual. What [`../README.md`](../README.md) describes, this explains how to
run. For why it is shaped this way, see [`how-it-works.md`](how-it-works.md).

Requires Python 3 and `openpyxl`. In this environment use `python3.13`.

---

## The commands

```bash
python3 build/build.py            # what the model currently says
python3 build/build.py check      # validate facts/, report problems
python3 build/build.py workbook   # write out/AI-Capability-Model.xlsx
python3 build/build.py views      # write the reports
python3 build/build.py all        # workbook + views
python3 build/build.py ingest [path]   # read a returned workbook back in
```

`check` must pass before and after any change. It catches claims without evidence,
`n/a` without a reason, orphaned references and missing observations.

---

## Running a review round

This is the main loop. Everything else is a variation on it.

**1 · Produce the workbook**

```bash
python3 build/build.py workbook
```

Eight sheets. Sheet 2 is the one that gets filled in; the rest are reference. There are
no formulas anywhere — every derived value is computed and written as a value, so it
opens identically in Excel, LibreOffice and a browser, and there is nothing to
recalculate.

**2 · Decide who gets it, and cut it down**

Send the whole file, or filter sheet 2 to the rows that person can answer. A capability
owner answers `practised` and `skilled` for their own capabilities. A platform team
answers `enabled` and the in-the-box questions on sheet 4. Cybersecurity, Data
Management, Legal and Learning & Development each answer `defined` for their own subject.

**One reviewer at a time.** Excel does not merge. Two returned copies of the same sheet
means one of them loses.

**3 · They fill the yellow cells**

Sheet 2, four columns: the value, the evidence, who observed it, and when. Everything
else on that sheet is reference and is regenerated.

The values, and what they mean:

| Value | Means |
|---|---|
| `yes` | Yes, and here is the evidence |
| `partial` | In some places, or incompletely. Say where |
| `no` | No. This is a real, evidenced negative |
| `n-a` | Does not apply here. **Requires a reason** |
| `unknown` | Nobody has looked. **Not a zero** |

`yes` and `partial` require evidence or `check` fails. An observation without evidence is
an opinion, and the model does not store opinions.

**4 · Read it back**

```bash
python3 build/build.py ingest ~/Downloads/returned.xlsx
python3 build/build.py all
git add -A && git commit -m "Observations from <who>, <date>"
```

`ingest` reads sheet 2 only, and only the four editable columns. It cannot damage the
capability map, the offerings or the assets. One commit per review round keeps the
history of who said what.

---

## Recording a single change

For one or two facts, edit [`../facts/observations.json`](../facts/observations.json)
directly, then `check` and `all`. The workbook is for review rounds, not for every edit.

---

## Adding to the model

**A capability** → [`../facts/capabilities.json`](../facts/capabilities.json). It also
needs four observation rows and an owner mapping. New capabilities carry
`confidence: low` until their owner validates them (ADR-0009).

**An offering** → [`../facts/offerings.json`](../facts/offerings.json). It needs
`enables` (capability ids), `assets` (ids from the asset register), and ideally its
in-the-box control list. Adding one changes the `enabled` observation for the
capabilities it enables — update those rows and cite the offering as the evidence.

**An asset** → [`../facts/assets.json`](../facts/assets.json). Status is the field that
matters: `Pre-release`, `In review` and `Built, not yet distributed` do **not** establish
that something exists. They establish that it is one release away, which is a different
and more useful statement.

**A scale** → one file in [`../scales/`](../scales/README.md) exposing `NAME`, `SHORT`,
`BASIS`, `LEVELS` and `level(obs)`. Nothing else changes; a view is generated for it
automatically. State in `BASIS` what is adopted and what is ours.

---

## What comes out

| File | For | Regenerated |
|---|---|---|
| `out/management-report.html` | **Management. The one to send** — charts, findings, decisions. Self-contained, opens offline, prints | Every build |
| `out/management-report.md` | The same report as plain text, for pasting into email or a wiki | Every build |
| `out/agent-readiness.md` | The agent question specifically | Every build |
| `out/capability-assessment-level.md` | All 52, four observations each, default scale | Every build |
| `out/capability-assessment-exec.md` | The same facts through the coarser executive lens | Every build |
| `out/AI-Capability-Model.xlsx` | Reading and reviewing | Every build |

Everything in `out/` can be deleted and rebuilt. Nothing in `facts/` can.

---

## Things that will bite you

**Do not type a level anywhere.** Levels are derived. If you are typing a number into
`facts/`, you are recording a judgement where a fact belongs.

**Do not fill in `unknown` to make a view look finished.** An unrated capability is a
true statement about the assessment. Guessing to complete the picture is the one change
that would make the model worthless.

**Do not edit `out/`.** It is overwritten on the next build. Fix the fact.

**Do not restart the rubric workstream.** Earlier versions required 52 rubrics and 258
typed criteria to derive a rating. That is closed (ADR-0013). The criteria are now the
checklist behind a `practised` judgement, not gates.

**Watch the asset statuses.** They are the cheapest roadmap items in the model and they
change without anyone updating this repository.

---

## Answering "do we have the capability to X?"

X is almost always a use case, not a capability, and touches several with different
owners. The answer is a short table, not a number:

1. Which capabilities does it touch?
2. What are the four observations for each, and who owns it?
3. Which offerings enable them, and what is still unreleased?
4. What would move each observation, and who does it?

[`../out/agent-readiness.md`](../out/agent-readiness.md) is the worked example. It is
generated, so it stays true as the facts change.

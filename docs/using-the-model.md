# Using the model

The operating manual. What [`../README.md`](../README.md) describes, this explains how to
run. For why it is shaped this way, see [`how-it-works.md`](how-it-works.md). For the shape
of every file in `facts/`, see [`../facts/README.md`](../facts/README.md).

Requires Python 3 and `openpyxl`. In this environment use `python3.13`.

---

## The commands

```bash
python3 build/build.py            # what the model currently says
python3 build/build.py check      # validate facts/ and scales/, report problems
python3 build/build.py workbook   # write out/AI-Capability-Model.xlsx
python3 build/build.py views      # write the reports and views
python3 build/build.py all        # check, then workbook + views
python3 build/build.py ingest [path ...]   # read returned workbook(s) back in
python3 build/build.py test       # run the test suite
```

`check` must pass before and after any change. It catches claims without evidence, a `no`
with nothing behind it, `n/a` without a reason, orphaned references, missing observations,
a citation that does not resolve in the source register, a derived value stored as a fact,
and a scale that breaks its contract. `all` runs it first and refuses to build if it fails.

`check` also prints **advisories**, which do not fail the build: an observation taken from
the asset register that the register no longer supports (an asset was released since), a
recorded value with no observer or date, a capability listed as needing no tooling that an
offering nonetheless enables.

---

## Running a review round

This is the main loop. Everything else is a variation on it.

**1 · Produce the workbook**

```bash
python3 build/build.py workbook
```

Ten sheets. Sheet 2 is the one that gets filled in; the rest are reference. There are no
formulas anywhere — every derived value is computed and written as a value, so it opens
identically in Excel, LibreOffice and a browser, and there is nothing to recalculate.

| Sheet | Holds | Who reads it |
|---|---|---|
| 0. Start here | What the workbook is and how to use it | Everyone |
| 1. Capabilities | The whole map three levels deep — domain, capability, criterion — each with its description, the observations against it and the derived level. Collapsible to any level. Read only | Everyone |
| **2. Observations** | **The sheet that flows back.** One row per criterion for *practised*, one per capability for the rest | Capability owners, platform teams, standard-setters |
| 3. Offerings | What a delivery team can get | Platform teams |
| 4. In the box | The 27 control questions | Platform teams |
| 5. Assets | Every asset, its status, and whether that status counts as released | Platform teams |
| 6. Criteria (L3) | The same three levels, definitions only: 8 domains, 52 capabilities, 258 criteria | Reference |
| 7. Owners | The mapping to the Bank's catalogue | The operating-model conversation |
| 8. Sources | The graded source register | The provenance reviewer |
| 9. Obligations | Statutory references, all candidate | Legal |

**2 · Decide who gets it, and cut it down**

Send the whole file, or filter sheet 2 to the rows that person can answer. A capability
owner answers `practised` (per criterion) and `skilled` for their own capabilities. A
platform team answers `enabled` and the in-the-box questions on sheet 4. Cybersecurity,
Data Management, Legal and Learning & Development each answer `defined` for their own
subject.

**Several reviewers, several files.** Each answers only their own rows, so returned files
can be ingested together. If two files set the same cell, `ingest` says so and the file
given last wins — check before you rebuild.

**3 · They fill the yellow cells**

Sheet 2, four columns: the value, the evidence, who observed it, and when. Everything
else on that sheet is reference and is regenerated.

Sheet 2 has **414 rows, not 52**, grouped into a block per capability. `practised` is
asked once per L3 criterion (ADR-0014), which is why there are more rows and why each
one names a specific practice with its definition. `enabled`, `skilled` and `defined`
are asked once per capability. A reviewer answers only for the capabilities they own.

The values, and what they mean:

| Value | Means | Requires |
|---|---|---|
| `yes` | Yes, and here is the evidence | Evidence |
| `partial` | In some places, or incompletely. Say where | Evidence |
| `no` | No. **A real, evidenced negative:** you looked, and it is not there | Evidence, or a basis saying what you looked at |
| `n/a` | Does not apply here | A reason in the basis column |
| `unknown` | Nobody has looked. **Not a zero.** The right answer when you have not looked | Nothing |

`yes` and `partial` require evidence or `check` fails. An observation without evidence is
an opinion, and the model does not store opinions. `n-a` is accepted as `n/a`.

**4 · Read it back**

```bash
python3 build/build.py ingest review/2026-09-12-owner-D4.xlsx review/2026-09-12-platform.xlsx
python3 build/build.py all
git add -A && git commit -m "Observations from <who>, <date>"
```

Returned files go in `review/`, dated and named for the reviewer, and are never edited.
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
needs an owner mapping and observation rows: three at capability level, plus one
`practised` row per L3 criterion (ADR-0014). New capabilities carry
`confidence: low` until their owner validates them (ADR-0009). Every string in its
`sources` must resolve in `facts/sources.json` → `normalize`.

**An offering** → [`../facts/offerings.json`](../facts/offerings.json). It needs
`enables` (capability ids), `assets` (ids from the asset register), and ideally its
in-the-box control list. Do **not** type release counts: they are derived from asset
statuses. Adding an offering changes the `enabled` observation for the capabilities it
enables — update those rows and cite the offering as the evidence.

**An asset** → [`../facts/assets.json`](../facts/assets.json). Status is the field that
matters. Which statuses count as released is declared once in the same file, under
`statuses`; a new status must be declared there before it is used. `Pre-release`,
`In review` and `Built, not yet distributed` do **not** establish that something exists.
They establish that it is one release away, which is a different and more useful statement.
When a status changes, `check` advises which observations were taken from the register and
may now be stale.

**A use-case question** ("can we do X?") → [`../facts/questions.json`](../facts/questions.json).
Name the offerings and capabilities it touches; write the finding with who made it and
when. A page `out/<output>.md` appears on the next build with everything else derived.

**A source** → [`../facts/sources.json`](../facts/sources.json), graded A–D (ADR-0010) and
verified first — see the `citing` skill. Add the citation string to `normalize` so the
capability that uses it resolves.

**A scale** → one file in [`../scales/`](../scales/README.md) meeting the contract there:
`NAME`, `SHORT`, `BASIS`, `QUESTION`, `LEVELS`, `level(obs)`; optionally
`DERIVABLE_MAX`, `note()`. Nothing else changes; a view is generated for it automatically
and `check` validates it. State in `BASIS` what is adopted and what is ours.

---

## What comes out

| File | For | Regenerated |
|---|---|---|
| `out/management-report.html` | **Management. The one to send** — charts, findings, decisions, and every scale over the same evidence. Self-contained, opens offline, prints | Every build |
| `out/management-report.md` | The same report as plain text, for pasting into email or a wiki | Every build |
| `out/management-report-illustrative.html` | **Sample observations.** The identical report with every chart populated, for agreeing the approach before the assessment runs. Never for reporting | Every build |
| `out/agent-readiness.md` | The agent question. One such page per entry in `facts/questions.json` | Every build |
| `out/capability-assessment-level.md` | All 52, four observations each, every criterion, default scale | Every build |
| `out/capability-assessment-exec.md`, `-maturity.md` | The same facts through each lens | Every build |
| `out/provenance.md` | Sources by grade, what rests on grade D, locus coverage, obligations | Every build |
| `out/AI-Capability-Model.xlsx` | Reading and reviewing | Every build |

Everything in `out/` can be deleted and rebuilt. Nothing in `facts/` can.

---

## Things that will bite you

**Do not type a level anywhere.** Levels are derived. If you are typing a number into
`facts/`, you are recording a judgement where a fact belongs.

**Do not write `no` for "I did not find it".** `no` is an evidenced negative and the
lenses will score it as one. If nobody has asked the owner, it is `unknown`.

**Do not present the illustrative edition as an assessment.** Its observations are
invented. It carries a banner, a per-view badge and a watermark for that reason. Use it
to agree the approach; use `management-report.html` to report. Its capability map,
offerings, assets and owners *are* real; only the observations are sampled.

**Do not fill in `unknown` to make a view look finished.** An unrated capability is a
true statement about the assessment. Guessing to complete the picture is the one change
that would make the model worthless.

**Do not edit `out/`.** It is overwritten on the next build. Fix the fact.

**Do not store a derived value.** Release counts, the capability's *practised*, levels:
computed. `check` fails if it finds one stored.

**Do not restart the rubric workstream.** Earlier versions required 52 rubrics and 258
typed criteria to derive a rating. That is closed (ADR-0013). The criteria are now the
checklist behind a `practised` judgement, not gates.

**Watch the asset statuses.** They are the cheapest roadmap items in the model and they
change without anyone updating this repository. `check` advises when an observation taken
from the register has drifted from it.

---

## Answering "do we have the capability to X?"

X is almost always a use case, not a capability, and touches several with different
owners. The answer is a short table, not a number:

1. Which capabilities does it touch?
2. What are the four observations for each, and who owns it?
3. Which offerings enable them, and what is still unreleased?
4. What would move each observation, and who does it?

[`../out/agent-readiness.md`](../out/agent-readiness.md) is the worked example. It is
generated from [`../facts/questions.json`](../facts/questions.json), so it stays true as
the facts change, and a second question is one more entry in that file.

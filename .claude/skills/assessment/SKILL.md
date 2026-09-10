---
name: assessment
description: Use when recording, changing, or reasoning about capability observations, levels, offerings, assets or use-case questions in this AI capability model — including running a review round, ingesting returned workbooks, adding a capability, offering, asset or scale, or answering "how mature is X" / "do we have the capability to Y". Also use when someone hands you a level, a score or a "no" to write down.
---

# Working with the capability model

Facts live in `facts/` (schemas: `facts/README.md`). Scales turn facts into levels. `out/`
is generated. Full explanation: `docs/how-it-works.md`. Governing decisions: ADR-0013 and
ADR-0014.

## Before anything else

```bash
uv run python build/build.py            # what the model currently says
uv run python build/build.py check      # validate facts/ and scales/, must pass
uv run python build/build.py test       # tests/, must pass
```

`check` must pass before and after any change. It catches unevidenced claims, an
unevidenced `no`, `n/a` without a reason, orphaned references, missing observations,
citations that do not resolve, derived values stored as facts, and a scale that breaks its
contract. Its **advisories** do not fail the build but each one is a question to answer
before the next report goes out.

## The rules that are easy to get wrong

1. **Never write a level anywhere.** Levels are derived by `scales/`, always. If someone
   tells you "4.4 is Level 1", that is a conclusion, not an observation: record what they
   saw, per criterion, and let the scale say what level it is. If the derived level differs
   from the number they gave, that difference is the finding.
2. **Never edit `out/`.** Fix the fact, rebuild. `build.py ingest` is the only program that
   writes to `facts/`, and only to observations.
3. **`unknown` is not zero.** It means nobody has looked. Do not "fill it in" with a guess
   to make a view look complete — an unrated capability is a true statement.
4. **`no` is an evidenced negative.** Someone looked and it is not there, and the record
   says what they looked at. "We did not find it in the register" is `unknown`, not `no`,
   until the owner has been asked. `check` rejects a `no` with neither evidence nor basis.
5. **`n/a` needs a reason** in the basis field, or `check` fails. For `enabled`, the reason
   is also recorded in `facts/enablement-context.json`.
6. **`yes` and `partial` need evidence**, or `check` fails. An observation with no evidence
   is an opinion.
7. **Performance gates everything.** Without `practised`, no level is derived, however good
   the tooling and standards are. That is deliberate (ADR-0013). **`practised` is observed
   per L3 criterion, never at L2** (ADR-0014). The capability value is rolled up by
   `Model.roll_up`: `yes` only if every criterion was examined and every one passed; any
   unexamined criterion holds it at `partial`; one examined `no` with the rest unexamined
   reads `no`. The asymmetry is deliberate. The other three observations stay at L2.
8. **Derived values are never stored.** Release counts on offerings come from asset
   statuses; the capability's `practised` comes from its criteria; levels come from scales.
   `check` fails if it finds one typed.
9. **`defined` is not "did EA write it".** The standard-setter is whoever owns the subject:
   Cybersecurity, Data Management, Legal, HR, a platform team, or EA. Architecture is the
   accountable owner of 2 of 52 capabilities. Do not write the model as though it were the
   centre of it.
10. **A lens is not the assessment.** Where `executive.py` or `maturity.py` disagree with the
    default scale, the default is the finding.

## Recording what you learned

Edit `facts/observations.json` directly for one or two changes: find the row by
`capability` + `observation` (+ `criterion` for `practised`), set `value`, `evidence`,
`observed_by`, `observed_on` (`YYYY-MM-DD`), and `basis` if the value is `n/a` or `no`. Keep
the file's form (indent 1, no trailing newline; `facts.save_facts` does it).

Overriding a value that was seeded from the offerings/asset register with a human answer
also retires the register-drift advisory on that row — `check` only re-raises it while
`observed_by` still contains the literal text "asset register." Once a name replaces it,
the row is a human observation and stands until a human changes it again; nothing further
to do.

For a review round, use the workbook:

```bash
uv run python build/build.py workbook              # out/AI-Capability-Model.xlsx
# send it; reviewers fill yellow cells on sheet 2; returns go in review/, dated
uv run python build/build.py ingest review/<date>-<who>.xlsx [review/<date>-<who2>.xlsx ...]
uv run python build/build.py all                   # check, then workbook + views
```

Ingest reads sheet 2 only: value, evidence, observed_by, observed_on. It never touches
capabilities, offerings or assets. Several files can be given at once; a cell set by more
than one is reported, and the last file wins.

## Answering "do we have the capability to X"

X is almost always a use case, not a capability, and touches several with different
owners. Do not answer with one number. Add an entry to `facts/questions.json` naming the
offerings and capabilities it touches and the finding (attributed and dated), then build:
a page `out/<output>.md` appears with the release state, the pending assets, the
in-the-box controls, the four observations per capability and what moves next, all
derived. `out/agent-readiness.md` is the worked example.

## Adding things

**A capability** → `facts/capabilities.json`, plus observation rows in
`facts/observations.json` (three at capability level, one `practised` row per criterion,
all `unknown` unless you have evidence today), plus an entry in `facts/owners.json`. Its
`sources` strings must resolve in `facts/sources.json` (the `citing` skill). New
capabilities carry `confidence: low` until the owner validates them (ADR-0009).

**An offering** → `facts/offerings.json`. It needs `enables` (capability ids), `assets`
(ids from `facts/assets.json`), and ideally `in_the_box` control rows. Do not type release
counts. Adding one changes the `enabled` observation for the capabilities it enables —
update those rows with the offering as evidence.

**An asset** → `facts/assets.json`. Status matters more than anything else, and a status
must be declared under `statuses` (with whether it counts as released) before it is used.
`Pre-release` and `In review` do not establish that something exists, they establish that
it is one release away. When a status changes, `check` advises which observations taken
from the register may now be stale; re-observe them, do not let the seed rule overwrite a
human answer.

**A scale** → one file in `scales/` meeting the contract in `scales/README.md` (`NAME`,
`SHORT`, `BASIS`, `QUESTION`, `LEVELS`, `level(obs)`; optionally `DERIVABLE_MAX`, `note()`;
exactly one scale carries `DEFAULT = True`). Nothing else changes; a view is generated for
it and `check` validates it. Adding or retiring a scale is a decision: the `decisions` skill.

## What not to rebuild

The rubric and criteria-typing workstreams are closed (ADR-0013). The 258 L3 criteria carry
a `practised` observation each (ADR-0014), but they are still not gates: no rubric, no
mandatory/conditional/enhancing typing. Recording an observation against a criterion is not
reopening the rubric workstream. If a task seems to need 52 rubrics, re-read ADR-0013 and
ADR-0014 before starting.

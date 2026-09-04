---
name: assessment
description: Use when recording, changing, or reasoning about capability observations, levels, offerings or assets in this AI capability model — including running a review round, ingesting a returned workbook, adding a capability or offering, adding a scale, or answering "how mature is X" / "do we have the capability to Y". Enforces facts-before-scores and the build/ingest loop.
---

# Working with the capability model

Facts live in `facts/`. Scales turn facts into levels. `out/` is generated.
Full explanation: `docs/how-it-works.md`. Governing decision: ADR-0013.

## Before anything else

```bash
python3.13 build/build.py            # what the model currently says
python3.13 build/build.py check      # validate facts/, must pass
```

`check` must pass before and after any change. It catches unevidenced claims,
`n/a` without a reason, orphaned references and missing observations.

## The rules that are easy to get wrong

1. **Never write a level anywhere.** Levels are derived by `scales/`, always.
   If you find yourself typing a number into `facts/`, stop — you are recording
   a judgement where a fact belongs.
2. **Never edit `out/`.** Fix the fact, rebuild. `build.py ingest` is the only
   path that writes to `facts/`, and only to observations.
3. **`unknown` is not zero.** It means nobody has looked. Do not "fill it in"
   with a guess to make a view look complete — an unrated capability is a true
   statement about the assessment.
4. **`n/a` needs a reason** in the basis field, or `check` fails.
5. **`yes` and `partial` need evidence**, or `check` fails. An observation with
   no evidence is an opinion.
6. **Performance gates everything.** Without `practised`, no level is derived,
   however good the tooling and standards are. That is deliberate (ADR-0013).

## Recording what you learned

Edit `facts/observations.json` directly for one or two changes. For a review
round, use the workbook.

```bash
python3.13 build/build.py workbook              # out/AI-Capability-Model.xlsx
# send it; reviewer fills yellow cells on sheet 2; one reviewer at a time
python3.13 build/build.py ingest path/to/returned.xlsx
python3.13 build/build.py all
```

Ingest reads sheet 2 only: value, evidence, observed_by, observed_on. It never
touches capabilities, offerings or assets.

## Answering "do we have the capability to X"

X is almost always a use case, not a capability, and touches several with
different owners. Do not answer with one number.

1. Find the capabilities it touches (`facts/capabilities.json`).
2. Show the four observations per capability and the owner.
3. Name the offerings that enable them and what is still unreleased
   (`facts/offerings.json`, `facts/assets.json`).
4. Say what would move the observation, and who does it.

`out/agent-readiness.md` is the worked example of this shape.

## Adding things

**A capability** → `facts/capabilities.json`, plus four observation rows in
`facts/observations.json` (start `unknown` unless you have evidence today), plus
an entry in `facts/owners.json`. New capabilities carry `confidence: low` until
the owner validates them (ADR-0009).

**An offering** → `facts/offerings.json`. It needs `enables` (capability ids),
`assets` (ids from `facts/assets.json`), and ideally `in_the_box` control rows.
Adding one changes the `enabled` observation for the capabilities it enables —
update those rows with the offering as evidence.

**An asset** → `facts/assets.json`. Status matters more than anything else:
`Pre-release` and `In review` do not establish that something exists, they
establish that it is one release away.

**A scale** → one file in `scales/` exposing `NAME`, `SHORT`, `BASIS`, `LEVELS`
and `level(obs)`. Nothing else changes; views are generated per scale. State in
`BASIS` what is adopted and what is ours (ADR-0010).

## What not to rebuild

The rubric and criteria-typing workstreams are closed (ADR-0013). The 258 L3
criteria are the checklist behind a `practised` judgement, never gates. If a
task seems to need 52 rubrics, re-read ADR-0013 before starting.

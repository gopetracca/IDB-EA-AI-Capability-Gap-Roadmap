# Returned workbooks

Workbooks that came back from a reviewer. **Nothing here is ever edited.**

They are the record of who said what, and when. `build.py ingest` reads sheet 2 of each and
applies the four editable columns to `facts/observations.json`; the file itself stays
exactly as the reviewer sent it, so a value in `facts/` can always be traced back to the
sheet a named person filled in.

## Naming

```
YYYY-MM-DD-<who>.xlsx
```

The date the file came back, and the reviewer or unit — `2026-09-12-platform.xlsx`,
`2026-09-12-cybersecurity.xlsx`, `2026-09-12-owner-D4.xlsx`. One file per reviewer, even
when several arrive on the same day.

## Reading them in

```bash
uv run python build/build.py ingest review/2026-09-12-platform.xlsx review/2026-09-12-cybersecurity.xlsx
uv run python build/build.py check
uv run python build/build.py all
git add -A && git commit -m "Observations from <who>, <date>"
```

Several files ingest together: each reviewer answers only their own rows. **If two files set
the same cell, `ingest` says so and the file given last wins** — resolve it with the
reviewers before rebuilding rather than letting argument order decide a fact.

`ingest` reads sheet 2 only, and only the value, evidence, observer and date columns. It
cannot damage the capability map, the offerings, the assets or the owners.

Expect `check` to fail on a first round — a `yes` with no evidence, a `no` with no basis, an
`n/a` with no reason. That is the instrument working. Go back to the reviewer with the
specific row; do not soften the value to make the build pass.

One commit per round.

## What goes where

| | |
|---|---|
| **Here** | Workbooks as they came back, unedited |
| [`../facts/`](../facts/README.md) | What was extracted from them — the observations themselves |
| [`../out/`](../out/README.md) | Everything generated afterwards. Deletable, regenerable |

Full instructions: [`../docs/using-the-model.md`](../docs/using-the-model.md).
The plan for the first round: [`../docs/first-round.md`](../docs/first-round.md).

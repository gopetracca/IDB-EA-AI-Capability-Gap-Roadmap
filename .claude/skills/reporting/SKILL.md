---
name: reporting
description: Use when adding, changing or reviewing anything that renders the model — a view, a chart, a section of the management report, the illustrative edition, a Markdown page, or a sheet of the workbook — or when a reader asks why a chart is empty, why a number in the report differs from the facts, or how to show the facts through another frame.
---

# Changing what the model shows

The rule that governs every view: **a view renders facts; it never stores, guesses or types
one.** `build/` reads `facts/` through `facts.Model` and writes `out/`. If a sentence would
go stale when a fact changes, it is generated from the fact. Full map of the builders:
`build/README.md`.

## Before you start

```bash
python3.13 build/build.py check     # must pass; advisories are fine
python3.13 build/build.py test      # tests/; several are about the views
```

Then find the right place:

| You want to change… | Edit | Not |
|---|---|---|
| A chart's geometry or colour | `build/charts.py` | the report or the sample module |
| A section of the HTML report | `build/build_report.py` | `out/*.html` |
| A Markdown page (capability view, question page, provenance) | `build/build_views.py` | `out/*.md` |
| A sheet of the workbook | `build/build_workbook.py` | the `.xlsx` |
| What the illustrative edition shows | `build/sample.py` | anything that touches `facts/` |
| A number that is wrong | `facts/` — then rebuild | any builder |

## The shape of a view

A view is: **a heading · a one-line description · the chart or table · the legend · at most
one paragraph of interpretation**, and when the facts it needs do not exist, an **honest
empty state** (`charts.empty_state(title, what is missing, who supplies it)`) instead of a
chart. Populate it in the illustrative edition; in the live edition, empty means empty.

Every number in prose comes from the same variables the chart is drawn from:

```python
en = collections.Counter(obsv[c['id']]['defined'] for c in m.capabilities)
w('<p>%d capabilities have an approved standard.</p>' % en['yes'])   # yes
w('<p>10 capabilities have an approved standard.</p>')               # no — will be wrong next month
```

Section numbers, forward references ("listed in Section 6"), the count of usable views and
which scales gate on performance are all computed already; follow those patterns.

## What the code must not know

- **Which scales exist.** `F.load_scales()` gives all; `F.default_scale()` the default;
  each has `NAME`, `SHORT`, `QUESTION`, `BASIS`, `LEVELS`, `DERIVABLE_MAX`. A test fails if
  a builder contains a scale's `SHORT` as a string.
- **Which questions exist.** Iterate `m.questions`.
- **Which statuses count as released.** `m.released(asset)`, `m.release_count(offering)`,
  `m.pending_assets()`.
- **`practised` at capability level.** `m.values(cid)` (rolled up) or
  `m.criteria_obs(cid, 'practised')`. `m.obs_by_cap[...]['practised']` raises on purpose.

## Sample data

The illustrative edition wraps the real model in `sample.Demo` and substitutes observations
in memory. Every sample view carries the `SAMPLE` tag and the watermark; the page carries
the banner. Nothing from `sample.py` may be written anywhere. If a view needs a new derived
input in demo mode (targets, for instance), add it to `sample.py` and pass it in; do not
invent it inside the view.

## Palette and tone

Navy ramp, one warm accent for the thing to act on, palest tone for *nobody has looked*.
No traffic lights. `charts.C` for observation values, `charts.LVL` for levels,
`charts.legend()` for legends. Not-rated is never drawn as zero: it is the pale segment
at the end of the bar.

## After the change

```bash
python3.13 build/build.py all       # check, workbook, views
python3.13 build/build.py test
git diff --stat facts/              # must be empty unless you meant to change a fact
```

Open `out/management-report.html` **and** `out/management-report-illustrative.html`: the
new view must read correctly with real facts and with sample ones, and the tag on it must
say which it is.

## Common mistakes

| Mistake | Why it matters | Instead |
|---|---|---|
| Typing a count into prose | Wrong the moment a fact changes; nobody notices | Compute it beside the chart |
| Filling an empty view with an estimate | An estimate quoted once becomes the number | `charts.empty_state`, naming who supplies the fact |
| Editing `out/` to fix a finding | Overwritten on the next build; the fact stays wrong | Fix the fact, rebuild |
| Naming a scale or a question in code | Adding one no longer adds a view | Iterate `load_scales()` / `m.questions` |
| Hard-coding the released statuses | Drifts from `facts/assets.json` | `m.released()` |
| A new view only in the live edition | The illustrative edition is how the approach is agreed | Both, with the right tag |
| Reading level numbers across scales as if comparable | A 1–5 ladder against 0–3 "reads higher" by construction | `_comparable()` in the report already handles this; follow it |

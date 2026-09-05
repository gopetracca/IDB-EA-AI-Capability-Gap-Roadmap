# `build/` — one command, seven modules

```bash
python3 build/build.py            # status: what the model currently says
python3 build/build.py check      # validate facts/ and scales/; must pass
python3 build/build.py workbook   # out/AI-Capability-Model.xlsx
python3 build/build.py views      # every view in out/
python3 build/build.py all        # check, then workbook + views
python3 build/build.py ingest [path ...]   # read returned workbook(s) into facts/
python3 build/build.py test       # the test suite (tests/)
```

Python 3 and `openpyxl` only. In this environment use `python3.13`.

| Module | Role | Reads facts/? | Names a scale? |
|---|---|---|---|
| `build.py` | Entry point: status, check, workbook, views, ingest, test | via `facts` | no |
| `facts.py` | **The only module that opens `facts/*.json`.** `Model` joins everything; `roll_up_values` is ADR-0014; `load_scales` / `default_scale` / `validate_scale(s)` discover and check `scales/` | yes | no |
| `build_workbook.py` | The ten-sheet review workbook, no formulas | no | no |
| `build_views.py` | Markdown: one capability page per scale, one page per question, the text report, the provenance view | no | no |
| `build_report.py` | The self-contained HTML management report, live and illustrative | no | no |
| `charts.py` | Inline-SVG primitives and the palette, shared by the report and its illustrative edition | no | no |
| `sample.py` | SAMPLE observations for the illustrative edition, generated in memory, never written | no | no |

**Adding a scale** changes nothing here: `facts.load_scales()` lists `scales/`, and every
builder iterates. **Adding a question** to `facts/questions.json` adds a view. **Adding a
fact file** means one loader line in `facts.Model.__init__`, a `check` rule in
`build.check`, and a paragraph in `facts/README.md`.

## Rules the code keeps

- **Nothing in `out/` is edited.** Every derived value is computed and written as a value;
  the workbook has no formulas, so there is no recalc step.
- **`check` before `all`.** `all` refuses to build from facts that fail validation, because
  the numbers in the views would be wrong. Advisories (register drift, a value without a
  date) print but do not fail.
- **Sample data never reaches `facts/`.** `sample.Demo` wraps the real model and substitutes
  observations in memory. A test asserts the facts digest is unchanged by a build.
- **Prose with a number in it is computed**, in both report builders. If a sentence would go
  stale when a fact changes, generate it from the fact.
- **Never read `obs_by_cap[...]['practised']`.** It raises on purpose (ADR-0014). Use
  `Model.values(cid)` for the four rolled-up values, `Model.criteria_obs(cid, 'practised')`
  for the rows.

## Ingest

`ingest_workbook(path, doc)` is pure: it applies sheet 2 of one workbook to an
observations document in memory and returns what changed and what was skipped.
`cmd_ingest` runs it over one or more files in order and reports any cell set by more than
one file, because the last file wins and someone should know that it did. Only the four
yellow columns (value, evidence, observed by, date) are read; `n-a` is accepted as `n/a`.

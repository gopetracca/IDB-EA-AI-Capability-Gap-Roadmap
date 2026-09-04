# The builders before the refactor

Eleven files, replaced by four in `build/`.

| File | Built | Replaced by |
|---|---|---|
| `build_wb.py` | The 13-sheet workbook, with Excel formulas throughout | `build/build_workbook.py` — no formulas |
| `build_md.py` | The capability register Markdown | `build/build_views.py` |
| `build_tax.py`, `build_prov.py` | The two reviewer workbooks | Sheet 2 of the one workbook |
| `run.py` | Assembled a flat temp directory so the builders could find each other | Nothing. `build/build.py` imports properly |
| `recalc.py`, `office/soffice.py` | Drove LibreOffice to recalculate formulas, a mandatory ship gate | **Nothing, and nothing is needed.** Derived values are computed in Python and written as values |
| `wb_data.py`, `wb_assets.py` | Scales, realizations, control checklists, assets — **model data in build/** | `facts/*.json` |
| `prov_data.py` | Loaded the source register | `facts/sources.json` is read directly |

The formulas in `build_wb.py` are worth one look if you ever wonder why the workbook now
has none: sheet 2 column I was a single nested `COUNTIFS` expression roughly fifteen
lines long, and it could not be checked by reading it.

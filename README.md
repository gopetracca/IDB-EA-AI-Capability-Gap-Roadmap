# Enterprise AI Capability Model

**IDB Enterprise Architecture** · AI maturity assessment, capability map, gap analysis and roadmap

A capability model for AI at the Bank, and the assessment instruments built on it.

**8 domains · 52 L2 capabilities · 258 L3 criteria**

---

## The one rule

> **`model/` is edited. `out/` is generated.**

Never fix a finding by editing a workbook. Fix it in the model and rebuild. Every workbook,
Markdown file and HTML artifact is reproducible from `model/` plus `build/` — that is what makes
the assessment defensible rather than a set of spreadsheets that have quietly drifted apart.

Anything in `out/` can be deleted and regenerated. Nothing in `model/` can.

---

## Layout

| Directory | What it is | Edited? |
|---|---|---|
| [`decisions/`](decisions/README.md) | **ADRs** — how the model is structured, one decision per file | ✏️ |
| [`model/`](model/) | **The model** — capabilities, catalog, realizations, obligations, sources | ✏️ |
| [`build/`](build/) | **The builders** — everything in `out/` comes from here | ✏️ |
| [`provenance/`](provenance/README.md) | **Where the data came from** — grading rule, findings log | ✏️ |
| [`analysis/`](analysis/) | **Worked reasoning** — comparisons, explainers, rationale | ✏️ |
| [`sources/`](sources/) | Source documents obtained for the work | 📥 |
| [`review/`](review/README.md) | Reviewer returns, one dated file per return | 📥 |
| [`notes/`](notes/) | Scratch. Not authoritative | 🗒️ |
| `out/` | **Generated.** Never edit | 🚫 |

## Start here

| If you want to… | Read |
|---|---|
| Understand how the model works | [`analysis/como-funciona-el-modelo.md`](analysis/como-funciona-el-modelo.md) *(ES)* |
| Know why it is structured this way | [`decisions/README.md`](decisions/README.md) |
| Know what is unresolved | [`OPEN-ITEMS.md`](OPEN-ITEMS.md) |
| Know where a claim came from | [`provenance/README.md`](provenance/README.md) |
| Defend the two scales to a reviewer | [`decisions/adr/0011-scale-provenance.md`](decisions/adr/0011-scale-provenance.md) |
| Rebuild the deliverables | *Rebuilding*, below |

---

## The two scales

The single most important thing to understand — [ADR-0001](decisions/adr/0001-two-scales-never-merged.md):

| | **Maturity** | **Readiness** |
|---|---|---|
| Attaches to | An L2 **capability** | A **realization** (capability × pattern × technology) |
| Asks | Can the institution *do* this, to what standard, with what evidence? | Has the enterprise *packaged* this well enough to consume? |
| Scale | 1–5, evidence-gated, plus 0 / NE / UC / NA | 0–5, structural, read by inspection |
| Owner | The accountable capability owner | The platform |
| Clock | 5–10 years | Quarterly |

**The gap between them is the finding.** Never merge them, and never write a readiness level into
the capability catalog. Both numbers or neither.

---

## The model

| File | Holds |
|---|---|
| `model/model3.json` | 8 domains, 52 L2 capabilities, 258 L3 criteria |
| `model/catalog4.py` | Reference catalog — 143 entries (76 services, 57 ABBs, 5 patterns, 5 standards) |
| `model/realization.json` | Realizations, readiness and consumption definitions |
| `model/obligations.json` | 18 statutory references — Legal-owned, all candidate |
| `model/sources.json` | Verified source register — 40 sources, graded A–D |
| `model/idb-assets.json` | Enterprise asset register |
| `model/idb_owners.py` | Owner assignments |

---

## Rebuilding

Everything runs through `build/run.py`, from inside `build/`. Requires Python 3 and `openpyxl`.

    cd build
    python run.py build_tax.py

`run.py` assembles a flat working directory from `model/`, `build/` and `out/`, runs the builder
there, and copies anything new or changed into `out/`. **Nothing in `model/` is ever written to.**
Run it with no arguments to list the builders.

| Builder | Produces |
|---|---|
| `build_tax.py` | `AI-Capability-Taxonomy-for-review.xlsx` |
| `build_prov.py` | `AI-Capability-Provenance-for-review.xlsx` |
| `build_wb.py` | `Enterprise-AI-Capability-Model.xlsx` — the 13-sheet assessment workbook |
| `build_md.py` | `Enterprise-AI-Capability-Model.md` |
| `mkregister.py` | `register.json` — feeds the TRM |
| `gen_trm.py` | `trm_data.js` (needs `register.json` first) |
| `gen_views_data.py` | `views_data.json` — **illustrative scores, not an assessment** |

After any workbook build:

    python recalc.py ../out/<file>.xlsx

**Ship only on `"status": "success"` with zero errors.**

> ⚠ In the current environment `recalc.py` cannot run — LibreOffice is not on `PATH` — and
> `openpyxl` is only installed for `python3.13`. See [`OPEN-ITEMS.md`](OPEN-ITEMS.md) #13.

---

## Handling rules that are easy to break

- **Cite by name, never by number**, for any list whose numbering changes between editions — the
  OWASP Top 10 above all.
- **NIST AI RMF locus form is `GOVERN 1.1`**, not hyphenated. The hyphenated form belongs to
  AI 600-1 action ids (`GV-1.1-001`).
- **Licensed analyst material** is usable inside the Bank, never reproduced externally, and never
  listed as a source in the model.
- **Grade D cannot support a claim in anything that leaves the Bank.**
- **Do not invent a clause number.** Mark it unverified or reclassify as Synthesized.
- **Never average or median an ordinal maturity score.** The rubric is gated.
- **Excel formulas must survive LibreOffice recalc.** Excel-2007-era functions only — no XLOOKUP,
  FILTER, SORT, UNIQUE. `SUMPRODUCT(MAX(...))` instead of MAXIFS.
- **`views_data.json` is invented.** Never quote it.

---

## Working agreement

- **One session per workstream**, not one per project. Natural splits: taxonomy validation ·
  provenance pinning · the risk instrument · views and deliverables.
- **Point at files, don't paste model content into chat.**
- **Decisions go to `decisions/` as they settle**, not at the end.

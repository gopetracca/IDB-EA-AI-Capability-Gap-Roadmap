# AI Capability Model — working brief

**IDB Enterprise Architecture · AI maturity assessment, capability map, gap analysis and roadmap**
Last updated 4 September 2026 · ADR refactor, `analysis/` and `provenance/` split

Read this first — you and Claude both. It exists so a new session starts warm instead of
re-deriving decisions that are already settled. It is not a summary of past conversations; it is
the set of conventions that govern the work.

---

## 1. What this is

A capability model for AI at the Bank, and the assessment instruments built on it:

- **8 domains · 52 L2 capabilities · 258 L3 criteria** — `model/model3.json`
- **143-entry reference catalog** (76 services, 57 ABBs, 5 patterns, 5 standards) — `model/catalog4.py`
- **Realization and readiness register** — `model/realization.json`
- **Obligations register** — 18 statutory references, all candidate, Legal-owned — `model/obligations.json`
- **Verified source register** — 40 sources with edition, date, access and evidence grade — `model/sources.json`
  (`build/prov_data.py` only loads it)

Deliverables in `out/`, generated. Reviewer returns in `review/`.

**Decisions are ADRs.** `decisions/adr/NNNN-*.md`, one per file, indexed in `decisions/README.md`,
**which is canonical** — the claude.ai Project doc is now a mirror. The old `D1`–`D10` identifiers
still name the same records (alias table in that README), but `D1`–`D8` are *also* the eight domain
ids. **Write `ADR-0001` for a decision and `domain D3` for a domain; never rewrite a D-number
mechanically.**

| Where | What |
|---|---|
| `decisions/adr/` | The 12 ADRs. 0001–0011 accepted, **0012 proposed** |
| `analysis/` | Reasoning written to be handed to someone else — comparison, comparators, the Spanish explainer |
| `provenance/` | The grading rule, dated verification findings, and what feeds the reviewer workbook |
| `notes/` | Scratch. `external-model-screenshots.md` is **grade D, internal only** |

## 2. The rule that governs everything else

**`model/` is edited. `out/` is generated.**

Never fix a finding by editing a workbook. Fix it in the model and rebuild. The workbooks, the
Markdown and the HTML artifacts are all reproducible from `model/` plus `build/` — that is what
makes the assessment defensible rather than a set of spreadsheets that have quietly drifted apart.

## 3. Settled decisions

Full text in `decisions/adr/`, indexed in `decisions/README.md`. The ones that come up most —
old alias in brackets:

**ADR-0001 (D1) — two scales, never merged.** A *capability* carries **maturity** (1–5, evidence-gated, plus
states 0/NE/UC/NA). A *realization* carries **readiness** (0–5, structural, read by inspection).
The gap between them is the finding. Never write a readiness level into the capability catalog —
the workbook enforces this: sheet 1 column M is a locked formula pulling the best readiness from
sheet 2. Provenance and the answer to *"is this standard?"* are in **ADR-0011**:
**maturity adopted (CMMI lineage), readiness synthesized — nothing available measured enterprise
packaging, TRL included.**

**ADR-0002 (D2) — readiness levels.** 0 Not available · 1 Available/project-proven · 2 Approved ·
3 Standardized · 4 Industrialized · 5 Productized. Level 5 is not the target everywhere.

**ADR-0003 (D3) — consumption model** (Guidance · Building blocks · Reference implementation · Managed
platform · Service/API) is recorded on the realization, not the capability.

**ADR-0004 (D4) — objects.** Capability → Pattern → ABB → SBB, plus Service. Technology offering and deployed
instance are *fields on the SBB*, not model objects. An SBB may be procured **or developed** — our
Terraform modules are SBBs. A pattern is not a name: it needs problem, context, forces, solution,
resulting context, rationale, known uses.

**ADR-0005 (D5) — two registers kept apart.** Reference catalog (what could exist, vendor-neutral) vs
realization catalog (what IDB actually provides).

**ADR-0006 (D6) — one primary domain per subject**, plus typed links. The eight domains are reporting
clusters, not a lifecycle.

**ADR-0007 (D7) — anchoring is provisional.** Every capability carries New / Specialization / **Lens**.
*Lens means do not create a node* — keep the existing enterprise capability and attach an AI
profile. Unverified until the Bank's existing capability map is crosswalked.

**ADR-0008 (D8) — statutory references live outside the model**, in a Legal-owned register, all marked
candidate. `7.6.6 Regulatory Role Determination` is the prerequisite.

**ADR-0009 (D9) — the taxonomy is validated before anything is scored against it.** `1.5 AI Ecosystem &
Alliance Management` and `2.6 AI Innovation & Incubation` were added 3 September 2026; `8.6.4` was
removed into `2.6.5`.

**ADR-0010 (D10) — provenance is graded by whether a reviewer can open it.** A = open, dated, versioned,
standards body. B = open and dated but vendor or non-normative. C = undated, superseded, flagged
historical, or paywalled. D = non-public or not a publication. **Grade D cannot support a claim in
anything that leaves the Bank.**

## 4. Rules that are easy to break

- **Cite by name, never by number**, for any list whose numbering changes between editions. The
  OWASP Top 10 above all.
- **NIST AI RMF locus form is `GOVERN 1.1`** — function, space, category.subcategory. Not
  hyphenated. The hyphenated form belongs to AI 600-1 action ids (`GV-1.1-001`).
- **Gartner material is licensed.** Usable inside the Bank; never reproduced in anything that
  circulates externally, and never listed as a source in the model. Any crosswalk lives in an
  internal-only sheet citing the document number.
- **The World Bank slide is a maturity model, not a readiness scale.** It is titled *Maturity
  Model* (Initial → Optimizing); the "readiness" in its deck title names the subject, not a scale.
  Grade D — *Official Use Only*, no date, no URL. Never cite it outside the Bank, never add it to
  `model/sources.json`. **ADR-0011** §2.4.
- **Do not invent a clause number.** If a locus cannot be verified against the source text, mark it
  unverified or reclassify the capability as Synthesized. A citation that does not resolve is worse
  than an honest "we assembled this."
- **Never average or median an ordinal maturity score.** The rubric is gated: the rating is the
  highest level for which every applicable mandatory criterion at that level and all lower levels is
  met by valid evidence.
- **Excel formulas must survive LibreOffice recalc.** Excel-2007-era functions only; no XLOOKUP,
  FILTER, SORT, UNIQUE. `SUMPRODUCT(MAX(...))` instead of MAXIFS. Always run
  `recalc.py` and ship only at zero errors.

## 5. Known open items

**All of them live in `OPEN-ITEMS.md`** — 13 items, grouped by what they block. Do not keep a
second copy here; it drifts.

The four that change what you may do:

- **Grade-D sources back 4 capabilities** and "institutional practice" is used 6 times — both
  block external publication (`provenance/findings-2026-09-03.md`).
- **Control mapping is absent** — carve `ADR-0007` (D7) out of any approval request.
- **51 of 52 rubrics do not exist** — every rating is provisional and must be labelled so.
- **No target state exists anywhere in `model/`**, so the roadmap cannot yet be generated. Sheet 5
  computes the gap but its Target column references a column nobody has filled.

## 6. Rebuilding

Everything runs through `build/run.py`, from inside `build/`. Requires Python 3 and `openpyxl`.

    cd build
    python run.py build_tax.py

`run.py` assembles a flat working directory from `model/`, `build/` and `out/`, runs the builder
there, and copies anything new or changed into `out/`. **Nothing in `model/` is ever written to.**
Run it with no arguments to list the builders.

| Builder | Produces |
|---|---|
| `build_tax.py` | `AI-Capability-Taxonomy-for-review.xlsx` — the taxonomy review workbook |
| `build_prov.py` | `AI-Capability-Provenance-for-review.xlsx` — the provenance review workbook |
| `build_wb.py` | `Enterprise-AI-Capability-Model.xlsx` — the 13-sheet assessment workbook |
| `build_md.py` | `Enterprise-AI-Capability-Model.md` |
| `mkregister.py` | `register.json` — feeds the TRM |
| `gen_trm.py` | `trm_data.js` for the TRM artifact (needs `register.json` first) |
| `gen_views_data.py` | `views_data.json` — **illustrative scores, not an assessment** |

After any workbook build:

    python recalc.py ../out/<file>.xlsx

Ship only on `"status": "success"` with zero errors.

⚠ **In this environment `recalc.py` cannot run** — LibreOffice is not on `PATH`. `openpyxl` is
installed only for `python3.13`, so builders need `python3.13 run.py <builder>`. All six builders were verified working from
this layout on 4 September 2026.

## 7. Working agreement

- **One session per workstream**, not one per project. Natural splits: taxonomy validation ·
  provenance pinning · the risk instrument · views and deliverables.
- **Point at files, don't paste model content into chat.**
- **Decisions go to `decisions/adr/`** as they are settled, not at the end — new file, next free
  number, row in the README index. An ADR is never edited to reverse itself: a reversal is a new
  ADR that supersedes it. Mirror to the Project doc afterwards.
- Anything in `out/` can be deleted and regenerated. Nothing in `model/` can.

## 8. Where things are

| | |
|---|---|
| This folder | OneDrive → Projects → IDB-EA-AI-Capability-Gap-Roadmap |
| Decisions, canonical | **`decisions/README.md` + `decisions/adr/`, in this repo.** The claude.ai Project doc is a mirror — update it after a decision settles here |
| Published artifacts | Capability register · TRM · Capability Views Catalogue (claude.ai artifacts) |
| Illustrative data warning | `views_data.json` and everything drawn from it is invented. Never quote it. Only **1 of 5 realizations** is confirmed (`conf: true`) — the rest are marked *ILLUSTRATIVE*. |
| Strip before external circulation | Gartner material anywhere · the World Bank slide and its wording · **ADR-0011** §2.4 and §3.4 · everything in `notes/` |

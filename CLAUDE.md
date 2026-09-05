# AI Capability Model — working brief

**IDB Enterprise Architecture · AI capability map, assessment and roadmap**
Last updated 4 September 2026 · facts + scales (ADR-0013), practised at L3 (ADR-0014)

Read this first. It exists so a new session starts warm instead of re-deriving decisions
that are already settled. Two project skills carry the working rules in more depth:
`assessment` (recording and reasoning about observations) and `citing` (anything that
names an external standard); two more cover `reporting` (changing a view) and
`decisions` (writing an ADR).

---

## 1. What this is

A capability model for AI at the Bank, and the assessment built on it.

- **8 domains · 52 L2 capabilities · 258 L3 criteria** — `facts/capabilities.json`
- **7 offerings · 20 assets · 27 in-the-box questions** — `facts/offerings.json`, `facts/assets.json`
- **414 observations** — `facts/observations.json` (258 criterion-level `practised`
  plus 3 × 52 capability-level)
- **52 capabilities mapped to the Bank's own catalogue**, 8 with no owner — `facts/owners.json`
- **40 graded sources · 18 candidate obligations · 1 use-case question** —
  `facts/sources.json`, `facts/obligations.json`, `facts/questions.json`

Schemas for every file: `facts/README.md`.

## 2. The architecture, and the rule that follows from it

```
facts/    what is TRUE about the Bank, with evidence and a date   ← edited
scales/   rules that turn observations into a level                ← rarely edited
out/      views, one per scale, one per question, plus the report  ← generated
```

> **`facts/` is edited. `out/` is generated. Derived values are never stored.**

Never fix a finding by editing a workbook or a view. Fix the fact and rebuild.
`build.py ingest` is the **only** program that writes to `facts/`, and only to observations.
Release counts, capability-level `practised`, levels: all derived, none typed. `check`
fails if a derived value is found stored.

**An observation is a fact, not a score.** That is what makes several scales possible over
one body of evidence without reassessing anything.

## 3. How assessment works — read this before touching a number

Four observations per capability, each `yes` / `partial` / `no` / `n/a` / `unknown`,
each with evidence:

**Practised** (done on real systems? — **asked per L3 criterion**, ADR-0014) ·
**Enabled** (tooling provided?) · **Skilled** (people competent?) ·
**Defined** (approved institutional standard?)

The capability's `practised` value is **rolled up** from its criteria: `yes` only if
every criterion was examined and every one passed · `partial` if some are `yes`/`partial`
**or any is left unexamined** · `no` if none is `yes`/`partial` and at least one is `no` ·
`unknown` if none has been looked at. One weak link stops the claim, and an unexamined
criterion is never counted as satisfied. The asymmetry is deliberate: under-claiming is
accepted, over-claiming is not.

> Read `Model.values(cid)` — it returns all four already rolled up. **`obs_by_cap` does
> not hold `practised`** and raises if asked; criterion rows live in `obs_by_crit`.

**The values mean exactly this**, and `check` enforces it:

| Value | Means | Needs |
|---|---|---|
| `yes` / `partial` | Done, or done in places | Evidence |
| `no` | **An evidenced negative** — someone looked and it is not there | Evidence or a basis saying what was looked at |
| `n/a` | Does not apply here | A reason; for `enabled`, an entry in `enablement-context.json` |
| `unknown` | **Nobody has looked. Never a zero** | Nothing. It is the honest default |

A register that was searched and had nothing is `unknown`, not `no`, until the owner is
asked (ADR-0013 Amendment 2). 24 `enabled` rows were corrected to this on 4 September 2026.

**A level is never typed. It is always derived.** The default scale
(`scales/capability_level.py`) is adapted from ISO/IEC 33020:2019:

| Level | Requires |
|---|---|
| 1 Performed | It is done on real systems |
| 2 Managed | …plus tooling provided and competent people |
| 3 Established | …plus done against a published Bank standard |

**Performance comes first.** A standard with nothing performed against it earns **no
level**. That ordering is the standard's, and it is what stops *"we approved the
technology"* from reading as *"we have the capability"*. Level 3 is the ceiling of what is
measured today (`DERIVABLE_MAX`), not of the scale.

- **Not rated is a result.** Today every capability is unrated because `practised` has
  never been observed. Do not paper over that.
- **Lenses are not the assessment.** `executive.py` and `maturity.py` read the same facts
  through another frame. Where a lens and the default disagree, the default is the finding.

## 4. Rules that are easy to break

- **Never quote ISO/IEC 33020's N-P-L-F percentage bands or its exact level rule.** The
  published preview stops before clause 5.3; those come from secondary sources about the
  superseded ISO/IEC 15504. Cite the scale by name and levels by clause. See `scales/README.md`.
- **Grade D cannot support a claim that leaves the Bank.** Licensed analyst material is
  usable internally, never reproduced externally, never listed as a source.
  `out/provenance.md` lists the 10 capabilities that currently rest partly on grade D.
- **The World Bank slide is a maturity model, not a readiness scale.** Grade D, Official
  Use Only. Never cite outside the Bank. The maturity lens's level names are the generic
  CMM vocabulary and must never be attributed to that slide.
- **Cite by name, never by number**, for lists that renumber between editions — the OWASP
  Top 10 above all.
- **NIST AI RMF locus form is `GOVERN 1.1`**, not hyphenated.
- **Do not invent a clause number.** Mark it unverified or say it is ours.
- **No formulas in the workbook.** Every derived value is computed in Python and written
  as a value. This is why there is no recalc step and why LibreOffice is not needed.
- **Do not average an ordinal level** in the default scale. The executive lens does
  average, deliberately, and says so — that is why it is a lens and not the default.
- **Nothing in `build/` names a scale or a question.** Scales are discovered from
  `scales/`, questions from `facts/questions.json`. A test fails if a builder names one.
- **Prose with a number in it is generated**, never typed into a builder.
- **Sample data never reaches `facts/`.** The illustrative report substitutes observations
  in memory (`build/sample.py`); a test checks the facts digest is unchanged by a build.

## 5. Settled decisions

`docs/decisions/`, indexed in `docs/decisions/README.md`.

**ADR-0014** — `practised` is observed at L3 and derived at L2. Never type a
capability-level `practised` value; `Model.roll_up` computes it.

**ADR-0013 is the one that governs the model.** It supersedes ADR-0001 (two scales),
ADR-0002 (readiness levels) and ADR-0003 (consumption model), and amends ADR-0004 and
ADR-0005. Those three are kept unedited, with banners. Amendment 1 fixes the wording of
`defined`; Amendment 2 fixes the meaning of `no` against `unknown`.

Still current and worth knowing:

- **ADR-0006** — the 8 domains are reporting clusters, not a lifecycle.
- **ADR-0007** — anchoring is provisional; 14 of 52 are lenses. **Carve out of any
  approval request** until control mapping exists.
- **ADR-0008** — statutory references are Legal-owned and all candidate.
- **ADR-0009** — the taxonomy is validated before anything is scored against it.
- **ADR-0010** — provenance is graded by whether a reviewer can open it.
- **ADR-0012** — ownership model, still **Proposed**. Its own text says the dependency
  flag is the stronger route.

## 6. Building

Python 3 and `openpyxl`. In this environment use `python3.13`.

```bash
python3.13 build/build.py           # status
python3.13 build/build.py check     # validate facts/ and scales/ — must pass
python3.13 build/build.py all       # check, then workbook + views
python3.13 build/build.py ingest review/2026-09-xx-<who>.xlsx   # one or more files
python3.13 build/build.py test      # tests/: roll-up table, ladder, contract, ingest round trip
```

`build/` is seven modules, described in `build/README.md`. `facts.py` is the only one that
opens `facts/`. Adding a scale to `scales/` adds a view automatically; adding a question to
`facts/questions.json` adds a page. `check` validates every scale against the contract in
`scales/README.md`, including running `level()` over all 625 observation combinations.

## 7. Working agreement

- **Point at files, don't paste model content into chat.**
- **Decisions go to `docs/decisions/adr/` as they settle.** An ADR is never edited to
  reverse itself; a reversal is a new ADR with a banner on the old one. A refinement is a
  dated `## Amendment N`. A moved file gets a dated location note, not a rewritten record.
- **Anything in `out/` can be deleted and regenerated. `facts/` cannot.**
- **`archive/` is history.** Nothing there is current; see `archive/README.md`.
- **Returned workbooks go in `review/`**, dated and named, and are never edited.
- **Run `check` and `test` after every change**, and `all` before anything is sent.

## 8. Strip before external circulation

Licensed analyst material anywhere · the World Bank slide and its wording · everything in
`docs/notes/` · ADR-0011 §2.4 and §3.4 · anything `out/provenance.md` lists as resting on
a grade-D source.

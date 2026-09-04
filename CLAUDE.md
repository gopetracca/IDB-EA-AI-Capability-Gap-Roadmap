# AI Capability Model — working brief

**IDB Enterprise Architecture · AI capability map, assessment and roadmap**
Last updated 4 September 2026 · **refactored to facts + scales (ADR-0013)**

Read this first. It exists so a new session starts warm instead of re-deriving decisions
that are already settled.

---

## 1. What this is

A capability model for AI at the Bank, and the assessment built on it.

- **8 domains · 52 L2 capabilities · 258 L3 criteria** — `facts/capabilities.json`
- **7 offerings · 20 assets · 27 in-the-box questions** — `facts/offerings.json`, `facts/assets.json`
- **414 observations** — `facts/observations.json` (258 criterion-level `practised`
  plus 3 × 52 capability-level)
- **52 capabilities mapped to the Bank's own catalogue**, 8 with no owner — `facts/owners.json`
- **40 graded sources · 18 candidate obligations** — `facts/sources.json`, `facts/obligations.json`

## 2. The architecture, and the rule that follows from it

```
facts/    what is TRUE about the Bank, with evidence and a date   ← edited
scales/   rules that turn observations into a level                ← rarely edited
out/      views, one per scale                                     ← generated
```

> **`facts/` is edited. `out/` is generated.**

Never fix a finding by editing a workbook or a view. Fix the fact and rebuild.
`build.py ingest` is the **only** path that writes to `facts/`, and only to observations.

**An observation is a fact, not a score.** That is what makes two scales possible over
one body of evidence without reassessing anything.

## 3. How assessment works — read this before touching a number

Four observations per capability, each `yes` / `partial` / `no` / `n/a` / `unknown`,
each with evidence:

**Practised** (done on real systems? — **asked per L3 criterion**, ADR-0014) ·
**Enabled** (tooling provided?) · **Skilled** (people competent?) ·
**Defined** (approved institutional standard?)

**A level is never typed. It is always derived.** The default scale
(`scales/capability_level.py`) is adapted from ISO/IEC 33020:2019:

| Level | Requires |
|---|---|
| 1 Performed | It is done on real systems |
| 2 Managed | …plus tooling provided and competent people |
| 3 Established | …plus done against a published Bank standard |

**Performance comes first.** A standard with nothing performed against it earns **no
level**. That ordering is the standard's, and it is what stops *"we approved the
technology"* from reading as *"we have the capability"*.

- **`unknown` is never a zero.** It means nobody has looked.
- **`n/a` needs a recorded reason**, and drops out of the calculation.
- **Not rated is a result.** Today every capability is unrated because `practised` has
  never been observed. Do not paper over that.

## 4. Rules that are easy to break

- **Never quote ISO/IEC 33020's N-P-L-F percentage bands or its exact level rule.** The
  published preview stops before clause 5.3; those come from secondary sources about the
  superseded ISO/IEC 15504. Cite the scale by name and levels by clause. See `scales/README.md`.
- **Grade D cannot support a claim that leaves the Bank.** Licensed analyst material is
  usable internally, never reproduced externally, never listed as a source.
- **The World Bank slide is a maturity model, not a readiness scale.** Grade D, Official
  Use Only. Never cite outside the Bank.
- **Cite by name, never by number**, for lists that renumber between editions — the OWASP
  Top 10 above all.
- **NIST AI RMF locus form is `GOVERN 1.1`**, not hyphenated.
- **Do not invent a clause number.** Mark it unverified or say it is ours.
- **No formulas in the workbook.** Every derived value is computed in Python and written
  as a value. This is why there is no recalc step and why LibreOffice is not needed.
- **Do not average an ordinal level** in the default scale. The executive lens does
  average, deliberately, and says so — that is why it is a lens and not the default.

## 5. Settled decisions

`docs/decisions/`, indexed in `docs/decisions/README.md`.

**ADR-0014** — `practised` is observed at L3 and derived at L2. Never type a
capability-level `practised` value; `Model.roll_up` computes it.

**ADR-0013 is the one that governs the model.** It supersedes ADR-0001 (two scales),
ADR-0002 (readiness levels) and ADR-0003 (consumption model), and amends ADR-0004 and
ADR-0005. Those three are kept unedited, with banners.

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
python3.13 build/build.py check     # validate facts/
python3.13 build/build.py all       # workbook + views
python3.13 build/build.py ingest    # read reviewer edits back
```

`build/` is four files: `build.py` (entry point), `facts.py` (loader), `build_workbook.py`,
`build_views.py`. Adding a scale to `scales/` adds a view automatically — nothing in
`build_views.py` names a scale.

## 7. Working agreement

- **Point at files, don't paste model content into chat.**
- **Decisions go to `docs/decisions/adr/` as they settle.** An ADR is never edited to
  reverse itself; a reversal is a new ADR with a banner on the old one.
- **Anything in `out/` can be deleted and regenerated. `facts/` cannot.**
- **`archive/` is history.** Nothing there is current; see `archive/README.md`.

## 8. Strip before external circulation

Licensed analyst material anywhere · the World Bank slide and its wording · everything in
`docs/notes/` · ADR-0011 §2.4 and §3.4.

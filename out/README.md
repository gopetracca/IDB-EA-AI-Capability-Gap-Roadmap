# `out/` — generated. Do not edit.

Everything here is produced by `uv run python build/build.py all` from `facts/` and `scales/`,
and is overwritten on the next build. A finding is never fixed here; fix the fact and
rebuild. These files are tracked in git so that the current state of the model can be
read without running anything.

| File | What it is | For |
|---|---|---|
| `capability-map.md` | **The taxonomy alone** — 8 domains, 52 capabilities, 258 criteria, with owner, anchor and confidence. No observations, no scale, no levels | Reviewing the map as a map, before anything is measured against it (ADR-0009) |
| `walkthrough.html` | **The deck.** A slide walkthrough of the model — map, observations, scale, first round. Self-contained, arrow keys, prints one slide per page | Presenting the model to a room seeing it for the first time |
| `management-report.html` | **The management report.** Self-contained, opens offline, prints | Management. The one to send |
| `management-report-illustrative.html` | The same report with every chart populated from **SAMPLE observations**. Banner, badges and watermark say so | Agreeing the approach before the assessment runs. Never for reporting |
| `management-report.md` | The report as plain text | Pasting into email or a wiki |
| `capability-assessment-level.md` | All 52 capabilities, four observations each and every criterion, under the **default scale** | The detail |
| `capability-assessment-<short>.md` | The same facts under each lens in `scales/` (`exec`, `maturity`) | Reporting into a frame a room already holds |
| `agent-readiness.md` | The answer to *"can the Bank run AI agents?"* — one page per entry in `facts/questions.json` | The worked example |
| `provenance.md` | Sources by grade, capabilities resting on grade-D sources, locus coverage, obligations | The provenance workstream; what blocks external circulation |
| `AI-Capability-Model.xlsx` | The ten-sheet review workbook. Sheet 2 is filled in and read back with `ingest` | Review rounds |

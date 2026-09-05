# Review returns

Completed review workbooks land here, dated, one file per return, named for who filled it in:

    2026-09-12-owner-D4.xlsx
    2026-09-12-platform-team.xlsx
    2026-09-15-cybersecurity.xlsx

**Never edit a returned file.** It is the record of who said what. Read it in:

    python3 build/build.py ingest review/2026-09-12-owner-D4.xlsx review/2026-09-12-platform-team.xlsx
    python3 build/build.py all
    git add -A && git commit -m "Observations from <who>, <date>"

`ingest` reads sheet 2 only — value, evidence, observed by, date — and writes only
`facts/observations.json`. Several files can be given at once; if two set the same cell,
`ingest` says so and the last one wins, so look before rebuilding. Anything a return settles
about the *structure* of the model (a capability renamed, an owner corrected) is applied by
hand to the relevant `facts/` file and, if it changes a decision, recorded in
`docs/decisions/`.

The taxonomy-validation workbook sent before the ADR-0013 refactor
(`archive/generated-2026-09/AI-Capability-Taxonomy-for-review.xlsx`) is still out. When it
returns, file it here too; its decision columns are applied to `facts/capabilities.json` by
hand (OPEN-ITEMS item 15).

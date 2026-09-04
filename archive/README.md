# Archive

**Nothing here is current.** Read [`../README.md`](../README.md) instead.

Kept because it is what reviewers were sent before 4 September 2026, and because the
evidence in it was migrated rather than discarded. Every folder has its own README
saying what is inside and where it went.

| Folder | What it holds |
|---|---|
| [`old-model/`](old-model/README.md) | The model before the refactor — positional JSON, and model data that lived in Python files |
| [`old-build/`](old-build/README.md) | The eleven builders, `run.py`, and the LibreOffice recalc bridge |
| [`generated-2026-09/`](generated-2026-09/README.md) | Every artifact generated before the refactor |
| [`reference-catalog/`](reference-catalog/README.md) | The 143-entry catalog and the TRM. **Frozen, not maintained** |
| [`pre-adr-originals/`](pre-adr-originals/README.md) | The single files the ADR set was split out of |
| [`migration-2026-09-04/`](migration-2026-09-04/README.md) | The one-off conversion scripts, so the migration can be audited |

## Why the refactor happened

Three files each claimed to be the register of what IDB provides, and they disagreed:

| File | Said | Confirmed |
|---|---|---|
| `old-model/realization.json` | 1 realization, readiness 4 | 1 of 5 |
| `old-build/wb_data.py` + `old-model/idb-assets.json` | 8 realizations, 20 assets | 7 of 8 |
| `reference-catalog/mkregister.py` | A fourth scale entirely, 0 Nothing → 4 Managed service | 1 of 77 |

The generated Markdown was built from the first and the workbook from the second, so the
two main deliverables made different claims about the Bank's estate.

`facts/offerings.json` merges them, taking the asset-backed version as canonical because
it is the one with evidence behind it. The rest of the story is
[ADR-0013](../docs/decisions/adr/0013-facts-and-scales.md).

## What was deleted rather than archived

- `_transfer.tar.gz` — a snapshot of three files that all still exist in the repository.
- `views_data.json` in `generated-2026-09/` is kept but was **invented illustrative
  data**. It is not evidence and must never be quoted.

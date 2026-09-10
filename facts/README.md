# `facts/` — what is true about the Bank

Every file here records something true, with evidence and a date where a claim is
made. **Nothing here is a score.** Levels are derived by `scales/`; views are generated
into `out/`. This directory is edited; the other two are not.

`uv run python build/build.py check` validates every file below and must pass before and after
any change. `uv run python build/build.py ingest` is the only program that writes here, and it
writes only `observations.json`.

All files are JSON, UTF-8, indent 1, no trailing newline (the form `ingest` writes, so a
hand edit and a program edit produce the same diff).

| File | Holds | Edited when |
|---|---|---|
| [`capabilities.json`](capabilities.json) | The map: 8 domains (L1), 52 capabilities (L2), 258 criteria (L3) | The taxonomy changes (ADR-0009: validated by the owner first) |
| [`observations.json`](observations.json) | The four observations, with evidence, observer and date | Someone learns something. Usually via the workbook and `ingest` |
| [`offerings.json`](offerings.json) | What a delivery team can get: bundles of assets, what they enable, the in-the-box control checklist | The platform changes what it offers |
| [`assets.json`](assets.json) | Every standard, reference architecture, template and module, with status and location; and which statuses count as released | An asset is written, released or withdrawn |
| [`owners.json`](owners.json) | The Bank's units and the mapping of each capability to the unit whose catalogue entry claims it | The catalogue or the org changes |
| [`enablement-context.json`](enablement-context.json) | Why a capability has no platform offering and is not a gap: realized by an enterprise service, or purely organizational | An `enabled: n/a` is recorded or withdrawn |
| [`sources.json`](sources.json) | The graded source register (ADR-0010) and the table that resolves each citation string on a capability to a source and a locus | A source is verified, superseded or re-graded |
| [`obligations.json`](obligations.json) | Statutory references, Legal-owned, all candidate (ADR-0008) | Legal determines applicability |
| [`questions.json`](questions.json) | Use-case questions of the form *"do we have the capability to X"*, each with an attributed finding | A new question needs a page |

---

## `capabilities.json`

```json
{"domains": [{"id": "D1", "name": "...", "definition": "Able to ..."}],
 "capabilities": [{
   "id": "4.4", "domain": "D4", "name": "...", "definition": "Able to ...",
   "sources": ["citation string", ...],          // resolved through sources.json
   "criteria": [{"id": "4.4.1", "name": "...", "definition": "...", "agentic": true}],
   "agentic": true, "anchor": "new|specialization|lens",
   "proposed_owner": "role", "confidence": "high|medium|low"}]}
```

- `id` is `<domain number>.<n>`; criterion ids are `<capability id>.<n>`. `check` enforces
  the nesting.
- `anchor` is ADR-0007: `lens` means *do not create a node*; attach an AI profile to the
  existing enterprise capability instead.
- `confidence` is ADR-0009: `low` until the owner has validated it.
- `sources` are strings as originally cited; `sources.json` → `normalize` maps each to a
  register id. `check` fails on a string that does not resolve.

## `observations.json`

```json
{"observation_types": [{"id": "practised", "question": "...", "evidence_expected": "...",
                        "recorded_at": "criterion"}, ...],
 "values": ["yes", "partial", "no", "n/a", "unknown"],
 "observations": [
   {"capability": "4.4", "criterion": "4.4.5", "observation": "practised",
    "value": "unknown", "evidence": "", "basis": "...", "observed_on": "", "observed_by": ""},
   {"capability": "4.4", "observation": "enabled", "value": "partial",
    "evidence": "OFF-02 ...", "basis": "...", "observed_on": "2026-09-04", "observed_by": "..."}]}
```

- A type with `recorded_at: "criterion"` has one row **per L3 criterion** and no row at
  capability level; the capability value is rolled up by `Model.roll_up` (ADR-0014).
  Today that is `practised` only. The other three have one row per capability.
- **What the values mean** — and `check` enforces the first three:
  - `yes` / `partial` — require `evidence`. An observation without evidence is an opinion.
  - `no` — an **evidenced negative**: someone looked and it is not there. Requires
    `evidence` or a `basis` saying what was looked at.
  - `n/a` — does not apply here. Requires a `basis` (the reason), and for `enabled` the
    reason must also be recorded in `enablement-context.json`.
  - `unknown` — nobody has looked. **Never a zero.** The right answer when the register
    was checked but the owner has not been asked. Leave `observed_on`/`observed_by` empty.
- `basis` is *why this value*, `evidence` is *what shows it*. Both are free text.
- `observed_on` is `YYYY-MM-DD`. A recorded value without a date and observer is flagged
  as an advisory.

## `offerings.json`

```json
{"generic_assets": [...], "consumption_models": [...],
 "offerings": [{
   "id": "OFF-02", "name": "Foundry agents", "was": ["REAL-002"],
   "assets": ["STD-03", "STD-07", ...],             // ids in assets.json
   "enables": ["4.4", "5.1", "5.6"],                // capability ids
   "consumption": "Building blocks", "operated_by": "...", "status": "Approved",
   "not_provided": "what the team must still supply", "note": "...",
   "in_the_box": [{"control": "...", "catalog_ref": "S6.9", "capability": "7.4.4",
                   "why": "...", "status": ""}]}]}
```

- **Released counts are not stored.** `Model.release_count(offering)` derives them from
  asset statuses; `check` fails if `assets_released`/`assets_total` reappear.
- `in_the_box[].capability` is an L3 criterion (or an L2 id); `status` is what the platform
  team answers on sheet 4 of the workbook: `yes` / `no` / `partial` / `unknown`, or empty.
- `was` and `note` are the migration trail from the pre-ADR-0013 realization register.
  The notes may still speak of "readiness 3" and "the step to 4": that vocabulary is
  superseded (ADR-0013) and the notes are kept as history until rewritten.

## `assets.json`

```json
{"statuses": {"Published": {"released": true, "meaning": "..."},
              "Pre-release": {"released": false, "meaning": "..."}, ...},
 "assets": [{"id": "STD-07", "type": "Standard", "name": "...", "status": "Pre-release",
             "location": "https://...", "note": "..."}]}
```

- `statuses` is the one place that says what counts as released to delivery teams.
  Every asset's `status` must be declared there or `check` fails. Add a status here before
  using it.
- `type` is one of Standard · Reference architecture · Template · IaC module (used to seed
  `defined`: standards and reference architectures count, templates and modules do not).

## `owners.json`

```json
{"source": "sources/Product and Applications_ENTERPRISE.xlsx", "read_on": "...",
 "units": [{"name": "Artificial Intelligence", "function": "Enabler", "family": "...",
            "lead": "...", "technical_lead": "", "claims": "..."}],
 "mapping": [{"capability": "1.1", "unit": "Artificial Intelligence",
              "match": "Direct|Partial|Inferred|NO MATCH", "basis": "..."}]}
```

- Exactly one unit per capability (COBIT single accountability; ADR-0012 discusses adding
  typed contribution columns and is still **Proposed**). `unit` empty ⇔ `match: NO MATCH`.
- `basis` quotes the catalogue entry that justifies the match.

## `enablement-context.json`

```json
{"realized_by_enterprise_service": {"1.2": "Enterprise portfolio and investment management"},
 "purely_organizational": ["1.1", "8.1", "8.5"]}
```

The reason register behind `enabled: n/a`. `check` fails on an `n/a` with no entry here,
and advises when a capability listed here is nonetheless enabled by an offering.

## `sources.json`

```json
{"access_date": "3 September 2026",
 "grades": {"A": "...", "B": "...", "C": "...", "D": "..."},
 "sources": [{"id": "S08", "short": "NIST AI RMF", "title": "...", "publisher": "...",
              "edition": "1.0", "date": "2023-01", "url": "...", "access": "Free",
              "type": "...", "locus_form": "GOVERN 1.1", "grade": "A", "status": "Current",
              "caution": "..."}],
 "normalize": {"citation string as written on a capability": {"source": "S08", "locus": ""}},
 "extra_from": {"...": {"source": "S26", "locus": ""}}}
```

- Grades are ADR-0010. **Grade D cannot support anything that leaves the Bank.**
- `normalize` (and `extra_from`) is the join: every string in a capability's `sources`
  must appear here. `locus` is the clause, section or control relied on; empty means
  *not yet pinned*. `out/provenance.md` reports coverage.

## `obligations.json`

```json
{"obligations": [{"capability": "7.6", "capability_name": "...", "instrument": "EU AI Act",
                  "subject": "...", "status": "candidate - applicability not determined"}]}
```

Legal-owned (ADR-0008). `capability` must resolve. Six rows that once pointed at
services in the frozen reference catalog were re-homed to capabilities on 4 September
2026 using the catalog's own criterion links; their `subject` names the former service id.

## `questions.json`

```json
{"questions": [{
   "id": "agents", "output": "agent-readiness", "title": "Can the Bank run AI agents?",
   "claim": "We cannot run AI agents.",
   "offerings": ["OFF-01", "OFF-02", "OFF-03", "OFF-07"],
   "capabilities": ["4.4", "5.1", "5.5", "7.7", "2.5", "4.5", "7.4", "8.3"],
   "finding": "...", "finding_by": "EA", "finding_on": "2026-09-04",
   "next": [{"who": "Platform team", "what": "..."}]}]}
```

- One view `out/<output>.md` per question. Everything on it except `finding` and `next`
  is derived: release state, pending assets, in-the-box controls, the four observations
  per capability, and the further capabilities the controls reach.
- `finding` and `next` are judgements, so they carry who made them and when, exactly as
  an observation does. `check` fails on a finding without attribution.
- `offerings` and `capabilities` are curated: which offerings and capabilities the
  question is really about. Derived candidates (everything an offering enables or a
  control touches) would be twenty-plus; the page states how many more the controls reach.

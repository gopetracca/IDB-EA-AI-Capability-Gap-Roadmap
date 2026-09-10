---
id: ADR-0016
title: D4 criterion refinements from the first review round
status: Accepted
date: 2026-09-10
decision_owner: Gabriel Petracca, Enterprise Architecture
supersedes: []
superseded_by: []
depends_on: [ADR-0009, ADR-0013, ADR-0014, ADR-0015]
---

# ADR-0016 · D4 criterion refinements from the first review round

## Status

**Accepted** — 10 September 2026. Refines four criteria in domain D4 and adds one.
Reverses nothing. Nothing is renumbered.

## Context

The first review round was worked as a walkthrough rather than a returned workbook: an EA
workshop on 9 September 2026 went through domain D4 criterion by criterion, graded
`practised` on all seven capabilities, and wrote the evidence down beside each row.
The workbook is kept unedited at
[`review/2026-09-09-ea-workshop.xlsx`](../../../review/2026-09-09-ea-workshop.xlsx).

Four criteria did not survive contact with the people who do the work. The workshop did not
argue with the levels — it argued with the words:

**4.5.1 and 4.5.2 named the wrong thing.** `API & System Integration Design` and
`Tool & Function Definition` were written before the Bank had settled how AI clients reach
its systems. It has now settled: MCP servers front the integrations, APIM stands in as the
MCP gateway, and the published standard is
`STD-02 Custom MCP Server Standard`. A reviewer reading "API integration design" answered
about the API estate, which is a different practice with a different owner. The criterion
that is actually being assessed is the MCP one.

**4.7.5 was two criteria wearing one name.** `Release Documentation & Evidence Capture`
bundled a thing the Bank does well — GitHub produces release documentation out of the box,
on the same SDLC as everything else — with a thing it does not yet do: capturing at release
the evidence that later assurance work will need. Graded as one criterion it reads `yes`,
and the assurance gap disappears inside it. The workshop's note on 4.7.6 is the finding:
*"We depend on the process."*

**4.1.4 read as a closed list.** `latency, cost, availability, and degradation behavior`
was written as an illustration and read as an enumeration.

This is ADR-0009 working as intended. The taxonomy is validated by the people who own the
work, and the first time it is put to them is the first time the wording is really tested.

## Decision

**Two criteria are renamed, one is split in two, and one definition is opened up.**

| Criterion | Was | Is |
|---|---|---|
| `4.5.1` | API & System Integration Design | **MCP & System Integration Design** |
| `4.5.2` | Tool & Function Definition | **MCP Tool & Function Definition** |
| `4.7.5` | Release Documentation & Evidence Capture | **Release Documentation** |
| `4.7.6` | — | **Evidence Capture** (new) |
| `4.1.4` | …latency, cost, availability, and degradation behavior. | …and any other non-functional requirement the solution carries. |

`4.7.6 Evidence Capture` takes the definition the old `4.7.5` carried for the half that was
split out: *"Capture at release the evidence that later assurance work will need."*
`4.7.5` keeps its number and narrows to the documentation half.

D4 goes from 39 criteria to 40; the model goes from 281 to 282.

**Naming a protocol inside a criterion is permitted here** because the protocol is a
registered source, not an assumption: `S33 Model Context Protocol Specification`
(Agentic AI Foundation, revision 2026-07-28) is already among 4.5's sources, and the Bank
has a published standard built on it. Where a protocol is *not* registered, the criterion
stays protocol-neutral.

Two wordings were normalized rather than transcribed literally from the sheet, in keeping
with the file's one-sentence imperative style: the workshop wrote `4.7.5` as *"Release
documentation of the new chages deployed"* and appended *", or others."* to `4.1.4`. The
substance is unchanged and the sheet holds the original.

## Options considered

| Option | For | Against |
|---|---|---|
| A — Rename 4.5.1/4.5.2 to MCP, split 4.7.5 (**chosen**) | Matches how the work is actually organized and owned; MCP is a registered source and a published Bank standard; the split stops a real assurance gap hiding inside a `yes` | Ties two criterion names to one protocol; if the Bank adopts another integration route the names need revisiting |
| B — Keep 4.5.1/4.5.2 protocol-neutral, record MCP in the definition and evidence | Survives a change of protocol without a taxonomy change | Reviewers demonstrably answer the general question instead of the specific one — which is what produced the ambiguity this ADR is fixing |
| C — Leave 4.7.5 as one criterion | No change | Grades `yes` on the documentation half and the assurance half disappears; over-claiming, which ADR-0013 exists to prevent |
| D — Make Evidence Capture a capability | Gives the assurance gap its own owner | Fails the ADR-0015 test: it has an adequate existing home in 4.7 and no distinct owner. A criterion is the right size |

## Consequences

- `facts/capabilities.json` changes: two names, two definitions, one new criterion.
- `facts/observations.json` gains one `practised` row for `4.7.6`, `unknown` until observed.
  It was never put to the workshop — the criterion did not exist yet — so it is not carried
  over from the old `4.7.5` grade.
- **`4.7` cannot read `yes` on `practised` while `4.7.6` is unexamined** (ADR-0014). That is
  the intended effect: the split makes the gap visible instead of absorbing it.
- Nothing is renumbered, so every ID in the returned workbook still resolves. The precedent
  is ADR-0015: taxonomy change is additive, and a number, once issued, is permanent.
- `4.5.1` and `4.5.2` now carry a protocol name. If the Bank's integration route changes,
  this ADR is superseded, not edited.

## Open

- **The `agentic` flag on `4.7.6`** is set to match `4.7.5`. Whether evidence capture for
  agent releases needs its own treatment is not settled here.
- **Who owns evidence capture.** The workshop's note is *"We depend on the process (SPM?)"*
  — a question mark in the record, not an owner. `4.7`'s owner in `facts/owners.json` is
  Core Platforms by inference; the workshop said Core Platforms **and product teams**, which
  the ownership schema cannot yet express. ADR-0012 remains Proposed and this is another
  case for it.
- **`4.3 Prompt & Context Engineering` was marked `n/a` in full** at the same workshop, on
  the grounds that prompt templating and registries are superseded practice and prompts sit
  with each product. That is recorded as observations with a rationale, not as a taxonomy
  change. Whether the capability should instead be *reframed* around agent skills, plugins
  and hooks — the reusable unit that replaced the prompt template — is raised in
  `OPEN-ITEMS.md` and is not decided here.

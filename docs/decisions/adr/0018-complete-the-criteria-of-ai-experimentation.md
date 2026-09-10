---
id: ADR-0018
title: Complete the criteria of AI Experimentation
status: Accepted
date: 2026-09-10
decision_owner: Gabriel Petracca, Enterprise Architecture
supersedes: []
superseded_by: []
depends_on: [ADR-0006, ADR-0009, ADR-0014, ADR-0015, ADR-0017]
---

# ADR-0018 · Complete the criteria of AI Experimentation

## Status

**Accepted** — 10 September 2026. Adds four criteria to one capability. Reverses nothing.
Nothing is renumbered.

## Context

[ADR-0017](0017-carve-out-experimentation-and-rehome-shared-agent-assets.md) carved
`5.9 AI Experimentation` out of `5.3` with the one criterion the meeting had named —
isolation — and left in **Open** the question of whether it needed more: *what may enter an
experiment, how results graduate to delivery, and when an experiment must stop*. Its
Amendment 1 restated the definition to say what the capability is for: *an isolated place
for teams to explore AI functionality*.

A capability with one criterion is thin in two ways. `practised` is observed per criterion
(ADR-0014), so a single criterion makes the capability's roll-up a single answer, with no
room for *"the sandbox exists, but nobody can get into it"* or *"it exists, but nothing new
is in it"*. And a one-line capability gives the owner nothing to validate against
(ADR-0009): *"do you have an isolated environment?"* is a narrower question than the one
the decision owner asked.

The criteria have to stay on the platform side of the seam. `2.6 AI Innovation &
Incubation` — same owner in the Bank's catalogue, Emerging Tech — already holds the
**practice** of experimenting: `2.6.2 Sandboxed Experimentation` runs the experiment,
`2.6.3` decides which scale, `2.6.4` moves a proven one onto the funded route, `2.6.5`
captures the learning. `5.9` is the environment that practice happens in, and its criteria
must describe what the environment **provides**, not what the experimenters decide. The
domains are reporting clusters (ADR-0006), so one unit answering for both is not a conflict;
two capabilities asking the same question would be.

## Decision

**Four criteria are added to `5.9`. `5.9.1` is unchanged.**

| | |
|---|---|
| `5.9.1` **Isolated Experimentation Environment Provision** | *Provide an experimentation environment that is fully isolated from institutional systems and data.* (ADR-0017, unchanged) |
| `5.9.2` **Self-Service Access & Onboarding** (new) | *Let any team obtain and enter an experimentation space quickly, without the intake and approval route that delivery work requires.* |
| `5.9.3` **Emerging AI Service & Tool Access** (new) | *Make new models, services and tools available to explore ahead of their approval for delivery environments.* |
| `5.9.4` **Experiment Data Admission & Result Egress** (new) | *Define what data may be brought into an experiment, and the only route by which its artefacts may leave it for the delivery environments.* |
| `5.9.5` **Time-Boxing, Spend Guardrails & Teardown** (new) | *Give every experiment an expiry and a spend ceiling, and decommission it when either is reached.* |

Each answers one of ADR-0017's open questions from the platform side. What may enter, and
how results leave, is `5.9.4`; when an experiment must stop is `5.9.5` — the environment
enforces an expiry and a ceiling, while the *decision* to stop or scale stays with `2.6.3`.
`5.9.2` and `5.9.3` are what makes the capability about exploration at all: an isolated
environment nobody can reach, or that holds only what is already approved for delivery,
is a smaller `5.3`.

Sources are unchanged — Microsoft Cloud Adoption Framework for AI and institutional
practice — and no criterion names a standard or a protocol. The `agentic` flag is `false`
on all five. The capability keeps `confidence: low` and `anchor: new` until the Tech Lab
validates it (ADR-0009).

D5 stays at 9 capabilities; the model goes from 283 criteria to 287.

## Options considered

| Option | For | Against |
|---|---|---|
| A — Four platform-side criteria (**chosen**) | Answers ADR-0017's open questions; gives the owner something to validate; keeps the seam with `2.6` clean | Adds four unevidenced criteria to a capability with no evidence, so `5.9` stays *not rated* and now reads that way five times |
| B — Leave `5.9` at one criterion until the Tech Lab is asked | Nothing is written the owner did not say | The owner is asked a one-line question and cannot correct what was never proposed. ADR-0009 validates a taxonomy; it does not write one |
| C — Add graduation as a `5.9` criterion (*Experiment-to-Delivery Promotion*) | It was one of ADR-0017's open questions | It is `2.6.4 Experiment-to-Product Transition`, already in the model. The platform's part is the egress route, which is `5.9.4` |
| D — Add an experiment risk-screening criterion | Experiments touch new vendors and models | Screening an experiment is D7's job (`7.3 AI Risk Management`, `7.9 AI Impact Assessment & Risk Classification`); the environment's contribution is isolation, which is `5.9.1` |
| E — Fold `5.9.2`-`5.9.5` into `2.6` as criteria of the practice | One capability for one owner | `2.6` would then carry environment provision, and `5.9` would be back to the single answer ADR-0017 said was too thin. The practice / platform split is the one the rest of the model uses |

## Consequences

- `facts/capabilities.json`: four criteria on `5.9`. Nothing else changes.
- `facts/observations.json` gains four `practised` rows, `5.9.2` to `5.9.5`, all `unknown`
  with the basis *"Criterion added 10 September 2026 (ADR-0018); to be confirmed with the
  Tech Lab."* The capability-level `enabled`, `skilled` and `defined` rows are untouched.
- `5.9` rolls up to `practised: unknown` as before; nothing is rated or unrated by this.
- OPEN-ITEMS #28 narrows from *"has one criterion and no evidence"* to *"has no evidence"*.
- The Tech Lab review of `5.9` now has five things to confirm, amend or strike instead of
  one.

## Open

- **None of the five criteria has been seen by the Tech Lab.** The meeting's note was *"ASK
  tech lab"*; that is still the next step. A criterion the Tech Lab strikes is removed by
  amendment here, not by editing `facts/` alone.
- **Whether `5.9.3` needs a control on *what* may be made available** — a vendor or model
  the Bank has not screened at all, even for a sandbox — is a D7 question and is not
  answered here.

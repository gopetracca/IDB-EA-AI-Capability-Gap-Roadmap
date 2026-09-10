# Running the first round

How to get from *nothing is rated* to a first defensible picture. This is the
project-specific plan; the mechanics it relies on are in
[`using-the-model.md`](using-the-model.md) and are not repeated here.

*Planning document, not normative. Figures are as of the date of the build that produced
the numbers quoted; the live ones are always in `out/`.*

---

## 1 · Where the model is, and why

**No capability is rated.** Not one. The report says so on its first page, and that is
correct rather than embarrassing: the default scale gates on performance, and `practised`
has never been observed against any of the 258 criteria. `skilled` has never been observed
either.

What *is* established is the part that does not need a review round — the map, the
offerings, the assets and their statuses, the owner mapping, and the source register. So
the first round is not building the model. **It is asking the two questions the model is
already shaped to receive.**

| Observation | State | Who closes it |
|---|---|---|
| **Practised** | Never observed, all 258 criteria | Capability owners |
| **Skilled** | Never observed, all 52 | Capability owners, or L&D |
| **Enabled** | Recorded where an offering exists; `unknown` where nobody has yet asked whether an enterprise service provides it | Platform teams, and the owners of the unexamined ones |
| **Defined** | Recorded from the asset register, which covers **AI platform assets only** | Cybersecurity, Data Management, Legal, HR, L&D — each for their own subject |

> The `defined` gap is the one most likely to be misread in the room. A capability showing
> `defined: unknown` is **not** evidence that no standard exists — it means the standard, if
> there is one, is owned by a function whose assets this register does not cover. Those are
> questions to ask, not gaps to assume.
> → [ADR-0013 Amendment 1](decisions/adr/0013-facts-and-scales.md#amendment-1--4-september-2026)

---

## 2 · Decide the scope — the one real choice

Two credible shapes for round one. The volume argument does not decide it, because the
volume is smaller than it looks.

### The load, per reviewer, if you go wide

Sheet 2 has 414 rows in total, but **no single reviewer ever sees 414**. Rows are answered
by the unit that owns the capability:

| Reviewer | Capabilities | Rows to answer |
|---|:-:|:-:|
| Artificial Intelligence | 14 | 112 |
| Data Management · Core Platforms · Cloud & Infrastructure | 4 each | ~30 each |
| Strategic Portfolio Management · Emerging Tech | 3 each | ~22 each |
| Enterprise Architecture · Digital Transformation · Service Delivery · Strategic Resource Management | 2 each | ~16 each |
| Cybersecurity · People Experience · Risk, Audit & Compliance · IT Risk | 1 each | 7–10 each |
| **Nobody claims these** | 8 | 66 unassigned |

One reviewer carries a real load. Everyone else is answering between seven and thirty-two
rows about work they already know. **Volume is not the reason to narrow the round.**

### Option A — the agent slice *(recommended for round one)*

The eight capabilities behind the question the Bank is already arguing about — 43 criteria,
five owning units.

| | |
|---|---|
| `4.4` Agent & Workflow Orchestration Design | Artificial Intelligence |
| `5.1` AI Platform Service Provisioning | Artificial Intelligence |
| `5.5` Tool & Connector Catalog Management | Artificial Intelligence |
| `7.7` AI System & Agent Inventory Management | Artificial Intelligence |
| `4.5` Integration & Tool Enablement | Core Platforms |
| `7.4` AI Security & Resilience | Cybersecurity |
| `2.5` Human-AI Interaction & Oversight Design | People Experience — IBT |
| `8.3` AI Literacy & Awareness | Emerging Tech |

**Why this slice.** It is the only part of the map where practice plausibly exists to be
observed, so it is the only one that can produce a rating rather than another *not rated*.
It answers a question already on the table. It proves the whole loop — send, answer, ingest,
rebuild — against five units rather than fifteen. And it produces a finished artifact
people already know: [`../out/agent-readiness.md`](../out/agent-readiness.md), currently
answering with columns rather than levels.

**What it does not do.** It cannot produce an institution-wide picture, and it will show
levels for eight capabilities against forty-four that stay *not rated*. Say that out loud
before anyone reads the chart.

### Option B — go wide

All 52, every owner, one round.

**Why.** The load per reviewer is genuinely small, and a partial picture invites the
question *"why these eight?"* every time it is shown.

**Why not, for a first round.** Every mistake in the instrument is made fifteen times
instead of five, in front of the people whose willingness to answer the second round you
need. A reviewer who receives a confusing workbook does not send back a worse answer — they
send back nothing.

### If you go wide anyway

Do it in two waves in the same round: **wave 1** the five units in Option A, **wave 2**
everyone else, sent a week later with the instrument fixed by what wave 1 got wrong. That
keeps the institution-wide claim and still buys the correction.

---

## 3 · The packet, per reviewer

Everyone gets the same workbook. What changes is which rows they are asked for and what the
covering note says.

```bash
uv run python build/build.py all
```

| Reviewer | Asked for | On |
|---|---|---|
| **Capability owner** | `practised` for each of their criteria, and `skilled` for each of their capabilities | Sheet 2 |
| **Platform team** | `enabled` for the capabilities their offering enables, plus the 27 in-the-box control questions | Sheet 2, sheet 4 |
| **Cybersecurity, Data Management, Legal, HR, L&D** | `defined` for their own subject | Sheet 2 |
| **The 8 unowned capabilities** | Not sent to anyone. **They go to the meeting, not to a reviewer** | — |

Filter sheet 2 to their rows before sending, or send the whole file and name the rows in the
covering note. Several reviewers may work in parallel: each answers only their own rows, so
the returned files ingest together.

### What the covering note has to say

Four things, and the round degrades badly if any is left out.

1. **`unknown` is a real answer.** If you have not looked, say `unknown`. It is never
   counted as a zero, and it is better than a guess.
2. **`no` means you looked and it is not there** — and say what you looked at. If you simply
   do not know, that is `unknown`.
3. **`yes` and `partial` need evidence** — a named system, agent, document or person. An
   observation without evidence is an opinion, and the build rejects it.
4. **You are not being scored.** There is no level in the workbook for you to defend. The
   level is computed afterwards from what you record, by a rule you can read.

> The fourth point is the one that determines the quality of everything that comes back. A
> reviewer who believes they are being rated answers defensively, and the model's whole
> value is that it can distinguish *we did not look* from *it is not there*.

---

## 4 · Read it back

```bash
uv run python build/build.py ingest review/2026-09-DD-<who>.xlsx [...]
uv run python build/build.py check
uv run python build/build.py all
git add -A && git commit -m "Observations from <who>, <date>"
```

Returned workbooks go in `review/`, dated and named, and are never edited. One commit per
round keeps the record of who said what.

**Expect `check` to fail the first time.** That is the instrument working: a `yes` with no
evidence, a `no` with no basis, an `n/a` with no reason. Do not fix it by softening the
value — go back to the reviewer with the specific row. A round that passes `check` on the
first attempt usually means the covering note asked for too little.

---

## 5 · What the round can and cannot produce

**It can produce**, for the capabilities answered:

- A derived level per capability on the default scale, and the same evidence through both
  lenses.
- A gap with a **name**: not *"improve agent orchestration"* but *"multi-agent coordination
  and termination control have never been done, guardrails exist on one agent of four, and
  nobody has looked at agent memory design."* That is the return on asking at L3.
- The first honest count of how much of the map has been examined at all.

**It cannot produce:**

- **A level above 3.** Levels 4 and 5 need threshold monitoring and a closed improvement
  cycle, and nothing collects either. Level 3 is the top of what is measured, not the top of
  the scale — every view says so.
- **Evidence of conformance.** Level 3 reads it from a standard and a practice co-existing;
  it does not show the work follows the standard. → [OPEN-ITEMS](../OPEN-ITEMS.md) #7
- **A rating for the 10 capabilities carrying `confidence: low`**, or for anything whose
  taxonomy validation has not come back. Structure is settled ahead of assessment
  ([ADR-0009](decisions/adr/0009-taxonomy-validated-before-scoring.md)) — do not score a
  line whose owner has not yet agreed it is the right line.
- **A benchmark.** No comparable dataset exists.

### Before you show a chart

Run the illustrative edition alongside the live one:

```
out/management-report.html                # what the facts actually support
out/management-report-illustrative.html   # the same report with SAMPLE observations
```

The illustrative edition exists so a room can agree the **approach** before the assessment
runs, and it is the right thing to show when the live charts are still mostly empty. It
carries a banner, a per-view badge and a watermark. **Never present it as an assessment.**

---

## 6 · The round after this one

Not required for round one, but worth naming so nobody proposes them as blockers:

| | What it would take |
|---|---|
| The 27 in-the-box questions | The platform team, one sitting. Each unanswered one is a roadmap item already |
| Two pre-release documents | Publishing them moves `defined` for the agent capabilities |
| The `defined` sweep | One question to each standard-setting function, covering the capabilities that read `unknown` today |
| Targets | Target *column states* with a date, recordable now — no new machinery |
| The anchoring crosswalk | The Bank's existing enterprise capability map, mapped against. Blocks approval of [ADR-0007](decisions/adr/0007-anchoring-is-provisional.md), not this round |

The full list, with what closes each, is [`../OPEN-ITEMS.md`](../OPEN-ITEMS.md).

# Where the scales, levels and lenses come from

The provenance of the **measurement instrument** — not of the map. Where each ladder was
taken from, what was adopted, what is ours, what has been verified against the source and
what has not, and which scales were retired.

*Orientation and handling. The live declaration for each shipped scale is generated into
[`../out/provenance.md`](../out/provenance.md) §"The measurement instrument", read from the
scale modules themselves; the contract every scale must keep is
[`../scales/README.md`](../scales/README.md); the decisions are
[ADR-0011](decisions/adr/0011-scale-provenance.md) and
[ADR-0013](decisions/adr/0013-facts-and-scales.md).*

> ### ⚠ Handling
>
> This page names a paywalled standard and a non-public comparator. Before anything here
> circulates outside the Bank, read §6. **Do not quote ISO/IEC 33020's N-P-L-F percentage
> bands or its exact capability level rule** — see §2.3.

---

## 1. Two registers, kept apart

The single most common confusion about provenance in this repository:

| | Where the **map** comes from | Where the **instrument** comes from |
|---|---|---|
| What it covers | The 52 capabilities and 258 criteria — which published frameworks each line was drawn from | The rules that turn four observations into a level |
| Recorded in | `facts/sources.json`, graded A–D | Each scale module's own `BASIS` and `CAUTION` |
| Reported in | [`../out/provenance.md`](../out/provenance.md), sheet 8 of the workbook | [`../out/provenance.md`](../out/provenance.md) §"The measurement instrument", and on **every** view that uses the scale |
| Graded by | Whether a reviewer can open the source (ADR-0010) | Whether it was adopted, adapted or assembled by us (ADR-0010 derivation types) |

**A source is something we cite. A scale is something we wrote.** That is why the scales do
not appear in the graded source register: putting them there would imply the ladder is a
citation, when it is a rule of ours that happens to be adapted from one. ADR-0010's answer
is to say which half is borrowed, on the face of the artifact — which is what `BASIS` does,
and why it is a required field.

---

## 2. The default scale — Capability level

**`scales/capability_level.py` · 0 Incomplete → 5 Innovating · derivable to 3 today.**

This is the assessment. Everything else is a lens.

### 2.1 What it is adapted from

**ISO/IEC 33020:2019** — *Information technology — Process assessment — Process measurement
framework for assessment of process capability*, second edition, 2019-11. It is the
measurement framework behind the ISO/IEC 330xx family, and the second edition cancels and
replaces the 2015 edition.

The four observations map onto its process attributes:

| Our observation | ISO/IEC 33020 attribute |
|---|---|
| **Practised** | PA 1.1 Process performance |
| **Enabled** | PA 2.1 outcome — resources provided and maintained |
| **Skilled** | PA 2.1 outcome — competent persons |
| **Defined** | PA 3.1 Process definition, deployed per PA 3.2 |

**The ordering is the standard's, not ours.** Performance is the Level 1 attribute;
resources and competence are Level 2; a defined process is Level 3. This is why an approved
standard with nothing performed against it earns **no level at all** — and it is the single
most useful thing about the borrowing, because it is the ordering that stops *"we approved
the technology"* from reading as *"we have the capability"*.

### 2.2 What is adopted, and what is ours

| | |
|---|---|
| **Adopted** | The level ladder and its names; the ordering of the attributes; the idea that a level is *derived from attribute achievement* rather than asserted |
| **Ours** | Collapsing five process attributes to four capability observations; a three-value scale (`yes` / `partial` / `no`) in place of the standard's four-point N-P-L-F; applying a *process* measurement framework to a *capability* map; the exact rule in `level()` |

Under ADR-0010 the derivation type is **adapted** — not *adopted*, because the rule is a
simplification of ours, and not *synthesized*, because the ladder and its ordering are not.

### 2.3 What has **not** been verified — the standing caution

ISO/IEC 33020:2019 is **paywalled** (grade C: available, but a reviewer without a licence
cannot open it), and its published preview stops before clause 5.3.

| | |
|---|---|
| **Verified from the preview, safe to cite** | The six-point scale 0 Incomplete → 5 Innovating; the process attribute identifiers and names; PA 2.1's resource and competence outcomes; that the second edition cancels and replaces the 2015 edition |
| **NOT verified — must not be quoted** | The **N-P-L-F percentage bands**, and the **exact capability level rule**. Both come from secondary sources describing the *superseded* ISO/IEC 15504, not from this standard |

> **Cite the scale by name and the levels by clause. Never quote the percentages.** A
> secondary source establishes that a claim exists, not that it is true; a summary of a
> paywalled standard is evidence about the summary.

Closing this needs someone to open the standard through the Bank's ISO subscription —
[OPEN-ITEMS](../OPEN-ITEMS.md) #10.

### 2.4 The one thing the ladder cannot prove

**Level 3 is read, not evidenced.** `defined` says an approved standard exists; `practised`
says the work is done. Neither says the work *follows* the standard. Level 3 infers
conformance from the two facts sitting together, and its reason line says so rather than
asserting what the evidence does not carry. A fifth observation — `conforms` — would make it
checkable. [OPEN-ITEMS](../OPEN-ITEMS.md) #7.

**Levels 4 and 5 are defined but unreachable.** They need threshold monitoring and a closed
improvement cycle, and nothing collects either. `DERIVABLE_MAX = 3` declares the ceiling so
that a capability at 3 does not quietly read as *the best there is*.
[OPEN-ITEMS](../OPEN-ITEMS.md) #8.

---

## 3. The lenses

A **lens** is a scale that is not the default. It exists so a room that already holds a
frame can be answered in it, without the assessment being redone and without anyone
pretending the evidence changed. **Where a lens and the default disagree, the default is
the finding.**

### 3.1 Institutional maturity

**`scales/maturity.py` · 1 Initial → 5 Optimizing · derivable to 3 today.**

The five-stage ladder — Initial · Emerging · Consolidating · Integrating · Optimizing — is
the conventional maturity vocabulary:

- **Initial** at 1 and **Optimizing** at 5 are CMM/CMMI (**SEI, 1991**) — public, citable,
  and the origin of the whole convention.
- The **middle-band words** are the generic vocabulary that recurs across many published
  maturity models. No model owns them.

> **Cite the shape, never a slide.** This ladder is **not** adopted from any particular
> institution's maturity model and must never be attributed to one. A reader may recognise
> the vocabulary from a peer institution's deck; that recognition is the convention, not a
> lineage. Writing *"adopted from <that institution>'s maturity model"* would turn a
> non-public artifact into the stated support for a claim, which the handling rules forbid.
> See §6 and [ADR-0011](decisions/adr/0011-scale-provenance.md) §2.4.

**It deliberately does not behave like a maturity model.** Maturity ladders are
conventionally the forgiving instrument, rating the enablers when practice is unobserved.
This one applies **the same performance gate as the default**: tooling and an approved
standard with no observed practice is *not rated*, not Level 1. The lens changes the
question — how far has a practice spread, rather than what has been established — not the
evidence required to answer it.

### 3.2 Executive readiness

**`scales/executive.py` · 1 Planning → 5 Leading.**

**Wholly ours.** Derivation type **synthesized** under ADR-0010: no published model,
licensed or otherwise, is reproduced. The level names are our own words, and no analyst
capability names, descriptions or level text are carried into this repository.

Two things to know before showing it:

- **It averages, deliberately** — the fraction of applicable observations achieved, banded.
  `n/a` and `unknown` drop out of the denominator rather than counting as failures.
- **It does not gate on performance.** It is the one instrument here that will place a level
  from the enablers alone. That is what makes it useful for the room that asks *"how much of
  what we said we would do exists?"* — and exactly why it is a lens and never the
  assessment. Every level it currently shows rests on enablers with no observed practice
  behind them.

A floor guards the worst failure: below two *scored* dimensions it declines to rate at all,
because a fraction computed from one cell is not an average. Before that floor existed, a
single `yes` produced a reported Level 5.

---

## 4. What the numbers on a ladder are not

| | |
|---|---|
| **A taxonomy level** (L1 domain, L2 capability, L3 criterion) | A position in the map. Written `L3`. |
| **A capability level** (0–5) | What a scale returns. Written `Level 3`. |

They are different things, and a ladder's digits are **not comparable across scales**: the
executive lens runs 1–5 where the default derives 0–3 today, so a 4 there is not "better"
than a 3 here. The report compares the maturity lens level for level, because every level it
can return is one the default can return, and refuses to compare the executive one's digits.

**Do not average an ordinal level** in the default scale. The executive lens does average,
deliberately, and says so on every view — that is why it is a lens.

---

## 5. What was retired, and why

Earlier versions carried **two scales**: maturity on a capability, readiness on a
realization, never to be merged.

| Retired | It was | Provenance it had | Replaced by |
|---|---|---|---|
| **Maturity 1–5** on a capability | The institution's ability, typed against 52 rubrics | **Adopted** — the CMMI shape | A level **derived** from four observations |
| **Readiness 0–5** on a realization | How well the enterprise had packaged something for consumption | **Synthesized** — built here, because nothing published measured it | The `enabled` observation, which cannot produce a level alone |

[ADR-0011](decisions/adr/0011-scale-provenance.md) is the survey behind those two: what was
available to adopt, what was found, and why readiness had to be built. **Its survey is still
accurate and worth reading. Its conclusion is superseded** by
[ADR-0013](decisions/adr/0013-facts-and-scales.md) — and the current default scale has a
*stronger* provenance position than the synthesized readiness scale ever did, because it is
adapted from a published standard rather than assembled.

**The fact the old model was protecting is still protected**, structurally rather than by
convention: supply cannot produce a level, because `enabled` contributes nothing without
`practised`. See [`what-is-settled.md`](what-is-settled.md) §4 and
[`glossary.md`](glossary.md) §3 for the three surviving senses of the word *readiness*.

---

## 6. Before any of this leaves the Bank

| Check | Why |
|---|---|
| **No ISO/IEC 33020 percentage bands or level rule quoted** | Unverified, and from a superseded predecessor (§2.3) |
| **The maturity ladder is not attributed to any institution's model** | It is the generic convention; attributing it would rest a claim on a non-public artifact |
| **No licensed analyst wording anywhere** | Usable internally, never reproduced externally, never listed as a source |
| **Nothing from `docs/notes/`** | Grade D, internal only |
| **ADR-0011 §2.4 and §3.4 stripped** | They discuss the non-public comparator |
| **[`../out/provenance.md`](../out/provenance.md) checked for grade-D support** | A grade-D source cannot support a claim that leaves the Bank, whatever its quality |

ISO/IEC 33020 itself is **grade C**, not D: it is a real, citable, current standard — a
reviewer simply needs a licence to open it. Citing it by name is fine. Quoting what we have
not read is not.

---

## 7. If you are asked *"is this standard?"*

The honest answer, in one paragraph:

> The capability map is ours, drawn from published frameworks that are cited and graded.
> The measurement scale is **adapted from ISO/IEC 33020:2019**, the ISO process measurement
> framework — we took its ladder and, more importantly, its ordering, in which performance
> precedes definition. What is ours is stated on the face of every view: four observations
> in place of five process attributes, three values in place of its four, and a simplified
> rule. The two lenses are ours; one borrows only the conventional CMM ladder shape, the
> other borrows nothing. Nothing here claims to *be* an ISO assessment, and no capability is
> rated against a clause we have not opened.


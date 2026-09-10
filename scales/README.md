# Scales

A **scale** turns observations into a level. It is the only place in this repository
where a judgement is encoded.

The separation that makes this work:

| Layer | What it holds | Changes when |
|---|---|---|
| `facts/` | What is true about the Bank, with evidence and a date | The Bank changes |
| `scales/` | Rules that read facts and produce a level | We change our mind about measurement |
| `out/` | Views, one per scale | Either of the above changes |

**An observation is a fact, not a score.** *"The Foundry Agents Standard is pre-release"*
is true whichever framework reads it. That single record feeds every scale below, so
no two scales can contradict each other on the underlying evidence — only on what
they choose to make of it. **Where a lens and the default disagree, the default is the
finding.**

## The scales that ship

| File | Level names | Use it for | Status |
|---|---|---|---|
| `capability_level.py` | 0 Incomplete → 5 Innovating | **The default.** Engineering, platform teams, assurance | Adapted from ISO/IEC 33020:2019 |
| `executive.py` | 1 Planning → 5 Leading | A committee that already knows the analyst frame. **Averages**, and does not gate on performance | Lens |
| `maturity.py` | 1 Initial → 5 Optimizing | A reader who arrives holding the CMMI-shaped maturity frame. Same performance gate as the default | Lens |

The report compares all three over the same capabilities. Because the executive ladder
runs 1–5 and the default derives 0–3 today, the report does not read one's digits against
the other's; it compares the maturity lens level for level because every level it can
return is one the default can return.

Run `python3 build/build.py views` to regenerate every view for every scale, and
`python3 build/build.py check` to validate every scale against the contract below.

## Adding a scale — the contract

One file in this directory. The build discovers scales by listing the directory and
`check` refuses to build if any scale breaks the contract, so a mistake here is caught
before it reaches a view.

```python
NAME     = "Human-readable name"            # required
SHORT    = "name"                           # required; lowercase, digits, _ or -; names out/capability-assessment-<SHORT>.md
BASIS    = "What is adopted, what is ours"  # required; shown on every view (ADR-0010)
CAUTION  = "What is verified against the source, and what is not"  # optional but
                                            # expected where BASIS names a source;
                                            # travels with the claim into every
                                            # provenance view
QUESTION = "The one question this scale puts to the observations"   # required for the report's comparison table
LEVELS   = [(0, "Level name", "What it means"), ...]                # required; ints ascending, unique
DEFAULT  = True                             # exactly one scale in the directory; the others are lenses
DERIVABLE_MAX = 3                           # optional; the highest level today's observations can reach

def level(obs):
    """obs: {"practised": v, "enabled": v, "skilled": v, "defined": v},
    v in yes / partial / no / n/a / unknown.  Return (n, why): n one of the
    LEVELS numbers, or None for NOT RATED; why one sentence a reader can act on."""

def note():                                 # optional; one paragraph shown under BASIS on every view
    return "..."
```

**`CAUTION` is where the boundary of the check lives.** `BASIS` says what was borrowed; `CAUTION` says how far anyone actually opened the source, and what therefore must not be quoted. Keeping it on the scale rather than in this README means the caveat travels with the claim into `out/provenance.md` and every view. The full narrative — including what was retired and the handling rules — is [`../docs/where-the-scales-come-from.md`](../docs/where-the-scales-come-from.md).

What `check` verifies: the required names exist and have the right types; `SHORT` is
unique and file-safe; `LEVELS` are ascending and unique; `DERIVABLE_MAX` is one of them;
`level()` returns `(int-or-None, non-empty str)` for **all 625 combinations** of the five
values over the four observations, never a level outside `LEVELS`, never above
`DERIVABLE_MAX`, and returns `None` for at least one combination (a scale must be able to
say *not rated*).

Two conventions the builders rely on:

- **`None` means not rated** — the evidence to place it has never been gathered. It is a
  result, not a zero, and the views draw it in the palest tone rather than as 0.
- **A scale that gates on performance** returns `None` when `practised` is `unknown`,
  however good the other three look. The report detects this from behaviour, not from a
  flag, and says which scales gate and which do not.

Nothing else in the repository needs to change.

## Why the default is what it is

`capability_level.py` is **adapted from ISO/IEC 33020:2019**, the process measurement
framework behind the ISO/IEC 330xx family. Verified against the standard's published
preview on 4 September 2026:

- Six-point ordinal scale, **0 Incomplete → 5 Innovating** (clause 5.2).
- **PA 1.1 Process performance** at Level 1: *"the extent to which the process purpose
  is achieved"*.
- **PA 2.1 Performance management** at Level 2, whose outcomes include that
  *"resources necessary for performing the process are determined, provided and
  maintained"* and that *"person(s) performing the process are competent on the basis
  of appropriate education, training, or experience"*.
- **PA 3.1 Process definition** and **PA 3.2 Process deployment** at Level 3.

Our four observations map onto those attributes:

| Observation | ISO/IEC 33020 attribute |
|---|---|
| Practised | PA 1.1 Process performance |
| Enabled | PA 2.1 outcome (e) — resources provided and maintained |
| Skilled | PA 2.1 outcome (f) — competent persons |
| Defined | PA 3.1 Process definition, deployed per PA 3.2 |

**The order matters and it is the standard's, not ours.** Performance comes first. A
published standard with nothing performed against it earns **no level at all**. That is
the opposite of what an earlier draft of this model assumed, and it is the finding the
Bank needs: *the enablers for Levels 2 and 3 were built before Level 1 was widely
performed.*

### What is ours, stated plainly

Under [ADR-0010](../docs/decisions/adr/0010-provenance-grading.md), say which half is
borrowed:

- **Adapted:** the level ladder, the attribute ordering, the idea that a level is
  derived from attribute achievement rather than asserted.
- **Ours:** collapsing five process attributes to four capability observations; a
  three-value scale (yes / partial / no) in place of the standard's four-point
  N-P-L-F; applying a *process* measurement framework to a *capability* map.

## Why the maturity lens is safe to ship

`maturity.py` uses the conventional five-stage ladder — **1 Initial · 2 Emerging ·
3 Consolidating · 4 Integrating · 5 Optimizing**. A reader may recognize that vocabulary
from a peer institution's slide. It is not taken from one.

- **Initial** and **Optimizing** are CMM/CMMI levels 1 and 5 (SEI, 1991) — public,
  citable, and the origin of the whole convention.
- The middle-band words are the generic vocabulary that recurs across many published
  maturity models. No model owns them.

What ADR-0011 §2.4 grades **D** is a specific non-public artifact, not the observation
that maturity ladders are conventionally named this way. So: cite the shape, never the
slide. `BASIS` says the ladder is ours and conventional, and no `BASIS`, level name or
reason string in this repository attributes it to any particular institution or model.
Writing *"adopted from <that institution>'s maturity model"* would turn a grade-D
artifact into the stated support for a claim, which is exactly what the handling rule
forbids — do not.

**It does not behave like a typical maturity model, on purpose.** Maturity ladders are
conventionally the forgiving instrument, rating the enablers when the practice is
unobserved. This one applies the same performance gate as the default scale: a
capability with tooling and an approved standard but no observed practice is **not
rated**, not Level 1. Rating the enablers alone is how *"we approved the technology"*
comes to read as *"we have the capability"*, which is the finding this model exists to
prevent. The lens changes the question — how far has a practice spread, rather than what
has been established — not the evidence required to answer it.

### Not yet verified — do not write these down

ISO/IEC 33020:2019 is paywalled (CHF 181, 42 pages). The published preview stops before
clause 5.3. Two things therefore rest on secondary sources and **must not be quoted**
until someone opens the standard through the Bank's ISO subscription:

- the **N-P-L-F percentage bands** (0–15 / >15–50 / >50–85 / >85–100). Those bands are
  confirmed for the superseded ISO/IEC 15504, not for 33020.
- the exact **capability level rule** (lower attributes Fully, current level at least
  Largely).

Our `level()` implements a simplified rule of our own and says so. Cite the scale by
name and the level definitions by clause. Do not cite percentages.

**Grade C** — paywalled, so a reviewer without a licence cannot open it.

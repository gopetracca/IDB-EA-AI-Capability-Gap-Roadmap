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
two scales can never contradict each other on the underlying evidence — only on what
they choose to make of it.

## The scales that ship

| File | Level names | Use it for | Status |
|---|---|---|---|
| `capability-level.py` | 0 Incomplete → 5 Innovating | **The default.** Engineering, platform teams, assurance | Adapted from ISO/IEC 33020:2019 |
| `executive.py` | 1 Planning → 5 Leading | A committee that already knows the analyst frame | Lens |

Run `python3 build/build.py views` to regenerate every view for every scale.

## Adding a scale

One file in this directory exposing three names:

```python
NAME    = "Human-readable name"
LEVELS  = [(0, "Level name", "What it means"), ...]
def level(obs):        # obs: {"practised": "yes", "enabled": "n/a", ...}
    return (n, "why")  # the level, and one sentence explaining it
```

Nothing else in the repository needs to change. The build discovers scales by
directory listing.

## Why the default is what it is

`capability-level.py` is **adapted from ISO/IEC 33020:2019**, the process measurement
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

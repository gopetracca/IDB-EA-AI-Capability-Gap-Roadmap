# Migration scripts · 4 September 2026

One-off, already run. Kept so the conversion can be audited or repeated.

| Script | Does |
|---|---|
| `extract.py` | Reads `../old-model/`, `../old-build/` and the old `model/`, writes `facts/*.json`. Pure conversion — no judgement, no data invented |
| `seed_obs.py` | Writes `facts/observations.json`. Seeds `enabled` and `defined` from the asset register; writes `practised` and `skilled` as `unknown` because they had never been observed |

`seed_obs.py` is the one to read if you want to know where today's observations came
from. The rule it applied: an asset that is `Published`, `Published (JFrog)` or `In use`
counts as released; `Pre-release`, `In review by DX` and `Built, not yet distributed` do
not, and hold the observation at `partial`.

Neither script will run correctly again now that the old paths have moved. They are
history, not tooling.

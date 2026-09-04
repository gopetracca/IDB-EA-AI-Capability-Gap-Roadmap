# Reference catalog and TRM · frozen

**Not maintained.** Frozen 4 September 2026, not deleted.

`catalog4.py` holds 143 vendor-neutral entries — 76 services, 57 ABBs, 5 patterns,
5 standards — with typed edges to capability criteria. It is good work that answers a
question nobody at the Bank was asking, and maintaining it against a market that renames
its products twice a year is a standing cost with no reader.

Worth lifting if you ever need it:

- **`S3.16 Hybrid Retrieval Pattern`** is a properly written architecture pattern —
  problem, context, forces, solution, resulting context, rationale, known uses. If a
  retrieval design review needs a pattern, start here.
- The **currency notes** in `gen_trm.py` record what changed in the market through 2026:
  Azure AI Foundry renamed, AWS's July 2026 retirement wave, Agentspace becoming Gemini
  Enterprise, MCP and A2A moving to the Agentic AI Foundation. Those date fast.

`mkregister.py` contained a **fourth** delivery-state scale (0 Nothing → 4 Managed
service), different again from the two in the model. That contradiction is why the
refactor happened.

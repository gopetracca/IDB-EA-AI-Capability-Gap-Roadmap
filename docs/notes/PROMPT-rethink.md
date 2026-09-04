# Prompt — full rethink of the AI capability model

Paste to a fresh Fable session with this repository attached.
Written 4 September 2026.

---

You are reviewing a body of work I have built over several weeks and am no longer
confident in. I want you to think hard about whether it is the right shape, and to
tell me plainly if it is not. **Nothing here is settled.** Every ADR in `decisions/adr/`
is provisional for the purposes of this conversation — including ADR-0001, which the
repo currently treats as load-bearing. If the honest answer is that the core structure
is wrong, say that.

## Who I am and what I actually need

I work in **Enterprise Architecture at the Inter-American Development Bank**. My job
here is to produce, for AI: a capability map, a maturity assessment, a gap analysis,
a current and target state, and a roadmap.

The concrete thing that is going wrong:

> **People inside the Bank say we do not have the capability to run AI agents.**
> That is false (in part). EA has already defined the Microsoft Foundry deployment standard, the
> agent build standard, reference architectures, Terraform modules, template
> repositories, and standards for custom MCP servers. The work exists. I cannot make
> it visible in a form that settles the argument.

The thing is that we are missing the rest of the work. Platform teams now need to operationalize what we defined in the standards. Product teams need to implement. People need to learn and catch up. 

That is the test. Whatever you propose has to let me walk into a room and answer that
claim in a way that holds up.

## What is in the repository

Read it fully before responding. Orientation, not a substitute for reading:

- `README.md`, `CLAUDE.md` — the conventions as they currently stand
- `OPEN-ITEMS.md` — 13 unresolved items, honestly kept; read this early
- `model/model3.json` — 8 domains, 52 L2 capabilities, 258 L3 criteria
- `model/catalog4.py` — 143-entry vendor-neutral reference catalog
- `model/realization.json` — the readiness scale and the realization register
- `model/sources.json` — 40 sources graded A–D for whether a reviewer can open them
- `decisions/adr/` — 12 ADRs, 0001 and 0011 the most consequential
- `analysis/como-funciona-el-modelo.md` — my attempt to explain the whole thing in Spanish
- `provenance/findings-2026-09-03.md` — four findings that block external publication
- `build/`, `out/` — generators and generated deliverables

## What I think is wrong (test these — do not just agree)

1. **It is a mess, and it is too big.** 52 capabilities × 258 criteria, 51 of 52
   rubrics unwritten, no target state designed at all. The cost to populate this
   honestly is enormous and I am not sure the Bank gets that value back.

2. **Capability + realization is hard to explain.** I built the two-scale split
   (ADR-0001) because a single number conflates *can we do this* with *is it packaged*.
   I still believe the distinction is real. But I cannot get colleagues to hold both
   ideas at once, and I do not fully hold them myself under pressure. Either the idea
   needs a better surface, or it needs to stop being the centerpiece.

3. **Provenance may be over-engineered.** I built a graded source register because
   much of what I defined exists in no single external framework and I wanted evidence
   behind my proposals. It may be more rigor than the audience will ever ask for —
   or it may be the only thing that makes this defensible. I genuinely do not know.

4. **I have not chosen a register.** Strategic (Gartner/McKinsey — narrative,
   executive-legible, thin underneath) or technical (architecturally precise, credible
   to engineers, unreadable to a VP). **My instinct is technical.** But I want the
   reporting quality of the strategy firms — the one-page story, the clean visual, the
   finding that lands. Tell me whether those can coexist in one artifact or whether
   they must be two, and say which is primary.

## What I want from you

Work in this order. Do not skip to the model.

**1 — Read and diagnose.** What is actually here, what is genuinely good and worth
keeping, what is scaffolding I built to feel rigorous. Be blunt. I would rather throw
away three weeks now than defend the wrong thing in front of a steering committee.

**2 — Answer the agent question first.** Using only what is already in the repo, show
me the smallest artifact that rebuts *"we cannot run AI agents."* If the current model
can already produce it, show me how and tell me why I could not see it. If it cannot,
that is the sharpest evidence something structural is wrong — name what.

**3 — Then propose the target shape**, as options, not one answer. For each:
   - what the core objects are and how many of each a human must populate
   - the effort to reach a first credible assessment, in weeks, honestly
   - what it costs me — which ADRs it breaks, what evidence it throws away
   - how it handles the Foundry/agents case specifically
   - who can read the output without me in the room

   Include at least one option that is **substantially smaller** than what exists
   today, and be explicit about what precision it sacrifices. If collapsing maturity
   and readiness back into one number is the right call, argue for it properly —
   read ADR-0001 and ADR-0011 first and defeat them on the merits.

**4 — Settle strategic vs. technical** with a recommendation, not a survey.

**5 — Give me a path.** What I do first, what I stop doing, what I keep on ice. Assume
one person, part-time, with reviewers who are not waiting patiently.

## How to work

- **Recommend. Do not enumerate.** Where you are uncertain, say so in a sentence and
  still make the call.
- **Disagree with the repo where it is wrong.** Approval is not the goal. The ADRs are
  my prior reasoning, not a constraint; where one is well argued, tell me that too —
  I need to know what survives, not only what falls.
- **Do not write code or edit any file this pass.** This is a thinking pass. Proposals
  in prose. If a change is worth making, we make it after I agree.
- **Ask me before proposing** if something material is undecidable from the repo. A
  short list of real blocking questions beats an answer built on guesses about the
  Bank's politics, appetite, or reviewers.
- research if you need to

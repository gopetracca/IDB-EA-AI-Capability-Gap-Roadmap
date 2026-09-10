---
name: decisions
description: Use when something about how the model is structured or measured is being decided, changed, reversed, refined or questioned — a new rule, a scale added or retired, an observation redefined, a file moved that an ADR points at — or when someone asks "why is it like this", "is this settled", or "which ADR covers this".
---

# Recording a decision

`docs/decisions/adr/` holds Architecture Decision Records, one decision per file, numbered
`ADR-NNNN`, never renumbered. The index and status vocabulary are in
`docs/decisions/README.md`; the template is `docs/decisions/TEMPLATE.md`. ADR-0013 governs
the model; ADR-0014 amends it. Read both before deciding anything about observations,
scales or levels.

## Is it a decision?

| It is… | Record it in |
|---|---|
| Something true about the Bank (an asset was released, an owner confirmed) | `facts/` — it is a fact, not a decision |
| A rule for turning facts into a level | `scales/` — and an ADR if the rule is new or changes meaning |
| How the model is structured or measured, and a standard does not settle it | An ADR |
| A file an ADR points at has moved | A dated *location note* under the pointer in that ADR |
| A refinement of wording that reverses nothing | A dated `## Amendment N` at the end of the ADR |
| A reversal | A **new** ADR, and a banner on the old one |

If a standard settles it, cite the standard (the `citing` skill) and there is no ADR to write.

## The four moves

**New decision.** Copy `TEMPLATE.md` to `adr/NNNN-short-imperative-title.md` with the next
free number. Fill the frontmatter (`id`, `title`, `status: Proposed` or `Accepted`, `date`,
`decision_owner`, `supersedes`, `depends_on`). Write Context, Decision (present tense, as a
rule someone can apply), Options considered (record the rejected ones — someone will ask),
Consequences, Open. Add a row to the index table in `docs/decisions/README.md`. If it
changes what the builders do, make the code change in the same piece of work and say so in
Consequences.

**Amendment.** Append `## Amendment N — <date>` to the ADR. First sentence says what kind:
*"Wording only; no decision reversed"* or *"Enforcement only"*. Add `amended: <date>` to the
frontmatter and update the index status to *Accepted, amended*. ADR-0009 and ADR-0013 are
the precedents.

**Supersession.** Write the new ADR with `supersedes: [ADR-000X]`. In the old one, add
`superseded_by: [ADR-NNNN]` to the frontmatter, set `status: Superseded`, and put a banner
at the top:

```markdown
> ## ⚠ SUPERSEDED by [ADR-NNNN](NNNN-title.md) — <date>
>
> <One paragraph: what replaces it, and where the old record was right.>
>
> This record is kept unedited: an ADR is never rewritten to reverse itself.
```

Then update the index row. Do not touch the body. ADR-0001 to ADR-0003 are the precedents.

**Location note.** Under the pointer:

```markdown
> *Location note, <date>:* now `facts/…`. <One sentence on what changed around it.>
```

## Never

- Edit an ADR's Decision or Consequences to say something different. Reversal is a new ADR.
- Delete or renumber an ADR.
- Leave the index out of date: status and "amended by" live there too.
- Write `D3` for a decision. `D1`–`D8` are also the domain ids; write `ADR-0003` and
  `domain D3`.
- Record a judgement in `facts/` to avoid writing an ADR, or type a level anywhere.

## If the working tree does not match what an ADR or `git log` implies

`git status` before you start. A workspace can carry uncommitted work from an interrupted
session, someone else's in-progress change, or content that arrived by a path other than
`git checkout` and so has no commit to diff against. Do not build a new decision on top of
content you cannot explain:

- **Read the tracked state directly** (`git show HEAD:<path>`) for anything you rely on —
  a rating count, a level distribution, whether a file exists — rather than trusting what
  is currently on disk if the two might differ. Recompute a cited figure by running the
  real build against that tracked state; do not carry forward a number from unexplained
  content without checking it.
- **Do not silently adopt unrelated pending work**, however competent it looks, and do not
  silently discard it either. Restore only the specific files your decision needs to a
  known-good state to build cleanly; leave everything else exactly as found.
- **Say so in your report**, plainly and early, with what you found and what you did about
  it. The repository owner decides what to do with pending work that is not yours to judge.

## Retiring or adding a scale, specifically

Scales are discovered from `scales/`, so the code change is one file. The decision is not:
a lens that ships has been quoted, and removing it changes what the report compares. Write
the ADR (it does not supersede ADR-0013, which allows lenses; it refines which ones ship),
then move the file to `archive/` with a line in `archive/README.md`, update
`scales/README.md` and `OPEN-ITEMS.md`, and run:

```bash
uv run python build/build.py check && uv run python build/build.py all && uv run python build/build.py test
```

## After recording

Update `CLAUDE.md` §5 if the decision is one a new session must know, `OPEN-ITEMS.md` if
it opens or closes an item, and `docs/how-it-works.md` if it changes what a reader is told.

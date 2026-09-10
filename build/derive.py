# -*- coding: utf-8 -*-
"""Explain a scale by running it, not by describing it.

A scale is a rule in Python.  A reader who has to ask *"why is this one a 2 and
that one a 3?"* cannot open the rule, and a prose paragraph describing it is a
second copy that goes wrong the moment the rule changes.  So this module derives
the explanation from the rule itself, by evaluating it over all 625 combinations
of the five observation values across the four observations.

Two things come out:

  ladder(scale)   what each rung actually requires, and what the next rung adds
  worked(scales)  a set of named situations, run through every scale at once

Both are computed.  Neither is typed anywhere, and neither can disagree with the
code it describes - if a scale changes, the tables change with it.

Nothing here reads facts/ and nothing here names a scale.
"""
import itertools

# The four observations, in the order a reader meets them, and the five values
# any one of them may take.  These are properties of the observation model
# (ADR-0013), not of any scale.
TYPES = ["practised", "enabled", "skilled", "defined"]
VALUES = ["yes", "partial", "no", "n/a", "unknown"]


def _all_combos():
    return [dict(zip(TYPES, c)) for c in itertools.product(VALUES, repeat=len(TYPES))]


def _phrase(vals):
    """The permitted values for one observation, as something readable.

    Returns (text, kind) where kind is 'any', 'one' or 'some' - the caller
    decides how to style each.
    """
    n = len(vals)
    if n == len(VALUES):
        return "any", "any"
    if n == 1:
        return vals[0], "one"
    missing = [v for v in VALUES if v not in vals]
    if len(missing) == 1:
        return "not %s" % missing[0], "some"
    return " or ".join(vals), "some"


def ladder(scale):
    """What it takes to reach each level of one scale.

    Returns a list of rungs, lowest first, each:

        {"n", "name", "meaning",       the level itself
         "conds": {observation: {"vals", "text", "kind"}},
         "exact": bool,                 whether the conditions ARE the rule
         "adds":  [(observation, text)] what this rung requires that the one
                                        below it did not - empty on a scale
                                        no per-observation rule describes,
         "lowest": bool,                the bottom rung: "rated at all"
         "combos": int}                 how many of the 625 reach it

    The conditions are cumulative - *to reach at least this level* - because
    that is the form in which an ordered ladder is exactly describable.  When
    `exact` is False the conditions are still true of every capability at that
    level, but they do not by themselves determine it: the scale is doing
    something no per-observation condition can express, such as averaging.
    """
    combos = _all_combos()
    scored = [(o, scale.level(o)[0]) for o in combos]
    out = []
    prev, prev_exact = None, False
    for n, name, meaning in scale.LEVELS:
        reach = [o for o, lv in scored if lv is not None and lv >= n]
        if not reach:
            continue
        conds, size = {}, 1
        for t in TYPES:
            vals = [v for v in VALUES if any(o[t] == v for o in reach)]
            text, kind = _phrase(vals)
            conds[t] = {"vals": vals, "text": text, "kind": kind}
            size *= len(vals)
        exact = size == len(reach)
        # What this rung asks for that the one below did not.  Only meaningful
        # when both rungs are exactly described by their conditions; on a scale
        # that averages, "what the next level adds" is not a per-observation
        # statement at all, and pretending otherwise would mislead.
        adds = []
        if prev is not None and exact and prev_exact:
            for t in TYPES:
                if conds[t]["vals"] != prev[t]["vals"]:
                    adds.append((t, conds[t]["text"]))
        out.append({"n": n, "name": name, "meaning": meaning, "conds": conds,
                    "exact": exact, "adds": adds, "combos": len(reach),
                    "lowest": prev is None})
        prev, prev_exact = conds, exact
    return out


def unrated(scale):
    """What leaves this scale unable to place a level.

    Returns (parts, count) where parts is [(observation, [values])] - each pair
    meaning *whenever this observation holds one of these values, the scale
    returns not rated, whatever the other three say*.  An empty parts list with
    a non-zero count means no single observation forces it: the scale declines
    for some other reason, such as too few dimensions observed to average.

    Markup is the caller's business; nothing here is formatted.
    """
    combos = _all_combos()
    none = [o for o in combos if scale.level(o)[0] is None]
    if not none:
        return [], 0
    parts = []
    for t in TYPES:
        vals = [v for v in VALUES if any(o[t] == v for o in none)]
        # an observation only explains 'not rated' when it is constrained
        if len(vals) < len(VALUES):
            always = [v for v in vals
                      if all(scale.level(o)[0] is None
                             for o in combos if o[t] == v)]
            if always:
                parts.append((t, always))
    return parts, len(none)


def gates_on_practice(scale):
    """True if this scale refuses to place a level when performance has never
    been observed, however good the other three look.  Read from behaviour."""
    return scale.level({"practised": "unknown", "enabled": "yes",
                        "skilled": "yes", "defined": "yes"})[0] is None


# ---------------------------------------------------------------- worked cases
# Situations a reviewer will actually record, written as observation values.
# No level appears here: every level in the rendered table is computed by
# running each scale over these values.
CASES = [
    ("Nobody has looked yet",
     ("unknown", "unknown", "unknown", "unknown")),
    ("The enablers exist, but nobody has asked whether the work is done",
     ("unknown", "yes", "yes", "yes")),
    ("Someone looked: it is not done, though the enablers exist",
     ("no", "yes", "yes", "yes")),
    ("Done on some systems, nothing else observed",
     ("partial", "unknown", "unknown", "unknown")),
    ("Done everywhere, but no tooling is provided",
     ("yes", "no", "yes", "yes")),
    ("Done everywhere, tooled, but competence not evidenced",
     ("yes", "yes", "unknown", "yes")),
    ("Done everywhere, tooled and staffed, no standard recorded",
     ("yes", "yes", "yes", "unknown")),
    ("Done everywhere, tooled and staffed, standard pre-release",
     ("yes", "yes", "yes", "partial")),
    ("Done everywhere, tooled and staffed, approved standard",
     ("yes", "yes", "yes", "yes")),
    ("Done everywhere and staffed; no tooling is needed here",
     ("yes", "n/a", "yes", "yes")),
]


def worked(scales, cases=None):
    """The same observations read by every scale, side by side.

    Returns [(label, obs, [(scale, level|None, level name|'not rated', why)])].
    This is the answer to *"how do I get from four answers to a number?"* - it
    shows the arithmetic happening rather than asserting it.
    """
    out = []
    for label, vals in (cases or CASES):
        obs = dict(zip(TYPES, vals))
        row = []
        for s in scales:
            n, why = s.level(obs)
            names = dict((k, nm) for k, nm, _ in s.LEVELS)
            row.append((s, n, names.get(n, "not rated") if n is not None
                        else "not rated", why))
        out.append((label, obs, row))
    return out


def recorded_at(m):
    """Where each observation is entered, and where it is derived.

    Reads the observation model from facts (via the caller's Model), so it
    stays right if an observation moves between taxonomy levels.  Returns
    [(observation, at, rows, derived_at, question)].
    """
    n_crit = sum(len(c['criteria']) for c in m.capabilities)
    out = []
    for t in m.observation_types:
        tid = t['id']
        per_crit = tid in m.criterion_types
        out.append({
            "id": tid,
            "at": "L3 criterion" if per_crit else "L2 capability",
            "rows": n_crit if per_crit else len(m.capabilities),
            "derived_at": "L2 capability" if per_crit else "",
            "question": t.get('question', ''),
            "evidence": t.get('evidence_expected', ''),
        })
    return out

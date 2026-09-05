# -*- coding: utf-8 -*-
"""Executive lens - the same observations, read the way a steering committee reads.

A LENS, not the default.  Use it only when a room arrives already holding the
analyst frame.  The default scale is scales/capability_level.py.

This deliberately answers a different question.  The default asks "has the
institution established this practice?".  This asks "how much of what we said we
would do exists?", which is coarser, more forgiving, and the question executives
actually ask.  The two will disagree on individual capabilities.  That is not an
error - it is the point of keeping the measurement separable from the facts.

Nothing here reproduces licensed analyst material: the level names below are our
own words, and no analyst capability names, descriptions or level text are
carried into this repository (CLAUDE.md handling rules).
"""

NAME = "Executive readiness"
SHORT = "exec"
QUESTION = "How much of what we said we would do actually exists?"
BASIS = ("Our own coarse roll-up for executive reporting. Reads the same "
         "observations as the default scale. Not adopted from any published model.")

LEVELS = [
    (1, "Planning", "Considered. Little or nothing exists yet."),
    (2, "Experimenting", "Something exists, in pieces, not joined up."),
    (3, "Stabilizing", "It exists and is used, with gaps."),
    (4, "Scaling", "It exists, is used, and is supported across the institution."),
    (5, "Leading", "Relied upon, measured and improved."),
]

WEIGHT = {"yes": 1.0, "partial": 0.5, "no": 0.0}

# An average over one observation is not an average, it is that one value
# wearing an average's clothes.  One 'yes' out of four dimensions produced a
# reported Level 5 "Leading" before this floor existed - the least-gated
# scale in the repository placing the most confident claim on the thinnest
# evidence, which is exactly the over-claiming this whole model exists to
# prevent.  Below this many SCORED dimensions (n/a and unknown do not count
# toward it - see level()), the lens declines to average at all.
MIN_SCORED = 2


def level(obs):
    """Fraction of the applicable observations that are achieved, banded.

    'n/a' observations drop out of the denominator rather than counting as
    failures - a governance capability with no platform component is not worse
    for having none.  'unknown' also drops out, but is reported, because an
    average over two known cells is not the same claim as one over four.

    Fewer than MIN_SCORED observed dimensions is not rated, however strong the
    one or two that exist look: a fraction computed from one cell is not an
    average, and reporting it as one would let a single 'yes' read as
    institution-wide reliance.
    """
    scored = {k: v for k, v in obs.items() if v in WEIGHT}
    na = [k for k, v in obs.items() if v == "n/a"]
    unknown = [k for k, v in obs.items() if v in ("unknown", "")]

    if len(scored) < MIN_SCORED:
        if not scored:
            return None, "Not rated: nothing has been observed"
        return None, ("Not rated: only %d of 4 dimensions observed (%s) - too "
                      "few to average without one cell carrying the whole claim"
                      % (len(scored), ", ".join(sorted(scored))))

    frac = sum(WEIGHT[v] for v in scored.values()) / len(scored)
    lvl = (1 if frac == 0 else 2 if frac < 0.5 else
           3 if frac < 0.75 else 4 if frac < 1.0 else 5)

    why = "%d of %d observed dimensions achieved" % (
        round(sum(WEIGHT[v] for v in scored.values())), len(scored))
    if unknown:
        why += "; %s not observed" % ", ".join(sorted(unknown))
    if na:
        why += "; %s not applicable" % ", ".join(sorted(na))
    return lvl, why


def note():
    return ("A LENS for executive reporting, not the assessment. It averages, which "
            "the default scale deliberately does not: a capability can look adequate "
            "here while the default scale holds it at Level 1 because nothing is "
            "performed. Where they disagree, the default scale is the finding.")

# -*- coding: utf-8 -*-
"""Capability level - the default scale.

Adapted from ISO/IEC 33020:2019, Information technology - Process assessment -
Process measurement framework for assessment of process capability, second
edition, 2019-11.  See scales/README.md for what is adopted, what is ours, and
what is not yet verified against the standard's text.

The rule, in one sentence: performance comes first.  A published standard with
nothing performed against it earns no level at all.
"""

NAME = "Capability level"
SHORT = "level"
# The assessment itself. Exactly one scale in scales/ carries this flag; the
# others are lenses, and the builders label them so.
DEFAULT = True
# The one-sentence question this scale puts to the four observations.
QUESTION = "Has the institution established this practice?"
BASIS = ("Adapted from ISO/IEC 33020:2019 (process measurement framework). "
         "Simplified: four observations rather than five process attributes, "
         "three values rather than the standard's four-point N-P-L-F scale.")
# What about this scale's basis has been verified against the source, and what
# has not.  Shown wherever the scale's provenance is reported, so the boundary
# of the check travels with the claim rather than living only in a README.
CAUTION = (
    "ISO/IEC 33020:2019 is paywalled and its published preview stops before "
    "clause 5.3. Verified from the preview and safe to cite: the six-point "
    "scale 0 Incomplete to 5 Innovating, the process attribute identifiers and "
    "names, and PA 2.1's resource and competence outcomes. NOT verified, and "
    "must not be quoted: the N-P-L-F percentage bands and the exact capability "
    "level rule - both come from secondary sources about the superseded "
    "ISO/IEC 15504, not from this standard. The rule implemented here is our "
    "own simplification and is labelled as such. Grade C: paywalled, so a "
    "reviewer without a licence cannot open it.")

LEVELS = [
    (0, "Incomplete",
     "The capability is not performed, or performance cannot be shown."),
    (1, "Performed",
     "It is done on real AI systems. Nothing is guaranteed to be repeatable."),
    (2, "Managed",
     "It is done, the tooling is provided, and the people doing it are competent."),
    (3, "Established",
     "An approved institutional standard exists and the work is done against it."),
    (4, "Predictable",
     "Performance is measured against thresholds and held there."),
    (5, "Innovating",
     "One evidence-driven improvement cycle has closed with a verified benefit."),
]

# Levels this scale can actually derive from the observations collected today.
# Anything above this is defined but unreachable, and the model says so rather
# than quietly topping out and letting a reader assume 3 means "the best we do".
DERIVABLE_MAX = 3

# Observation values that count as achieved / partly achieved.
FULL = {"yes"}
PART = {"partial"}
# "n/a" means the attribute does not apply to this capability and cannot block it.
NA = {"n/a"}
UNKNOWN = {"unknown", ""}


def _has(v):
    return v in FULL


def _at_least_partial(v):
    return v in FULL or v in PART


def _ok(v):
    """Achieved, or legitimately not applicable."""
    return v in FULL or v in NA


def level(obs):
    """obs: {'practised': 'yes'|'partial'|'no'|'n/a'|'unknown', ...} for the
    four observation types.  Returns (level:int|None, why:str).

    None means NOT RATED - the evidence to place it has never been gathered.
    That is a result, not a zero (see docs/how-it-works.md).
    """
    practised = obs.get("practised", "unknown")
    enabled = obs.get("enabled", "unknown")
    skilled = obs.get("skilled", "unknown")
    defined = obs.get("defined", "unknown")

    # ---- Not rated.  Performance is the gate for every level, so if it has
    # never been observed there is nothing to derive from.
    if practised in UNKNOWN:
        known = [n for n, v in (("enabled", enabled), ("skilled", skilled),
                                ("defined", defined)) if v not in UNKNOWN]
        return None, ("Not rated: performance has never been observed"
                      + (" (%s recorded, which cannot place a level on its own)"
                         % ", ".join(known) if known else ""))

    # ---- Level 0.  Nothing performed.
    if practised == "no":
        if _at_least_partial(enabled) or _at_least_partial(defined):
            return 0, ("Not performed, although enablers exist - the platform or the "
                       "standard is ahead of the practice")
        return 0, "Not performed"

    # ---- Level 1.  Performed at all.
    if practised == "n/a":
        return None, "Not rated: marked not applicable, which needs an approver and a rationale"

    # practised is yes or partial from here.
    lvl, why = 1, "Performed"
    if practised == "partial":
        return 1, ("Performed on some AI systems but not repeatably - "
                   "that is Level 1 until it is consistent")

    # ---- Level 2.  Managed: resources provided and people competent
    # (ISO/IEC 33020 PA 2.1 outcomes e and f).
    if not (_ok(enabled) and _has(skilled)):
        missing = []
        if not _ok(enabled):
            missing.append("tooling is not provided" if enabled == "no"
                           else "tooling is incomplete" if enabled == "partial"
                           else "tooling is unknown")
        if not _has(skilled):
            missing.append("competence is not evidenced" if skilled in UNKNOWN
                           else "competence is partial" if skilled == "partial"
                           else "competence is absent")
        return 1, "Performed, but not managed: " + " and ".join(missing)
    lvl, why = 2, "Performed, tooled and staffed by competent people"

    # ---- Level 3.  Established: an approved standard exists AND the work is
    # done against it.
    #
    # Note what this model can and cannot see.  `defined` says a standard
    # exists.  `practised` says the work is done.  Neither says the work
    # FOLLOWS the standard - conformance is a fifth observation nobody has
    # collected.  Level 3 is therefore stated as a reading of two facts sitting
    # together, and the reason line says so, rather than asserting conformance
    # the evidence does not carry.  Adding a `conforms` observation would let
    # this be checked instead of read; until then it must not be overstated.
    if not _has(defined):
        return 2, ("Managed, but no approved standard - "
                   + ("the standard is pre-release" if defined == "partial"
                      else "none is recorded"))
    return 3, ("Consistently performed and an approved standard exists. "
               "Conformance to it is not separately evidenced")


def note():
    """Shown on every view that uses this scale."""
    return ("Level %d is the highest this model can currently derive. Levels 4 and 5 "
            "are defined but need observations nobody collects yet - threshold "
            "monitoring and a closed improvement cycle - so a capability at %d is at "
            "the top of what is measured here, not at the top of the scale. Level 3 "
            "also reads conformance from a standard and a practice co-existing; it is "
            "not separately evidenced."
            % (DERIVABLE_MAX, DERIVABLE_MAX))

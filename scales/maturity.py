# -*- coding: utf-8 -*-
"""Institutional maturity - the same observations, read as how far a practice
has spread rather than what has been established.

A LENS, not the default.  The default scale is scales/capability_level.py.

The five-stage ladder below - initial, emerging, consolidating, integrating,
optimizing - is the conventional maturity vocabulary in the CMM/CMMI line
(SEI, 1991: 'Initial' at 1, 'Optimizing' at 5), and the middle-band words are
the generic ones that recur across published maturity models.  It is used here
because it is the shape a reader arrives holding, not because it was adopted
from any particular model, and nothing in this file reproduces the wording,
structure or level text of a specific one.  See scales/README.md.

What makes this different from the default scale is the QUESTION, not the
rule.  The default asks 'has the institution established this practice?' and
answers per attribute.  This asks 'how far has it spread?' - the same
evidence read as reach rather than as attainment.  The two will place the
same capability differently.  Where they disagree the default scale is the
finding.

What is NOT different is the gate.  Performance is observed before anything is
claimed, exactly as in the default scale: a standard nobody performs against
earns no maturity either.  A maturity ladder is conventionally the forgiving
instrument, and this one deliberately is not, because rating the enablers
while performance is unobserved is how 'we approved the technology' comes to
read as 'we have the capability'.
"""

NAME = "Institutional maturity"
SHORT = "maturity"
QUESTION = "How far has this practice spread beyond the people doing it?"
BASIS = ("Ours. The conventional five-stage maturity ladder (CMM/CMMI line, "
         "SEI 1991) applied to the same four observations as the default "
         "scale. Not adopted from any specific published maturity model.")
CAUTION = (
    "'Initial' at 1 and 'Optimizing' at 5 are CMM/CMMI (SEI, 1991) - public, "
    "citable, and the origin of the whole convention. The middle-band words are "
    "the generic vocabulary that recurs across many published maturity models; "
    "no model owns them. This ladder is NOT adopted from any particular "
    "institution's maturity model and must never be attributed to one: cite the "
    "shape, never a slide. Under ADR-0010 its derivation type is adapted for "
    "the ladder and ours for the rule.")

LEVELS = [
    (1, "Initial",
     "Done where an individual or a team makes it happen. Nothing carries "
     "beyond them."),
    (2, "Emerging",
     "Done in more than one place and supported by tooling and competent "
     "people, but each team still assembles its own way of working."),
    (3, "Consolidating",
     "Done against an approved institutional standard. The practice is the "
     "Bank's, not a team's."),
    (4, "Integrating",
     "Joined up across units and measured against thresholds."),
    (5, "Optimizing",
     "Improved on evidence, with a closed cycle showing a verified benefit."),
]

# Levels 4 and 5 need observations nobody collects: cross-unit integration and
# threshold monitoring, and a closed improvement cycle.  Declaring the ceiling
# keeps a capability at 3 from reading as 'the best there is'.
DERIVABLE_MAX = 3

FULL = {"yes"}
PART = {"partial"}
NA = {"n/a"}
UNKNOWN = {"unknown", ""}


def _has(v):
    return v in FULL


def _ok(v):
    """Achieved, or legitimately not applicable."""
    return v in FULL or v in NA


def level(obs):
    """obs: {'practised': 'yes'|'partial'|'no'|'n/a'|'unknown', ...}.
    Returns (level:int|None, why:str).  None means NOT RATED.
    """
    practised = obs.get("practised", "unknown")
    enabled = obs.get("enabled", "unknown")
    skilled = obs.get("skilled", "unknown")
    defined = obs.get("defined", "unknown")

    # ---- Not rated.  Maturity is a claim about how far a practice has
    # spread, so an unobserved practice has no maturity to report - not a low
    # one.  Same gate as the default scale, deliberately.
    if practised in UNKNOWN:
        known = [n for n, v in (("enabled", enabled), ("skilled", skilled),
                                ("defined", defined)) if v not in UNKNOWN]
        return None, ("Not rated: the practice has never been observed"
                      + (" (%s recorded, which describes the enablers, not the "
                         "practice)" % ", ".join(known) if known else ""))

    if practised == "n/a":
        return None, ("Not rated: marked not applicable, which needs an approver "
                      "and a rationale")

    # ---- Below the ladder.  Nothing is happening, so nothing is maturing.
    if practised == "no":
        if _has(defined) or _has(enabled):
            return None, ("Not rated: nothing is performed, so there is no practice "
                          "to place on this ladder - although the enablers exist, "
                          "which is the finding")
        return None, "Not rated: nothing is performed"

    # ---- Level 1.  It happens somewhere.
    if practised == "partial":
        return 1, ("Done where individuals or teams make it happen, not "
                   "consistently across the Bank")

    # practised == 'yes' from here: every criterion examined and passed.

    # ---- Level 2.  Carried by tooling and competent people rather than by
    # the people who happen to care.
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
        return 1, ("Done consistently, but nothing yet carries it beyond the "
                   "people doing it: " + " and ".join(missing))

    # ---- Level 3.  An approved institutional standard exists alongside the
    # practice.  As in the default scale, conformance is not separately
    # observed and the reason line must not imply that it is.
    if not _has(defined):
        return 2, ("Done consistently, tooled and staffed, but each team still "
                   "works to its own definition - "
                   + ("the standard is pre-release" if defined == "partial"
                      else "no approved standard is recorded"))
    return 3, ("Done consistently against an approved institutional standard. "
               "Conformance to it is not separately evidenced")


def note():
    return ("A LENS, not the assessment. It reads the same observations as the "
            "default scale and asks how far a practice has spread rather than "
            "what has been established, so it will place some capabilities "
            "differently; where the two disagree, the default scale is the "
            "finding. Level %d is the highest it can derive - Integrating and "
            "Optimizing need cross-unit measurement and a closed improvement "
            "cycle, which nobody observes yet. Unlike most maturity ladders "
            "this one does not rate the enablers on their own: a capability "
            "with tooling and an approved standard but no observed practice is "
            "NOT RATED, not Level 1." % DERIVABLE_MAX)

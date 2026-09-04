# -*- coding: utf-8 -*-
"""Views: one Markdown page per scale, plus the agent one-pager.

A view renders one scale over the capability map. Adding a scale to scales/
adds a view here automatically - nothing in this file names a scale.
"""
import os
from datetime import date

BAR = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5"}
MARK = {"yes": "yes", "partial": "part", "no": "no", "n/a": "n-a", "unknown": "?"}


def _levels(scale):
    return dict((n, k) for n, k, _ in scale.LEVELS)


def capability_view(m, scale):
    names = _levels(scale)
    o = []
    w = o.append
    w("# Capability assessment — %s" % scale.NAME)
    w("")
    w("**IDB Enterprise Architecture** · generated %s · scale `%s`"
      % (date.today().isoformat(), scale.SHORT))
    w("")
    w("> %s" % scale.BASIS)
    if hasattr(scale, "note"):
        w(">")
        w("> %s" % scale.note())
    w("")

    rated = {c['id']: m.rate(scale, c['id']) for c in m.capabilities}
    n_rated = sum(1 for v in rated.values() if v[0] is not None)
    w("| | |")
    w("|---|---|")
    w("| Capabilities | %d |" % len(m.capabilities))
    w("| Rated | %d |" % n_rated)
    w("| Not rated | %d |" % (len(m.capabilities) - n_rated))
    w("| Offerings | %d |" % len(m.offerings))
    w("| Assets | %d |" % len(m.assets))
    w("")
    if n_rated == 0:
        w("> **Nothing is rated yet.** Every capability is missing the observation this "
          "scale needs most. That is a true statement about the assessment, not a "
          "failure of the model: the facts that exist are recorded, and the ones that "
          "do not are visibly absent. Fill in sheet 2 of the workbook to change it.")
        w("")
    w("---")
    w("")

    # ---- levels
    w("## The scale")
    w("")
    w("| Level | Name | Meaning |")
    w("|---|---|---|")
    for n, k, d in scale.LEVELS:
        w("| **%d** | %s | %s |" % (n, k, d))
    w("")

    # ---- observations
    w("## The four observations")
    w("")
    w("| Observation | The question | Evidence expected |")
    w("|---|---|---|")
    for t in m.observation_types:
        w("| **%s** | %s | %s |" % (t['id'].title(), t['question'],
                                    t['evidence_expected']))
    w("")
    w("Values: `yes` · `partial` · `no` · `n/a` (with a reason) · "
      "`unknown` (nobody has looked — never a zero).")
    w("")
    w("---")
    w("")

    # ---- by domain
    w("## By domain")
    w("")
    for d in m.domains:
        caps = [c for c in m.capabilities if c['domain'] == d['id']]
        w("### %s · %s" % (d['id'], d['name']))
        w("")
        w("*%s*" % d['definition'])
        w("")
        w("| ID | Capability | Owner | Pra | Ena | Ski | Def | Level | Why |")
        w("|---|---|---|:-:|:-:|:-:|:-:|:-:|---|")
        for c in sorted(caps, key=lambda x: m.sort_key(x['id'])):
            v = m.values(c['id'])
            lvl, why = rated[c['id']]
            unit = m.owner(c['id'])[0] or "**none**"
            lab = ("**%d** %s" % (lvl, names[lvl])) if lvl is not None else "*not rated*"
            w("| `%s` | %s | %s | %s | %s | %s | %s | %s | %s |"
              % (c['id'], c['name'], unit, MARK[v['practised']], MARK[v['enabled']],
                 MARK[v['skilled']], MARK[v['defined']], lab, why))
        w("")
    w("---")
    w("")

    # ---- what the bank has
    w("## What the Bank has built")
    w("")
    w("| Offering | What a team gets | Assets released | Enables |")
    w("|---|---|:-:|---|")
    for off in m.offerings:
        w("| **%s** | %s | %d of %d | %s |"
          % (off['name'], off['consumption'] or "-",
             off['assets_released'], off['assets_total'],
             ", ".join("`%s`" % x for x in off['enables'])))
    w("")
    return "\n".join(o) + "\n"


def agent_view(m):
    """The one-pager that answers 'we cannot run AI agents'."""
    AGENT_CAPS = ["4.4", "5.1", "5.5", "7.7", "2.5", "4.5", "7.4", "8.3"]
    o = []
    w = o.append
    w("# Can the Bank run AI agents?")
    w("")
    w("**IDB Enterprise Architecture** · generated %s" % date.today().isoformat())
    w("")
    w("Short answer: **the Bank can provision and build agents to a published standard "
      "today. What it cannot yet do is operate them as an institution.** Both halves of "
      "that sentence are evidenced below.")
    w("")
    w("---")
    w("")
    w("## What exists, with the evidence")
    w("")
    w("| Layer | What exists | Assets released | The whole distance to the next step |")
    w("|---|---|:-:|---|")
    NEXT = {
        "OFF-01": "Nothing. A per-use-case runtime is correctly packaged here.",
        "OFF-02": "Release two documents: the Foundry Agents Standard and its reference architecture.",
        "OFF-03": "Distribute template v2 and migrate v1 servers inside the July 2026 spec window.",
        "OFF-07": "Nothing pending.",
    }
    for off in m.offerings:
        if off['id'] not in ("OFF-01", "OFF-02", "OFF-03", "OFF-07"):
            continue
        w("| **%s** | %s | %d of %d | %s |"
          % (off['name'], ", ".join(off['assets']),
             off['assets_released'], off['assets_total'],
             NEXT.get(off['id'], "")))
    w("")

    # in the box
    box = [(o_, x) for o_ in m.offerings for x in o_['in_the_box']
           if o_['id'] == "OFF-02"]
    if box:
        answered = sum(1 for _, x in box if x['status'])
        w("## What comes in the box")
        w("")
        w("The twelve questions that decide whether an agent inherits its controls or "
          "every team rebuilds them. **%d of %d answered.**" % (answered, len(box)))
        w("")
        w("| Control | Status | Capability | Why it matters |")
        w("|---|:-:|:-:|---|")
        for _, x in box:
            w("| %s | %s | `%s` | %s |"
              % (x['control'], x['status'] or "**unanswered**", x['capability'], x['why']))
        w("")
        nb = [o_['not_provided'] for o_ in m.offerings if o_['id'] == "OFF-02"]
        if nb and nb[0]:
            w("**What the platform never provides:** %s" % nb[0])
            w("")
    w("---")
    w("")
    w("## The capabilities this actually touches")
    w("")
    w('"Can we build agents?" is not one question. It is these, with these owners.')
    w("")
    w("| ID | Capability | Owner | Practised | Enabled | Skilled | Defined |")
    w("|---|---|---|:-:|:-:|:-:|:-:|")
    for cid in AGENT_CAPS:
        c = m.by_id.get(cid)
        if not c:
            continue
        v = m.values(cid)
        w("| `%s` | %s | %s | %s | %s | %s | %s |"
          % (cid, c['name'], m.owner(cid)[0] or "**none**", MARK[v['practised']],
             MARK[v['enabled']], MARK[v['skilled']], MARK[v['defined']]))
    w("")
    w("---")
    w("")
    w("## What this means")
    w("")
    w("The enablers were built before the practice. In the terms of the scale this model "
      "uses, the Bank has assembled its **Level 2 and Level 3 enablers** — the tooling "
      "and the standards — while **Level 1, the practice itself, has never been "
      "observed**. That is precisely the complaint, stated in a way that names the fix.")
    w("")
    w("| Who | What they do next |")
    w("|---|---|")
    w("| Platform team | Answer the twelve in-the-box questions. Release the two "
      "pre-release documents. Distribute template v2. |")
    w("| Product teams | Build against the standard, so there is practice to observe. |")
    w("| EA | Observe it. Record `practised` with named systems. |")
    w("| People | 8.3 literacy and 8.2 skills: no observation exists yet. |")
    w("")
    return "\n".join(o) + "\n"

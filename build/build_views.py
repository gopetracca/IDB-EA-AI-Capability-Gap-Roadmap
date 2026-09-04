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
    w("**Inter-American Development Bank** · generated %s · scale `%s`"
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
    cap = getattr(scale, "DERIVABLE_MAX", None)
    w("| Level | Name | Meaning | Derivable today |")
    w("|---|---|---|:-:|")
    for n, k, d in scale.LEVELS:
        ok = "—" if cap is not None and n > cap else "yes"
        w("| **%d** | %s | %s | %s |" % (n, k, d, ok))
    w("")
    if cap is not None:
        w("Levels above **%d** are defined but cannot be reached from the observations "
          "this model collects. A capability at %d is at the top of what is *measured* "
          "here, not at the top of what is *possible*." % (cap, cap))
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
    w("**Inter-American Development Bank** · generated %s" % date.today().isoformat())
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
    w("| Capability owners | Confirm what is actually practised, with named systems. |")
    w("| Cybersecurity, Data Mgmt, Legal | Confirm whether a standard exists in their own domain. |")
    w("| People | 8.3 literacy and 8.2 skills: no observation exists yet. |")
    w("")
    return "\n".join(o) + "\n"


def management_report(m, scale):
    """The management report: what we can say today, and what we cannot.

    Deliberately leads with what is evidenced, states the coverage of the
    assessment honestly, and never presents an unobserved capability as a zero.
    """
    RELEASED = {"Published", "Published (JFrog)", "In use"}
    o = []
    w = o.append
    total = len(m.capabilities)
    rated = {c['id']: m.rate(scale, c['id']) for c in m.capabilities}
    n_rated = sum(1 for v in rated.values() if v[0] is not None)
    pending = [a for a in m.assets if a['status'] not in RELEASED]
    noowner = [c for c in m.capabilities if m.owner(c['id'])[1] == 'NO MATCH']
    box_total = sum(len(x['in_the_box']) for x in m.offerings)
    box_done = sum(1 for x in m.offerings for y in x['in_the_box'] if y['status'])

    w("# AI capability — management report")
    w("")
    w("**Inter-American Development Bank** · %s" % date.today().isoformat())
    w("")
    w("---")
    w("")
    w("## 1 · What this report can and cannot say")
    w("")
    w("Read this section before the findings. It states the coverage of the assessment "
      "so that nothing below is read as more than it is.")
    w("")
    w("| | |")
    w("|---|---|")
    w("| Capabilities in the map | %d |" % total)
    w("| **Rated** | **%d** |" % n_rated)
    w("| Not yet rated | %d |" % (total - n_rated))
    w("| Platform offerings with evidence | %d |" % len(m.offerings))
    w("| Assets recorded, with status and location | %d |" % len(m.assets))
    w("")
    if n_rated == 0:
        w("> **No capability is rated yet, and that is a factual statement rather than a "
          "bad result.** A rating requires knowing whether something is actually "
          "*practised* on real AI systems. That question has not yet been put to the "
          "capability owners. What has been established is what the institution has "
          "*built* — and that is substantial, evidenced, and set out in section 2.")
        w("")
        w("This is the difference between *we do not know* and *we do not have it*. Most "
          "maturity assessments cannot tell those apart, and score an unexamined "
          "capability as if it were absent. This one refuses to.")
    else:
        w("> %d of %d capabilities carry a rating. The remainder are not zero — they are "
          "unobserved, and are shown as such throughout." % (n_rated, total))
    w("")
    w("---")
    w("")

    # ---------------------------------------------- 2. what exists
    w("## 2 · What the institution has built")
    w("")
    w("Every row below is backed by a named asset with a location and a status. This is "
      "the part of the picture that is **not** an opinion.")
    w("")
    w("| Offering | What a delivery team gets | Assets released | Capabilities it enables |")
    w("|---|---|:-:|---|")
    for off in m.offerings:
        flag = "" if off['assets_released'] == off['assets_total'] else " ⚠"
        w("| **%s** | %s | %d of %d%s | %s |"
          % (off['name'], off['consumption'] or "—",
             off['assets_released'], off['assets_total'], flag,
             ", ".join("`%s`" % x for x in off['enables'])))
    w("")
    ready = [x for x in m.offerings if x['assets_released'] == x['assets_total']]
    w("**%d of %d offerings are complete.** The other %d are each waiting on named "
      "documents or modules, listed in section 4."
      % (len(ready), len(m.offerings), len(m.offerings) - len(ready)))
    w("")

    # ---------------------------------------------- 3. the finding
    w("---")
    w("")
    w("## 3 · The finding")
    w("")
    w("> **The institution has built its enablers ahead of its practice.**")
    w("")
    w("The scale used here places *performance* at Level 1, *tooling and competent "
      "people* at Level 2, and *an approved standard, applied* at Level 3. Measured "
      "that way, the institution has assembled a large part of its Level 2 and Level 3 "
      "apparatus — platforms, standards, reference architectures, infrastructure "
      "modules — while Level 1, whether the work is actually done, has never been "
      "examined.")
    w("")
    w("That is not a criticism of the build. It is the explanation for a disagreement "
      "that recurs in this institution: one person says the capability exists, meaning "
      "the platform and the standard exist, and another says it does not, meaning "
      "nothing is running on it. **Both are right about different things**, and a model "
      "carrying a single number cannot show that. This one shows it as four columns.")
    w("")
    w("| What we can evidence today | What we cannot |")
    w("|---|---|")
    w("| %d offerings, %d assets, with locations | Whether any of it is used in production |"
      % (len(m.offerings), len(m.assets)))
    w("| Which capabilities have approved standards | Whether work is done against them |")
    w("| Which capabilities have no tooling and no reason recorded | Whether the people who need the skills have them |")
    w("")

    # ---------------------------------------------- 4. decisions
    w("---")
    w("")
    w("## 4 · What needs a decision")
    w("")
    w("### 4.1 · Capabilities nobody owns")
    w("")
    w("%d of %d capabilities are claimed by no product or enabler in the institution's "
      "own catalogue. This is a finding about the operating model, not a gap in the "
      "model. Several are governance capabilities that an institution of this kind is "
      "normally expected to hold." % (len(noowner), total))
    w("")
    w("| ID | Capability | Domain |")
    w("|---|---|---|")
    for c in sorted(noowner, key=lambda x: m.sort_key(x['id'])):
        w("| `%s` | **%s** | %s |" % (c['id'], c['name'],
                                      m.domain_by_id[c['domain']]['name']))
    w("")
    w("**Decision required:** assign an owner to each, or record a deliberate decision "
      "not to hold it.")
    w("")

    w("### 4.2 · Work that is finished but not released")
    w("")
    w("%d assets exist and are not yet available to delivery teams. Each is days of "
      "work from being usable, and each currently holds a capability below the level "
      "the underlying work would support." % len(pending))
    w("")
    w("| Asset | What it is | Status |")
    w("|---|---|---|")
    for a in pending:
        w("| `%s` | %s | **%s** |" % (a['id'], a['name'], a['status']))
    w("")
    w("**Decision required:** a release date for each, with a named owner.")
    w("")

    w("### 4.3 · Questions only the platform teams can answer")
    w("")
    w("**%d of %d answered.** These decide whether a delivery team inherits its controls "
      "or rebuilds them. Every unanswered row is both an unknown and, once answered "
      "with a *no*, a roadmap item — usually a cheap one, because it means extending a "
      "module rather than building a platform." % (box_done, box_total))
    w("")
    w("| Offering | Questions outstanding |")
    w("|---|:-:|")
    for off in m.offerings:
        if off['in_the_box']:
            miss = sum(1 for x in off['in_the_box'] if not x['status'])
            w("| %s | %d of %d |" % (off['name'], miss, len(off['in_the_box'])))
    w("")

    # ---------------------------------------------- 5. next
    w("---")
    w("")
    w("## 5 · What would make the next report say more")
    w("")
    w("| Who | What is being asked of them | What it unlocks |")
    w("|---|---|---|")
    w("| Capability owners | For each capability they own: is this done on real AI "
      "systems, and where? | Every rating in the model. Nothing can be rated without it |")
    w("| Platform teams | The %d in-the-box questions | Whether controls are inherited "
      "or rebuilt per team |" % (box_total - box_done))
    w("| Cybersecurity · Data Management · Legal · HR | Does an approved standard exist "
      "in your domain? | %d capabilities currently show *unknown* because the asset "
      "register covers platform assets only |"
      % sum(1 for c in m.capabilities if m.values(c['id'])['defined'] == 'unknown'))
    w("| Learning & Development | Who is trained, and in what? | Level 2 for every "
      "capability where practice exists |")
    w("")
    w("None of this requires new tooling or new investment. It requires four questions "
      "put to the people who already know the answers.")
    w("")
    w("---")
    w("")
    w("*Generated from the capability model. Scale: %s. %s*" % (scale.NAME, scale.BASIS))
    return "\n".join(o) + "\n"

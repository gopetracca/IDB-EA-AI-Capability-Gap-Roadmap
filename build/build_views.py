# -*- coding: utf-8 -*-
"""Views in Markdown: one capability page per scale, one page per use-case
question, the management report as text, and the provenance view.

A view renders facts, optionally through one scale, and never stores anything.
Nothing in this file names a scale, a capability, an offering or a question:
the scales are discovered from scales/, and the questions come from
facts/questions.json, so adding to either adds a view without touching code.
"""
from datetime import date

MARK = {"yes": "yes", "partial": "part", "no": "no", "n/a": "n-a", "unknown": "?"}


def _levels(scale):
    return dict((n, k) for n, k, _ in scale.LEVELS)


def _stamp(m):
    return "**Inter-American Development Bank** · generated %s" % date.today().isoformat()


# ================================================================ capabilities
def capability_view(m, scale):
    names = _levels(scale)
    o = []
    w = o.append
    w("# Capability assessment — %s" % scale.NAME)
    w("")
    w("%s · scale `%s`%s" % (_stamp(m), scale.SHORT,
                              " · **the default scale**" if getattr(scale, "DEFAULT", False)
                              else " · **a lens, not the assessment**"))
    w("")
    if getattr(scale, "QUESTION", None):
        w("> **The question this scale asks:** %s" % scale.QUESTION)
        w(">")
    w("> %s" % scale.BASIS)
    if hasattr(scale, "note"):
        w(">")
        w("> %s" % scale.note())
    w("")

    rated = {c['id']: m.rate(scale, c['id']) for c in m.capabilities}
    n_rated = sum(1 for v in rated.values() if v[0] is not None)
    n_crit = sum(len(c['criteria']) for c in m.capabilities)
    w("The taxonomy has three levels: **%d domains (L1)**, a reporting cluster that is "
      "never scored; **%d capabilities (L2)** — the unit that carries a level and an "
      "accountable owner; and **%d criteria (L3)** — the specific practices that can "
      "actually be witnessed. *Practised* is observed once per criterion and the "
      "capability value is **derived** from those observations, never typed: it reads "
      "`yes` only when every criterion was examined and every one passed (ADR-0014). "
      "Criteria carry no level of their own. They are listed per capability in section "
      "*By domain* below, and each has a row on sheet 2 of the workbook."
      % (len(m.domains), len(m.capabilities), n_crit))
    w("")
    w("| | |")
    w("|---|---|")
    w("| Domains (L1) | %d |" % len(m.domains))
    w("| Capabilities (L2) | %d |" % len(m.capabilities))
    w("| Criteria (L3) | %d |" % n_crit)
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
    w("| Observation | The question | Asked at | Evidence expected |")
    w("|---|---|---|---|")
    for t in m.observation_types:
        w("| **%s** | %s | %s | %s |"
          % (t['id'].title(), t['question'],
             "each L3 criterion" if t['id'] in m.criterion_types else "the capability",
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
        # the L3 criteria behind each capability in this domain, with what has
        # been observed against each
        for c in sorted(caps, key=lambda x: m.sort_key(x['id'])):
            if not c['criteria']:
                continue
            rows = m.criteria_obs(c['id'], m.criterion_types[0]) if m.criterion_types else \
                [(x, {}) for x in c['criteria']]
            seen = sum(1 for _, r in rows if r.get('value', 'unknown') != 'unknown')
            w("<details><summary><code>%s</code> %s — %d L3 criteria, %d observed</summary>"
              % (c['id'], c['name'], len(c['criteria']), seen))
            w("")
            w("| L3 | Criterion | What it means | Practised | Evidence |")
            w("|---|---|---|:-:|---|")
            for x, r in rows:
                w("| `%s` | **%s** | %s | %s | %s |"
                  % (x['id'], x['name'], x['definition'],
                     MARK[r.get('value', 'unknown')], r.get('evidence', '') or ""))
            w("")
            w("</details>")
            w("")
    w("---")
    w("")

    # ---- what the bank has
    w("## What the Bank has built")
    w("")
    w("| Offering | What a team gets | Assets released | Enables |")
    w("|---|---|:-:|---|")
    for off in m.offerings:
        rel, tot = m.release_count(off)
        w("| **%s** | %s | %d of %d | %s |"
          % (off['name'], off['consumption'] or "-", rel, tot,
             ", ".join("`%s`" % x for x in off['enables'])))
    w("")
    return "\n".join(o) + "\n"


# ================================================================== questions
def question_view(m, q):
    """One page answering a use-case question of the form 'can we do X?'.

    X is not a capability. It touches several, with different owners, so the
    answer is a table: what exists (with evidence), what comes in the box, the
    capabilities touched with their four observations, and what moves next.
    Everything except the attributed finding is derived from facts/.
    """
    o = []
    w = o.append
    w("# %s" % q['title'])
    w("")
    w(_stamp(m))
    w("")
    if q.get('claim'):
        w("The claim being answered: *\"%s\"*" % q['claim'])
        w("")
    if q.get('finding'):
        w("Short answer: **%s**" % q['finding'])
        w("")
        w("*Finding recorded by %s on %s. Everything below it is derived from the "
          "recorded facts and regenerates as they change.*"
          % (q.get('finding_by', 'unattributed'), q.get('finding_on', 'undated')))
        w("")
    w("---")
    w("")

    offs = [m.offering_by_id[x] for x in q.get('offerings', []) if x in m.offering_by_id]
    if offs:
        w("## What exists, with the evidence")
        w("")
        w("| Offering | What exists | Assets released | The whole distance to complete |")
        w("|---|---|:-:|---|")
        for off in offs:
            rel, tot = m.release_count(off)
            pend = m.pending_assets(off)
            nxt = ("Nothing pending." if not pend else
                   "Release " + "; ".join("%s %s (%s)" % (a['id'], a['name'], a['status'])
                                          for a in pend) + ".")
            w("| **%s** | %s | %d of %d | %s |"
              % (off['name'], ", ".join(off['assets']), rel, tot, nxt))
        w("")

        box = [(off, x) for off in offs for x in off['in_the_box']]
        if box:
            answered = sum(1 for _, x in box if x['status'])
            w("## What comes in the box")
            w("")
            w("The %d questions that decide whether a team inherits its controls or "
              "rebuilds them. **%d of %d answered.**" % (len(box), answered, len(box)))
            w("")
            w("| Offering | Control | Status | Capability | Why it matters |")
            w("|---|---|:-:|:-:|---|")
            for off, x in box:
                w("| %s | %s | %s | `%s` | %s |"
                  % (off['name'], x['control'], x['status'] or "**unanswered**",
                     x['capability'], x['why']))
            w("")
        for off in offs:
            if off.get('not_provided'):
                w("**What %s never provides:** %s" % (off['name'], off['not_provided']))
                w("")
        w("---")
        w("")

    caps = [m.by_id[c] for c in q.get('capabilities', []) if c in m.by_id]
    if caps:
        w("## The capabilities this actually touches")
        w("")
        w('"%s" is not one question. It is these, with these owners.'
          % q['title'].rstrip('?'))
        w("")
        w("| ID | Capability | Owner | Practised | Enabled | Skilled | Defined |")
        w("|---|---|---|:-:|:-:|:-:|:-:|")
        for c in caps:
            v = m.values(c['id'])
            w("| `%s` | %s | %s | %s | %s | %s | %s |"
              % (c['id'], c['name'], m.owner(c['id'])[0] or "**none**",
                 MARK[v['practised']], MARK[v['enabled']], MARK[v['skilled']],
                 MARK[v['defined']]))
        w("")
        # capabilities reached through the in-the-box controls but not listed
        touched = set()
        for off in offs:
            for x in off['in_the_box']:
                touched.add(m.criterion_parent.get(x['capability'], x['capability']))
        extra = sorted(touched - {c['id'] for c in caps}, key=m.sort_key)
        if extra:
            w("The in-the-box controls above also reach %d further capabilities: %s."
              % (len(extra), ", ".join("`%s`" % x for x in extra)))
            w("")
        w("---")
        w("")

    if q.get('next'):
        w("## What this means")
        w("")
        w("| Who | What they do next |")
        w("|---|---|")
        for step in q['next']:
            w("| %s | %s |" % (step['who'], step['what']))
        w("")
    return "\n".join(o) + "\n"


# ========================================================== management report
def management_report(m, scale):
    """The management report as plain text: what we can say today, and what we
    cannot. Deliberately leads with what is evidenced, states the coverage of
    the assessment honestly, and never presents an unobserved capability as a
    zero."""
    o = []
    w = o.append
    total = len(m.capabilities)
    rated = {c['id']: m.rate(scale, c['id']) for c in m.capabilities}
    n_rated = sum(1 for v in rated.values() if v[0] is not None)
    pending = m.pending_assets()
    noowner = [c for c in m.capabilities if m.owner(c['id'])[1] == 'NO MATCH']
    box_total = sum(len(x['in_the_box']) for x in m.offerings)
    box_done = sum(1 for x in m.offerings for y in x['in_the_box'] if y['status'])
    vals = {c['id']: m.values(c['id']) for c in m.capabilities}

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
        rel, tot = m.release_count(off)
        flag = "" if rel == tot else " ⚠"
        w("| **%s** | %s | %d of %d%s | %s |"
          % (off['name'], off['consumption'] or "—", rel, tot, flag,
             ", ".join("`%s`" % x for x in off['enables'])))
    w("")
    ready = [x for x in m.offerings if m.offering_complete(x)]
    w("**%d of %d offerings are complete.** %s"
      % (len(ready), len(m.offerings),
         "The other %d are each waiting on named documents or modules, listed in "
         "section 4." % (len(m.offerings) - len(ready))
         if len(ready) < len(m.offerings) else "Nothing is pending."))
    w("")

    # ---------------------------------------------- 3. the finding
    w("---")
    w("")
    w("## 3 · The finding")
    w("")
    w("> **The institution has built its enablers ahead of its practice.**")
    w("")
    w("The scale used here — *%s* — places *performance* at Level 1, *tooling and "
      "competent people* at Level 2, and *an approved standard, applied* at Level 3. "
      "Measured that way, the institution has assembled a large part of its Level 2 "
      "and Level 3 apparatus — platforms, standards, reference architectures, "
      "infrastructure modules — while Level 1, whether the work is actually done, %s."
      % (scale.NAME, "has never been examined" if n_rated == 0 else
         "has been examined for %d of %d capabilities" % (n_rated, total)))
    w("")
    w("That is not a criticism of the build. It is the explanation for a disagreement "
      "that recurs in this institution: one person says the capability exists, meaning "
      "the platform and the standard exist, and another says it does not, meaning "
      "nothing is running on it. **Both are right about different things**, and a model "
      "carrying a single number cannot show that. This one shows it as four columns.")
    w("")
    import collections
    en = collections.Counter(v['enabled'] for v in vals.values())
    de = collections.Counter(v['defined'] for v in vals.values())
    sk = collections.Counter(v['skilled'] for v in vals.values())
    w("| What we can evidence today | What we cannot |")
    w("|---|---|")
    w("| %d offerings, %d assets, with locations | Whether any of it is used in production |"
      % (len(m.offerings), len(m.assets)))
    w("| Which capabilities have platform tooling (%d), partial tooling (%d), or none "
      "needed (%d) | Whether tooling exists for the %d nobody has yet examined |"
      % (en['yes'], en['partial'], en['n/a'], en['unknown']))
    w("| Which capabilities have an approved standard (%d) or one in pre-release (%d) | "
      "Whether work is done against them |" % (de['yes'], de['partial']))
    w("| Where a standard exists in the platform register | Whether the people who need "
      "the skills have them: %d of %d unobserved |" % (sk['unknown'], total))
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
    w("| Capability owners | For each L3 criterion under a capability they own: is this "
      "done on real AI systems, and where? | Every rating in the model. Nothing can be "
      "rated without it |")
    w("| Platform teams | The %d in-the-box questions | Whether controls are inherited "
      "or rebuilt per team |" % (box_total - box_done))
    w("| Cybersecurity · Data Management · Legal · HR | Does an approved standard exist "
      "in your domain? | %d capabilities currently show *unknown* because the asset "
      "register covers platform assets only |" % de['unknown'])
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


# ================================================================= provenance
def provenance_view(m):
    """Where the model's claims come from, and whether a reviewer can open the
    source.  Operationalises ADR-0010: grade exposure per capability, what
    rests on a grade-D source and therefore cannot leave the Bank, and how
    many citations point into a specific part of a source."""
    import collections
    o = []
    w = o.append
    w("# Provenance — where the capability map comes from")
    w("")
    w("%s · register `facts/sources.json`, access date %s"
      % (_stamp(m), m.sources_doc.get('access_date', 'unrecorded')))
    w("")
    w("> **The rule (ADR-0010):** provenance is graded by whether a reviewer can open it, "
      "not by prestige. **A grade-D source cannot support a claim in anything that "
      "leaves the Bank**, whatever its quality.")
    w("")
    grades = m.source_grades
    w("| Grade | Meaning | Sources |")
    w("|---|---|:-:|")
    cnt = collections.Counter(s['grade'] for s in m.sources)
    for g in sorted(grades):
        w("| **%s** | %s | %d |" % (g, grades[g], cnt.get(g, 0)))
    w("")
    pairs = [(c, cit, src, loc) for c in m.capabilities
             for cit, src, loc in m.capability_sources(c['id'])]
    resolved = [p for p in pairs if p[2]]
    with_locus = [p for p in resolved if p[3]]
    w("| | |")
    w("|---|---|")
    w("| Sources in the register | %d |" % len(m.sources))
    w("| Capability–source citations | %d |" % len(pairs))
    w("| Citations resolving to a registered source | %d |" % len(resolved))
    w("| Citations pinned to a locus (clause, section, control) | %d |" % len(with_locus))
    w("")
    w("A citation without a locus says *this source informed the capability*; it does "
      "not say where. Under ADR-0010 a capability whose loci are never pinned is "
      "reclassified as **synthesized** — assembled by us — rather than left claiming a "
      "source it cannot point into.")
    w("")
    w("---")
    w("")

    # ---- grade-D exposure
    d_caps = collections.OrderedDict()
    for c, cit, src, loc in resolved:
        if src['grade'] == 'D':
            d_caps.setdefault(c['id'], []).append((cit, src))
    w("## Capabilities resting partly on a grade-D source")
    w("")
    w("These %d capabilities cite at least one source a reviewer outside the Bank cannot "
      "open. Each still has other sources; the grade-D citation must be replaced or the "
      "claim restated as ours before anything containing it circulates externally."
      % len(d_caps))
    w("")
    w("| ID | Capability | Grade-D citation | Register entry | What would close it |")
    w("|---|---|---|---|---|")
    for cid, lst in sorted(d_caps.items(), key=lambda kv: m.sort_key(kv[0])):
        for cit, src in lst:
            w("| `%s` | %s | %s | %s `%s` | %s |"
              % (cid, m.by_id[cid]['name'], cit, src['short'], src['id'],
                 (src.get('caution') or src.get('status') or '').split('. ')[0]))
    w("")
    w("---")
    w("")

    # ---- the register
    w("## The register")
    w("")
    w("| ID | Grade | Source | Publisher | Edition · date | Status | Cited by |")
    w("|---|:-:|---|---|---|---|:-:|")
    used = collections.Counter(src['id'] for _, _, src, _ in resolved)
    for s in m.sources:
        w("| `%s` | **%s** | [%s](%s) | %s | %s · %s | %s | %d |"
          % (s['id'], s['grade'], s['short'], s.get('url') or '', s.get('publisher', ''),
             s.get('edition', ''), s.get('date', ''), s.get('status', ''), used.get(s['id'], 0)))
    w("")
    unused = [s for s in m.sources if not used.get(s['id'])]
    if unused:
        w("%d sources are in the register but cited by no capability: %s."
          % (len(unused), ", ".join("`%s`" % s['id'] for s in unused)))
        w("")
    w("---")
    w("")

    # ---- per capability
    w("## Sources by capability")
    w("")
    w("A locus in *italics* after a source is the clause, section or control the citation "
      "points into. A source with no locus informed the capability without saying where.")
    w("")
    w("| ID | Capability | Sources (grade) *· locus* | Loci pinned |")
    w("|---|---|---|:-:|")
    for c in m.capabilities_sorted():
        srcs = m.capability_sources(c['id'])
        parts = []
        for cit, src, loc in srcs:
            if not src:
                parts.append("%s (**unresolved**)" % cit)
            elif loc:
                parts.append("%s (%s) *· %s*" % (src['short'], src['grade'], loc))
            else:
                parts.append("%s (%s)" % (src['short'], src['grade']))
        w("| `%s` | %s | %s | %d of %d |"
          % (c['id'], c['name'], "; ".join(parts), sum(1 for _, s_, l in srcs if l), len(srcs)))
    w("")

    # ---- obligations
    if m.obligations:
        w("---")
        w("")
        w("## Statutory references (candidate, Legal-owned — ADR-0008)")
        w("")
        w("%d references, all marked candidate until Legal determines applicability. "
          "`7.6.6 Regulatory Role Determination` is the prerequisite." % len(m.obligations))
        w("")
        w("| Capability | Instrument | Subject | Status |")
        w("|---|---|---|---|")
        for ob in m.obligations:
            w("| `%s` %s | %s | %s | %s |"
              % (ob['capability'], ob.get('capability_name', ''), ob['instrument'],
                 ob['subject'], ob['status']))
        w("")
    return "\n".join(o) + "\n"

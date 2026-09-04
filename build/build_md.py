import json, re, io
from datetime import date
M = json.load(open('model3.json'))
L2 = [(d, c) for d in M for c in d[3]]
NL2, NL3 = len(L2), sum(len(c[4]) for _, c in L2)
AG = [c for _, c in L2 if (len(c) > 5 and c[5]) or any(len(x) > 3 and x[3] for x in c[4])]
ag2 = lambda c: (len(c) > 5 and c[5]) or any(len(x) > 3 and x[3] for x in c[4])
ag3 = lambda x: len(x) > 3 and x[3]
o = []
w = o.append

w("# Enterprise AI Capability Model")
w("")
w("**Reference model v0.1** · vendor-neutral composite · generated %s" % date.today().isoformat())
w("")
w("One capability tree covering what the institution must be able to do with AI, decomposed to a "
  "level where maturity can be scored against evidence. Lifecycle, risk controls, platform "
  "realization and agentic scope attach as overlays, never as branches of the tree.")
w("")
w("| | |")
w("|---|---|")
w("| L1 domains | 8 |")
w("| L2 capabilities (the scored unit) | %d |" % NL2)
w("| L3 assessment units | %d |" % NL3)
w("| L2 capabilities carrying agentic scope | %d |" % len(AG))
w("")
w("---")
w("")

w("## 1. How to read this")
w("")
w("| Level | What it is | What you do with it |")
w("|---|---|---|")
w("| **L1** | Domain. Covers the space; there are eight and they are mutually exclusive. | Never scored. Averaging a domain hides the one capability that is failing. |")
w("| **L2** | A capability coherent enough to have one accountable owner. | **This is the scored unit.** Current and target maturity, 1–5. |")
w("| **L3** | The assessment unit — where evidence actually exists. | Defines the scope of its L2 and tells you what evidence to gather. Score at L3 only in domains on the critical path. |")
w("")
w("The **⬥** marker denotes agentic-AI scope. It is a tag across the tree, not a domain — a "
  "separate agentic branch would break mutual exclusivity and date the model within eighteen months.")
w("")

w("## 2. The meta-model")
w("")
w("### Why one tree and not eight")
w("")
w("Every published AI framework is a *different dimension*, not a competing map. AWS CAF-AI is an "
  "organizational perspective. IBM's model is platform realization. ISO/IEC 5338 is lifecycle. "
  "NIST AI RMF is risk. MITRE is a scoring scale. Merging them into one hierarchy produces a tree "
  "that mixes abilities, phases, assets and products — which is why most enterprise AI capability "
  "maps fail their first architecture review.")
w("")
w("This model keeps a single capability spine. Everything else is an overlay joined by a "
  "cross-mapping matrix:")
w("")
w("| Overlay | Source | How it attaches |")
w("|---|---|---|")
w("| Lifecycle | ISO/IEC 5338 | A value stream cross-mapped to capabilities |")
w("| Risk & controls | ISO/IEC 42001, NIST AI RMF | Requirements mapped onto capabilities |")
w("| Maturity | MITRE-style 1–5 scale | An attribute on the capability node |")
w("| Realization | Platform and product catalogs | Matrix A and Matrix B, below |")
w("| Agentic scope | IMDA, SAP, Salesforce | A tag (⬥) across the tree |")
w("| Organization | Operating model | Owner attribute on the capability node |")
w("")
w("### Capability, pattern, product")
w("")
w("The commonest modelling error is wiring a capability straight to a product. Three tiers, and "
  "the middle one is the one that gets skipped:")
w("")
w("| Tier | What it is | Clock | Example |")
w("|---|---|---|---|")
w("| **Capability** | What the organization is able to do. Survives replacing every vendor. | 5–10 years | `3.6` Knowledge Access & Retrieval |")
w("| **ABB** | Architecture Building Block — one of several competing logical patterns. Vendor-neutral. | 2–5 years | Vector Index & Similarity Search · Lexical + Rerank · Graph Traversal · Hybrid |")
w("| **SBB** | Solution Building Block — the product you run. Has a SKU, a version, a contract. | quarterly | Azure AI Search · pgvector · Cosmos DB vector |")
w("")
w("The relationship is many-to-many in **both** directions: one capability realized by several "
  "patterns; one pattern by several products; and one product realizing several capabilities. "
  "A two-tier model cannot express the third case without duplicating the product under four "
  "capabilities — and it is exactly that case (three products realizing one pattern) that surfaces "
  "a rationalization finding no maturity questionnaire would ever produce.")
w("")
w("Only the **capability** tier appears in this document. Matrix A (capability × ABB) and "
  "Matrix B (ABB × SBB) are deliberately separate artifacts, because they change on different "
  "clocks. Keeping them in one document is what causes a roadmap to be invalidated by a licensing "
  "decision.")
w("")
w("### Design rules")
w("")
w("1. **The ability test.** *“The organization is able to ___”* must read naturally, and the node "
  "must be scorable 1–5 with evidence and an accountable owner. *“We have Databricks”* fails. "
  "*“MLOps”* fails as an ambiguous blob — decompose it.")
w("2. **Appears exactly once.** If a capability seems to belong in two places, either it is two "
  "distinct capabilities or the parent is wrong. Cross-cutting concerns are handled by overlays, "
  "never by duplication.")
w("3. **Stop at L3.** L1 covers the space. L2 is coherent enough to have one owner. L3 is where "
  "evidence exists. L4 only where a specific area genuinely needs it.")
w("4. **Score at L2, decompose to L3 on the critical path.** %d scores is a workshop series; "
  "%d is a survey nobody finishes. Never score L1." % (NL2, NL3))
w("")


w("### The fourth overlay: lines of defence")
w("")
w("Several capabilities look like duplicates until you know this axis. Designing a prompt boundary "
  "(`4.3.5`) and defending one at run time (`7.4.3`) are different capabilities with different owners, "
  "different evidence and different failure modes. So are placing a workload (`5.4.4`) and deciding "
  "where data may go (`3.1.5`). The model separates **design-time** (D2, D4), **run-time** (D5, D6) and "
  "**assurance-time** (D7) — and where a pair could not be separated on that axis it was collapsed to "
  "one node.")
w("")
w("### How an L2 score is derived from L3 evidence")
w("")
w("Without this rule the gap arithmetic is arithmetic performed on opinion.")
w("")
w("1. **Weakest link — mandatory for D7 and any capability supporting a risk-tiered use case.** The L2 "
  "score may not exceed the lowest scored L3 beneath it.")
w("2. **Median elsewhere**, with an explicit written justification for any override, recorded on the "
  "capability.")
w("3. **Never score L1.**")
w("4. An L2 scored with no L3 evidence recorded is marked *unevidenced* and excluded from the heat map, "
  "rather than shown as a number.")
w("")
w("### Repository anchoring — read before loading this into an EA repository")
w("")
w("Every capability carries an anchor class, because a third of this tree would otherwise duplicate "
  "capabilities the institution already has.")
w("")
w("| Class | Count | What to do with it |")
w("|---|---:|---|")
_ac = {}
for d in M:
    for c in d[3]: _ac[c[6]] = _ac.get(c[6], 0) + 1
w("| **New** | %d | No existing enterprise capability covers it. Record as a new node with a new owner. |" % _ac.get("new",0))
w("| **Specialization** | %d | An AI-specific specialization of an existing capability. Keep as its own node, linked to the parent. |" % _ac.get("specialization",0))
w("| **Lens** | %d | **Should not become a separate node.** Record as an AI view on the existing capability, keeping its existing owner. |" % _ac.get("lens",0))
w("")
w("Loading the %d lenses as new nodes is how an institution ends up with two change-management "
  "capabilities, two owners and two maturity scores that disagree." % _ac.get("lens",0))
w("")
w("### Where the shape came from, stated plainly")
w("")
w("The **L1 partition follows AWS CAF-AI's perspectives**, deliberately, with Security folded into "
  "Governance and three domains inserted in the middle. Per-capability provenance records where the "
  "*content* came from; it cannot record where the *shape* came from, so it is recorded here. The "
  "largest single content source is ISO/IEC 42001. D2, D3 and D4 have no CAF analogue and derive from "
  "IBM's GenAI capability model and ISO/IEC 5338.")
w("")
w("### What this model does not yet do")
w("")
w("- **No control mapping.** ISO/IEC 42001 Annex A and the NIST AI RMF functions are not mapped onto "
  "capabilities. Until they are, D7's claim to coverage is an assertion, and **D7 should be carved out "
  "of any approval request**.")
w("- **No per-capability rubrics.** One generic 1–5 scale covers all 50.")
w("- **Legal applicability is undetermined.** See section 10.")
w("- **The scale is CMMI-derived**, not a MITRE artifact. It is a generic maturity scale and is "
  "described as one.")
w("")

w("## 3. Domain index")
w("")
w("| ID | Domain | Able to… | L2 | L3 | ⬥ | Lens |")
w("|---|---|---|---:|---:|:-:|---:|")
for d in M:
    n3 = sum(len(c[4]) for c in d[3])
    na = sum(1 for c in d[3] if ag2(c))
    anchor = re.sub(r"[^a-z0-9 -]", "", ("%s  %s" % (d[0], d[1])).lower()).replace(" ", "-")
    nl = sum(1 for c in d[3] if c[6] == "lens")
    w("| **%s** | [%s](#%s) | %s | %d | %d | %s | %s |" %
      (d[0], d[1], anchor,
       d[2].replace("Able to ", "").rstrip("."), len(d[3]), n3, na or "", nl or ""))
w("")
w("---")
w("")

w("## 4. The model")
for d in M:
    w("")
    w("### %s · %s" % (d[0], d[1]))
    w("")
    w("*%s*" % d[2])
    w("")
    w("| ID | Assessment subject | Proposed owner | Anchor | Conf. | Criteria | Primary provenance |")
    w("|---|---|---|---|---|---:|---|")
    for c in d[3]:
        w("| `%s` | **%s**%s | %s | %s | %s | %d | %s |" %
          (c[0], c[1], " ⬥" if ag2(c) else "", c[7],
           {"new":"New","specialization":"Spec.","lens":"**Lens**"}[c[6]], c[8],
           len(c[4]), " · ".join(c[3])))
    w("")
    for c in d[3]:
        w("#### %s %s%s" % (c[0], c[1], " ⬥" if ag2(c) else ""))
        w("")
        w("%s" % c[2])
        w("")
        w("| L3 | Assessment unit | Definition |")
        w("|---|---|---|")
        for x in c[4]:
            w("| `%s` | %s%s | %s |" % (x[0], x[1], " ⬥" if ag3(x) else "", x[2]))
        w("")
w("---")
w("")

w("## 5. Maturity scale")
w("")
w("| Level | Name | Definition | Evidence you would expect to find |")
w("|:-:|---|---|---|")
for n, nm, dfn, ev in [
 (0,"Absent","Applicability confirmed and a documented inquiry finds no operating instance of the ability.","A positive absence finding — not simply the lack of a search."),
 (1,"Initial","Verified isolated execution that relies on individuals and is not repeatable.","Evidence of isolated execution; no common method."),
 (2,"Repeatable","Repeatable within named local scopes over a defined period.","Repeated execution, local ownership, specified coverage."),
 (3,"Defined","An approved common method and roles are applied across the required scope.","A published standard, a coverage rule, sampled conformance."),
 (4,"Managed","Thresholds, exceptions and corrective actions operate over a defined period.","Monitoring with thresholds, control tests, retained evidence."),
 (5,"Adaptive","At least one completed evidence-driven improvement cycle produced a verified outcome.","Trend, action, verified benefit, external comparison."),
]:
    w("| **%d** | %s | %s | %s |" % (n, nm, dfn, ev))
w("")
w("**States — not levels. They never enter arithmetic.**")
w("")
w("| State | Meaning |")
w("|:-:|---|")
w("| **NE** | Applicable, but evidence is insufficient to rate. Appears in the completeness view. |")
w("| **UC** | Applicability or legal status under clarification. An active decision gap with an owner and a due date. |")
w("| **NA** | Formally not applicable, with approver, rationale, effective date and expiry. |")
w("")
w("Absence of evidence is not evidence of absence. `0` means a documented inquiry positively established "
  "that the ability does not operate; where that inquiry has not happened the honest answer is `NE` or `UC`.")
w("")
w("### How a rating is derived — gated, not averaged")
w("")
w("1. The rating is the **highest level for which every applicable mandatory criterion at that level and at "
  "all lower levels** is satisfied by valid evidence.")
w("2. Alternative routes are expressed as approved AND/OR gate logic. Enhancing criteria never compensate for "
  "an unmet mandatory gate.")
w("3. Conditional criteria enter the gate only when a pre-approved trigger is true; applicability is settled "
  "and versioned before evidence is examined.")
w("4. Only a **predeclared essential control** may cap maturity. Other failed controls create conformance gaps "
  "and affect assurance rather than silently lowering the organizational rating.")
w("5. **Never rate L1.** Domains are reporting containers.")
w("")
w("Every result belongs to an **assessment context** — organizational boundary, as-of date, assessor, rubric "
  "version, and in a full implementation jurisdiction, use-case class, risk tier and autonomy level. "
  "**Local ratings are not averaged into an enterprise rating**; enterprise maturity is assessed separately "
  "against enterprise coverage criteria, and local results are reported as a distribution.")
w("")
w("Rate **current** against evidence that exists today, not intent. Set **target** at the level the "
  "institution's risk appetite requires — not every subject needs a 5.")
w("")
w("**Priority is a governed decision, not a subtraction.** A three-level gap can be low priority and a "
  "one-level gap can be urgent. Subjects fall into categorical lanes — *Mandatory/urgent*, "
  "*Foundational/enabling*, *Value-led*, *Deferred/monitor*, plus *Blocked* for `NE` and `UC` — and a "
  "Priority Decision record capturing outcome contribution, deadline, residual risk, dependency, capacity "
  "and sponsor settles each one. Never subtract ordinal levels to estimate effort or benefit.")
w("")

w("## 6. Provenance index")
w("")
w("Which published framework each capability was normalized from. This is not an endorsement of "
  "that framework's wording, and no vendor term is carried into the taxonomy itself. Use it to "
  "answer *“where did this come from”* in architecture and audit review.")
w("")
idx = {}
for _, c in L2:
    for s in c[3]:
        idx.setdefault(s, []).append(c[0])
w("| Source | Capabilities |")
w("|---|---|")
for s in sorted(idx, key=lambda k: (-len(idx[k]), k)):
    w("| %s | %s |" % (s, ", ".join("`%s`" % i for i in idx[s])))
w("")

# ---------------- service layer ----------------
_ns = {}
exec(io.open("catalog4.py", encoding="utf-8").read(), _ns)
SVC = _ns["S"]
SVCS = [(g, sv) for g in SVC for sv in g[4]]
L3TOL2 = {x[0]: c[0] for d in M for c in d[3] for x in c[4]}
L2NAME = {c[0]: c[1] for d in M for c in d[3]}
COV, ANYEDGE = {}, {}
for g, sv in SVCS:
    seen = set()
    for ref, et in sv[4]:
        l2 = L3TOL2.get(ref, ref)
        ANYEDGE[l2] = ANYEDGE.get(l2, 0) + 1
        if et not in ("required-enabler", "optional-enabler"): continue
        if (l2, g[0]) in seen: continue
        seen.add((l2, g[0]))
        COV.setdefault(l2, {}).setdefault(g[0], 0)
        COV[l2][g[0]] += 1
_gv0 = {}
exec(io.open("gen_trm.py", encoding="utf-8").read().split("CAPJSON =")[0]
     .replace("exec(io.open('catalog4.py', encoding='utf-8').read())", ""), _gv0)
EXT, HUMAN = _gv0["EXT"], _gv0["HUMAN"]

w("## 7. AI reference catalog — services, building blocks, patterns, standards")
w("")
w("What *could* exist in the AI domain, vendor-neutral and stable. **Nothing here is a capability and "
  "nothing here is a product.** %d entries across %d groups, %d typed edges. Four kinds:" %
  (len(SVCS), len(SVC), sum(len(sv[4]) for _, sv in SVCS)))
w("")
w("| Kind | Meaning | Test | Count |")
w("|---|---|---|---:|")
_kc = {}
for _, _sv in SVCS: _kc[_sv[6]] = _kc.get(_sv[6], 0) + 1
w("| **SVC** | Service type — something a consumer calls | Can someone call it and get a result? | %d |" % _kc.get("SVC",0))
w("| **ABB** | Logical building block | Is it a piece *inside* an architecture? | %d |" % _kc.get("ABB",0))
w("| **PAT** | Pattern — a governed arrangement of blocks | Does it have forces and a resulting context? | %d |" % _kc.get("PAT",0))
w("| **STD** | Open standard or protocol profile | Is it a specification someone else maintains? | %d |" % _kc.get("STD",0))
w("")
w("Entries marked *either* are genuinely ambiguous: OCR is an ABB when you are designing a document "
  "pipeline and a Service when someone exposes an endpoint. Same concept, two registers — not a conflict.")
w("")
w("Read this layer with the tier table in section 2 in mind. A service here is expected to be replaced on a "
  "2-5 year clock without the capability model changing.")
w("")
w("| ID | Service group | Services | Primary provenance |")
w("|---|---|---:|---|")
for g in SVC:
    w("| **%s** | %s | %d | %s |" % (g[0], g[1], len(g[4]), " · ".join(g[3][:3])))
w("")
for g in SVC:
    w("### %s · %s" % (g[0], g[1]))
    w("")
    w("*%s*" % g[2])
    w("")
    w("Group provenance: %s" % " · ".join(g[3]))
    w("")
    w("| ID | Entry | Kind | Definition | Typed edges | Flags |")
    w("|---|---|---|---|---|---|")
    for sv in g[4]:
        fl = sv[5] if len(sv) > 5 else ""
        flag = " ".join(x for x in [
            "⬥ agentic" if fl == "a" else ("⚑ regulatory" if fl == "r" else ""),
            "*either*" if sv[11] else ""] if x)
        edges = ", ".join("`%s` %s" % (r_, t_) for r_, t_ in sv[4]) or "—"
        w("| `%s` | **%s** | **%s** | %s | %s | %s |" % (sv[0], sv[1], sv[6], sv[2], edges, flag))
    w("")
w("---")
w("")
w("## 8. Matrix A — subject × catalog group")
w("")
w("The join between the two models. **The blanks are the finding, and they come in three kinds.** "
  "Some capabilities are realized by existing non-AI enterprise services (ENT). Others are purely "
  "organizational and no technology realizes them (HUM). A blank that is neither would be a genuine gap.")
w("")
w("| Capability | %s | Σ | Blank reason |" % " | ".join(g[0] for g in SVC))
w("|---|%s---:|---|" % ("---:|" * len(SVC)))
for d in M:
    w("| **%s · %s** %s" % (d[0], d[1], "| " * (len(SVC) + 2) + "|"))
    for c in d[3]:
        row = COV.get(c[0], {})
        tot = sum(row.values())
        cells = " | ".join(str(row.get(g[0], "") or "") for g in SVC)
        if tot:
            reason = ""
        elif c[0] in EXT:
            reason = "**ENT** — %s" % EXT[c[0]]
        elif ANYEDGE.get(c[0]):
            reason = "control / evidence support only — the ability itself is organizational"
        elif c[0] in HUMAN:
            reason = "**HUM** — organizational capability"
        else:
            reason = "**UNEXPLAINED — review**"
        w("| `%s` %s | %s | %s | %s |" % (c[0], c[1], cells, tot or "", reason))
w("")
unex = [c[0] for d in M for c in d[3] if not COV.get(c[0]) and not ANYEDGE.get(c[0]) and c[0] not in EXT and c[0] not in HUMAN]
w("Unexplained blanks: **%s**." % ("none" if not unex else ", ".join(unex)))
w("")
w("## 9. What backs the reference catalog")
w("")
w("Assessed rather than asserted. The honest finding: **no standards body publishes a functional taxonomy "
  "of AI services.** ISO/IEC 42001, 5338, 23894 and the NIST AI RMF — the backbone of the capability model — "
  "contain none. Verified September 2026.")
w("")
_gv = {}
exec(io.open("gen_trm.py", encoding="utf-8").read().split("CAPJSON =")[0]
     .replace("exec(io.open('services.py', encoding='utf-8').read())", ""), _gv)
import re as _re
_strip = lambda t: _re.sub(r"<[^>]+>", "", t).replace("&amp;", "&")
w("| Source | What it actually gives | Status | Backing | Caveat |")
w("|---|---|---|---|---|")
for b in _gv["BACKING"]:
    lab = {"strong":"**strong**","partial":"partial","weak":"weak","none":"**not a taxonomy**"}[b[3]]
    w("| %s | %s | %s | %s | %s |" % (_strip(b[0]), _strip(b[1]), _strip(b[2]), lab, _strip(b[4])))
w("")
w("### Currency corrections verified September 2026")
w("")
w("| Area | What changed | Consequence |")
w("|---|---|---|")
for cur in _gv["CURRENCY"]:
    w("| %s | %s | %s |" % (_strip(cur[0]), _strip(cur[1]), _strip(cur[2])))
w("")


w("## 10. Obligations register — held outside the model, owned by Legal")
w("")
w("Statutory references were **removed from capability provenance** and are held here. Nothing in "
  "this model asserts that any regulation binds the institution. Capability `7.6.5` is the "
  "prerequisite legal determination — a legal opinion that either exists or does not, not a "
  "maturity dimension.")
w("")
w("Two cautions on the entries below, both material:")
w("")
w("- **Articles 49, 72 and 73 are provider obligations.** On every use case contemplated here the "
  "institution would be a *deployer*. Capability `7.6.6` (Regulatory Role Determination) is the "
  "control that establishes which.")
w("- **Article 49 is not authority for an internal asset inventory.** It governs registration in "
  "the EU database. Capability `7.7` is defensible on management grounds alone and should be "
  "justified that way.")
w("")
_ob = json.load(open("obligations.json"))
w("| Applies to | Name | Instrument | Subject |")
w("|---|---|---|---|")
for _o in _ob:
    w("| `%s` | %s | %s | %s |" % (_o["capability"], _o["capability_name"], _o["instrument"], _o["subject"] or "—"))
w("")
w("**Status of every row above: candidate — applicability not determined.**")
w("")


_reg = json.load(open("realization.json"))
w("## 11. Realization catalog — readiness, and why it is not maturity")
w("")
w("The reference catalog above says what *could* exist. This register says what IDB provides today. "
  "Confusing the two is how \"we approved the technology\" becomes \"we have the capability\".")
w("")
w("A service's **state** is a structural fact, not a rating — it depends on which objects exist and who "
  "operates the instances, so it can be read off by inspection.")
w("")
w("| Readiness | Meaning | Evidence that establishes it |")
w("|:-:|---|---|")
for x in _reg["readiness"]:
    w("| **%d · %s** | %s | %s |" % (x["n"], x["k"], x["d"], x["ev"]))
w("")
w("Two questions decide every row: **is there a reusable solution building block, separable from any one "
  "application?** (2 vs 3), and **who operates the instances?** (3 vs 4).")
w("")
w("### Realizations")
w("")
w("One row per capability x pattern x technology. A technology appears on as many rows as it realizes "
  "patterns — that is correct, and a two-tier model cannot express it.")
w("")
w("| ID | Capability | Pattern | Technology | Readiness | Consumption | Status |")
w("|---|---|---|---|:-:|---|---|")
for _sv in _reg["realizations"]:
    _r = _sv["readiness"]
    w("| `%s`%s | `%s` | %s | %s | %s | %s | %s |" % (
        _sv["id"], "" if _sv["conf"] else " *(illustrative)*", _sv["cap"], _sv["pattern"],
        _sv["tech"] or "—",
        ("**%d** %s" % (_r, _reg["readiness"][_r]["k"])) if _r is not None else "—",
        _sv["consumption"] or "—", _sv["status"] or "—"))
w("")
for _sv in _reg["realizations"]:
    if not _sv["note"]: continue
    w("- **`%s`** — %s" % (_sv["id"], _sv["note"]))
w("")
w("### Consumption model")
w("")
w("What the consuming team still has to build. Recorded on the realization, not the capability. "
  "**This is the column that settles the recurring argument** — *\"a capability means I don't have to build "
  "it\"* — without redefining the word capability. That belief is about consumption model; record it as one "
  "and the argument stops being definitional.")
w("")
w("| Model | Meaning |")
w("|---|---|")
for _c in _reg["consumption"]:
    w("| **%s** | %s |" % (_c["k"], _c["d"]))
w("")
w("### Enablement evidence")
w("")
w("Generic assets — standard, pattern document, reference architecture, IaC, CI/CD, security baseline, "
  "observability, runbook, support model — mostly tick together and carry little information once a "
  "realization reaches readiness 4. **The pattern-specific controls are the ones that stay unticked, and the "
  "reason to read the list at all.** An inherited control that cannot be skipped is stronger evidence than a "
  "procurement approval.")
w("")
for _rid, _ctl in _reg["controls"].items():
    w("**%s**" % _rid)
    w("")
    w("| Control | Reference block | Capability | Why it matters |")
    w("|---|---|---|---|")
    for _c in _ctl:
        w("| %s | `%s` | `%s` | %s |" % (_c["name"], _c["ref"], _c["cap"], _c["why"]))
    w("")
w("The workbook carries 76 further candidate realizations generated from the reference catalog, each "
  "awaiting a readiness level. That list is the survey: mark the ones that matter, leave the rest. "
  "**An unmarked row is an unanswered question, not a zero.**")
w("")
w("## 12. Open items")
w("")
w("| # | Item | Note |")
w("|---|---|---|")
w("| 1 | Matrix A — subject × catalog | **Done** — section 8. |")
w("| 2 | Matrix B — service × product | The product mapping against the actual Azure estate. Not started. |")
w("| 3 | Lifecycle value stream | ISO/IEC 5338 stages cross-mapped to L2 capabilities. Not started. |")
w("| 4 | Control mapping | ISO 42001 Annex A and NIST AI RMF functions mapped onto capabilities. Not started. |")
w("| 5 | Anchor points | Where these capabilities specialize the existing enterprise business capability model. Deferred — model built greenfield. |")
w("| 6 | L2 boundary review | D7 at 8 L2s, and the D2/D4 split, are the two decisions most likely to be challenged in review. |")
w("")
w("---")
w("")
w("*Generated from the same source data as the published capability register. "
  "Edit the source, not this file.*")

open("Enterprise-AI-Capability-Model.md","w").write("\n".join(o) + "\n")
print("markdown lines:", len(o))

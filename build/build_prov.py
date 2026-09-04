# -*- coding: utf-8 -*-
import json
import prov_data as P
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

M = json.load(open('model3.json'))
OUT = 'AI-Capability-Provenance-for-review.xlsx'
ARIAL = 'Arial'
NAVY, BLUE, GREY, YELLOW = 'FF1F3864', 'FFDCE6F1', 'FFF2F2F2', 'FFFFF2CC'
RED, AMBER, GREEN = 'FFF8CBAD', 'FFFFE699', 'FFE2EFDA'
thin = Side(style='thin', color='FFBFBFBF')
BORD = Border(left=thin, right=thin, top=thin, bottom=thin)
GRADE_FILL = {'A': GREEN, 'B': 'FFEDF3E8', 'C': AMBER, 'D': RED}

SRC = {s[0]: s for s in P.SOURCES}
DOMNAME = {d[0]: d[1] for d in M}

# ---- candidate loci: (source, domain) -> the part of the source most likely relied on.
# UNVERIFIED against the source text. Offered so the reviewer confirms rather than starts blank.
CAND = {
 ('S01','D1'):'Clause 5 Leadership','(S01,D2)':'', ('S01','D2'):'A.6 AI system life cycle',
 ('S01','D3'):'A.7 Data for AI systems', ('S01','D4'):'A.6 AI system life cycle',
 ('S01','D5'):'A.4 Resources for AI systems', ('S01','D6'):'A.6 AI system life cycle',
 ('S01','D7'):'A.2 Policies related to AI; 8.2 AI risk assessment', ('S01','D8'):'A.3 Internal organization',
 ('S02','D1'):'6.2.3 Portfolio management', ('S02','D2'):'6.4.1 Business or mission analysis',
 ('S02','D3'):'6.4.8 AI data engineering', ('S02','D4'):'6.4.3 System requirements definition to 6.4.13 Validation',
 ('S02','D5'):'6.2.2 Infrastructure management', ('S02','D6'):'6.4.15 Operation; 6.4.16 Maintenance',
 ('S02','D7'):'6.3.4 Risk management', ('S02','D8'):'6.2.4 Human resource management',
 ('S03','D1'):'6.2 Governance oversight of AI', ('S03','D7'):'6.6 Compliance; 6.7 Risk',
 ('S03','D2'):'6.3 Governance of decision-making', ('S03','D3'):'6.4 Governance of data use',
 ('S03','D8'):'6.5 Culture and values',
 ('S04','D7'):'6.4 Risk assessment', ('S04','D1'):'5.2 Leadership and commitment',
 ('S05','D7'):'Clause 5 Developing and implementing an AI system impact assessment process',
 ('S05','D2'):'Clause 6 Documenting the AI system impact assessment',
 ('S06','D7'):'Annex A.5 Organizational; A.8 Technological controls',
 ('S07','D7'):'8.2 Privacy risk assessment',
 ('S08','D1'):'GOVERN', ('S08','D2'):'MAP', ('S08','D3'):'MAP', ('S08','D4'):'MEASURE',
 ('S08','D5'):'GOVERN', ('S08','D6'):'MANAGE', ('S08','D7'):'GOVERN', ('S08','D8'):'GOVERN',
 ('S09','D3'):'Information Integrity; Data Privacy', ('S09','D4'):'Confabulation; Human-AI Configuration',
 ('S09','D7'):'Information Security; Harmful Bias or Homogenization', ('S09','D2'):'Human-AI Configuration',
 ('S10','D1'):'1.1. Inclusive growth, sustainable development and well-being',
 ('S10','D7'):'1.3. Transparency and explainability; 1.5. Accountability',
 ('S10','D2'):'1.2. Respect for the rule of law, human rights and democratic values',
 ('S11','D1'):'Governance principle - organizational level', ('S11','D3'):'Data principle',
 ('S11','D4'):'Performance principle - component level', ('S11','D6'):'Monitoring principle',
 ('S11','D7'):'Governance principle - system level',
 ('S12','D1'):'Business perspective', ('S12','D2'):'Business perspective',
 ('S12','D3'):'Platform perspective - Data Architecture, Data Engineering',
 ('S12','D4'):'Platform perspective - AI Lifecycle Management and MLOps',
 ('S12','D5'):'Platform perspective - Platform Architecture, Platform Engineering',
 ('S12','D6'):'Operations perspective', ('S12','D7'):'Governance perspective - Responsible use of AI; Security perspective',
 ('S12','D8'):'People perspective',
 ('S13','D1'):'Strategy phase', ('S13','D2'):'Plan phase', ('S13','D3'):'Ready phase',
 ('S13','D4'):'Ready phase', ('S13','D5'):'Ready phase', ('S13','D6'):'Manage phase',
 ('S13','D7'):'Govern phase; Secure phase', ('S13','D8'):'Plan phase',
 ('S14','D1'):'Lead theme', ('S14','D2'):'Lead theme', ('S14','D3'):'Access theme',
 ('S14','D4'):'Automate theme', ('S14','D5'):'Scale theme', ('S14','D6'):'Automate theme',
 ('S14','D7'):'Secure theme', ('S14','D8'):'Learn theme',
 ('S15','D3'):'Data Management', ('S15','D4'):'GenAI Application Development',
 ('S15','D5'):'GenAI Operations', ('S15','D6'):'GenAI Operations',
 ('S15','D7'):'GenAI Governance; GenAI Security Management', ('S15','D2'):'Supporting Capabilities',
 ('S16','D5'):'Ecosystem Architecture; Validated Full Stack AI Factories', ('S16','D4'):'Agentic AI in the Factory',
 ('S16','D6'):'Deployment Strategies',
 ('S17','D3'):'Foundation Layer (AI & data)', ('S17','D4'):'Process Layer', ('S17','D5'):'Platform Layer',
 ('S17','D2'):'User Experience Layer',
 ('S18','D4'):'Development; Testing and Validation', ('S18','D6'):'Monitoring and Tuning',
 ('S18','D2'):'Ideation and Design',
 ('S19','D1'):'New value creation', ('S19','D2'):'Operations redesign',
 ('S19','D3'):'Intelligence engines', ('S19','D4'):'Adaptive technology stacks',
 ('S19','D5'):'Adaptive technology stacks', ('S19','D6'):'Adaptive technology stacks',
 ('S19','D8'):'Human-AI teaming', ('S19','D7'):'Human-AI teaming',
 ('S20','D4'):'Architecture Content; ADM Techniques', ('S20','D1'):'Enterprise Architecture Capability and Governance',
 ('S21','D1'):'G193 in full', ('S22','D2'):'Part 2 The Agile Enterprise',
 ('S22','D4'):'Part 3 The Agile Architecture Capability', ('S22','D8'):'Part 1 The Agile Way of Thinking',
 ('S22','D1'):'Part 2 The Agile Enterprise', ('S22','D5'):'Part 4 The Ways of Supporting',
 ('S23','D1'):'Evaluate value stream', ('S23','D2'):'Explore value stream',
 ('S23','D4'):'Integrate value stream', ('S23','D5'):'Deploy value stream',
 ('S23','D6'):'Operate value stream',
 ('S24','D6'):'Service management practices - incident, problem, monitoring',
 ('S24','D5'):'Service management practices - service configuration, deployment',
 ('S24','D8'):'General management practices - workforce and talent management',
 ('S25','D3'):'Data Quality Management; Govern Data & Data Management Program',
 ('S26','D3'):'', ('S27','D6'):'Optimize Usage & Cost; Quantify Business Value',
 ('S27','D1'):'Quantify Business Value - Unit Economics', ('S27','D5'):'Optimize Usage & Cost - Architecting & Workload Placement',
 ('S28','D7'):'Principle 4 - distinct sources of assurance',
 ('S29','D1'):'Strategy and Resources pillar', ('S29','D2'):'Performance and Application pillar',
 ('S29','D3'):'Data pillar', ('S29','D4'):'Technology Enablers pillar',
 ('S29','D5'):'Technology Enablers pillar', ('S29','D6'):'Performance and Application pillar',
 ('S29','D7'):'Ethical, Equitable, and Responsible Use pillar', ('S29','D8'):'Organization pillar',
 ('S30','D1'):'Stage 3 Develop AI Ways of Working', ('S30','D8'):'Stage 3 Develop AI Ways of Working',
 ('S31','D7'):'Accountability; Testing and Assurance', ('S31','D2'):'Trusted Development and Deployment',
 ('S31','D3'):'Data; Content Provenance', ('S31','D4'):'Trusted Development and Deployment',
 ('S31','D5'):'Security',
 ('S32','D7'):'By entry name only - e.g. Excessive Agency, Prompt Injection',
 ('S32','D4'):'By entry name only - e.g. Improper Output Handling',
 ('S33','D4'):'2026-07-28, Server Features', ('S33','D5'):'2026-07-28, Architecture',
}

# capabilities that no external source names as a capability - assembled, not adopted
SYNTH = {'1.5','2.6','3.6','3.7','4.3','4.4','5.2','5.5','7.7','7.8','7.9','2.5','5.6','6.6'}

DERIV_DEFS = [
 ('Adopted','The source names this capability as a capability, and our wording follows it. Strongest claim - a reviewer can put the two side by side.'),
 ('Adapted','The source names it, and we narrowed, renamed or re-scoped it for the institution. The commonest honest case.'),
 ('Corroborating','The source did not originate the capability but independently supports that it belongs in the model. Never the only source on a row.'),
 ('Synthesized','No single source names it. Assembled from two or more that each cover part of it - or from what the model demonstrably needs and nothing published yet covers.'),
 ('Institutional','Derived from IDB policy or practice, not from any external source.'),
 ('Unsupported','The cited source does not substantiate the capability. Must be removed or replaced before the model is published.'),
]
GRADE_DEFS = [
 ('A','Openly available, dated, versioned, from a standards body or public authority. A reviewer can open it today and find the cited part.'),
 ('B','Openly available and dated, but vendor-published or non-normative. Verifiable, not authoritative.'),
 ('C','Available but undated, superseded, flagged historical by its own publisher, or paywalled. A reviewer may not be able to check it.'),
 ('D','Non-public, or not a publication at all. Cannot serve as evidence in anything that leaves the Bank.'),
]

FINDINGS = [
 ("F01","EDM Council ADAC is not a publication","S26","3.1, 3.3, 3.4, 3.7","Critical",
  "ADAC (AI, Data & Analytics Controls) is an EDM Council workgroup, not a framework. It is absent from EDM Council's own Frameworks page; the visible output is webinars and a 2024 SIG deck. It was cited four times as if it were a document.",
  "Remove ADAC from all four capabilities. If an EDM Council AI/data-controls reference is needed, substitute CDMC, which is openly available for internal use."),
 ("F02","TOGAF capability-based planning was removed from the current edition","S21","1.2","Critical",
  "Capability-Based Planning was Chapter 28 of TOGAF 9.2. The Open Group deliberately removed it in the 10th Edition because it is incompatible with the Business Capabilities Series Guide. Our citation pointed at a section that no longer exists.",
  "Re-cite as TOGAF Series Guide G193 (Capability-Based Planning) or G190 (Business Capabilities v2). Already reflected in the register as S21."),
 ("F03","The IIA Three Lines Model we cited has been superseded","S28","7.8","High",
  "The 2020 position paper was replaced on 8 July 2026 by the Statement of Position 'Assurance and Advice in Support of Effective Governance'. It carries five principles, not six. 'Three Lines of Defense' is doubly retired.",
  "Cite the 2026 Statement of Position. Check any capability wording that assumed the six-principle structure."),
 ("F04","ISO/IEC 27701:2019 clause references no longer resolve","S07","7.5","High",
  "The second edition (October 2025) converted 27701 from an extension of 27001/27002 into a standalone management system standard. The old PIMS-specific clause forms do not exist in it.",
  "Re-pin against the 2025 edition; Annex F carries the correspondence from the 2019 numbering."),
 ("F05","ITIL 4 is no longer the current ITIL","S24","6.1, 6.4, 5.3","Medium",
  "ITIL Version 5 was announced in January 2026 and is rolling out; ITIL 4 remains valid in parallel through a transition period.",
  "Keep the ITIL 4 citation but add the qualifier. Do not describe ITIL 4 as current without it."),
 ("F06","AWS flags CAF-AI as historical reference only","S12","seven capabilities","Medium",
  "AWS displays 'This whitepaper is for historical reference only. Some content might be outdated' on the CAF-AI page. It is our most-used vendor capability source.",
  "Keep it - it is still the best-structured public AI capability model - but cite it as a February 2024 artifact and disclose the banner rather than let a reviewer find it."),
 ("F07","Our IMDA citation is ambiguous across three documents","S31","five capabilities","High",
  "Three published frameworks share the name: the original Model AI Governance Framework (2nd ed. 2020), the Generative AI framework (May 2024, nine dimensions) and the Agentic AI framework (v1.0, January 2026, four dimensions). We cited it unqualified.",
  "Pick one per capability. Agentic capabilities should point at the January 2026 agentic framework (added to the register as S31b)."),
 ("F08","MIT CISR is a research centre, not a document","S30","1.3","High",
  "'MIT CISR' names no artifact. A citation has to name a Research Briefing or Working Paper with its volume and number.",
  "Substitute the August 2025 Research Briefing 'Grow Enterprise AI Maturity for Bottom-Line Impact' (Vol. XXV, No. 8), already in the register."),
 ("F09","NIST AI RMF locus form","S08","all NIST citations","Medium",
  "The correct citation form is GOVERN 1.1 - function, space, category.subcategory. The hyphenated GOVERN-1.1 is not valid; that convention belongs to AI 600-1 action identifiers (GV-1.1-001).",
  "Use the space form throughout. Any hyphenated reference in draft text is wrong."),
 ("F10","OECD principle 1.2 was retitled","S10","1.1, 7.2","Medium",
  "The Recommendation was amended in November 2023 and May 2024. Principle 1.2, cited widely under its 2019 name 'Human-centred values and fairness', is now 'Respect for the rule of law, human rights and democratic values, including fairness and privacy'.",
  "Cite the amended text and the current principle titles."),
 ("F11","Non-public sources cannot carry evidence","S34, S35","four capabilities","Critical",
  "Gartner research is subscription-licensed - usable internally, not quotable in anything that circulates externally, and not openable by a reviewer without a seat. 'Consultancy transformation patterns' names nothing at all.",
  "Remove both from the published provenance. Where a capability rests only on them, find an open source or reclassify it as Synthesized and say so."),
 ("F12","'Institutional practice' names no document","S36, S37, S38, S39","six capabilities","High",
  "Institutional origin is legitimate, but 'institutional practice' is not a citation - a reviewer cannot open it, date it, or find its owner.",
  "Replace each use with a named internal policy, standard or procedure, with an owner and a date. Data Governance, Legal and Internal Audit each own one of these."),
 ("F13","Google's framework is undated and pre-GenAI","S14","four capabilities","Medium",
  "The whitepaper carries no date or version and addresses neither generative AI nor agents. It is a genuine maturity grid, which is why it is useful.",
  "Cite as undated, accessed on a stated day, and do not rely on it for anything GenAI-specific."),
 ("F14","NVIDIA: the landing page is marketing, not a design document","S16","5.4","Medium",
  "nvidia.com/solutions/ai-factories/validated-design is a product landing page. The citable artifact is the Enterprise AI Factory Design Guide on docs.nvidia.com.",
  "Point the citation at the design guide. Register already does."),
 ("F15","SAP disclaims that its North Star is a specification","S17","three capabilities","Low",
  "SAP states: 'This is not a specification, roadmap, or promise of delivery. It is a direction of travel.'",
  "Quote the disclaimer wherever the source is cited, and never present it as a specification."),
 ("F16","The MCP revision we built against has been superseded by a breaking change","S33","4.5, 5.5","High",
  "Revision 2026-07-28 removes protocol-level sessions and the initialize handshake, adds server/discover, and deprecates Roots, Sampling and Logging. Anything written against 2025-11-25 is out of date.",
  "Re-read 4.5 and 5.5 and the MCP-related realizations against the 2026-07-28 revision before the assessment is signed."),
 ("F17","Salesforce ADLC has no publication date","S18","4.4","Low",
  "The guide carries no date or version.",
  "Cite as undated, accessed " + P.ACCESS_DATE + "."),
 ("F18","Every candidate locus in this workbook is unverified","all","all","High",
  "Column H of the mapping sheet is my best reading of which part of each source a capability rests on. None of it has been checked against the source text, and eleven of the sources are paywalled or members-only.",
  "Confirm or correct each one. A capability whose locus is never pinned should be downgraded to Synthesized rather than left claiming a source it cannot point into."),
]

# ------------------------------------------------------------------ build rows
PAIRS = []
for d in M:
    did = d[0]
    for l2 in d[3]:
        lid, lname, ldef, prov, l3s, agentic, anchor, owner, conf = l2
        expanded = []
        for raw in prov:
            sid, locus = P.NORMALIZE[raw]
            expanded.append((raw, sid, locus))
            if raw in P.EXTRA_FROM:
                x = P.EXTRA_FROM[raw]
                expanded.append((raw + '  (second artifact named in the same string)', x[0], x[1]))
        n_ext = sum(1 for _, sid, _ in expanded if SRC[sid][11] not in ('Not a publication',)
                    and not sid.startswith('S3') or sid in ('S30','S31','S31b','S32','S33'))
        for i, (raw, sid, locus) in enumerate(expanded):
            s = SRC[sid]
            grade = s[10]
            if sid == 'S26':
                deriv = 'Unsupported'
            elif sid in ('S34','S35'):
                deriv = 'Unsupported'
            elif sid in ('S36','S37','S38','S39'):
                deriv = 'Institutional'
            elif lid in SYNTH:
                deriv = 'Synthesized'
            elif i == 0:
                deriv = 'Adapted'
            else:
                deriv = 'Corroborating'
            cand = locus or CAND.get((sid, did), '')
            status = ('stated in our own citation' if locus
                      else ('candidate - unverified' if cand else 'NOT PINNED'))
            PAIRS.append([did, lid, lname, sid, s[1], raw, cand, status, deriv, grade,
                          s[11], s[7]])

USED = {}
for r in PAIRS:
    USED[r[3]] = USED.get(r[3], 0) + 1

# ------------------------------------------------------------------ workbook
wb = Workbook()

def head(ws, hdr, widths, hrow=30):
    for i, h in enumerate(hdr, 1):
        c = ws.cell(1, i, h)
        c.font = Font(name=ARIAL, size=10, bold=True, color='FFFFFFFF')
        c.fill = PatternFill('solid', fgColor=NAVY)
        c.alignment = Alignment(wrap_text=True, vertical='center')
        ws.column_dimensions[get_column_letter(i)].width = widths[i-1]
    ws.row_dimensions[1].height = hrow

# ---- 0. Read me
ws = wb.active; ws.title = '0. Read me'
ws.column_dimensions['A'].width = 3
ws.column_dimensions['B'].width = 34
ws.column_dimensions['C'].width = 104
rows = [
 ('h','AI Capability Model - provenance for review',''),
 ('','','Where each capability definition came from, how strongly, and whether a reviewer can open the source and check it.'),
 ('','','Companion to AI-Capability-Taxonomy-for-review.xlsx. That workbook asks whether the capability is right. This one asks whether we can prove where it came from.'),
 ('s','What changed before you got this',''),
 ('','Every source was re-verified','Publisher, edition, date, URL and access were checked on ' + P.ACCESS_DATE + '. That check found eighteen problems, all on sheet 3. Four are serious enough to block publication.'),
 ('','The worst of them','We cited EDM Council ADAC four times. It is a workgroup, not a publication - there is nothing to open. We cited TOGAF capability-based planning, which The Open Group deliberately removed from the 10th Edition. And four capabilities rest on Gartner or unattributed consultancy patterns, neither of which can appear in anything that leaves the Bank.'),
 ('','50 citation strings, 40 sources','The model carried inconsistent variants - IBM GenAI vs IBM Generative AI, NIST AI RMF vs NIST AI RMF - Map. They are now one canonical source each, with the part of the source recorded separately.'),
 ('s','How to use it',''),
 ('','Sheet 1 - Source register','One row per source. Read the Grade and Caution columns first. Grade D means it cannot be used as evidence outside the Bank.'),
 ('','Sheet 2 - Capability to source','One row per capability-source pair. Column G is the specific part of the source the capability rests on; column H says how much to trust that.'),
 ('','Sheet 3 - Findings','The eighteen problems, with what to do about each. Column I is yours.'),
 ('','Sheet 4 - Scales','What the derivation types and evidence grades mean. Read once.'),
 ('','Sheet 5 - Coverage','How the evidence base looks by domain. Where the thin spots are.'),
 ('s','The one thing to be careful about',''),
 ('','Candidate loci are unverified','Column G on sheet 2 is my best reading of which part of each source a capability rests on. None of it is checked against the source text, and eleven sources are paywalled or members-only, so I could not check them. Treat column G as a work instruction, not a finding.'),
 ('','What honest looks like here','A capability that never gets its locus pinned should be reclassified Synthesized - assembled by us - rather than left claiming a source it cannot point into. That is a stronger position with Internal Audit than a citation that does not resolve.'),
 ('s','Counts',''),
]
r = 1
for kind, b, c in rows:
    if kind == 'h':
        ws.cell(r, 2, b).font = Font(name=ARIAL, size=16, bold=True, color=NAVY)
    elif kind == 's':
        r += 1
        ws.cell(r, 2, b).font = Font(name=ARIAL, size=12, bold=True, color=NAVY)
    else:
        ws.cell(r, 2, b).font = Font(name=ARIAL, size=10, bold=True)
        cc = ws.cell(r, 3, c); cc.font = Font(name=ARIAL, size=10)
        cc.alignment = Alignment(wrap_text=True, vertical='top')
        ws.row_dimensions[r].height = 14 + 14 * (len(c) // 108)
    r += 1
for lbl, f in (
  ('Sources cited', "=COUNTA('1. Source register'!$A$2:$A$100)"),
  ('Capability-source pairs', "=COUNTA('2. Capability to source'!$A$2:$A$400)"),
  ('Pairs on grade A evidence', "=COUNTIF('2. Capability to source'!$J$2:$J$400,\"A\")"),
  ('Pairs on grade D - unusable externally', "=COUNTIF('2. Capability to source'!$J$2:$J$400,\"D\")"),
  ('Pairs with no locus at all', "=COUNTIF('2. Capability to source'!$H$2:$H$400,\"NOT PINNED\")"),
  ('Findings to clear', "=COUNTA('3. Findings'!$A$2:$A$60)")):
    ws.cell(r, 2, lbl).font = Font(name=ARIAL, size=10, bold=True)
    ws.cell(r, 3, f).font = Font(name=ARIAL, size=10)
    r += 1
ws.sheet_view.showGridLines = False

# ---- 1. Source register
ws = wb.create_sheet('1. Source register')
H = ['ID','Short name','Canonical title','Publisher','Edition / version','Date','URL','Access',
     'Type','What a valid citation looks like','Grade','Status','Caution','Times cited',
     'Your decision','Your notes']
W = [7,26,52,30,22,16,52,26,26,42,7,26,74,10,20,44]
head(ws, H, W)
r = 2
for s in P.SOURCES:
    vals = list(s[:13]) + [USED.get(s[0], 0), '', '']
    for i, v in enumerate(vals, 1):
        c = ws.cell(r, i, v)
        c.font = Font(name=ARIAL, size=10, bold=(i == 2))
        c.border = BORD
        c.alignment = Alignment(wrap_text=True, vertical='top')
    ws.cell(r, 11).fill = PatternFill('solid', fgColor=GRADE_FILL[s[10]])
    ws.cell(r, 11).alignment = Alignment(horizontal='center', vertical='top')
    ws.cell(r, 11).font = Font(name=ARIAL, size=11, bold=True)
    if s[10] == 'D':
        for i in (1, 2, 12):
            ws.cell(r, i).fill = PatternFill('solid', fgColor=RED)
    if s[6].startswith('http'):
        ws.cell(r, 7).hyperlink = s[6]
        ws.cell(r, 7).font = Font(name=ARIAL, size=9, color='FF0563C1', underline='single')
    for i in (15, 16):
        ws.cell(r, i).fill = PatternFill('solid', fgColor=YELLOW)
    r += 1
SRC_LAST = r - 1
dv = DataValidation(type='list', allow_blank=True, showDropDown=False,
  formula1='"Keep,Keep with caution noted,Replace,Remove,Pin the edition,Not sure - discuss"')
ws.add_data_validation(dv); dv.add('O2:O%d' % SRC_LAST)
ws.freeze_panes = 'C2'; ws.auto_filter.ref = 'A1:P%d' % SRC_LAST

# ---- 2. Capability to source
ws = wb.create_sheet('2. Capability to source')
H = ['Domain','Capability','Capability name','Source ID','Source','As cited in the model today',
     'Candidate locus (UNVERIFIED)','Locus status','Derivation','Grade','Source status','Access',
     'Your decision','Corrected locus','Your notes']
W = [8,10,42,8,26,38,50,22,15,7,24,24,20,34,44]
head(ws, H, W)
r = 2
for p in PAIRS:
    vals = p + ['', '', '']
    for i, v in enumerate(vals, 1):
        c = ws.cell(r, i, v)
        c.font = Font(name=ARIAL, size=10, bold=(i == 3))
        c.border = BORD
        c.alignment = Alignment(wrap_text=True, vertical='top')
    ws.cell(r, 10).fill = PatternFill('solid', fgColor=GRADE_FILL[p[9]])
    ws.cell(r, 10).alignment = Alignment(horizontal='center', vertical='top')
    ws.cell(r, 10).font = Font(name=ARIAL, size=11, bold=True)
    if p[8] == 'Unsupported':
        ws.cell(r, 9).fill = PatternFill('solid', fgColor=RED)
        ws.cell(r, 9).font = Font(name=ARIAL, size=10, bold=True)
    elif p[8] == 'Synthesized':
        ws.cell(r, 9).fill = PatternFill('solid', fgColor=AMBER)
    if p[7] == 'NOT PINNED':
        ws.cell(r, 8).fill = PatternFill('solid', fgColor=AMBER)
    for i in (13, 14, 15):
        ws.cell(r, i).fill = PatternFill('solid', fgColor=YELLOW)
    r += 1
MAP_LAST = r - 1
dv2 = DataValidation(type='list', allow_blank=True, showDropDown=False,
  formula1='"Locus confirmed,Locus corrected,Wrong source - remove,Reclassify as Synthesized,Add a source,Not sure - discuss"')
ws.add_data_validation(dv2); dv2.add('M2:M%d' % MAP_LAST)
dv3 = DataValidation(type='list', allow_blank=True, showDropDown=False,
  formula1='"Adopted,Adapted,Corroborating,Synthesized,Institutional,Unsupported"')
ws.add_data_validation(dv3); dv3.add('I2:I%d' % MAP_LAST)
ws.freeze_panes = 'D2'; ws.auto_filter.ref = 'A1:O%d' % MAP_LAST

# ---- 3. Findings
ws = wb.create_sheet('3. Findings')
H = ['ID','Finding','Sources','Capabilities affected','Severity','What we found',
     'Recommended action','Your decision','Your notes']
W = [7,52,16,26,11,86,80,22,44]
head(ws, H, W)
SEV = {'Critical': RED, 'High': AMBER, 'Medium': 'FFFFF2CC', 'Low': GREY}
r = 2
for f in FINDINGS:
    vals = list(f[:5]) + [f[5], f[6], '', '']
    vals = [f[0], f[1], f[2], f[3], f[4], f[5], f[6], '', '']
    for i, v in enumerate(vals, 1):
        c = ws.cell(r, i, v)
        c.font = Font(name=ARIAL, size=10, bold=(i == 2))
        c.border = BORD
        c.alignment = Alignment(wrap_text=True, vertical='top')
    ws.cell(r, 5).fill = PatternFill('solid', fgColor=SEV[f[4]])
    ws.cell(r, 5).font = Font(name=ARIAL, size=10, bold=True)
    for i in (8, 9):
        ws.cell(r, i).fill = PatternFill('solid', fgColor=YELLOW)
    r += 1
FIND_LAST = r - 1
dv4 = DataValidation(type='list', allow_blank=True, showDropDown=False,
  formula1='"Accept - I will action,Accept - you action,Disagree,Defer,Not sure - discuss"')
ws.add_data_validation(dv4); dv4.add('H2:H%d' % FIND_LAST)
ws.freeze_panes = 'B2'; ws.auto_filter.ref = 'A1:I%d' % FIND_LAST

# ---- 4. Scales
ws = wb.create_sheet('4. Scales')
ws.column_dimensions['A'].width = 3
ws.column_dimensions['B'].width = 22
ws.column_dimensions['C'].width = 108
r = 1
ws.cell(r, 2, 'Derivation - how a capability relates to a source').font = Font(name=ARIAL, size=13, bold=True, color=NAVY)
r += 2
for k, v in DERIV_DEFS:
    ws.cell(r, 2, k).font = Font(name=ARIAL, size=10, bold=True)
    c = ws.cell(r, 3, v); c.font = Font(name=ARIAL, size=10)
    c.alignment = Alignment(wrap_text=True, vertical='top')
    ws.row_dimensions[r].height = 14 + 14 * (len(v) // 108)
    r += 1
r += 2
ws.cell(r, 2, 'Evidence grade - whether a reviewer can check it').font = Font(name=ARIAL, size=13, bold=True, color=NAVY)
r += 2
for k, v in GRADE_DEFS:
    cc = ws.cell(r, 2, k)
    cc.font = Font(name=ARIAL, size=12, bold=True)
    cc.fill = PatternFill('solid', fgColor=GRADE_FILL[k])
    cc.alignment = Alignment(horizontal='center')
    c = ws.cell(r, 3, v); c.font = Font(name=ARIAL, size=10)
    c.alignment = Alignment(wrap_text=True, vertical='top')
    ws.row_dimensions[r].height = 14 + 14 * (len(v) // 108)
    r += 1
r += 2
ws.cell(r, 2, 'Locus status').font = Font(name=ARIAL, size=13, bold=True, color=NAVY)
r += 2
for k, v in (('stated in our own citation','The model already named the part of the source - e.g. "AWS CAF-AI - Business perspective". Still worth confirming, but it was a deliberate choice at the time.'),
             ('candidate - unverified','I inferred which part of the source the capability rests on, from the source structure verified on ' + P.ACCESS_DATE + '. Not checked against the text. Confirm or correct.'),
             ('NOT PINNED','No candidate could be offered - usually because the source has no enumerable structure, or is one we cannot open. These need a decision, not a confirmation.')):
    ws.cell(r, 2, k).font = Font(name=ARIAL, size=10, bold=True)
    c = ws.cell(r, 3, v); c.font = Font(name=ARIAL, size=10)
    c.alignment = Alignment(wrap_text=True, vertical='top')
    ws.row_dimensions[r].height = 14 + 14 * (len(v) // 108)
    r += 1
ws.sheet_view.showGridLines = False

# ---- 5. Coverage
ws = wb.create_sheet('5. Coverage')
H = ['Domain','Domain name','Capabilities','Citations','Citations on A','Citations on B',
     'Citations on C','Citations on D','Citations not pinned','Citations marked Synthesized',
     'Citations marked Unsupported']
W = [8,44,12,11,11,11,11,11,13,15,15]
head(ws, H, W)
r = 2
NCAP = {d[0]: len(d[3]) for d in M}
for d in M:
    did = d[0]
    ws.cell(r, 1, did); ws.cell(r, 2, d[1]); ws.cell(r, 3, NCAP[did])
    m = "'2. Capability to source'!"
    ws.cell(r, 4, '=COUNTIF(%s$A$2:$A$400,$A%d)' % (m, r))
    for col, (rng, val) in enumerate([('$J','A'),('$J','B'),('$J','C'),('$J','D'),
                                      ('$H','NOT PINNED'),('$I','Synthesized'),('$I','Unsupported')], 5):
        ws.cell(r, col, '=COUNTIFS(%s$A$2:$A$400,$A%d,%s%s$2:%s$400,"%s")'
                % (m, r, m, rng, rng, val))
    for i in range(1, 12):
        c = ws.cell(r, i); c.font = Font(name=ARIAL, size=10, bold=(i == 1))
        c.border = BORD; c.alignment = Alignment(wrap_text=True, vertical='top')
        if i >= 3: c.alignment = Alignment(horizontal='center')
    r += 1
TOT = r
ws.cell(r, 2, 'Total').font = Font(name=ARIAL, size=10, bold=True)
for i in range(3, 12):
    L = get_column_letter(i)
    c = ws.cell(r, i, '=SUM(%s2:%s%d)' % (L, L, r-1))
    c.font = Font(name=ARIAL, size=10, bold=True)
    c.border = BORD; c.alignment = Alignment(horizontal='center')
ws.cell(r, 1).border = BORD; ws.cell(r, 2).border = BORD
r += 2
note = ('Read the D column and the Unsupported column first. A domain whose evidence sits mostly in C '
        'and D is not weakly assessed - it is unassessable by anyone outside the Bank, which is a '
        'different and worse problem. D7 is the domain where that matters most, because it is the one '
        'Internal Audit will open first.')
c = ws.cell(r, 2, note); c.font = Font(name=ARIAL, size=10, italic=True)
c.alignment = Alignment(wrap_text=True, vertical='top')
ws.merge_cells(start_row=r, start_column=2, end_row=r+2, end_column=11)
ws.freeze_panes = 'C2'

wb.save(OUT)
print('written', OUT)
print('sources', len(P.SOURCES), 'pairs', len(PAIRS), 'findings', len(FINDINGS))

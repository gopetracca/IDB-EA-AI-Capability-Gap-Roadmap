# -*- coding: utf-8 -*-
"""Realization & Readiness workbook — 12 sheets, rebuilt clean."""
import json, io, collections
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, Protection
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.hyperlink import Hyperlink
from openpyxl.formatting.rule import CellIsRule

D = {}; exec(io.open('wb_data.py', encoding='utf-8').read(), D)
A = {}; exec(io.open('wb_assets.py', encoding='utf-8').read(), A)
M = json.load(open('model3.json'))
C = {}; exec(io.open('catalog4.py', encoding='utf-8').read(), C); CAT = C['S']
OBL = json.load(open('obligations.json'))
GV = {}
exec(io.open('gen_trm.py', encoding='utf-8').read().split('CAPJSON =')[0]
     .replace("exec(io.open('catalog4.py', encoding='utf-8').read())", ""), GV)

L2 = [(d, c) for d in M for c in d[3]]
L3TOL2 = {x[0]: c[0] for d in M for c in d[3] for x in c[4]}
CATE = [(g, s) for g in CAT for s in g[4]]
N2 = len(L2)

F = "Arial"; INK = "0E1A21"; ACC = "1B4A63"
H  = Font(name=F, size=10, bold=True, color="FFFFFF")
B  = Font(name=F, size=10, bold=True, color=INK)
T  = Font(name=F, size=10, color=INK)
TS = Font(name=F, size=9,  color="55666F")
IN = Font(name=F, size=10, bold=True, color="0000FF")
LK = Font(name=F, size=10, color="008000")
TITLE = Font(name=F, size=15, bold=True, color=ACC)
HDR = PatternFill("solid", fgColor=ACC); BAND = PatternFill("solid", fgColor="F2F6F8")
INPUT = PatternFill("solid", fgColor="FFF6CC"); NOTE = PatternFill("solid", fgColor="EDF2F5")
WARN = PatternFill("solid", fgColor="F4DCD8")
thin = Side(style="thin", color="CFD8DE"); BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(vertical="top", wrap_text=True); TOP = Alignment(vertical="top")
CTR = Alignment(horizontal="center", vertical="center")
MHEAT = {1:"8E3226", 2:"9E5A21", 3:"C9AE4A", 4:"3F6F32", 5:"25583F"}
RHEAT = {0:"C3CCD3", 1:"8E3226", 2:"9E5A21", 3:"C9AE4A", 4:"3F6F32", 5:"25583F"}

wb = Workbook(); wb.remove(wb.active)

# row each capability's criteria block will occupy on sheet 6 (header row 1, then 1 hdr + n criteria each)
CRITROW = {}
_rr = 2
for _d, _c in L2:
    CRITROW[_c[0]] = _rr
    _rr += 1 + len(_c[4])
def head(ws, hs, ws_, row=1):
    for i, (h_, w) in enumerate(zip(hs, ws_), 1):
        c = ws.cell(row=row, column=i, value=h_); c.font = H; c.fill = HDR; c.border = BOX
        c.alignment = Alignment(vertical="center", wrap_text=True)
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[row].height = 32
def note(ws, row, ncols, text, h=44):
    c = ws.cell(row=row, column=1, value=text); c.font = TS; c.alignment = WRAP; c.fill = NOTE
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=ncols)
    ws.row_dimensions[row].height = h

# ============================================================ 0. Read me
ws = wb.create_sheet("0. Read me"); ws.sheet_view.showGridLines = False
for i, w in enumerate([3, 30, 104], 1): ws.column_dimensions[get_column_letter(i)].width = w
rows = [
 ("T","Enterprise AI Capability Model",""),
 ("S","Realization & Readiness · v0.5 · %d capabilities · %d criteria · %d catalog entries" %
     (N2, sum(len(c[4]) for _, c in L2), len(CATE)), ""),
 ("","",""),
 ("H","The one rule that keeps this model honest",""),
 ("P","Two scales, never merged","A CAPABILITY carries MATURITY: is the institution able to do this, to what standard, with what evidence? A REALIZATION carries READINESS: has the enterprise packaged this well enough to consume? They measure different things and are never combined into a single number."),
 ("P","The gap is the finding","A capability can be readiness 4 and maturity 2 - the product is well packaged and the institution still cannot do the thing to the standard it needs. That combination is common, and it is invisible to any model carrying only one number."),
 ("W","Never do this","Never write a readiness level into the capability catalog. 'Semantic retrieval: readiness 4 via Azure AI Search' is a true statement about SUPPLY that silently substitutes for the maturity question. Both numbers or neither."),
 ("","",""),
 ("H","Three catalogs",""),
 ("P","1 · Capability","One row per L2 capability. Maturity, owner, target. No products, nothing below L2, no readiness."),
 ("P","2 · Realization","One row per capability x pattern x technology. Readiness, consumption model, status, preferred. This is where the architecture goes."),
 ("P","3 · Enablement","One row per realization x control. Evidence ticks. Replaces argument about whether a capability is 'had' with a list of things that either exist or do not."),
 ("","",""),
 ("H","Grain - the mistake to avoid",""),
 ("P","Sheet 1 rows are L2","Semantic retrieval, lexical retrieval and retrieval ranking are CATALOG entries (S3.2, S3.1, S3.4), not capabilities: they share an owner and fail the one-owner test. Put them in sheet 1 and the catalog grows from 50 rows to several hundred."),
 ("","",""),
 ("H","Cell conventions",""),
 ("Y","Yellow fill, blue bold","Your input. The only cells to edit."),
 ("K","Black","Fixed reference content. Changing it breaks the link to the published model."),
 ("G","Green","Formula, linked from another sheet."),
 ("","",""),
 ("H","What is not done yet",""),
 ("P","Rubrics","One worked rubric exists (sheet 11). Until a capability has one, its maturity rating is provisional and must be labelled so."),
 ("P","Control mapping","ISO/IEC 42001 Annex A and NIST AI RMF outcomes are not mapped onto capabilities. Carve D7 out of any approval request until they are."),
 ("P","Anchors","New / Specialization / Lens are hypotheses with a confidence, unverified until the institution's existing capability map is crosswalked."),
 ("P","Legal applicability","Statutory references sit in sheet 10, all marked candidate. Nothing here asserts that any regulation binds the institution."),
]
r = 1
for k, a, b in rows:
    if k == "T":
        ws.cell(row=r, column=2, value=a).font = TITLE
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3); ws.row_dimensions[r].height = 22
    elif k == "S":
        ws.cell(row=r, column=2, value=a).font = TS
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
    elif k == "H":
        c = ws.cell(row=r, column=2, value=a); c.font = Font(name=F, size=11, bold=True, color=ACC)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3); ws.row_dimensions[r].height = 20
    elif k in ("P","Y","K","G","W"):
        c1 = ws.cell(row=r, column=2, value=a); c1.font = B; c1.alignment = TOP
        c2 = ws.cell(row=r, column=3, value=b); c2.font = T; c2.alignment = WRAP
        if k == "Y": c1.fill = INPUT; c1.font = IN
        if k == "G": c1.font = LK
        if k == "W": c1.font = Font(name=F, size=10, bold=True, color="8E3226"); c2.fill = WARN
        ws.row_dimensions[r].height = max(14, 12.6 * (1 + len(b) // 100))
    r += 1

# ============================================================ 1. Capability catalog
ws = wb.create_sheet("1. Capability catalog")
head(ws, ["Domain","ID","Capability","Definition","Accountable owner","Anchor","Conf.","Agentic",
          "Criteria","Criterion IDs","MATURITY now","MATURITY target","Best readiness","Gap: why maturity trails",
          "Evidence ref","Notes"],
         [8,7,34,50,26,15,8,8,9,17,13,14,12,50,26,32])
CAPROW = {}
for i, (d, c) in enumerate(L2):
    r = i + 2; CAPROW[c[0]] = r
    ag = "Yes" if (len(c) > 5 and c[5]) or any(len(x) > 3 and x[3] for x in c[4]) else ""
    anchor = {"new":"New","specialization":"Specialization","lens":"Lens - keep existing node"}[c[6]]
    crange = ("%s - %s" % (c[4][0][0], c[4][-1][0])) if c[4] else ""
    vals = [d[0], c[0], c[1], c[2], c[7], anchor, c[8], ag, len(c[4]), crange, None, None,
            '=IF(COUNTIF(\'2. Realization catalog\'!$B$2:$B$500,$B{0})=0,"",'
            'SUMPRODUCT(MAX((\'2. Realization catalog\'!$B$2:$B$500=$B{0})*'
            '(\'2. Realization catalog\'!$H$2:$H$500))))'.format(r),
            None, None, None]
    for j, v in enumerate(vals, 1):
        cell = ws.cell(row=r, column=j, value=v); cell.border = BOX; cell.font = T
        cell.alignment = WRAP if j in (3,4,5,14,15,16) else (CTR if j in (6,7,8,9,10,11,12,13) else TOP)
        if j == 2: cell.font = Font(name=F, size=10, bold=True, color=ACC)
        if j == 3: cell.font = B
        if j == 4: cell.font = TS
        if j == 6 and c[6] == "lens": cell.font = Font(name=F, size=9, bold=True, color="9E5A21")
        if j == 7 and c[8] == "low": cell.font = Font(name=F, size=9, bold=True, color="9E5A21")
        if j == 10 and c[4]:
            cell.font = Font(name=F, size=9, color="0000EE", underline="single")
            cell.hyperlink = Hyperlink(ref="J%d" % r, location="'6. Criteria (L3)'!B%d" % (CRITROW[c[0]]),
                                       tooltip="Jump to this capability's criteria")
        if j in (11,12,14,15,16):
            cell.fill = INPUT; cell.font = IN if j in (11,12) else T
            cell.protection = Protection(locked=False)
        if j == 13: cell.font = LK
    ws.row_dimensions[r].height = 30
CAP_LAST = N2 + 1
dvm = DataValidation(type="list", formula1='"1,2,3,4,5,0,NE,UC,NA"', allow_blank=True,
    showErrorMessage=True, errorTitle="Maturity",
    error="1-5, or a state: 0 Absent / NE not evidenced / UC under clarification / NA not applicable. See sheet 4.")
ws.add_data_validation(dvm); dvm.add("K2:L%d" % CAP_LAST)
for lvl, hx in MHEAT.items():
    ws.conditional_formatting.add("K2:K%d" % CAP_LAST,
        CellIsRule(operator="equal", formula=[str(lvl)], fill=PatternFill("solid", fgColor=hx),
                   font=Font(name=F, size=10, bold=True, color="2A2200" if lvl == 3 else "FFFFFF")))
for lvl, hx in RHEAT.items():
    ws.conditional_formatting.add("M2:M%d" % CAP_LAST,
        CellIsRule(operator="equal", formula=[str(lvl)], fill=PatternFill("solid", fgColor=hx),
                   font=Font(name=F, size=10, bold=True, color="2A2200" if lvl == 3 else ("FFFFFF" if lvl else INK))))
ws.freeze_panes = "D2"; ws.auto_filter.ref = "A1:P%d" % CAP_LAST
ws.protection.sheet = True; ws.protection.autoFilter = False; ws.protection.sort = False
note(ws, CAP_LAST + 2, 16,
 "MATURITY only. Column J links to the criteria. Best readiness in column M is pulled from sheet 2 for comparison - it is NOT a property of the capability and must never be edited here. Where M exceeds K, column N must say why: that gap is the finding. Rows are L2, one accountable owner each; nothing below L2 belongs here.", 46)

# ============================================================ 2. Realization catalog
ws = wb.create_sheet("2. Realization catalog")
head(ws, ["Realization ID","Capability","Also realizes","Pattern (PAT / ABB)","Technology (SBB)",
          "Supporting building blocks","Operated by","READINESS","Evidence-implied","Consumption model",
          "Status","Preferred","Enterprise assets","Does not provide","Note"],
         [13,10,14,36,24,34,26,11,13,20,12,10,30,40,54])
ENB = "'3. Enablement evidence'!"
def realrow(r, d_):
    vals = [d_["id"], d_["cap"], d_["also"], d_["pattern"], d_["tech"], d_["support"],
            d_["operated"], d_["readiness"],
            ('=IF(COUNTIFS({0}$A$2:$A$400,$A{1},{0}$D$2:$D$400,"Generic")=0,"",'
             'IF(COUNTIFS({0}$A$2:$A$400,$A{1},{0}$D$2:$D$400,"Generic",{0}$G$2:$G$400,"Yes")'
             '+COUNTIFS({0}$A$2:$A$400,$A{1},{0}$D$2:$D$400,"Generic",{0}$G$2:$G$400,"No")'
             '+COUNTIFS({0}$A$2:$A$400,$A{1},{0}$D$2:$D$400,"Generic",{0}$G$2:$G$400,"Partial")=0,"no evidence",'
             'IF(COUNTIFS({0}$A$2:$A$400,$A{1},{0}$D$2:$D$400,"Generic",{0}$G$2:$G$400,"Yes")'
             '+COUNTIFS({0}$A$2:$A$400,$A{1},{0}$D$2:$D$400,"Generic",{0}$G$2:$G$400,"No")'
             '+COUNTIFS({0}$A$2:$A$400,$A{1},{0}$D$2:$D$400,"Generic",{0}$G$2:$G$400,"Partial")'
             '<COUNTIFS({0}$A$2:$A$400,$A{1},{0}$D$2:$D$400,"Generic"),'
             '"incomplete "&COUNTIFS({0}$A$2:$A$400,$A{1},{0}$D$2:$D$400,"Generic",{0}$G$2:$G$400,"Yes")'
             '&"/"&COUNTIFS({0}$A$2:$A$400,$A{1},{0}$D$2:$D$400,"Generic"),'
             'IF(COUNTIFS({0}$A$2:$A$400,$A{1},{0}$D$2:$D$400,"Generic",{0}$G$2:$G$400,"Yes")>=8,4,'
             'IF(AND(COUNTIFS({0}$A$2:$A$400,$A{1},{0}$C$2:$C$400,"Published standard",{0}$G$2:$G$400,"Yes")=1,'
             'COUNTIFS({0}$A$2:$A$400,$A{1},{0}$C$2:$C$400,"Architecture pattern document",{0}$G$2:$G$400,"Yes")'
             '+COUNTIFS({0}$A$2:$A$400,$A{1},{0}$C$2:$C$400,"Reference architecture",{0}$G$2:$G$400,"Yes")>=1),3,'
             'IF(COUNTIFS({0}$A$2:$A$400,$A{1},{0}$D$2:$D$400,"Generic",{0}$G$2:$G$400,"Yes")>=1,2,1))))))'
             ).format(ENB, r),
            d_["consumption"], d_["status"], d_["preferred"],
            ", ".join(A["ASSET_LINK"].get(d_["id"], [])), d_["notprov"], d_["note"]]
    for j, v in enumerate(vals, 1):
        cell = ws.cell(row=r, column=j, value=v); cell.border = BOX; cell.font = T
        cell.alignment = WRAP if j in (4,5,6,7,10,13,14,15) else (CTR if j in (8,9,12) else TOP)
        if j == 1: cell.font = Font(name=F, size=10, bold=True, color=ACC)
        if j == 9: cell.font = LK
        if j == 13: cell.font = Font(name=F, size=9, color=ACC)
        if j in (14,15): cell.font = TS
        if j in (3,4,5,6,7,8,10,11,12,14):
            cell.fill = INPUT; cell.font = IN if j in (8,) else T
            cell.protection = Protection(locked=False)
    if not d_["conf"]:
        for j in (1,2,4,5): ws.cell(row=r, column=j).font = Font(name=F, size=10, italic=True, color="7E8E97")
    ws.row_dimensions[r].height = 46 if d_["note"] else 26

r = 2
for d_ in D["REAL"]:
    realrow(r, d_); r += 1
FIRST_CAND = r
seen = set()
for g, s in CATE:
    if s[6] != "SVC": continue
    caps = sorted({L3TOL2.get(x, x) for x, _ in s[4]})
    cap = caps[0] if caps else ""
    realrow(r, dict(id="REAL-%03d" % (200 + r - FIRST_CAND), conf=False, cap=cap,
                    also=", ".join(caps[1:]), pattern=s[0] + " " + s[1], tech="", support="",
                    operated="", readiness=None, consumption="", status="Candidate",
                    preferred="", notprov="", note=""))
    r += 1
REAL_LAST = r - 1
dvr = DataValidation(type="list", formula1='"0,1,2,3,4,5"', allow_blank=True, showErrorMessage=True,
    errorTitle="Readiness", error="0 Not available / 1 Available or project-proven / 2 Approved / 3 Standardized / 4 Industrialized / 5 Productized. See sheet 4.")
ws.add_data_validation(dvr); dvr.add("H2:H%d" % REAL_LAST)
dvc = DataValidation(type="list", formula1='"%s"' % ",".join(k for k, _ in D["CONSUMPTION"]), allow_blank=True)
ws.add_data_validation(dvc); dvc.add("J2:J%d" % REAL_LAST)
dvst = DataValidation(type="list", formula1='"Approved,Conditional,Candidate,Retiring,Not available"', allow_blank=True)
ws.add_data_validation(dvst); dvst.add("K2:K%d" % REAL_LAST)
dvp = DataValidation(type="list", formula1='"Y,N"', allow_blank=True)
ws.add_data_validation(dvp); dvp.add("L2:L%d" % REAL_LAST)
for lvl, hx in RHEAT.items():
    ws.conditional_formatting.add("H2:H%d" % REAL_LAST,
        CellIsRule(operator="equal", formula=[str(lvl)], fill=PatternFill("solid", fgColor=hx),
                   font=Font(name=F, size=10, bold=True, color="2A2200" if lvl == 3 else ("FFFFFF" if lvl else INK))))
ws.freeze_panes = "D2"; ws.auto_filter.ref = "A1:O%d" % REAL_LAST
note(ws, REAL_LAST + 2, 15,
 "One row per capability x pattern x technology. A technology appears on as many rows as it realizes patterns - that is correct, and a two-tier model cannot express it. "
 "Column I recomputes readiness from the GENERIC evidence rows on sheet 3 and reports 'incomplete n/9' until all nine are answered; where it then disagrees with column H the claim is not carried by the evidence. "
 "REAL-001 to REAL-008 are populated from the actual IDB asset inventory on sheet 12. REAL-005 is the row to settle first: it decides whether capability 3.6 carries a readiness lead of 2 or of 0.", 62)

# ============================================================ 3. Enablement evidence
ws = wb.create_sheet("3. Enablement evidence")
head(ws, ["Realization ID","Realization","Control","Type","Reference block","Capability",
          "Status","Why it matters","Evidence ref","Owner"],
         [13,40,54,17,14,11,11,62,26,22])
RNAME = {d_["id"]: (d_["pattern"] + (" / " + d_["tech"] if d_["tech"] else "")) for d_ in D["REAL"]}
r = 2
for d_ in D["REAL"]:
    rid = d_["id"]

    pre = d_.get("prefill", {})
    for name, why in D["GENERIC_ASSETS"]:
        for j, v in enumerate([rid, RNAME[rid], name, "Generic", "", "",
                               pre.get(name), why, None, None], 1):
            cell = ws.cell(row=r, column=j, value=v); cell.border = BOX; cell.font = T
            cell.alignment = WRAP if j in (2,3,8) else (CTR if j in (4,7) else TOP)
            if j == 1: cell.font = Font(name=F, size=10, bold=True, color=ACC)
            if j == 8: cell.font = TS
            if j in (7,9,10):
                cell.fill = INPUT; cell.font = IN if j == 7 else T
                cell.protection = Protection(locked=False)
        ws.row_dimensions[r].height = 24; r += 1
    for name, ref, cap, why in D["CONTROLS_BY_REAL"].get(rid, []):
        for j, v in enumerate([rid, RNAME[rid], name, "Pattern-specific", ref, cap, None, why, None, None], 1):
            cell = ws.cell(row=r, column=j, value=v); cell.border = BOX; cell.font = T
            cell.alignment = WRAP if j in (2,3,8) else (CTR if j in (4,5,6,7) else TOP)
            if j == 1: cell.font = Font(name=F, size=10, bold=True, color=ACC)
            if j == 3: cell.font = B
            if j == 4: cell.font = Font(name=F, size=9, bold=True, color=ACC)
            if j == 8: cell.font = TS
            if j in (7,9,10):
                cell.fill = INPUT; cell.font = IN if j == 7 else T
                cell.protection = Protection(locked=False)
        ws.row_dimensions[r].height = 32; r += 1
ENB_LAST = r - 1
dve = DataValidation(type="list", formula1='"Yes,No,Partial,Unknown"', allow_blank=True)
ws.add_data_validation(dve); dve.add("G2:G%d" % ENB_LAST)
for val, hx, fc in [("Yes","3F6F32","FFFFFF"), ("No","8E3226","FFFFFF"),
                    ("Partial","C9AE4A","2A2200"), ("Unknown","C3CCD3",INK)]:
    ws.conditional_formatting.add("G2:G%d" % ENB_LAST,
        CellIsRule(operator="equal", formula=['"%s"' % val], fill=PatternFill("solid", fgColor=hx),
                   font=Font(name=F, size=10, bold=True, color=fc)))
ws.freeze_panes = "C2"; ws.auto_filter.ref = "A1:J%d" % ENB_LAST
note(ws, ENB_LAST + 2, 10,
 "GENERIC rows mostly tick together and carry little information once a realization reaches readiness 4. PATTERN-SPECIFIC rows are the ones that stay unticked, and the reason to read this sheet at all. An inherited control that cannot be skipped is stronger evidence than a procurement approval. Every 'No' on a pattern-specific row is a roadmap item - and a cheap one where the building block already exists: you are extending a module, not building a platform.", 52)

# ============================================================ 4. Scales
ws = wb.create_sheet("4. Scales"); ws.sheet_view.showGridLines = False
head(ws, ["", "Level", "Name", "Meaning", "Evidence that establishes it"], [3, 9, 26, 66, 62])
r = 2
def block(title, rows_, heat, ncol=5):
    global r
    c = ws.cell(row=r, column=2, value=title); c.font = Font(name=F, size=12, bold=True, color=ACC)
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=ncol); ws.row_dimensions[r].height = 22
    r += 1
    for row in rows_:
        n, nm, dfn, ev = row
        c1 = ws.cell(row=r, column=2, value=n); c1.alignment = CTR
        fill = heat.get(n) if heat else None
        c1.font = Font(name=F, size=11, bold=True, color=("2A2200" if n == 3 else "FFFFFF") if fill else ACC)
        c1.fill = PatternFill("solid", fgColor=fill) if fill else PatternFill("solid", fgColor="DEE9EF")
        ws.cell(row=r, column=3, value=nm).font = B
        ws.cell(row=r, column=4, value=dfn).font = T
        ws.cell(row=r, column=5, value=ev).font = TS
        for j in range(2, 6):
            cell = ws.cell(row=r, column=j); cell.border = BOX
            if j > 2: cell.alignment = WRAP
        ws.row_dimensions[r].height = 38
        r += 1
    r += 1
block("MATURITY - attaches to a capability. Evidence-gated. Owner: the accountable capability owner. Clock: 5-10 years.",
      D["MATURITY"], MHEAT)
block("Maturity states - not levels. They never enter arithmetic.", D["MAT_STATES"], None)
block("READINESS - attaches to a realization. Structural, read off by inspection. Owner: the platform. Clock: quarterly.",
      D["READINESS"], RHEAT)
c = ws.cell(row=r, column=2, value="Two questions settle every readiness row: is there a reusable building block separable from any one application (2 vs 3-4), and who operates the instances (4 vs 5)? Level 5 is not the target everywhere - agent runtimes are per-use-case by nature, 4 is the correct destination and the improvement path is enriching what comes in the box.")
c.font = TS; c.alignment = WRAP; c.fill = NOTE
ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=5); ws.row_dimensions[r].height = 40
r += 2
c = ws.cell(row=r, column=2, value="CONSUMPTION MODEL - what the consuming team still has to build. Recorded on the realization, not the capability.")
c.font = Font(name=F, size=12, bold=True, color=ACC)
ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=5); ws.row_dimensions[r].height = 22
r += 1
for nm, dfn in D["CONSUMPTION"]:
    ws.cell(row=r, column=2, value="").border = BOX
    ws.cell(row=r, column=3, value=nm).font = B
    ws.cell(row=r, column=4, value=dfn).font = T
    for j in range(2, 6):
        cell = ws.cell(row=r, column=j); cell.border = BOX; cell.alignment = WRAP
    ws.row_dimensions[r].height = 20; r += 1
r += 1
c = ws.cell(row=r, column=2, value="This column settles the recurring disagreement - 'a capability means I do not have to build it' - without redefining the word capability. That belief is about CONSUMPTION MODEL. Record it as one and the argument stops being definitional.")
c.font = TS; c.alignment = WRAP; c.fill = NOTE
ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=5); ws.row_dimensions[r].height = 34

# ============================================================ 5. Gap & roadmap
ws = wb.create_sheet("5. Gap & roadmap")
head(ws, ["Domain","ID","Capability","Owner","Maturity now","Target","Maturity gap",
          "Best readiness","Readiness lead","Lane","Why maturity trails","Anchor"],
         [8,7,36,26,12,9,11,13,13,24,50,15])
CAP = "'1. Capability catalog'!"
for i, (d, c) in enumerate(L2):
    r = i + 2; s = CAPROW[c[0]]
    vals = [d[0], c[0], c[1], "={0}E{1}".format(CAP, s),
            "={0}K{1}".format(CAP, s), "={0}L{1}".format(CAP, s),
            '=IF(AND(ISNUMBER({0}K{1}),ISNUMBER({0}L{1})),MAX(0,{0}L{1}-{0}K{1}),"")'.format(CAP, s),
            "={0}M{1}".format(CAP, s),
            '=IF(AND(ISNUMBER({0}K{1}),ISNUMBER({0}M{1})),{0}M{1}-{0}K{1},"")'.format(CAP, s),
            '=IF({0}K{1}="","not rated",IF(NOT(ISNUMBER({0}K{1})),'
            'IF({0}K{1}="UC","Blocked - applicability",IF({0}K{1}="NE","Blocked - no evidence","Out of scope")),'
            'IF(G{2}>=2,IF(OR($A{2}="D7",$A{2}="D3"),"Mandatory / urgent","Foundational / enabling"),'
            'IF(G{2}=1,"Value-led","Deferred / monitor"))))'.format(CAP, s, r),
            "={0}N{1}".format(CAP, s), "={0}F{1}".format(CAP, s)]
    for j, v in enumerate(vals, 1):
        cell = ws.cell(row=r, column=j, value=v); cell.border = BOX; cell.font = LK if j > 3 else T
        cell.alignment = WRAP if j in (3,4,10,11,12) else (CTR if j in (5,6,7,8,9) else TOP)
        if j == 2: cell.font = Font(name=F, size=10, bold=True, color=ACC)
        if j == 3: cell.font = B
    ws.row_dimensions[r].height = 26
ws.conditional_formatting.add("I2:I%d" % CAP_LAST,
    CellIsRule(operator="greaterThanOrEqual", formula=["2"], fill=PatternFill("solid", fgColor="F4DCD8"),
               font=Font(name=F, size=10, bold=True, color="8E3226")))
ws.freeze_panes = "D2"; ws.auto_filter.ref = "A1:L%d" % CAP_LAST
note(ws, CAP_LAST + 2, 12,
 "Column I is the READINESS LEAD: how far supply has run ahead of the institution's ability to use it. A positive lead with an empty column K is an unexplained claim - the product is packaged and nobody has said why the capability still trails. Priority is a governed decision, not a subtraction: a three-level gap can be low priority and a one-level gap can be urgent. Lanes are a starting proposal; a Priority Decision record settles each one.", 50)

# ============================================================ 6. Criteria (L3)
ws = wb.create_sheet("6. Criteria (L3)")
head(ws, ["Domain","Capability ID","Capability","Criterion ID","Criterion","Definition","Agentic",
          "Mandatory / conditional / enhancing","Applicability trigger","Evidence type","Owner"],
     [8,11,30,10,38,66,8,26,26,24,22])
ws.sheet_properties.outlinePr.summaryBelow = False
CAPHDR = PatternFill("solid", fgColor="DEE9EF")
r = 2
for d, c in L2:
    # one collapsible header per capability, its criteria grouped beneath it
    for j, v in enumerate([d[0], c[0], c[1], "", "%d criteria" % len(c[4]), c[7], "", "", "", "", ""], 1):
        cell = ws.cell(row=r, column=j, value=v); cell.border = BOX; cell.fill = CAPHDR
        cell.font = Font(name=F, size=10, bold=True, color=ACC if j == 2 else INK)
        cell.alignment = WRAP if j == 3 else TOP
    ws.row_dimensions[r].height = 20
    r += 1
    for x in c[4]:
        vals = [d[0], c[0], c[1], x[0], x[1], x[2], "Yes" if len(x) > 3 and x[3] else "",
                None, None, None, None]
        for j, v in enumerate(vals, 1):
            cell = ws.cell(row=r, column=j, value=v); cell.border = BOX; cell.font = T
            cell.alignment = WRAP if j in (3,5,6,8,9,10) else (CTR if j == 7 else TOP)
            if j == 4: cell.font = Font(name=F, size=10, bold=True, color=ACC)
            if j == 5: cell.font = B
            if j == 6: cell.font = TS
            if j >= 8:
                cell.fill = INPUT; cell.font = T; cell.protection = Protection(locked=False)
        ws.row_dimensions[r].height = 26
        ws.row_dimensions[r].outlineLevel = 1
        r += 1
CRIT_LAST = r - 1
dvt = DataValidation(type="list", formula1='"mandatory,conditional,enhancing"', allow_blank=True)
ws.add_data_validation(dvt); dvt.add("H2:H%d" % CRIT_LAST)
ws.freeze_panes = "E2"; ws.auto_filter.ref = "A1:K%d" % CRIT_LAST
note(ws, CRIT_LAST + 2, 11,
 "All %d criteria, grouped under their capability. Use the +/- outline handles in the left margin to collapse a capability, or filter column B to one capability ID. Criteria are not yet typed mandatory / conditional / enhancing - until they are, the maturity gates on sheet 11 cannot be evaluated and every rating is provisional." % sum(len(c[4]) for _, c in L2), 34)

# ============================================================ 7. Reference catalog
ws = wb.create_sheet("7. Reference catalog")
head(ws, ["Group","Group name","ID","Entry","Kind","Either?","Domain","Element","Facets",
          "Standard","Definition","Provenance","Typed edges","Agentic","Reg."],
         [7,24,8,32,8,8,13,20,17,11,54,50,28,8,9])
r = 2
for g, s in CATE:
    fl = s[5] if len(s) > 5 else ""
    vals = [g[0], g[1], s[0], s[1], s[6], "either" if s[11] else "", s[7], s[8].replace("_", " "),
            ", ".join(s[9]) or "-", ", ".join(s[10]) or "-", s[2], " · ".join(s[3]),
            ", ".join("%s (%s)" % (a_, b_) for a_, b_ in s[4]) or "-",
            "Yes" if fl == "a" else "", "Elevated" if fl == "r" else ""]
    for j, v in enumerate(vals, 1):
        cell = ws.cell(row=r, column=j, value=v); cell.border = BOX; cell.font = T
        cell.alignment = WRAP if j in (2,4,9,11,12,13) else (CTR if j in (5,6,14,15) else TOP)
        if j == 3: cell.font = Font(name=F, size=10, bold=True, color=ACC)
        if j == 4: cell.font = B
        if j == 5: cell.font = Font(name=F, size=9, bold=True,
                    color={"PAT":ACC, "STD":"9E5A21", "SVC":"3F6F32"}.get(s[6], INK))
        if j in (6,11,12,13): cell.font = TS
    ws.row_dimensions[r].height = 50; r += 1
CATL = r - 1
ws.freeze_panes = "E2"; ws.auto_filter.ref = "A1:O%d" % CATL
note(ws, CATL + 2, 15,
 "What COULD exist in the AI domain - vendor-neutral, stable, not a statement about this institution. SVC = something a consumer calls. ABB = a piece inside an architecture. PAT = a governed arrangement of blocks. STD = a specification someone else maintains. Entries marked 'either' are genuinely ambiguous: OCR is an ABB when you design a document pipeline and a Service when someone exposes an endpoint. Same concept, two registers - not a conflict. Pick patterns and building blocks from here when you write a row on sheet 2.", 52)

# ============================================================ 8. Matrix A
ws = wb.create_sheet("8. Matrix A")
EDGE = "'9. Typed edges'!"
head(ws, ["Domain","ID","Capability"] + [g[0] for g in CAT] + ["Enabler total","All edges","Blank reason"],
     [8,7,34] + [7]*len(CAT) + [11,9,46])
EXT, HUMAN = GV["EXT"], GV["HUMAN"]
for i, (d, c) in enumerate(L2):
    r = i + 2
    ws.cell(row=r, column=1, value=d[0]).font = T
    ws.cell(row=r, column=2, value=c[0]).font = Font(name=F, size=10, bold=True, color=ACC)
    ws.cell(row=r, column=3, value=c[1]).font = B
    for k, g in enumerate(CAT):
        ws.cell(row=r, column=4 + k,
            value='=SUMIFS({0}$I$2:$I$400,{0}$F$2:$F$400,$B{1},{0}$C$2:$C$400,{2}$1)'.format(
                EDGE, r, get_column_letter(4 + k))).font = LK
    tc = 4 + len(CAT)
    ws.cell(row=r, column=tc, value="=SUM(D{0}:{1}{0})".format(r, get_column_letter(tc - 1))).font = B
    ws.cell(row=r, column=tc + 1,
        value='=SUMIFS({0}$H$2:$H$400,{0}$F$2:$F$400,$B{1})'.format(EDGE, r)).font = LK
    reason = ("Realized by existing enterprise services - " + EXT[c[0]]) if c[0] in EXT else (
             "Organizational capability - no technology realizes it" if c[0] in HUMAN else "")
    tl, al = get_column_letter(tc), get_column_letter(tc + 1)
    ws.cell(row=r, column=tc + 2,
        value='=IF({0}{2}>0,"",IF({1}{2}>0,"Control and evidence support only - the ability itself is organizational",{3}))'.format(
              tl, al, r, '"' + reason.replace('"', '""') + '"' if reason else '"UNEXPLAINED - review"')).font = TS
    for j in range(1, tc + 3):
        cell = ws.cell(row=r, column=j); cell.border = BOX
        cell.alignment = CTR if 4 <= j <= tc + 1 else (WRAP if j in (3, tc + 2) else TOP)
    ws.row_dimensions[r].height = 28
for k, g in enumerate(CAT): ws.cell(row=1, column=4 + k).value = g[0]
ws.freeze_panes = "D2"; ws.auto_filter.ref = "A1:%s%d" % (get_column_letter(6 + len(CAT)), CAP_LAST)
note(ws, CAP_LAST + 2, 6 + len(CAT),
 "Counts are NAVIGATION, not coverage. More edges does not mean better realization - relevance, obligation and sufficiency do. Only required- and optional-enabler edges are counted, because only those assert that the ability depends on the block. Blanks come in four kinds; anything reading UNEXPLAINED is a real finding and should not exist.", 40)

# ============================================================ 9. Typed edges
ws = wb.create_sheet("9. Typed edges")
head(ws, ["Entry ID","Entry","Group","Kind","Edge type","Capability","Criterion ref","Count once",
          "Count once (enabler)"], [10,32,8,8,20,11,13,10,16])
r = 2
for g, s in CATE:
    for ref, et in s[4]:
        l2 = L3TOL2.get(ref, ref)
        for j, v in enumerate([s[0], s[1], g[0], s[6], et, l2, ref], 1):
            cell = ws.cell(row=r, column=j, value=v); cell.border = BOX; cell.font = T
            cell.alignment = WRAP if j == 2 else TOP
            if j in (1, 6, 7): cell.font = Font(name=F, size=10, color=ACC)
            if j == 5: cell.font = Font(name=F, size=9, bold=True, color=ACC)
        ws.cell(row=r, column=8, value='=IF(COUNTIFS($A$2:A{0},A{0},$F$2:F{0},F{0})=1,1,0)'.format(r)).font = LK
        ws.cell(row=r, column=9,
            value='=IF(AND(OR(E{0}="required-enabler",E{0}="optional-enabler"),'
                  'COUNTIFS($A$2:A{0},A{0},$F$2:F{0},F{0},$E$2:E{0},E{0})=1),1,0)'.format(r)).font = LK
        for j in (8, 9):
            cell = ws.cell(row=r, column=j); cell.border = BOX; cell.alignment = CTR
        r += 1
EDG_LAST = r - 1
ws.freeze_panes = "C2"; ws.auto_filter.ref = "A1:I%d" % EDG_LAST

# ============================================================ 10. Obligations
ws = wb.create_sheet("10. Obligations register")
head(ws, ["Applies to","Name","Instrument","Subject","Status","Legal owner","Determination"],
     [14,40,26,50,50,22,30])
FIXED = 0
for i, o in enumerate(OBL):
    r = i + 2
    cap = o["capability"]; nm = o["capability_name"]
    if cap == "1.4" and "role" in o["subject"].lower():
        cap, nm, FIXED = "7.6", "Legal, Regulatory & Contractual Compliance for AI", FIXED + 1
    for j, v in enumerate([cap, nm, o["instrument"], o["subject"], o["status"], None, None], 1):
        cell = ws.cell(row=r, column=j, value=v); cell.border = BOX; cell.alignment = WRAP
        cell.font = B if j == 2 else T
        if j == 3: cell.font = Font(name=F, size=10, bold=True, color="9E5A21")
        if j == 5: cell.font = TS
        if j >= 6:
            cell.fill = INPUT; cell.font = T; cell.protection = Protection(locked=False)
    ws.row_dimensions[r].height = 30
ws.freeze_panes = "C2"; ws.auto_filter.ref = "A1:G%d" % (len(OBL) + 1)
note(ws, len(OBL) + 3, 7,
 "Statutory references were removed from capability provenance and held here. NOTHING in this workbook asserts that any regulation binds the institution. Capability 7.6.6 Regulatory Role Determination is the prerequisite: Articles 49, 72 and 73 of the EU AI Act are PROVIDER obligations and on the use cases contemplated here the institution would be a deployer. This register is owned by Legal, not by Enterprise Architecture.", 46)

# ============================================================ 11. Rubric template
ws = wb.create_sheet("11. Rubric template")
head(ws, ["Capability","Rubric ver.","Level","Criterion ID","Criterion","Status","Gate",
          "Applicability trigger","Evidence type","Sufficiency rule","Caps maturity","Assessor","Approver"],
     [10,12,7,12,38,13,8,26,24,38,12,18,18])
TPL = [
 ["3.6","v0.5-draft",2,"3.6.1","Retrieval Service Provision","mandatory","AND","Always",
  "Service description + two named consuming teams","Operating >= 1 quarter in >= 2 scopes","No","",""],
 ["3.6","v0.5-draft",3,"3.6.2","Access-Trimmed Retrieval Enforcement","mandatory","AND",
  "Corpus contains access-restricted content","ACL regression test results",
  "Sampled conformance across all indexed sources, within 6 months","YES - essential control","",""],
 ["3.6","v0.5-draft",3,"3.6.5","Citation, Grounding & Traceability","mandatory","AND",
  "Output used in decision support","Citation accuracy measurement","Benchmark run within 6 months","No","",""],
 ["3.6","v0.5-draft",4,"3.6.3","Retrieval Quality Evaluation & Tuning","mandatory","AND","Always",
  "Relevance benchmark with thresholds","Breaches tracked over >= 2 quarters","No","",""],
 ["3.6","v0.5-draft",4,"3.6.4","Multi-Source Federation & Ranking","conditional","OR",
  "More than one authoritative repository in scope","Federation coverage report","Covers all in-scope repositories","No","",""],
 ["3.6","v0.5-draft",5,"-","Evidence-driven improvement cycle completed","mandatory","AND","Always",
  "Trend + action + verified benefit","One full cycle closed and verified","No","",""],
]
for i, row in enumerate(TPL):
    r = i + 2
    for j, v in enumerate(row, 1):
        cell = ws.cell(row=r, column=j, value=v); cell.border = BOX; cell.alignment = WRAP; cell.font = T
        if j in (12, 13): cell.fill = INPUT; cell.font = IN; cell.protection = Protection(locked=False)
        if j == 6 and v == "mandatory": cell.font = Font(name=F, size=10, bold=True, color="8E3226")
        if j == 11 and str(v).startswith("YES"): cell.font = Font(name=F, size=10, bold=True, color="8E3226")
    ws.row_dimensions[r].height = 34
note(ws, len(TPL) + 3, 13,
 "ONE worked rubric. Forty-nine more are required before an enterprise baseline. The rating is the highest level for which every applicable MANDATORY criterion at that level AND ALL LOWER LEVELS is met by valid evidence. Conditional criteria enter the gate only when their trigger is true. Enhancing criteria never compensate for an unmet mandatory gate. Only a criterion marked 'caps maturity' may hold a rating down on control grounds. Until a capability has an approved rubric its rating is provisional and must be labelled so.", 58)

# ============================================================ 12. Enterprise assets
ws = wb.create_sheet("12. Enterprise assets")
head(ws, ["Asset ID","Type","Name","Status","Location","Used by","Note"],
     [10,22,44,26,64,26,66])
STCOL = {"Published":"3F6F32","Published (JFrog)":"3F6F32","In use":"3F6F32",
         "Pre-release":"C9AE4A","Built, not yet distributed":"C9AE4A","In review by DX":"9E5A21"}
USED = {}
for rid, aids in A["ASSET_LINK"].items():
    for aid in aids: USED.setdefault(aid, []).append(rid)
for i, (typ, aid, nm, status, loc, note_) in enumerate(A["ASSETS"]):
    r = i + 2
    for j, v in enumerate([aid, typ, nm, status, loc, ", ".join(USED.get(aid, [])), note_], 1):
        cell = ws.cell(row=r, column=j, value=v); cell.border = BOX; cell.font = T
        cell.alignment = WRAP if j in (3,5,7) else TOP
        if j == 1: cell.font = Font(name=F, size=10, bold=True, color=ACC)
        if j == 3: cell.font = B
        if j == 4:
            hx = STCOL.get(status, "C3CCD3")
            cell.fill = PatternFill("solid", fgColor=hx)
            cell.font = Font(name=F, size=9, bold=True,
                             color="2A2200" if hx == "C9AE4A" else "FFFFFF")
            cell.alignment = CTR
        if j == 5 and loc:
            cell.font = Font(name=F, size=9, color="0000EE", underline="single")
            cell.hyperlink = loc
        if j == 6: cell.font = Font(name=F, size=9, color=ACC)
        if j == 7: cell.font = TS
    ws.row_dimensions[r].height = 34
AST_LAST = len(A["ASSETS"]) + 1
ws.freeze_panes = "C2"; ws.auto_filter.ref = "A1:G%d" % AST_LAST
note(ws, AST_LAST + 2, 7,
 "The evidence layer. Every readiness level on sheet 2 and every generic tick on sheet 3 should trace to a row here. Status is the thing to watch: PRE-RELEASE and IN REVIEW assets do not establish readiness, they establish that readiness is one release away. Two Foundry Agents documents are pre-release; two Terraform modules sit in review with DX; MCP template v2 is built but not distributed. Those five rows are the cheapest roadmap items in the whole model.", 46)

wb.save("Enterprise-AI-Capability-Model.xlsx")
print("saved %d sheets | capabilities %d | realizations %d | enablement %d | edges %d | obligations fixed %d"
      % (len(wb.sheetnames), N2, REAL_LAST - 1, ENB_LAST - 1, EDG_LAST - 1, FIXED))
print(wb.sheetnames)

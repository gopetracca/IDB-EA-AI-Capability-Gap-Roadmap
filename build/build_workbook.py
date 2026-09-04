# -*- coding: utf-8 -*-
"""The working workbook: read it, fill it in, send it, get it back.

Seven sheets. No formulas anywhere - every derived number is computed in Python
and written as a value, so the workbook needs no recalculation and opens the
same way in Excel, LibreOffice and the browser.

Yellow cells are the only ones to edit. `python3 build/build.py ingest` reads
them back into facts/observations.json.
"""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

import facts

F = "Aptos Narrow"
INK, ACC = "0E1A21", "1B4A63"
H = Font(name=F, size=10, bold=True, color="FFFFFF")
B = Font(name=F, size=10, bold=True, color=INK)
T = Font(name=F, size=10, color=INK)
TS = Font(name=F, size=9, color="55666F")
IN = Font(name=F, size=10, bold=True, color="0000CC")
TITLE = Font(name=F, size=16, bold=True, color=ACC)
HDR = PatternFill("solid", fgColor=ACC)
INPUT = PatternFill("solid", fgColor="FFF6CC")
NOTE = PatternFill("solid", fgColor="EDF2F5")
thin = Side(style="thin", color="CFD8DE")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(vertical="top", wrap_text=True)
TOP = Alignment(vertical="top")
CTR = Alignment(horizontal="center", vertical="center")
VAL_FILL = {"yes": "3F6F32", "partial": "C9AE4A", "no": "8E3226",
            "n/a": "C3CCD3", "unknown": "E8EDF0"}
VAL_FONT = {"yes": "FFFFFF", "partial": "2A2200", "no": "FFFFFF",
            "n/a": INK, "unknown": "8A9AA3"}
LVL_FILL = {0: "8E3226", 1: "9E5A21", 2: "C9AE4A", 3: "3F6F32",
            4: "25583F", 5: "163E2C"}


def head(ws, cols, row=1):
    for i, (label, w) in enumerate(cols, 1):
        c = ws.cell(row=row, column=i, value=label)
        c.font = H; c.fill = HDR; c.border = BOX
        c.alignment = Alignment(vertical="center", wrap_text=True)
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[row].height = 30


def note(ws, row, ncols, text, h=42):
    c = ws.cell(row=row, column=1, value=text)
    c.font = TS; c.alignment = WRAP; c.fill = NOTE
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=ncols)
    ws.row_dimensions[row].height = h


def build(m, scale, path):
    wb = Workbook(); wb.remove(wb.active)

    # =============================================== 0. Start here
    ws = wb.create_sheet("0. Start here"); ws.sheet_view.showGridLines = False
    for i, w in enumerate([3, 26, 104], 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    rows = [
        ("T", "Enterprise AI Capability Model", ""),
        ("S", "A capability model for AI  ·  Inter-American Development Bank", ""),
        ("", "", ""),
        ("H", "What this workbook is", ""),
        ("P", "It is the model", "Not a report generated from somewhere else. This file is where the facts live. Edit the yellow cells, save, and the views are rebuilt from it."),
        ("P", "Facts, not scores", "You never type a level. You record four observations per capability, each with evidence. The level is computed."),
        ("", "", ""),
        ("H", "The four observations", ""),
        ("P", "Practised", "Is this done on real AI systems in production, repeatedly?"),
        ("P", "Enabled", "Can a team get the tooling for this without building it themselves?"),
        ("P", "Skilled", "Do the people who must do this know how?"),
        ("P", "Defined", "Is there an approved institutional standard, policy or method? Whoever owns the subject sets it - the platform team, Cybersecurity, Data Management, Legal, HR or EA. Not one function's job."),
        ("P", "Values", "yes / partial / no / n-a / unknown.  n-a needs a reason. unknown means nobody has looked - it is not a zero."),
        ("", "", ""),
        ("H", "The order matters", ""),
        ("W", "Performance comes first", "A published standard with nothing performed against it earns NO LEVEL. That is the ISO/IEC 33020 ordering and it is deliberate: it is what stops 'we approved the technology' from reading as 'we have the capability'."),
        ("", "", ""),
        ("H", "How to use it", ""),
        ("P", "1 - Read", "Sheet 1 for the capability map. Sheet 3 for what the platform actually offers today."),
        ("P", "2 - Complete", "Sheet 2. One row per capability per observation. Fill value, evidence, who said so, when."),
        ("P", "3 - Send", "Send this file. One reviewer at a time - Excel does not merge."),
        ("P", "4 - Rebuild", "python3 build/build.py ingest   then   python3 build/build.py views"),
        ("", "", ""),
        ("H", "Cell conventions", ""),
        ("Y", "Yellow, blue bold", "Your input. The only cells to edit."),
        ("K", "Black", "Reference content, regenerated on every build. Edits here are overwritten."),
    ]
    r = 1
    for kind, a, b in rows:
        if kind == "T":
            ws.cell(row=r, column=2, value=a).font = TITLE
            ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
            ws.row_dimensions[r].height = 24
        elif kind == "S":
            ws.cell(row=r, column=2, value=a).font = TS
            ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
        elif kind == "H":
            c = ws.cell(row=r, column=2, value=a)
            c.font = Font(name=F, size=11, bold=True, color=ACC)
            ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
            ws.row_dimensions[r].height = 20
        elif kind:
            c1 = ws.cell(row=r, column=2, value=a); c1.font = B; c1.alignment = TOP
            c2 = ws.cell(row=r, column=3, value=b); c2.font = T; c2.alignment = WRAP
            if kind == "Y": c1.fill = INPUT; c1.font = IN
            if kind == "W":
                c1.font = Font(name=F, size=10, bold=True, color="8E3226")
                c2.fill = PatternFill("solid", fgColor="F4DCD8")
            ws.row_dimensions[r].height = max(14, 12.4 * (1 + len(b) // 98))
        r += 1

    # =============================================== 1. Capabilities
    ws = wb.create_sheet("1. Capabilities")
    head(ws, [("Domain", 8), ("ID", 7), ("Capability", 34), ("Able to...", 52),
              ("Owner (Bank unit)", 26), ("Match", 11), ("Practised", 10),
              ("Enabled", 10), ("Skilled", 10), ("Defined", 10),
              ("LEVEL", 8), ("Level name", 14), ("Why", 62), ("Criteria", 9)])
    r = 2
    for c in sorted(m.capabilities, key=lambda x: m.sort_key(x['id'])):
        vals = m.values(c['id'])
        lvl, why = m.rate(scale, c['id'])
        unit, match, _ = m.owner(c['id'])
        lname = dict((n, k) for n, k, _ in scale.LEVELS).get(lvl, "not rated")
        row = [c['domain'], c['id'], c['name'], c['definition'], unit or "NO OWNER",
               match, vals['practised'], vals['enabled'], vals['skilled'],
               vals['defined'], lvl if lvl is not None else "-", lname, why,
               len(c['criteria'])]
        for j, v in enumerate(row, 1):
            cell = ws.cell(row=r, column=j, value=v)
            cell.border = BOX; cell.font = T
            cell.alignment = WRAP if j in (3, 4, 5, 12, 13) else (
                CTR if j in (2, 6, 7, 8, 9, 10, 11, 14) else TOP)
            if j == 2: cell.font = Font(name=F, size=10, bold=True, color=ACC)
            if j == 3: cell.font = B
            if j == 4: cell.font = TS
            if j == 5 and not unit:
                cell.font = Font(name=F, size=10, bold=True, color="8E3226")
            if j in (7, 8, 9, 10):
                cell.fill = PatternFill("solid", fgColor=VAL_FILL[v])
                cell.font = Font(name=F, size=9, bold=True, color=VAL_FONT[v])
            if j == 11 and lvl is not None:
                cell.fill = PatternFill("solid", fgColor=LVL_FILL[lvl])
                cell.font = Font(name=F, size=11, bold=True, color="FFFFFF")
            if j == 13: cell.font = TS
        ws.row_dimensions[r].height = 28
        r += 1
    ws.freeze_panes = "D2"; ws.auto_filter.ref = "A1:N%d" % (r - 1)
    note(ws, r + 1, 14,
         "READ ONLY - every column is computed. Observations are edited on sheet 2. "
         "Scale: %s. %s  %s" % (scale.NAME, scale.BASIS,
                                scale.note() if hasattr(scale, 'note') else ""), 46)

    # =============================================== 2. Observations
    ws = wb.create_sheet("2. Observations")
    head(ws, [("Capability", 11), ("Name", 32), ("Observation", 12),
              ("The question", 54), ("VALUE", 11), ("Evidence", 46),
              ("Observed by", 22), ("Date", 12), ("Basis / why", 56)])
    q = {t['id']: t['question'] for t in m.observation_types}
    r = 2
    for c in sorted(m.capabilities, key=lambda x: m.sort_key(x['id'])):
        for t in m.observation_types:
            o = m.obs_by_cap.get(c['id'], {}).get(t['id'], {})
            v = o.get('value', 'unknown')
            row = [c['id'], c['name'], t['id'], q[t['id']], v, o.get('evidence', ''),
                   o.get('observed_by', ''), o.get('observed_on', ''), o.get('basis', '')]
            for j, val in enumerate(row, 1):
                cell = ws.cell(row=r, column=j, value=val)
                cell.border = BOX; cell.font = T
                cell.alignment = WRAP if j in (2, 4, 6, 9) else (
                    CTR if j == 5 else TOP)
                if j == 1: cell.font = Font(name=F, size=10, bold=True, color=ACC)
                if j == 3: cell.font = Font(name=F, size=9, bold=True, color=ACC)
                if j == 4: cell.font = TS
                if j == 5:
                    cell.fill = PatternFill("solid", fgColor=VAL_FILL[v])
                    cell.font = Font(name=F, size=10, bold=True, color=VAL_FONT[v])
                if j in (6, 7, 8):
                    cell.fill = INPUT; cell.font = T
                if j == 9: cell.font = TS
            ws.row_dimensions[r].height = 26
            r += 1
    dv = DataValidation(type="list", formula1='"yes,partial,no,n-a,unknown"',
                        allow_blank=False, showErrorMessage=True,
                        errorTitle="Observation value",
                        error="yes / partial / no / n-a (needs a reason) / unknown (nobody has looked)")
    ws.add_data_validation(dv); dv.add("E2:E%d" % (r - 1))
    ws.freeze_panes = "C2"; ws.auto_filter.ref = "A1:I%d" % (r - 1)
    note(ws, r + 1, 9,
         "THIS IS THE SHEET YOU FILL IN. Column E is the value; columns F, G and H are "
         "yours. An observation with no evidence is an opinion - write what you saw and "
         "who says so. 'unknown' is an honest answer and is never treated as a zero. "
         "Use 'n-a' only with a reason in column I.", 46)

    # =============================================== 3. Offerings
    ws = wb.create_sheet("3. Offerings")
    head(ws, [("ID", 9), ("Offering", 26), ("What a team gets", 22),
              ("Operated by", 30), ("Status", 12), ("Assets", 30),
              ("Released", 10), ("Enables capabilities", 26),
              ("In the box", 11), ("Does not provide", 46), ("Note", 60)])
    r = 2
    for o in m.offerings:
        answered = sum(1 for x in o['in_the_box'] if x['status'])
        row = [o['id'], o['name'], o['consumption'], o['operated_by'], o['status'],
               ", ".join(o['assets']),
               "%d of %d" % (o['assets_released'], o['assets_total']),
               ", ".join(o['enables']),
               "%d of %d" % (answered, len(o['in_the_box'])) if o['in_the_box'] else "-",
               o['not_provided'], o['note']]
        for j, v in enumerate(row, 1):
            cell = ws.cell(row=r, column=j, value=v)
            cell.border = BOX; cell.font = T
            cell.alignment = WRAP if j in (2, 4, 6, 8, 10, 11) else (
                CTR if j in (5, 7, 9) else TOP)
            if j == 1: cell.font = Font(name=F, size=10, bold=True, color=ACC)
            if j == 2: cell.font = B
            if j in (10, 11): cell.font = TS
            if j == 7 and o['assets_released'] < o['assets_total']:
                cell.fill = PatternFill("solid", fgColor="C9AE4A")
                cell.font = Font(name=F, size=10, bold=True, color="2A2200")
        ws.row_dimensions[r].height = 46
        r += 1
    ws.freeze_panes = "C2"
    note(ws, r + 1, 11,
         "What the platform actually gives a delivery team today. This is the object the "
         "room asks about - not the capability. Readiness is not a score here: it is the "
         "'In the box' column on sheet 4, counted.", 40)

    # =============================================== 4. In the box
    ws = wb.create_sheet("4. In the box")
    head(ws, [("Offering", 9), ("Offering name", 24), ("Control", 52),
              ("STATUS", 11), ("Capability", 11), ("Catalog ref", 11),
              ("Why it matters", 66), ("Evidence", 30)])
    r = 2
    for o in m.offerings:
        for x in o['in_the_box']:
            row = [o['id'], o['name'], x['control'], x['status'] or "",
                   x['capability'], x['catalog_ref'], x['why'], ""]
            for j, v in enumerate(row, 1):
                cell = ws.cell(row=r, column=j, value=v)
                cell.border = BOX; cell.font = T
                cell.alignment = WRAP if j in (2, 3, 7) else (
                    CTR if j in (4, 5, 6) else TOP)
                if j == 1: cell.font = Font(name=F, size=10, bold=True, color=ACC)
                if j == 3: cell.font = B
                if j in (4, 8): cell.fill = INPUT; cell.font = IN if j == 4 else T
                if j == 7: cell.font = TS
            ws.row_dimensions[r].height = 32
            r += 1
    if r > 2:
        dvb = DataValidation(type="list", formula1='"yes,no,partial,unknown"',
                             allow_blank=True)
        ws.add_data_validation(dvb); dvb.add("D2:D%d" % (r - 1))
    ws.freeze_panes = "C2"; ws.auto_filter.ref = "A1:H%d" % (r - 1)
    note(ws, r + 1, 8,
         "Does the offering inherit this control, or is every team left to build it? "
         "Every 'no' is a roadmap item, and a cheap one where the building block already "
         "exists: you are extending a module, not building a platform. These are the "
         "questions for the platform team.", 42)

    # =============================================== 5. Assets
    ws = wb.create_sheet("5. Assets")
    head(ws, [("ID", 9), ("Type", 22), ("Name", 46), ("Status", 26),
              ("Used by", 22), ("Location", 62), ("Note", 62)])
    used = {}
    for o in m.offerings:
        for a in o['assets']:
            used.setdefault(a, []).append(o['id'])
    STC = {"Published": "3F6F32", "Published (JFrog)": "3F6F32", "In use": "3F6F32",
           "Pre-release": "C9AE4A", "Built, not yet distributed": "C9AE4A",
           "In review by DX": "9E5A21"}
    r = 2
    for a in m.assets:
        row = [a['id'], a['type'], a['name'], a['status'],
               ", ".join(used.get(a['id'], [])), a['location'], a['note']]
        for j, v in enumerate(row, 1):
            cell = ws.cell(row=r, column=j, value=v)
            cell.border = BOX; cell.font = T
            cell.alignment = WRAP if j in (3, 6, 7) else TOP
            if j == 1: cell.font = Font(name=F, size=10, bold=True, color=ACC)
            if j == 3: cell.font = B
            if j == 4:
                hx = STC.get(a['status'], "C3CCD3")
                cell.fill = PatternFill("solid", fgColor=hx)
                cell.font = Font(name=F, size=9, bold=True,
                                 color="2A2200" if hx == "C9AE4A" else "FFFFFF")
                cell.alignment = CTR
            if j == 6 and a['location']:
                cell.font = Font(name=F, size=9, color="0000EE", underline="single")
                cell.hyperlink = a['location']
            if j == 7: cell.font = TS
        ws.row_dimensions[r].height = 32
        r += 1
    ws.freeze_panes = "C2"; ws.auto_filter.ref = "A1:G%d" % (r - 1)
    note(ws, r + 1, 7,
         "The evidence layer. Everything the Bank has actually built. Status is what to "
         "watch: PRE-RELEASE and IN REVIEW do not establish anything, they establish that "
         "it is one release away. Those rows are the cheapest roadmap items here.", 40)

    # =============================================== 6. Criteria
    ws = wb.create_sheet("6. Criteria")
    head(ws, [("Domain", 8), ("Capability", 11), ("Capability name", 30),
              ("Criterion", 10), ("Criterion name", 40), ("Definition", 74),
              ("Agentic", 9)])
    r = 2
    for c in sorted(m.capabilities, key=lambda x: m.sort_key(x['id'])):
        for x in c['criteria']:
            row = [c['domain'], c['id'], c['name'], x['id'], x['name'],
                   x['definition'], "yes" if x['agentic'] else ""]
            for j, v in enumerate(row, 1):
                cell = ws.cell(row=r, column=j, value=v)
                cell.border = BOX; cell.font = T
                cell.alignment = WRAP if j in (3, 5, 6) else (
                    CTR if j in (2, 4, 7) else TOP)
                if j == 4: cell.font = Font(name=F, size=10, bold=True, color=ACC)
                if j == 5: cell.font = B
                if j == 6: cell.font = TS
            ws.row_dimensions[r].height = 24
            r += 1
    ws.freeze_panes = "E2"; ws.auto_filter.ref = "A1:G%d" % (r - 1)
    note(ws, r + 1, 7,
         "The checklist behind a Practised judgement - what to look for when deciding "
         "whether a capability is genuinely performed. These are NOT gates and they do "
         "not carry scores. Filter column B to one capability before an interview.", 40)

    # =============================================== 7. Owners
    ws = wb.create_sheet("7. Owners")
    head(ws, [("Capability", 11), ("Capability name", 34), ("Bank unit", 28),
              ("Match", 11), ("Basis - what the catalogue says", 96)])
    r = 2
    for c in sorted(m.capabilities, key=lambda x: m.sort_key(x['id'])):
        unit, match, basis = m.owner(c['id'])
        row = [c['id'], c['name'], unit or "NO MATCH", match, basis]
        for j, v in enumerate(row, 1):
            cell = ws.cell(row=r, column=j, value=v)
            cell.border = BOX; cell.font = T
            cell.alignment = WRAP if j in (2, 3, 5) else (CTR if j == 4 else TOP)
            if j == 1: cell.font = Font(name=F, size=10, bold=True, color=ACC)
            if j == 2: cell.font = B
            if j in (3, 4) and match == "NO MATCH":
                cell.font = Font(name=F, size=10, bold=True, color="8E3226")
            if j == 5: cell.font = TS
        ws.row_dimensions[r].height = 34
        r += 1
    nomatch = sum(1 for c in m.capabilities if m.owner(c['id'])[1] == "NO MATCH")
    ws.freeze_panes = "C2"; ws.auto_filter.ref = "A1:E%d" % (r - 1)
    note(ws, r + 1, 5,
         "Mapped against the Bank's own product and enabler catalogue (%s, read %s). "
         "%d capabilities have NO MATCH: nothing in the Bank's own catalogue claims them. "
         "That is a finding about the Bank, not a gap in this model."
         % (m.owners_source['source'], m.owners_source['read_on'], nomatch), 40)

    wb.save(path)
    return wb.sheetnames

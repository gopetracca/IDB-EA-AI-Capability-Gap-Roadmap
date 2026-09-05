# -*- coding: utf-8 -*-
"""The review workbook: read it, fill in sheet 2, send it, get it back.

Ten sheets. No formulas anywhere - every derived number is computed in Python
and written as a value, so the workbook needs no recalculation and opens the
same way in Excel, LibreOffice and the browser.

The workbook is GENERATED from facts/ and is not where the facts live. Sheet 2
is the one instrument that flows back: its yellow cells are the only ones to
edit, and `python3 build/build.py ingest` reads them into
facts/observations.json. Every other sheet is reference and is overwritten on
the next build.
"""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.hyperlink import Hyperlink

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
        ("P", "It is the review instrument", "Generated from the model's recorded facts. Sheet 2 is the one sheet that flows back: fill its yellow cells, save, send it, and your answers are read into the model. Every other sheet is reference and is regenerated on the next build."),
        ("P", "Facts, not scores", "You never type a level. You record observations, each with evidence. The level is computed by a published rule, and the same evidence can be read by more than one rule without anyone re-answering."),
        ("", "", ""),
        ("H", "Three levels, and what you DO with each", ""),
        ("P", "L1 - Domain  (8)", "A reporting cluster. You read it. Never scored, never assessed. Sheet 1, column A."),
        ("P", "L2 - Capability  (52)", "THE UNIT YOU MANAGE. One accountable owner, one derived level. This is what you report, assign and fund. You never fill anything in here - every value on sheet 1 is computed. One row each on sheet 1."),
        ("P", "L3 - Criterion  (258)", "THE UNIT YOU JUDGE. A specific practice you can actually witness. This is where you answer PRACTISED, because 'is the capability practised?' has no single honest answer when the capability covers six different things. Sheet 2. Definitions on sheet 6."),
        ("W", "How they connect", "You judge at L3. The model derives L2 from it. Nobody types a capability's Practised value or its level - that is the whole design, and it is why two people cannot argue about a number without arguing about a criterion first."),
        ("", "", ""),
        ("H", "The four observations", ""),
        ("P", "Practised  (per L3)", "Is this specific practice done on real AI systems in production, repeatedly?  Asked once per criterion. The capability value is DERIVED: 'yes' only if every criterion was examined and every one passed."),
        ("P", "Enabled  (per L2)", "Can a team get the tooling for this without building it themselves?"),
        ("P", "Skilled  (per L2)", "Do the people who must do this know how?"),
        ("P", "Defined  (per L2)", "Is there an approved institutional standard, policy or method? Whoever owns the subject sets it - the platform team, Cybersecurity, Data Management, Legal, HR or EA. Not one function's job."),
        ("P", "Values", "yes / partial / no / n/a / unknown.  'no' is an evidenced negative - say what you looked at. 'n/a' means it does not apply here and needs the reason in column K. 'unknown' means nobody has looked - it is not a zero, and it is the right answer when you have not."),
        ("", "", ""),
        ("H", "The order matters", ""),
        ("W", "Performance comes first", "A published standard with nothing performed against it earns NO LEVEL. That is the ISO/IEC 33020 ordering and it is deliberate: it is what stops 'we approved the technology' from reading as 'we have the capability'."),
        ("", "", ""),
        ("H", "How to use it", ""),
        ("P", "1 - Read", "Sheet 1 for the capability map. Find the capabilities you own. Sheet 3 for what the platform actually offers today. Sheets 8 and 9 hold the source register and the statutory references, for the provenance and Legal reviewers."),
        ("P", "2 - Jump", "Click the last column of sheet 1 - 'Assess it' - to land on that capability's block on sheet 2."),
        ("P", "3 - Complete", "Sheet 2. For each of your capabilities: judge every L3 criterion for Practised, then answer Enabled, Skilled and Defined once. Fill value, evidence, who said so, when. Answer only for the capabilities you own - leave the rest 'unknown'."),
        ("P", "4 - Send", "Send this file back. One reviewer at a time - Excel does not merge."),
        ("P", "5 - Rebuild", "python3 build/build.py ingest   then   python3 build/build.py all"),
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
              ("LEVEL", 8), ("Level name", 14), ("Why", 62),
              ("Assess it (click)", 18)])
    # row each capability's block starts on, on sheet 6, so sheet 1 can link to it
    critrow, _rr = {}, 2
    for c in sorted(m.capabilities, key=lambda x: m.sort_key(x['id'])):
        critrow[c['id']] = _rr
        _rr += 1 + len(c['criteria'])

    # and the row its block starts on, on sheet 2, where the work is actually done
    n_cap_types = len([t for t in m.observation_types
                       if t['id'] not in m.criterion_types])
    obsrow, _or = {}, 2
    for c in sorted(m.capabilities, key=lambda x: m.sort_key(x['id'])):
        obsrow[c['id']] = _or
        _or += 1 + n_cap_types + len(c['criteria']) * len(m.criterion_types)
    r = 2
    for c in sorted(m.capabilities, key=lambda x: m.sort_key(x['id'])):
        vals = m.values(c['id'])
        lvl, why = m.rate(scale, c['id'])
        unit, match, _ = m.owner(c['id'])
        lname = dict((n, k) for n, k, _ in scale.LEVELS).get(lvl, "not rated")
        row = [c['domain'], c['id'], c['name'], c['definition'], unit or "NO OWNER",
               match, vals['practised'], vals['enabled'], vals['skilled'],
               vals['defined'], lvl if lvl is not None else "-", lname, why,
               ("%d criteria to judge" % len(c['criteria']))
               if c['criteria'] else ""]
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
            if j == 14 and c['criteria']:
                cell.font = Font(name=F, size=9, color="0000EE", underline="single")
                cell.hyperlink = Hyperlink(
                    ref="N%d" % r,
                    location="'2. Observations'!A%d" % obsrow[c['id']],
                    tooltip="Go to sheet 2 and judge the %d criteria behind %s"
                            % (len(c['criteria']), c['id']))
        ws.row_dimensions[r].height = 28
        r += 1
    ws.freeze_panes = "D2"; ws.auto_filter.ref = "A1:N%d" % (r - 1)
    note(ws, r + 1, 14,
         "READ ONLY - every column is computed. Observations are edited on sheet 2. "
         "PRACTISED is rolled up from the L3 criteria: it reads 'yes' only when every "
         "criterion was examined and every one passed, so one unexamined criterion "
         "holds it at 'partial'. "
         "Scale: %s. %s  %s" % (scale.NAME, scale.BASIS,
                                scale.note() if hasattr(scale, 'note') else ""), 46)

    # =============================================== 2. Observations
    ws = wb.create_sheet("2. Observations")
    head(ws, [("Capability", 11), ("Name", 26), ("Observation", 12),
              ("L3 criterion", 11), ("What you are judging", 30),
              ("The question", 46), ("VALUE", 11), ("Evidence", 42),
              ("Observed by", 20), ("Date", 12), ("Basis / why", 46)])
    q = {t['id']: t['question'] for t in m.observation_types}
    SUBHDR = PatternFill("solid", fgColor="DEE9EF")
    r = 2
    obsrow = {}                       # capability -> first row, for sheet 1 links
    for c in sorted(m.capabilities, key=lambda x: m.sort_key(x['id'])):
        obsrow[c['id']] = r
        # a banner per capability, so 414 rows read as 52 blocks
        hdr = [c['id'], c['name'], "", "", "", c['definition'], "", "", "", "", ""]
        for j, v in enumerate(hdr, 1):
            cell = ws.cell(row=r, column=j, value=v)
            cell.border = BOX; cell.fill = SUBHDR
            cell.font = Font(name=F, size=10, bold=True,
                             color=ACC if j in (1, 2) else INK)
            cell.alignment = WRAP if j in (2, 6) else TOP
        ws.row_dimensions[r].height = 20
        r += 1
        for t in m.observation_types:
            crit_level = t['id'] in m.criterion_types
            # one row per criterion for practised; one row for the rest
            items = (m.criteria_obs(c['id'], t['id']) if crit_level
                     else [(None, m.obs_by_cap.get(c['id'], {}).get(t['id'], {}))])
            for x, o in items:
                v = o.get('value', 'unknown')
                row = [c['id'], c['name'], t['id'],
                       x['id'] if x else "",
                       x['name'] if x else "the capability as a whole",
                       (x['definition'] if x else q[t['id']]),
                       v, o.get('evidence', ''), o.get('observed_by', ''),
                       o.get('observed_on', ''), o.get('basis', '')]
                for j, val in enumerate(row, 1):
                    cell = ws.cell(row=r, column=j, value=val)
                    cell.border = BOX; cell.font = T
                    cell.alignment = WRAP if j in (2, 5, 6, 8, 11) else (
                        CTR if j in (1, 4, 7) else TOP)
                    if j == 1: cell.font = Font(name=F, size=10, bold=True, color=ACC)
                    if j == 3: cell.font = Font(name=F, size=9, bold=True, color=ACC)
                    if j == 4: cell.font = Font(name=F, size=10, bold=True, color=ACC)
                    if j == 5: cell.font = B
                    if j == 6: cell.font = TS
                    if j == 7:
                        cell.fill = PatternFill("solid", fgColor=VAL_FILL[v])
                        cell.font = Font(name=F, size=10, bold=True,
                                         color=VAL_FONT[v])
                    if j in (8, 9, 10):
                        cell.fill = INPUT
                        cell.font = T
                    if j == 11: cell.font = TS
                if crit_level:
                    ws.row_dimensions[r].outlineLevel = 1
                ws.row_dimensions[r].height = 26
                r += 1
    dv = DataValidation(type="list", formula1='"yes,partial,no,n/a,unknown"',
                        allow_blank=False, showErrorMessage=True,
                        errorTitle="Observation value",
                        error="yes / partial / no / n/a (needs a reason) / unknown (nobody has looked)")
    ws.add_data_validation(dv); dv.add("G2:G%d" % (r - 1))
    ws.freeze_panes = "E2"; ws.auto_filter.ref = "A1:K%d" % (r - 1)
    note(ws, r + 1, 11,
         "THIS IS THE SHEET YOU FILL IN. Column G is the value; H, I and J are yours. "
         "PRACTISED is asked once per L3 criterion - the specific practice you can "
         "actually witness - because 'is this capability practised?' has no single "
         "honest answer when the capability covers six different things. The "
         "capability-level Practised value is DERIVED from those rows and appears on "
         "sheet 1; you never type it. ENABLED, SKILLED and DEFINED are asked once for "
         "the capability. An observation with no evidence is an opinion - write what "
         "you saw and who says so. 'unknown' is an honest answer and is never a zero. "
         "Use 'n/a' only with a reason in column K.", 62)

    # =============================================== 3. Offerings
    ws = wb.create_sheet("3. Offerings")
    head(ws, [("ID", 9), ("Offering", 26), ("What a team gets", 22),
              ("Operated by", 30), ("Status", 12), ("Assets", 30),
              ("Released", 10), ("Enables capabilities", 26),
              ("In the box", 11), ("Does not provide", 46), ("Note", 60)])
    r = 2
    for o in m.offerings:
        answered = sum(1 for x in o['in_the_box'] if x['status'])
        rel, tot = m.release_count(o)
        row = [o['id'], o['name'], o['consumption'], o['operated_by'], o['status'],
               ", ".join(o['assets']),
               "%d of %d" % (rel, tot),
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
            if j == 7 and rel < tot:
                cell.fill = PatternFill("solid", fgColor="C9AE4A")
                cell.font = Font(name=F, size=10, bold=True, color="2A2200")
        ws.row_dimensions[r].height = 46
        r += 1
    ws.freeze_panes = "C2"
    note(ws, r + 1, 11,
         "What the platform actually gives a delivery team today. This is the object the "
         "room asks about - not the capability. 'Released' is derived from the asset "
         "statuses on sheet 5. Readiness is not a score here: it is the 'In the box' "
         "column on sheet 4, counted. The Note column carries the migration notes from "
         "the old realization register and may still use its superseded readiness "
         "vocabulary.", 46)

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
    head(ws, [("ID", 9), ("Type", 22), ("Name", 46), ("Status", 26), ("Released", 9),
              ("What the status means", 40), ("Used by", 22), ("Location", 62),
              ("Note", 62)])
    used = {}
    for o in m.offerings:
        for a in o['assets']:
            used.setdefault(a, []).append(o['id'])
    r = 2
    for a in m.assets:
        rel = m.released(a)
        row = [a['id'], a['type'], a['name'], a['status'], "yes" if rel else "no",
               m.asset_statuses.get(a['status'], {}).get('meaning', ''),
               ", ".join(used.get(a['id'], [])), a['location'], a['note']]
        for j, v in enumerate(row, 1):
            cell = ws.cell(row=r, column=j, value=v)
            cell.border = BOX; cell.font = T
            cell.alignment = WRAP if j in (3, 6, 8, 9) else TOP
            if j == 1: cell.font = Font(name=F, size=10, bold=True, color=ACC)
            if j == 3: cell.font = B
            if j == 4:
                hx = "3F6F32" if rel else "C9AE4A"
                cell.fill = PatternFill("solid", fgColor=hx)
                cell.font = Font(name=F, size=9, bold=True,
                                 color="FFFFFF" if rel else "2A2200")
                cell.alignment = CTR
            if j == 5: cell.alignment = CTR
            if j == 6: cell.font = TS
            if j == 8 and a['location']:
                cell.font = Font(name=F, size=9, color="0000EE", underline="single")
                cell.hyperlink = a['location']
            if j == 9: cell.font = TS
        ws.row_dimensions[r].height = 32
        r += 1
    ws.freeze_panes = "C2"; ws.auto_filter.ref = "A1:I%d" % (r - 1)
    note(ws, r + 1, 9,
         "The evidence layer. Everything the Bank has actually built. Status is what to "
         "watch: a status that is not RELEASED does not establish anything, it "
         "establishes that the asset is one release away. Those rows are the cheapest "
         "roadmap items here. Which statuses count as released is declared once, in "
         "facts/assets.json.", 40)

    # =============================================== 6. Criteria (L3)
    ws = wb.create_sheet("6. Criteria (L3)")
    head(ws, [("Domain", 8), ("L2 capability", 12), ("Capability name", 30),
              ("L3 criterion", 11), ("Criterion name", 40), ("Definition", 74),
              ("Agentic", 9)])
    ws.sheet_properties.outlinePr.summaryBelow = False
    CAPHDR = PatternFill("solid", fgColor="DEE9EF")
    r = 2
    for c in sorted(m.capabilities, key=lambda x: m.sort_key(x['id'])):
        # one header row per capability, its criteria grouped and collapsible beneath
        hdr = [c['domain'], c['id'], c['name'], "",
               "%d L3 criteria" % len(c['criteria']),
               m.owner(c['id'])[0] or "no owner in the catalogue", ""]
        for j, v in enumerate(hdr, 1):
            cell = ws.cell(row=r, column=j, value=v)
            cell.border = BOX; cell.fill = CAPHDR
            cell.font = Font(name=F, size=10, bold=True,
                             color=ACC if j in (2, 5) else INK)
            cell.alignment = WRAP if j in (3, 6) else TOP
        ws.row_dimensions[r].height = 20
        r += 1
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
            ws.row_dimensions[r].outlineLevel = 1
            r += 1
    ws.freeze_panes = "E2"; ws.auto_filter.ref = "A1:G%d" % (r - 1)
    note(ws, r + 1, 7,
         "ALL %d L3 CRITERIA with their full definitions, grouped under their L2 "
         "capability. This sheet is the REFERENCE - read it to understand what a "
         "criterion means. You JUDGE them on sheet 2, which carries one Practised row "
         "for each of them. Use the +/- outline handles to collapse a capability, or "
         "filter column B to one capability ID. "
         "Criteria carry no level of their own: they carry an observation, and the "
         "capability's Practised value is derived from them (ADR-0014)."
         % sum(len(c['criteria']) for c in m.capabilities), 46)

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

    # =============================================== 8. Sources
    ws = wb.create_sheet("8. Sources")
    head(ws, [("ID", 7), ("Grade", 7), ("Source", 30), ("Title", 44), ("Publisher", 26),
              ("Edition", 16), ("Date", 11), ("Status", 26), ("Access", 30),
              ("Cited by", 9), ("Caution", 70), ("URL", 40)])
    cited = {}
    for c in m.capabilities:
        for _cit, src, _loc in m.capability_sources(c['id']):
            if src:
                cited[src['id']] = cited.get(src['id'], 0) + 1
    GRADE = {"A": "3F6F32", "B": "6E8F3A", "C": "C9AE4A", "D": "8E3226"}
    r = 2
    for s in m.sources:
        row = [s['id'], s['grade'], s['short'], s.get('title', ''), s.get('publisher', ''),
               s.get('edition', ''), s.get('date', ''), s.get('status', ''),
               s.get('access', ''), cited.get(s['id'], 0), s.get('caution', ''),
               s.get('url', '')]
        for j, v in enumerate(row, 1):
            cell = ws.cell(row=r, column=j, value=v)
            cell.border = BOX; cell.font = T
            cell.alignment = WRAP if j in (3, 4, 5, 8, 9, 11) else (
                CTR if j in (1, 2, 7, 10) else TOP)
            if j == 1: cell.font = Font(name=F, size=10, bold=True, color=ACC)
            if j == 2:
                cell.fill = PatternFill("solid", fgColor=GRADE.get(v, "C3CCD3"))
                cell.font = Font(name=F, size=10, bold=True,
                                 color="2A2200" if v == "C" else "FFFFFF")
            if j == 3: cell.font = B
            if j == 11: cell.font = TS
            if j == 12 and v:
                cell.font = Font(name=F, size=9, color="0000EE", underline="single")
                cell.hyperlink = v
        ws.row_dimensions[r].height = 46
        r += 1
    ws.freeze_panes = "D2"; ws.auto_filter.ref = "A1:L%d" % (r - 1)
    note(ws, r + 1, 12,
         "The source register (ADR-0010). Grade A: open, dated, versioned, standards body "
         "or public authority. B: open and dated, vendor or non-normative. C: undated, "
         "superseded, flagged historical, or paywalled. D: non-public or not a "
         "publication - USABLE INTERNALLY, NEVER IN ANYTHING THAT LEAVES THE BANK. "
         "'Cited by' counts the capabilities on sheet 1 that name this source. Edited in "
         "facts/sources.json; the full picture is out/provenance.md.", 52)

    # =============================================== 9. Obligations
    ws = wb.create_sheet("9. Obligations")
    head(ws, [("Capability", 11), ("Capability name", 40), ("Instrument", 24),
              ("Subject", 60), ("Status", 46)])
    r = 2
    for ob in m.obligations:
        row = [ob['capability'], ob.get('capability_name', ''), ob['instrument'],
               ob['subject'], ob['status']]
        for j, v in enumerate(row, 1):
            cell = ws.cell(row=r, column=j, value=v)
            cell.border = BOX; cell.font = T
            cell.alignment = WRAP if j in (2, 4, 5) else (CTR if j == 1 else TOP)
            if j == 1: cell.font = Font(name=F, size=10, bold=True, color=ACC)
            if j == 3: cell.font = B
            if j == 5: cell.font = TS
        ws.row_dimensions[r].height = 30
        r += 1
    ws.freeze_panes = "C2"; ws.auto_filter.ref = "A1:E%d" % (r - 1)
    note(ws, r + 1, 5,
         "Statutory references, Legal-owned, all CANDIDATE until applicability is "
         "determined (ADR-0008). 7.6.6 Regulatory Role Determination is the prerequisite: "
         "on the use cases contemplated the Bank would be a deployer, not a provider. "
         "Edited in facts/obligations.json.", 40)

    wb.save(path)
    return wb.sheetnames

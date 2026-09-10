# -*- coding: utf-8 -*-
"""The review workbook: read it, fill in sheet 2, send it, get it back.

Ten sheets. No formulas anywhere - every derived number is computed in Python
and written as a value, so the workbook needs no recalculation and opens the
same way in Excel, LibreOffice and the browser.

The workbook is GENERATED from facts/ and is not where the facts live. Sheet 2
is the one instrument that flows back: its yellow cells are the only ones to
edit, and `uv run python build/build.py ingest` reads them into
facts/observations.json. Every other sheet is reference and is overwritten on
the next build.
"""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.hyperlink import Hyperlink
from openpyxl.comments import Comment

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


def values_block(m, indent="  "):
    """The observation vocabulary, rendered.  The list is the one facts/ declares,
    so a value can never be shown here that the model does not accept, nor one it
    accepts be left out.  `check` refuses to build if a declared value has no
    meaning to render."""
    w = max(len(v) for v in m.observation_values)
    return "\n".join("%s%-*s  %s" % (indent, w, v, facts.OBS_MEANING[v])
                      for v in m.observation_values)


def levels_block(scale, indent="  "):
    """The scale's ladder, rendered, saying which levels it can actually reach."""
    cap = getattr(scale, "DERIVABLE_MAX", None)
    out = []
    for n, k, d in scale.LEVELS:
        out.append("%s%s  %-12s %s%s" % (indent, n, k, d,
                   "  NOT DERIVABLE from the observations collected today."
                   if cap is not None and n > cap else ""))
    out.append("%s%s  %-12s %s" % (indent, "-", "not rated",
               "Nobody has observed performance, so there is nothing to place a "
               "level on. A result, not a zero."))
    return "\n".join(out)


def hint(ws, col, title, body, height=260, width=380):
    """A note on a column header, so a reader can ask a cell what it may say."""
    c = ws.cell(row=1, column=col)
    c.comment = Comment("%s\n\n%s" % (title, body), "AI Capability Model",
                        height=height, width=width)


def sheet2_rows(m):
    """Where sheet 2 puts every block, so sheet 1 can link straight into it.

    Mirrors the loop that writes sheet 2 - a banner row per capability, then
    one row per criterion for the criterion-level observations and one row for
    each of the rest, in observation_types order.  Sheet 2 re-derives the same
    numbers as it writes and refuses to build if the two disagree.
    """
    cap, crit, r = {}, {}, 2
    for c in m.capabilities_sorted():
        cap[c['id']] = r
        r += 1
        for t in m.observation_types:
            if t['id'] in m.criterion_types:
                for x in c['criteria']:
                    crit[(t['id'], x['id'])] = r
                    r += 1
            else:
                r += 1
    return cap, crit


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
        ("P", "L1 - Domain  (8)", "A reporting cluster. You read it. Never scored, never assessed. Its own row on sheets 1 and 6, with its capabilities nested under it."),
        ("P", "L2 - Capability  (52)", "THE UNIT YOU MANAGE. One accountable owner, one derived level. This is what you report, assign and fund. You never fill anything in here - every value on sheet 1 is computed. One row each on sheet 1, under its domain."),
        ("P", "L3 - Criterion  (258)", "THE UNIT YOU JUDGE. A specific practice you can actually witness. This is where you answer PRACTISED, because 'is the capability practised?' has no single honest answer when the capability covers six different things. Judged on sheet 2; nested under its capability on sheets 1 and 6, with its definition."),
        ("W", "How they connect", "You judge at L3. The model derives L2 from it. Nobody types a capability's Practised value or its level - that is the whole design, and it is why two people cannot argue about a number without arguing about a criterion first."),
        ("", "", ""),
        ("H", "The four observations", ""),
        ("P", "Practised  (per L3)", "Is this specific practice done on real AI systems in production, repeatedly?  Asked once per criterion. The capability value is DERIVED: 'yes' only if every criterion was examined and every one passed."),
        ("P", "Enabled  (per L2)", "Can a team get the tooling for this without building it themselves?"),
        ("P", "Skilled  (per L2)", "Do the people who must do this know how?"),
        ("P", "Defined  (per L2)", "Is there an approved institutional standard, policy or method? Whoever owns the subject sets it - the platform team, Cybersecurity, Data Management, Legal, HR or EA. Not one function's job."),
        ("P", "Values", "  ".join("%s - %s" % (v, facts.OBS_MEANING[v])
                                  for v in m.observation_values)
                        + " On sheet 2 the value is a dropdown; an 'n/a' needs its reason in column K."),
        ("", "", ""),
        ("*", "", ""),                       # the scale's ladder, generated below
        ("H", "The order matters", ""),
        ("W", "Performance comes first", "A published standard with nothing performed against it earns NO LEVEL. That is the ISO/IEC 33020 ordering and it is deliberate: it is what stops 'we approved the technology' from reading as 'we have the capability'."),
        ("", "", ""),
        ("H", "How to use it", ""),
        ("P", "1 - Read", "Sheet 1 for the capability map - the whole model in one view, three levels deep. Use the +/- outline handles or the 1/2/3 buttons above them to collapse it to domains, to capabilities, or to open the criteria, and find the capabilities you own. Sheet 3 for what the platform actually offers today. Sheets 8 and 9 hold the source register and the statutory references, for the provenance and Legal reviewers."),
        ("P", "2 - Jump", "Click the last column of sheet 1 - 'Assess it' - to land on that capability's block on sheet 2, or on an L3 row to land on the exact criterion row that judges it."),
        ("P", "3 - Complete", "Sheet 2. For each of your capabilities: judge every L3 criterion for Practised, then answer Enabled, Skilled and Defined once. Fill value, evidence, who said so, when. Answer only for the capabilities you own - leave the rest 'unknown'."),
        ("P", "4 - Send", "Send this file back. One reviewer at a time - Excel does not merge."),
        ("P", "5 - Rebuild", "uv run python build/build.py ingest   then   uv run python build/build.py all"),
        ("", "", ""),
        ("H", "Cell conventions", ""),
        ("Y", "Yellow, blue bold", "Your input. The only cells to edit."),
        ("K", "Black", "Reference content, regenerated on every build. Edits here are overwritten."),
    ]
    # The levels are the scale's to name, never this file's: whichever scale the
    # workbook was built with says what its own ladder means, and which rungs
    # today's observations can actually reach.
    cap = getattr(scale, "DERIVABLE_MAX", None)
    ladder = [("H", "The levels, and what each one asserts", "")]
    for n, k, d in scale.LEVELS:
        ladder.append(("P" if cap is None or n <= cap else "K",
                       "%s - %s" % (n, k),
                       d + ("" if cap is None or n <= cap else
                            "  Defined, but not derivable from the observations "
                            "collected today - so nothing can reach it.")))
    ladder.append(("P", "-   (not rated)",
                   "Nobody has observed performance, so there is nothing to place a "
                   "level on. A result, not a zero, and not the bottom of the scale."))
    rows[rows.index(("*", "", "")):1 + rows.index(("*", "", ""))] = ladder

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
    # One sheet, the whole taxonomy: L1 domain, L2 capability, L3 criterion,
    # each with its own definition, grouped so the reader can collapse to any
    # of the three.  Domains carry no assessment (ADR-0006) and criteria carry
    # no level (ADR-0014) - those cells are left empty rather than filled with
    # a zero.
    ws = wb.create_sheet("1. Capabilities")
    OBS0 = 7                              # first observation column
    NOBS = len(m.observation_types)
    LVLC, LNAME, WHY, LINK = (OBS0 + NOBS, OBS0 + NOBS + 1,
                              OBS0 + NOBS + 2, OBS0 + NOBS + 3)
    NC = LINK
    head(ws, [("Level", 6), ("ID", 9), ("Name", 38), ("Description", 58),
              ("Owner (Bank unit)", 26), ("Match", 11)]
             + [(t['id'].capitalize(), 10) for t in m.observation_types]
             + [("LEVEL", 8), ("Level name", 14), ("Why", 60),
                ("Assess it (click)", 18)])
    ws.sheet_properties.outlinePr.summaryBelow = False
    DOMHDR = PatternFill("solid", fgColor="C5D6E0")
    CAPHDR = PatternFill("solid", fgColor="EDF2F5")
    ACCF = Font(name=F, size=10, bold=True, color=ACC)

    # What each judgement column may say. Hover the header to read it. There is
    # no dropdown here on purpose: every cell on this sheet is computed, and a
    # dropdown would invite someone to type over a derived value.
    for k, t in enumerate(m.observation_types):
        crit = t['id'] in m.criterion_types
        hint(ws, OBS0 + k, "%s  -  recorded per %s"
             % (t['id'].upper(), "L3 criterion" if crit else "L2 capability"),
             "%s\n\nPossible values\n%s\n\n%s\nEvidence expected: %s"
             % (t['question'], values_block(m),
                ("On an L3 row this is the observation itself. On an L2 row it is "
                 "DERIVED from the L3 rows beneath it and is never typed: 'yes' only "
                 "when every criterion was examined and every one passed (ADR-0014)."
                 if crit else
                 "Asked once for the capability, so only L2 rows carry a value."),
                t['evidence_expected']),
             height=300)
    hint(ws, LVLC, "LEVEL  -  %s  (derived, never typed)" % scale.NAME,
         "%s\n\nPossible values\n%s\n\nBlank on an L1 domain row (a reporting "
         "cluster is never scored, ADR-0006) and on an L3 criterion row (a criterion "
         "carries an observation, not a level, ADR-0014).\n\n%s\n%s"
         % (scale.QUESTION, levels_block(scale), scale.BASIS,
            scale.note() if hasattr(scale, 'note') else ""),
         height=340, width=460)
    hint(ws, LNAME, "LEVEL NAME  -  the same value in words",
         "The name %s gives the level in the LEVEL column. Nothing else can appear "
         "here.\n\nPossible values\n%s"
         % (scale.NAME, levels_block(scale)), height=300, width=460)

    caprow, critrow = sheet2_rows(m)      # where sheet 2 puts each block

    def put(row, fills, level):
        """Write one row, then style what is present. Empty cells stay empty."""
        for j, v in enumerate(row, 1):
            cell = ws.cell(row=r, column=j, value=v)
            cell.border = BOX; cell.font = T
            cell.alignment = WRAP if j in (3, 4, 5, LNAME, WHY) else (
                CTR if j == 2 or 6 <= j <= LVLC or j == LINK else TOP)
            if j == 3:
                cell.alignment = Alignment(vertical="top", wrap_text=True,
                                           indent=level - 1)
            if fills.get(j):
                cell.fill = fills[j]
        ws.row_dimensions[r].outlineLevel = level - 1

    r = 2
    for d in m.domains:
        caps = [c for c in m.capabilities_sorted() if c['domain'] == d['id']]
        ncrit = sum(len(c['criteria']) for c in caps)
        row = (["L1", d['id'], d['name'], d['definition'], "", ""]
               + [""] * NOBS
               + ["", "", "%d capabilities, %d L3 criteria. A domain is a "
                          "reporting cluster and is never scored (ADR-0006)."
                          % (len(caps), ncrit), ""])
        put(row, dict.fromkeys(range(1, NC + 1), DOMHDR), 1)
        ws.cell(row=r, column=1).font = Font(name=F, size=10, bold=True, color=ACC)
        ws.cell(row=r, column=2).font = Font(name=F, size=11, bold=True, color=ACC)
        ws.cell(row=r, column=3).font = Font(name=F, size=11, bold=True, color=INK)
        ws.cell(row=r, column=4).font = TS
        ws.cell(row=r, column=WHY).font = TS
        ws.row_dimensions[r].height = 24
        r += 1

        for c in caps:
            vals = m.values(c['id'])
            lvl, why = m.rate(scale, c['id'])
            unit, match, _ = m.owner(c['id'])
            lname = dict((n, k) for n, k, _ in scale.LEVELS).get(lvl, "not rated")
            row = (["L2", c['id'], c['name'], c['definition'],
                    unit or "NO OWNER", match]
                   + [vals[t['id']] for t in m.observation_types]
                   + [lvl if lvl is not None else "-", lname, why,
                      ("%d criteria to judge" % len(c['criteria']))
                      if c['criteria'] else ""])
            fills = {j: CAPHDR for j in range(1, 7)}
            for k, t in enumerate(m.observation_types):
                fills[OBS0 + k] = PatternFill("solid",
                                              fgColor=VAL_FILL[vals[t['id']]])
            if lvl is not None:
                fills[LVLC] = PatternFill("solid", fgColor=LVL_FILL[lvl])
            put(row, fills, 2)
            ws.cell(row=r, column=1).font = TS
            ws.cell(row=r, column=2).font = ACCF
            ws.cell(row=r, column=3).font = B
            ws.cell(row=r, column=4).font = TS
            if not unit:
                ws.cell(row=r, column=5).font = Font(name=F, size=10, bold=True,
                                                     color="8E3226")
            for k, t in enumerate(m.observation_types):
                ws.cell(row=r, column=OBS0 + k).font = Font(
                    name=F, size=9, bold=True, color=VAL_FONT[vals[t['id']]])
            if lvl is not None:
                ws.cell(row=r, column=LVLC).font = Font(name=F, size=11,
                                                        bold=True, color="FFFFFF")
            ws.cell(row=r, column=WHY).font = TS
            if c['criteria']:
                cell = ws.cell(row=r, column=LINK)
                cell.font = Font(name=F, size=9, color="0000EE", underline="single")
                cell.hyperlink = Hyperlink(
                    ref="%s%d" % (get_column_letter(LINK), r),
                    location="'2. Observations'!A%d" % caprow[c['id']],
                    tooltip="Go to sheet 2 and judge the %d criteria behind %s"
                            % (len(c['criteria']), c['id']))
            ws.row_dimensions[r].height = 28
            r += 1

            # the criterion rows: the unit that is actually judged.  Only the
            # criterion-level observations have a value here; the rest are
            # asked once for the capability and are left blank.
            crit_obs = {tid: dict((x['id'], o) for x, o
                                  in m.criteria_obs(c['id'], tid))
                        for tid in m.criterion_types}
            for x in c['criteria']:
                obs = [crit_obs[t['id']].get(x['id'], {})
                       if t['id'] in m.criterion_types else None
                       for t in m.observation_types]
                seen = [o.get('value', 'unknown') if o is not None else ""
                        for o in obs]
                said = next((o.get('evidence') or o.get('basis') or ''
                             for o in obs if o), '')
                row = (["L3", x['id'], x['name'], x['definition'], "", ""]
                       + seen + ["", "", said, "judge this criterion"])
                fills = {}
                for k, v in enumerate(seen):
                    if v:
                        fills[OBS0 + k] = PatternFill("solid", fgColor=VAL_FILL[v])
                put(row, fills, 3)
                ws.cell(row=r, column=1).font = TS
                ws.cell(row=r, column=2).font = ACCF
                ws.cell(row=r, column=3).font = B
                ws.cell(row=r, column=4).font = TS
                for k, v in enumerate(seen):
                    if v:
                        ws.cell(row=r, column=OBS0 + k).font = Font(
                            name=F, size=9, bold=True, color=VAL_FONT[v])
                ws.cell(row=r, column=WHY).font = TS
                cell = ws.cell(row=r, column=LINK)
                cell.font = Font(name=F, size=9, color="0000EE", underline="single")
                cell.hyperlink = Hyperlink(
                    ref="%s%d" % (get_column_letter(LINK), r),
                    location="'2. Observations'!A%d"
                             % critrow[(m.criterion_types[0], x['id'])],
                    tooltip="Go to the row on sheet 2 that judges %s" % x['id'])
                ws.row_dimensions[r].height = 24
                r += 1

    ws.freeze_panes = "E2"
    ws.auto_filter.ref = "A1:%s%d" % (get_column_letter(NC), r - 1)
    note(ws, r + 1, NC,
         "THE WHOLE MODEL IN ONE VIEW, three levels deep: %d L1 domains, %d L2 "
         "capabilities, %d L3 criteria, each with its own description. Use the "
         "+/- outline handles at the left, or the 1/2/3 buttons above them, to "
         "collapse to domains, to capabilities, or to open the criteria; filter "
         "column A to one level to read it flat. "
         "READ ONLY - every column is computed. Observations are edited on sheet 2. "
         "A domain is a reporting cluster and is never scored (ADR-0006); a criterion "
         "carries an observation but no level of its own (ADR-0014). "
         "PRACTISED on an L2 row is rolled up from the L3 rows beneath it: it reads "
         "'yes' only when every criterion was examined and every one passed, so one "
         "unexamined criterion holds it at 'partial'. "
         "Scale: %s. %s  %s"
         % (len(m.domains), len(m.capabilities),
            sum(len(c['criteria']) for c in m.capabilities),
            scale.NAME, scale.BASIS,
            scale.note() if hasattr(scale, 'note') else ""), 58)


    # =============================================== 2. Observations
    ws = wb.create_sheet("2. Observations")
    head(ws, [("Capability", 11), ("Name", 26), ("Observation", 12),
              ("L3 criterion", 11), ("What you are judging", 30),
              ("The question", 46), ("VALUE", 11), ("Evidence", 42),
              ("Observed by", 20), ("Date", 12), ("Basis / why", 46)])
    q = {t['id']: t['question'] for t in m.observation_types}
    SUBHDR = PatternFill("solid", fgColor="DEE9EF")
    r = 2
    obsrow = {}                       # re-derived here, checked against sheet 1
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
    dv = DataValidation(type="list",
                        formula1='"%s"' % ",".join(m.observation_values),
                        allow_blank=False, showErrorMessage=True,
                        errorTitle="Observation value",
                        error="yes / partial / no / n/a (needs a reason) / unknown (nobody has looked)")
    ws.add_data_validation(dv); dv.add("G2:G%d" % (r - 1))
    hint(ws, 7, "VALUE  -  what you record", "Pick from the dropdown. Nothing else "
         "is accepted.\n\nPossible values\n%s" % values_block(m), height=240)
    if obsrow != caprow:
        raise AssertionError("sheet 1's links no longer match sheet 2's layout")
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
    # The definition sheet, same three levels as sheet 1: every domain,
    # capability and criterion with the words that say what it means.
    ws = wb.create_sheet("6. Criteria (L3)")
    head(ws, [("Level", 6), ("ID", 10), ("Name", 40), ("Definition", 84),
              ("Owner (Bank unit)", 26), ("Contains", 18), ("Agentic", 9)])
    ws.sheet_properties.outlinePr.summaryBelow = False
    DOMHDR = PatternFill("solid", fgColor="C5D6E0")
    CAPHDR = PatternFill("solid", fgColor="EDF2F5")
    r = 2
    for d in m.domains:
        caps = [c for c in m.capabilities_sorted() if c['domain'] == d['id']]
        ncrit = sum(len(c['criteria']) for c in caps)
        rows = [("L1", d['id'], d['name'], d['definition'], "",
                 "%d capabilities, %d criteria" % (len(caps), ncrit), "", 1)]
        for c in caps:
            rows.append(("L2", c['id'], c['name'], c['definition'],
                         m.owner(c['id'])[0] or "no owner in the catalogue",
                         "%d L3 criteria" % len(c['criteria']),
                         "yes" if c['agentic'] else "", 2))
            for x in c['criteria']:
                rows.append(("L3", x['id'], x['name'], x['definition'], "", "",
                             "yes" if x['agentic'] else "", 3))
        for lvl, cid, name, defn, owner, contains, ag, level in rows:
            for j, v in enumerate([lvl, cid, name, defn, owner, contains, ag], 1):
                cell = ws.cell(row=r, column=j, value=v)
                cell.border = BOX; cell.font = T
                cell.alignment = WRAP if j in (4, 5, 6) else (
                    CTR if j in (1, 2, 7) else TOP)
                if j == 3:
                    cell.alignment = Alignment(vertical="top", wrap_text=True,
                                               indent=level - 1)
                if level < 3:
                    cell.fill = DOMHDR if level == 1 else CAPHDR
            size = 11 if level == 1 else 10
            ws.cell(row=r, column=1).font = TS if level > 1 else Font(
                name=F, size=10, bold=True, color=ACC)
            ws.cell(row=r, column=2).font = Font(name=F, size=size, bold=True,
                                                 color=ACC)
            ws.cell(row=r, column=3).font = Font(name=F, size=size, bold=True,
                                                 color=INK)
            ws.cell(row=r, column=4).font = TS
            ws.cell(row=r, column=6).font = TS
            ws.row_dimensions[r].outlineLevel = level - 1
            ws.row_dimensions[r].height = {1: 24, 2: 22}.get(level, 24)
            r += 1
    ws.freeze_panes = "D2"; ws.auto_filter.ref = "A1:G%d" % (r - 1)
    note(ws, r + 1, 7,
         "WHAT EVERY ROW OF THE MODEL MEANS: %d L1 domains, %d L2 capabilities and "
         "%d L3 criteria, each with its full definition, nested three deep. Use the "
         "+/- outline handles, or the 1/2/3 buttons above them, to collapse to "
         "domains, to capabilities, or to open the criteria; filter column A to one "
         "level to read it flat. This sheet is the REFERENCE - read it to understand "
         "what a row means. You JUDGE the criteria on sheet 2, which carries one "
         "Practised row for each of them, and sheet 1 shows the same three levels "
         "with the observations and the derived level against them. "
         "Criteria carry no level of their own: they carry an observation, and the "
         "capability's Practised value is derived from them (ADR-0014)."
         % (len(m.domains), len(m.capabilities),
            sum(len(c['criteria']) for c in m.capabilities)), 46)


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

# -*- coding: utf-8 -*-
"""Taxonomy-only review workbook: 8 domains / 52 L2 / 258 L3 with decision columns."""
import json
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

M = json.load(open('model3.json'))
import idb_owners as IDB
OUT = 'AI-Capability-Taxonomy-for-review.xlsx'

ARIAL = 'Arial'
NAVY   = 'FF1F3864'
BLUE   = 'FFDCE6F1'
GREY   = 'FFF2F2F2'
YELLOW = 'FFFFF2CC'
GREEN  = 'FFE2EFDA'
RED    = 'FFF8CBAD'
AMBER  = 'FFFFE699'
MATCH_FILL = {'Direct': GREEN, 'Inferred': 'FFEDF3E8', 'Partial': AMBER, 'NO MATCH': RED}
thin = Side(style='thin', color='FFBFBFBF')
BORD = Border(left=thin, right=thin, top=thin, bottom=thin)

# what changed in this round
NEW_L2  = {'1.5', '2.6'}
CHANGED_L2 = {'8.6'}
NOTE = {
 '1.4': 'Boundary check: 1.4 is now procurement/contract only. Ecosystem-level dependency moved to 1.5.',
 '1.4.4': 'Boundary check: per-supplier concentration and exit. Aggregate ecosystem dependency is 1.5.5 - confirm the split holds.',
 '1.5': 'ADDED this round. Gap found against an external reference model: 1.4 had no home for non-supplier relationships (academic, multilateral, peer institutions).',
 '1.5.5': 'Boundary check against 1.4.4 - see note there.',
 '2.1': 'Boundary check: 2.1 is the controlled front door for demand that is already a request. 2.6 is what happens before an idea is a request.',
 '2.1.1': 'Boundary check: overlaps 2.6.1. Options: keep both (2.1.1 = business-need sourcing into the funnel, 2.6.1 = open idea capture), or merge into 2.6.1.',
 '2.6': 'ADDED this round. Alternative home: D1 (strategy) or D8 (culture). Placed in D2 because incubation feeds demand. Your call.',
 '2.6.1': 'Boundary check against 2.1.1 - see note there.',
 '2.6.5': 'Absorbs former 8.6.4 Experimentation & Learning Culture.',
 '8.6': 'CHANGED this round: 8.6.4 Experimentation & Learning Culture removed and promoted into 2.6. 8.6 now has 3 L3.',
}

wb = Workbook()

# ---------------------------------------------------------------- Read me
ws = wb.active; ws.title = '0. Read me'
ws.column_dimensions['A'].width = 3
ws.column_dimensions['B'].width = 34
ws.column_dimensions['C'].width = 96
rows = [
 ('h', 'AI Capability Taxonomy - for review', ''),
 ('', '', 'Structure only. No maturity, no readiness, no realizations, no evidence. Those live in the assessment workbook.'),
 ('', '', 'Purpose: agree the shape of the map before anything is scored against it.'),
 ('s', 'How to use it', ''),
 ('', '1. Read sheet "1. Taxonomy"', 'One row per node. Domains and L2 capabilities are frozen at the top; L3 rows collapse with the +/- controls in the left margin.'),
 ('', '2. Fill column L "Decision"', 'Pick from the dropdown. Blank means Keep - you only need to touch the rows you disagree with.'),
 ('', '3. Use M and N', '"Rename to" for a better name. "Notes" for anything else - wrong owner, wrong domain, missing sibling, definition too vague.'),
 ('', '4. Anything missing?', 'Add it on sheet "4. Proposed additions". One row per capability you think is absent. Rough wording is fine.'),
 ('', '5. Send it back', 'Nothing else needs filling. I will apply the decisions to the model and rebuild the assessment from it.'),
 ('s', 'What the columns mean', ''),
 ('', 'Level', 'Domain (8) > L2 capability (52) > L3 capability (258). L2 is the unit that gets assessed and owned.'),
 ('', 'Definition', 'Written as "Able to ..." at L2. The test is that one accountable owner could be held to it.'),
 ('', 'Owner', 'Proposed accountable role, not a person. Contested owners are the point of the review.'),
 ('', 'Anchor', 'How this relates to IDB\'s existing enterprise capability map: new = no equivalent today; specialization = an AI-specific narrowing of one that exists; lens = do NOT create a node, the existing enterprise capability already covers it and this is only an AI view of it.'),
 ('', 'Agentic', 'Y = this capability only becomes necessary once agents act autonomously. Used to phase the roadmap.'),
 ('', 'Confidence', 'How settled I consider the node. low = expect to change it. Prioritise your reading there.'),
 ('', 'Sources', 'The published frameworks the node was derived from, so you can check it rather than take it on trust.'),
 ('s', 'Changed in this round', ''),
 ('', 'Added 1.5', 'AI Ecosystem & Alliance Management (D1) - non-supplier external relationships. 1.4 was procurement-shaped only.'),
 ('', 'Added 2.6', 'AI Innovation & Incubation (D2) - idea to evidence to funded product, or a cheap recorded stop.'),
 ('', 'Removed 8.6.4', 'Experimentation & Learning Culture, promoted into 2.6 so experimentation is an owned capability rather than a cultural aspiration.'),
 ('s', 'Counts', ''),
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
        cc = ws.cell(r, 3, c); cc.font = Font(name=ARIAL, size=10); cc.alignment = Alignment(wrap_text=True, vertical='top')
        ws.row_dimensions[r].height = 28 if len(c) > 110 else 14
    r += 1
CNT = r
for lbl, crit in (('Domains', 'Domain'), ('L2 capabilities', 'L2'), ('L3 capabilities', 'L3')):
    ws.cell(r, 2, lbl).font = Font(name=ARIAL, size=10, bold=True)
    ws.cell(r, 3, '=COUNTIF(\'1. Taxonomy\'!$A:$A,"%s")' % crit).font = Font(name=ARIAL, size=10)
    r += 1
ws.cell(r, 2, 'Rows you have marked').font = Font(name=ARIAL, size=10, bold=True)
ws.cell(r, 3, '=COUNTA(\'1. Taxonomy\'!$P$2:$P$400)').font = Font(name=ARIAL, size=10)
r += 1
for lbl, m in (('Owners - direct match', 'Direct'), ('Owners - inferred', 'Inferred'),
               ('Owners - partial', 'Partial'), ('Capabilities with NO owner', 'NO MATCH')):
    ws.cell(r, 2, lbl).font = Font(name=ARIAL, size=10, bold=True)
    ws.cell(r, 3, '=COUNTIF(\'1. Taxonomy\'!$H$2:$H$400,"%s")' % m).font = Font(name=ARIAL, size=10)
    r += 1
ws.sheet_view.showGridLines = False

# ---------------------------------------------------------------- Taxonomy
ws = wb.create_sheet('1. Taxonomy')
HDR = ['Level', 'ID', 'Domain', 'Name', 'Definition',
       'Owner - IDB product / enabler', 'Lead', 'Match', 'Basis / what to settle',
       'Previously proposed role', 'Anchor', 'Agentic', 'Confidence', 'Sources',
       'Change this round', 'Decision', 'Rename to',
       'Owner decision', 'Correct owner', 'Notes']
W   = [9, 8, 7, 42, 76, 30, 24, 11, 78, 26, 14, 9, 11, 36, 17, 20, 26, 20, 28, 50]
for i, h in enumerate(HDR, 1):
    c = ws.cell(1, i, h)
    c.font = Font(name=ARIAL, size=10, bold=True, color='FFFFFFFF')
    c.fill = PatternFill('solid', fgColor=NAVY)
    c.alignment = Alignment(wrap_text=True, vertical='center')
    ws.column_dimensions[get_column_letter(i)].width = W[i-1]
ws.row_dimensions[1].height = 30

r = 2
for d in M:
    did, dname, ddef, l2s = d[0], d[1], d[2], d[3]
    ws.cell(r, 1, 'Domain'); ws.cell(r, 2, did); ws.cell(r, 3, did)
    ws.cell(r, 4, dname); ws.cell(r, 5, ddef)
    ws.cell(r, len(HDR), NOTE.get(did, ''))
    for col in range(1, len(HDR) + 1):
        cell = ws.cell(r, col)
        cell.fill = PatternFill('solid', fgColor=BLUE)
        cell.font = Font(name=ARIAL, size=11, bold=True, color=NAVY)
        cell.border = BORD
        cell.alignment = Alignment(wrap_text=True, vertical='top')
    r += 1
    for l2 in l2s:
        lid, lname, ldef, prov, l3s, agentic, anchor, owner, conf = l2
        own_name, match, basis = IDB.MAP.get(lid, ('', 'NOT MAPPED', ''))
        rec = IDB.OWNER_BY_NAME.get(own_name)
        lead = ''
        if rec:
            lead = ' / '.join(x for x in (rec[3], rec[4]) if x)
        vals = [ 'L2', lid, did, lname, ldef,
                 own_name or '— none in the catalogue —', lead, match, basis, owner,
                 anchor, 'Y' if agentic else '', conf, '; '.join(prov),
                 'NEW' if lid in NEW_L2 else ('CHANGED' if lid in CHANGED_L2 else ''),
                 '', '', '', '', NOTE.get(lid, '') ]
        for col, v in enumerate(vals, 1):
            cell = ws.cell(r, col, v)
            cell.fill = PatternFill('solid', fgColor=GREY)
            cell.font = Font(name=ARIAL, size=10, bold=(col <= 6))
            cell.border = BORD
            cell.alignment = Alignment(wrap_text=True, vertical='top')
        mc = ws.cell(r, 8)
        mc.fill = PatternFill('solid', fgColor=MATCH_FILL.get(match, GREY))
        mc.font = Font(name=ARIAL, size=10, bold=True,
                       color='FF9C0006' if match == 'NO MATCH' else 'FF0E1114')
        mc.alignment = Alignment(horizontal='center', vertical='top')
        if match == 'NO MATCH':
            ws.cell(r, 6).fill = PatternFill('solid', fgColor=RED)
            ws.cell(r, 6).font = Font(name=ARIAL, size=10, bold=True, color='FF9C0006')
        if lid in NEW_L2 or lid in CHANGED_L2:
            ws.cell(r, 15).fill = PatternFill('solid', fgColor=GREEN)
            ws.cell(r, 15).font = Font(name=ARIAL, size=10, bold=True, color='FF375623')
        for col in (16, 17, 18, 19, 20):
            ws.cell(r, col).fill = PatternFill('solid', fgColor=YELLOW)
        r += 1
        for l3 in l3s:
            ag = 'Y' if len(l3) > 3 and l3[3] else ''
            vals = ['L3', l3[0], did, l3[1], l3[2], '', '', '', '', '', '', ag, '', '',
                    'NEW' if l3[0].rsplit('.', 1)[0] in NEW_L2 else '',
                    '', '', '', '', NOTE.get(l3[0], '')]
            for col, v in enumerate(vals, 1):
                cell = ws.cell(r, col, v)
                cell.font = Font(name=ARIAL, size=10)
                cell.border = BORD
                cell.alignment = Alignment(wrap_text=True, vertical='top')
            ws.cell(r, 4).alignment = Alignment(wrap_text=True, vertical='top', indent=1)
            for col in (16, 17, 20):
                ws.cell(r, col).fill = PatternFill('solid', fgColor=YELLOW)
            ws.row_dimensions[r].outlineLevel = 1
            r += 1
LAST = r - 1
ws.sheet_properties.outlinePr.summaryBelow = False
dv = DataValidation(type='list', allow_blank=True, showDropDown=False,
    formula1='"Keep,Rename,Reword definition,Move to another domain,Merge with another,Split,Remove,Wrong owner,Not sure - discuss"')
ws.add_data_validation(dv); dv.add('P2:P%d' % LAST)
dvo = DataValidation(type='list', allow_blank=True, showDropDown=False,
    formula1='"Confirmed,Change owner,Split between two,Needs an owner that does not exist,Not sure - discuss"')
ws.add_data_validation(dvo); dvo.add('R2:R%d' % LAST)
ws.freeze_panes = 'D2'
ws.auto_filter.ref = 'A1:T%d' % LAST

# ---------------------------------------------------------------- IDB owners
def _sheet(name, hdr, widths, hrow=30):
    w = wb.create_sheet(name)
    for i, h in enumerate(hdr, 1):
        c = w.cell(1, i, h)
        c.font = Font(name=ARIAL, size=10, bold=True, color='FFFFFFFF')
        c.fill = PatternFill('solid', fgColor=NAVY)
        c.alignment = Alignment(wrap_text=True, vertical='center')
        w.column_dimensions[get_column_letter(i)].width = widths[i-1]
    w.row_dimensions[1].height = hrow
    return w

wo = _sheet('2. IDB owners',
    ['Product / enabler', 'Function', 'Family', 'Lead', 'Technical lead',
     'What they claim (from the fact sheet)', 'Capabilities mapped to them'],
    [34, 12, 34, 30, 26, 96, 34])
_count = {}
for _k, _v in IDB.MAP.items():
    if _v[0]:
        _count.setdefault(_v[0], []).append(_k)
r = 2
for o in IDB.IDB_OWNERS:
    mapped = sorted(_count.get(o[0], []), key=lambda x: [int(p) for p in x.split('.')])
    vals = list(o[:6]) + [(', '.join(mapped) + '   (' + str(len(mapped)) + ')') if mapped
                          else '— none —']
    for i, v in enumerate(vals, 1):
        c = wo.cell(r, i, v)
        c.font = Font(name=ARIAL, size=10, bold=(i == 1))
        c.border = BORD
        c.alignment = Alignment(wrap_text=True, vertical='top')
    if not mapped:
        wo.cell(r, 7).fill = PatternFill('solid', fgColor=GREY)
    r += 1
wo.freeze_panes = 'B2'
note = ('Source: ' + IDB.SOURCE_FILE + ', sheet "' + IDB.SOURCE_SHEET + '", read ' + IDB.READ_ON
        + '. Only the products and enablers that could plausibly own an AI capability are listed; '
          'the catalogue also holds business products (Treasury, Impact Management, Project Design '
          'and so on) that own none.')
c = wo.cell(r + 1, 1, note)
c.font = Font(name=ARIAL, size=10, italic=True)
c.alignment = Alignment(wrap_text=True, vertical='top')
wo.merge_cells(start_row=r + 1, start_column=1, end_row=r + 3, end_column=7)

# ---------------------------------------------------------------- Unowned
wu = _sheet('3. No owner or partial',
    ['Match', 'ID', 'Capability', 'Domain', 'Nearest owner in the catalogue',
     'What is missing', 'Your decision', 'Who should own it'],
    [11, 8, 42, 8, 30, 96, 22, 30])
NAMES = {}
for _d in M:
    for _l2 in _d[3]:
        NAMES[_l2[0]] = (_l2[1], _d[0])
r = 2
for want in ('NO MATCH', 'Partial'):
    for cid, (own, match, basis) in sorted(
            IDB.MAP.items(), key=lambda kv: [int(p) for p in kv[0].split('.')]):
        if match != want:
            continue
        nm, dm = NAMES[cid]
        vals = [match, cid, nm, dm, own or '— none —', basis, '', '']
        for i, v in enumerate(vals, 1):
            c = wu.cell(r, i, v)
            c.font = Font(name=ARIAL, size=10, bold=(i == 3))
            c.border = BORD
            c.alignment = Alignment(wrap_text=True, vertical='top')
        wu.cell(r, 1).fill = PatternFill('solid', fgColor=MATCH_FILL[match])
        wu.cell(r, 1).font = Font(name=ARIAL, size=10, bold=True,
                                  color='FF9C0006' if match == 'NO MATCH' else 'FF0E1114')
        for i in (7, 8):
            wu.cell(r, i).fill = PatternFill('solid', fgColor=YELLOW)
        r += 1
dvu = DataValidation(type='list', allow_blank=True, showDropDown=False,
    formula1='"Assign to the nearest owner,Assign to someone else,Needs a new role,'
             'Out of scope - drop the capability,Not sure - discuss"')
wu.add_data_validation(dvu); dvu.add('G2:G%d' % (r - 1))
wu.freeze_panes = 'C2'; wu.auto_filter.ref = 'A1:H%d' % (r - 1)

# ---------------------------------------------------------------- Additions
ws = wb.create_sheet('4. Proposed additions')
H2 = ['Proposed name', 'Level (L2 or L3)', 'Which domain / parent', 'What it means ("Able to ...")',
      'Proposed owner', 'Why it is missing / where you have seen it needed']
W2 = [40, 16, 26, 76, 26, 70]
for i, h in enumerate(H2, 1):
    c = ws.cell(1, i, h)
    c.font = Font(name=ARIAL, size=10, bold=True, color='FFFFFFFF')
    c.fill = PatternFill('solid', fgColor=NAVY)
    c.alignment = Alignment(wrap_text=True, vertical='center')
    ws.column_dimensions[get_column_letter(i)].width = W2[i-1]
ws.row_dimensions[1].height = 30
ex = ['AI Model Hosting Cost Attribution', 'L3', '6.5 AI Cost Management',
      'Able to attribute inference and hosting spend back to the consuming business unit.',
      'FinOps Owner', 'EXAMPLE ROW - overwrite or delete. Raised by Finance during budget review.']
for i, v in enumerate(ex, 1):
    c = ws.cell(2, i, v)
    c.font = Font(name=ARIAL, size=10, italic=True, color='FF808080')
    c.alignment = Alignment(wrap_text=True, vertical='top')
for rr in range(3, 41):
    for i in range(1, 7):
        c = ws.cell(rr, i); c.font = Font(name=ARIAL, size=10)
        c.fill = PatternFill('solid', fgColor=YELLOW)
        c.alignment = Alignment(wrap_text=True, vertical='top')
dv2 = DataValidation(type='list', allow_blank=True, showDropDown=False, formula1='"L2,L3"')
ws.add_data_validation(dv2); dv2.add('B2:B40')
ws.freeze_panes = 'A2'

wb.save(OUT)
print('written', OUT, 'last row', LAST)

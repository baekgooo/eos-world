#!/usr/bin/env python3
"""Restore full grid from _section3_output.html, then apply targeted fixes."""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')

# ── 1. Read source files ───────────────────────────────────────────────────
with open('docs/naming-rules-preview.html', encoding='utf-8') as f:
    html = f.read()

with open('scripts/_section3_output.html', encoding='utf-8') as f:
    src = f.read()

# ── 2. Extract full flow-grid from _section3_output.html ──────────────────
# Find <div class="flow-grid" id="flowGrid"> ... </div>  (last </div> in src)
m = re.search(r'(<div class="flow-grid" id="flowGrid">.*?</div>)\s*</div>', src, re.DOTALL)
if not m:
    sys.exit('ERROR: could not find flow-grid in _section3_output.html')
grid_html = m.group(1)
print(f'Extracted grid: {len(grid_html)} chars')

# Verify node count
nodes_in_grid = re.findall(r'data-section="S\w+"', grid_html)
print(f'Nodes in grid: {len(nodes_in_grid)}')

# ── 3. Fix ending section layout INSIDE grid_html ─────────────────────────
# Strategy: exact string operations, no DOTALL wildcards over large spans.

# 3a. Extract individual button HTML for S079, S078, S081, S080
def get_button(sid, text):
    # Find <button ... data-section="SID" ...>...</button>
    # Use a targeted pattern: from <button up to next </button>
    idx = text.find(f'data-section="{sid}"')
    if idx < 0:
        return None, -1, -1
    # Walk backward to find the opening <button
    start = text.rfind('<button', 0, idx)
    # Walk forward to find the closing </button>
    end = text.find('</button>', idx) + len('</button>')
    return text[start:end], start, end

btn_s079, _, _ = get_button('S079', grid_html)
btn_s078, _, _ = get_button('S078', grid_html)
btn_s081, _, _ = get_button('S081', grid_html)
btn_s080, _, _ = get_button('S080', grid_html)

for name, btn in [('S079', btn_s079), ('S078', btn_s078), ('S081', btn_s081), ('S080', btn_s080)]:
    if btn:
        print(f'{name}: found ({len(btn)} chars)')
    else:
        print(f'{name}: MISSING!')

# 3b. Find the exact row strings for the ending section
# Original layout in _section3_output.html:
#   branch-row: S079 + S081
#   single-row: S078
#   chapter-band: 엔딩
#   single-row: S080

row_branch_old = f'<div class="flow-row branch-row">{btn_s079} {btn_s081}</div>'
row_single_s078 = f'<div class="flow-row single-row">{btn_s078}</div>'
row_band_ending = '<div class="chapter-band">엔딩</div>'
row_single_s080 = f'<div class="flow-row single-row">{btn_s080}</div>'

# New layout:
#   branch-row: S079 + S078 + S081
#   single-row: S080   (no 엔딩 band)
row_branch_new = f'<div class="flow-row branch-row">{btn_s079} {btn_s078} {btn_s081}</div>'

# Check all old rows are present
for label, row in [
    ('branch S079+S081', row_branch_old),
    ('single S078',      row_single_s078),
    ('band 엔딩',         row_band_ending),
    ('single S080',      row_single_s080),
]:
    present = row in grid_html
    print(f'  {"✓" if present else "✗"} {label}')

# 3c. Apply replacements (order matters)
# First remove the S078 single row (we'll add it into branch row)
grid_html = grid_html.replace('\n        ' + row_single_s078, '', 1)
# Remove the 엔딩 band
grid_html = grid_html.replace('\n        ' + row_band_ending, '', 1)
# Replace branch row with new merged one
grid_html = grid_html.replace(row_branch_old, row_branch_new, 1)

# Verify
print('After fix:')
print(f'  엔딩 band gone: {"✓" if row_band_ending not in grid_html else "✗"}')
print(f'  S078 in branch: {"✓" if btn_s078 in grid_html else "✗"}')
pat = r'data-section="S\w+"'
print(f'  Nodes count: {len(re.findall(pat, grid_html))}')

# ── 4. Replace flow-grid in naming-rules-preview.html ─────────────────────
# Find <div class="flow-grid" id="flowGrid"> ... </div>  in html
m2 = re.search(r'<div class="flow-grid" id="flowGrid">.*?</div>(?=\s*</div>)', html, re.DOTALL)
if not m2:
    sys.exit('ERROR: could not find flow-grid in naming-rules-preview.html')
print(f'\nReplacing grid in preview HTML (old: {len(m2.group(0))} chars, new: {len(grid_html)} chars)')
html = html[:m2.start()] + grid_html + html[m2.end():]

# ── 5. Verify z-index / CSS (should still be there from v2 run) ──────────
checks = [
    ('z-index: 0' in html and 'z-index: -1' not in html, 'edge-layer z-index:0'),
    ('position: relative;\n  z-index: 1;\n  display: flex' in html, 'flow-grid z-index:1'),
    ('.flow-node.decision.minor { background: #e8f0e9; border-color: #b8cfba; width:' in html or
     'border-color: #b8cfba; width: 110px' in html, 'no border-radius on minor'),
    ('.flow-node.ending { background: #f1f1f1; border-color: #aaa; width: 130px; }' in html, 'no border-radius on ending'),
    ('marker-end' in html, 'marker-end on paths'),
    ('getElementById(\'arr\')' in html, 'arrow marker JS'),
]
for ok, label in checks:
    print(f'  {"✓" if ok else "✗"} {label}')

# ── 6. Verify grid node count in final html ───────────────────────────────
nodes_final = re.findall(r'data-section="S\w+"', html)
# Exclude duplicates from sectionData JSON
html_grid_part = html[html.find('<div class="flow-canvas"'):html.find('</div>\n\n    <script type')]
nodes_grid = re.findall(r'data-section="S\w+"', html_grid_part)
print(f'\nNodes in flow-grid: {len(nodes_grid)} (expected 118)')

# ── 7. Save ───────────────────────────────────────────────────────────────
with open('docs/naming-rules-preview.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Saved.')

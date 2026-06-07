#!/usr/bin/env python3
"""Fix flowchart: z-index, node shapes, ending layout, arrowheads"""
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('docs/naming-rules-preview.html', encoding='utf-8') as f:
    content = f.read()

# ── 1. z-index fix ─────────────────────────────────────────────────────────
# edge-layer: z-index -1 hides it behind flow-canvas background → change to 0
content = content.replace(
    'top: 0; left: 0; z-index: -1; pointer-events: none; overflow: visible; }',
    'top: 0; left: 0; z-index: 0; pointer-events: none; overflow: visible; }'
)

# flow-grid needs position:relative + z-index:1 so buttons stack above SVG
content = content.replace(
    '.flow-grid {\n  display: flex;',
    '.flow-grid {\n  position: relative;\n  z-index: 1;\n  display: flex;'
)
print('1. z-index fixed')

# ── 2. Node shapes: remove rounded corners everywhere ─────────────────────
content = content.replace(
    '.flow-node.decision.minor { background: #e8f0e9; border-color: #b8cfba; border-radius: 12px; width: 110px; min-height: 44px; }',
    '.flow-node.decision.minor { background: #e8f0e9; border-color: #b8cfba; width: 110px; min-height: 44px; }'
)
content = content.replace(
    '.flow-node.ending { background: #f1f1f1; border-color: #aaa; border-radius: 999px; width: 130px; }',
    '.flow-node.ending { background: #f1f1f1; border-color: #aaa; width: 130px; }'
)
print('2. Node shapes fixed (no border-radius)')

# ── 3. Ending layout: remove "엔딩" band, merge S079/S078/S081 in one row ──
# Parse out the four individual buttons we need to rearrange
def extract_btn(sid, text):
    """Extract the full <button...>...</button> for a given data-section"""
    pattern = rf'(<button[^>]+data-section="{re.escape(sid)}"[^>]*>.*?</button>)'
    m = re.search(pattern, text, re.DOTALL)
    return m.group(1) if m else None

btn_s079 = extract_btn('S079', content)
btn_s078 = extract_btn('S078', content)
btn_s081 = extract_btn('S081', content)
btn_s080 = extract_btn('S080', content)

if all([btn_s079, btn_s078, btn_s081, btn_s080]):
    # Build new ending rows
    new_ending = (
        f'        <div class="flow-row branch-row">{btn_s079} {btn_s078} {btn_s081}</div>\n'
        f'        <div class="flow-row single-row">{btn_s080}</div>'
    )

    # Find and replace the old 4-part ending section (S079+S081 branch, S078 single, band, S080 single)
    old_pattern = re.compile(
        r'        <div class="flow-row branch-row">.*?data-section="S079".*?</div>\s*'
        r'<div class="flow-row single-row">.*?data-section="S078".*?</div>\s*'
        r'<div class="chapter-band">엔딩</div>\s*'
        r'<div class="flow-row single-row">.*?data-section="S080".*?</div>',
        re.DOTALL
    )
    content, n = old_pattern.subn(new_ending, content)
    print(f'3. Ending layout fixed ({n} replacements)')
else:
    missing = [s for s, b in [('S079',btn_s079),('S078',btn_s078),('S081',btn_s081),('S080',btn_s080)] if not b]
    print(f'3. WARNING: could not find buttons for {missing}')

# ── 4. Arrowheads ──────────────────────────────────────────────────────────
# a) Add marker setup inside renderEdges() after path cleanup
old_cleanup = '[...edgeLayer.querySelectorAll(\'path.edge\')].forEach(p=>p.remove());'
new_cleanup = (
    '[...edgeLayer.querySelectorAll(\'path.edge\')].forEach(p=>p.remove());\n'
    '  if(!document.getElementById(\'arr\')){const defs=document.createElementNS(\'http://www.w3.org/2000/svg\',\'defs\');'
    'const mk=document.createElementNS(\'http://www.w3.org/2000/svg\',\'marker\');'
    'mk.setAttribute(\'id\',\'arr\');mk.setAttribute(\'viewBox\',\'0 0 4 4\');'
    'mk.setAttribute(\'refX\',\'4\');mk.setAttribute(\'refY\',\'2\');'
    'mk.setAttribute(\'markerWidth\',\'4\');mk.setAttribute(\'markerHeight\',\'4\');'
    'mk.setAttribute(\'orient\',\'auto\');mk.setAttribute(\'markerUnits\',\'userSpaceOnUse\');'
    'const pl=document.createElementNS(\'http://www.w3.org/2000/svg\',\'polygon\');'
    'pl.setAttribute(\'points\',\'0,0 4,2 0,4\');pl.setAttribute(\'fill\',\'#b9afa5\');'
    'mk.appendChild(pl);defs.appendChild(mk);edgeLayer.insertBefore(defs,edgeLayer.firstChild);}'
)
if old_cleanup in content:
    content = content.replace(old_cleanup, new_cleanup, 1)
    print('4a. Arrowhead marker setup added')
else:
    print('4a. WARNING: could not find path cleanup line')

# b) Add marker-end to each path — insert after path.setAttribute('class','edge');
old_class = "path.setAttribute('class','edge');"
new_class = "path.setAttribute('class','edge');path.setAttribute('marker-end','url(#arr)');"
if old_class in content:
    content = content.replace(old_class, new_class, 1)
    print('4b. marker-end attribute added to paths')
else:
    print('4b. WARNING: could not find path class line')

# ── 5. Save ────────────────────────────────────────────────────────────────
with open('docs/naming-rules-preview.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('\nAll done. Verifying...')
# Quick sanity checks
checks = [
    ('z-index: 0;' in content and 'z-index: -1' not in content, 'z-index:0 on edge-layer'),
    ('z-index: 1;\n  display: flex' in content, 'flow-grid z-index:1'),
    ('border-radius: 12px' not in content, 'no rounded minor'),
    ('border-radius: 999px' not in content, 'no pill ending'),
    ('chapter-band">엔딩' not in content, 'no 엔딩 band'),
    ('marker-end' in content, 'marker-end on paths'),
    ('id=\'arr\'' in content or "id='arr'" in content, 'arrow marker'),
    (content.count('data-section="S079"') == 1, 'S079 appears once'),
    (content.count('data-section="S080"') == 1, 'S080 appears once'),
]
for ok, label in checks:
    print(f'  {"✓" if ok else "✗"} {label}')

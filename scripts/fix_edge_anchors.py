#!/usr/bin/env python3
"""
Add custom anchor point overrides to renderEdges() in both flowchart files.
"""
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

CUSTOM_ANCHORS_JS = (
    "const CUSTOM_ANCHORS={"
    "'S030:S031':{from:'bottom',to:'top',straight:true},"
    "'S039:S040':{from:'bottom',to:'top',straight:true},"
    "'S053:S054':{from:'bottom',to:'top',straight:true},"
    "'S063:S064':{from:'bottom',to:'top',straight:true},"
    "'S045:S051':{to:'left'},"
    "'S047A:S051':{to:'left'},"
    "'S047B:S051':{to:'right'},"
    "'S048A:S050':{to:'left'},"
    "'S048B:S050':{to:'right'},"
    "'S057:S058':{to:'left'},"
    "'S068:S070':{to:'left'},"
    "'S075:S076A':{to:'right'},"
    "'S077:S081':{to:'right'},"
    "'S078:S080':{to:'right'},"
    "'S077:S079':{to:'right'},"
    "'S076:S077':{from:'left'}"
    "};"
)

CURVE_PATH_JS = (
    "const curvePath=(sx,sy,ex,ey,fromDir,toDir)=>{"
    "const dx=Math.abs(ex-sx),dy=Math.abs(ey-sy);"
    "const t=Math.max(50,(dx+dy)*0.4);"
    "let cp1x=sx,cp1y=sy,cp2x=ex,cp2y=ey;"
    "if(fromDir==='bottom')cp1y=sy+t;else if(fromDir==='top')cp1y=sy-t;"
    "else if(fromDir==='left')cp1x=sx-t;else if(fromDir==='right')cp1x=sx+t;"
    "if(toDir==='top')cp2y=ey-t;else if(toDir==='bottom')cp2y=ey+t;"
    "else if(toDir==='left')cp2x=ex-t;else if(toDir==='right')cp2x=ex+t;"
    "return `M ${sx} ${sy} C ${cp1x} ${cp1y}, ${cp2x} ${cp2y}, ${ex} ${ey}`;"
    "};"
)

CUSTOM_ANCHOR_CHECK_JS = (
    "    const ca=CUSTOM_ANCHORS[edge.from+':'+edge.to];\n"
    "    if(ca){\n"
    "      const fromDir=ca.from||(downward?'bottom':'top');\n"
    "      const toDir=ca.to||(downward?'top':'bottom');\n"
    "      const start=point(ar,a,fromDir);\n"
    "      const end=point(br,b,toDir);\n"
    "      if(ca.straight){\n"
    "        path.setAttribute('d',`M ${start.x} ${start.y} L ${end.x} ${end.y}`);\n"
    "      }else{\n"
    "        path.setAttribute('d',curvePath(start.x,start.y,end.x,end.y,fromDir,toDir));\n"
    "      }\n"
    "    }else "
)

# ── naming-rules-preview.html ─────────────────────────────────────────────────
print('=== docs/naming-rules-preview.html ===')
with open('docs/naming-rules-preview.html', encoding='utf-8') as f:
    html = f.read()

# 1. Add left/right support to point()
OLD_POINT_RETURN = "    return {x:centerX,y:(where==='bottom'?rect.bottom:where==='top'?rect.top:rect.top+rect.height/2)-box.top+flowCanvas.scrollTop};"
NEW_POINT_RETURN = (
    "    if(where==='left') return {x:rect.left-box.left+flowCanvas.scrollLeft,y:centerY};\n"
    "    if(where==='right') return {x:rect.right-box.left+flowCanvas.scrollLeft,y:centerY};\n"
    "    return {x:centerX,y:(where==='bottom'?rect.bottom:where==='top'?rect.top:rect.top+rect.height/2)-box.top+flowCanvas.scrollTop};"
)
if OLD_POINT_RETURN in html:
    html = html.replace(OLD_POINT_RETURN, NEW_POINT_RETURN, 1)
    print('  ✓ point() left/right added')
else:
    print('  ✗ could not find point() return line')

# 2. Add CUSTOM_ANCHORS + curvePath after marker setup, before sideRoutes
OLD_SIDEROUTES = "  const sideRoutes=new Map();"
NEW_SIDEROUTES = f"  {CUSTOM_ANCHORS_JS}\n  {CURVE_PATH_JS}\n  {OLD_SIDEROUTES}"
if OLD_SIDEROUTES in html:
    html = html.replace(OLD_SIDEROUTES, NEW_SIDEROUTES, 1)
    print('  ✓ CUSTOM_ANCHORS + curvePath added (naming-rules)')
else:
    print('  ✗ could not find sideRoutes declaration')

# 3. Insert custom anchor check before sameColumn&&longJump branch
OLD_IF_SAME = "    if(sameColumn&&longJump){"
NEW_IF_SAME = CUSTOM_ANCHOR_CHECK_JS + "if(sameColumn&&longJump){"
if OLD_IF_SAME in html:
    html = html.replace(OLD_IF_SAME, NEW_IF_SAME, 1)
    print('  ✓ custom anchor check inserted')
else:
    print('  ✗ could not find sameColumn&&longJump branch')

with open('docs/naming-rules-preview.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('  Saved.\n')

# ── big-workshop.html ─────────────────────────────────────────────────────────
print('=== docs/big-workshop.html ===')
with open('docs/big-workshop.html', encoding='utf-8') as f:
    bw = f.read()

# 1. Add left/right support to point()
# big-workshop uses multi-line return
OLD_POINT_BW = (
    "    return {\n"
    "      x:centerX,\n"
    "      y:(where==='bottom'?rect.bottom:where==='top'?rect.top:rect.top+rect.height/2)-box.top+flowCanvas.scrollTop\n"
    "    };"
)
NEW_POINT_BW = (
    "    if(where==='left') return {x:rect.left-box.left+flowCanvas.scrollLeft,y:centerY};\n"
    "    if(where==='right') return {x:rect.right-box.left+flowCanvas.scrollLeft,y:centerY};\n"
    "    return {\n"
    "      x:centerX,\n"
    "      y:(where==='bottom'?rect.bottom:where==='top'?rect.top:rect.top+rect.height/2)-box.top+flowCanvas.scrollTop\n"
    "    };"
)
if OLD_POINT_BW in bw:
    bw = bw.replace(OLD_POINT_BW, NEW_POINT_BW, 1)
    print('  ✓ point() left/right added')
else:
    print('  ✗ could not find point() return in big-workshop')

# 2. Add CUSTOM_ANCHORS + curvePath after [...].forEach(p=>p.remove());
# big-workshop does NOT have the marker setup line, goes straight to sideRoutes
OLD_SIDEROUTES_BW = "  const sideRoutes=new Map();"
NEW_SIDEROUTES_BW = f"  {CUSTOM_ANCHORS_JS}\n  {CURVE_PATH_JS}\n  {OLD_SIDEROUTES_BW}"
# Count occurrences to be safe
n_side = bw.count(OLD_SIDEROUTES_BW)
if n_side == 1:
    bw = bw.replace(OLD_SIDEROUTES_BW, NEW_SIDEROUTES_BW, 1)
    print('  ✓ CUSTOM_ANCHORS + curvePath added (big-workshop)')
else:
    print(f'  ✗ sideRoutes found {n_side} times in big-workshop')

# 3. Insert custom anchor check before sameColumn&&longJump branch
# big-workshop has this same pattern
OLD_IF_BW = "    if(sameColumn&&longJump){"
n_if = bw.count(OLD_IF_BW)
if n_if == 1:
    bw = bw.replace(OLD_IF_BW, CUSTOM_ANCHOR_CHECK_JS + "if(sameColumn&&longJump){", 1)
    print('  ✓ custom anchor check inserted')
else:
    print(f'  ✗ sameColumn&&longJump found {n_if} times in big-workshop')

with open('docs/big-workshop.html', 'w', encoding='utf-8') as f:
    bw_bytes = bw
    f.write(bw_bytes)
print('  Saved.\n')

# ── Verify ────────────────────────────────────────────────────────────────────
print('=== Verification ===')
for fname in ['docs/naming-rules-preview.html', 'docs/big-workshop.html']:
    with open(fname, encoding='utf-8') as f:
        t = f.read()
    checks = [
        ('CUSTOM_ANCHORS' in t, 'CUSTOM_ANCHORS present'),
        ('curvePath' in t, 'curvePath present'),
        ("where==='left'" in t, "left anchor support"),
        ("where==='right'" in t, "right anchor support"),
        ("ca.straight" in t, "straight line support"),
        ("S076:S077" in t, "S076:S077 anchor"),
    ]
    print(f'\n{fname}:')
    for ok, label in checks:
        print(f'  {"✓" if ok else "✗"} {label}')

print('\nDone.')

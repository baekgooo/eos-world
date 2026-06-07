#!/usr/bin/env python3
"""Inject new CSS + section③ into naming-rules-preview.html"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

NEW_CSS = """
/* ─── Big-workshop style flowchart (section③) ─── */
.flow-canvas {
  position: relative;
  overflow: auto;
  max-height: 80vh;
  min-height: 400px;
  border: 1px solid var(--hair);
  border-radius: 12px;
  background: #faf9f7;
  padding: 28px 32px 60px;
  margin-top: 8px;
}
.flow-grid {
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  gap: 16px;
  align-items: center;
  justify-content: flex-start;
  min-width: 480px;
}
.flow-grid .chapter-band {
  width: min(480px, 90%);
  margin: 4px 0 0;
  padding: 7px 14px;
  border: 1px solid var(--hair);
  border-radius: 999px;
  background: rgba(255,255,255,.88);
  color: var(--muted);
  font-size: 12px;
  font-weight: 900;
  text-align: center;
  letter-spacing: .06em;
}
.flow-grid .flow-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
  width: 100%;
  min-height: 58px;
}
.flow-grid .branch-row { gap: 12px; }
.flow-node {
  position: relative;
  width: 130px;
  min-height: 50px;
  border: 1px solid #c9c2b8;
  background: #fff;
  color: #171615;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3px;
  padding: 5px 8px;
  font-family: -apple-system, "Apple SD Gothic Neo", "Noto Sans KR", sans-serif;
  box-shadow: 0 2px 0 rgba(0,0,0,.04);
  cursor: default;
  text-align: center;
}
.flow-node .nid { font-size: 11px; font-weight: 900; letter-spacing: -.01em; line-height: 1; }
.flow-node .ntitle { font-size: 9.5px; font-weight: 500; color: var(--muted); line-height: 1.3; max-width: 120px; word-break: keep-all; }
.flow-node.decision.major {
  background: #f0c994; border-color: #c9b27a;
  transform: rotate(45deg); width: 64px; height: 64px; min-height: 64px;
  margin: 8px 18px; padding: 4px; gap: 0;
}
.flow-node.decision.major .node-inner { transform: rotate(-45deg); display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; width: 70px; }
.flow-node.decision.major .nid { font-size: 10px; font-weight: 900; }
.flow-node.decision.major .ntitle { font-size: 8px; color: rgba(0,0,0,.55); max-width: 64px; }
.flow-node.decision.minor { background: #e8f0e9; border-color: #b8cfba; border-radius: 12px; width: 110px; min-height: 44px; }
.flow-node.ending { background: #f1f1f1; border-color: #aaa; border-radius: 999px; width: 130px; }
.flow-node.changed { background: #fffae0; border: 2px solid #d4a800; }
.flow-node.decision.major.changed { background: #f8d080; border: 2px solid #d4a800; }
.flow-node.decision.minor.changed { background: #fff3c0; border: 2px solid #d4a800; }
.flow-node.ending.changed { background: #e8edff; border: 2px solid #7090d0; }
.edge-layer { position: absolute; inset: 0; z-index: 1; pointer-events: none; overflow: visible; }
.edge-layer path { stroke: #b9afa5; stroke-width: 1.55; fill: none; }
.changed-badge { background: #fffae0; border: 1px solid #d4a800; padding: 1px 7px; border-radius: 4px; font-weight: 700; font-size: 12px; }
"""

with open('docs/naming-rules-preview.html', encoding='utf-8') as f:
    content = f.read()

with open('scripts/_section3_output.html', encoding='utf-8') as f:
    new_section3 = f.read()

# 1. Add CSS before </style>
content = content.replace('</style>', NEW_CSS + '</style>', 1)

# 2. Find section③ boundaries and replace
start_marker = '  <!-- ③ 7장 순서도 -->'
end_marker = '  <!-- ④ 4장 분기 구조도 (간략) -->'
start_idx = content.index(start_marker)
end_idx = content.index(end_marker)
content = content[:start_idx] + new_section3 + '\n\n  ' + content[end_idx:]

with open('docs/naming-rules-preview.html', 'w', encoding='utf-8') as f:
    f.write(content)
print(f'Done! File length: {len(content)} chars')

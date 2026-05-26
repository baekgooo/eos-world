#!/usr/bin/env python3
"""Build a simple mobile-friendly HTML preview site from 03_sections/*.md."""
from __future__ import annotations

import html
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTIONS_DIR = ROOT / "03_sections"
PROJECT_DIR = ROOT / "00_project"
OUTLINE_DIR = ROOT / "01_outline"
PUZZLES_DIR = ROOT / "04_puzzles"
DOCS_DIR = ROOT / "docs"
ASSETS_DIR = DOCS_DIR / "assets"
SECTION_OUT_DIR = DOCS_DIR / "sections"
REFERENCE_COLLECTIONS = [
    ("설정집", PROJECT_DIR, DOCS_DIR / "project"),
    ("구성 노트", OUTLINE_DIR, DOCS_DIR / "outline"),
    ("퍼즐 노트", PUZZLES_DIR, DOCS_DIR / "puzzles"),
]

SECTION_REF_RE = re.compile(r"\b(S\d{3}[A-Z]?)\.\s*([^<\n]+)")


def inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def linkify_section_refs(fragment: str, section_links: dict[str, str]) -> str:
    """Turn visible refs like 'S002. 멈춘 시계...' into links when possible."""

    def repl(match: re.Match[str]) -> str:
        section_id = match.group(1)
        label = f"{section_id}. {match.group(2).strip()}"
        href = section_links.get(section_id)
        if not href:
            return match.group(0)
        return f'<a class="section-ref" href="{href}">{label}</a>'

    return SECTION_REF_RE.sub(repl, fragment)


def md_to_html(markdown: str, section_links: dict[str, str]) -> str:
    out: list[str] = []
    paras: list[str] = []
    in_code = False

    def finish(fragment: str) -> str:
        return linkify_section_refs(fragment, section_links)

    def flush_para() -> None:
        if paras:
            text = " ".join(paras).strip()
            out.append(f"<p>{finish(inline(text))}</p>")
            paras.clear()

    for raw in markdown.splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            flush_para()
            if not in_code:
                out.append("<pre><code>")
                in_code = True
            else:
                out.append("</code></pre>")
                in_code = False
            continue
        if in_code:
            out.append(html.escape(line) + "\n")
            continue
        if not line.strip():
            flush_para()
            continue
        if line.startswith("# "):
            flush_para()
            out.append(f"<h1>{inline(line[2:].strip())}</h1>")
            continue
        if line.startswith("## "):
            flush_para()
            out.append(f"<h2>{inline(line[3:].strip())}</h2>")
            continue
        if line.startswith("### "):
            flush_para()
            out.append(f"<h3>{inline(line[4:].strip())}</h3>")
            continue
        if line.startswith("> "):
            flush_para()
            out.append(f"<blockquote>{finish(inline(line[2:].strip()))}</blockquote>")
            continue
        if line.startswith("- "):
            flush_para()
            out.append(f"<li>{finish(inline(line[2:].strip()))}</li>")
            continue
        if re.match(r"\d+\.\s", line):
            flush_para()
            text = re.sub(r"^\d+\.\s*", "", line).strip()
            out.append(f"<li>{finish(inline(text))}</li>")
            continue
        paras.append(line)
    flush_para()
    return "\n".join(out)


def extract_title(markdown: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled"


def extract_section_id(filename: str) -> str | None:
    match = re.match(r"(S\d{3}[A-Z]?)_", filename)
    return match.group(1) if match else None


def section_sort_key(path: Path) -> tuple[int, str, str]:
    """Sort base sections before same-number lettered branches."""

    match = re.match(r"S(\d{3})([A-Z]?)_", path.name)
    if not match:
        return (9999, "", path.name)
    number = int(match.group(1))
    suffix = match.group(2)
    return (number, suffix, path.name)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def build_updated_at() -> str:
    """Return a reader-facing timestamp for checking whether the preview is current."""

    return datetime.now().astimezone().strftime("%Y.%m.%d %H:%M")


def extract_choice_targets(markdown: str) -> list[str]:
    """Return section IDs linked from the explicit choice block only."""

    if "## 선택지" not in markdown:
        return []
    choice_block = markdown.split("## 선택지", 1)[1].split("## 다음 섹션", 1)[0]
    return re.findall(r"→\s*(S\d{3}[A-Z]?)\.", choice_block)


def validate_choice_targets(
    source_sections: list[dict[str, str]], section_links: dict[str, str]
) -> None:
    """Prevent confusing gamebook choices before generating the preview."""

    errors: list[str] = []
    for section in source_sections:
        targets = extract_choice_targets(section["markdown"])
        if len(targets) > 1 and len(set(targets)) != len(targets):
            duplicate_targets = sorted({target for target in targets if targets.count(target) > 1})
            errors.append(
                f"{section['src']}: 선택지 여러 개가 같은 페이지로 이동함 "
                f"({', '.join(duplicate_targets)})"
            )
        missing_targets = sorted({target for target in targets if target not in section_links})
        if missing_targets:
            errors.append(
                f"{section['src']}: 존재하지 않는 섹션으로 이동함 "
                f"({', '.join(missing_targets)})"
            )
    if errors:
        detail = "\n".join(f"- {error}" for error in errors)
        raise SystemExit(f"선택지 검증 실패:\n{detail}")


def render_page(title: str, body: str, css_href: str, back_href: str, updated_at: str) -> str:
    return f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · 어스름 너머의 세계</title>
<link rel="stylesheet" href="{css_href}">
</head>
<body>
<div class="updated-at" aria-label="최종 업데이트">최종 업데이트 {html.escape(updated_at)}</div>
<header class="top"><a href="{back_href}">← 작업실</a></header>
<main class="page section-page">
{body}
<nav class="bottom-nav"><a href="{back_href}">목록으로</a></nav>
</main>
</body>
</html>'''


def build_reference_collection(
    label: str,
    source_dir: Path,
    out_dir: Path,
    section_links: dict[str, str],
    updated_at: str,
) -> list[tuple[str, str, str]]:
    """Build reference markdown pages for mobile review."""

    out_dir.mkdir(parents=True, exist_ok=True)
    for old_page in out_dir.glob("*.html"):
        old_page.unlink()
    if not source_dir.exists():
        return []

    items: list[tuple[str, str, str]] = []
    reference_section_links = {
        section_id: f"../sections/{outname}" for section_id, outname in section_links.items()
    }
    for path in sorted(source_dir.glob("*.md")):
        markdown = path.read_text(encoding="utf-8")
        title = extract_title(markdown)
        outname = path.with_suffix(".html").name
        body = md_to_html(markdown, reference_section_links)
        page = render_page(title, body, "../assets/style.css", "../index.html", updated_at)
        write(out_dir / outname, page)
        items.append((title, f"{out_dir.name}/{outname}", path.name))
    return items



def strip_heading(markdown: str) -> str:
    '''Remove the first H1 line for panel rendering.'''
    lines = markdown.splitlines()
    if lines and lines[0].startswith('# '):
        return '\n'.join(lines[1:]).strip()
    return markdown


def section_kind(markdown: str) -> str:
    targets = extract_choice_targets(markdown)
    title = extract_title(markdown)
    if '엔딩' in title or '실패' in title:
        return 'ending'
    if len(targets) > 1:
        return 'decision'
    return 'story'


def extract_all_targets(markdown: str) -> list[str]:
    '''Extract next-section refs used by the workshop flow.'''
    targets = extract_choice_targets(markdown)
    if targets:
        return targets
    if '## 다음 섹션' in markdown:
        block = markdown.split('## 다음 섹션', 1)[1].split('## ', 1)[0]
        targets = re.findall(r'\b(S\d{3}[A-Z]?)\.', block)
    return targets


def extract_illustration_note(markdown: str) -> str:
    if '## 삽화 필요' not in markdown:
        return '아직 삽화 메모가 없어. 이 섹션의 핵심 장면을 기준으로 추후 삽화를 정하면 돼.'
    block = markdown.split('## 삽화 필요', 1)[1].split('## ', 1)[0].strip()
    return block or '삽화 위치만 표시되어 있고 상세 설명은 아직 비어 있어.'


def build_big_workshop(source_sections: list[dict[str, str]], section_links: dict[str, str], updated_at: str) -> None:
    '''Build the desktop-first 큰작업실 flow review page.'''
    import json

    section_ids = [extract_section_id(section['src']) for section in source_sections]
    section_ids = [section_id for section_id in section_ids if section_id]
    id_set = set(section_ids)

    data_sections = []
    edges = []
    for section in source_sections:
        section_id = extract_section_id(section['src'])
        if not section_id:
            continue
        markdown = section['markdown']
        title = extract_title(markdown)
        targets = [target for target in extract_all_targets(markdown) if target in id_set]
        for target in targets:
            edges.append({'from': section_id, 'to': target})
        body_html = md_to_html(strip_heading(markdown), section_links)
        data_sections.append({
            'id': section_id,
            'title': title,
            'kind': section_kind(markdown),
            'src': section['src'],
            'html': body_html,
            'illustration': inline(extract_illustration_note(markdown)),
            'smallUrl': f"sections/{section['outname']}",
        })

    section_json = json.dumps(data_sections, ensure_ascii=False).replace("</", "<\\/")
    edges_json = json.dumps(edges, ensure_ascii=False).replace("</", "<\\/")
    nodes = '\n'.join(
        f'<button class="flow-node {item["kind"]}" data-section="{html.escape(item["id"])}" aria-label="{html.escape(item["title"])}"><span>{html.escape(item["id"])}</span></button>'
        for item in data_sections
    )

    page = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>큰작업실 · 어스름 너머의 세계</title>
<link rel="preconnect" href="https://cdn.jsdelivr.net">
<link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
<style>
:root{{--paper:#fbfaf8;--surface:#ffffff;--surface-warm:#f5f2ee;--ink:#171615;--muted:#69635d;--hair:#dfdbd4;--hair-strong:#c9c2b8;--accent:#8f5b2e;--accent-soft:#f3e6d8;--story:#ffffff;--decision:#fff7e8;--ending:#f1f1f1;}}
*{{box-sizing:border-box}} html,body{{height:100%}} body{{margin:0;background:var(--paper);color:var(--ink);font-family:Pretendard,-apple-system,BlinkMacSystemFont,"Noto Sans KR","Apple SD Gothic Neo",Segoe UI,sans-serif;letter-spacing:-.012em;word-break:keep-all;overflow:hidden}}
a{{color:inherit}} .workshop{{display:grid;grid-template-columns:220px minmax(560px,1fr) minmax(420px,34vw);height:100vh}}
.sidebar{{border-right:1px solid var(--hair);background:#fff;padding:24px 18px;display:flex;flex-direction:column;gap:22px}}
.brand small{{display:block;color:var(--muted);font-size:12px;font-weight:600;margin-bottom:6px}} .brand strong{{display:block;font-size:22px;line-height:1.05;letter-spacing:-.04em}} .brand span{{display:block;margin-top:8px;color:var(--muted);font-size:13px;line-height:1.45}}
.nav{{display:grid;gap:6px}} .nav button,.small-link{{border:0;background:transparent;text-align:left;border-radius:10px;padding:10px 11px;color:var(--muted);font:600 15px/1 Pretendard,sans-serif;text-decoration:none;cursor:pointer}} .nav button.active,.nav button:hover,.small-link:hover{{background:var(--surface-warm);color:var(--ink)}} .small-link{{display:block;margin-top:auto;border:1px solid var(--hair);text-align:center;color:var(--ink);background:#fff}}
.legend{{border-top:1px solid var(--hair);padding-top:16px;color:var(--muted);font-size:12px;line-height:1.7}} .legend b{{color:var(--ink)}} .legend-row{{display:flex;align-items:center;gap:8px;margin:6px 0}} .sample{{width:18px;height:13px;border:1px solid var(--hair-strong);background:#fff;display:inline-block}} .sample.decision{{transform:rotate(45deg);background:var(--decision)}} .sample.ending{{border-radius:999px;background:var(--ending)}}
.flow-wrap{{position:relative;display:flex;flex-direction:column;min-width:0;background:linear-gradient(90deg,rgba(0,0,0,.035) 1px,transparent 1px),linear-gradient(rgba(0,0,0,.035) 1px,transparent 1px);background-size:32px 32px}}
.flow-header{{height:70px;display:flex;align-items:center;justify-content:space-between;padding:0 28px;border-bottom:1px solid var(--hair);background:rgba(251,250,248,.86);backdrop-filter:blur(14px);z-index:3}} .flow-header h1{{margin:0;font-size:21px;letter-spacing:-.04em}} .flow-header p{{margin:4px 0 0;color:var(--muted);font-size:13px}} .flow-tools button{{border:1px solid var(--hair);background:#fff;border-radius:999px;padding:8px 12px;font-weight:700;color:var(--muted);cursor:pointer}}
.flow-canvas{{position:relative;flex:1;overflow:auto;padding:54px 70px 90px}} .flow-grid{{position:relative;z-index:2;display:grid;grid-template-columns:repeat(4,112px);gap:42px 72px;align-items:center;justify-content:center;min-width:680px}}
.flow-node{{position:relative;width:112px;height:58px;border:1px solid var(--hair-strong);background:var(--story);color:var(--ink);display:flex;align-items:center;justify-content:center;font:800 15px/1 Pretendard,sans-serif;box-shadow:0 2px 0 rgba(0,0,0,.04);cursor:pointer;transition:transform .16s ease,box-shadow .16s ease,border-color .16s ease,background .16s ease}} .flow-node:hover{{transform:translateY(-2px);box-shadow:0 10px 22px rgba(31,25,18,.10)}} .flow-node.decision{{background:var(--decision);transform:rotate(45deg);width:74px;height:74px;margin:0 19px}} .flow-node.decision span{{transform:rotate(-45deg)}} .flow-node.ending{{background:var(--ending);border-radius:999px}} .flow-node.selected{{border-color:var(--accent);background:var(--accent-soft);box-shadow:0 0 0 4px rgba(143,91,46,.14),0 12px 28px rgba(143,91,46,.14)}} .flow-node.decision.selected{{background:#f2d8ba}}
.edge-layer{{position:absolute;inset:0;z-index:1;pointer-events:none;overflow:visible}} .edge-layer path{{stroke:#b7afa5;stroke-width:1.5;fill:none;marker-end:url(#arrow)}}
.reader{{background:#fff;border-left:1px solid var(--hair);display:flex;flex-direction:column;min-width:0}} .reader-head{{height:70px;border-bottom:1px solid var(--hair);padding:17px 24px;background:#fff;display:flex;align-items:center;justify-content:space-between;gap:16px}} .reader-kicker{{color:var(--accent);font-size:12px;font-weight:800;letter-spacing:.05em}} .reader-title{{font-size:20px;font-weight:800;letter-spacing:-.035em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}} .open-small{{font-size:12px;font-weight:700;color:var(--muted);text-decoration:none;border:1px solid var(--hair);padding:7px 10px;border-radius:999px;white-space:nowrap}}
.reader-body{{overflow:auto;padding:26px 30px 70px;font-size:16px;line-height:1.76}} .reader-body h2{{font-size:15px;margin:30px 0 10px;padding-top:16px;border-top:1px solid var(--hair);letter-spacing:-.02em}} .reader-body h3{{font-size:15px;margin:22px 0 8px}} .reader-body p{{margin:0 0 15px}} .reader-body blockquote{{margin:0 0 15px;padding:11px 13px;border-left:3px solid var(--accent);background:var(--surface-warm);border-radius:0 10px 10px 0}} .reader-body li{{margin:8px 0}} .reader-body a{{color:var(--accent);font-weight:700;text-decoration:none;border-bottom:1px solid rgba(143,91,46,.25)}}
.illust-card{{margin:28px 0 0;padding:16px;border:1px solid var(--hair);background:var(--surface-warm);border-radius:16px}} .illust-card strong{{display:block;font-size:13px;margin-bottom:7px;color:var(--accent)}} .illust-card p{{margin:0;color:var(--muted);font-size:14px;line-height:1.65}}
.info-panel{{display:none;padding:26px 30px 70px;overflow:auto}} .info-panel.active{{display:block}} .info-panel h2{{font-size:26px;letter-spacing:-.045em;margin:0 0 14px}} .info-panel p{{line-height:1.75;color:var(--muted)}} .info-list{{display:grid;gap:10px;margin-top:22px}} .info-list a{{display:block;padding:14px;border:1px solid var(--hair);border-radius:14px;background:#fff;text-decoration:none}} .info-list small{{display:block;color:var(--muted);margin-top:3px}}
@media(max-width:1100px){{body{{overflow:auto}}.workshop{{grid-template-columns:1fr;height:auto}}.sidebar{{position:sticky;top:0;z-index:5;border-right:0;border-bottom:1px solid var(--hair)}}.reader{{min-height:70vh;border-left:0;border-top:1px solid var(--hair)}}}}
</style>
</head>
<body>
<div class="workshop">
  <aside class="sidebar">
    <div class="brand"><small>큰작업실</small><strong>어스름 너머의 세계</strong><span>분기와 본문을 한 화면에서 검토하는 PC 작업실</span></div>
    <nav class="nav" aria-label="큰작업실 메뉴"><button class="active" data-view="story">스토리</button><button data-view="world">세계관</button><button data-view="character">캐릭터</button></nav>
    <div class="legend"><b>기호</b><div class="legend-row"><i class="sample"></i>스토리</div><div class="legend-row"><i class="sample decision"></i>분기발생지점</div><div class="legend-row"><i class="sample ending"></i>엔딩</div></div>
    <a class="small-link" href="index.html">작은작업실로 이동</a>
  </aside>
  <section class="flow-wrap"><header class="flow-header"><div><h1>스토리줄기</h1><p>기호를 누르면 오른쪽에 원고가 열려.</p></div><div class="flow-tools"><button id="fitFlow">처음으로</button></div></header><div class="flow-canvas" id="flowCanvas"><svg class="edge-layer" id="edgeLayer"><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#b7afa5"></path></marker></defs></svg><div class="flow-grid" id="flowGrid">{nodes}</div></div></section>
  <aside class="reader"><div class="reader-head"><div><div class="reader-kicker" id="readerId">SECTION</div><div class="reader-title" id="readerTitle">섹션을 선택해줘</div></div><a class="open-small" id="openSmall" href="index.html">작은작업실</a></div><div class="reader-body" id="readerBody"></div><div class="info-panel" id="worldPanel"><h2>세계관</h2><p>작은작업실의 세계관 문서로 바로 이동할 수 있어. 큰작업실 안에서도 다음 단계에서 요약 카드를 붙일 수 있게 자리를 잡아두었어.</p><div class="info-list"><a href="project/world_rules.html">사잇별의 땅 규칙<small>world_rules.md</small></a><a href="project/game_rules.html">게임 규칙<small>game_rules.md</small></a><a href="project/concept.html">기획 개념<small>concept.md</small></a></div></div><div class="info-panel" id="characterPanel"><h2>캐릭터</h2><p>주요 인물 설정을 확인하는 자리야. 지금은 캐릭터 바이블로 연결해두었고, 이후 인물별 카드형 보기로 확장할 수 있어.</p><div class="info-list"><a href="project/character_bible.html">캐릭터 바이블<small>character_bible.md</small></a><a href="project/style_guide.html">문체와 분위기<small>style_guide.md</small></a></div></div></aside>
</div>
<script type="application/json" id="sectionData">{section_json}</script><script type="application/json" id="edgeData">{edges_json}</script>
<script>
const sections=JSON.parse(document.getElementById('sectionData').textContent);const edges=JSON.parse(document.getElementById('edgeData').textContent);const byId=new Map(sections.map(s=>[s.id,s]));const nodes=[...document.querySelectorAll('.flow-node')];const readerBody=document.getElementById('readerBody');const readerId=document.getElementById('readerId');const readerTitle=document.getElementById('readerTitle');const openSmall=document.getElementById('openSmall');const flowCanvas=document.getElementById('flowCanvas');const edgeLayer=document.getElementById('edgeLayer');
function renderEdges(){{const box=flowCanvas.getBoundingClientRect();edgeLayer.setAttribute('width',flowCanvas.scrollWidth);edgeLayer.setAttribute('height',flowCanvas.scrollHeight);[...edgeLayer.querySelectorAll('path.edge')].forEach(p=>p.remove());for(const edge of edges){{const a=document.querySelector(`[data-section="${{edge.from}}"]`);const b=document.querySelector(`[data-section="${{edge.to}}"]`);if(!a||!b)continue;const ar=a.getBoundingClientRect();const br=b.getBoundingClientRect();const x1=ar.left+ar.width/2-box.left+flowCanvas.scrollLeft;const y1=ar.top+ar.height/2-box.top+flowCanvas.scrollTop;const x2=br.left+br.width/2-box.left+flowCanvas.scrollLeft;const y2=br.top+br.height/2-box.top+flowCanvas.scrollTop;const midY=y1+(y2-y1)*0.55;const path=document.createElementNS('http://www.w3.org/2000/svg','path');path.setAttribute('class','edge');path.setAttribute('d',`M ${{x1}} ${{y1}} C ${{x1}} ${{midY}}, ${{x2}} ${{midY}}, ${{x2}} ${{y2}}`);edgeLayer.appendChild(path);}}}}
function selectSection(id){{const s=byId.get(id);if(!s)return;nodes.forEach(n=>n.classList.toggle('selected',n.dataset.section===id));readerId.textContent=`${{s.id}} · ${{s.kind==='decision'?'분기발생지점':s.kind==='ending'?'엔딩':'스토리'}}`;readerTitle.textContent=s.title;openSmall.href=s.smallUrl;readerBody.style.display='block';document.querySelectorAll('.info-panel').forEach(p=>p.classList.remove('active'));readerBody.innerHTML=s.html+`<section class="illust-card"><strong>삽화 메모</strong><p>${{s.illustration}}</p></section>`;requestAnimationFrame(renderEdges);}}
nodes.forEach(n=>n.addEventListener('click',()=>selectSection(n.dataset.section)));document.getElementById('fitFlow').addEventListener('click',()=>{{flowCanvas.scrollTo({{left:0,top:0,behavior:'smooth'}});selectSection(sections[0].id);}});document.querySelectorAll('.nav button').forEach(btn=>btn.addEventListener('click',()=>{{document.querySelectorAll('.nav button').forEach(b=>b.classList.remove('active'));btn.classList.add('active');const view=btn.dataset.view;if(view==='story'){{readerBody.style.display='block';document.querySelectorAll('.info-panel').forEach(p=>p.classList.remove('active'));selectSection(document.querySelector('.flow-node.selected')?.dataset.section||sections[0].id);}}if(view==='world'){{readerBody.style.display='none';document.querySelectorAll('.info-panel').forEach(p=>p.classList.remove('active'));document.getElementById('worldPanel').classList.add('active');readerId.textContent='REFERENCE';readerTitle.textContent='세계관';openSmall.href='project/world_rules.html';}}if(view==='character'){{readerBody.style.display='none';document.querySelectorAll('.info-panel').forEach(p=>p.classList.remove('active'));document.getElementById('characterPanel').classList.add('active');readerId.textContent='REFERENCE';readerTitle.textContent='캐릭터';openSmall.href='project/character_bible.html';}}}}));
window.addEventListener('resize',renderEdges);flowCanvas.addEventListener('scroll',()=>requestAnimationFrame(renderEdges));selectSection(sections[0].id);requestAnimationFrame(renderEdges);
</script>
</body>
</html>'''
    write(DOCS_DIR / 'big-workshop.html', page)


def main() -> None:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    SECTION_OUT_DIR.mkdir(parents=True, exist_ok=True)
    updated_at = build_updated_at()
    for old_page in SECTION_OUT_DIR.glob("S*.html"):
        old_page.unlink()

    source_sections: list[dict[str, str]] = []
    section_links: dict[str, str] = {}
    for path in sorted(SECTIONS_DIR.glob("S*.md"), key=section_sort_key):
        markdown = path.read_text(encoding="utf-8")
        title = extract_title(markdown)
        outname = path.with_suffix(".html").name
        section_id = extract_section_id(path.name)
        if section_id:
            section_links[section_id] = outname
        source_sections.append(
            {"title": title, "outname": outname, "src": path.name, "markdown": markdown}
        )

    validate_choice_targets(source_sections, section_links)

    items: list[tuple[str, str, str]] = []
    for section in source_sections:
        title = section["title"]
        outname = section["outname"]
        src = section["src"]
        body = md_to_html(section["markdown"], section_links)
        items.append((title, outname, src))
        page = render_page(title, body, "../assets/style.css", "../index.html", updated_at)
        write(SECTION_OUT_DIR / outname, page)

    big_section_links = {
        section_id: f"sections/{outname}" for section_id, outname in section_links.items()
    }
    build_big_workshop(source_sections, big_section_links, updated_at)

    reference_groups: list[tuple[str, list[tuple[str, str, str]]]] = []
    for label, source_dir, out_dir in REFERENCE_COLLECTIONS:
        ref_items = build_reference_collection(label, source_dir, out_dir, section_links, updated_at)
        if ref_items:
            reference_groups.append((label, ref_items))

    links = "\n".join(
        f'<li><a href="sections/{outname}"><span>{html.escape(title)}</span><small>{html.escape(src)}</small></a></li>'
        for title, outname, src in items
    )
    reference_cards = "\n".join(
        f'<section class="card"><h2>{html.escape(label)}</h2><ul class="section-list">'
        + "\n".join(
            f'<li><a href="{href}"><span>{html.escape(title)}</span><small>{html.escape(src)}</small></a></li>'
            for title, href, src in ref_items
        )
        + '</ul></section>'
        for label, ref_items in reference_groups
    )
    index = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>어스름 너머의 세계 작업실</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="updated-at" aria-label="최종 업데이트">최종 업데이트 {html.escape(updated_at)}</div>
<main class="page">
<section class="hero">
<p class="eyebrow">PDF 전자책 게임북 제작 미리보기</p>
<h1>어스름 너머의 세계</h1>
<p>원고와 게임 구조를 모바일에서 확인하기 위한 작은작업실이야. 긴 분기 흐름은 PC용 큰작업실에서 한눈에 볼 수 있어.</p>
<p><a class="workshop-link" href="big-workshop.html">큰작업실로 이동</a></p>
</section>
<section class="card">
<h2>프롤로그 섹션</h2>
<ul class="section-list">
{links}
</ul>
</section>
{reference_cards}
<section class="card muted">
<h2>검토 메모</h2>
<p>대장은 모바일로 읽고, 수정 의견은 Telegram으로 말해주면 돼. 내가 원고 파일을 고친 뒤 이 사이트를 다시 갱신할게.</p>
</section>
</main>
</body>
</html>'''
    write(DOCS_DIR / "index.html", index)

    css = '''@charset "utf-8";
:root{--bg:#14131a;--panel:#201f2a;--text:#f3eee7;--muted:#b8ad9f;--line:#34303d;--accent:#d9b76f;--link:#ffe2a3;}
*{box-sizing:border-box} body{margin:0;background:radial-gradient(circle at top,#252338 0,#14131a 52%,#0f0e14 100%);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Noto Sans KR",Segoe UI,sans-serif;line-height:1.78;font-size:18px;word-break:keep-all;overflow-wrap:break-word;}
a{color:var(--link);text-decoration:none}.section-ref{font-weight:700;border-bottom:1px solid rgba(255,226,163,.45)}.page{width:min(760px,100%);margin:0 auto;padding:28px 18px 64px}.top{position:sticky;top:0;background:rgba(20,19,26,.88);backdrop-filter:blur(10px);border-bottom:1px solid var(--line);padding:12px 18px;z-index:5}.top a{font-size:15px;color:var(--muted)}
.updated-at{position:fixed;top:10px;right:12px;z-index:10;padding:5px 9px;border:1px solid rgba(217,183,111,.35);border-radius:999px;background:rgba(20,19,26,.82);backdrop-filter:blur(10px);color:var(--accent);font-size:12px;line-height:1.2;letter-spacing:-.01em;box-shadow:0 8px 20px rgba(0,0,0,.18)}
.hero{padding:28px 0 16px}.eyebrow{color:var(--accent);font-size:14px;letter-spacing:.04em;margin:0 0 6px}.hero h1{font-size:34px;line-height:1.2;margin:0 0 14px}.card{background:rgba(32,31,42,.86);border:1px solid var(--line);border-radius:18px;padding:18px;margin:18px 0;box-shadow:0 12px 36px rgba(0,0,0,.18)}.muted{color:var(--muted)}
h1{font-size:30px;line-height:1.25;margin:24px 0 22px;color:#fff4dc}h2{font-size:20px;margin:30px 0 10px;color:var(--accent);border-top:1px solid var(--line);padding-top:20px}h3{font-size:18px;color:#f6dca0}p{margin:0 0 18px}.workshop-link{display:inline-block;padding:10px 14px;border:1px solid rgba(217,183,111,.45);border-radius:999px;background:rgba(217,183,111,.1);color:var(--link);font-weight:700}blockquote{margin:0 0 18px;padding:12px 14px;border-left:3px solid var(--accent);background:rgba(217,183,111,.08);color:#f7e6c0;border-radius:0 12px 12px 0}pre{background:#0d0c12;border:1px solid var(--line);border-radius:12px;padding:14px;overflow:auto;white-space:pre-wrap;color:#f7e6c0}code{font-family:ui-monospace,SFMono-Regular,Consolas,monospace;font-size:.92em}.section-list{list-style:none;margin:0;padding:0}.section-list li{border-top:1px solid var(--line)}.section-list li:first-child{border-top:0}.section-list a{display:block;padding:14px 4px}.section-list span{display:block;color:var(--text);font-weight:700}.section-list small{display:block;color:var(--muted);font-size:13px;margin-top:2px}.bottom-nav{margin-top:40px;padding-top:20px;border-top:1px solid var(--line)}li{margin:8px 0}
@media (max-width:480px){body{font-size:17px;line-height:1.82}.page{padding:42px 16px 56px}.hero h1{font-size:30px}h1{font-size:26px}h2{font-size:19px}.card{border-radius:16px;padding:16px}.updated-at{top:8px;right:8px;font-size:11px;padding:5px 8px}}
'''
    write(ASSETS_DIR / "style.css", css)
    write(DOCS_DIR / ".nojekyll", "")
    print(f"Generated {len(items)} section pages and {sum(len(group) for _, group in reference_groups)} reference pages in {DOCS_DIR}")


if __name__ == "__main__":
    main()


#!/usr/bin/env python3
"""Build a simple mobile-friendly HTML preview site from 03_sections/*.md."""
from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTIONS_DIR = ROOT / "03_sections"
DOCS_DIR = ROOT / "docs"
ASSETS_DIR = DOCS_DIR / "assets"
SECTION_OUT_DIR = DOCS_DIR / "sections"

SECTION_REF_RE = re.compile(r"\b(S\d{3})\.\s*([^<\n]+)")


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
        if line.startswith("- "):
            flush_para()
            out.append(f"<li>{finish(inline(line[2:].strip()))}</li>")
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
    match = re.match(r"(S\d{3})_", filename)
    return match.group(1) if match else None


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def main() -> None:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    SECTION_OUT_DIR.mkdir(parents=True, exist_ok=True)

    source_sections: list[dict[str, str]] = []
    section_links: dict[str, str] = {}
    for path in sorted(SECTIONS_DIR.glob("S*.md")):
        markdown = path.read_text(encoding="utf-8")
        title = extract_title(markdown)
        outname = path.with_suffix(".html").name
        section_id = extract_section_id(path.name)
        if section_id:
            section_links[section_id] = outname
        source_sections.append(
            {"title": title, "outname": outname, "src": path.name, "markdown": markdown}
        )

    items: list[tuple[str, str, str]] = []
    for section in source_sections:
        title = section["title"]
        outname = section["outname"]
        src = section["src"]
        body = md_to_html(section["markdown"], section_links)
        items.append((title, outname, src))
        page = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · 어스름 너머의 세계</title>
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<header class="top"><a href="../index.html">← 작업실</a></header>
<main class="page section-page">
{body}
<nav class="bottom-nav"><a href="../index.html">목록으로</a></nav>
</main>
</body>
</html>'''
        write(SECTION_OUT_DIR / outname, page)

    links = "\n".join(
        f'<li><a href="sections/{outname}"><span>{html.escape(title)}</span><small>{html.escape(src)}</small></a></li>'
        for title, outname, src in items
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
<main class="page">
<section class="hero">
<p class="eyebrow">PDF 전자책 게임북 제작 미리보기</p>
<h1>어스름 너머의 세계</h1>
<p>원고와 게임 구조를 모바일에서 확인하기 위한 작업실이야. 현재는 프롤로그 섹션 초안이 올라와 있어.</p>
</section>
<section class="card">
<h2>프롤로그 섹션</h2>
<ul class="section-list">
{links}
</ul>
</section>
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
.hero{padding:28px 0 16px}.eyebrow{color:var(--accent);font-size:14px;letter-spacing:.04em;margin:0 0 6px}.hero h1{font-size:34px;line-height:1.2;margin:0 0 14px}.card{background:rgba(32,31,42,.86);border:1px solid var(--line);border-radius:18px;padding:18px;margin:18px 0;box-shadow:0 12px 36px rgba(0,0,0,.18)}.muted{color:var(--muted)}
h1{font-size:30px;line-height:1.25;margin:24px 0 22px;color:#fff4dc}h2{font-size:20px;margin:30px 0 10px;color:var(--accent);border-top:1px solid var(--line);padding-top:20px}h3{font-size:18px;color:#f6dca0}p{margin:0 0 18px}pre{background:#0d0c12;border:1px solid var(--line);border-radius:12px;padding:14px;overflow:auto;white-space:pre-wrap;color:#f7e6c0}code{font-family:ui-monospace,SFMono-Regular,Consolas,monospace;font-size:.92em}.section-list{list-style:none;margin:0;padding:0}.section-list li{border-top:1px solid var(--line)}.section-list li:first-child{border-top:0}.section-list a{display:block;padding:14px 4px}.section-list span{display:block;color:var(--text);font-weight:700}.section-list small{display:block;color:var(--muted);font-size:13px;margin-top:2px}.bottom-nav{margin-top:40px;padding-top:20px;border-top:1px solid var(--line)}li{margin:8px 0}
@media (max-width:480px){body{font-size:17px;line-height:1.82}.page{padding:22px 16px 56px}.hero h1{font-size:30px}h1{font-size:26px}h2{font-size:19px}.card{border-radius:16px;padding:16px}}
'''
    write(ASSETS_DIR / "style.css", css)
    write(DOCS_DIR / ".nojekyll", "")
    print(f"Generated {len(items)} section pages in {DOCS_DIR}")


if __name__ == "__main__":
    main()

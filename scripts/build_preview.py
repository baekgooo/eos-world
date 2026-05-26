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
<p>원고와 게임 구조를 모바일에서 확인하기 위한 작업실이야. 프롤로그 섹션과 설정집을 함께 읽을 수 있어.</p>
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
h1{font-size:30px;line-height:1.25;margin:24px 0 22px;color:#fff4dc}h2{font-size:20px;margin:30px 0 10px;color:var(--accent);border-top:1px solid var(--line);padding-top:20px}h3{font-size:18px;color:#f6dca0}p{margin:0 0 18px}blockquote{margin:0 0 18px;padding:12px 14px;border-left:3px solid var(--accent);background:rgba(217,183,111,.08);color:#f7e6c0;border-radius:0 12px 12px 0}pre{background:#0d0c12;border:1px solid var(--line);border-radius:12px;padding:14px;overflow:auto;white-space:pre-wrap;color:#f7e6c0}code{font-family:ui-monospace,SFMono-Regular,Consolas,monospace;font-size:.92em}.section-list{list-style:none;margin:0;padding:0}.section-list li{border-top:1px solid var(--line)}.section-list li:first-child{border-top:0}.section-list a{display:block;padding:14px 4px}.section-list span{display:block;color:var(--text);font-weight:700}.section-list small{display:block;color:var(--muted);font-size:13px;margin-top:2px}.bottom-nav{margin-top:40px;padding-top:20px;border-top:1px solid var(--line)}li{margin:8px 0}
@media (max-width:480px){body{font-size:17px;line-height:1.82}.page{padding:42px 16px 56px}.hero h1{font-size:30px}h1{font-size:26px}h2{font-size:19px}.card{border-radius:16px;padding:16px}.updated-at{top:8px;right:8px;font-size:11px;padding:5px 8px}}
'''
    write(ASSETS_DIR / "style.css", css)
    write(DOCS_DIR / ".nojekyll", "")
    print(f"Generated {len(items)} section pages and {sum(len(group) for _, group in reference_groups)} reference pages in {DOCS_DIR}")


if __name__ == "__main__":
    main()


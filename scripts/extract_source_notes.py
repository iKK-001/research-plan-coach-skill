#!/usr/bin/env python3
"""Extract research-planning notes from PDF, DOCX, PPTX, TXT, and MD files."""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile


SECTION_PATTERNS = [
    "abstract",
    "introduction",
    "literature review",
    "theoretical background",
    "hypothesis",
    "method",
    "methodology",
    "results",
    "discussion",
    "limitations",
    "future research",
    "conclusion",
    "references",
    "摘要",
    "引言",
    "文献综述",
    "研究方法",
    "研究结果",
    "讨论",
    "局限",
    "未来研究",
    "结论",
    "要旨",
    "はじめに",
    "先行研究",
    "仮説",
    "方法",
    "結果",
    "考察",
    "限界",
    "今後",
    "結論",
]


def clean_text(text: str) -> str:
    text = text.replace("\x00", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip()


def require_import(module: str, install_hint: str):
    try:
        return __import__(module)
    except ImportError as exc:
        raise SystemExit(
            f"Missing dependency: {module}. {install_hint}\n"
            "If you are using Codex, try the bundled Python runtime listed in references/toolkit.md."
        ) from exc


def extract_pdf(path: Path, max_pages: int | None) -> str:
    pypdf = require_import("pypdf", "Install pypdf or use the bundled Codex Python runtime.")
    reader = pypdf.PdfReader(str(path))
    chunks: list[str] = []
    pages = reader.pages[:max_pages] if max_pages else reader.pages
    for index, page in enumerate(pages, start=1):
        text = page.extract_text() or ""
        chunks.append(f"\n\n===== PAGE {index} =====\n{clean_text(text)}")
    return clean_text("".join(chunks))


def extract_docx(path: Path) -> str:
    docx = require_import("docx", "Install python-docx or use the bundled Codex Python runtime.")
    document = docx.Document(str(path))
    blocks = [paragraph.text.strip() for paragraph in document.paragraphs if paragraph.text.strip()]
    for table in document.tables:
        for row in table.rows:
            cells = [cell.text.strip() for cell in row.cells if cell.text.strip()]
            if cells:
                blocks.append(" | ".join(cells))
    return clean_text("\n".join(blocks))


def extract_pptx(path: Path) -> str:
    ns = {
        "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
        "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    }
    slides: list[str] = []
    with ZipFile(path) as archive:
        names = [
            name
            for name in archive.namelist()
            if name.startswith("ppt/slides/slide") and name.endswith(".xml")
        ]
        names.sort(key=lambda value: int(re.search(r"slide(\d+)\.xml", value).group(1)))
        for name in names:
            root = ET.fromstring(archive.read(name))
            texts: list[str] = []
            for paragraph in root.findall(".//a:p", ns):
                runs: list[str] = []
                for node in paragraph:
                    tag = node.tag.split("}")[-1]
                    if tag in {"r", "fld"}:
                        text_node = node.find("a:t", ns)
                        if text_node is not None and text_node.text:
                            runs.append(text_node.text)
                    elif tag == "br":
                        runs.append("\n")
                text = "".join(runs).strip()
                if text:
                    texts.append(text)
            slide_no = re.search(r"slide(\d+)\.xml", name).group(1)
            slides.append(f"===== SLIDE {slide_no} =====\n" + "\n".join(texts))
    return clean_text("\n\n".join(slides))


def extract_plain(path: Path) -> str:
    return clean_text(path.read_text(encoding="utf-8", errors="ignore"))


def extract(path: Path, max_pages: int | None) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return extract_pdf(path, max_pages)
    if suffix == ".docx":
        return extract_docx(path)
    if suffix == ".pptx":
        return extract_pptx(path)
    if suffix in {".txt", ".md"}:
        return extract_plain(path)
    raise SystemExit(f"Unsupported file type: {path.suffix}")


def find_likely_sections(text: str, keywords: list[str]) -> list[str]:
    patterns = [pattern.lower() for pattern in SECTION_PATTERNS + keywords]
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    hits: list[str] = []
    for line in lines:
        normalized = line.lower()
        if len(line) <= 180 and any(pattern in normalized for pattern in patterns):
            hits.append(line)
    return hits[:100]


def keyword_contexts(text: str, keywords: list[str], window: int) -> list[str]:
    if not keywords:
        return []
    contexts: list[str] = []
    lowered = text.lower()
    for keyword in keywords:
        start = 0
        needle = keyword.lower()
        while True:
            index = lowered.find(needle, start)
            if index == -1:
                break
            left = max(0, index - window)
            right = min(len(text), index + len(keyword) + window)
            contexts.append(clean_text(text[left:right]))
            start = index + len(keyword)
            if len(contexts) >= 60:
                return contexts
    return contexts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("sources", nargs="+", help="PDF/DOCX/PPTX/TXT/MD files to extract")
    parser.add_argument("-o", "--output-dir", default="/tmp/research-plan-coach-extracted")
    parser.add_argument("--max-pages", type=int, default=None, help="Limit PDF pages")
    parser.add_argument("--sections-only", action="store_true", help="Do not include full raw text")
    parser.add_argument("--keywords", default="", help="Comma-separated keywords for section/context scan")
    parser.add_argument("--context-window", type=int, default=500)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    keywords = [item.strip() for item in args.keywords.split(",") if item.strip()]

    for raw in args.sources:
        path = Path(raw)
        if not path.exists():
            print(f"Missing file: {path}", file=sys.stderr)
            continue
        text = extract(path, args.max_pages)
        if not text:
            print(f"No extractable text found: {path}. OCR may be required.", file=sys.stderr)
        sections = find_likely_sections(text, keywords)
        contexts = keyword_contexts(text, keywords, args.context_window)

        out = output_dir / f"{path.stem}.notes.txt"
        body = [
            f"# Source: {path}",
            "",
            "## Likely Sections",
            *[f"- {section}" for section in sections],
            "",
        ]
        if contexts:
            body.extend(["## Keyword Contexts", *[f"\n---\n{context}" for context in contexts], ""])
        if not args.sections_only:
            body.extend(["## Raw Extracted Text", text])
        out.write_text("\n".join(body), encoding="utf-8")
        print(out)


if __name__ == "__main__":
    main()


#!/usr/bin/env python3
"""
fetch-gfm-spec.py

Downloads the GitHub Flavored Markdown specification from https://github.github.com/gfm/
and converts it to a MkDocs-compatible Markdown file at:

    docs/references/markdown/gfm-spec.md

Usage:
    pip install -r scripts/fetch-gfm-spec-requirements.txt
    python scripts/fetch-gfm-spec.py
"""

import datetime
import sys
from pathlib import Path

import html2text
import requests
from bs4 import BeautifulSoup

GFM_SPEC_URL = "https://github.github.com/gfm/"

# Resolve output path relative to this script's location (repo root / docs / ...)
REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = REPO_ROOT / "docs" / "references" / "markdown" / "gfm-spec.md"

FRONTMATTER = """\
---
title: GitHub Flavored Markdown Spec
description: >
  The full GitHub Flavored Markdown (GFM) specification, imported from {url}
date:
  created: {today}
  updated: {today}
tags:
  - markdown
  - reference
  - github
---

<!--- Do not use a H1 element when the title is set in the frontmatter --->
<!--- Source: {url} --->
<!--- Re-generate this file by running: python scripts/fetch-gfm-spec.py --->

"""


def fetch_html(url: str) -> str:
    print(f"  GET {url}")
    resp = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()
    return resp.text


def extract_body(html: str) -> str:
    """Return the HTML of the main spec content, stripping nav/header/footer."""
    soup = BeautifulSoup(html, "html.parser")

    # Remove elements that don't belong in a docs page
    for tag in soup.select("script, style, nav, header, footer"):
        tag.decompose()

    # Try progressively broader containers
    for selector in [
        "div.spec-container",
        "article",
        "main",
        "div#content",
        "div.content",
        "body",
    ]:
        el = soup.select_one(selector)
        if el:
            return str(el)

    return str(soup)


def to_markdown(html_content: str) -> str:
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.body_width = 0        # No hard line wrapping
    h.wrap_links = False
    h.protect_links = False
    h.mark_code = True
    return h.handle(html_content)


def main() -> None:
    today = datetime.date.today().isoformat()

    print("Fetching GFM spec ...")
    try:
        html = fetch_html(GFM_SPEC_URL)
    except requests.RequestException as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    print("Extracting main content ...")
    body_html = extract_body(html)

    print("Converting HTML to Markdown ...")
    md_body = to_markdown(body_html)

    frontmatter = FRONTMATTER.format(url=GFM_SPEC_URL, today=today)
    output = frontmatter + md_body

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(output, encoding="utf-8")
    print(f"Written to {OUTPUT_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()

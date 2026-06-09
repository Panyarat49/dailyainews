#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

H1_RE = re.compile(r"^#\s+(.+?)\s*$")
TLDR_RE = re.compile(r"^>\s*-\s+(.+?)\s*$")
ACTION_RE = re.compile(r"^- \*\*สำหรับนักลงทุน:\*\*\s*(.+?)\s*$")


# Remove simple Markdown formatting so LINE gets clean readable text.
def clean_md(text: str) -> str:
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\[(.*?)\]\((.*?)\)", r"\1", text)
    return text.strip()


# Read the article text and pull out the title, top 3 TL;DR bullets, and investor note.
def parse_article(text: str):
    title = "Daily AI Brief"
    tldr: list[str] = []
    investor_watch = ""

    for line in text.splitlines():
        if m := H1_RE.match(line):
            title = clean_md(m.group(1))
        if m := TLDR_RE.match(line):
            tldr.append(clean_md(m.group(1)))
        if m := ACTION_RE.match(line):
            investor_watch = clean_md(m.group(1))

    return title, tldr[:3], investor_watch


# Build one LINE Flex Message card with a short summary and a real button link.
def make_flex(title: str, bullets: list[str], investor_watch: str, permalink: str):
    body_contents = [
        {
            "type": "text",
            "text": title.replace("สรุปข่าว AI ประจำวันที่", "AI Brief —"),
            "weight": "bold",
            "size": "lg",
            "wrap": True,
            "color": "#111827",
        },
        {
            "type": "separator",
            "margin": "md",
        },
    ]

    for i, bullet in enumerate(bullets, start=1):
        body_contents.append(
            {
                "type": "box",
                "layout": "horizontal",
                "margin": "md",
                "contents": [
                    {
                        "type": "text",
                        "text": str(i),
                        "size": "sm",
                        "weight": "bold",
                        "color": "#2563EB",
                        "flex": 0,
                    },
                    {
                        "type": "text",
                        "text": bullet,
                        "size": "sm",
                        "wrap": True,
                        "color": "#374151",
                        "margin": "sm",
                        "flex": 1,
                    },
                ],
            }
        )

    if investor_watch:
        body_contents.extend(
            [
                {
                    "type": "separator",
                    "margin": "lg",
                },
                {
                    "type": "text",
                    "text": "Investor watch",
                    "weight": "bold",
                    "size": "sm",
                    "margin": "lg",
                    "color": "#111827",
                },
                {
                    "type": "text",
                    "text": investor_watch,
                    "size": "sm",
                    "wrap": True,
                    "margin": "sm",
                    "color": "#4B5563",
                },
            ]
        )

    return {
        "type": "flex",
        "altText": title[:400],
        "contents": {
            "type": "bubble",
            "size": "mega",
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": body_contents,
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "อ่านฉบับเต็ม",
                            "uri": permalink,
                        },
                    }
                ],
            },
        },
    }


# Run the script from the command line: read article path + permalink, then print JSON.
def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(f"usage: {argv[0]} <article_path> <permalink>", file=sys.stderr)
        return 2

    article_path = Path(argv[1])
    permalink = argv[2]

    title, bullets, investor_watch = parse_article(
        article_path.read_text(encoding="utf-8")
    )
    message = make_flex(title, bullets, investor_watch, permalink)

    print(json.dumps(message, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
#!/usr/bin/env python3
"""Build and send the daily-ai-news brief as an HTML email (Office 365 SMTP).

Usage:
    send_email.py <article_path> <permalink>
    send_email.py <article_path> <permalink> --dry-run   # print HTML, do not send

Unlike the old LINE path, email has no 5000-char limit, so the FULL brief
is delivered — no sentence-fitting, no dropped stories. The markdown brief
is rendered to a styled, Thai-friendly HTML email with a plain-text fallback.

Environment (required to send; ignored with --dry-run):
    MAIL_USERNAME   Office 365 mailbox login (also the default From address)
    MAIL_PASSWORD   Mailbox password or app password
    MAIL_TO         Recipient(s), comma-separated
    MAIL_FROM       Optional. Defaults to MAIL_USERNAME.
    MAIL_HOST       Optional. Defaults to smtp.office365.com.
    MAIL_PORT       Optional. Defaults to 587 (STARTTLS).
"""

from __future__ import annotations

import os
import re
import smtplib
import sys
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

import markdown  # provided via `pip install markdown` in the workflow


H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


def extract_title(md_text: str) -> str:
    """First H1 becomes the email subject; fall back to a generic Thai title."""
    m = H1_RE.search(md_text)
    return m.group(1).strip() if m else "สรุปข่าว AI ประจำวัน"


def render_html(md_text: str, permalink: str) -> str:
    """Render the brief markdown to a self-contained, email-client-safe HTML
    document. Styles are inlined on the wrapper and applied via a <style>
    block; both are kept simple so Outlook/Gmail render them consistently."""
    # nl2br keeps the TL;DR block readable: its bullets live inside one
    # blockquote paragraph (no blank line after "TL;DR"), so without
    # <br> conversion they'd collapse onto a single line. Story bodies are
    # each a single source line, so nl2br is a no-op for them.
    body_html = markdown.markdown(
        md_text,
        extensions=["extra", "sane_lists", "nl2br"],
        output_format="html5",
    )

    return f"""\
<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  body {{
    margin: 0;
    padding: 0;
    background: #f4f5f7;
    font-family: -apple-system, "Segoe UI", "Helvetica Neue", Tahoma,
                 "Noto Sans Thai", Arial, sans-serif;
    color: #1a1a1a;
    line-height: 1.7;
  }}
  .wrap {{ max-width: 680px; margin: 0 auto; padding: 24px 16px; }}
  .card {{
    background: #ffffff;
    border: 1px solid #e3e6ea;
    border-radius: 12px;
    padding: 28px 32px;
  }}
  h1 {{ font-size: 22px; line-height: 1.35; margin: 0 0 18px; color: #0d1b2a; }}
  h2 {{ font-size: 18px; margin: 28px 0 10px; color: #0d1b2a;
        border-top: 1px solid #eef0f2; padding-top: 18px; }}
  h3 {{ font-size: 16px; margin: 22px 0 8px; color: #14213d; }}
  p {{ margin: 10px 0; }}
  a {{ color: #1565c0; word-break: break-word; }}
  blockquote {{
    margin: 16px 0;
    padding: 12px 18px;
    background: #f0f6ff;
    border-left: 4px solid #1565c0;
    border-radius: 6px;
  }}
  blockquote p:first-child {{ margin-top: 0; }}
  blockquote p:last-child {{ margin-bottom: 0; }}
  ul {{ margin: 10px 0; padding-left: 22px; }}
  li {{ margin: 6px 0; }}
  hr {{ border: none; border-top: 1px solid #eef0f2; margin: 24px 0; }}
  .footer {{ margin-top: 22px; font-size: 13px; color: #6b7280;
             text-align: center; }}
  .footer a {{ color: #6b7280; }}
</style>
</head>
<body>
  <div class="wrap">
    <div class="card">
      {body_html}
    </div>
    <div class="footer">
      <p>อ่านฉบับเต็มบน GitHub: <a href="{permalink}">{permalink}</a></p>
    </div>
  </div>
</body>
</html>
"""


def render_text(md_text: str, permalink: str) -> str:
    """Plain-text fallback. The raw markdown already reads cleanly, so we
    just append the permalink for clients that show text/plain."""
    return f"{md_text.rstrip()}\n\nอ่านฉบับเต็มบน GitHub: {permalink}\n"


def build_message(article_path: Path, permalink: str) -> EmailMessage:
    md_text = article_path.read_text(encoding="utf-8")
    title = extract_title(md_text)

    sender = os.environ.get("MAIL_FROM") or os.environ["MAIL_USERNAME"]
    recipients = [
        addr.strip()
        for addr in os.environ["MAIL_TO"].split(",")
        if addr.strip()
    ]
    if not recipients:
        raise SystemExit("MAIL_TO is empty — set at least one recipient.")

    msg = EmailMessage()
    msg["Subject"] = title
    msg["From"] = formataddr(("Daily AI News", sender))
    msg["To"] = ", ".join(recipients)
    msg.set_content(render_text(md_text, permalink))
    msg.add_alternative(render_html(md_text, permalink), subtype="html")
    return msg


def send(msg: EmailMessage) -> None:
    # Personal Outlook.com/Hotmail uses smtp-mail.outlook.com; Microsoft 365
    # business accounts use smtp.office365.com. Override via MAIL_HOST if needed.
    host = os.environ.get("MAIL_HOST", "smtp-mail.outlook.com")
    port = int(os.environ.get("MAIL_PORT", "587"))
    username = os.environ["MAIL_USERNAME"]
    password = os.environ["MAIL_PASSWORD"]

    print(f"Connecting to {host}:{port} as {username} …")
    with smtplib.SMTP(host, port, timeout=30) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username, password)
        server.send_message(msg)
    print(f"✅ Email sent. Subject: {msg['Subject']!r} → {msg['To']}")


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:] if not a.startswith("--")]
    dry_run = "--dry-run" in argv

    if len(args) != 2:
        print(
            f"usage: {argv[0]} <article_path> <permalink> [--dry-run]",
            file=sys.stderr,
        )
        return 2

    article_path = Path(args[0])
    permalink = args[1]

    if dry_run:
        md_text = article_path.read_text(encoding="utf-8")
        sys.stdout.write(render_html(md_text, permalink))
        return 0

    msg = build_message(article_path, permalink)
    send(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pboat_universe.py — RSS pre-screening funnel for pboat (Panyarat49/dailyainews).

================================  WHAT THIS FILE IS  ================================
The news-GATHERING half of the daily pipeline, written in plain Python. It runs BEFORE
Claude wakes up, casts a wide net over RSS, narrows it to fresh + relevant + trusted
stories, and hands Claude a ready-made candidate list so Claude can spend its time on
judgement and writing instead of hunting around the web.

==============================  WHERE IT FITS (daily)  =============================
  [1] pboat-data.yml  @05:57 BKK ─ runs THIS script ─▶ commits universe_{date}_{stream}.json
  [2] Claude Routine  @07:00 BKK ─ engine Step 0.5 reads that JSON ─▶ writes articles/{date}-{stream}.md
  [3] promote-brief.yml ─ copies the brief from a claude/* branch ─▶ main
  [4] email-notify.yml ─ send_email.py ─▶ Gmail SMTP ─▶ your inbox
  ▸ THIS FILE = STEP 1.

================================  WHAT IT DOES (steps)  ============================
  1. FETCH   ~14 direct RSS feeds + Google News searches (AI/Thai + one per Tier-1 company)
  2. DEDUP   drop the same URL arriving from multiple feeds
  3. KEYWORD keep only AI/tech (ainews) or watchlist-company (watchlist) items; drop noise
  4. TRUSTED drop any publisher not on shared/trusted-sources.md  (default; --all-sources keeps them)
  5. SCORE   rank by recency + keyword-hit count
  6. WRITE   top ~40 per stream → output/universe_{YYYYMMDD}_{ainews,watchlist}.json

Output files (one per stream):
    .github/scripts/output/universe_{YYYYMMDD}_ainews.json      (general AI/tech)
    .github/scripts/output/universe_{YYYYMMDD}_watchlist.json   (watchlist companies)

NOT a trust bypass: Claude still WebFetch-verifies every story and re-applies all engine
gates (freshness ≤24h, 7-day dedup, trusted-source allowlist) before it appears in a brief.
This script only replaces Claude's initial WebSearch discovery pass.

Usage:
    python pboat_universe.py                 # both streams, trusted-only (default)
    python pboat_universe.py --stream ainews
    python pboat_universe.py --hours 36      # widen the lookback window
    python pboat_universe.py --all-sources   # keep off-allowlist publishers (tagged, not dropped)

Deps (auto-installed on first run): requests feedparser
"""
from __future__ import annotations

import argparse
import html as _html
import importlib
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.parse import quote


# ── dependency bootstrap (stdlib only above this line) ──────────────────────

def _ensure(pkg: str) -> bool:
    name = pkg.split("[")[0]
    try:
        importlib.import_module(name)
        return True
    except ImportError:
        pass
    print(f"[setup] installing {pkg!r} ...", flush=True)
    r = subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", pkg],
                       capture_output=True, text=True)
    if r.returncode != 0 and "externally-managed-environment" in (r.stderr or ""):
        r = subprocess.run([sys.executable, "-m", "pip", "install", "--quiet",
                            "--break-system-packages", pkg],
                           capture_output=True, text=True)
    importlib.invalidate_caches()
    return r.returncode == 0


for _pkg in ("requests", "feedparser"):
    if not _ensure(_pkg):
        sys.exit(f"[fatal] could not install {_pkg!r}")

import requests   # noqa: E402
import feedparser # noqa: E402


# ── paths ────────────────────────────────────────────────────────────────────

REPO_ROOT  = Path(__file__).parent.parent.parent   # dailyainews/
SCRIPTS    = Path(__file__).parent                 # .github/scripts/
OUTPUT_DIR = SCRIPTS / "output"
WATCHLIST_PATH    = REPO_ROOT / ".claude/skills/daily-ai-watchlist/reference/watchlist.json"
TRUSTED_SRC_PATH  = REPO_ROOT / ".claude/skills/shared/trusted-sources.md"

UA = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"),
    "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*",
    "Accept-Language": "en-US,en;q=0.9,th;q=0.5",
}

BKK = timezone(timedelta(hours=7))   # Asia/Bangkok UTC+7


# ── AI/tech keyword set for ainews stream ───────────────────────────────────
# Covers: models/labs, chips/hardware, cloud/infra, research, regulation, products.
# Word-boundary aware for Latin terms; substring match for Thai/CJK.

AI_KEYWORDS: list[str] = [
    # labs & models
    "openai", "anthropic", "deepmind", "mistral", "cohere", "xai", "groq", "perplexity",
    "claude", "chatgpt", "gpt", "gemini", "llama", "copilot", "grok",
    # generic AI terms
    "ai", "artificial intelligence", "machine learning", "deep learning",
    "large language model", "llm", "foundation model", "generative ai", "gen ai",
    "multimodal", "agi", "neural network", "transformer", "diffusion model",
    "fine-tuning", "inference", "training run", "benchmark",
    # hardware & infra
    "nvidia", "gpu", "h100", "h200", "blackwell", "gb200",
    "amd", "instinct", "mi300", "mi400",
    "chip", "semiconductor", "wafer", "fab", "tsmc", "hbm", "dram",
    "data center", "cloud ai", "ai infrastructure", "ai accelerator",
    # products & use-cases
    "ai agent", "agentic", "ai assistant", "ai search", "ai coding",
    "robotics", "autonomous", "self-driving", "computer vision",
    # policy & safety
    "ai regulation", "ai safety", "ai governance", "export control", "ai act",
    "ai policy", "responsible ai",
    # investment signals
    "ai funding", "ai investment", "ai acquisition", "ai partnership",
    "ai earnings", "ai revenue",
    # Thai
    "เอไอ", "ปัญญาประดิษฐ์", "โมเดล", "ชิป", "ดาต้าเซ็นเตอร์", "เซมิคอนดักเตอร์",
    # Chinese (for Asia coverage)
    "人工智能", "大模型", "芯片", "英伟达", "谷歌", "OpenAI",
]

# Drop-list: these make a good story look AI-related but aren't (noise reduction).
AI_NOISE: list[str] = [
    "world cup", "fifa", "nba", "nfl", "oscar", "grammy", "celebrity", "concert",
    "accident", "crime", "weather", "horoscope",
]


# ── RSS feed catalog ─────────────────────────────────────────────────────────
# Direct RSS URLs for outlets where feeds are stable.
# These supplement Google News RSS queries (which handle the long tail).

DIRECT_FEEDS: list[dict] = [
    # High-value tech press
    {"name": "TechCrunch",    "url": "https://techcrunch.com/feed/"},
    {"name": "The Verge",     "url": "https://www.theverge.com/rss/index.xml"},
    {"name": "Ars Technica",  "url": "https://feeds.arstechnica.com/arstechnica/technology-lab"},
    {"name": "The Register",  "url": "https://www.theregister.com/headlines.atom"},
    {"name": "Tom's Hardware", "url": "https://www.tomshardware.com/rss.xml"},
    {"name": "VentureBeat",   "url": "https://venturebeat.com/feed/"},
    {"name": "Engadget",      "url": "https://www.engadget.com/rss.xml"},
    {"name": "ZDNet",         "url": "https://www.zdnet.com/news/rss.xml"},
    {"name": "IEEE Spectrum",  "url": "https://spectrum.ieee.org/feeds/feed.rss"},
    # Thai tech
    {"name": "Blognone",      "url": "https://www.blognone.com/node/feed"},
    {"name": "Techsauce",     "url": "https://techsauce.co/feed"},
    {"name": "Brand Inside",  "url": "https://brandinside.asia/feed/"},
    {"name": "The Standard",  "url": "https://thestandard.co/feed/"},
    # Wire / global
    {"name": "CNA Tech",      "url": "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml&category=10416"},
]

# Google News RSS queries for broad AI/tech sweeps.
# These catch the top stories across all trusted outlets without needing per-site feeds.
GNEWS_AI_QUERIES: list[str] = [
    "AI artificial intelligence news",
    "LLM large language model",
    "chip semiconductor GPU AI",
    "AI data center cloud computing",
    "AI regulation policy",
]

# Google News RSS queries for Thai-language AI news.
GNEWS_TH_QUERIES: list[str] = [
    "ข่าว AI ปัญญาประดิษฐ์",
    "ชิป เซมิคอนดักเตอร์ เอไอ",
]


def gnews_url(query: str, lang: str = "en", country: str = "US", hours: int = 24) -> str:
    """Build a Google News RSS search URL with a rolling time window."""
    days = max(1, (hours + 23) // 24)
    q = f"{query} when:{days}d"
    return f"https://news.google.com/rss/search?q={quote(q)}&hl={lang}&gl={country}&ceid={country}:{lang}"


# ── helpers ──────────────────────────────────────────────────────────────────

def strip_html(s: str) -> str:
    return re.sub(r"<[^>]+>", " ", _html.unescape(s or "")).strip()


def clean_title(t: str) -> str:
    # Google News appends "  - Publisher Name" — strip it so comparison is clean.
    return re.sub(r"\s{2,}-\s+[^-]+$", "", (t or "").strip()).strip()


def parse_feed(content: bytes | str, hours: int) -> list[dict]:
    """Parse an RSS/Atom feed and return items published within the lookback window."""
    import calendar
    feed = feedparser.parse(content)
    cutoff = time.time() - hours * 3600
    out: list[dict] = []
    for e in feed.entries:
        tp = e.get("published_parsed") or e.get("updated_parsed")
        ts = calendar.timegm(tp) if tp else None
        if ts is not None and ts < cutoff:
            continue  # older than window
        age_h = round((time.time() - ts) / 3600, 1) if ts else None
        body = ""
        if e.get("content"):
            try:
                body = e["content"][0].get("value", "") or ""
            except Exception:
                body = ""
        desc = strip_html(body or e.get("summary") or e.get("description") or "")[:500]
        link = e.get("link") or ""

        # Google News RSS items carry a <source url="https://realpublisher.com">Name</source>
        # element — feedparser exposes it as entry.source. Use it to recover the REAL
        # publisher (the link itself is a news.google.com redirect), with no extra HTTP call.
        src = e.get("source") or {}
        publisher_name   = (src.get("title") or "").strip()
        publisher_href   = (src.get("href") or "").strip()
        publisher_domain = source_domain(publisher_href) if publisher_href else ""

        raw_title = (e.get("title") or "").strip()
        # Google News appends " - {Publisher}" to titles. If we know the publisher, strip
        # exactly that suffix (precise — won't eat legit " - " inside a real headline).
        if publisher_name and raw_title.endswith(f" - {publisher_name}"):
            title = raw_title[: -(len(publisher_name) + 3)].strip()
        else:
            title = clean_title(raw_title)

        if not title or not link:
            continue
        out.append({
            "title":            title,
            "url":              link,
            "description":      desc,
            "published_raw":    e.get("published") or e.get("updated") or "",
            "age_h":            age_h,
            "has_timestamp":    tp is not None,
            "publisher":        publisher_name,
            "publisher_domain": publisher_domain,
        })
    return out


def fetch_feed(url: str, hours: int, timeout: int = 15) -> tuple[list[dict], str]:
    """Fetch one RSS feed URL. Returns (items, error_str)."""
    try:
        r = requests.get(url, headers=UA, timeout=timeout)
        if r.status_code != 200:
            return [], f"HTTP {r.status_code}"
        items = parse_feed(r.content, hours)
        return items, ""
    except Exception as e:
        return [], f"{type(e).__name__}: {e}"


def source_domain(url: str) -> str:
    m = re.search(r"https?://(?:www\.)?([^/]+)", url or "")
    return m.group(1).lower() if m else ""


# ── keyword matching ─────────────────────────────────────────────────────────

_WB = r"[^\W_]"  # Unicode word character (letter or digit, not underscore/punct)


def _kw_hit(kw: str, text: str) -> bool:
    """Word-boundary match for Latin keywords; substring match for Thai/CJK."""
    if re.search(r"[a-z0-9]", kw):
        return bool(re.search(
            r"(?<!" + _WB + r")" + re.escape(kw) + r"(?!" + _WB + r")", text
        ))
    return kw in text


def keyword_hits(text: str, keywords: list[str]) -> list[str]:
    """Return subset of `keywords` that match `text` (lowercased)."""
    low = text.lower()
    return [k for k in keywords if _kw_hit(k, low)]


def is_noise(text: str) -> bool:
    low = text.lower()
    return any(_kw_hit(k, low) for k in AI_NOISE)


# ── scoring ──────────────────────────────────────────────────────────────────

def score_item(item: dict, matched: list[str]) -> float:
    """
    Simple score = recency bonus (0–2) + keyword hit count (capped at 5).
    Claude does the real editorial ranking; this just surface the most
    plausible candidates first so Claude's shortlist isn't buried.
    """
    age = item.get("age_h")
    recency = round(max(0.0, (24 - age) / 24 * 2), 2) if age is not None else 0.0
    kw_score = min(len(matched), 5) * 0.8
    return round(recency + kw_score, 2)


# ── deduplication ────────────────────────────────────────────────────────────

def dedup_url(url: str) -> str:
    """Normalise URL for dedup: strip scheme, www, trailing slash, query params."""
    u = re.sub(r"^https?://(?:www\.)?", "", url.lower()).rstrip("/")
    u = re.sub(r"\?.*$", "", u)
    return u


# ── watchlist keyword extraction ─────────────────────────────────────────────

def load_watchlist_keywords(path: Path) -> list[str]:
    """
    Read watchlist.json and return a flat, deduplicated list of all keywords
    and cn_terms across all tiers. Used for watchlist stream keyword matching.
    """
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[warn] could not read watchlist.json: {e}", flush=True)
        return []
    kws: list[str] = []
    for tier_companies in data.get("tiers", {}).values():
        for co in tier_companies:
            kws.extend(co.get("keywords", []))
            kws.extend(co.get("cn_terms", []))
    # Lowercase everything, drop empties
    return list({k.lower() for k in kws if k.strip()})


def load_watchlist_gnews_queries(path: Path) -> list[str]:
    """
    Build Google News queries per Tier-1 company for targeted watchlist sweeps.
    Returns a list of queries like '"Nvidia" OR "Jensen Huang" AI'.
    """
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []
    queries: list[str] = []
    for co in data.get("tiers", {}).get("1", []):
        kws = co.get("keywords", [])
        if not kws:
            continue
        # Take the first 2 keywords (company name + main product/person) to keep query tight
        terms = " OR ".join(f'"{k}"' for k in kws[:2])
        queries.append(f"({terms}) AI news")
    return queries


# ── trusted-source allowlist ─────────────────────────────────────────────────

def load_trusted_domains(path: Path) -> set[str]:
    """
    Extract the set of allow-listed domains from trusted-sources.md. Scans only the
    source bullet lines (`- **Name** — domain …`), grabbing every domain-like token on
    each — including parenthetical extras like `(+ blogs.nvidia.com)`. Paths after the
    domain (e.g. `cnn.com/business`) are ignored; only the host is kept.
    """
    dom_re = re.compile(r"\b((?:[a-z0-9-]+\.)+[a-z]{2,})\b", re.I)
    domains: set[str] = set()
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except Exception as e:
        print(f"[warn] could not read trusted-sources.md: {e}", flush=True)
        return domains
    for line in lines:
        if not line.lstrip().startswith("- **"):
            continue
        for m in dom_re.findall(line):
            domains.add(m.lower().strip("."))
    return domains


def is_trusted(domain: str, allowlist: set[str]) -> bool:
    """True if `domain` equals, or is a subdomain of, any allow-listed domain."""
    d = (domain or "").lower()
    if not d:
        return False
    return any(d == a or d.endswith("." + a) for a in allowlist)


# ── main pipeline ─────────────────────────────────────────────────────────────

def run_stream(
    stream: str,
    hours: int,
    watchlist_keywords: list[str],
    watchlist_gnews: list[str],
    trusted_domains: set[str],
    trusted_only: bool = True,
    top_n: int = 40,
) -> dict:
    """
    Fetch, filter, score, and return the candidate pool for one stream.
    stream: "ainews" | "watchlist"
    """
    print(f"\n{'='*60}", flush=True)
    print(f"[{stream}] starting (window={hours}h)", flush=True)

    if stream == "ainews":
        keywords      = AI_KEYWORDS
        extra_queries = GNEWS_AI_QUERIES + GNEWS_TH_QUERIES
        gnews_lang_pairs = [("en", "US")] * len(GNEWS_AI_QUERIES) + [("th", "TH")] * len(GNEWS_TH_QUERIES)
    else:  # watchlist
        keywords      = watchlist_keywords
        extra_queries = watchlist_gnews
        gnews_lang_pairs = [("en", "US")] * len(watchlist_gnews)

    # ── Phase 1: collect raw items from all feeds ──
    raw: list[dict] = []
    ok_count = 0

    # 1a. Direct RSS feeds (same for both streams — they cover all trusted outlets)
    print(f"[{stream}] fetching {len(DIRECT_FEEDS)} direct feeds ...", flush=True)
    for feed in DIRECT_FEEDS:
        items, err = fetch_feed(feed["url"], hours)
        if err:
            print(f"  [skip] {feed['name']}: {err}", flush=True)
        else:
            ok_count += 1
            for it in items:
                it["feed_name"] = feed["name"]
            raw.extend(items)
        time.sleep(0.25)  # be polite

    # 1b. Google News RSS sweeps (topic + watchlist per-company)
    print(f"[{stream}] fetching {len(extra_queries)} Google News queries ...", flush=True)
    for i, query in enumerate(extra_queries):
        lang, country = gnews_lang_pairs[i] if i < len(gnews_lang_pairs) else ("en", "US")
        url = gnews_url(query, lang, country, hours)
        items, err = fetch_feed(url, hours)
        if err:
            print(f"  [skip] GNews '{query[:40]}': {err}", flush=True)
        else:
            ok_count += 1
            for it in items:
                it["feed_name"] = f"GNews:{query[:30]}"
            raw.extend(items)
        time.sleep(0.3)

    total_raw = len(raw)
    print(f"[{stream}] raw items: {total_raw} (from {ok_count} feeds)", flush=True)

    # ── Phase 2: dedup by URL ──
    seen_urls: set[str] = set()
    deduped: list[dict] = []
    for it in raw:
        key = dedup_url(it["url"])
        if key and key not in seen_urls:
            seen_urls.add(key)
            deduped.append(it)

    print(f"[{stream}] after URL dedup: {len(deduped)}", flush=True)

    # ── Phase 3: keyword filter + noise gate ──
    candidates: list[dict] = []
    for it in deduped:
        text = it["title"] + " " + it.get("description", "")
        if is_noise(text):
            continue
        matched = keyword_hits(text, keywords)
        if not matched:
            continue
        it["keywords_matched"] = matched
        it["match_count"]      = len(matched)
        it["score"]            = score_item(it, matched)
        # Prefer the REAL publisher domain (from the feed's <source> element) over the
        # link domain, which for Google News items is just the news.google.com redirect.
        it["source"]           = it.get("publisher_domain") or source_domain(it["url"])
        candidates.append(it)

    n_after_keyword = len(candidates)
    print(f"[{stream}] after keyword filter: {n_after_keyword}", flush=True)

    # ── Phase 3.5: trusted-source allowlist (trusted-sources.md) ──
    # Tag every candidate; by default DROP off-allowlist publishers so the pool Claude
    # receives only contains citeable outlets. `--all-sources` keeps everything (still
    # tagged) for wide discovery. On thin days the engine's Step 0.5 fallback supplements
    # with WebSearch, so filtering here is safe.
    for it in candidates:
        it["on_allowlist"] = is_trusted(it["source"], trusted_domains)
    trusted_n = sum(1 for it in candidates if it["on_allowlist"])
    if trusted_only:
        before = len(candidates)
        candidates = [it for it in candidates if it["on_allowlist"]]
        print(f"[{stream}] trusted-source filter: kept {len(candidates)} / {before} "
              f"(dropped {before - len(candidates)} off-allowlist)", flush=True)
    else:
        print(f"[{stream}] allowlist annotation only: {trusted_n}/{len(candidates)} on trusted-sources", flush=True)
    n_after_trusted = len(candidates)

    # ── Phase 4: sort by score desc, take top_n ──
    candidates.sort(key=lambda x: x["score"], reverse=True)
    candidates = candidates[:top_n]

    # ── Phase 5: clean up for JSON output ──
    output_items: list[dict] = []
    for it in candidates:
        output_items.append({
            "title":           it["title"],
            "url":             it["url"],
            "source":          it.get("source", ""),
            "publisher":       it.get("publisher", ""),
            "on_allowlist":    it.get("on_allowlist", False),
            "feed_name":       it.get("feed_name", ""),
            "published_raw":   it.get("published_raw", ""),
            "age_h":           it.get("age_h"),
            "has_timestamp":   it.get("has_timestamp", False),
            "description":     it.get("description", "")[:300],
            "keywords_matched": it.get("keywords_matched", [])[:8],  # trim for readability
            "match_count":     it.get("match_count", 0),
            "score":           it.get("score", 0.0),
        })

    now_bkk = datetime.now(BKK)
    result = {
        "generated_at":  now_bkk.isoformat(),
        "date":          now_bkk.strftime("%Y-%m-%d"),
        "stream":        stream,
        "window_hours":  hours,
        "stats": {
            "feeds_ok":            ok_count,
            "items_raw":           total_raw,
            "items_after_dedup":   len(deduped),
            "items_after_keyword": n_after_keyword,
            "items_after_trusted": n_after_trusted,
            "trusted_filter":      trusted_only,
        },
        "candidates": output_items,
    }
    print(f"[{stream}] {len(output_items)} candidates written", flush=True)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="pboat RSS universe funnel")
    parser.add_argument("--stream", choices=["ainews", "watchlist", "both"],
                        default="both", help="Which stream(s) to generate")
    parser.add_argument("--hours", type=int, default=24,
                        help="Lookback window in hours (default 24)")
    parser.add_argument("--top", type=int, default=40,
                        help="Max candidates per stream (default 40)")
    parser.add_argument("--all-sources", action="store_true",
                        help="Keep off-allowlist publishers too (still tagged on_allowlist). "
                             "Default: drop them so the pool only contains trusted outlets.")
    args = parser.parse_args(argv)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    now_bkk = datetime.now(BKK)
    date_str = now_bkk.strftime("%Y%m%d")

    # Load watchlist + the trusted-source allowlist once
    watchlist_keywords = load_watchlist_keywords(WATCHLIST_PATH)
    watchlist_gnews    = load_watchlist_gnews_queries(WATCHLIST_PATH)
    trusted_domains    = load_trusted_domains(TRUSTED_SRC_PATH)
    trusted_only       = not args.all_sources
    print(f"[init] watchlist keywords loaded: {len(watchlist_keywords)}", flush=True)
    print(f"[init] watchlist GNews queries: {len(watchlist_gnews)}", flush=True)
    print(f"[init] trusted-source domains loaded: {len(trusted_domains)} "
          f"(filter {'ON' if trusted_only else 'OFF — --all-sources'})", flush=True)

    streams = ["ainews", "watchlist"] if args.stream == "both" else [args.stream]

    for stream in streams:
        result = run_stream(
            stream=stream,
            hours=args.hours,
            watchlist_keywords=watchlist_keywords,
            watchlist_gnews=watchlist_gnews,
            trusted_domains=trusted_domains,
            trusted_only=trusted_only,
            top_n=args.top,
        )
        out_path = OUTPUT_DIR / f"universe_{date_str}_{stream}.json"
        out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[{stream}] wrote → {out_path}", flush=True)

    print("\n[done]", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())

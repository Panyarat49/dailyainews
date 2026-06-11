---
name: daily-ai-news
description: Generate a daily Thai-language AI/tech news brief covering up to 5 significant stories from anywhere in the AI/tech world in the last 24 hours (rolling window, Asia/Bangkok), deduplicated against the recent general briefs, each enriched with three expert perspectives (professor / AI specialist / professional programmer). This is the GENERAL brief (no watchlist) — for the company-watchlist monitor use `daily-ai-watchlist`. Writes one Markdown file; the host runner commits it and the email sender delivers it. Use this when the user asks for the "daily AI news brief", a "สรุปข่าว AI วันนี้", or when it runs on schedule.
---

# Daily AI News Brief — General

Thin skill. **First `Read` `.claude/skills/shared/engine.md` and follow it** — that
holds all the shared mechanics (freshness/dedup/tiered-verify/personas/length/output).
This file supplies only what is distinct to the **general** brief.

## Bindings (for the engine)

| Binding | Value |
|---|---|
| `BRIEF_KIND` | `ainews` |
| `OUTPUT_PATH` | `articles/{TODAY}-ainews.md` |
| `DEDUP_GLOB` | `articles/*-ainews.md` (this stream only — never the `-watchlist.md` files) |
| `ARTIFACT_DIR` | `.claude/skills/daily-ai-news/reference/` |
| `EXTRA_GATES` | none beyond engine Gates A (freshness) + B (dedup) |

## SCOPE — what qualifies

**Any genuinely significant AI or technology development from the last 24h**, from
anywhere in the world. Not bounded to a company list. Still must be:
- a real **AI/tech** story (model/product, compute/chips, AI infra/cloud, AI research
  or benchmark, AI-driven business/regulatory move, major incident/outage) — not
  generic non-tech news; and
- **significance = ranking, not a hard drop**: the major events (launch/major update,
  M&A/funding, partnership/contract, chips/data-center capacity, earnings with an AI
  angle, regulation, notable research/benchmark, security/outage, AI-unit exec change)
  rank FIRST. To reach `STORY_COUNT` (4–5, floor 3) you may then fill with less-major
  but genuinely AI/tech-relevant stories (incl. minor launches/updates, smaller funding).
- **Always drop** (never fill with these): recycled rumor, pure opinion/listicles, and
  generic non-AI / non-tech commentary.

## SEARCH_STRATEGY

Broad first, efficient. ~4–8 searches on a normal day:
1. **Wide pass:** `AI news today`, `AI model / chip launch today`, Thai `ข่าว AI วันนี้`
   / `ปัญญาประดิษฐ์`, one CN `AI 新闻` if useful. Add a date hint (`qdr:d`) when supported.
2. **Source-targeted top-ups:** `site:techcrunch.com AI`, `site:blognone.com AI`, etc.,
   for trusted outlets that often carry same-day frontier news.
Map each surfaced story to a publisher on `trusted-sources.md`; discard off-list outlets.

## SELECTION

Fill to the shared `STORY_COUNT` policy: land at **4–5**, **try hard never below 3**
(`shared/defaults.json`: min 3 / prefer 4 / max 5). Verify each (engine 1b-ver, Tier-1
preferred). Rank, in order:
1. **Significance** (launches / M&A / regulation outrank incremental updates).
2. **Breadth** — prefer distinct companies/topics over stacking one story.
3. **Source mix** — aim for ≥1 Thai-language source and ≥3 international when supply allows.
4. Prefer primary announcements over commentary; Tier 1 over Tier 2 for the same story.

Take the significant items first, then **backfill with relevant-but-less-major AI/tech
stories** (still real + within 24h + on a trusted source) to reach 4–5. If short of 3,
**search harder** (more queries / outlets / Thai + CN angles) before settling. Only a
genuinely dead 24h ships <3 (flag it) or 0 (stub) — never pad with older or off-topic
items. Story 1 is the day's most material item; the TL;DR mirrors the top three.

## HEADING_FORMAT

```
### N. {Headline} — [{Publisher}]({URL})
```
No company/ticker/tier (this is the general brief). The trailing ` — [{Publisher}]({URL})`
is required (the email sender parses it). No roundup blocks in this brief.

## Title suffix / footer
- H1 title suffix: **none** (plain `# สรุปข่าว AI ประจำวันที่ {TODAY}`).
- No watchlist-coverage footer.

Everything else (preflight, dedup mechanics, verification, sources.md template, the
three perspectives, the integrated rewrite, length budget, write-only output, final
report, error-handling) is in `engine.md`. Do not re-derive it here.

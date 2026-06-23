# DEVLOG — pboat (dailyainews) change history

> **What this file is:** the running log of notable changes to this repo — what changed, why,
> and how to maintain it. Read the newest entry first. For the *current* end-to-end pipeline see
> the README ("Hosts" + flow diagram); this file is the history of how it got there.

---

## 2026-06-23 — Smarter WebFetch banner: distinguish Actions-fetched bodies from degraded snippet runs

**Problem.** The engine had two banner states — no banner (`WEBFETCH_OK`) or the alarming
"RSS snippet" banner (`WEBFETCH_BLOCKED`). But on every scheduled run GitHub Actions pre-fetches
full article bodies into `body_text` in the universe JSON. When Claude's own WebFetch was
blocked, it was still verifying from Tier-1 article bodies already on disk — not degraded
snippets — yet the banner falsely implied the opposite. The fix is a pure `engine.md` change;
no script or workflow was touched.

**Delivered on branch `claude/vigilant-ride-6pj4mq`** (commits `a000e65` brief, `f80c72b` engine fix).

### What changed (`.claude/skills/shared/engine.md` only)

**Step 2 — Verification-mode visibility** now has four cases instead of two:

| State | Banner shown |
|---|---|
| `WEBFETCH_OK` (with or without funnel bodies) | none |
| `WEBFETCH_BLOCKED` + `stats.items_enriched > 0` (funnel fetched full bodies — the normal scheduled path) | soft informational: _"WebFetch ถูกบล็อกใน Claude session นี้ แต่ GitHub Actions เข้าถึงบทความฉบับเต็มได้ — การตรวจสอบข่าวรอบนี้ใช้ข้อมูล Tier 1 จากบทความที่ดึงไว้ล่วงหน้าโดย Actions"_ |
| `WEBFETCH_BLOCKED` + `items_enriched = 0` (only RSS snippets — genuinely degraded) | existing alarming banner |
| No funnel, WebSearch snippets only | existing alarming banner |

**Error-handling table** (`WEBFETCH_BLOCKED` row): now branches on `items_enriched`. If `> 0`,
runner tags `[verify=funnel]` (not `[verify=search]`) and uses the soft banner. If `= 0`,
existing degraded path applies.

**Also produced today:** `articles/2026-06-23-ainews.md` (Anthropic Mythos NSA breach, Groq
$650M, Google DeepMind A24, Thailand Siam Silica, Samsung ChatGPT Enterprise) and
`articles/2026-06-23-watchlist.md` (Nvidia ISC 2026 roundup: Halos for Robotics + 35 Europe AI
supercomputers + Vera Rubin; Alphabet $75M A24; Alibaba HappyHorse 1.1 #2; Microsoft Chevron
power deal; Tesla Autopilot fatal crash pushback). Both verified at Tier 1 from funnel body_text.

**Not changed.** Funnel script, workflows, email chain, article format, perspectives, story-count targets.

---

## 2026-06-22 — Full-text bypass + multi-factor ranking + ranked Excel + Codex backup

Three changes, all bringing pboat closer to the cafeinvest (pjah) design. Delivered on
branch `fixed-403-rank-codex` (commits `da3fe58`, `6c48a0c`). pjah was read-only reference;
nothing in that repo was changed.

**Goal.** Close the three gaps the local routine couldn't cover: (1) deliver a **full-quality
brief even when the writer's `WebFetch` is 403-blocked**, (2) give every story a **transparent
relevance score exported to Excel** so the brief is written from the highest-rated items (not a
flat discovery list), and (3) add a **Claude-independent cloud backup writer** so a Claude
outage no longer means no brief.

### Issue 2 — Pre-fetch full article bodies (the real WebFetch-403 bypass)

**Problem.** The 2026-06-19 change made a blocked run citeable, but only at **Tier-2 snippet**
quality (≤300-char RSS `description`). pjah avoids 403 entirely because its *Python funnel*
fetches the full article body (browser UA + Playwright) and commits it — so its writer never
calls WebFetch. pboat's funnel only fetched RSS, so the writer still had to WebFetch each body
(→ 403) or fall back to thin snippets.

**Fix.** Port pjah's extraction into the funnel so `body_text` is committed in the universe JSON.

`.github/scripts/pboat_universe.py`:
| Chunk | Before | After |
|---|---|---|
| dependency bootstrap | imported `requests`, `feedparser` only | + optional Playwright import block setting `PLAYWRIGHT_OK` (degrades gracefully if absent) |
| headers | one `UA` dict (RSS `Accept`) | + `ARTICLE_HEADERS` (HTML `Accept`, same browser UA) for fetching article *pages* |
| new functions | — | `is_gnews()`, `extract_article()` (browser-UA requests), `ensure_chromium()`, `pw_fetch()` (headless Chromium; resolves `news.google.com` redirects to the real article), `enrich_item()` |
| `run_stream()` | scored, sorted, wrote JSON | + **Phase 4.5**: enrich the top `enrich_n` (default 12) picks with `body_text`; output items gain `resolved_url`, `body_text`, `extract_status`; stats gain `items_enriched`, `playwright` |
| `run_stream()` signature | `(…, top_n)` | `(…, top_n, enrich_n=12, use_playwright=True)` |
| CLI flags | `--stream --hours --top --all-sources` | + `--enrich-n`, `--no-enrich`, `--no-playwright` |

`.github/workflows/pboat-data.yml`:
| Chunk | Before | After |
|---|---|---|
| deps install | `pip install requests feedparser` | `pip install requests feedparser playwright` + new step `python -m playwright install --with-deps chromium` |
| job timeout | `timeout-minutes: 15` | `timeout-minutes: 25` (headroom for Chromium + per-article fetch) |

`.claude/skills/shared/engine.md`:
| Chunk | Before | After |
|---|---|---|
| Step 0.5 field list | listed `description`, `published_raw`, `has_timestamp` | + `body_text`, `extract_status`, `resolved_url`; explains body_text = Tier-1-grade evidence already on disk |
| Step 0.5 item 4 | branch on WebFetch probe (OK→fetch, BLOCKED→snippet) | priority order: **`body_text` first** (verify from it, no WebFetch — works even when blocked) → else WebFetch (OK) → else funnel snippet (blocked) |
| §1b-ver tier table | Tier-1 Full fetch / Tier-2 snippet | + **"Tier 1 — funnel body"** row (preferred, no egress); Full-fetch now only for picks lacking body_text |
| sources.md template | `Runtime:` line | + `Verification mode: {funnel\|webfetch\|search}` line |
| commit-tag note | `[verify={webfetch\|search}]` | `[verify={funnel\|webfetch\|search}]` |

`.github/workflows/daily-brief.yml` (the Actions backup runner):
| Chunk | Before | After |
|---|---|---|
| verify-tag logic | `verify=webfetch`; if `WEBFETCH_BLOCKED` in sources.md → `search` | reads the engine's `Verification mode:` line → `funnel\|webfetch\|search`; old heuristic kept as fallback |

### Issue 1 — Multi-factor ranking in JSON + a ranked Excel workbook

**Problem.** pboat's score was trivial (recency + keyword-hit count) and there was no Excel —
unlike pjah, which ranks every story with a transparent multi-factor score and exports a
multi-tab workbook. The writer also re-ranked from scratch instead of leading with the score.

**Fix.** Port pjah's scoring structure (adapted to AI/tech) + an Excel exporter.

`.github/scripts/pboat_universe.py`:
| Chunk | Before | After |
|---|---|---|
| required deps | `("requests", "feedparser")` | `("requests", "feedparser", "openpyxl")` |
| `score_item()` | `recency(0–2) + min(hits,5)*0.8` → returns `float`; signature `(item, matched)` | multi-factor: `recency(banded) + signal + source_role + corroboration + watchlist_tier` → returns `(score, breakdown)`; signature `(item, stream)` |
| new scoring constants | — | `ROLE_W` (primary 2.0 / citation 1.2 / screening 0.5), `WL_TIER_W` (T1 +1.5 / T2 +0.8), `SCORING_README` |
| clustering | — | `tokenize()` + `cluster()` → `cluster_size` = cross-outlet corroboration |
| source roles | — | `load_source_roles()` + `source_role()` (parse trusted-sources.md sections A/A2→primary, B→citation, C→screening) |
| watchlist tagging | flat keyword list only | + `load_watchlist_companies()` + `tag_watchlist()` → `matched_company`, `company_tier` |
| Excel | — | `export_universe_xlsx()` + style constants → combined workbook |
| `run_stream()` phases | Phase 3 scored inline; Phase 4 sorted | Phase 3 (no inline score) → **3.4 cluster** → **3.45 watchlist tag** → 3.5 trusted → **3.6 score (with source_role)** → Phase 4 sort |
| `run_stream()` signature | `(…, trusted_domains, trusted_only, top_n, …)` | + `source_roles`, `watchlist_companies` |
| output item fields | …`score` | + `source_role`, `cluster_size`, `matched_company`, `company_tier`, `score_breakdown` |
| result top-level | `stats`, `candidates` | + `scoring` (the SCORING_README block) |
| `main()` | loop streams → write JSON each | + loads `source_roles`/`watchlist_companies`; collects `results` dict; after loop writes `universe_<DATE>.xlsx` + `universe-latest.xlsx` (Excel failure never aborts the run) |

`.github/workflows/pboat-data.yml`:
| Chunk | Before | After |
|---|---|---|
| deps install | `requests feedparser playwright` | + `openpyxl` |
| commit step | `git add …universe_*.json` | + `git add …universe_*.xlsx universe-latest.xlsx` |

`.claude/skills/shared/engine.md`:
| Chunk | Before | After |
|---|---|---|
| Step 0.5 field list | ranking not mentioned | + the ranking fields (`score`, `score_breakdown`, `cluster_size`, `source_role`, `matched_company`, `company_tier`) |
| Step 0.5 | (no lead-with-score rule) | + **item 2b**: candidates are pre-ranked; **lead selection with `score`**, use `cluster_size` as corroboration, don't re-rank from scratch |
| output template footer | skill footer only | + "full ranked universe (Excel)" link to `universe-latest.xlsx` (only when funnel JSON was used) |

**Excel layout** (`universe-latest.xlsx`, same concept as pjah's `universe-latest.xlsx`):
`AI news — all` (sorted by score) · `AI news — top` · `Watchlist — all` · `Watchlist — top` ·
`Watchlist — by company`. Styled header, frozen row, auto-filter, clickable URLs.

### Issue 3 — Codex cloud backup writer (no repo code change)

A Claude-independent third writer, mirroring pjah's `docs/CAFEINVEST-CODEX-BACKUP.md`. It is an
**external OpenAI Codex cloud automation**, so there is **no code in this repo** for it — the
only in-repo enabler is Issue 1's Excel-footer link + the `body_text` data it writes from.
- Schedule: **daily 09:00 Asia/Bangkok**, repo `Panyarat49/dailyainews`, branch `main`.
- It gap-fills each stream independently (writes `articles/<DATE>-{ainews,watchlist}.md` only if
  missing AND that stream's `universe_<DATE>_<stream>.json` exists), writing strictly from the
  committed JSON's `body_text`. Commits to `main` → `email-notify.yml` delivers.
- Sits between the ~07:00 Claude routine and the 13:49 Actions backup. The prompt lives in the
  Codex automation (not committed here yet; a `docs/PBOAT-CODEX-BACKUP.md` can be added later).

### How it works now (the daily runtime flow)

1. **05:57 BKK — `pboat-data.yml` → `pboat_universe.py`.** RSS + Google-News sweep →
   keyword/noise filter → **cluster** near-identical headlines (corroboration) → tag trusted
   domains + their role (primary/citation/screening) + watchlist company/tier → **multi-factor
   score** → **enrich the top 12/stream** with full `body_text` (browser-UA requests, Playwright
   for Google-News redirects + 403s). Commits `universe_<date>_<stream>.json` (now carrying
   `body_text`, `score`, `score_breakdown`, `cluster_size`, the `scoring` README) **and**
   `universe-latest.xlsx`.
2. **~07:00 BKK — Claude routine.** Engine Step 0.5 reads the JSON: candidates are pre-ranked,
   so it **leads selection with `score`** and verifies each pick from its `body_text`
   (**Tier-1 funnel body — no WebFetch**, so the 403 block is moot). Writes the briefs, footer
   links the Excel → email fires.
3. **~09:00 BKK — Codex cloud backup.** If a brief is missing, writes it from the same JSON's
   `body_text` and commits to `main` → email fires. (External automation; not in this repo.)
4. **13:49 BKK — `daily-brief.yml`.** Final always-on floor if a brief is still missing; tags
   the commit `[verify=funnel|webfetch|search]` from the engine's `Verification mode:` line.

The new artifacts: per-stream JSON gains the body + ranking fields; **`universe-latest.xlsx`**
is the human-readable ranked workbook (tabs: AI news all/top, Watchlist all/top, by company).

**Not changed.** Email chain, freshness/dedup gates, trusted-sources allowlist, perspectives,
article format, story-count targets, the two `SKILL.md` files.

---

## 2026-06-19 — WebFetch-block wiring: funnel snippets become first-party Tier-2 evidence

**Problem.** The active writer is the claude.ai cloud Routine, where `WebFetch` is
403-blocked → every brief landed `[verify=search]` with the degraded banner. The RSS
funnel (`pboat_universe.py`, runs in Actions where egress is **open**) already writes a
`description` snippet + `published_raw` timestamp per candidate — everything a blocked run
needs for a real Tier-2 — **but the engine never told the writer those fields existed**, so
it fell back to live WebSearch (also flaky in a blocked host) instead of using the snippet
it already had on disk. The fix is a pure `engine.md` wiring change — **no script/workflow
or funnel-output change** (the JSON already carries the fields).

### What changed (`.claude/skills/shared/engine.md` only)
| Section | Change |
|---|---|
| Step 0.5 — field list | Documents `description`, `published_raw`, `has_timestamp`; notes the funnel runs in an **unblocked** runner, so these are first-party evidence even when this routine's `WebFetch` is blocked. |
| Step 0.5 — item 4 | After gates, **branch on the WebFetch probe**: `WEBFETCH_OK` → Tier-1 WebFetch; `WEBFETCH_BLOCKED` → **Tier-2 directly from the funnel** (`source` + `published_raw` + `description`), do **not** fall back to WebSearch. A blocked run is now a real citeable brief, not a stub. |
| §1b-ver — Tier-2 row | Renamed "Tier 2 — Snippet (funnel ▸ or WebSearch)"; the snippet may come from the funnel (**preferred**, needs no egress) or WebSearch. |
| §1b-ver — provenance/date | Freshness date hierarchy now body → **funnel `published_raw`** → slug; a funnel `candidates[]` entry is sufficient citation provenance on its own (no longer "must appear in a WebSearch result"). |
| Step 1d — sources.md template | Verification enum adds `Tier 2 — funnel snippet`. |
| Step 2 — degraded banner | Two wordings: funnel-snippet (normal blocked path) vs WebSearch-snippet; pick the one matching where the evidence came from. |
| Error-handling table | `WEBFETCH_BLOCKED` row: prefer the funnel snippet over WebSearch. |

**Effect.** The cloud writer no longer depends on `WebFetch` *or* `WebSearch` for the core:
a blocked run summarizes from the funnel's first-party RSS snippet + real timestamp.
`WebFetch` becomes a Tier-1 *upgrade* when available, never a hard dependency. Commit still
tags `[verify=search]` when no WebFetch happened (accurate), but the brief is real, not a
degraded stub.

**Not changed.** `pboat_universe.py` output shape, the workflows, email chain, story-count
targets, freshness/dedup gates, trusted-sources allowlist, perspectives, article format.

### Maintenance notes
- The engine is the single source of truth for these mechanics (per its Editability rule);
  the two `SKILL.md` Step 0.5 callouts just point here and were left unchanged.
- Open follow-up (NOT done here): the funnel is **hardcoded-list-driven** (14 `DIRECT_FEEDS`
  + a few Google-News topic queries) vs. cafeinvest's **catalog-driven** `sources_catalog.json`
  (235 sources, per-source `site:` sweep). Same funnel *pattern*, narrower active gather.
  Aligning to a catalog is an optional coverage upgrade, tracked separately.

---

## 2026-06-17 — RSS Universe Funnel (Option A hybrid upgrade)

**Goal:** Replace Claude's manual WebSearch pass with a richer, RSS-sourced candidate
pool while keeping all existing quality guarantees (freshness gate, dedup, Tier-1
WebFetch verification). Inspired by the sourcing architecture in pjah
(DailyNewsP-Jah/cafeinvest_brief.py). pjah files were read-only; nothing in that repo
was modified.

---

### What changed

#### New files

| File | Purpose |
|---|---|
| `.github/scripts/pboat_universe.py` | RSS funnel script — pulls feeds, keyword-filters, scores, writes JSON candidate pools |
| `.github/scripts/output/.gitkeep` | Ensures the output directory is tracked in git |
| `.github/workflows/pboat-data.yml` | GitHub Actions workflow that runs the funnel daily at 05:57 BKK (22:57 UTC) |

#### Modified files (non-email, sourcing only)

| File | Change |
|---|---|
| `.claude/skills/shared/engine.md` | Added **Step 0.5 — Universe pre-load** between Step 0 and Step 1 |
| `.claude/skills/daily-ai-news/SKILL.md` | Added Step 0.5 callout at the top of `SEARCH_STRATEGY` |
| `.claude/skills/daily-ai-watchlist/SKILL.md` | Added Step 0.5 callout at the top of `SEARCH_STRATEGY` |

#### Untouched files (email + delivery chain)

- `.github/scripts/send_email.py` — unchanged
- `.github/workflows/email-notify.yml` — unchanged
- `.github/workflows/promote-brief.yml` — unchanged
- `.github/workflows/daily-brief.yml` — unchanged

---

### How the new flow works

```
05:57 BKK  pboat-data.yml runs pboat_universe.py  (22:57 UTC — off-peak, beats the 06:00 queue)
             └─ fetches ~14 direct RSS feeds (TechCrunch, Verge, Blognone, etc.)
             └─ fetches 5 Google News AI queries + 2 Thai queries
             └─ fetches 10 Google News per-company queries (Tier-1 watchlist)
             └─ keyword-filters → deduplicates → scores by recency + keyword hits
             └─ writes output/universe_{YYYY-MM-DD}_ainews.json     (top 40)
             └─ writes output/universe_{YYYY-MM-DD}_watchlist.json  (top 40)
             └─ commits with [skip email]

07:11 BKK  Claude Routine wakes up, runs daily-ai-news skill:
             └─ Step 0.5: reads universe_{TODAY}_ainews.json (fresh ≤ 4h ✅)
             └─ loads candidates[] as START_POOL (~40 pre-screened items)
             └─ applies Gate A (≤24h) + Gate B (dedup) → keeps qualifying items
             └─ if ≥8 survive → skips WebSearch, goes straight to WebFetch verify
             └─ Step 1b-ver: WebFetches each candidate → confirms headline + timestamp
             └─ Steps 2–6: writes Thai brief, perspectives, article → commits

           Then runs daily-ai-watchlist skill (same pattern with watchlist JSON)
```

---

### Design decisions

**Why RSS + Google News, not just direct crawling?**
RSS is fast (one HTTP call per feed, no JS rendering), reliable (structured XML with
publish timestamps), and catches everything a site publishes — not just what a keyword
search surfaces. Google News RSS adds breadth across sources we don't have direct feed
URLs for, and handles Thai/Chinese queries natively.

**Why keep WebFetch verification?**
RSS items may have stale or missing timestamps, and Google News aggregation can surface
off-topic results. Claude still WebFetch-verifies each story body + timestamp before
including it — the JSON only replaces the initial discovery step, not the quality gate.

**Why top 40 candidates (not a strict 5)?**
Gate A (freshness) and Gate B (dedup) applied by Claude will reduce the pool. Giving
Claude 40 candidates ensures it has enough raw material to reach 4–5 stories even after
gates and significance ranking.

**Real publisher recovery (Google News).** Google News RSS `<link>`s are `news.google.com`
redirects, so the funnel reads each item's `<source url="…">Publisher</source>` element
(exposed by feedparser as `entry.source`) to fill the real `source` domain + `publisher`
name — no extra HTTP call — and strips the " - Publisher" suffix Google appends to titles.
Without this, ~90% of candidates showed `source: news.google.com`, which is useless for
allowlist matching.

**Trusted-source filtering (default ON).** After keyword + dedup, the funnel drops any
candidate whose real publisher isn't on `trusted-sources.md`, so the pool only contains
citeable outlets. `load_trusted_domains()` parses the allowlist; `is_trusted()` matches a
candidate domain to it (exact or subdomain). Rationale: the engine already forbids citing
off-allowlist sources, but the pre-screened pool shouldn't tempt that — defense in depth.
`--all-sources` disables the drop (items kept, tagged `on_allowlist: false`) for wide
discovery; engine Step 0.5 then treats off-allowlist items as discovery-only. Measured on
2026-06-17: ainews 349 keyword → 73 trusted; watchlist 734 → 101 — both well above the
≥8 threshold, so filtering doesn't starve the pool (and Step 0.5 falls back to WebSearch if
it ever did).

**Fallback behaviour**
If `pboat-data.yml` doesn't run (weekend manual trigger, GitHub outage, first day), the
JSON simply won't exist. Engine Step 0.5 detects this and falls back silently to the
original WebSearch flow — no error, no stub, zero user impact.

**What we did NOT change**
- Story count targets (4–5, floor 3)
- Freshness gate (≤24h)
- Dedup window (7 days)
- Trusted-sources allowlist
- The three-persona perspectives
- Email delivery chain
- Article format / heading format

---

### Keyword coverage

**ainews stream** (`AI_KEYWORDS` in pboat_universe.py):
Labs/models, generic AI terms, hardware (GPUs/chips/HBM), cloud/infra, products,
policy/safety, investment signals, Thai terms, Chinese terms (人工智能/大模型/芯片).

**watchlist stream**:
Dynamically extracted from `watchlist.json` — all `keywords` and `cn_terms` across
Tier 1 + Tier 2, lowercased and deduplicated. Plus per-company Google News queries
for each Tier-1 company (e.g. `("Nvidia" OR "Jensen Huang") AI news`).

---

### Maintenance notes

- **To add a new RSS feed:** add an entry to `DIRECT_FEEDS` in `pboat_universe.py`.
- **To add a new Google News query:** add to `GNEWS_AI_QUERIES` or `GNEWS_TH_QUERIES`.
- **To change the schedule:** edit the `cron` in `pboat-data.yml`. Keep it ≥ 1h before the Claude Routine, and avoid UTC minute `:00` (top-of-hour queue congestion on GitHub Actions). Note 06:00 BKK = 23:00 UTC is a double-congestion slot; 22:57 UTC sidesteps it.
- **To widen the lookback window:** change `--hours` in the workflow or pass it in `workflow_dispatch`.
- **To disable the pre-screen:** rename or delete the JSON file before the Routine runs — it will fall back to WebSearch automatically.
- **To check what ran:** GitHub Actions → `pboat RSS universe funnel` → latest run logs.

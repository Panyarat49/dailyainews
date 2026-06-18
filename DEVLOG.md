# DEVLOG — pboat (dailyainews) change history

> **What this file is:** the running log of notable changes to this repo — what changed, why,
> and how to maintain it. Read the newest entry first. For the *current* end-to-end pipeline see
> the README ("Hosts" + flow diagram); this file is the history of how it got there.

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

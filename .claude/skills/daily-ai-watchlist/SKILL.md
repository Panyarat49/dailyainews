---
name: daily-ai-watchlist
description: Generate a daily Thai-language AI/tech news brief that MONITORS a configured company watchlist (defined in `reference/watchlist.json`) across two priority tiers. Surface up to 5 significant, AI/tech-relevant stories from the last 24h (rolling, Asia/Bangkok), prioritizing Tier-1 companies and descending to Tier 2 only to top up; deduplicated against the recent watchlist briefs; each enriched with three expert perspectives. This is the WATCHLIST monitor — for general AI news use `daily-ai-news`. Writes one Markdown file; the host runner commits it and the email sender delivers it. Use when the user asks for the watchlist brief / company monitor, or when it runs on schedule.
---

# Daily AI News Brief — Watchlist Edition

Thin skill. **First `Read` `.claude/skills/shared/engine.md` and follow it** — that
holds the shared mechanics. This file supplies only what is distinct to the
**watchlist** brief. It is **entity-driven**: it monitors the universe in
`reference/watchlist.json`, not "any AI news."

## Bindings (for the engine)

| Binding | Value |
|---|---|
| `BRIEF_KIND` | `watchlist` |
| `OUTPUT_PATH` | `articles/{TODAY}-watchlist.md` |
| `DEDUP_GLOB` | `articles/*-watchlist.md` (this stream only — never the `-ainews.md` files) |
| `ARTIFACT_DIR` | `.claude/skills/daily-ai-watchlist/reference/` |
| `EXTRA_GATES` | Gate C (AI/tech relevance), Gate D (significance), Gate W (watchlist membership) |

## Per-skill preflight (engine Step 0.4)
`Read` `reference/watchlist.json`. Validate it parses and has `tiers.1` and `tiers.2`.
Cache `WATCHLIST` and `_meta` (`target_story_count`, `roundup_update_cap`,
`dedup_window_days`, `tier_descent`, `bloomberg_enabled`). **`watchlist.json` is the
SINGLE SOURCE OF TRUTH** for the monitored universe (companies, tiers, tickers,
keywords, cn_terms) AND its tuning knobs — read these, never hardcode; to change the
universe or a knob, edit `watchlist.json` only. If missing/unparseable → abort.
Use `_meta.dedup_window_days` as the engine's dedup window. **Story counts follow the
shared `STORY_COUNT` policy** (`shared/defaults.json`: min 3 / prefer 4 / max 5 — aim 4–5,
floor 3), NOT a single target. (`_meta.target_story_count` is superseded by `STORY_COUNT`.)

## SCOPE — what qualifies
Only stories about a company in `WATCHLIST`, that are AI/tech-relevant AND significant.
Tickers are not used for selection; company **keywords / cn_terms** drive the search.
*(V2, inert: a Tier-0 Bloomberg stream + quantitative significance leg activate only
when `_meta.bloomberg_enabled = true`; ignore in V1.5.)*

## SEARCH_STRATEGY — wide first, then narrow

> **Check engine Step 0.5 first.** If `.github/scripts/output/universe_{TODAY}_watchlist.json`
> exists and is fresh (≤ 4 h old), load its `candidates[]` as START_POOL and skip or reduce
> the searches below (see engine Step 0.5 for exact logic). The JSON is pre-filtered for
> watchlist company keywords, so Gate W is likely already satisfied — still verify each
> candidate with WebFetch and apply all gates before including. If START_POOL is thin (< 8
> candidates after gates), supplement with the per-company gap-fill searches (steps 3–4 below).

Do NOT blindly run one search per company. ~4 wide + up to ~6 gap-fill = under 10 on a
normal day; Tier-2 days add a few.
1. **Wide pass (~2–4 searches):** broad WebSearches for the day's significant AI/tech
   stories (`AI news today`, `AI chip / model launch today`, Thai `ข่าว AI วันนี้`, one
   CN `AI 新闻`). One day's big stories usually surface several watchlist names at once.
2. **Map** each surfaced story to a watchlist company via its `keywords` / `cn_terms`;
   discard anything off-watchlist (Gate W).
3. **Gap-fill (targeted):** for each **Tier-1** company not yet covered, run ONE
   keyword search (`"Nvidia" OR "Blackwell" AI`, `site:techcrunch.com Nvidia`, `腾讯 混元`).
   Skip companies already covered.
4. **Tier-2 descent:** only if Tier 1 cannot reach `TARGET` significant stories.

## EXTRA_GATES (beyond engine A + B)
- **Gate W — Watchlist membership.** The story's company must be in `WATCHLIST`
  (matched via keywords/cn_terms). Off-watchlist → drop.
- **Gate C — AI/tech relevance.** A genuine AI or technology development involving the
  company (model/product, compute/chips, cloud/AI infra, AI research, AI-driven
  business move, AI regulation). A non-AI corporate story → drop.
- **Gate D — Significance (ranking + fill, NOT a hard drop).** Significant events rank
  FIRST: model/product launch or major update · M&A, strategic investment, or funding ·
  major partnership/customer/contract · chips/compute/data-center capex or capacity ·
  earnings/guidance **with an AI angle** · regulatory/legal/antitrust/export-control
  touching AI · exec/org change in an AI unit · security/safety/major outage · notable
  research/benchmark. To reach the `STORY_COUNT` floor/target you MAY then **fill with
  less-major but genuinely AI/tech-relevant** on-watchlist items. Still **drop outright**:
  recycled rumor, pure opinion/listicles, and generic non-AI commentary — filler must
  still be real AI/tech news about a watchlist company.

## SELECTION — tiers, top-up, roundup, fill
Counts follow shared `STORY_COUNT` (min 3 / prefer 4 / max 5).
1. From **Tier 1** candidates passing the gates, group by company, rank by significance,
   select **one slot per company**, strongest first, up to `max`.
2. **Top-up descent.** If fewer than `prefer` (4) slots filled, take **Tier 2** candidates
   (same gates), top up — strongest first, one slot per company. (`tier_descent = "top-up-to-target"`.)
3. **Fill to 4–5 (floor 3).** If still short, **backfill with less-major but genuinely
   AI/tech-relevant on-watchlist items** (Gate C + W pass) across both tiers until you reach
   4–5, **never below 3**. Search harder first (per-company gap-fill, Thai + CN angles).
4. **Roundup block.** A company with **≥2** items today → **one slot** rendered as a roundup
   (see heading), capped at `roundup_update_cap` (default 3), strongest first.
5. Only a genuinely dead 24h ships **<3** (flag in sources.md) or **0** (stub naming the
   blocking gate). Never reach past 24h or pad with off-topic items. Never exceed `max`.
Record `TIERS_USED` (`1` or `1+2`) for sources.md and the runner's commit tag.
**Priority order:** (1) tier (Tier 1 above Tier 2), (2) significance, (3) breadth.

## HEADING_FORMAT
Single-story slot:
```
### N. {Company} ({TICKER} · Tier {n}) — {Headline} — [{Publisher}]({URL})
```
Roundup slot (one of the slots; a company with ≥2 updates):
```
### N. {Company} ({TICKER} · Tier {n}) — อัปเดตสำคัญ {k} รายการ
**N.1 {Headline A} — [{Publisher}]({URL})**
{2–3 sentences + integrated perspectives}
**N.2 {Headline B} — [{Publisher}]({URL})**
```
The trailing ` — [{Publisher}]({URL})` (single slots) and the `**N.M … — [Pub](URL)**`
sub-items (roundups) are **load-bearing** — the email sender parses them.

## Title suffix / footer
- H1 title suffix: ` — Watchlist` (i.e. `# สรุปข่าว AI ประจำวันที่ {TODAY} — Watchlist`),
  so it's distinct from the general brief in an inbox.
- **Watchlist-coverage footer** (append before the `---`):
  > ## การครอบคลุม watchlist
  > คัดจาก Tier {1 | 1+2} · บริษัทที่มีข่าวสำคัญวันนี้: {list} · {"Tier 2 ไม่ถูกเรียกใช้" | "เติมจาก Tier 2: {list}"}
- `sources.md` must also include a **significance ledger** (Company | Tier | Significant? |
  Reason | Selected) and a **tier-descent record**, in addition to the engine's per-story ledger.

Everything else (preflight base, dedup mechanics, verification, perspectives, integrated
rewrite, length budget, write-only output, final report, error-handling) is in
`engine.md`. Do not re-derive it here.

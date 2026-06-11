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
Let `TARGET = _meta.target_story_count`. Use `_meta.dedup_window_days` as the engine's
dedup window.

## SCOPE — what qualifies
Only stories about a company in `WATCHLIST`, that are AI/tech-relevant AND significant.
Tickers are not used for selection; company **keywords / cn_terms** drive the search.
*(V2, inert: a Tier-0 Bloomberg stream + quantitative significance leg activate only
when `_meta.bloomberg_enabled = true`; ignore in V1.5.)*

## SEARCH_STRATEGY — wide first, then narrow
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
- **Gate D — Significance (qualitative checklist).** Must match a material event type:
  model/product launch or major update · M&A, strategic investment, or funding ·
  major partnership/customer/contract · chips/compute/data-center capex or capacity ·
  earnings/guidance **with an AI angle** · regulatory/legal/antitrust/export-control
  touching AI · exec/org change in an AI unit · security/safety/major outage · notable
  research/benchmark. **Not** significant (drop): routine analyst rating/price-target
  changes, recycled rumor, opinion/listicles, minor feature tweaks, generic commentary.

## SELECTION — tiers, top-up, roundup
1. From **Tier 1** candidates passing all gates, group by company, rank by significance,
   select **one slot per company**, strongest first, up to `TARGET`.
2. **Top-up descent.** If fewer than `TARGET` slots filled, take **Tier 2** candidates
   (same gates), top up — strongest first, one slot per company — until `TARGET` or out
   of significant items. (`tier_descent = "top-up-to-target"`.)
3. **Roundup block.** If a selected company has **≥2** significant updates today, keep it
   as **one slot** rendered as a roundup (see heading), capped at `roundup_update_cap`
   (default 3), strongest first.
4. Fewer than `TARGET` significant across both tiers → ship what you have. Never pad.
5. **0** stories → one-line stub naming the blocking gate (A/B/C/D/W). The empty-day
   signal is information.
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

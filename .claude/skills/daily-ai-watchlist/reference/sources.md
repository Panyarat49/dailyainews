# Sources — 2026-08-09 (watchlist)

Generated: 2026-08-09 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel   # funnel body_text for Amazon/Nvidia items; Tier-2 headline-only for Apple/Alibaba (funnel description was headline-only, cross-verified via WebSearch)
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok) — all 3 selected items are same-day (<24h)
Dedup against: last 7 watchlist briefs (38 URLs loaded)
Tiers used: 1 (Tier 2 searched for top-up but nothing fresh/significant found — see below)
Story count: 3 (below `prefer` 4 — see shortfall note)

## Significance ledger
| Company | Tier | Significant? | Reason | Selected |
|---|---|---|---|---|
| Amazon | 1 | ✅ | Data-center capex/climate-regulatory exposure (major); Anthropic (Claude Code) product update (minor, fill) | ✅ roundup (2 items) |
| Nvidia | 1 | ✅ | AI infra capacity build-out (major, launch of new AI factory) | ✅ |
| Apple | 1 | ✅ | Strategic AI partnership move (Qwen integration for China) — also touches Alibaba (Tier 1) | ✅ |
| Alibaba | 1 | partial | Covered indirectly via the Apple/Qwen story; the day's other Alibaba item (pricing) is a rehash of an already-published story | not separately selected |
| Microsoft, Alphabet, Tesla, Meta, AMD, Oracle | 1 | — | No AI/tech story from these companies cleared both freshness (<24h write-up) AND verifiable-content gates today; Alphabet's DeepMind/Hassabis story only existed as an unresolved news.google.com redirect with no fetchable body — dropped rather than cite an unverified link | not selected |
| TSMC, Tencent, Xiaomi, Micron, Palantir, others | 2 | — | Gap-fill searches run; nothing fresh (<24h) and AI/tech-significant surfaced | not selected |

## Tier-descent record
Tier 1 alone did not reach `prefer` (4). Ran explicit Tier-2 gap-fill searches
(TSMC, Micron, Palantir, Tencent, Xiaomi) per SELECTION step 2 — no fresh (<24h),
verifiable, significant items surfaced. Shipping **3** stories (at the `min` floor)
rather than padding with stale or unverifiable items. Also re-tried Tier-1 gap-fill
(Microsoft, Meta, Oracle, AMD) — same result.

## Selected stories
1. **Amazon (AMZN US · Tier 1) — roundup, 2 items**

   1.1 **Planned Amazon data center could become the biggest climate polluter in the U.S.**
   - URL: https://techcrunch.com/2026/08/08/planned-amazon-data-center-could-become-the-biggest-climate-polluter-in-the-u-s/
   - Published: Sat, 08 Aug 2026 21:24:02 +0000
   - FreshnessCheck: ✅ · DedupCheck: ✅ (not in last-7-day watchlist set)
   - Verification: Tier 1 — funnel body
   - Summary: Amazon's planned Pecos County, TX AI data center includes an on-site gas plant permitted to emit 33M tons CO2/yr, potentially the largest single U.S. emitter.

   1.2 **Claude Code เพิ่มความสามารถคุยกันเองข้ามเซสชันได้**
   - URL: https://www.blognone.com/node/151324
   - Published: Sat, 08 Aug 2026 10:53:06 +0000
   - FreshnessCheck: ✅ · DedupCheck: ✅
   - Verification: Tier 2 — funnel snippet
   - Summary: Anthropic (Amazon-backed) เพิ่มความสามารถให้ Claude Code คุยข้ามเซสชันได้เอง — matched to Amazon via the "Anthropic" keyword in watchlist.json.

2. **Nvidia (NVDA US · Tier 1) — Firebird Launches CIS Region's Largest AI Factory in Armenia**
   - Publisher: NVIDIA (blogs.nvidia.com) — Primary
   - URL: https://blogs.nvidia.com/blog/firebird-ai-factory-armenia-blackwell-rubin-dsx/
   - Published: Sat, 08 Aug 2026 10:33:57 GMT
   - FreshnessCheck: ✅ · DedupCheck: ✅
   - Verification: Tier 1 — funnel body
   - Summary: Firebird, with NVIDIA/Dell/CoreWeave, opened the CIS region's largest AI factory in Armenia; 70,000+ Rubin/Blackwell GPUs and 300MW planned.

3. **Apple (AAPL US · Tier 1) — Apple says Mac users in China can connect to Alibaba's Qwen AI service**
   - Publisher: Reuters
   - URL: https://www.reuters.com/business/retail-consumer/apple-says-mac-users-china-can-connect-alibabas-qwen-ai-service-2026-08-08/
   - Published: Sat, 08 Aug 2026 12:35:45 GMT
   - FreshnessCheck: ✅ · DedupCheck: ✅
   - Verification: Tier 2 — headline-only (funnel `body_text` extraction was blocked at source and `description` only echoed the headline; the headline itself is a complete, specific factual claim on a Tier-1 trusted domain with an explicit fresh timestamp, so it is used verbatim with nothing added beyond it)
   - Summary: Apple now lets Mac users in China connect directly to Alibaba's Qwen AI service.

## Dropped
- https://news.google.com/rss/articles/...(Alphabet/Hassabis, resolves to theguardian.com) — provenance: could not resolve to a real fetchable URL (WebFetch blocked this run); per engine rule, never cite an unresolved news.google.com redirect. WebSearch surfaced the underlying event but it traces to CNBC/Axios write-ups dated 2026-08-05/06 (>24h, stale write-up) — dropped rather than guess at the Guardian piece's exact URL or added content.
- Alibaba "may start charging for latest AI model" (Reuters, Aug 8) — editorial (rehash): same story already published in the 2026-08-07 watchlist brief (Reuters, Aug 7 dateline).
- Amazon/Tom's Hardware "Gilroy" community-vote story — verification: funnel body_text/description returned only membership-wall/author-bio boilerplate; could not verify substance without WebFetch.
- Amazon/The Verge "worst polluting power plant" — editorial (dup topic): same Pecos County power-plant story as the selected TechCrunch item.
- AMD/Tom's Hardware "DDR5-8800" (CXMT) — verification: same Tom's Hardware boilerplate-extraction issue; also marginal AMD relevance (story is about a Chinese memory maker, AMD only as the reference platform).
- Tesla/The Verge "X replaces revenue-sharing program" — Gate C (no AI/tech relevance): a creator-payments product change, not an AI story.
- Nvidia/The Information "$3B in Blackstone-backed Lancium" — Screening source (paywalled, discovery-only); no open Citation-tier outlet found carrying the same story (only off-allowlist aggregators: Yahoo Finance, Investing.com, Benzinga, etc.) — dropped per the Screening cross-match rule.
- Oracle "Multicloud – What's News" (Oracle blog) — funnel description was headline-only with no substantive content; generic recurring digest post, not a discrete news event.

# Sources — 2026-06-29 (watchlist)

Generated: 2026-06-29 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 watchlist briefs (35+ URLs loaded)
TIERS_USED: 1+2
Source mix: 2 international Tier 1 body (Livemint, TechCrunch ×1) + 1 Tier 2 snippet (Reuters) + 1 Tier 1 body fill from Tier 2 company (TechCrunch)

## Selected stories

1. **Google limits Meta's Gemini access — Backlog $462B (Alphabet · Tier 1)**
   - Publisher: Mint (livemint.com)
   - URL: https://www.livemint.com/technology/tech-news/google-limits-meta-s-use-of-its-gemini-ai-models-11782624880463.html
   - Published: Sun, 28 Jun 2026 05:41:08 GMT (age_h: 17.7h)
   - FreshnessCheck: ✅ within last 24h
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Gate W: ✅ Alphabet (Tier 1) — matched_company confirmed
   - Gate C: ✅ AI/tech — Gemini AI compute limits, enterprise AI infrastructure
   - Gate D: ✅ Significant — $462B backlog, Meta project delays, Google infrastructure constraint
   - Verification: Tier 1 — funnel body (extract_status: ok; body confirms headline, March incident, Meta disruption, Sundar Pichai $462B backlog quote, 24-month clearance target)
   - cluster_size: 15

2. **Tesla FSD under growing scrutiny after fatal Texas crash — NHTSA + NTSB investigations open (Tesla · Tier 1)**
   - Publisher: TechCrunch (techcrunch.com)
   - URL: https://techcrunch.com/2026/06/28/techcrunch-mobility-all-eyes-on-tesla-fsd/
   - Published: Sun, 28 Jun 2026 16:05:00 +0000 (age_h: 7.3h)
   - FreshnessCheck: ✅ within last 24h
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Gate W: ✅ Tesla (Tier 1) — matched_company confirmed
   - Gate C: ✅ AI/tech — Tesla FSD (Full Self-Driving), autonomous driving AI
   - Gate D: ✅ Significant — fatal crash, dual regulatory investigation (NHTSA+NTSB), FSD controversy, settled 2023 case
   - Verification: Tier 1 — funnel body (extract_status: ok; body confirms crash details, Elluswamy quote, NHTSA+NTSB investigation openings, settlement mention)
   - cluster_size: 2

3. **Firmus Technologies (Australia) strikes AI access deal with Nvidia (Nvidia · Tier 1)**
   - Publisher: Reuters (reuters.com)
   - Resolved URL: https://www.reuters.com/world/asia-pacific/australias-firmus-technologies-strikes-ai-access-deal-with-nvidia-2026-06-28/
   - Published: Sun, 28 Jun 2026 14:03:43 GMT (age_h: 9.3h)
   - FreshnessCheck: ✅ within last 24h
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Gate W: ✅ Nvidia (Tier 1) — matched_company confirmed
   - Gate C: ✅ AI/tech — Nvidia AI deal, data center (Indonesia), AI access partnership
   - Gate D: ✅ Significant — new partnership, AI infrastructure expansion in Southeast Asia
   - Verification: Tier 2 — funnel snippet (extract_status: blocked; no body_text; Reuters title + description confirm headline; Bloomberg corroborates with "AI Startup Firmus to Build Indonesia Data Center With Nvidia")
   - cluster_size: 7 (Reuters) + 2 (Bloomberg)

4. **Wall Street: Micron คือ "Nvidia รุ่นถัดไป" — Market Cap แตะ $1.27T (Micron · Tier 2)**
   - Publisher: TechCrunch (techcrunch.com)
   - URL: https://techcrunch.com/2026/06/28/why-wall-street-thinks-us-memory-maker-micron-is-the-next-nvidia/
   - Published: Sun, 28 Jun 2026 15:00:00 +0000 (age_h: 8.4h)
   - FreshnessCheck: ✅ within last 24h
   - DedupCheck: ✅ URL not in last-7-day watchlist set (Reuters/CNBC Micron URLs from 2026-06-26 and 2026-06-25 are different stories/URLs)
   - Gate W: ✅ Micron Technology (Tier 2) — matched_company (system matched as Nvidia but primary subject is Micron)
   - Gate C: ✅ AI/tech — HBM memory chip, AI data center demand, AI infrastructure
   - Gate D: Fill — Tier 2 fill to reach prefer=4; significant market event (market cap milestone, 236% monthly gain)
   - Verification: Tier 1 — funnel body (extract_status: ok; body confirms $1.27T market cap, 236% monthly gain, $1,132/share, HBM demand driver, position vs Meta $1.39T and Tesla $1.42T)
   - cluster_size: 2

## Significance ledger

| Company | Tier | Significant? | Reason | Selected |
|---|---|---|---|---|
| Alphabet | 1 | ✅ Yes | $462B enterprise backlog, Meta project disruption, infrastructure constraint news | ✅ Story 1 |
| Tesla | 1 | ✅ Yes | Fatal crash, NHTSA+NTSB dual investigation, FSD liability escalation | ✅ Story 2 |
| Nvidia | 1 | ✅ Yes | New AI partnership/data center deal, APAC expansion | ✅ Story 3 (Tier 2 verify) |
| Micron | 2 | Fill | Market cap milestone, HBM demand (new angle vs previous coverage) | ✅ Story 4 (Tier 2 company fill) |
| Apple | 1 | Low | Touchscreen MacBook roadmap (Gurman sources, no AI angle in body) | ❌ Dropped |
| Amazon | 1 | Weak | Z.ai/GLM-5.2 story (primary subject not a watchlist company; Amazon tie indirect) | ❌ Dropped |
| Meta Platforms | 1 | — | Mentioned as customer in Story 1 (Alphabet story) | No direct story |
| Microsoft | 1 | — | No qualifying AI/tech story in 24h window | — |
| AMD | 1 | — | No qualifying story (skipped items only; 3D-print story off-topic) | — |
| Oracle | 1 | — | No qualifying story in 24h window | — |

## Tier-descent record
Tier 1 companies yielded 3 strong stories (Alphabet, Tesla, Nvidia). Story 3 (Nvidia) uses Tier 2 verification due to extract_status: blocked, though Nvidia itself is Tier 1. Story 4 fills to prefer=4 using Tier 2 company Micron with a new angle (TechCrunch "next Nvidia" framing vs prior Reuters/CNBC coverage of same event from different dates).

## Dropped
- Reuters Google/Meta Gemini (reuters.com/business/google-limits-metas...): same story as Livemint Story 1; blocked body; Livemint preferred
- Bloomberg Google/Meta Gemini: screening source; same story; redundant
- FT Google caps Meta Gemini: screening source; same story; redundant
- Blognone Google/Meta Gemini (blognone.com/node/151009): same story; used in ainews stream already; note that ainews/watchlist are separate streams so no dedup conflict, but redundant with Livemint selection
- Bloomberg Firmus Indonesia data center: screening source (extract_status: skipped); corroborates Reuters Story 3 but not citable as primary
- Livemint "Buy Nvidia at 2am" (tokenised stocks): off-topic, not AI/tech development — Gate C FAIL
- Engadget Apple touchscreen MacBook: borderline Gate C; no AI angle in body; borderline significance; dropped in favor of 4 stronger stories
- ZDNet Gemini Android Auto: extract_status: skipped; no body; advisory article (how-to), not news development
- Lenovo RAMageddon Tom's Hardware: extract_status: skipped; AMD matched but Lenovo is primary subject; no body; Tier 2 only
- AMD 3D-print Tom's Hardware: off-topic DIY content — Gate C FAIL
- PlayStation UK movies removal: off-topic — Gate C FAIL
- Meta/Facebook meme factories (The Guardian): not AI/tech development — Gate C FAIL
- Brand Inside Instagram Reels: not AI/tech development — Gate C FAIL
- Bloomberg Apple price increases: screening source; extract_status: skipped; same angle covered 2026-06-26 watchlist (Apple price increases — The National)

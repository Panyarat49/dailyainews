# Sources — 2026-06-25 (watchlist)

Generated: 2026-06-25 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 watchlist briefs (Jun 18–24, ~30 URLs loaded — no candidate collisions found)
Source mix: 1 primary (blog.google), 3 citation (CNBC ×2, TechCrunch, CNA)
Universe pre-load: 46 candidates from universe_2026-06-25_watchlist.json (generated_at 2026-06-25T06:25:09.662169+07:00) — WebSearch skipped (≥ 8 candidates after gates)
Tiers used: 1+2 | Story count: 4 slots (Alphabet roundup = 1 slot; Tier 2: Micron; satisfies prefer=4)

## Significance ledger

| Company | Tier | Significant? | Reason | Selected |
|---|---|---|---|---|
| Alibaba | 1 | ✅✅ | Anthropic accuses Alibaba of illicitly extracting Claude capabilities — letter to Congress, cluster_size=6 | yes (slot 1) |
| Alphabet | 1 | ✅✅ (×2) | Gemini 3.5 Flash computer use built-in (model launch) + core Gemini researchers Adler & Pritzel depart for Anthropic (exec/talent change) | yes (roundup, slot 2) |
| Micron | 2 | ✅✅ | Record quarterly earnings: 84.9% gross margin, surpasses Nvidia and Meta, new company record | yes (slot 3) |
| Microsoft | 1 | ✅ | Qualcomm names Microsoft as anchor data center chip customer; $15B forecast by 2029; shares +12% | yes (slot 4) |
| Meta | 1 | near-dup | US govt AI review request — same story as Jun 24 brief (Reuters 2026-06-23); no new development today | no |
| Amazon | 1 | ❌ Gate C | Prime Day deals (aboutamazon.com) — retail commercial content, not AI/tech development | no |
| Apple | 1 | ❌ Gate C | Prime Day deals on Apple products (The Verge) — retail commercial content | no |
| Apple | 1 | ◻ | Apple supplier Lingyi iTech HK IPO (Reuters blocked) — Apple-adjacent story; no body_text | no |
| Nvidia | 1 | ◻ | Mentioned in Micron story incidentally; no standalone Nvidia story in universe today | no |
| TSMC | 2 | ❌ paywall | Tom's Hardware TSMC price hike — membership wall body_text; no usable content | no |

## Tier-descent record
Tier 1 yielded 3 significant slots (Alibaba, Alphabet roundup, Microsoft). Tier 2 descent used to add Micron (slot 3) to reach prefer=4. TIERS_USED: 1+2.

## Selected stories

1. **Alibaba — Anthropic accuses Alibaba of illicitly extracting Claude capabilities**
   - Publisher: CNBC (Citation — best body_text; Reuters original blocked; Bloomberg screening-only)
   - URL: https://www.cnbc.com/video/2026/06/24/anthropic-sends-congress-letter-accusing-alibaba-of-ai-model-illicit-access.html
   - Published: Wed, 24 Jun 2026 20:52:26 GMT (= Jun 25 03:52 Bangkok)
   - FreshnessCheck: ✅ within last 24h via published_raw (age_h 2.5)
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 1 — funnel body (extract_status: ok; CNBC body confirms video report on Anthropic letter to Congress accusing Alibaba of illicitly accessing AI models; Greg Brockman quote on OpenAI chip also confirms same timeframe; Reuters resolved_url https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/ further confirms; cluster_size=6 with Bloomberg, TechCrunch coverage)
   - Summary: Anthropic sent a letter to Congress accusing Alibaba of illicitly extracting Claude AI model capabilities. The Reuters/CNBC/Bloomberg cluster confirms this as a major IP dispute with potential legislative implications.

2a. **Alphabet — Gemini 3.5 Flash built-in computer use**
   - Publisher: blog.google (Primary)
   - URL: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/
   - Published: Wed, 24 Jun 2026 16:27:46 GMT (= Jun 24 23:27 Bangkok)
   - FreshnessCheck: ✅ within last 24h via published_raw (age_h 6.9)
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 1 — funnel body (extract_status: ok; body confirms computer use is now a built-in tool in Gemini 3.5 Flash, previously only standalone 2.5 model, now integrated natively in main Flash model; browser/mobile/desktop agents; Gemini Enterprise Agent Platform; prompt injection mitigations; Mateo Quiros PM quote)
   - Summary: Computer use is now built-in to Gemini 3.5 Flash, enabling developers to build agents that interact across browser, mobile, and desktop environments using a fast, cost-efficient model.

2b. **Alphabet — AI researchers continue to leave Google for rivals**
   - Publisher: TechCrunch (Citation)
   - URL: https://techcrunch.com/2026/06/24/ai-researchers-continue-to-leave-google-for-its-rivals/
   - Published: Wed, 24 Jun 2026 21:42:07 +0000 (= Jun 25 04:42 Bangkok)
   - FreshnessCheck: ✅ within last 24h via published_raw (age_h 1.7)
   - DedupCheck: ✅ URL not in last-7-day watchlist set (Jun 21 brief used different URL https://techcrunch.com/2026/06/20/nobel-laureate-john-jumper-is-leaving-deepmind-for-rival-anthropic/ for Jumper; this is a new article about Adler + Pritzel)
   - Verification: Tier 1 — funnel body (extract_status: ok; body confirms Jonas Adler and Alexander Pritzel leaving Google for Anthropic; both played key roles in Gemini; Shazeer to OpenAI; Jumper to Anthropic; IPO equity draw context)
   - Corroboration: CNBC (body_text = video report confirming Alphabet shares slide + Gemini product timeline concerns)
   - Summary: Core Gemini researchers Jonas Adler and Alexander Pritzel are leaving Google DeepMind for Anthropic, extending a talent exodus that also took Noam Shazeer (OpenAI) and John Jumper (Anthropic) in the preceding week.

3. **Micron — Tech's new margin king**
   - Publisher: CNBC (Citation)
   - URL: https://www.cnbc.com/2026/06/24/micron-is-techs-margin-king-memory-crisis-pushes-it-past-nvidia-meta.html
   - Published: Wed, 24 Jun 2026 22:32:56 GMT (= Jun 25 05:32 Bangkok)
   - FreshnessCheck: ✅ within last 24h via published_raw (age_h 0.9 — near-breaking)
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 1 — funnel body (extract_status: ok; body confirms 84.9% gross margin, up from 39% a year ago; beats Nvidia 75% and Meta 81.9%; new company record; CFO Mark Murphy quote "Fiscal Q3 gross margin more than doubled from a year ago and was a new company record"; memory crisis + AI demand context)
   - Summary: Micron reported a record 84.9% gross margin, surpassing Nvidia (75%) and Meta (81.9%). The HBM-driven earnings beat reflects sustained AI infrastructure demand.

4. **Microsoft — Qualcomm names Microsoft as data center chip customer**
   - Publisher: CNA (Citation)
   - URL: https://www.channelnewsasia.com/business/qualcomm-forecasts-15-billion-data-center-chip-sales-2029-shares-soar-6207736
   - Published: Wed, 24 Jun 2026 19:57:57 GMT (= Jun 25 02:57 Bangkok)
   - FreshnessCheck: ✅ within last 24h via published_raw (age_h 3.4)
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 1 — funnel body (extract_status: ok; body confirms Qualcomm forecasts $15B data center sales by 2029; $5B for FY2027; $1B from new custom-chip customers; Microsoft and Meta named as customers; CFO Akash Palkhiwala quote; shares +12% after-hours; $40B revenue from chips outside smartphone by 2029; Bank of America analysts cited)
   - Summary: Qualcomm named Microsoft (and Meta) as customers for its new data center AI chips at an investor presentation, forecasting $15B in data center revenue by 2029. Shares surged over 12%.

## Dropped
- Reuters (resolved_url: https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/) — blocked (extract_status: blocked); used CNBC as primary cite for Story 1
- Bloomberg (https://www.bloomberg.com/news/articles/2026-06-24/anthropic-accuses-alibaba-of-illicitly-accessing-its-ai-models) — source_role: screening; body_text = paywall block; not citable per trusted-sources.md screening policy
- aboutamazon.com Prime Day — Gate C fail (retail, not AI/tech development)
- theverge.com Prime Day Apple deals — Gate C fail (retail)
- tomshardware.com TSMC price hike — membership wall body_text; no usable content (same as ainews drop)
- engadget.com US govt urging Meta AI review — near-duplicate of Jun 24 watchlist story (same event, no new development); dropped despite passing Gate B (different URL)
- engadget.com Google Home Speaker review — lower significance (product review vs. model launch/partnership); no body_text
- reuters.com Apple supplier Lingyi iTech IPO — Reuters blocked; Apple-adjacent not Apple primary; Gate W marginal

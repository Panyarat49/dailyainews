# Sources — 2026-07-02 (watchlist)

Generated: 2026-07-02 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED (control probe on https://example.com → HTTP 403)
Verification mode: funnel + search (3 picks verified from funnel body_text; 2 picks — Amazon, Palantir — had only headline-repeat funnel snippets, so verified via live WebSearch that surfaced the real citeable URL + substantive detail)
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok) — all 5 selected stories are same-day (Jul 1, 2026)
Dedup against: last 7 watchlist briefs (2026-06-25 → 2026-07-01; 32 URLs loaded, none overlapping today's picks)
Universe pre-load: 40 candidates from universe_2026-07-02_watchlist.json (generated_at 2026-07-02T06:28:27+07:00) — no Tier-2 candidates present in the pool at all; Tier-1 pool alone yielded only 3 citeable stories (Meta, Alphabet, Microsoft), so 2 slots were filled via targeted gap-fill WebSearch (Amazon Tier 1, Palantir Tier 2) per SEARCH_STRATEGY step 3–4
Tiers used: 1+2 | Story count: 5 slots (target 4–5, floor 3 — met)

## Significance ledger
| Company | Tier | Significant? | Reason | Selected |
|---|---|---|---|---|
| Meta Platforms | 1 | ✅✅✅ | New cloud-infrastructure business reselling excess AI compute/models to compete with AWS/GCP/Azure — cluster_size 3+ across Reuters/Bloomberg/CNBC/TechCrunch/CNA, shares reportedly surged on the report | yes (slot 1) |
| Alphabet | 1 | ✅✅ | Gemini Spark (agentic assistant) launches on Mac with real-time tracking + new app integrations — cluster_size 2 | yes (slot 2) |
| Amazon | 1 | ✅✅ | Claude Fable 5 relaunched on Amazon Bedrock with strengthened safety classifiers, directly tied to today's US export-control reversal | yes (slot 3) |
| Microsoft | 1 | ◻ fill | TeamDynamix (Microsoft Frontier partner) cuts IT workloads up to 70% with Azure AI — genuine primary-source case study but modest significance; used as backfill to reach STORY_COUNT | yes (slot 4) |
| Palantir | 2 | ✅ | CEO Alex Karp publicly criticizes OpenAI/Anthropic token-based pricing as "completely wrong," ties to Palantir-Nvidia Nemotron government deal — well-corroborated (CNBC, Yahoo, IBTimes, TipRanks); stock reportedly rallied 9% | yes (slot 5, Tier-2 top-up) |
| Nvidia | 1 | ◻ | Only candidate ("NVIDIA and Partners Build in America, for America") turned out to be a rehash of an Oct 2025 investor press release recirculated in the RSS feed, not a genuine new write-up — dropped under Gate A (stale rehash) | no |
| Oracle | 1 | ◻ | All 3 blogs.oracle.com candidates had body_text = site error page ("technical difficulty"); "Oracle outlines all the ways it could lose the farm" (Register) had only a headline-repeat snippet, no substantive content available | no |
| Alibaba | 1 | ◻ | Only in-window item was a $600M US drug-sales-probe settlement — not AI/tech relevant (Gate C fail); no fresh Qwen news found in-window via gap-fill search | no |
| Apple | 1 | ◻ | Candidates were MacBook Pro redesign rumors and a Hide My Email bug — neither is an AI-relevant development (Gate C fail) | no |
| Tesla | 1 | ◻ | Only candidate was the SpaceX AI-phone-prototype denial story — concerns SpaceX/xAI, not Tesla itself; dropped as off-target for this company slot (also carried in today's general brief) | no |
| AMD | 1 | ◻ | Gap-fill search surfaced only stock-price/rally commentary and stale CES 2026 (Jan) product recaps — no fresh AMD-specific news in-window | no |

## Tier-descent record
Tier 1 pool (via funnel) yielded 3 solid, well-evidenced stories (Meta, Alphabet, Microsoft). No Tier-2 candidates existed in the pre-loaded universe JSON at all. Per SEARCH_STRATEGY step 3 (gap-fill), ran targeted WebSearches for the remaining Tier-1 companies (Nvidia, Amazon, Apple, AMD, Alibaba, Tesla) — only Amazon produced a genuine fresh, citeable, on-topic story (Claude Fable 5 on Bedrock). To reach the 4–5 target, descended to Tier 2 per step 4 and searched Palantir specifically (surfaced via the funnel's mis-tagged "Amazon" candidate #31, re-verified as a genuine Palantir story via WebSearch) — confirmed fresh and well-corroborated. Final: 4 Tier-1 + 1 Tier-2 = 5 slots.

## Selected stories
1. **Meta Platforms — building a cloud business to resell excess AI compute**
   - Company · Ticker · Tier: Meta Platforms · META US · Tier 1
   - Publisher: TechCrunch
   - URL: https://techcrunch.com/2026/07/01/meta-like-spacex-looks-to-turn-excess-ai-compute-into-cash/
   - Published: Jul 1, 2026, 13:43 UTC
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 1 — funnel body (full body_text, extract_status=ok; cluster_size=3, corroborated by Reuters/Bloomberg, CNBC, CNA, Blognone)
   - Summary: Meta is developing a cloud-infrastructure business to sell its excess AI compute and models, competing directly with AWS, Google Cloud, and Azure; shares reportedly surged on the report.

2. **Alphabet — Gemini Spark, Google's agentic assistant, launches on Mac**
   - Company · Ticker · Tier: Alphabet · GOOGL US · Tier 1
   - Publisher: TechCrunch
   - URL: https://techcrunch.com/2026/07/01/gemini-spark-googles-agentic-assistant-is-now-available-on-mac/
   - Published: Jul 1, 2026, 14:20 UTC
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 1 — funnel body (full body_text, extract_status=ok; cluster_size=2)
   - Summary: Gemini Spark, Google's 24/7 agentic assistant, is now available on Mac via the Gemini desktop app, adding real-time topic tracking and integrations with Google Tasks and Keep.

3. **Amazon — Claude Fable 5 relaunched on Amazon Bedrock with stronger guardrails**
   - Company · Ticker · Tier: Amazon · AMZN US · Tier 1
   - Publisher: About Amazon (Primary)
   - URL: https://www.aboutamazon.com/news/aws/claude-fable-5-anthropic-available-amazon-bedrock
   - Published: Jul 1, 2026 (per aboutamazon.com; corroborated by AWS's own "what's new" post and AWS News Blog)
   - FreshnessCheck: ✅ within WINDOW — dated Jul 1, 2026, matches today's US export-control-reversal story
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 2 — WebSearch snippet (funnel snippet was headline-only; live WebSearch surfaced the primary aboutamazon.com URL plus corroborating detail from AWS's own blog and docs)
   - Summary: Anthropic's Claude Fable 5 is available again on Amazon Bedrock as of July 1, with strengthened safety classifiers that reroute high-risk queries to Claude Opus 4.8; Anthropic says the classifiers trigger in fewer than 5% of sessions.

4. **Microsoft — TeamDynamix cuts IT workloads up to 70% with Azure AI**
   - Company · Ticker · Tier: Microsoft · MSFT US · Tier 1
   - Publisher: Microsoft (news.microsoft.com, Primary)
   - URL: https://news.microsoft.com (candidate resolved via Google News redirect; original Microsoft customer-story post)
   - Published: ~Jul 1–2, 2026 (age_h 4.2 at funnel generation)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 1 — funnel body (734-char body_text, extract_status=ok, confirms TeamDynamix/Azure AI details)
   - Summary: TeamDynamix, a Microsoft Frontier partner, used Azure data and AI to add agent-led automation to its ITSM platform, cutting customers' routine IT workloads by up to 70%.

5. **Palantir — CEO Karp criticizes OpenAI/Anthropic's token pricing model**
   - Company · Ticker · Tier: Palantir · PLTR US · Tier 2
   - Publisher: CNBC
   - URL: https://www.cnbc.com/2026/07/01/palantir-karp-open-ai-anthropic-tokens.html
   - Published: Jul 1, 2026
   - FreshnessCheck: ✅ within WINDOW (dated Jul 1, 2026)
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 2 — WebSearch snippet (funnel candidate had only a headline-repeat snippet and was mis-tagged "Amazon"; live WebSearch located and confirmed the real CNBC article plus corroboration from Yahoo Finance, IBTimes, TipRanks)
   - Summary: Palantir CEO Alex Karp told CNBC that OpenAI and Anthropic's token-based pricing has "gone completely wrong," arguing enterprises want outcome-based pricing over per-token billing; the remarks follow a Palantir-Nvidia deal bringing Nvidia's open Nemotron models to US government agencies, and Palantir shares reportedly rallied on the comments.

## Dropped
- https://www.theregister.com/ai-and-ml/2026/07/01/... (Alibaba — $600M US drug-sales-probe settlement) — Gate C fail: not AI/tech relevant
- blogs.nvidia.com "NVIDIA and Partners Build in America, for America" — Gate A fail: content matches an Oct 2025 investor press release, a stale rehash recirculated in the RSS feed, not a genuine new write-up
- 3× blogs.oracle.com candidates (Agentic AI Lifecycle, Model Distillation Pipeline, Exadata Cloud) — body_text was a site error page ("technical difficulty"); no citeable content
- theregister.com "Oracle outlines all the ways it could lose the farm it bet on AI" — only a headline-repeat snippet available, insufficient to summarize without fabrication
- theverge.com/engadget MacBook Pro redesign rumor, Hide My Email bug — Gate C fail: not AI-relevant Apple stories
- theverge.com SpaceX AI phone prototype (Musk denial) — concerns SpaceX/xAI, not Tesla; off-target for the Tesla watchlist slot (covered in today's general brief instead)
- Duplicate Meta-cloud-business coverage (Reuters/Bloomberg via Google News redirect, CNBC, CNA, Blognone, Livemint, Engadget) — same story as Selected #1; not double-counted
- Duplicate Gemini Spark coverage (2nd TechCrunch RSS entry) — same story as Selected #2; not double-counted

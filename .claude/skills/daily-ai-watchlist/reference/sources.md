# Sources — 2026-08-13 (watchlist)

Generated: 2026-08-13 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel   # verified from RSS-funnel body_text (items_enriched=11>0) + funnel snippets
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 watchlist briefs (2026-08-06 → 2026-08-12; 30 URLs loaded, 0 overlap)
Tiers used: 1 (Tier 2 not called — no Tier-2 company had a candidate in today's funnel pool; WebSearch gap-fill for AMD/Tesla/Apple/Alibaba/Microsoft found only stale (>24h) coverage, so none qualified)

## Significance ledger
| Company | Tier | Significant? | Reason | Selected |
|---|---|---|---|---|
| Meta Platforms | 1 | Yes | Legal/regulatory action (criminal complaint re: AI glasses) + AI product launch (Creator Studio) — 2 qualifying items → roundup | ✅ (roundup, 2 items) |
| Alphabet | 1 | Yes | Major product launch (Pixel 11 line) with AI as the headline feature | ✅ |
| Nvidia | 1 | Yes | New enterprise AI infra product (NeMo Switchyard router) cutting inference cost | ✅ |
| Amazon | 1 | Yes (fill) | AI-training data policy change affecting Twitch creators — genuinely AI/tech-relevant, less major than the top 3 | ✅ |
| Oracle | 1 | Undetermined | 4 candidates in pool, but every blogs.oracle.com body_text returned only the site's generic "technical difficulty" error page, and RSS descriptions carried no substantive content; WebFetch also blocked (EGRESS_BLOCKED on control probe). Could not verify — dropped, not scored on merit. | ❌ |
| Microsoft | 1 | Undetermined | Only candidate (MindTopo AI spatial-reasoning post) had no body_text and a title-only description; unverifiable | ❌ |
| Apple | 1 | No | Only candidate was Pixel-11-vs-Apple commentary (comparison piece, not an Apple-originated development) | ❌ |
| Tesla, AMD, Alibaba | 1 | No | No candidate in today's funnel pool; WebSearch gap-fill surfaced only >24h-old coverage | ❌ |
| Tier 2 (all 10) | 2 | N/A | Zero Tier-2 company candidates in today's funnel pool; not needed since Tier 1 filled to `prefer` (4) | ❌ |

## Tier-descent record
Tier 1 alone reached 4 stories (= `prefer`). Tier 2 was not invoked (`tier_descent = top-up-to-target` only triggers below `prefer`). Stopped at 4 rather than force a 5th from unverifiable Oracle/Microsoft candidates or stale (>24h) WebSearch results — Gate A / verification held firm over hitting `max`.

## Selected stories
1. **Meta Platforms (META US · Tier 1) — roundup, 2 updates**
   1.1
   - URL: https://www.channelnewsasia.com/business/german-advocacy-group-lodges-criminal-complaint-over-meta-ai-glasses-6314716 (resolved from Google News redirect; CNA republishing Reuters)
   - Published: Wed, 12 Aug 2026 10:38 GMT (~13h old)
   - FreshnessCheck: ✅ within WINDOW via funnel body_text
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: A German advocacy group (HateAid) filed a criminal complaint against Meta over its AI smart glasses, alleging the discreet on-face cameras breach German privacy/data-protection law.
   1.2
   - URL: https://techcrunch.com/2026/08/12/facebook-officially-rolls-out-its-standalone-creator-studio-app-with-ai-tools-for-creators/
   - Published: Wed, 12 Aug 2026 15:56 GMT (~7.7h old)
   - FreshnessCheck: ✅ within WINDOW via funnel body_text
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Facebook rolled out a stand-alone Creator Studio app with an AI creator assistant that gives personalized growth tips based on content style, performance, and audience engagement.

2. **Alphabet (GOOGL US · Tier 1) — Google unveils Pixel 11 line with AI as the centerpiece — [AP News](https://apnews.com/article/google-pixel-11-android-3bbad7afc4d25e15527477123415e50a)**
   - URL: https://apnews.com/article/google-pixel-11-android-3bbad7afc4d25e15527477123415e50a (resolved from Google News redirect)
   - Published: Wed, 12 Aug 2026 14:00 GMT (~9.6h old)
   - FreshnessCheck: ✅ within WINDOW via funnel body_text
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Google unveiled its Pixel 11 lineup (phones, Pixel Watch 5, earbuds) with slimmer cameras and AI features aimed at completing tasks in fewer taps/steps.

3. **Nvidia (NVDA US · Tier 1) — NeMo Switchyard model-routing platform — [The Register](https://www.theregister.com/ai-and-ml/2026/08/12/nvidias-latest-solution-for-soaring-enterprise-costs-nemo-switchyard-software-router/5286911)**
   - Published: Wed, 12 Aug 2026 21:00:10 +0200 (~4.6h old)
   - FreshnessCheck: ✅ within WINDOW via funnel body_text
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Nvidia launched NeMo Switchyard, a routing layer that sends inference requests to different models to optimize cost/latency/quality, claiming up to 74% lower job-completion cost vs. Claude Opus 4.8 alone (~6-point accuracy tradeoff). (Note: also covered in today's general brief — legitimate per-stream story, no cross-stream dedup required.)

4. **Amazon (AMZN US · Tier 1) — Twitch will train Amazon AI on streamer content by default, adds opt-out — [TechCrunch](https://techcrunch.com/2026/08/12/amazon-will-train-on-twitch-streamers-content-by-default-unless-they-opt-out/)**
   - Published: Wed, 12 Aug 2026 20:10:40 GMT (~3.5h old)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet (TechCrunch quote from Twitch CPO Mike Minton + The Verge's snippet on what content the opt-out covers; no body_text on any outlet, WebFetch blocked)
   - Summary: Amazon's Twitch will use streamers' content (streams, VODs, clips, chat, channel text/images) to train its generative AI models by default; streamers can opt out. Twitch CPO Mike Minton: "If this was opt-in, nobody would opt in."

## Dropped
- https://news.google.com/...(Announcing the Private Large Language Model Service, Oracle) — Gate: funnel body_text was an Oracle site-error page ("experiencing technical difficulty"); description was headline-only; WebFetch blocked. Unverifiable.
- https://news.google.com/...(Getting Started with Private LLM Service – Part 1, Oracle) — same Gate as above.
- https://news.google.com/...(Oracle APEX AI Application Generator, Oracle) — same Gate as above (also site-error page).
- https://news.google.com/...(Oracle Exadata Database Service on Oracle AI Database@AWS) — same Gate as above; also mistagged by the funnel as "Amazon" (it's an Oracle product announcement) — dropped on verification grounds regardless.
- https://news.google.com/...(MindTopo puts AI's spatial reasoning to the test, Microsoft) — Gate: no body_text, description was title-only; WebFetch blocked. Unverifiable.
- https://www.cnbc.com/... (Pixel 11 offers an early look at the AI experience Apple is chasing) — Gate C: this is Pixel/Google-centric commentary about Apple, not an Apple-originated AI development; and duplicates the Alphabet Pixel-11 story already selected (#2).
- https://news.google.com/...(EXCLUSIVE: Inside the Google executive moves..., Reuters) — Gate: extract_status skipped, no body_text or substantive description; WebFetch blocked. Also thematically close to the 2026-08-06 brief's DeepMind reshuffle story. Unverifiable + likely stale angle.
- Multiple lower-score Pixel/Twitch/Nvidia duplicate-URL entries (Google News redirects of the same story already selected) — same story, not double-counted.
- Nvidia RTX PRO 6000 price story, CoreWeave GPU-profit story, "Sovereign AI" sponsored piece, Norway wealth-fund gain story — extract_status skipped, no usable body/description; not selected (below the top-4 cut and unverifiable content, not merely lower score).
- AMD, Tesla, Alibaba (Tier 1) — no candidate in today's funnel pool; WebSearch gap-fill (`AMD AI chip news`, `Alibaba Qwen AI news`, `Tesla OR AMD OR Apple OR Microsoft OR Alibaba AI news today`) surfaced only articles from early August or earlier — Gate A (>24h) — dropped.

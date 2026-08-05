# Sources — 2026-08-05 (ainews)

Generated: 2026-08-05 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED (control probe to https://example.com failed in this Claude session; GitHub Actions funnel fetched full article bodies for the enriched picks — 11/40 candidates had `body_text`, `extract_status: ok`)
Verification mode: funnel (all 5 selected stories verified from funnel `body_text` — Tier 1 — funnel body)
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok); all 5 selected stories are same-day write-ups (age_h 2.0–4.5h)
Dedup against: last 7 ainews briefs (2026-07-29, 2026-07-30, 2026-07-31, 2026-08-03, 2026-08-04 — 08-01/08-02 missing/not run; 25 URLs loaded)
Source mix: TechCrunch ×2, The Verge ×2, Engadget ×1 (no Thai-language candidate reached Tier 1 today — the only Thai items in the universe JSON, e.g. bangkokbiznews.com Malaysia-semiconductor piece, had `extract_status: skipped`, i.e. Tier-2-only; deprioritized in favor of 5 Tier-1-verified, more globally material stories)
Universe pre-load: 40 candidates from RSS funnel (generated_at: 2026-08-05T07:00:24+07:00, ≤ 4h before NOW) → START_POOL used, WebSearch skipped (≥8 candidates after gates)

## Selected stories
1. **Anthropic signs $10B deal with AI cloud startup Volta**
   - TechCrunch
   - URL: https://techcrunch.com/2026/08/04/anthropic-signs-10-billion-deal-with-ai-cloud-startup-volta/
   - Published: Tue, 04 Aug 2026 19:48:40 +0000 (age_h 4.2)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Anthropic signed a $10B, six-year cloud compute deal with startup Volta (partnered with crypto-miner Bitdeer) for a 133MW Nvidia Vera Rubin data center in Norway, part of Anthropic's ongoing compute-expansion spree (also SpaceX, Amazon).

2. **AMD's data center business is booming while gaming takes a backseat**
   - The Verge
   - URL: https://www.theverge.com/tech/975381/amd-q2-2026-earnings-ai-gaming-ryzen
   - Published: 2026-08-04T16:57:49-04:00 (age_h 3.0)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: AMD's Q2 2026 data center revenue more than doubled YoY to $6.7B (up from $3.2B a year ago) on AI demand; CEO Lisa Su guided for data center revenue to again more than double in 2027; gaming revenue fell 31% to $779M on price hikes/component shortages.

3. **SpaceX made more revenue as an AI company than a space company**
   - The Verge
   - URL: https://www.theverge.com/science/975335/spacex-made-more-money-as-a-neocloud
   - Published: 2026-08-04T16:47:55-04:00 (age_h 3.2)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: SpaceX's AI-compute division revenue tripled YoY to $2.6B (from deals with Anthropic and Google), while still losing $1.5B this quarter; capex hit $18B+ as SpaceX competes with neoclouds like CoreWeave.

4. **Perplexity has successfully overturned Amazon's injunction on its AI shopping bot**
   - Engadget
   - URL: https://www.engadget.com/2230471/perplexity-has-successfully-overturned-amazon-injunction-on-its-ai-shopping-bot/
   - Published: Tue, 04 Aug 2026 21:58:34 +0000 (age_h 2.0)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: The Ninth Circuit overturned an injunction that had barred Perplexity's Comet AI browser from accessing Amazon, ruling Amazon's CFAA claim doesn't hold since it's the user, not Perplexity, "accessing" Amazon's servers; Amazon says it disagrees with the ruling.

5. **Nvidia doesn't mess around: a week after open AI industry group formed, it's already showing progress**
   - TechCrunch
   - URL: https://techcrunch.com/2026/08/04/nvidia-doesnt-mess-around-a-week-after-open-ai-industry-group-formed-its-already-showing-progress/
   - Published: Tue, 04 Aug 2026 19:28:49 +0000 (age_h 4.5)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: A week after Nvidia-led Open Secure AI Alliance (OSAA, 120+ members incl. Hugging Face) formed, its SAFE working group already published draft proposals (managed by the Linux Foundation) for confidential incident reporting and blame-free analysis of AI cybersecurity incidents, following the OpenAI-model-hacks-Hugging-Face episode.

## Dropped
- https://news.google.com/rss/articles/... (Anthropic names global affairs chief, resolves to reuters.com) — not dropped for gate failure; deprioritized (lower materiality: personnel/policy hire) vs. the 5 selected; extract_status blocked (would need Tier 2 only)
- https://www.theregister.com/security/2026/08/04/this-one-time-at-hacker-summer-camp/5282999 — deprioritized: conference-preview feature, not a discrete news event
- https://www.tomshardware.com/... (AMD doubles data center revenue) — duplicate of selected story 2 (same AMD Q2 earnings); The Verge write-up selected instead
- All remaining `extract_status: skipped` candidates (score < 4.1, incl. Thai bangkokbiznews.com/techsauce.co/thestandard.co items) — deprioritized in favor of higher-scored Tier-1-verified picks; none failed a hard gate, simply not selected within the 5-story cap

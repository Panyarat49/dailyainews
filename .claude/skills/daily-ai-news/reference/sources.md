# Sources — 2026-08-13 (ainews)

Generated: 2026-08-13 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel   # verified from RSS-funnel body_text (items_enriched=12>0) + one funnel snippet
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 ainews briefs (2026-08-06 → 2026-08-12; 35 URLs loaded, 0 overlap)
Source mix: 4 international (venturebeat.com ×2, theregister.com ×2, techcrunch.com ×2) — no Thai-language source cleared the significance/verification bar today; best Thai candidate (blognone, Gemini 1B MAU) duplicates a story already run 2026-08-12.

## Selected stories
1. **SpaceXAI (xAI) เปิดตัว Grok 4.6 แซงหน้า Kimi K3 เทียบชั้น GPT-5.6 Sol**
   - Publisher: VentureBeat
   - URL: https://venturebeat.com/technology/spacexai-debuts-grok-4-6-overtaking-kimi-k3s-performance-and-matching-gpt-5-6-sol-for-worlds-third-best-on-artificial-analysis
   - Published: Wed, 12 Aug 2026 17:26:58 GMT (~6.2h old)
   - FreshnessCheck: ✅ within WINDOW via funnel body_text + published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: xAI (now SpaceXAI) released Grok 4.6, scoring 61 on Artificial Analysis Intelligence Index — ahead of Moonshot's Kimi K3, tied with GPT-5.6 Sol Max, still behind Anthropic's Claude Opus 5/Fable 5 — while keeping API pricing at $2/$6 per million tokens in/out.

2. **จีนต้องสงสัยใช้ AI โจมตีไซเบอร์แบบอัตโนมัติเต็มรูปแบบครั้งแรก เจาะหน่วยงานนิวเคลียร์ไต้หวัน**
   - Publisher: The Register
   - URL: https://www.theregister.com/security/2026/08/12/near-autonomous-ai-agents-attack-taiwans-nuclear-safety-agency/5287055
   - Published: Wed, 12 Aug 2026 23:45:16 +0200 (~1.9h old)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet (substantive RSS description; corroborated by a same-day Tom's Hardware write-up on the same incident, cluster confirms)
   - Summary: Suspected China-linked operatives used publicly available AI tools to run a "near-autonomous" cyberattack that compromised Taiwanese government systems, then spread to the nuclear safety agency, supply-chain vendors, and at least seven energy companies.

3. **Anthropic เริ่มใส่ลายน้ำดิจิทัลในผลงาน Claude ตามกฎ EU AI Act — ผู้ใช้บางส่วนไม่พอใจ**
   - Publisher: TechCrunch
   - URL: https://techcrunch.com/2026/08/12/some-claude-users-are-mad-that-anthropics-new-watermarks-will-catch-them-cheating-at-their-jobs-classes/
   - Published: Wed, 12 Aug 2026 22:26:37 +0000 (~1.2h old)
   - FreshnessCheck: ✅ within WINDOW via funnel body_text
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Anthropic began watermarking Claude's text/image outputs with a hidden statistical pattern to comply with the EU AI Act's Transparency Code; the move is drawing backlash from users worried it will expose AI-assisted work at school or their jobs.

4. **Nvidia เปิดตัว NeMo Switchyard เราเตอร์สลับโมเดล AI ลดต้นทุนองค์กร**
   - Publisher: The Register
   - URL: https://www.theregister.com/ai-and-ml/2026/08/12/nvidias-latest-solution-for-soaring-enterprise-costs-nemo-switchyard-software-router/5286911
   - Published: Wed, 12 Aug 2026 21:00:10 +0200 (~4.6h old)
   - FreshnessCheck: ✅ within WINDOW via funnel body_text
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Nvidia unveiled NeMo Switchyard, a proxy/router (alongside its new Nemotron 3.5-30B-A3B-Lightning open-weight model) that dynamically routes inference requests across models by cost/latency/quality — claiming up to 74% lower job-completion cost vs. Claude Opus 4.8 alone, with roughly a 6-point accuracy tradeoff.

5. **นักวิจัย AI ระดับตำนาน 3 คนออกโรงหนุน "โอเพนซอร์ส" ท่ามกลางกระแสกังวลด้านความปลอดภัย AI**
   - Publisher: TechCrunch
   - URL: https://techcrunch.com/2026/08/12/as-ai-safety-concerns-mount-three-pioneers-make-the-case-for-staying-open/
   - Published: Wed, 12 Aug 2026 17:51:00 +0000 (~5.8h old)
   - FreshnessCheck: ✅ within WINDOW via funnel body_text
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: At the Ai4 conference, Geoffrey Hinton, Fei-Fei Li, and Andrew Ng argued for keeping frontier AI open-weight despite mounting safety concerns, warning that closed control by a few major labs risks slowing innovation and creating AI "gatekeepers."

## Dropped
- https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-will-begin-digitally-watermarking-marking-ai-generated-text-and-images-anthropic-details-how-itll-comply-with-the-eus-artificial-intelligence-act — superseded: same story covered via TechCrunch (#3) which had usable Tier-1 body_text; Tom's Hardware's funnel body_text was paywall/membership boilerplate, not article content.
- https://news.google.com/rss/articles/...(Oracle Private LLM Service) — Gate: funnel body_text returned an Oracle site-error page ("experiencing technical difficulty"), not the article; could not verify content, WebFetch blocked (EGRESS_BLOCKED on control probe) so no live fallback. Dropped for unverifiable content.
- https://www.blognone.com/node/151352 (Gemini 1B MAU) — Editorial dedup: same underlying milestone already reported via The Verge in the 2026-08-12 brief; this write-up adds no new development.
- https://www.engadget.com/2235919/claude-cowork-can-now-run-in-a-chrome-sidebar/ — Not selected: extract_status skipped, no body/description strong enough for Tier 2; lower priority vs. selected set.
- Numerous lower-score candidates (CoreWeave earnings, Cognition funding talks, Twitch/Amazon AI opt-out, Pixel 11 comparison, etc.) — not selected; below the top-5 cut after significance ranking, no gate failure.

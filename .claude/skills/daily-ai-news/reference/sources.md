# Sources — 2026-07-02 (ainews)

Generated: 2026-07-02 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED (control probe on https://example.com → HTTP 403)
Verification mode: funnel (10/40 candidates enriched with full body_text by the GitHub Actions funnel; picks without a usable body verified via funnel RSS snippet + published_raw)
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok) — all 5 selected stories are same-day (≤ 22h)
Dedup against: last 7 ainews briefs (2026-06-25 → 2026-07-01; 36 URLs loaded, none overlapping today's picks)
Universe pre-load: 40 candidates from universe_2026-07-02_ainews.json (generated_at 2026-07-02T06:27:38+07:00) — WebSearch skipped (≥ 8 candidates after gates)
Source mix: TechCrunch ×3, The Register, The Verge — all Citation-tier open press; no Thai-language pick reached the top 5 by significance this run (Techsauce/Blognone covered the same Fable 5 story but with lower corroboration than the TechCrunch original — see Dropped)

## Selected stories
1. **Trump drops restrictions on Anthropic's Mythos and Fable models (Claude Fable 5 restored globally)**
   - Publisher: TechCrunch
   - URL: https://techcrunch.com/2026/06/30/trump-drops-restrictions-on-anthropics-mythos-and-fable-models/
   - Published: Jul 1, 2026, 02:16 UTC (~22h before run)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (full body_text, extract_status=ok; cluster_size=3, corroborated by VentureBeat, Tom's Hardware, Techsauce, Blognone)
   - Summary: US Commerce Dept withdrew the June 12 export-control order on Anthropic's Mythos/Fable models after Anthropic agreed to proactively detect/address security risks and keep the government informed of malicious activity; Anthropic restored global access starting July 1.

2. **Red teamers turned Claude Desktop into a "double agent" to gain full RCE**
   - Publisher: The Register
   - URL: https://www.theregister.com/security/2026/07/01/red-teamers-turned-claude-desktop-into-a-double-agent-to-do-their-evil-bidding/5264692
   - Published: Jul 1, 2026, 19:00 +0200 (~6.5h before run)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (full body_text, extract_status=ok)
   - Summary: Pentera Labs red-teamers compromised a developer's Claude Desktop agent via a hijacked email-aggregator inbox and escalated it to full remote code execution on the victim's machine, demonstrating how a trusted AI assistant can be turned into an attacker's proxy.

3. **Elon Musk denies WSJ report of a SpaceX AI phone prototype**
   - Publisher: The Verge
   - URL: https://www.theverge.com/science/960442/spacex-phone-prototype-elon-musk
   - Published: Jul 1, 2026, 20:10 UTC (~3.3h before run)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (full body_text, extract_status=ok; corroborated by a separate Engadget write-up)
   - Summary: WSJ reported SpaceX showed investors a slimmer-than-iPhone "handset-like prototype" running Snapdragon hardware and an xAI-powered OS ahead of its June IPO; Musk called the report "utterly false."

4. **Meta building a cloud business to resell excess AI compute**
   - Publisher: TechCrunch
   - URL: https://techcrunch.com/2026/07/01/meta-like-spacex-looks-to-turn-excess-ai-compute-into-cash/
   - Published: Jul 1, 2026, 13:43 UTC (~9.7h before run)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet (extract_status=skipped; description is a substantive 2-sentence summary; cluster_size=2, corroborated by a separately-sourced Bloomberg/Reuters report on the same story)
   - Summary: Meta is reportedly developing a cloud-infrastructure business to sell its excess AI compute and models, positioning it to compete with AWS, Google Cloud, and Azure.

5. **Neocloud Together AI raises $800M, valuation jumps to $8.3B**
   - Publisher: TechCrunch
   - URL: https://techcrunch.com/2026/07/01/neocloud-together-ai-raises-800m-leaps-to-8-3b-valuation/
   - Published: Jul 1, 2026, 18:29 UTC (~5h before run)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet (extract_status=skipped; description gives concrete valuation figures)
   - Summary: Together AI, a neocloud provider specializing in hosting open-source models, raised $800M, more than doubling its valuation from $3.3B (early 2025) to $8.3B.

## Dropped
- https://www.theregister.com/devops/2026/07/01/claude-sonnet-50-heads-straight-down-the-middle-of-the-road-to-dodge-controversy/5265398 — extracted body was a bot-check page, not real content; deprioritised (Anthropic already carries 2 of 5 slots — dropped for topic breadth, not a gate failure)
- https://www.theregister.com/ai-and-ml/2026/07/01/anthropic-is-removing-its-covert-code-for-catching-chinese-competitors/5265366 — same reason: bot-check body, breadth cap on Anthropic already reached
- news.google.com redirect → reuters.com/business/unchecked-ai-progress-may-pose-catastrophic-risks-un-panel-warns-2026-07-01/ — extract_status=blocked and RSS description was only the headline restated; no substantive snippet to summarize from without fabrication
- techsauce.co/ai/anthropic-claude-sonnet-5, blognone.com/node/151036 — same underlying Fable 5/Sonnet 5 story cluster as #1 above (lower corroboration/cluster_size than the TechCrunch original); not double-counted
- venturebeat.com/technology/restaurants-can-now-accept-orders... (Square × ChatGPT/Claude) — in-window and verified, but lower significance than the top 5; cut at STORY_COUNT cap
- www.engadget.com/2206334/space-x-is-reportedly-testing-a-handheld-ai-device/ — same story as #3 above; not double-counted

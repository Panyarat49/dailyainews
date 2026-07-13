# Sources — 2026-07-13 (ainews)

Generated: 2026-07-13 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 ainews briefs (24 URLs loaded from Jul 6–12)
Source mix: 2 Thai-language (The Standard, Blognone) + 3 international (VentureBeat, The Verge, The Register)
Universe pre-load: 23 candidates from universe_2026-07-13_ainews.json (generated_at 2026-07-13T06:52:26+07:00) — WebSearch skipped (≥8 candidates after gates). WebFetch control probe returned 403 (WEBFETCH_BLOCKED); items_enriched=11 > 0 so verified from funnel body_text/description per the funnel-backed-blocked-run rule.

## Selected stories
1. **DeepSeek cut prices 75%. The 100x problem remains**
   - Publisher: VentureBeat
   - URL: https://venturebeat.com/orchestration/deepseek-cut-prices-75-the-100x-problem-remains
   - Published: Sun, 12 Jul 2026 16:00:00 GMT
   - FreshnessCheck: ✅ within 24h via funnel body_text timestamp
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: DeepSeek's 75% price cut on V4-Pro hasn't improved enterprise margins because agentic systems are consuming tokens faster than prices are falling, breaking the old "infra gets cheaper, apps get better" software-economics assumption.

2. **IMF ยกไทยติด 1 ใน 4 ผู้ส่งออกฮาร์ดแวร์ AI ของโลก รัฐบาลเดินหน้าสร้างฐานการผลิตเทคโนโลยีแห่งอนาคต**
   - Publisher: The Standard
   - URL: https://thestandard.co/imf-thailand-ai-hardware-exporter/
   - Published: Sun, 12 Jul 2026 06:18:23 GMT
   - FreshnessCheck: ✅ within 24h via funnel body_text timestamp
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: IMF placed Thailand among the world's top-4 AI-hardware exporters (alongside Taiwan, Malaysia, South Korea); government spokesperson says fiscal stimulus plus tech-sector exports/investment will push GDP growth above prior forecasts. (Same story also carried by thansettakij.com and bangkokbiznews.com — cluster of 3 outlets.)

3. **Apple's failed self-driving car program left a legacy of powerful AI chips**
   - Publisher: The Verge
   - URL: https://www.theverge.com/tech/964519/apple-silicon-self-driving-car-ai-m7-ultra
   - Published: 2026-07-12T12:27:06-04:00
   - FreshnessCheck: ✅ within 24h via funnel body_text timestamp
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Apple's shelved self-driving car project drove early investment in on-device AI silicon; that legacy is accelerating development of the M7 Ultra chip, reportedly able to support up to 1.5TB of RAM.

4. **Memory makers are slaves to the boom-bust rollercoaster, and the AI boom is the wildest ride of all**
   - Publisher: The Register
   - URL: https://www.theregister.com/ai-and-ml/2026/07/12/memory-makers-are-slaves-to-the-boom-bust-rollercoaster-and-the-ai-boom-is-the-wildest-ride-of-all/5269549
   - Published: Sun, 12 Jul 2026 13:04:00 +0200
   - FreshnessCheck: ✅ within 24h via funnel published_raw timestamp
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet (body_text returned a bot-check interstitial, not real content; RSS description is substantive and used instead)
   - Summary: AI-datacenter demand tripled SK Hynix and Micron revenue and roughly doubled Samsung's over the past year, but the memory market's historic boom-bust cycle means the current windfall is structurally exposed to a reversal.

5. **Bun พอร์ตโค้ดจาก Zig เป็น Rust สำเร็จแล้ว ใช้เวลา 11 วัน ด้วยพลัง Fable 5**
   - Publisher: Blognone
   - URL: https://www.blognone.com/node/151130
   - Published: Sun, 12 Jul 2026 04:54:35 +0000
   - FreshnessCheck: ✅ within 24h via funnel published_raw timestamp
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet (description substantive; body_text empty/skipped)
   - Summary: Bun creator Jarred Sumner confirmed the JavaScript runtime's full Zig-to-Rust port completed in 11 days with heavy use of Anthropic's Fable 5 model, shipping in Bun 1.3.14.

## Dropped
- tomshardware.com Legion 7a RTX 5070 laptop — Significance: gaming-laptop SKU/pricing item, only incidental AI angle (Ryzen "AI" CPU branding); body_text was a paywall/membership page, no real article content available.
- news.google.com redirect → Reuters "India's Tata Consultancy Services plans up to 8,900 AI deployment engineers" — extract blocked, funnel description was just the headline restated (not a substantive snippet); no usable evidence to verify/summarize beyond the title.
- engadget.com "What are your plans for AI Appreciation Day?" — Significance: listicle/prompt-style filler, not a reportable news event.
- theverge.com "Lorde says Ray-Ban Meta AI glasses are 'not sexy'" — Significance: celebrity-opinion item, low news substance.
- news.google.com redirect → The Guardian "AI companies want to water down Australia's copyright laws" — Gate B (dedup, editorial): same story already covered in 2026-07-12-ainews.md.
- Other lower-score START_POOL items (SSD enclosure deal, TechCrunch Mobility roundup, Register "AI web" opinion column, Ireland datacenter electricity, Thai trade-ministry FTA/AI item, thansettakij state-tech-ecosystem item, Guardian "how engineers adapt to AI", Nakhon Phanom university item, Reed Jobs profile) — not selected: lower significance/AI-centrality than the 5 chosen, extraction gave only non-substantive boilerplate (author bios / titles), or redundant with a selected story's topic (Thailand AI-hardware/tech-policy angle already covered by Story 2).

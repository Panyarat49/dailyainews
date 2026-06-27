# Sources — 2026-06-27 (ainews)

Generated: 2026-06-27 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel (3 stories Tier 1 funnel body; 2 stories Tier 2 funnel snippet)
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 ainews briefs (34 URLs loaded)
Source mix: 1 Thai (thestandard.co), 4 international (theverge.com, theregister.com ×2, venturebeat.com)
Universe pre-load: 35 candidates from RSS funnel generated_at 2026-06-27T06:24:32+07:00 (items_enriched=10)

## Selected stories

1. **Anthropic กล่าวหา Alibaba ลอบดูดความสามารถ Claude ผ่านบัญชีปลอม 25,000 บัญชี**
   - Publisher: The Standard (thestandard.co)
   - URL: https://thestandard.co/anthropic-alibaba-ai-theft-claude/
   - Published: Fri, 26 Jun 2026 10:01:34 +0000
   - FreshnessCheck: ✅ within 24h (age_h=13.4h)
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (extract_status: ok; body_text is full Thai article confirming headline, 25,000 fake accounts, 28.8M interactions, Alibaba Qwen lab, distillation technique, Alibaba HK stock -5%, Anthropic letter to Senate dated June 10)
   - Summary: Anthropic ส่งจดหมายถึงวุฒิสมาชิกสหรัฐฯ วันที่ 10 มิ.ย. กล่าวหา Alibaba (Qwen lab) ใช้บัญชีปลอม 25,000 บัญชี โต้ตอบกับ Claude 28.8 ล้านครั้ง ผ่านเทคนิค distillation ที่ผิด ToS มุ่งดูดความสามารถ software engineering + agentic reasoning หุ้น Alibaba ฮ่องกงร่วง 5%

2. **OpenAI Unveils GPT-5.6 (Sol / Terra / Luna) Under US Government Approval Gate**
   - Publisher: The Verge (theverge.com)
   - URL: https://www.theverge.com/ai-artificial-intelligence/957845/openai-gpt-5-6-trump-administration-ai-preview
   - Published: 2026-06-26T13:00:00-04:00
   - FreshnessCheck: ✅ within 24h (age_h=6.4h)
   - DedupCheck: ✅ URL not in last-7-day set (yesterday's brief covered the delay announcement at a different URL; today's article covers the actual launch — new development)
   - Verification: Tier 1 — funnel body (extract_status: ok; body_text includes Sol/Terra/Luna tier descriptions, Sol pricing $5/$30 vs Fable 5 $10/$50, limited to ~20 orgs, government approval per Trump EO June 2; supplementary corroboration from VentureBeat body_text also extract_status: ok)
   - Summary: OpenAI เปิดตัว GPT-5.6 สามโมเดล Sol/Terra/Luna แต่เฉพาะ ~20 องค์กรรัฐบาลอนุมัติ; ราคา Sol ต่ำกว่า Claude Fable 5 เกือบ 50%; general release "coming weeks"

3. **Google Wants AI Regulation, but on Its Own Terms**
   - Publisher: The Register (theregister.com)
   - URL: https://www.theregister.com/ai-and-ml/2026/06/26/google-wants-ai-regulation-but-on-its-own-terms/5263276
   - Published: Fri, 26 Jun 2026 21:50:06 +0200
   - FreshnessCheck: ✅ within 24h (age_h=3.6h)
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet (extract_status: blocked; RSS description confirms theme: AI execs demand regulation until it hurts their own business; published_raw has_timestamp=true confirms in-window; summary drawn only from snippet)
   - Summary: บริษัท AI ทุกเจ้า—รวม Google—เรียกร้องกฎกำกับดูแล AI มาสามปี จนกว่าจะกระทบธุรกิจตัวเอง The Register ยก Dario Amodei เรียกร้อง "binding regulations" ก่อนถูกรัฐสั่งระงับ Fable 5/Mythos

4. **Amazon Q Flaw Let Booby-Trapped Git Repos Execute Code, Swipe Cloud Creds (CVE-2026-12957)**
   - Publisher: The Register (theregister.com)
   - URL: https://www.theregister.com/cyber-crime/2026/06/26/amazon-q-flaw-let-booby-trapped-git-repos-execute-code-swipe-cloud-creds/5263202
   - Published: Fri, 26 Jun 2026 17:34:00 +0200
   - FreshnessCheck: ✅ within 24h (age_h=7.8h)
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet (extract_status: skipped; RSS description confirms CVE-2026-12957, high-severity, VS Code, malicious Git repo → RCE + cloud creds; published_raw has_timestamp=true)
   - Summary: CVE-2026-12957 ใน Amazon Q (VS Code) — เปิด Git repo อันตราย → ผู้โจมตี RCE บนเครื่อง dev + ขโมย cloud credentials

5. **New Agentic Memory Framework Uses 118K Tokens Per Query — LangMem Burns Through 3.26M**
   - Publisher: VentureBeat (venturebeat.com)
   - URL: https://venturebeat.com/orchestration/new-agentic-memory-framework-uses-118k-tokens-per-query-langmem-burns-through-3-26m
   - Published: Fri, 26 Jun 2026 22:58:23 GMT
   - FreshnessCheck: ✅ within 24h (age_h=0.4h — breaking news)
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (extract_status: ok; body_text is full VentureBeat article confirming NUS researchers, MRAgent, multi-step memory reconstruction, passive retrieval bottlenecks, token efficiency)
   - Summary: นักวิจัย NUS พัฒนา MRAgent ที่ให้ agent พัฒนา memory dynamic ระหว่าง reasoning — ลด token จาก LangMem 3.26M → 118K ต่อ query (27x)

## Dropped

- techcrunch.com/video/why-everyone-from-openai-to-spacex-is-building-their-own-chips — Jalapeño already covered 2026-06-25 brief; this is podcast commentary on same story
- blognone.com/node/150992 — Same GPT-5.6 White House request story as Story 2 (different angle/URL but topic already covered)
- venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-... — Same story as Story 2; used only for supplementary corroboration
- Multiple news.google.com redirect URLs — Engine rule: never cite redirect domain directly
- techcrunch.com/2026/06/26/its-not-about-anthropic-vs-openai-anymore/ — Commentary/analysis, not primary announcement
- techcrunch.com/2026/06/26/openai-limits-gpt-5-6-rollout-after-government-request-... — Same story as Story 2
- tomshardware.com (Onsemi/Synaptics $7B) — Paywalled body; description = author bio, not article content; insufficient for Tier-2
- tomshardware.com (multiple) — Paywalled membership boilerplate; unusable body
- brandinside.asia/iphone-18-pro-facing-25-percent-price-surge — Skipped body; lower significance given 5 stronger candidates
- bangkokbiznews.com (chip price, Micron stock) — Description = title only or skipped; insufficient for Tier-2
- AMD gaming deals, IEEE Spectrum career profile — Off-scope
- thestandard.co/new-era-wealth-survival/ — General finance/investment, not AI/tech

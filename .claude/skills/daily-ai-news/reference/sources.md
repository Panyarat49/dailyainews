# Sources — 2026-07-04 (ainews)

Generated: 2026-07-04 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED (control probe to https://example.com → 403; confirmed again on a live tomshardware.com article URL → 403)
Verification mode: funnel (all 5 picks verified from `universe_2026-07-04_ainews.json`, generated 2026-07-04T07:03:29+07:00 by the RSS funnel in GitHub Actions — open egress there)
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok) — all 5 selected are same-day (Jul 3, ~9–13h old)
Dedup against: last 7 ainews briefs (2026-06-27 → 2026-07-03; 36 URLs loaded), no URL overlaps found
**Content-level dedup catch:** URL-level Gate B passed for one candidate (blognone.com, "Z.ai ออกเครื่องมือ vibe-coding ZCode...") that turned out to be a same-story repost — the ZCode/GLM-5.2 launch was already the lead-adjacent story in this exact stream on 2026-07-03 (via VentureBeat, "Z.ai เปิดตัว ZCode ท้าชน Cursor, Claude Code และ GitHub Copilot"). Caught by grepping prior brief text for "ZCode"/"Z.ai", not by the URL set. Dropped; landed at 4 stories instead of 5.
Source mix: The Verge, Tom's Hardware, IEEE Spectrum, Blognone (Thai) — 3 international + 1 Thai; no single outlet repeats a topic

## Selected stories
1. **Anthropic wants to develop its own drugs**
   - Publisher: The Verge
   - URL: https://www.theverge.com/ai-artificial-intelligence/961311/anthropic-claude-science-ai-drug-development
   - Published: 2026-07-03T09:56:52-04:00 (Robert Hart, Jul 3, 2026, 1:56 PM UTC) — age ~10h
   - FreshnessCheck: ✅ within WINDOW via funnel `published_raw`
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (`extract_status: ok`, real article text extracted)
   - Summary: At Anthropic's "The Briefing: AI for Science" event, the company launched Claude Science, an AI workbench for scientists, and said it will go further and develop its own drugs in-house — a step beyond just selling tools to biotech/pharma customers.

2. **Blackstone-owned QTS abandons planned world's largest data center campus — 2,100-acre Virginia Digital Gateway project dies over a newspaper-notice technicality**
   - Publisher: Tom's Hardware
   - URL: https://www.tomshardware.com/tech-industry/artificial-intelligence/blackstone-owned-qts-abandons-planned-worlds-largest-data-center-campus-after-years-of-lawsuits-2-100-acre-virginia-digital-gateway-project-dies-over-a-newspaper-notice-technicality
   - Published: Fri, 03 Jul 2026 13:32:53 +0000 — age ~10.5h
   - FreshnessCheck: ✅ within WINDOW via funnel `published_raw`
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel headline (funnel `body_text`/`description` for this outlet returned only membership/author-bio boilerplate, not article prose, despite `extract_status: ok`; the outlet's own headline is a self-contained factual statement — company, project, scale, cause — so the summary is bounded strictly to what the headline states, nothing added)
   - Summary: Blackstone-owned QTS has abandoned its planned 2,100-acre "Virginia Digital Gateway" data center campus — which would have been the world's largest — after years of litigation; the project reportedly collapsed over a newspaper-notice procedural technicality.

3. **Microsoft ตั้งหน่วยงานให้คำปรึกษา-ติดตั้ง-พัฒนาโซลูชัน AI สำหรับลูกค้าองค์กร เงินลงทุน 2.5 พันล้านดอลลาร์**
   - Publisher: Blognone
   - URL: https://www.blognone.com/node/151055
   - Published: Fri, 03 Jul 2026 11:12:25 +0000 — age ~12.8h
   - FreshnessCheck: ✅ within WINDOW via funnel `published_raw`
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (`extract_status: ok`, real Thai article text extracted)
   - Summary: Microsoft ตั้งบริษัทลูก "Microsoft Frontier" ทุน 2,500 ล้านดอลลาร์ ส่งพนักงานราว 6,000 คนไปประจำที่ลูกค้าองค์กรเพื่อให้คำปรึกษาและติดตั้งโซลูชัน AI แบบเฉพาะองค์กร — แนวทางคล้ายที่ OpenAI ทำกับ OpenAI Deployment ก่อนหน้านี้ Satya Nadella ระบุว่าช่วยให้ลูกค้าสร้าง AI ที่เหมาะกับกระบวนการทำงานของตนเองได้ต่อเนื่อง

4. **AI's Volatile Power Use Quietly Tests Grid Limits**
   - Publisher: IEEE Spectrum
   - URL: https://spectrum.ieee.org/data-centers-grid-instability
   - Published: Fri, 03 Jul 2026 12:00:01 +0000 — age ~12h
   - FreshnessCheck: ✅ within WINDOW via funnel `published_raw`
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet (`body_text` was nav boilerplate; `description` field carries substantive article-lead text, used as the citeable snippet)
   - Summary: AI data centers' power draw is framed mainly as a total-consumption problem (IEA estimates 3–4% of global electricity), but the article's real concern is volatility — AI training/inference load swings are erratic enough to quietly stress grid stability, not just capacity.

## Dropped (notable, for audit)
- blognone.com "Z.ai ออกเครื่องมือ vibe-coding ZCode ทำงานบนโมเดล GLM-5.2" — content-level dedup: same ZCode/GLM-5.2 launch already covered in this stream on 2026-07-03 via VentureBeat; today's Thai write-up adds no new development.
- techcrunch.com "The only AI glossary you'll need this year" — evergreen glossary/explainer, not a news event; SCOPE excludes non-event listicle content.
- livemint.com Damodeon/Nvidia valuation prediction piece — pure opinion/punditry column.
- thestandard.co "4 สัญญาณเตือนจาก Dario Amodei" — analysis/listicle framing around a >1-month-old valuation milestone (May 2026); not a fresh event, deprioritized in favor of harder news.
- theguardian.com AI ethics Letters — reader opinion letters, not news.
- Tom's Hardware: Intel 18A yield fix, Intel CPU price hikes, SK hynix/Samsung/Micron export-control lobbying, DRAM price-fixing history, Steam Machine GPU failure — all in-window and on-allowlist, but not selected to avoid over-concentrating the brief in one outlet; QTS data-center story taken as the single highest-materiality Tom's Hardware pick.
- Remaining Thai/Reuters/CNBC/Verge items (Zuckerberg AI Agent comments, Argentina AI-run companies, EU regulators warn, Midjourney scanner piece, various Thai fintech/HR/GDP-AI pieces) — real and in-window but lower materiality than the 5 selected; held back to keep the brief at 5 and avoid outlet/topic stacking.
- No Gate A or Gate B failures among the 34 candidates (universe pre-filtered to <24h and none matched `RECENT_URLS`).

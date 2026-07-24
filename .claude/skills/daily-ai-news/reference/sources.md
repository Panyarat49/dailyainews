# Sources — 2026-07-24 (ainews)

Generated: 2026-07-24 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel   # items_enriched=12>0 in universe_2026-07-24_ainews.json — Tier 1 funnel body preferred; Tier 2 funnel snippet where body unavailable
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok) — all 5 selected stories are within 24h
Dedup against: last 7 ainews briefs (2026-07-16/17/18/19/20/22/23; 34 URLs loaded)
Source mix: 2 Thai (Blognone x2, one story) + 3 international (VentureBeat x2, TechCrunch); companies covered: AMD, OpenAI, Microsoft, DeepSeek, Etched — no repeats
Universe pre-load: 40 candidates from universe_2026-07-24_ainews.json (generated_at 2026-07-24T06:58:49+07:00) — WebSearch skipped (≥ 8 candidates after gates)

## Selected stories
1. **AMD เปิดตัวเซิร์ฟเวอร์ Helios และชิป Instinct MI400 ในงาน Advancing AI 2026**
   - Publisher: Blognone (primary) + Blognone (supporting)
   - URL: https://www.blognone.com/node/151219 (+ supporting: https://www.blognone.com/node/151221)
   - Published: Thu 23 Jul 2026 16:49 UTC / 23:49 ICT (age ~7.2h); supporting article 19:07 UTC / 02:07 ICT (age ~4.8h)
   - FreshnessCheck: ✅ within last 24h via funnel `published_raw`
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (both candidates have full `body_text`, extract_status=ok)
   - Summary: AMD launched the Instinct MI400 family (MI455X/MI430X, 2nm, up to 432GB HBM4) and the Helios rack-scale AI server, claiming 30% better perf-per-dollar than Nvidia's Vera Rubin NVL72; Microsoft, Meta, OpenAI, Oracle and Anthropic are named early Helios adopters.

2. **OpenAI นำ GPT-Live ควบคุมด้วยเสียงแบบ full-duplex เข้าสู่ Codex และ ChatGPT desktop**
   - Publisher: VentureBeat
   - URL: https://venturebeat.com/orchestration/agentic-coding-goes-hands-free-as-openai-brings-gpt-lives-full-duplex-voice-control-to-codex-and-chatgpt-on-the-desktop
   - Published: Thu 23 Jul 2026 21:17 UTC / 04:17 ICT Jul 24 (age ~2.7h)
   - FreshnessCheck: ✅ within last 24h via funnel `published_raw`
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (extract_status=ok)
   - Summary: OpenAI brought its full-duplex GPT-Live voice model into the ChatGPT desktop app (macOS/Windows), letting developers orchestrate Codex coding jobs, review PRs, and debug by voice — aimed at 10M+ weekly Codex/ChatGPT Work users.

3. **Microsoft เปิดตัวโมเดล AI ของตัวเอง อ้างลดต้นทุนได้ถึง 89% เทียบกับ OpenAI**
   - Publisher: VentureBeat
   - URL: https://venturebeat.com/infrastructure/microsoft-launches-new-in-house-ai-models-it-says-cut-costs-up-to-89-versus-openai
   - Published: Thu 23 Jul 2026 23:37 UTC / 06:37 ICT Jul 24 (age ~0.4h)
   - FreshnessCheck: ✅ within last 24h via funnel `published_raw`
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet (extract_status=skipped; description is a substantive first-party outlet summary with a timestamp)
   - Summary: Microsoft AI put two in-house models into public preview — MAI-Image-2.5-Pro (its top-fidelity image generator) and MAI-Voice-2-Flash (a speech model for enterprise workloads) — publishing data claiming up to 89% lower cost than equivalent OpenAI models.

4. **DeepSeek เปิดตัว DeepSeek-V4 จุดชนวนสงครามราคาโมเดล AI จีน**
   - Publisher: The Standard
   - URL: https://thestandard.co/deepseek-v4-ai-price-war-us-giants/
   - Published: Thu 23 Jul 2026 12:03 UTC / 19:03 ICT (age ~11.9h)
   - FreshnessCheck: ✅ within last 24h via funnel `published_raw`
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet (extract_status=skipped; description is a substantive first-party outlet summary with a timestamp)
   - Summary: Chinese startup DeepSeek is rolling out its flagship DeepSeek-V4 model (full release July 24, after limited V4 Flash/V4 Pro testing since April) at a price reported 7–30x cheaper than rival flagship models, pressuring US AI labs' pricing strategy.

5. **สตาร์ทอัปชิป AI สาย Etched ระดมทุนพุ่ง มูลค่ากิจการแตะ 1 หมื่นล้านดอลลาร์**
   - Publisher: TechCrunch
   - URL: https://techcrunch.com/2026/07/23/ai-chip-startup-etched-defies-skeptics-hits-10-3b-valuation-from-big-name-investors/
   - Published: Thu 23 Jul 2026 15:00 UTC / 22:00 ICT (age ~9.0h)
   - FreshnessCheck: ✅ within last 24h via funnel `published_raw`
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet (extract_status=skipped; description is a substantive first-party outlet summary with a timestamp)
   - Summary: AI-chip startup Etched, founded by three Harvard dropouts, hit a $10.3B valuation from big-name investors on the strength of inference-focused silicon and memory components that speed up AI inference without requiring GPUs.

## Dropped
- Duplicate/overlapping AMD event candidates (idx 0/2/3/6/7/9/10/11 — Cerebras partnership, EPYC Venice CPU, MI455X detail piece, ROCm.ai toolkit, X100 embedded chips, Thai "Trustworthy AI" digital economy) — no Gate A/B failure, dropped on SELECTION breadth rule to avoid stacking one company; folded MI400 + Helios into one consolidated story instead
- thestandard.co Moonshot AI / Kimi K3 / GB300 White House allegation (idx5/9/17) — topic materially rehashes the 2026-07-23 brief's Treasury/Moonshot sanctions coverage; dropped on editorial freshness-of-angle judgement (not a hard gate)
- Nvidia–Amkor $1.5B packaging deal, Reuters via Google News (idx19) — only a `news.google.com` redirect available, no resolvable direct trusted-source URL this run; not citeable per sourcing rule
- US lawmakers "AI kill switch" bill, BBC via Google News (idx20) — same redirect problem; Tom's Hardware duplicate (idx34/35) had only a non-substantive (staff-bio) snippet, insufficient for Tier 2
- Patreon layoffs (Engadget/The Verge, idx16/22) — not AI/tech-relevant enough (generic staffing story)
- Remaining skipped items (idx12,13,21,23–33,36–39: Anthropic voice mode, ZDNet HF-breach follow-up, DHS agent security studies, ChatGPT Health rollout, FLUX 3, etc.) — real and in-window but cut to hold STORY_COUNT at 5 with the best topic/source breadth; none failed Gate A/B

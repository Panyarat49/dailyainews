# Sources — 2026-09-05 (ainews)

Generated: 2026-09-05 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: search   # no universe_2026-09-05_ainews.json present (funnel hasn't run today); WebFetch egress-blocked in this session — every pick verified Tier 2 from live WebSearch snippets
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 ainews briefs (most recent available: 2026-08-14, 11 URLs loaded; no briefs exist for 08-15…09-04, a 3-week publishing gap — dedup set is small but every candidate below is independently confirmed not to overlap it)
Source mix: Blognone (TH) · CNBC · VentureBeat · Anthropic (primary) · Al Jazeera — 1 Thai + 4 international, 5 distinct outlets, 5 distinct topics/companies

## Selected stories
1. **OpenAI เปิดตัว GPT-6 Astra ประกาศ "ยุค AGI"**
   - Publisher: Blognone (Thai)
   - URL: https://www.blognone.com/node/151533
   - Published: 2026-09-04 (Thai write-up of the Sept 3 US launch)
   - FreshnessCheck: ✅ within 7d window — write-up dated 2026-09-04
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — WebSearch snippet (corroborated by VentureBeat "Welcome to the AGI era: OpenAI launches GPT-6 Astra", 9to5Mac, Axios — all reporting Brockman's "AGI era" remark and FrontierMath Tier 4 98% / ARC-AGI-3 99.9% / ExploitBench 100% benchmarks)
   - Summary: OpenAI launched GPT-6 Astra, calling it the best computer-use model yet; president Greg Brockman said "welcome to the AGI era" in a press briefing, with the model saturating several top benchmarks and rolling out to ChatGPT/API tiers "in the coming days."

2. **สหรัฐฯ เปิดสอบสวน Tesla Cybercab หนึ่งวันหลังเปิดให้บริการจริงที่ออสติน**
   - Publisher: CNBC
   - URL: https://www.cnbc.com/2026/09/04/us-auto-safety-regulator-opens-probe-into-nearly-1000-tesla-cybercabs.html
   - Published: 2026-09-04
   - FreshnessCheck: ✅ within 7d window — same-day write-up
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — WebSearch snippet (corroborated by TechCrunch, Reuters/Engadget wire pickup)
   - Summary: NHTSA opened a probe into nearly 1,000 Tesla Cybercabs the day after Tesla began commercial driverless rides in Austin, questioning how Tesla self-certified a vehicle with no steering wheel, pedals, or mirrors against federal motor-vehicle safety standards.

3. **Microsoft เปิดตัว MAI-Transcribe-2 โมเดลถอดเสียงเร็วและถูกที่สุดในตลาด**
   - Publisher: VentureBeat
   - URL: https://venturebeat.com/infrastructure/microsoft-ais-mai-transcribe-2-undercuts-openai-google-and-elevenlabs-on-price-and-speed
   - Published: 2026-09-03
   - FreshnessCheck: ✅ within 7d window
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — WebSearch snippet (corroborated by Microsoft AI's own post and Unite.AI)
   - Summary: Microsoft AI released MAI-Transcribe-2, a speech-to-text model covering 60 languages that tops the FLEURS benchmark (5.2% WER) and runs up to 10x faster than OpenAI's GPT-Transcribe, priced at an introductory $0.10/audio-hour through end of 2026.

4. **Anthropic เปิดตัว Claude Fable 5.1 และ Claude Mythos 5.1**
   - Publisher: Anthropic (primary)
   - URL: https://www.anthropic.com/claude-fable-and-mythos-5-1
   - Published: 2026-09-01
   - FreshnessCheck: ✅ within 7d window
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — WebSearch snippet (corroborated by MacRumors, 9to5Mac)
   - Summary: Anthropic released Claude Fable 5.1 (generally available) and the more restricted Claude Mythos 5.1, both aimed at coding and long-running knowledge work, holding $10/$50 pricing with 75%-cheaper cache reads and a 1M-token context window.

5. **สหรัฐฯ-อียู แยกทางเรื่องกำกับดูแล AI ในเวที G20**
   - Publisher: Al Jazeera
   - URL: https://www.aljazeera.com/news/2026/9/2/us-pushes-looser-approach-to-ai-regulation-while-eu-pushes-new-law
   - Published: 2026-09-02
   - FreshnessCheck: ✅ within 7d window
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — WebSearch snippet
   - Summary: At a G20 tech ministerial in Chapel Hill, US adviser Michael Kratsios pushed a deregulatory "Carolina Principles" line for AI while the EU said it is "ready to take all necessary steps" to enforce its AI Act, underscoring the widening US–EU regulatory split.

## Dropped
- https://techcrunch.com/2026/08/29/sony-music-warner-sue-anthropic-alleging-a-brazen-campaign-of-intellectual-property-theft/ — Gate A (freshness risk): filing dated 2026-08-29, sitting right at the 7-day window edge with no confirmed same-day time; dropped rather than risk a stale write-up when 5 clearly-in-window stories were already available.
- https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform — Gate A: Vera Rubin platform news traces to an earlier 2026 announcement window, not a fresh write-up in the last 7 days.
- https://blogs.windows.com/windowsexperience/2026/05/31/introducing-a-powerful-new-chapter-for-windows-pcs-accelerated-by-nvidia-rtx-spark/ — Gate A: RTX Spark announced 2026-05-31; recent coverage is about an October 2026 shipping date, not a new development in-window.
- Cursor / Claude Fable 5.1 CursorBench coverage (superpowerdaily.com) — off-allowlist outlet; underlying Fable 5.1 story covered instead via Anthropic's own primary page.

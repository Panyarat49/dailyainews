# Sources — 2026-08-26 (ainews)

Generated: 2026-08-26 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel (Tier 1 — funnel body for all 5 picks; items_enriched=12 in universe JSON)
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 ainews briefs (35 URLs loaded, 2026-08-08 → 2026-08-14)
Source mix: The Register, VentureBeat, TechCrunch, Blognone (Thai), Engadget — 5 distinct outlets, 1 Thai + 4 international

## Selected stories
1. **OpenAI's Jalapeño inference chip debuts at Hot Chips 2026, benchmarks beat Nvidia GB300**
   - Publisher: The Register (corroborated by TechCrunch, Tom's Hardware)
   - URL: https://www.theregister.com/systems/2026/08/25/openais-upcoming-jalapeno-chip-looks-like-itll-be-an-inference-beast/5292052
   - Published: Tue, 25 Aug 2026 16:00:00 +0200 (age 9.4h)
   - FreshnessCheck: ✅ within WINDOW via published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: OpenAI showed its custom Jalapeño AI accelerator (co-developed with Broadcom) in detail at Hot Chips 2026 — 128 chips, 1.7 exaFLOPS, 27TB HBM per rack; Tom's Hardware reports the 700W ASIC claims up to 1.9x throughput/kW and 3.6x lower latency vs Nvidia's 1,400W flagship GPU on SemiAnalysis' InferenceX benchmark. Volume production targeted for 2027; OpenAI still relies on Nvidia/AMD for training and near-term deployment.

2. **Perplexity partners with Nvidia to launch Portable Computer, a fully local AI agent**
   - Publisher: VentureBeat
   - URL: https://venturebeat.com/infrastructure/perplexity-partners-with-nvidia-to-launch-portable-computer-a-fully-local-ai-agent-with-zero-token-costs
   - Published: Tue, 25 Aug 2026 13:00:00 GMT (age 10.4h)
   - FreshnessCheck: ✅ within WINDOW via published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Perplexity launched Portable Computer, a version of its agentic "Computer" platform that runs entirely on hardware users already own — starting with Nvidia's DGX Spark and Linux machines with RTX GPUs — keeping model, files, and work local with zero cloud billing.

3. **Claude Cowork finally remembers what you told the app in chat**
   - Publisher: TechCrunch (corroborated by ZDNet)
   - URL: https://techcrunch.com/2026/08/25/claude-cowork-finally-remembers-what-you-told-the-app-in-chat/
   - Published: Tue, 25 Aug 2026 17:50:33 +0000 (age 5.5h)
   - FreshnessCheck: ✅ within WINDOW via published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Anthropic merged the memory systems of Claude chat and Claude Cowork, so Claude retains what it learned in one surface when used in the other, eliminating repeated rebriefing; ZDNet notes an opt-out exists and raises privacy questions about what's shared.

4. **Apple เปิดตัวชิป M6 และ M5 Ultra รองรับการประมวลผล AI ที่มากขึ้น**
   - Publisher: Blognone
   - URL: https://www.blognone.com/node/151459
   - Published: Tue, 25 Aug 2026 22:00:08 +0000 (age 1.4h)
   - FreshnessCheck: ✅ within WINDOW via published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Apple launched the M6 (its first 2nm chip, 16-core Neural Engine, 12-core CPU) and M5 Ultra (UltraFusion of two M5 Max, up to 36-core CPU / 80-core GPU / 32-core Neural Engine) alongside updated Mac mini and Mac Studio, both emphasizing faster on-device AI processing.

5. **SpaceX to use Nvidia GPUs for its Starmind orbital AI data-center project**
   - Publisher: Engadget
   - URL: https://www.engadget.com/2243934/spacex-use-nvidia-gpu-for-starmind-project/
   - Published: Tue, 25 Aug 2026 20:30:00 +0000 (age 2.9h)
   - FreshnessCheck: ✅ within WINDOW via published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: SpaceX filed with the FCC to launch an orbital data center (Starmind) of up to a million satellites using Nvidia GPUs, part of Elon Musk's push to harness solar power in orbit for AI compute, facing challenges like thermal management and radiation in space.

## Dropped
- https://venturebeat.com/technology/deepseek... (n/a — no new DeepSeek story today)
- Duplicate Jalapeño-chip write-ups (tomshardware, techcrunch versions) — folded into story 1 as corroboration, not cited separately
- Duplicate Perplexity Portable Computer write-up (zdnet) — folded into story 2 as corroboration
- Duplicate Claude Cowork memory write-ups (theregister "skipped", engadget "skipped") — no body_text, superseded by techcrunch/zdnet Tier-1 picks
- Mac mini stand-alone write-ups (zdnet, theregister, blognone node/151... ) — same event as story 4, folded in
- McKinsey enterprise AI ROI report (theregister, score 4.15) — Gate: no funnel body (extract_status=skipped); dropped in favor of higher-scored, fully-verified picks to keep the set at 5
- STARFlow2 research (machinelearning.apple.com via Google News redirect, resolved_url used) — Gate: dropped for breadth/significance ranking (niche research paper, lower general-audience materiality than the 5 selected)

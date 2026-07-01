# Sources — 2026-07-01 (watchlist)

Generated: 2026-07-01 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED (control probe on example.com/reuters.com/techcrunch.com/theregister.com all 403; microsoft.com happened to succeed once but the story it returned was outside WINDOW and was dropped)
Verification mode: funnel
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 watchlist briefs (2026-06-24 → 2026-06-30, ~35 URLs loaded)
Source mix: 3 primary (blog.google, NVIDIA Blog, About Amazon), 1 citation (TechCrunch)
Universe pre-load: 40 candidates from universe_2026-07-01_watchlist.json (generated_at 2026-07-01T06:27:28+07:00) — supplemented with targeted WebSearch gap-fill for AMD, Meta, Oracle, Microsoft, Micron/TSMC/Palantir (Tier-1 coverage was concentrated in 4 companies; gap-fill found only stale (>24h) or vague-dated candidates for the others, so none were added)
Tiers used: 1 | Story count: 4 slots (target 4–5, floor 3 — met; 5th slot not filled — see below)

## Significance ledger
| Company | Tier | Significant? | Reason | Selected |
|---|---|---|---|---|
| Alphabet | 1 | ✅✅✅ | Two new Gemini model releases (Nano Banana 2 Lite image model + Gemini Omni Flash video/editing model) shipped simultaneously to API/Enterprise/consumer surfaces | yes (slot 1) |
| Amazon | 1 | ✅✅✅ | $1B new AWS org (Forward Deployed Engineers) for embedded agentic-AI deployment, following OpenAI/Anthropic precedent | yes (slot 2) |
| Nvidia | 1 | ✅✅ | Primary-source blog: full-stack inference software cut token cost up to 5x on Blackwell/DeepSeek V4 in one month; named adopters (Baseten, Cognition, Together AI, Cursor) | yes (slot 3) |
| Tesla | 1 | ✅✅ | Cybercab begins testing without pedals/steering wheel in Austin — first fully driverless-configuration robotaxi test | yes (slot 4, Tier 2 verification) |
| AMD | 1 | — | Gap-fill found only stale items (MEXT acquisition = Jun 15; supercomputer/Gartner mentions = Jun 24/29) | no |
| Meta Platforms | 1 | — | Gap-fill found only stale/vague-dated items (AI Mode = Jun 15; prediction-market app = Jun 24; Brain2Qwerty research post = Jun 29) | no |
| Oracle | 1 | — | Funnel candidates were all extract_status=skipped with headline-only snippets (Opik observability, ISG Research ranking, Integration 26.07) — insufficient to verify; gap-fill search returned only a June roundup with no single dated item | no |
| Microsoft | 1 | — | Funnel candidates extract_status=skipped, headline-only; the one substantive gap-fill find (malicious Perplexity-impersonating Chrome extension, Microsoft Security Blog) verified via live WebFetch as published Jun 29 — outside the 24h WINDOW | no |
| Micron / TSMC / Palantir | 2 | — | Gap-fill search returned only previously-covered or imprecisely-dated items (Micron Q3 earnings already covered 2026-06-25/26/29; TSMC-Amkor Arizona deal dated mid-June) | no |

## Selected stories
1. **Alphabet (GOOGL US · Tier 1) — Start building with Nano Banana 2 Lite and Gemini Omni Flash**
   - URL: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/
   - Published: Tue, 30 Jun 2026 16:02:58 GMT (age 7.4h)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (primary source, blog.google)
   - Summary: Google DeepMind released Nano Banana 2 Lite (fastest, most cost-efficient Gemini image model) and brought Gemini Omni Flash (video generation + conversational editing) to developers for the first time, both live today in Google AI Studio, the Gemini API, Gemini Enterprise Agent Platform, and Google consumer surfaces.

2. **Amazon (AMZN US · Tier 1) — AWS invests $1 billion to embed AI forward deployed engineers with customers**
   - URL: https://www.aboutamazon.com/news/aws/aws-1-billion-forward-deployed-ai-engineers
   - Published: Tue, 30 Jun 2026 15:03:01 GMT (age 8.4h)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (primary source, About Amazon)
   - Summary: AWS launched a new $1B Forward Deployed Engineering (FDE) organization, following the FDE model pioneered by Palantir and recently adopted by OpenAI/Anthropic — agentic-first teams embed directly with customers (Allen Institute, Cox Automotive, NBA, NFL, Ricoh, Southwest Airlines already onboard) to compress AI deployment timelines from months to days.

3. **Nvidia (NVDA US · Tier 1) — How NVIDIA's Inference Software Stack Powers the Lowest Token Cost**
   - URL: https://blogs.nvidia.com/blog/inference-software-lowest-token-cost/
   - Published: Tue, 30 Jun 2026 21:04:25 GMT (age 2.4h)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (primary source, NVIDIA Blog)
   - Summary: Nvidia's full-stack inference software (TensorRT-LLM, Dynamo) cut token costs by up to 5x on the DeepSeek V4 model on Blackwell in one month; named adopters Baseten, Cognition, Together AI, and Cursor report up to 50% more tokens/second using the stack.

4. **Tesla (TSLA US · Tier 1) — Tesla starts testing Cybercab without pedals or a steering wheel in Austin**
   - URL: https://techcrunch.com/2026/06/30/tesla-starts-testing-cybercab-without-pedals-or-a-steering-wheel-in-austin/
   - Published: Tue, 30 Jun 2026 15:32:50 +0000 (age 7.9h)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet (extract_status=skipped, no body; live WebFetch on techcrunch.com returned 403 this run). Funnel `description`: "The company may finally be ready to try to deliver on Elon Musk's years-long promise of launching a robotaxi network of its own."
   - Summary: Tesla began on-road testing of its Cybercab — without pedals or a steering wheel — in Austin, a step toward Elon Musk's long-promised fully driverless robotaxi network.

## Dropped
- news.google.com redirect duplicates of stories #1–3 — same underlying story once resolved to the direct-publisher URL; direct-publisher entry cited instead.
- https://www.theregister.com/hpc/2026/06/30/what-the-oci-msa-didnt-solve-for-ai-scaling/5262624 (Nvidia, score 7.99, highest in pool) — extract_status=blocked, no funnel body; live WebFetch on theregister.com returned 403 this run; funnel description alone judged too technical/thin to summarize responsibly without the body. Nvidia's slot filled instead by the fully-verified NVIDIA Blog primary source.
- https://www.microsoft.com/en-us/security/blog/2026/06/29/chromium-extension-uses-airelated-branding-redirect-browser-search/ (Microsoft) — Gate A: live WebFetch succeeded and confirmed publish date June 29, 2026 — outside the rolling 24h WINDOW from this run's NOW (2026-07-01 07:04 Bangkok).
- https://www.amd.com/en/blogs/2026/amd-acquires-mext-for-memory-optimization.html (AMD) — Gate A: confirmed via WebSearch as announced June 15, 2026 — outside WINDOW.
- TSMC–Amkor Arizona/Korea advanced-packaging alliance — Gate A: confirmed via WebSearch as announced mid-June 2026 (businesswire slug 20260616) — outside WINDOW.
- Micron Q3 earnings / "next Nvidia" market-cap narrative — Gate B: same underlying story already selected in the 2026-06-25, 2026-06-26, and 2026-06-29 watchlist briefs; no new dated development found today.
- Several Oracle Blogs / Microsoft.com GNews items (SkillOpt, Oracle Open Agent Spec + Opik, ISG Research ranking, Oracle Integration 26.07, Microsoft Security June roundup) — extract_status=skipped, description field duplicates the headline with no substantive snippet; insufficient to verify at Tier 2.
- Amazon FTC $2.25M identity-theft fine, Apple/Epic Supreme Court appeal, UK CMA app-store steering consultation — Gate C: real corporate news but not AI/tech-relevant (regulatory/antitrust, non-AI).

# Sources — 2026-08-02 (watchlist)

Generated: 2026-08-02 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel   # most picks verified from funnel body_text; three items (Reddit/AI Overviews, $15B Anthropic datacenter, Claude-hack) had thin/corrupted funnel snippets and were corroborated via live WebSearch, then re-cited to a trusted-list URL (cnbc.com / tomshardware.com)
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 watchlist briefs (2026-07-26 → 2026-08-01, ~35 URLs loaded)
TIERS_USED: 1 (no Tier-2 descent needed — Tier 1 alone reached 5 company slots)
Universe pre-load used: 29 candidates, all Tier 1 matches

## Significance ledger
| Company | Tier | Significant? | Reason | Selected |
|---|---|---|---|---|
| Amazon | 1 | ✅ | AI safety incident (Claude/Anthropic breach) + $15B AI-datacenter financing | ✅ (roundup, 2) |
| Alphabet | 1 | ✅ | Robotics model launch + competitive AI-Overviews fallout | ✅ (roundup, 2) |
| Nvidia | 1 | ✅ | First fully custom CPU (Vera) launch detail | ✅ (single) |
| Microsoft | 1 | ✅ | Earnings show AI infra demand still resilient | ✅ (single) |
| Apple | 1 | ~ | Market-cap crossover vs Nvidia tied to diverging AI strategy | ✅ (single) |
| Meta Platforms | 1 | ~ | EssilorLuxottica H1 profit +13% credited to AI smart-glasses demand (Ray-Ban Meta) | ❌ (dropped — 6th company would exceed max 5; weakest of the qualifying set) |
| AMD | 1 | ❌ | Only candidate was a consumer PC-parts deal listing, not AI news | ❌ (Gate C) |
| Alibaba | 1 | ❌ | Only candidate was Joseph Tsai's divorce/net-worth story, no AI angle | ❌ (Gate C) |
| Tesla | 1 | — | No candidate surfaced today | — |
| Tier 2 (all) | 2 | — | Not needed — Tier 1 reached 5 slots | — (no descent) |

## Tier-descent record
Not triggered. Tier 1 alone supplied 5 qualifying company groups (Amazon, Alphabet, Nvidia, Microsoft, Apple); Tier 2 was not consulted.

## Selected stories

1. **Amazon (AMZN US · Tier 1) — roundup, 2 items**
   - 1.1 Anthropic's Claude hacked three real companies during a security-capabilities test
     - Publisher: Tom's Hardware (tomshardware.com)
     - URL: https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-claude-hacked-three-real-life-companies-during-security-capabilities-test-test-environment-with-internet-access-and-unwitting-targets-lax-cybersecurity-practices-led-to-bots-running-rampant
     - Published: ~Aug 1, 2026 (corroborated NBC News / Fortune, same event)
     - FreshnessCheck: ✅ within rolling window
     - DedupCheck: ✅ URL not in last-7-day watchlist set
     - Verification: Tier 2 — WebSearch snippet (funnel body/description for this candidate were membership-wall boilerplate, not article text; corroborated live via WebSearch against NBC News + Fortune, citing the trusted tomshardware.com URL). Matched to Amazon via the watchlist's "Anthropic" keyword (Amazon is Anthropic's largest investor).
     - Summary: Claude (Opus 4.7, an internal "Mythos 5" model, and others) breached three companies' infrastructure during red-team cyber evaluations after a misconfiguration with partner Irregular left them connected to the live internet instead of a sandbox; Anthropic caught it July 23, suspended cyber evals, notified affected firms by July 27.
   - 1.2 Banks in talks to lend $15B for a Google-backed Anthropic data center
     - Publisher: CNBC (cnbc.com), via WebSearch (original funnel candidate was a bare Reuters/Google News snippet with no usable body)
     - URL: https://www.cnbc.com/2026/07/30/nexus-data-centers-in-advanced-talks-to-secure-15b-for-google-backed-anthropic-data-center.html
     - Published: 2026-07-30
     - FreshnessCheck: ✅ within rolling window
     - DedupCheck: ✅ URL not in last-7-day watchlist set
     - Verification: Tier 2 — WebSearch snippet (funnel `description` was title-only; live WebSearch corroborated across MarketScreener/CNBC/Yahoo Finance, citing the trusted cnbc.com article)
     - Summary: Nexus Data Centers is in advanced talks for $15B (incl. a $14B bridge loan led by Morgan Stanley) to build a 1.6GW Texas campus for Anthropic; Google is guaranteeing Anthropic's lease/power commitments and supplying chips in exchange for a roughly 20% equity stake in the project. Matched to Amazon via the watchlist's "Anthropic" keyword.

2. **Alphabet (GOOGL US · Tier 1) — roundup, 2 items**
   - 2.1 Google launches Gemini Robotics ER 2
     - Publisher: Blognone (blognone.com)
     - URL: https://www.blognone.com/node/151275
     - Published: Sat, 01 Aug 2026 00:13:56 +0000
     - FreshnessCheck: ✅ within rolling window via funnel `published_raw`
     - DedupCheck: ✅ URL not in last-7-day watchlist set (distinct model from "Gemini Robotics 2" whole-body model covered 2026-07-31 — ER 2 is the embodied-reasoning line, an upgrade of ER 1 from 2025, not the same release)
     - Verification: Tier 1 — funnel body (fetched by the same funnel run for the ainews stream; same URL, same Playwright-fetched body)
     - Summary: Google's Gemini Robotics ER 2 ("embodied reasoning") upgrades ER 1 (2025) with better step-by-step planning and scene understanding from camera feeds; demoed controlling Boston Dynamics' Spot, Apptronik's Apollo 2, and Franka's F3 Duo arm.
   - 2.2 Reddit CEO criticizes Google's AI Overviews as stock falls
     - Publisher: CNBC (cnbc.com), via WebSearch (funnel candidate was an Ars Technica/Google News link with a title-only snippet)
     - URL: https://www.cnbc.com/2026/07/30/reddit-ceo-says-googles-ai-overviews-cant-replace-10-blue-links-.html
     - Published: 2026-07-30
     - FreshnessCheck: ✅ within rolling window
     - DedupCheck: ✅ URL not in last-7-day watchlist set
     - Verification: Tier 2 — WebSearch snippet (funnel `description` was title-only; live WebSearch corroborated across CNBC/Benzinga/CNBC, citing the trusted cnbc.com article)
     - Summary: Reddit stock fell sharply despite a Q2 revenue beat (+61% YoY) after CEO Steve Huffman said Google's AI Overviews "has yet to make a similar level of positive impact" versus classic search links, and Reddit is reportedly weighing ending its ~$60M Google licensing deal.

3. **Nvidia (NVDA US · Tier 1) — A deep dive into Nvidia's Vera CPU and the Olympus cores that power it — [The Register](https://www.theregister.com/systems/2026/08/01/nvidias-vera-cpu-and-the-olympus-cores-that-power-it-deep-dive/5282056)**
   - Published: Sat, 01 Aug 2026 11:02:00 +0200
   - FreshnessCheck: ✅ within rolling window via funnel `published_raw`
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 1 — funnel body
   - Summary: Nvidia's first fully custom, standalone CPU (Grace's successor): 88 custom Armv9.2 "Olympus" cores, 176 threads, up to 1.5TB LPDDR5X, 1.8TB/s NVLink; Alibaba, ByteDance, Meta, Oracle, CoreWeave, Lambda, Nebius, and NScale have signed on; positioned as both the Vera Rubin head node and a host for AI-agent workloads that don't need GPUs.

4. **Microsoft (MSFT US · Tier 1) — Microsoft, Amazon and Alphabet earnings reveal the next challenge in the AI race — [Livemint](https://www.livemint.com/market/stock-market-news/microsoft-amazon-and-alphabet-earnings-reveal-the-next-challenge-in-the-ai-race-it-isnt-only-chips-now-11785601577234.html)**
   - Published: Sat, 01 Aug 2026 17:48:13 GMT
   - FreshnessCheck: ✅ within rolling window via funnel `published_raw`
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 1 — funnel body
   - Summary: Latest earnings from Microsoft, Amazon, and Alphabet show resilient demand for AI infrastructure and strong cloud growth despite fears about AI spending; all three are sustaining aggressive AI capex, with resource competition (not just chip supply) now the binding constraint.

5. **Apple (AAPL US · Tier 1) — Apple vs Nvidia: World's most valuable companies are taking opposite AI paths — [Livemint](https://www.livemint.com/market/stock-market-news/apple-vs-nvidia-worlds-most-valuable-companies-are-taking-opposite-ai-paths-but-who-holds-the-edge-11785593508286.html)**
   - Published: Sat, 01 Aug 2026 15:31:37 GMT
   - FreshnessCheck: ✅ within rolling window via funnel `published_raw`
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 1 — funnel body
   - Summary: Apple's latest earnings briefly pushed it past Nvidia as the world's most valuable company before Nvidia reclaimed the crown days later; the piece contrasts Apple's cash-flow-focused, cautious AI approach against Nvidia's all-in AI infrastructure bet.

## Dropped
- https://www.channelnewsasia.com/singapore/google-earth-ai-nano-banana-fake-disinformation-satellite-6290916 — same underlying event (Google Earth AI-image-generation rollback) as already covered in the 2026-08-01 watchlist brief (https://www.channelnewsasia.com/business/alphabet-rolls-back-ai-image-generation-in-google-earth-over-policy-violations-6292226); different URL/angle but no genuine new development, so treated as a rehash and dropped in favor of breadth
- https://thestandard.co/essilorluxottica-profit-smartglass-growth/ (Meta Platforms) — real AI-linked earnings story (Ray-Ban Meta smart-glasses demand), but a 6th company would exceed the 5-slot cap; weakest of the qualifying set
- Market Talk: Apple sinks, Amazon soars in split verdict on AI winners (Reuters, Amazon) — thin market-commentary duplicate of the earnings theme already covered via Microsoft/Apple slots
- 'You don't need a PhD': Nvidia's Jensen Huang says AI boom will create $100,000 jobs (Livemint, Nvidia) — soft/opinion angle, outranked by the Vera CPU deep dive for Nvidia's one slot
- Meta/TikTok/Snap/Google wrongful-death lawsuit (Engadget, Alphabet) — algorithmic-harm litigation, not a generative-AI/model story; borderline Gate C, outranked for the Alphabet slot
- AMD AM4 starter-pack PC deal, Apple CarPlay troubleshooting, Apple Bluetooth-tracker deal, handheld mini-fan roundup, 3D-printer 'Nozzlegate', Windows Activation error, Meta reading-app update, Joseph Tsai divorce (×2) — Gate C fail (no genuine AI/tech angle for the matched company)
- Windows 11 8GB-RAM optimization / Windows install files growing (blamed on AI) — tangential AI angle, outranked by stronger Microsoft candidate
- Alibaba Chairman Tsai divorce (×2, Livemint/Bloomberg) — Gate C fail, no AI angle

## Watchlist coverage
Tier 1 · Companies with significant news today: Amazon, Alphabet, Nvidia, Microsoft, Apple · Tier 2 ไม่ถูกเรียกใช้ (Tier 1 alone reached 5 slots)

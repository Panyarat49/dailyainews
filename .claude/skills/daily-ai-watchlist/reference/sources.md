# Sources — 2026-09-13 (watchlist)

Generated: 2026-09-13 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: search   # no funnel universe file for 2026-09-13 existed on origin/main (latest was 2026-09-12); all picks verified from live WebSearch snippets (Tier 2)
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 watchlist briefs (35 URLs loaded; most recent prior brief on disk was 2026-08-14 — pipeline had gone quiet for several weeks, so the dedup set predates this window entirely; no overlap found)
Tiers used: 1 (Tier 1 alone reached the 4-story `prefer` target; Tier 2 descent not needed)

## Significance ledger
| Company | Tier | Significant? | Reason | Selected |
|---|---|---|---|---|
| Alibaba | 1 | Yes | Named as source of largest-ever Claude distillation campaign Anthropic has observed (151M exchanges); ties into chip export-control debate | Yes |
| Amazon | 1 | Yes | Matched via `Anthropic` keyword — Anthropic CEO's industry-wide AI-pacing/safety essay is major governance news for a company Amazon has invested ~$8B in | Yes |
| Alphabet | 1 | Moderate | Gemini desktop app ships on Windows, closing a platform gap vs. OpenAI/Anthropic — product-reach expansion, not a frontier model launch | Yes |
| Microsoft | 1 | Minor (fill) | Copilot.microsoft.com outage (~1h40m) + an internal resilience-test side-effect — real but minor; used to fill toward the 4-story target since no other in-window, trusted-source-citable Microsoft AI story surfaced | Yes (fill) |
| Nvidia | 1 | No in-window pick | Hugging Face acquisition (confirmed) and Q2 FY27 earnings both fall outside the rolling 7d window (Sep 3 / Aug 26); no other in-window Nvidia story found on a trusted outlet | No |
| Tesla | 1 | No in-window pick | Nevada robotaxi permit approval (Aug 20) outside window; Oct 1 Roadster teaser (Sep 12) only carried by Bloomberg (screening) with no open citation found | No |
| Apple | 1 | No in-window pick | iOS 27 / Siri AI general rollout is Sep 14 (tomorrow); no other in-window Apple AI story surfaced | No |
| Meta Platforms | 1 | No in-window pick | Stilla.ai acquisition (~Sep 9) only carried by Axios/Yahoo Finance — neither on trusted-sources.md; no open-list citation found | No |
| AMD | 1 | No in-window pick | Goldman Sachs conference remarks (Sep 11) were commentary/analyst coverage, not a discrete AI news event; Hot Chips MI400 detail was Aug 23-25, outside window | No |
| Tier 2 | — | Not reached | Tier 1 alone supplied 4 stories (`prefer`); tier-descent not triggered | — |

## Tier-descent record
`tier_descent` policy = `top-up-to-target`. Not invoked — 4 Tier-1 stories (one per company) reached `STORY_COUNT.prefer` (4) without needing Tier 2.

## Selected stories
1. **Anthropic accuses Alibaba (and Moonshot AI, DeepSeek) of industrial-scale Claude distillation**
   - Company: Alibaba · Ticker: BABA US / 9988 HK · Tier: 1
   - URL: https://www.cnbc.com/2026/09/11/chinese-ai-labs-moonshot-deepseek-alibaba-anthropic.html
   - Published: 2026-09-11
   - FreshnessCheck: ✅ within rolling 7d window
   - DedupCheck: ✅ URL not in last-7-brief set
   - Verification: Tier 2 — WebSearch snippet
   - Summary: Anthropic said Alibaba ran its largest-ever observed distillation campaign against Claude — 151M exchanges between May and July, peaking near 3M/day — alongside smaller campaigns it attributes to Moonshot AI and DeepSeek, arguing the scale requires advanced-chip access and reinforces the case for export controls.

2. **Anthropic CEO calls for pacing frontier AI development, warns of AI-agent-swarm risk**
   - Company: Amazon (matched via `Anthropic` keyword) · Ticker: AMZN US · Tier: 1
   - URL: https://venturebeat.com/security/anthropic-ceo-says-ai-swarm-could-take-over-the-entire-internet-in-6-12-months-commits-to-ai-slowdown-plan
   - Published: ~2026-09-11–12 (corroborated same-day by Axios [2026-09-12] and Daily Caller [2026-09-12] coverage of the same essay)
   - FreshnessCheck: ✅ within rolling 7d window
   - DedupCheck: ✅ URL not in last-7-brief set
   - Verification: Tier 2 — WebSearch snippet
   - Summary: Dario Amodei published "We Must Pace the Frontier," warning a more capable AI-agent swarm could "take over the entire internet" within 6-12 months, and committed Anthropic unilaterally to giving third-party evaluators permanent, employee-level system access as step one of a three-part industry plan.

3. **Google ships a native Gemini desktop app for Windows**
   - Company: Alphabet · Ticker: GOOGL US · Tier: 1
   - URL: https://www.engadget.com/apps/googles-new-windows-app-is-yet-another-way-to-access-gemini-214000564.html
   - Published: 2026-09-10
   - FreshnessCheck: ✅ within rolling 7d window
   - DedupCheck: ✅ URL not in last-7-brief set
   - Verification: Tier 2 — WebSearch snippet
   - Summary: Google released a native Gemini desktop app for Windows 10/11 (Alt+Space quick access), adding video generation and multi-agent workflow features — closing a platform gap versus Anthropic's and OpenAI's existing desktop apps.

4. **Microsoft's Copilot chat goes down for ~100 minutes**
   - Company: Microsoft · Ticker: MSFT US · Tier: 1
   - URL: https://www.theregister.com/ai-and-ml/2026/09/10/ai-uprising-postponed-after-copilot-falls-off-the-web/5295475
   - Published: 2026-09-10
   - FreshnessCheck: ✅ within rolling 7d window
   - DedupCheck: ✅ URL not in last-7-brief set
   - Verification: Tier 2 — WebSearch snippet
   - Summary: copilot.microsoft.com returned Cloudflare Error 1016 for about 1h40m (2225 UTC Sep 9 – 0005 UTC Sep 10); separately, an internal Microsoft 365 Copilot resilience drill briefly knocked out Copilot Chat's suggested-prompt feature for some users, prompting Microsoft to halt the drill and review its procedures.

## Dropped
- Nvidia confirms $12.9B Hugging Face acquisition (techcrunch.com, confirmed 2026-09-03) — Gate A (>7d).
- Nvidia Q2 FY27 earnings ($96.2B revenue) (nvidianews.nvidia.com, 2026-08-26) — Gate A (>7d).
- Tesla: Nevada robotaxi permits for Tesla/Waymo/Aviari (techcrunch.com, 2026-08-20) — Gate A (>7d).
- Tesla: Oct. 1 Roadster event teaser (Bloomberg, 2026-09-12) — dropped: Bloomberg is screening-only per trusted-sources.md; no open-citation outlet carrying this specific item was found.
- Meta: Stilla.ai acquisition (~2026-09-09) — dropped: only Axios/Yahoo Finance/ArcticStartup coverage found, none on trusted-sources.md.
- Microsoft: 26GW/38GW data-center capacity expansion plan (Bloomberg, 2026-09-10) — dropped: Bloomberg screening-only; no open trusted-list outlet had independently confirmed/carried the figure (only aggregators citing "Bloomberg reports" turned up).
- AMD: Goldman Sachs Communacopia conference remarks (2026-09-11) — dropped as analyst-conference commentary, not a discrete news event (Gate D).
- Apple: iOS 27 / Siri AI general rollout — not yet published (ships 2026-09-14, tomorrow).

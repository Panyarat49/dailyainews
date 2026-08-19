# Sources — 2026-08-19 (watchlist)

Generated: 2026-08-19 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel (items_enriched=12>0; most picks from funnel body_text, 2 from funnel description/Tier-2)
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 watchlist briefs (articles/2026-08-08 … 2026-08-14; URLs loaded — no collisions with today's candidates)
TIERS_USED: 1 (Tier 1 alone reached 4 stories; no Tier-2 descent needed)

## Significance ledger (Tier-1 companies scanned)
| Company | Tier | Significant? | Reason | Selected |
|---|---|---|---|---|
| Microsoft | 1 | ✅ Yes | Security researchers social-engineered M365 Copilot into revealing its own exfiltration exploit (credential/data theft risk) | ✅ |
| Nvidia | 1 | ✅ Yes | Analysts: China-made accelerators (Cambricon/Huawei) to hit 90% domestic share, a direct competitive/market-access threat to Nvidia in China | ✅ |
| Alphabet | 1 | ✅ Yes (3 items) | (a) Gemini defaults to reading Workspace business data — privacy/governance; (b) Gemini in Chrome ships to all Android US users w/ agentic auto-browse — product launch; (c) UK govt trial of Google AI for aviation-contrail reduction — applied research/public-sector deal | ✅ (roundup) |
| Tesla | 1 | ✅ Yes | Cybercab (robotaxi) nearing public launch — core to Tesla's autonomy/FSD narrative | ✅ |
| Amazon | 1 | Story exists (rare-book tracking device / AI-training destruction) but funnel body_text and description both returned only site boilerplate/author-bio — no verifiable content | ❌ dropped (no Tier-1/2 evidence) |
| AMD | 1 | Story exists (rack-scale AI energy-efficiency claim) but funnel body_text and description both returned only author-bio boilerplate — no verifiable content | ❌ dropped (no Tier-1/2 evidence) |
| Apple | 1 | Candidates found (image-processing security patch, AirPods-camera leak) but neither is AI-relevant (Gate C) | ❌ dropped (Gate C) |
| Meta Platforms | 1 | Candidates found (ICE-agents-glasses policy memo, addiction-trial) but neither is a genuine AI/tech development (Gate C) / no usable snippet | ❌ dropped (Gate C / no evidence) |
| Alibaba | 1 | Candidate (ShengShu HK IPO) sourced only via Bloomberg (screening) with no open cross-match found in START_POOL | ❌ dropped (screening, no citeable open source) |
| Oracle | 1 | Only candidate was an evergreen how-to blog post, not news | ❌ dropped (not news) |

Tier 2 not consulted — Tier 1 alone reached the `prefer` target (4).

## Selected stories
1. **Microsoft — Copilot social-engineered into revealing its own exploit**
   - Microsoft · MSFT US · Tier 1
   - URL: https://arstechnica.com/security/2026/08/microsoft-copilot-reveals-secret-input-that-allowed-it-to-be-hacked/
   - Published: Tue, 18 Aug 2026 13:00:04 UTC (~10.3h ago)
   - FreshnessCheck: ✅ within 7d window (10.3h) via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 1 — funnel body (extract_status: ok; corroborated by The Register, cluster_size 2)
   - Summary: Security firm Varonis got Microsoft 365 Copilot to describe its own guardrail logic well enough to build a zero-click exploit that exfiltrates user passwords and sensitive data.

2. **Nvidia — China's homegrown AI accelerators to hit 90% domestic share**
   - Nvidia · NVDA US · Tier 1
   - URL: https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-homegrown-ai-accelerators-to-supply-90-percent-of-the-countrys-domestic-market-analysts-suggest-cambricon-and-huawei-expected-to-be-the-biggest-winners-in-the-shift-away-from-nvidia-and-amd
   - Published: Tue, 18 Aug 2026 11:20 UTC (~12h ago)
   - FreshnessCheck: ✅ within 7d window (12h) via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 1 — funnel body (extract_status: ok; corroborated, cluster_size 2)
   - Summary: Analysts project Chinese-made accelerators (led by Cambricon and Huawei) will supply ~90% of China's domestic AI chip market as export controls and Beijing mandates push buyers away from Nvidia and AMD.

3. **Alphabet — roundup (3 items): Workspace AI defaults, Gemini in Chrome, UK contrail-AI trial**
   - Alphabet · GOOGL US · Tier 1
   - 3.1 URL: https://www.zdnet.com/article/googles-ai-can-see-your-business-data-by-default-in-workspace-unless-you-disable-it/ — Published Aug 18, 2026 8:11am PT (~8.2h ago) — Tier 1 funnel body (ok, cluster_size 2) — Gemini has default access to Gmail/Docs/Calendar/Chat in Workspace; admins must opt out.
   - 3.2 URL: https://blog.google/products-and-platforms/products/chrome/gemini-in-chrome-android-auto-browse/ — Published Aug 18, 2026 (~4.2h ago) — Tier 1 funnel body (ok, primary source) — Gemini in Chrome (incl. agentic "auto browse") rolls out to all US Android users.
   - 3.3 URL: https://www.theregister.com/public-sector/2026/08/18/uk-puts-google-ai-on-the-flight-path-to-fewer-contrails/5288516 — Published Tue 18 Aug 2026 11:45 +0200 (~13.6h ago) — Tier 2 — funnel snippet (extract_status: skipped; description substantive & citeable) — UK government trial uses Google AI to predict and reduce contrail formation on North Atlantic flight paths.
   - FreshnessCheck: ✅ all 3 within 7d window
   - DedupCheck: ✅ none of the 3 URLs in last-7-day watchlist set

4. **Tesla — Cybercab nears public launch**
   - Tesla · TSLA US · Tier 1
   - URL: https://www.theverge.com/transportation/981398/tesla-cybercab-launch-robotaxi-fsd-safe-ready
   - Published: 2026-08-18T12:26:29-04:00 (~6.9h ago)
   - FreshnessCheck: ✅ within 7d window (6.9h) via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 2 — funnel snippet (extract_status: skipped; description substantive & citeable, from The Verge)
   - Summary: Tesla's two-seat robotaxi, the Cybercab, is reportedly nearing its public launch, a milestone in Musk's autonomy push.

## Dropped
- Amazon "rare book tracking device" story (tomshardware.com) — Gate: no evidence (funnel body_text and description both boilerplate only)
- AMD "rack-scale AI 4X efficiency" claim (tomshardware.com) — Gate: no evidence (funnel body_text and description both boilerplate only)
- Apple image-processing security patch (theregister.com) — Gate C: not AI-specific
- Apple AirPods-camera macOS leak (techcrunch.com) — Gate C: rumor/leak, not a genuine AI development
- Meta "ICE agents can't wear Meta glasses" (engadget.com) — Gate C: policy/HR memo, not an AI development
- Meta social-media-addiction trial (via BBC/Google News redirect) — no substantive snippet available
- Alibaba "ShengShu HK IPO" — Gate: Bloomberg (screening) only, no open cross-match found in today's START_POOL
- Oracle "How to Build a REST API for an AI Application" (blogs.oracle.com) — not news (evergreen how-to)
- Google/Microsoft "buys Spirit Airlines data for AI training" (tomshardware.com) — Gate: no evidence (body_text empty; description was author-bio only, not article content)
- Remaining candidates (idx 15, 20-23, 26-35, 38-39 in universe_2026-08-19_watchlist.json) — below cut by score/editorial selection or off-watchlist mismatch (e.g. Intel Nova Lake mismatched to Amazon keyword hit)

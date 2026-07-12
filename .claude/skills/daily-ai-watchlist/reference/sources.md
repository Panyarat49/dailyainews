# Sources — 2026-07-12 (watchlist)

Generated: 2026-07-12 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel + search (Nvidia and Micron verified via WebSearch snippet since neither surfaced in the funnel; Microsoft verified from funnel body_text)
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 watchlist briefs (2026-07-05 through 2026-07-11; 37 URLs loaded)
Source mix: 2 citation (CNBC, Tom's Hardware) + 1 citation (Fox Business)
Universe pre-load: 31 candidates from universe_2026-07-12_watchlist.json (generated_at 2026-07-12T06:54:47+07:00) — used as START_POOL; ~30 of 31 candidates were either thematic dedup of already-covered stories (Meta Muse Image removal, Apple v. OpenAI lawsuit — both fully reported in the 2026-07-11 brief) or non-AI/thin snippets, so extensive per-company WebSearch gap-fill was run across nearly all Tier-1 companies and several Tier-2 companies (Nvidia, Tesla, Amazon, Alphabet, Oracle, TSMC, Alibaba, AMD, Apple, Tencent, Xiaomi, Oklo, Netflix, Goldman Sachs, Micron) to reach the floor.
Tiers used: 1+2 | Story count: 3 slots (target 4–5, floor 3 — floor met, not prefer; flagged below)

## Significance ledger
| Company | Tier | Significant? | Reason | Selected |
|---|---|---|---|---|
| Nvidia | 1 | ✅✅✅ | Kyber NVL144 rack-scale system reportedly delayed 12+ months to 2028 (SemiAnalysis); Nvidia publicly denies, "our roadmap is intact"; triggered a multi-country semiconductor supplier stock selloff (Japan's Ibiden, Kingboard, Samsung Electro-Mechanics) | yes (slot 1) |
| Microsoft | 1 | ✅✅ | FY2026 Environmental Sustainability Report: emissions up 25% YoY, driven by AI datacenter buildout; casts doubt on 2030 carbon-negative pledge | yes (slot 2) |
| Micron Technology | 2 | ✅✅✅ | Raised total planned US investment to $250B through 2035 (+$50B) for AI memory/DRAM/HBM capacity; new Clay, NY mega-fab breaks ground ahead of schedule | yes (slot 3, Tier-2 top-up) |
| Meta Platforms | 1 | ◻ dedup | All fresh Meta candidates in today's universe (AP News, TechCrunch, Engadget, Blognone) are the same Muse Image removal story already fully reported in the 2026-07-11 brief — no new development | no |
| Apple | 1 | ◻ dedup | Fresh AP News candidate is the same Apple v. OpenAI trade-secret lawsuit already fully reported in the 2026-07-11 brief; Bloomberg follow-up is screening-only, no open cross-match found | no |
| AMD | 1 | ◻ | Only fresh AMD candidate (Clorox content-creation case study) traced back to a July 2, 2026 publish date on amd.com — outside the freshness window despite recent RSS re-syndication; gaming-GPU price/thermal stories are non-AI | no |
| Alibaba | 1 | ◻ | Fresh candidates were a generic China-ETF investment listicle (not AI-specific) and a $600M DOJ drug-marketplace settlement (not AI-relevant); the PrismML/Qwen-on-iPhone story is genuinely fresh and significant but has no coverage on any trusted-sources.md outlet — rejected per citation rule | no |
| Tesla | 1 | ◻ | Miami robotaxi "unsupervised network" coverage traces back to the July 3 launch already reported in the 2026-07-05 brief — no new development | no |
| Alphabet | 1 | ◻ | No fresh (in-window), non-evergreen Alphabet/Gemini story found on a trusted outlet after gap-fill search | no |
| Oracle | 1 | ◻ | No fresh Oracle story found beyond evergreen monthly product digests of uncertain publish date | no |
| TSMC | 2 | ◻ | CoWoS/packaging coverage found was evergreen background, not a dated fresh event | no |
| Tencent | 2 | ◻ | WeChat "Xiaowei" AI agent coverage traces back to June 22 testing report — outside window | no |
| Affirm | 2 | ◻ | Only candidate (Thai BOT grey-money/BNPL regulation) is non-AI financial regulation | no |

## Tier-descent record
Tier 1 yielded only 2 significant, citable, in-window stories (Nvidia, Microsoft) after dropping thematic-dedup and non-AI candidates. Per `tier_descent: top-up-to-target`, descended to Tier 2 and found Micron's $250B investment announcement — significant, fresh, and citable. Combined total: 3 (floor met). Extensive additional gap-fill searching (15+ targeted queries) across remaining Tier-1 and Tier-2 companies did not surface a 4th story that was simultaneously fresh, genuinely AI-relevant, and citable on a `trusted-sources.md` outlet — shipping 3 rather than reaching for a stale or off-list source.

## Selected stories
1. **Nvidia — Kyber AI rack-scale system reportedly delayed to 2028; Nvidia denies, says roadmap "intact"**
   - Publisher: CNBC (Citation)
   - URL: https://www.cnbc.com/2026/07/06/nvidia-kyber-rack-system-delays-manufacturing-taiwan-rubin-chips-.html
   - Published: Mon, 6 Jul 2026 (per CNBC dateline; multiple outlets corroborate the same week)
   - FreshnessCheck: ✅ within rolling 7d window (~6 days old at time of writing; no fresher trusted follow-up found, but this is the first Nvidia-specific story in the watchlist stream in the last 7 days and remains the most current reporting)
   - DedupCheck: ✅ URL/story not in last-7-day watchlist set
   - Verification: Tier 2 — WebSearch snippet (CNBC not present in the RSS funnel for this story; corroborated independently by SemiAnalysis's original report, Yahoo Finance, Benzinga, wccftech, and the visible stock reaction in Ibiden/Kingboard Laminates/Samsung Electro-Mechanics shares — high cross-outlet consistency on the facts)
   - Summary: Research firm SemiAnalysis reported that Nvidia's next-gen Kyber NVL144 rack-scale system (built for the 2027 Rubin Ultra chip) has slipped over 12 months to 2028 due to manufacturing difficulty with its 78-layer PCB midplane. Nvidia publicly rejected the report: "Our roadmap is intact," noting current Rubin systems are already in full production, shipping to major cloud customers this fall. The rumor briefly hit shares of Asian supply-chain names (Ibiden, Kingboard Laminates, Samsung Electro-Mechanics).

2. **Microsoft — FY2026 sustainability report shows emissions up 25% amid AI datacenter expansion**
   - Publisher: Tom's Hardware (Citation)
   - URL: https://www.tomshardware.com/tech-industry/big-tech/microsoft-struggles-to-fulfill-its-2030-sustainability-promise-amid-carbon-heavy-ai-expansions-the-companys-chief-sustainability-officer-claims-the-target-is-still-feasible
   - Published: Sat, 11 Jul 2026 (article says "Published 11 hours ago" relative to funnel generation time; explicit feed timestamp 12:45 GMT)
   - FreshnessCheck: ✅ within last 24h — explicit body timestamp
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 1 — funnel body (body_text confirms FY2025 emissions rose 25% YoY to ~20.3M metric tons CO2e, up from 16.2M tons in FY2024 and 58% above the 2020 baseline; driven by datacenter buildout and the end of short-term renewable energy certificate purchases; company maintains its 2030 carbon-negative target is still feasible)
   - Summary: Microsoft's 2026 Environmental Sustainability Report shows FY2025 emissions rose 25% year over year, driven primarily by rapid AI datacenter expansion and the company's decision to stop relying on short-term renewable energy certificates. Microsoft's chief sustainability officer maintains the 2030 carbon-negative target remains feasible.

3. **Micron — raises planned US investment to $250B through 2035 for AI memory manufacturing**
   - Publisher: Fox Business (Citation)
   - URL: https://www.foxbusiness.com/media/micron-ceo-says-ai-boom-drives-unprecedented-memory-demand-company-invests-250b
   - Published: Sat, 11 Jul 2026
   - FreshnessCheck: ✅ within last 24h — multiple outlets (Fox Business, Yahoo Finance, Motley Fool, Interesting Engineering, Times Now World) independently dated this to July 11, 2026
   - DedupCheck: ✅ URL/story not in last-7-day watchlist set
   - Verification: Tier 2 — WebSearch snippet (Micron not present in the RSS funnel; verified via strong cross-outlet corroboration — CEO Sanjay Mehrotra's announcement at a Clay, NY event was independently reported with consistent figures by 5+ trusted-adjacent outlets)
   - Summary: Micron raised its total planned US investment to more than $250 billion through 2035 (a ~$50B increase), aimed at scaling DRAM and high-bandwidth memory (HBM) production for AI. The centerpiece is a new multi-fab complex near Syracuse, NY, where the first concrete pour happened more than a quarter ahead of schedule. Micron says it has sold out its 2026 HBM capacity and presold its full 2027 capacity amid what CEO Sanjay Mehrotra calls sustained AI-driven demand.

## Dropped
- https://apnews.com/article/meta-artificial-intelligence-instagram-images-privacy-4df3bdb3fec6e046c6562accc2d270a5 (and 5 more Meta Muse Image variants: TechCrunch, Engadget ×2, Blognone, BBC, Al Jazeera, Fox Business, thenationalnews, ABC AU) — thematic dedup: same Muse Image removal event already fully reported in the 2026-07-11 brief (techcrunch.com/2026/07/10/meta-removes-controversial-ai-feature-on-instagram-after-backlash/ was cited that day); no new development.
- https://apnews.com/article/apple-openai-lawsuit-trade-secrets-theft-6fff8833f5889d86406b89a02dd8fb16 (and CNA, Bloomberg ×2 variants) — thematic dedup: same Apple v. OpenAI trade-secret lawsuit already fully reported in the 2026-07-11 brief.
- https://www.blognone.com/node/151124 (EU Commission probes Meta/Instagram addictive app design under DSA) — Gate C: this is a general platform/UX-addiction regulatory story (infinite scroll, autoplay, notifications), not an AI-specific development; dropped despite being a real, fresh, significant Meta story.
- https://www.tomshardware.com/pc-components/gpus/hotspot-temperature-sensor-on-nvidias-blackwell-gaming-gpus-... and the AMD RX 9070 GRE price-cut story — Gate C: gaming-GPU hardware/pricing, not AI-relevant.
- AMD "Clorox Creates Scalable Content with AMD CPUs and GPUs" (amd.com case study) — traced via search to a July 2, 2026 publish date; outside the 7-day freshness window despite appearing freshly in today's RSS feed (re-syndication, not a new event).
- PrismML shrinks Alibaba's Qwen 3.6 to run on iPhone 17 Pro, drawing Apple's interest — genuinely fresh (~July 9-10) and significant (touches both Alibaba and Apple), but after checking MacRumors, 9to5Mac, TrendForce, MacDailyNews, BigGo Finance, and Mezha, none is on `trusted-sources.md`; The Register's PrismML coverage found was a different (April 2026) story. Rejected per the "cite only outlets on this list" rule — flagged here in case the maintainer wants to add a qualifying outlet.
- Nvidia Blackwell hotspot/thermal + AMD RX 9070 GRE — gaming hardware, non-AI (Gate C).
- Livemint "Want Alibaba, Tencent, Baidu in your portfolio? 5 China ETFs" — investment listicle, not company-specific AI news.
- Thai BOT grey-money/BNPL regulation (Affirm, Tier 2) — non-AI financial regulation (Gate C).
- Remaining low-score/skipped candidates (Microsoft Xbox Brazil court case, Samsung Gallery OneDrive sync end, Amazon layoffs burnout piece, Amazon Echo Studio listing, Bambu Lab/Insta360 contest mis-tagged to Apple) — non-AI or too thin to verify (`extract_status: skipped`, single-line snippet only).

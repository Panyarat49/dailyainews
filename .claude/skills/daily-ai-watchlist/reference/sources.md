# Sources — 2026-09-14 (watchlist)

Generated: 2026-09-14 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: search
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 watchlist briefs (0 overlapping URLs found; most recent on-disk brief is 2026-08-14, outside the 7d window, so RECENT_URLS is effectively empty for this run)
Tiers used: 1+2 (Tier 1 yielded 2 in-window significant stories after extensive gap-fill searches on Microsoft/Amazon/Meta/Tesla/Alibaba/AMD; topped up with 2 Tier-2 stories per `tier_descent: top-up-to-target`)

## Significance ledger
| Company | Tier | Significant? | Reason | Selected |
|---|---|---|---|---|
| Nvidia | 1 | Yes | Major infra/capacity partnership (2GW AI-factory buildout, 8 partners) | ✅ |
| Apple | 1 | Yes | Notable product launch (AI-provenance camera feature, new API) | ✅ |
| TSMC | 2 | Yes | Earnings-adjacent (record monthly revenue, explicit AI-demand driver) | ✅ (top-up) |
| Palantir | 2 | Yes | Major partnership/product (Nvidia-Palantir sovereign AI stack for supply chains) | ✅ (top-up) |
| Microsoft | 1 | No in-window item | Maia 300 chip reveal still "planned for September" per The Information as of Aug 10; no confirmed unveiling found in-window | ❌ dropped (no story) |
| Amazon | 1 | No in-window item | Most recent Anthropic/Trainium capacity news dated April 2026 (out of window); no Sept 7–14 development found | ❌ dropped (no story) |
| Meta Platforms | 1 | No in-window item | Meta Connect 2026 (glasses launch) confirmed for Sept 23–24, outside window; no in-window AI news found | ❌ dropped (no story) |
| Tesla | 1 | No in-window item | Cybercab reveal (Sept 3) and FSD v14.3.9 rollout are outside/at-edge of window with no fresh write-up located | ❌ dropped (no story) |
| Alibaba | 1 | No in-window item | Qwen3.8-Max (Aug 3) and Qwen Conference (May) both outside window; only routine pricing-page snapshot dated Sept 11 found, not a news event | ❌ dropped (no story) |
| AMD | 1 | No in-window item | HUMAIN/Cisco 250MW Instinct deployment dated Sept 1–2, just outside the rolling 7d window | ❌ dropped (freshness) |
| Tencent | 2 | Borderline | Hy4 model's Sept 7 "optimized update" claim sourced only to an unlisted blog (bighatgroup.com); no trusted-source (tencent.com/press, SCMP is explicitly excluded per trusted-sources.md) confirmation with that specific date found | ❌ dropped (unverifiable on allow-list) |

## Tier-descent record
Tier 1 alone produced only 2 verifiable in-window significant stories (Nvidia, Apple) despite per-company gap-fill searches on all 8 remaining Tier-1 names. Descended to Tier 2 per `tier_descent: top-up-to-target`, adding TSMC and Palantir (both Sept 10, both trusted-sourced) to reach 4 stories total (STORY_COUNT `prefer` floor). A 5th (Tencent Hy4) was investigated and dropped for insufficient allow-listed corroboration of its in-window claim; shipping 4 rather than padding with an unverifiable or stale item.

## Selected stories
1. **Nvidia (NVDA US · Tier 1) — NVIDIA expands AI infrastructure capacity in partnership with Australia's data center ecosystem**
   - Publisher: NVIDIA Newsroom (Primary)
   - URL: https://nvidianews.nvidia.com/news/nvidia-expands-ai-infrastructure-capacity-in-partnership-with-australias-data-center-ecosystem
   - Published: 2026-09-10
   - FreshnessCheck: ✅ within rolling 7d window
   - DedupCheck: ✅ not in last-7-brief set
   - Verification: Tier 2 — WebSearch snippet (corroborated by GlobeNewswire wire copy and TechNode Global follow-up)
   - Summary: Nvidia + 8 Australian data-center operators target up to 2GW combined "AI factory" capacity by 2027.

2. **Apple (AAPL US · Tier 1) — Apple has a new way to prove your iPhone photos aren't AI slop**
   - Publisher: TechCrunch (Citation)
   - URL: https://techcrunch.com/2026/09/09/apple-has-a-new-way-prove-your-iphone-photos-arent-ai-slop/
   - Published: 2026-09-09
   - FreshnessCheck: ✅ within window
   - DedupCheck: ✅ not in last-7-brief set
   - Verification: Tier 2 — WebSearch snippet (corroborated by Nieman Journalism Lab, Zamin.uz)
   - Summary: Apple's "Apple Reference Image" on iPhone 18 Pro creates a signed, unalterable "digital negative" via Private Cloud Compute to verify whether a photo was AI-edited; will support SynthID.

3. **TSMC (TSM US · Tier 2) — TSMC sees August revenue surge 53.3% to record high on AI chip demand**
   - Publisher: CNBC (Citation); also Focus Taiwan (Citation)
   - URL: https://www.cnbc.com/2026/09/10/tsmc-august-revenue-chip-ai.html
   - Published: 2026-09-10
   - FreshnessCheck: ✅ within window
   - DedupCheck: ✅ not in last-7-brief set
   - Verification: Tier 2 — WebSearch snippet, corroborated across two allow-listed outlets (CNBC + Focus Taiwan)
   - Summary: TSMC posted record August revenue of NT$514.8B (~US$16.35B), up 53.3% YoY and 10.1% MoM, its fourth straight month of growth, driven by AI-server and advanced-node (3nm/5nm) demand that kept capacity fully booked.

4. **Palantir (PLTR US · Tier 2) — NVIDIA and Palantir bring Sovereign Intelligence to critical supply chains**
   - Publisher: NVIDIA Newsroom (Primary)
   - URL: https://nvidianews.nvidia.com/news/nvidia-and-palantir-bring-sovereign-intelligence-to-critical-supply-chains
   - Published: 2026-09-10
   - FreshnessCheck: ✅ within window
   - DedupCheck: ✅ not in last-7-brief set
   - Verification: Tier 2 — WebSearch snippet (corroborated by BusinessWire wire copy and HPCwire/AIwire)
   - Summary: Nvidia and Palantir built a joint AI stack — Nvidia Nemotron open models running inside Palantir Foundry/AIP on the Palantir Ontology — first deployed inside Nvidia's own supply chain, then offered to manufacturing/pharma/agriculture/government customers.

## Dropped
- Microsoft Maia 300 — still reported as "planned for September," no confirmed reveal in-window; kept watching.
- Amazon $5B/$20B Anthropic investment — real but dated 2026-04-20, far outside the 7d window.
- Alphabet–Blackstone $25B TPU venture — dated 2026-05-19, outside window.
- AMD/Cisco/HUMAIN 250MW Saudi deployment — dated 2026-09-01/02, just outside the rolling 7d window (cutoff 2026-09-07).
- Tencent Hunyuan Hy4 "Sept 7 optimized update" — claim only found on a non-allow-listed blog (bighatgroup.com); Tencent's own Aug 28 launch post and SCMP coverage are both outside window or off-allow-list (SCMP explicitly excluded per trusted-sources.md China-concentration note).
- Tesla Cybercab reveal — dated 2026-09-03, outside window.

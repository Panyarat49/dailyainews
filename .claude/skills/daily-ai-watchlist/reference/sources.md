# Sources — 2026-08-17 (watchlist)

Generated: 2026-08-17 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel (mixed Tier 1 funnel body + Tier 2 funnel snippet; 12/29 items_enriched, funnel ran in GitHub Actions with open egress)
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok) — all selected stories are <24h old
Dedup against: last 7 watchlist briefs (35 URLs loaded, 2026-08-08 → 2026-08-14)
TIERS_USED: 1 (Tier 1 alone reached STORY_COUNT prefer=4; Tier 2 not invoked)
Companies with significant news today: Alphabet, Meta Platforms, Amazon (Anthropic-related, roundup), Nvidia

## Significance ledger
| Company | Tier | Significant? | Reason | Selected |
|---|---|---|---|---|
| Alphabet | 1 | Yes | Reported Google/AMD collaboration on next-gen (v10) custom TPU — chip/compute significance | ✅ single |
| Meta Platforms | 1 | Yes | Zuckerberg's AI-future manifesto draws public/press skepticism — notable business narrative | ✅ single |
| Amazon | 1 | Yes | Cluster of Anthropic-related developments (Amazon is Anthropic's largest backer/compute partner): CEO industry-trust remarks, first AI protester jailed (names Anthropic), watermark technical explainer | ✅ roundup ×3 |
| Nvidia | 1 | Yes (moderate) | RTX Pro 6000 Blackwell workstation-GPU price hike reflects AI-chip demand/supply dynamics | ✅ single |
| Nvidia (Ohio/OpenAI funding) | 1 | Yes (high) but undercited | WSJ/Reuters-reported scale-back of Nvidia's OpenAI Ohio data-center funding guarantee — highly significant, but only reachable via a `news.google.com` redirect (unresolved) and off-allowlist mirrors (Yahoo Finance, Seeking Alpha, etc.); no allowlisted source had a fetchable body or substantive snippet | ❌ dropped — no citeable source (see Dropped) |
| AMD | 1 | No | Candidates were false keyword matches (CD/DVD drive deal, OLED burn-in test mentioning "AMD" only incidentally) | ❌ not AI/company-relevant |
| Apple | 1 | No | Candidates were CarPlay-vs-Android-Auto and iPhone-leasing pieces — no AI content | ❌ Gate C fail |
| Tesla, Microsoft, Oracle, Alibaba | 1 | No | No in-window candidate in START_POOL; supplemental WebSearch (Copilot/Azure, Tesla FSD/Optimus, AMD Instinct) returned only stale/undated recap content, nothing fresh | ❌ none found |
| Tier 2 (all) | 2 | N/A | Not invoked — Tier 1 alone reached STORY_COUNT prefer (4) | — |

## Tier-descent record
Tier 1 candidates alone filled 4 of 4 target slots (prefer=4). Tier 2 top-up was not needed and not run.

## Selected stories
1. **Alphabet (GOOGL US · Tier 1) — Google reportedly taps AMD to design next-generation TPU**
   - URL: https://www.tomshardware.com/tech-industry/artificial-intelligence/google-reportedly-taps-amd-to-design-next-generation-tpu-hybrid-ai-asic-could-integrate-on-package-cpu-cores-for-reinforcement-learning
   - Published: Sun, 16 Aug 2026 12:40:00 +0000 (~10.6h old)
   - FreshnessCheck: ✅ | DedupCheck: ✅ not in last-7-brief set
   - Verification: Tier 1 — funnel body
   - Summary: Per a SemiAnalysis client note, Google is working with AMD on its 10th-gen TPU, potentially folding AMD CPU cores onto the package for CPU-heavy/RL workloads — AMD's first known role in a custom AI ASIC.

2. **Meta Platforms (META US · Tier 1) — Why people aren't buying Mark Zuckerberg's AI future**
   - URL: https://techcrunch.com/2026/08/16/why-people-arent-buying-mark-zuckerbergs-ai-future/
   - Published: Sun, 16 Aug 2026 20:32:01 +0000 (~2.8h old)
   - FreshnessCheck: ✅ | DedupCheck: ✅ not in last-7-brief set
   - Verification: Tier 1 — funnel body
   - Summary: Zuckerberg's 6,500-word "The Future is for Everyone" manifesto promising a personal AI agent for everyone drew skepticism from TechCrunch's Equity podcast hosts, who contrasted his optimism with Anthropic CEO Dario Amodei's more cautious tone and Meta's trust-eroding history.

3. **Amazon (AMZN US · Tier 1) — อัปเดตสำคัญ 3 รายการ (Anthropic ecosystem)**
   - 3.1 **Anthropic CEO says AI backlash is "fundamentally a crisis of trust"** — https://techcrunch.com/2026/08/16/anthropic-ceo-says-ai-backlash-is-fundamentally-a-crisis-of-trust/ — Published Sun 16 Aug 2026 16:53:51 +0000 (~6.4h) — Tier 1 funnel body.
   - 3.2 **The first anti-AI protester to be jailed has a message for OpenAI, Anthropic and Meta** — https://www.theguardian.com/us-news/2026/aug/16/california-openai-protester-wynd-kaufman — Published Sun 16 Aug 2026 08:00:00 GMT (~15.3h) — Tier 1 funnel body.
   - 3.3 **Anthropic อธิบายการทำงานของลายน้ำในข้อความเพิ่มเติม** — https://www.blognone.com/node/151387 — Published Sun 16 Aug 2026 04:13:13 +0000 (~19.1h) — Tier 2 funnel snippet.
   - FreshnessCheck: ✅ all three | DedupCheck: ✅ none in last-7-brief set
   - Note: matched to Amazon via the watchlist's "Anthropic" keyword (Amazon is Anthropic's largest strategic backer/compute partner, per `watchlist.json`).

4. **Nvidia (NVDA US · Tier 1) — NVIDIA ขึ้นราคา RTX Pro 6000 Blackwell เป็น 16,000 ดอลลาร์**
   - URL: https://www.blognone.com/node/151385
   - Published: Sun, 16 Aug 2026 03:02:04 +0000 (~20.3h old)
   - FreshnessCheck: ✅ | DedupCheck: ✅ not in last-7-brief set
   - Verification: Tier 2 — funnel snippet
   - Summary: Videocardz found Nvidia raised the listed price of its RTX Pro 6000 Blackwell workstation GPU to $16,000 — nearly double its launch price — the second hike in a short span.

## Dropped
- https://news.google.com/rss/articles/...OZ68cDfnsHeN... (Nvidia scales back funding guarantee for Ohio OpenAI data center, WSJ/Reuters) — no citeable source: only reachable via unresolved `news.google.com` redirect + off-allowlist mirrors (Yahoo Finance, Seeking Alpha, americanbazaaronline, etc.); funnel `description` was just the headline repeated, no substantive snippet; WebFetch blocked this session. Highly significant but undercited — flagged for tomorrow if a trusted outlet (Reuters/AP/CNBC) publishes its own write-up.
- https://news.google.com/rss/articles/...OqwNYX3aPRP8Y... (Nebius and CoreWeave Tout Short-Term Cloud Deals, While AWS Goes Long, The Information) — Gate: Screening-only source (theinformation.com is discovery-only per trusted-sources.md); no open-citation outlet found carrying the same specific comparison; description had no substantive snippet either.
- https://news.google.com/rss/articles/...MwUN5BsdihMQi... (AI News Tracker: Zuckerberg manifesto + EU AI Act, livemint.com) — near-duplicate of selected story #2 (same underlying Zuckerberg manifesto); funnel snippet was headline-only, insufficient for independent Tier-2 citation.
- https://www.engadget.com/2234248/android-auto-vs-apple-carplay-features-comparison/ (Apple) — Gate C: not AI-relevant (infotainment feature comparison).
- https://www.engadget.com/2234247/how-to-lease-iphone-instead-of-buying/ (Apple) — Gate C: not AI-relevant.
- https://www.theverge.com/tech/980752/amazon-class-action-arbitration-terms-and-conditions (Amazon) — Gate C: legal/arbitration story, no AI angle.
- https://www.tomshardware.com/pc-components/cpus/intel-says-it-will-launch-new-core-with-nova-lake-on-desktop-first... (mismatched to Amazon via "AMD" keyword collision) — Gate W: not actually about Amazon; also not AI-specific.
- https://www.tomshardware.com/pc-components/this-portable-external-cd-dvd-drive-comes-with-a-2-5-inch-sata... (mismatched to AMD) — Gate W/C: false keyword match, unrelated product.
- https://www.tomshardware.com/monitors/modern-oled-tvs-are-just-as-susceptible-to-burn-in... (mismatched to AMD) — Gate C: not AI-relevant.
- https://www.tomshardware.com/pc-components/gpus/thieves-swap-rtx-5080-gpus-for-rtx-3060s-in-chinese-gaming-hotels... (mismatched to AMD, actually Nvidia hardware theft) — Gate C: not a genuine AI development, novelty crime story.
- https://www.engadget.com/2236816/turn-on-settings-protect-android-phone-from-theft/ (Alphabet) — Gate C: not AI-relevant.
- https://www.engadget.com/2236808/might-want-to-skip-newegg-gpu-trade-in-program-reasons/ (Nvidia) — Gate C: consumer retail program, not an AI development.
- https://www.zdnet.com/article/google-pixel-11-pro-vs-apple-iphone-17-pro/, .../google-pixel-11-pro-hilight-feature-android-golden-days/, .../google-pixel-11-vs-pixel-9/ (Alphabet) — Gate C: hardware/feature comparisons, not genuine AI-development news.
- https://blog.google/products-and-platforms/devices/pixel/pixel-11-features/ (Alphabet) — deprioritized: consumer hardware launch roundup, not primarily an AI development (lower significance than the selected TPU/AMD story for the single Alphabet slot).
- https://venturebeat.com/orchestration/deepseeks-top-ranked-v4-flash-stumbles-on-real-agent-tasks-as-its-prices-surge (mismatched to Alphabet) — Gate W: story is about DeepSeek, not a watchlist company.
- https://www.engadget.com/2236802/dolby-vision-on-netflix-things-needed-first/, https://www.blognone.com/node/151392 (Netflix, Tier 2) — Gate C: not AI-relevant; also Tier 2 not needed since Tier 1 reached target.
- https://www.theverge.com/gadgets/980448/polaroid-go-second-generation-film-pack-bundle-deal-sale (mismatched to Amazon) — Gate W/C: unrelated retail deal.

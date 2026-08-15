# Sources — 2026-08-15 (watchlist)

Generated: 2026-08-15 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel (most picks verified from funnel body_text; items_enriched=10>0)
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok) — all selected stories within 24h
Dedup against: last 7 watchlist briefs (2026-08-08 → 2026-08-14; 30 URLs loaded)
Tiers used: 1 (no Tier-2 descent needed)
Story count: 3 (floor `min`) — the Apple/Alibaba China-AI-model story (funnel score 7.25) was investigated at length but every source repeating it (The Verge, Reuters, CNBC, TechCrunch) reached this session only via unresolvable news.google.com redirect links (WebFetch blocked, so the redirect could not be resolved to a citeable direct URL, and WebSearch could not surface the direct article URL either). Per the engine's no-fabrication rule, an uncitable story is dropped rather than shipped with a broken/indirect link. No other Tier-1/2 company had a fresh (≤24h), significant, directly-citeable item today after gap-fill search, so the brief ships 3 stories (meets floor, does not reach the 4 preferred).

## Significance ledger
| Company | Tier | Significant? | Reason | Selected |
|---|---|---|---|---|
| Alphabet | 1 | Yes | Product policy change (watermark toggle) + Waymo service-area expansion — same-day double | ✅ roundup (2 items) |
| Apple | 1 | Yes | New AI model developed with Alibaba for China market — cross-border partnership | ✅ |
| Nvidia | 1 | Yes | Security/geopolitical: Nvidia chip found in Russian weapon | ✅ |
| Amazon | 1 | Yes | AI market competition affecting Amazon-backed Anthropic (price war) | ✅ (via Anthropic keyword) |
| Meta Platforms | 1 | No | Only opinion/podcast pieces surfaced today ("does Zuckerberg believe...", Instagram-logo podcast) — dropped as pure commentary | ❌ |
| Oracle | 1 | No | Only a broken tutorial page (blogs.oracle.com 5xx) and a screening-only Bloomberg pipeline-delay item with no open cross-match reachable (WebFetch blocked) | ❌ |
| Microsoft | 1 | No | Available items (KBank Thai partnership; multi-company layoffs listicle) are minor/off-scope; the one major-looking item (Maia 300 chip reveal) is a rehash of the 2026-08-11 brief's story, not new | ❌ |
| Alibaba | 1 | Partial | Only distinct item was an AMD devrel blog post (Qwen on Ryzen AI) — folded into the Apple story instead (Apple partnered with Alibaba on the China AI model) rather than given its own thin slot | folded into Apple story |
| Tesla, Microsoft(chip), AMD, TSMC | 1/2 | No | No fresh (≤24h), on-list, non-duplicate items found via funnel + WebSearch gap-fill (Maia 300/TSMC story traces to an Aug 10 report, outside WINDOW as fresh reporting) | ❌ |

## Tier-descent record
Tier 1 alone produced 3 qualifying, directly-citeable company slots (Alphabet, Nvidia, Amazon). A 4th (Apple/Alibaba China AI model) was significant and fresh but had no resolvable direct URL (see story-count note above) and was dropped. Tier-2 descent was attempted via WebSearch gap-fill (Microsoft/TSMC/Tesla/AMD/Meta) but the strongest candidate found (Microsoft Maia 300 chip reveal) traces back to an Aug 10 report already covered in the 2026-08-11 brief — not a fresh write-up — and Meta/Tesla items found were either older manifesto coverage or product-update trackers with no single fresh news event. Shipping 3 stories (floor `min`, below the 4–5 target — genuine shortfall after real search effort).

## Selected stories
1. **Alphabet (GOOGL US · Tier 1) — อัปเดตสำคัญ 2 รายการ**
   - 1.1 Google removes visible AI watermarks
     - URL: https://www.engadget.com/2237340/google-will-now-allow-users-to-remove-visible-watermarks-from-ai-content/
     - Published: Fri, 14 Aug 2026 19:04:42 +0000 (~4.2h ago)
     - Verification: Tier 1 — funnel body
   - 1.2 Waymo gets permission to expand robotaxi rides to Sacramento and San Diego
     - URL: https://www.engadget.com/2237530/waymo-receives-permission-to-offer-rides-in-sacramento-and-san-diego/
     - Published: Fri, 14 Aug 2026 22:50:04 +0000 (~0.5h ago)
     - Verification: Tier 2 — funnel snippet (description: "The company will also be able to expand its fleet across more of the San Francisco Bay Area and Los Angeles.")
   - DedupCheck: ✅ both URLs not in last-7-day set

2. **Nvidia (NVDA US · Tier 1) — Nvidia Jetson chip found in Russian cruise missile**
   - URL: https://www.theregister.com/offbeat/2026/08/14/russian-missile-uses-nvidia-ai-chip-to-help-target-ukraine/5287976 (corroborated: tomshardware.com)
   - Published: Fri, 14 Aug 2026 18:52:51 +0200 (~6.4h ago)
   - FreshnessCheck: ✅ within last 24h
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Ukraine's GUR says it recovered an Nvidia Jetson Orin module from a downed Russian S-71 "Monochrome" cruise missile, despite Nvidia's 2022 Russia exit and sanctions.

3. **Amazon (AMZN US · Tier 1, via Anthropic) — OpenAI and Anthropic in price war as Chinese AI rivals gain ground**
   - URL: https://arstechnica.com/ai/2026/08/openai-and-anthropic-in-price-war-as-chinese-ai-rivals-gain-ground/
   - Published: Fri, 14 Aug 2026 14:27:14 +0000 (~8.9h ago)
   - FreshnessCheck: ✅ within last 24h
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Anthropic (Amazon-backed) is cutting prices — launching Claude Opus 5 as cheaper "frontier intelligence" than Fable 5 — alongside OpenAI's 80% GPT-5.6 Luna price cut, both defending share against Chinese rivals Moonshot and DeepSeek.

## Dropped
- theverge.com "Apple trained its own AI model for China with help from Alibaba" (Apple, funnel score 7.25, body_text verified) — significant and fresh (~14h), but every path to it (funnel URL, WebSearch results for Reuters/CNBC/TechCrunch/The Verge coverage) resolved only to a news.google.com redirect or a non-trusted aggregator (Rappler, MacRumors, Japan Times, Quartz, etc.); with WebFetch blocked the redirect could not be resolved to the real theverge.com/reuters.com URL. Dropped per no-fabrication rule rather than cited via redirect or an off-allowlist mirror.
- techcrunch.com "Does Mark Zuckerberg really believe AI is for everyone?" (Meta) — Gate D: pure opinion/video commentary.
- theverge.com Instagram-logo Vergecast podcast (Meta) — Gate D: not a news event.
- blogs.oracle.com PL/SQL tutorials (Oracle, x2) — Gate D: how-to content, and one URL 5xx'd on the funnel fetch.
- bloomberg.com "New Mexico Gas Pipeline for Oracle Data Center Delayed to 2027" (Oracle) — Screening-only source; no open cross-match reachable with WebFetch blocked.
- bloomberg.com "Nvidia's $500 Billion Plan Envelops Wall Street in Its AI Frenzy" (Nvidia) — Screening-only + same underlying $500B financing story already covered in 2026-08-11/2026-08-14 briefs.
- news.microsoft.com "KBank and Central Pattana Unveil 'Human + AI' Strategies" (Microsoft) — thin partner PR, below significance bar with a stronger Nvidia/Apple/Alphabet/Amazon slate available.
- livemint.com "Tech layoffs 2026... Meta, Microsoft take lead" (Microsoft) — multi-company listicle, no Microsoft-specific substantive detail in the accessible snippet.
- Microsoft Maia 300 AI chip / TSMC capacity story (WebSearch gap-fill) — Gate A: traces to an Aug 10 report (The Information), already covered in the 2026-08-11 brief; not a fresh write-up.
- amd.com "Run Qwen 3.8 27B on AMD Ryzen AI Max Agentic PCs" (Alibaba) — thin devrel post; Alibaba's role folded into the Apple story instead.

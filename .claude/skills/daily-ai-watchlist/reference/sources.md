# Sources — 2026-07-13 (watchlist)

Generated: 2026-07-13 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel + WebSearch cross-check
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 watchlist briefs (URLs loaded from Jul 6–12)
Source mix: 2 citation (The Verge, CNBC) + 1 citation (The Register, via ainews universe cross-load)
Universe pre-load: 21 candidates from universe_2026-07-13_watchlist.json (generated_at 2026-07-13T06:53:05+07:00) — after applying Gate C (genuine AI/tech relevance) most of the 21 candidates failed (Xbox lawsuit, email-hosting roundup, gadget deals, Apple Pencil, Apple-1 auction, celebrity-opinion glasses reaction, Bloomberg screening items with no open cross-match) — only 2 Tier-1 candidates survived. Supplemented with ~9 targeted WebSearch gap-fill queries (Nvidia, Microsoft, Alphabet, Amazon, Oracle, Alibaba, AMD, Goldman Sachs Chinese-AI-models) per SEARCH_STRATEGY step 3; none returned a single clearly-dated (≤24h), trusted, non-aggregated article beyond what the funnel already had. One Tier-2 story (Micron) was cross-loaded from the same-day `universe_2026-07-13_ainews.json` funnel run (it explicitly names Micron/HBM and was already Tier-1-verified there) since the watchlist funnel run didn't happen to surface it. WebFetch control probe returned 403 (WEBFETCH_BLOCKED).
Tiers used: 1+2 | Story count: 3 slots (target 4–5, floor 3 — floor met, shortfall flagged below)

## Significance ledger
| Company | Tier | Significant? | Reason | Selected |
|---|---|---|---|---|
| Apple | 1 | ✅ | Self-driving car program's AI-silicon legacy now driving M7 Ultra chip (up to 1.5TB RAM) — notable R&D/product angle | yes (slot 1) |
| Tesla | 1 | ✅ | Musk (Tesla/SpaceX CEO) vs. Altman public spat on X, triggered by Apple's trade-secret lawsuit against OpenAI — genuine new AI-industry dispute, not a rehash | yes (slot 2) |
| Micron Technology | 2 | ✅ | AI-datacenter demand tripled SK Hynix/Micron revenue, ~doubled Samsung's; boom-bust structural risk — chips/capacity angle | yes (slot 3, top-up) |
| Meta Platforms | 1 | ◻ | Only candidate was Lorde's "not sexy" quip about Ray-Ban Meta AI glasses at a concert — celebrity-opinion reaction, Gate D drop (not a reportable development) | no |
| Alphabet | 1 | ◻ | "Lawyer who took on Meta and Google" story is a social-media-addiction lawsuit, not an AI-specific story — Gate C fail; "AI News Tracker" livemint roundup item had no substantive funnel snippet and no reliably-dated standalone source found | no |
| Nvidia | 1 | ◻ | Only candidate was a Lenovo Legion 7a gaming-laptop SKU/pricing story with incidental "Ryzen AI 9" branding — Gate C fail (not a genuine Nvidia AI development) | no |
| Microsoft | 1 | ◻ | Only candidates were an Xbox account-restoration lawsuit and an "email hosting" buyer's guide — neither AI-relevant (Gate C fail); WebSearch gap-fill surfaced only vague, undated market-commentary aggregations | no |
| Amazon | 1 | ◻ | Only candidate was an Asus SSD-enclosure deal post — not AI-relevant (Gate C fail) | no |
| Alibaba | 1 | ◻ | No fresh candidate in funnel; WebSearch gap-fill surfaced only older Qwen Conference/Qwen Cloud coverage, no dated ≤24h item | no |
| AMD | 1 | ◻ | No fresh candidate in funnel; WebSearch gap-fill surfaced only generic, undated stock-commentary aggregations (no single citable dated article) | no |
| Goldman Sachs | 2 | ◻ | "Goldman Sachs picks its favorite Chinese AI models" (CNBC, published_raw within window) had no substantive funnel snippet; WebSearch could not pin a specific July 12/13 CNBC article distinct from earlier (May/June/July 9) Goldman China-AI reports — too much risk of citing a rehash as new | no |
| Xiaomi | 2 | ◻ | "Why Xiaomi phones aren't banned" is a US-market-access/tariff explainer, only tangentially AI — Gate C marginal, deprioritized below the 3 selected | no |

## Tier-descent record
Tier 1 (after Gate C) yielded only 2 citable significant stories (Apple, Tesla) — well short of `prefer` (4). Per `tier_descent: top-up-to-target`, descended to Tier 2 and added Micron (funnel-verified via the ainews-stream universe file, since the watchlist-stream funnel didn't surface it this run). Extensive WebSearch gap-fill (9 queries covering Nvidia, Microsoft, Alphabet, Amazon, Oracle, Alibaba, AMD, Goldman Sachs) failed to produce any additional clearly-dated (≤24h), non-aggregated, trusted-source story — WebFetch is blocked this run so none of the WebSearch snippets could be verified against a real article body/timestamp beyond the snippet text itself, and several were visibly generic/aggregated (no single dated URL). Rather than risk citing a stale rehash or an unverifiable aggregation, story count is shipped at the floor (3) with this shortfall flagged, per engine Step 1c ("ship fewer, record the gate breakdown") rather than padding.

## Selected stories
1. **Apple — self-driving car program's AI-silicon legacy drives M7 Ultra**
   - Publisher: The Verge (Citation)
   - URL: https://www.theverge.com/tech/964519/apple-silicon-self-driving-car-ai-m7-ultra
   - Published: 2026-07-12T12:27:06-04:00
   - FreshnessCheck: ✅ within 24h via funnel body_text timestamp
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 1 — funnel body
   - Summary: Apple's shelved self-driving car project drove early investment in on-device AI silicon; that legacy is now accelerating the M7 Ultra chip, reportedly able to support up to 1.5TB of RAM. (Corroborating angle: Bloomberg's "Apple's M6, M7 and M8 Chips Show How AI Is Reshaping the Company" — screening-only, not separately cited.)

2. **Tesla — Musk and Altman spar on X after Apple's OpenAI trade-secret lawsuit**
   - Publisher: CNBC (Citation)
   - URL (funnel/Google News): https://news.google.com/rss/articles/CBMidkFVX3lxTE9SLXZXRVdMZTFEOGZXeklZZ08teGV4cDBzX0QwamVMaXJwWjRxdjlyeFdEU25HTktDVEpjSHRxZkpBSkR3YmYzV0VvOHptNVV2Wi1INmpkdEpFcW1TTjNhMFRmSWFDbjluM1BJQms2QTEwMkxtTmc?oc=5
   - Resolved URL: https://www.cnbc.com/2026/07/12/elon-musk-and-sam-altman-spar-.html
   - Published: Sun, 12 Jul 2026 15:32:34 GMT
   - FreshnessCheck: ✅ within 24h via funnel body_text timestamp ("PUBLISHED SUN, JUL 12 2026 11:32 AM EDT")
   - DedupCheck: ✅ URL not in last-7-day watchlist set (2026-07-11-watchlist covered a different URL — theverge.com/tech/964350/apple-openai-lawsuit-trade-secrets — on the lawsuit filing itself; this is a distinct, later development: the Musk/Altman public reaction to it)
   - Verification: Tier 1 — funnel body
   - Summary: Elon Musk and Sam Altman traded barbs on X after Apple sued OpenAI for alleged trade-secret theft, reigniting their long-running dispute over OpenAI's for-profit transition (Musk left OpenAI's board in 2018; lost a related lawsuit against Altman earlier this year and is appealing).

3. **Micron Technology — AI-datacenter demand drives record memory revenue, boom-bust risk looms**
   - Publisher: The Register (Citation)
   - URL: https://www.theregister.com/ai-and-ml/2026/07/12/memory-makers-are-slaves-to-the-boom-bust-rollercoaster-and-the-ai-boom-is-the-wildest-ride-of-all/5269549
   - Published: Sun, 12 Jul 2026 13:04:00 +0200
   - FreshnessCheck: ✅ within 24h via funnel published_raw timestamp
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 2 — funnel snippet (body_text was a bot-check interstitial, not real content; RSS description is substantive and used instead; cross-loaded from the same-day ainews-stream universe file where it was also selected)
   - Summary: AI-datacenter demand tripled SK Hynix and Micron revenue and roughly doubled Samsung's over the past year, but the memory market's historic boom-bust cycle means the current windfall carries real reversal risk.

## Dropped
- tomshardware.com Lenovo Legion 7a RTX 5070 laptop (Nvidia, score 6.01) — Gate C: gaming-laptop SKU/pricing story, only incidental "Ryzen AI 9" branding, not a genuine Nvidia AI development.
- theverge.com "Lorde says Ray-Ban Meta AI glasses are 'not sexy'" (Meta, score 6.03) — Gate D: celebrity-opinion reaction at a concert, not a reportable AI/business development.
- news.google.com redirect → The Guardian "the lawyer who took on Meta and Google – and won" (Alphabet, score 5.9) — Gate C: social-media-addiction lawsuit story, not AI-specific.
- news.google.com redirect → Bloomberg "OpenAI, Meta, SpaceXAI Compete for More Cost-Efficient AI Models" (Meta, score 4.74) — screening source, body_text empty, no open-citation cross-match found.
- news.google.com redirect → Bloomberg "Apple's M6, M7 and M8 Chips Show How AI Is Reshaping the Company" (Apple, score 3.94) — screening source, body_text empty; same underlying theme as the selected Verge story, treated as corroboration rather than a separate citation.
- news.google.com redirect → thenationalnews.com "Meta's Muse AI disaster exposes Big Tech's costly pattern of getting things wrong" (Meta, score 4.45) — funnel description not substantive (headline only); topic (Muse AI backlash) already extensively covered in 2026-07-08/07-10/07-11 watchlist briefs — dropped for redundancy risk plus lack of citable new detail.
- news.google.com redirect → livemint.com "'LOL, I found out I can access...': Apple points to former employer's message in lawsuit against OpenAI" (Apple, score 4.44) — funnel description not substantive; WebSearch corroboration traced the "Chang Liu" detail to the original July 10 lawsuit-filing coverage (Axios/CNBC/TechCrunch/9to5Mac), already reflected in the 2026-07-11 watchlist brief — likely a derivative rehash rather than a fresh development, dropped to avoid double-counting the same underlying event.
- news.google.com redirect → CNBC "Goldman Sachs picks its favorite Chinese AI models" (Goldman Sachs, Tier 2, score 4.56) — funnel description not substantive; WebSearch could not confirm a distinct July 12 article separate from earlier (May 18 / June 3 / July 9) Goldman China-AI coverage.
- engadget.com "Why Xiaomi phones aren't banned, but are rarely sold in the US" (Xiaomi, Tier 2, score 4.09) — Gate C marginal (US market-access/tariff explainer, only tangentially AI); deprioritized.
- techcrunch.com "TechCrunch Mobility: A robotaxi ultimatum" (Tesla, score 4.84) — content is centered on the Uber–Waymo robotaxi partnership ending and an NHTSA directive to AV developers generally, not Tesla specifically; Gate W too marginal to select over the stronger Tesla item.
- Other lower-score START_POOL items (Xbox lawsuit, email-hosting buyer's guide, SteelSeries headset deal, Apple Pencil repairability rumor, Sotheby's Apple-1 auction, "AI News Tracker" livemint roundup) — Gate C fail (not genuine AI/tech developments) or no substantive citable content.

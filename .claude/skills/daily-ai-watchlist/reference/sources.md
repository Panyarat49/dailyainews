# Sources — 2026-07-10 (watchlist)

Generated: 2026-07-10 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 watchlist briefs (07-09, 07-08, 07-07, 07-06, 07-05, 07-04, 07-03 all read) — ~30 URLs loaded
Universe pre-load: 40+ candidates from universe_2026-07-10_watchlist.json (generated_at 2026-07-10T07:03:51+07:00) — used as START_POOL; supplemented with targeted gap-fill WebSearch for Tier-1 companies not yet covered (Nvidia, Tesla, Apple, Oracle, Amazon, Alibaba, AMD) per SEARCH_STRATEGY step 3
Source mix: TechCrunch ×2 (+1 secondary), OpenAI (primary), The Verge, Engadget (via WebSearch gap-fill), Reuters (secondary)
Tiers used: 1 | Story count: 4 slots (target 4–5, floor 3 — met; Tier 1 only, no descent needed)

## Significance ledger
| Company | Tier | Significant? | Reason | Selected |
|---|---|---|---|---|
| Meta Platforms | 1 | ✅✅✅ | Three distinct AI/tech developments same day: Instagram-photo consent backlash over Muse Image (cluster_size 7, high corroboration), AI chip production starting September doubling compute capacity, Muse Spark 1.1 agentic-coding model opened via API for the first time | yes (roundup, slot 1, 3 sub-items) |
| Microsoft | 1 | ✅✅ | GPT-5.6 becomes the new preferred model across Microsoft 365 Copilot (Word/Excel/PowerPoint/Chat/Cowork) — major product integration announced directly by OpenAI | yes (slot 2) |
| Alphabet | 1 | ✅ | Google auto-labels AI-generated/edited ads in My Ad Center across Search/Discover/YouTube — transparency feature with regulatory-adjacent significance | yes (slot 3) |
| Alibaba | 1 | ✅ | Federal judge paused a Pentagon rule barring DoD from working with lobbyists tied to 1260H-listed firms, giving Alibaba a temporary reprieve on its Washington lobbying operation — legal/export-control development touching an AI-designated company | yes (slot 4) |
| Nvidia | 1 | ❌ (thin) | Only candidate found: GeForce NOW Toronto server expansion (minor cloud-gaming infra update, low AI significance); gap-fill WebSearch surfaced only stock-price commentary, no fresh substantive story | no |
| Tesla | 1 | ❌ (sourcing) | Gap-fill found a genuine story (Tesla capping employee AI-coding-tool spend at $200/week, xAI exempted) but could not locate it on any trusted-sources.md outlet — all hits (Electrek, TechTimes, IBTimes, etc.) are off-allowlist; dropped rather than cite an unlisted source. Separate "Musk praises Mythos/Fable" item is about xAI/Anthropic, not genuinely a Tesla-company story (Gate C too weak) | no |
| AMD | 1 | ❌ (thin) | Only candidate: Zen 6 "Medusa Point" Geekbench leak — CPU benchmark leak, weak/incidental AI relevance (Ryzen AI branding only) | no |
| Amazon | 1 | ❌ | No qualifying Tier-1 candidate in START_POOL or gap-fill within the 7-day window | no |
| Oracle | 1 | ❌ | No qualifying candidate found | no |
| Apple | 1 | ❌ | Gap-fill found only recycled WWDC (June) Siri/Apple Intelligence recap coverage — stale write-ups, outside freshness intent; no genuine new development | no |
| Tier 2 (all) | 2 | N/A | Not reached — Tier 1 already filled 4 slots, hitting the `prefer` target, so no descent was needed | no |

## Tier-descent record
Tier 1 alone reached the `prefer` target (4 slots): Meta Platforms, Microsoft, Alphabet, Alibaba. Tier 2 was not invoked.

## Selected stories
1. **Meta Platforms (META US · Tier 1) — อัปเดตสำคัญ 3 รายการ**
   - **1.1** Muse Image sparks Instagram-photo consent backlash
     - Publisher: TechCrunch (+ ZDNet, Engadget corroborating, cluster_size 7)
     - URL: https://techcrunch.com/2026/07/09/how-to-stop-metas-ai-image-generator-from-using-your-instagram-photos/
     - Published: Thu, 09 Jul 2026 17:56:47 +0000 — age 6.1h
     - FreshnessCheck: ✅ within WINDOW · DedupCheck: ✅ not in last-7-day set (launch itself was covered 07-08; this is the distinct consent-backlash angle/URL)
     - Verification: Tier 1 — funnel body
     - Summary: Meta's Muse Image auto-opts all public Instagram accounts into being used as AI-generation source material via @mention; users can opt out via Settings > Sharing and reuse, but weren't notified by default — raising consent/harassment concerns.
   - **1.2** Meta to put AI chip into production in September, doubling compute capacity
     - Publisher: Reuters (+ TechCrunch, CNBC corroborating, cluster_size 3)
     - URL: https://www.reuters.com/world/asia-pacific/meta-put-ai-chip-into-production-september-it-looks-double-computing-capacity-2026-07-09/
     - Published: Thu, 09 Jul 2026 23:48:25 GMT — age 0.2h
     - FreshnessCheck: ✅ · DedupCheck: ✅ not in last-7-day set
     - Verification: Tier 2 — funnel snippet (extract_status: blocked; body_text empty — WEBFETCH_BLOCKED so no live fallback)
     - Summary: Reuters exclusive per internal memo: Meta's own AI chip enters production in September as part of a plan to double computing capacity; modular design approach per TechCrunch snippet.
   - **1.3** Meta launches Muse Spark 1.1, opens agentic-coding model via API for the first time
     - Publisher: TechCrunch (body fetched via the same-day ainews-stream funnel run, identical URL)
     - URL: https://techcrunch.com/2026/07/09/meta-enters-the-crowded-ai-coding-battle-with-muse-spark-1-1/
     - Published: Thu, 09 Jul 2026 19:40:45 +0000 — age 4.4h
     - FreshnessCheck: ✅ · DedupCheck: ✅ not in last-7-day set
     - Verification: Tier 1 — funnel body (fetched under the ainews stream's universe run for the same URL/date; treated as equivalent first-party evidence)
     - Summary: Meta launched Muse Spark 1.1, an agentic-coding/computer-use model, opened for the first time via the Meta Model API at $1.25/$4.25 per million tokens — priced slightly below Claude Haiku 4.5 and GPT-5.6 Luna.

2. **Microsoft (MSFT US · Tier 1) — GPT-5.6 กลายเป็นโมเดลหลักของ Microsoft 365 Copilot**
   - Publisher: OpenAI (primary)
   - URL: https://openai.com/index/gpt-5-6-preferred-model-microsoft-365-copilot/
   - Published: Thu, 09 Jul 2026 20:02:38 GMT — age 4.0h
   - FreshnessCheck: ✅ · DedupCheck: ✅ not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: OpenAI announced GPT-5.6 as the new preferred model across Microsoft 365 Copilot (Word, Excel, PowerPoint, Chat, Cowork), promising better performance-per-dollar and more capable on-demand assistance in everyday productivity tools.

3. **Alphabet (GOOGL US · Tier 1) — Google เริ่มติดป้าย "สร้างด้วย AI" บนโฆษณา**
   - Publisher: The Verge
   - URL: https://www.theverge.com/ai-artificial-intelligence/963628/google-ai-generated-ads-label
   - Published: 2026-07-09T16:11:38-04:00 (20:11 UTC) — age 3.9h
   - FreshnessCheck: ✅ · DedupCheck: ✅ not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Google added a "created or edited with AI" label under "how this ad was made" in My Ad Center for Search/Discover/YouTube ads, auto-applied for Google's own generative tools; other AI-made ads need manual disclosure.

4. **Alibaba (BABA US · 9988 HK · Tier 1) — ศาลสหรัฐฯ ระงับกฎ Pentagon ชั่วคราว คืนสิทธิ์ล็อบบี้ยิสต์ให้ Alibaba**
   - Publisher: Engadget (gap-fill via WebSearch; cross-corroborated by Bloomberg/Fortune, same date)
   - URL: https://www.engadget.com/2208232/alibaba-gets-a-reprieve-from-us-chinese-military-ban/
   - Published: ~2026-07-05 (cross-referenced against Fortune/Bloomberg same-story publish dates; exact Engadget timestamp not directly retrievable under WEBFETCH_BLOCKED)
   - FreshnessCheck: ✅ within 7-day WINDOW · DedupCheck: ✅ not in last-7-day set (none of the read watchlist briefs 07-03…07-09 covered this)
   - Verification: Tier 2 — WebSearch snippet (live search; not in funnel START_POOL, found via targeted gap-fill)
   - Summary: A US federal judge ordered the Pentagon not to enforce a rule barring the Defense Department from working with lobbyists tied to any 1260H-listed firm, giving Alibaba — added to the Pentagon's China-military list on June 8 alongside Baidu, BYD, and WuXi AppTec — a temporary reprieve after all its Washington lobbyists had withdrawn registration.

## Dropped
- https://www.zdnet.com/article/meta-muse-ai-feature-instagram-posts-opting-out/ — folded into story 1.1 (same event, secondary citation)
- https://www.engadget.com/2211315/heres-how-to-block-meta-from-using-your-instagram-pictures-for-its-ai/ — folded into story 1.1 (same event)
- https://news.google.com/... (CNBC) "Meta to put AI chip into production..." — same event as 1.2, Reuters kept as primary
- https://www.engadget.com/2211839/ai-generated-ads-google-get-disclosures-soon/ — folded into story 3 (same event)
- https://techcrunch.com/2026/07/09/google-will-now-disclose-which-ads-are-made-with-ai/ — folded into story 3 (same event)
- Tesla $200/week AI-spending-cap story (Electrek/TechTimes/IBTimes/etc.) — Gate: no trusted-sources.md outlet found carrying it; dropped rather than cite an unlisted domain
- https://techcrunch.com/2026/07/09/elon-musk-praises-mythos-fable-promises-not-to-cut-off-anthropic/ — Gate C too weak (about xAI/Anthropic hosting, not genuinely a Tesla-company development despite keyword match on "Elon Musk")
- GeForce NOW Toronto server expansion (blogs.nvidia.com) — real and on-allowlist, but low significance (minor cloud-gaming infra update)
- AMD Zen 6 "Medusa Point" Geekbench leak (Tom's Hardware) — real and on-allowlist, but weak AI relevance (CPU benchmark leak) and low significance
- Apple WWDC Siri/Apple Intelligence recap articles (gap-fill) — Gate A: stale write-ups from June, no genuine new July development found
- Remaining ~30 lower-score/off-watchlist candidates (Microsoft blog posts on niche customer case studies, Tom's Hardware CPU/GPU hobbyist pieces, Google Nest thermostat deal, etc.) — below selection cutoff or off-topic

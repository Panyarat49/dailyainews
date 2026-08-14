# Sources — 2026-08-14 (watchlist)

Generated: 2026-08-14 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel (3/4 slots verified from funnel body_text; 1/4 slot items from funnel snippet)
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 watchlist briefs (2026-08-07 → 2026-08-13; ~30 URLs loaded)
Tiers used: 1 (no Tier-2 descent — Tier 1 supplied 4 slots; no Tier-2 company candidates appeared in the funnel pool today, and WebFetch/WebSearch gap-fill was skipped per engine guidance for a blocked runtime)

Universe pre-load used: `.github/scripts/output/universe_2026-08-14_watchlist.json` (generated_at 2026-08-14T06:38:56+07:00, ~45 min before this run — fresh). Candidates pre-filtered/scored for watchlist company keywords.

## Significance ledger (Tier 1)
| Company | Tier | Significant AI/tech news today? | Reason | Selected |
|---|---|---|---|---|
| Nvidia | 1 | Yes | Follow-up analysis on Nvidia's $500B GPU-financing platform, framed around protecting GPU resale value ("aging GPUs") — financial-engineering angle relevant to chip demand/valuation | ✅ (single slot, Tier 2 — funnel snippet) |
| Tesla | 1 | No | No AI/tech-relevant Tesla candidate passed gates today | — |
| Microsoft | 1 | Yes | Mico avatar retired from Copilot voice mode + broader Copilot app consolidation (drops AI podcast, Group Chats, Deep Research) | ✅ (roundup, 2 items) |
| Amazon | 1 | No | No genuine Amazon/AWS-specific AI candidate in the funnel pool (only a mismatched Oracle-on-AWS press release and a mistagged Anthropic-agent story); insufficient evidence to cite | — |
| Oracle | 1 | No | Only low-signal Oracle Blogs press releases (Exadata/WebLogic/Essbase docs), no body_text, not brief-worthy news | — |
| Alphabet | 1 | Yes | Gemini 3.7 Flash launch — major coding/agent capability jump + 50% introductory API price cut | ✅ (lead story) |
| Apple | 1 | Yes | Apple in talks to pay news publishers (nine-figure budget) to power the upcoming Siri AI with current news/information | ✅ |
| Alibaba | 1 | No | No candidate surfaced in today's funnel pool | — |
| Meta Platforms | 1 | No (below bar) | Only thin/low-evidence items (AI screening for WhatsApp scams, skilled-trades hiring for AI infra) — descriptions duplicate the headline with no substantive snippet, insufficient to verify at any tier | — |
| AMD | 1 | No (below bar) | "$5B debt offering" (Bloomberg, screening-only source, description duplicates headline) — no open-source cross-match found, insufficient evidence | — |

Tier 2 (Berkshire Hathaway, Goldman Sachs, Palantir, Oklo, Netflix, Affirm, TSMC, Tencent, Xiaomi, Micron): no candidates appeared in today's funnel pool for any Tier-2 company. Tier-2 descent not triggered because Tier 1 already reached `prefer` (4 slots); per-company gap-fill searches were not run given `WEBFETCH_BLOCKED` (engine guidance: ship funnel-backed items rather than pad via search in a blocked runtime).

## Selected stories
1. **Alphabet (GOOGL US · Tier 1) — Gemini 3.7 Flash launch + 50% price cut**
   - URL: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/
   - Publisher: Google (primary)
   - Published: Thu, 13 Aug 2026 17:05:38 GMT (age_h 6.5)
   - FreshnessCheck: ✅ within WINDOW
   - DedupCheck: ✅ URL not in last-7-day watchlist set (distinct from the "Gemini/ChatGPT 1B users" story used 2026-08-12)
   - Verification: Tier 1 — funnel body (extract_status=ok); corroborated by Reuters (cluster_size 4/9) and VentureBeat (Tier-1 body in the general brief's pool)
   - Summary: Google shipped Gemini 3.7 Flash with major coding/agentic gains, temporarily halving API prices through end of 2026; next-gen Gemini Pro remains unannounced.

2. **Apple (AAPL US · Tier 1) — In talks to pay publishers to power Siri AI with current news**
   - URL: https://techcrunch.com/2026/08/13/apple-in-talks-to-pay-publishers-to-provide-siri-with-current-news-report/
   - Publisher: TechCrunch (citing WSJ)
   - Published: Thu, 13 Aug 2026 14:34:43 +0000 (age_h 9.1)
   - FreshnessCheck: ✅ within WINDOW
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 1 — funnel body (extract_status=ok); corroborated by Livemint (cluster_size 5-7 across outlets)
   - Summary: Apple is negotiating multiyear, pay-per-use content deals (considered nine-figure budget) with news publishers to give the upcoming Siri AI access to current news, departing from standard fixed-licensing norms.

3. **Microsoft (MSFT US · Tier 1) — อัปเดตสำคัญ 2 รายการ** (roundup)
   - 3.1 URL: https://www.theverge.com/tech/979871/microsoft-copilot-mico-retired — Publisher: The Verge — Published 2026-08-13T17:42:38-04:00 (age_h 1.9) — Verification: Tier 1 — funnel body (extract_status=ok); corroborated by Engadget (funnel body_text ok) — Summary: Microsoft is removing the Mico avatar from Copilot's voice mode, relocating it to the Learn Live tutoring hub.
   - 3.2 URL: https://techcrunch.com/2026/08/13/microsoft-kills-off-unsuccessful-ai-features-while-merging-its-separate-copilot-apps/ — Publisher: TechCrunch — Published Thu, 13 Aug 2026 15:30:52 +0000 (age_h 8.1) — Verification: Tier 2 — funnel snippet (extract_status=skipped, no body_text; WebFetch blocked so summarized from the substantive RSS description only) — Summary: Microsoft is merging its consumer and business Copilot apps and dropping underused AI features (AI-generated podcasts, Group Chats, Deep Research) alongside the Mico retirement.
   - Both FreshnessCheck ✅ / DedupCheck ✅ (URLs not in last-7-day watchlist set)

4. **Nvidia (NVDA US · Tier 1) — Nvidia's $500B GPU-value-protection financing plan**
   - URL: https://techcrunch.com/2026/08/13/nvidias-new-500b-plan-is-risky-but-brilliant-especially-for-aging-gpus/
   - Publisher: TechCrunch
   - Published: Thu, 13 Aug 2026 15:08:00 +0000 (age_h 8.5)
   - FreshnessCheck: ✅ within WINDOW — genuine new development (fresh analysis/reporting) on the $500B AI-infrastructure financing platform Nvidia announced with Apollo/BlackRock/Blackstone/Brookfield/Goldman Sachs/KKR (covered in the 2026-08-11 watchlist brief); this article's own publish time is today, reporting a new angle (protecting resale value of aging GPUs) — passes per engine 1b-hard ("freshly-published update on an older situation").
   - DedupCheck: ✅ URL not in last-7-day watchlist set (different URL/angle from the 2026-08-11 Nvidia Newsroom story)
   - Verification: Tier 2 — funnel snippet (extract_status=skipped, no body_text; substantive RSS description used, WebFetch blocked so no live fetch attempted)
   - Summary: Nvidia is pitching new financiers to keep lending for AI buildouts as a way to guarantee its GPUs won't lose resale value even as newer chip generations ship.

## Dropped
- https://www.theregister.com/offbeat/2026/08/13/twitch-feeds-your-streams-to-amazons-ai-unless-you-tell-it-to-stop/5287258 (Twitch/Amazon AI training opt-out) — genuinely an Amazon-subsidiary AI story but did not surface in the watchlist funnel pool (keyword match requires literal "Amazon"/"AWS"/etc.; "Twitch" isn't in Amazon's watchlist keyword list) — not independently re-verified given WEBFETCH_BLOCKED; flagged here for future keyword-list review (consider adding "Twitch" to Amazon's keywords).
- https://venturebeat.com/security/three-claude-agents-given-conflicting-orders-sabotaged-each-other-on-a-shared-server-then-didnt-tell-users-what-theyd-done — mistagged `matched_company: Amazon` by the funnel (via the "Anthropic" keyword, which is listed under Amazon's watchlist entry as an investment-relationship term) but the story is about Anthropic/Claude research, not an Amazon corporate action — dropped as not genuinely an Amazon-entity story.
- https://news.google.com/...WhatsApp scams (Meta) / Fox Business Meta skilled-trades hiring — RSS description duplicates the headline with no substantive content; extract_status=skipped; insufficient evidence to verify at any tier under WEBFETCH_BLOCKED — dropped.
- https://news.google.com/...AMD $5B debt offering (Bloomberg, screening-only, description duplicates headline) — no open-source cross-match located; insufficient evidence — dropped.
- Oracle Blogs items (Exadata/WebLogic/Essbase) — real primary-source URLs but pure product-documentation posts, not brief-worthy AI news; one (WebLogic) actually resolved to an Oracle error page — dropped.
- Various Apple items (Advanced Manufacturing Center Houston, Epic Games fee dispute, spyware notification, App Store ruling) — real but not AI-specific enough (Gate C) or lower significance than the selected Apple story — dropped in favor of the Siri/publishers story.

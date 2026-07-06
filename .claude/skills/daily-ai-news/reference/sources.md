# Sources — 2026-07-06 (ainews)

Generated: 2026-07-06 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel   # majority verified from funnel body_text (Tier 1); one Tier 2 (headline-level, TH boilerplate body)
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok); all 5 selected within 24h (funnel's own 24h pre-filter)
Dedup against: last 7 ainews briefs (2026-06-29 → 2026-07-05; 33 URLs loaded)
Source mix: 2 Thai (Blognone, bangkokbiznews) · 3 international (Tom's Hardware, The Guardian, ABC News Australia)
Universe pre-load: 27 candidates from universe_2026-07-06_ainews.json (generated_at 2026-07-06T07:04:01+07:00), items_enriched=11 > 0 — WebSearch skipped (≥ 8 candidates after gates)

## Selected stories
1. **Alibaba bans Anthropic's Claude Code after alleged hidden China-detection backdoor uncovered**
   - Publisher: Tom's Hardware
   - URL: https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-bans-anthropics-claude-code-after-an-alleged-hidden-china-detection-backdoor-is-uncovered-employees-told-to-switch-to-qoder-as-the-rift-between-the-firms-widens
   - Published: Sun, 05 Jul 2026 12:20:00 +0000 (age 11.7h)
   - FreshnessCheck: ✅ within 24h
   - DedupCheck: ✅ new URL — a genuine new development (backdoor allegation, switch to Qoder) on the Alibaba/Claude Code story last covered 2026-07-05 (different techcrunch.com URL, no backdoor detail)
   - Verification: Tier 2 — funnel snippet (headline). Funnel `body_text` for this Tom's Hardware URL was subscription-page boilerplate, not article text (a known extraction gap for this outlet) — summary paraphrases only the RSS headline itself, which is unusually detailed for this feed; no invented specifics beyond it.
   - Summary: Alibaba has reportedly banned internal use of Anthropic's Claude Code after employees allegedly found a hidden mechanism that detects and blocks use from China; staff were told to switch to the in-house Qoder tool instead, widening the rift between the two companies.

2. **Taiwan raids Super Micro over alleged smuggling of Nvidia AI chips to China**
   - Publisher: bangkokbiznews (กรุงเทพธุรกิจ)
   - URL: https://www.bangkokbiznews.com/world/economics/1240886
   - Published: Sun, 05 Jul 2026 06:20:46 GMT (age 17.7h)
   - FreshnessCheck: ✅ within 24h
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (full Thai-language article text, sourced to Bloomberg)
   - Summary: Taiwan's Keelung District Prosecutors Office raided Super Micro Computer's Taiwan offices and three affiliates, plus six individuals' homes, investigating alleged smuggling of Nvidia AI chips to China via servers routed through Japan; Super Micro's US stock fell 8%, partner Albatron fell 10%, and data-center operator Chief Telecom fell over 2%.

3. **UK foreign secretary warns AI poses 'Hiroshima'-style threat without global rules**
   - Publisher: The Guardian
   - URL: https://www.theguardian.com/politics/2026/jul/05/ai-hiroshima-style-threat-humanity-global-rules-yvette-cooper
   - Published: Sun 5 Jul 2026 15:00 EDT / 2026-07-05T23:08:00Z (age 0.9h)
   - FreshnessCheck: ✅ within 24h
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (full article text)
   - Summary: UK Foreign Secretary Yvette Cooper, in an essay for Chatham House, said AI carries a "Hiroshima"-style risk to humanity absent international agreement, urging the US and China to negotiate shared AI rules and predicting the issue will dominate foreign policy over the next two years.

4. **Singapore's central bank issues AI-agent safety framework for financial services**
   - Publisher: Blognone
   - URL: https://www.blognone.com/node/151072
   - Published: Sun, 05 Jul 2026 16:41:21 +0000 (age 7.4h)
   - FreshnessCheck: ✅ within 24h
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (full Thai-language article text)
   - Summary: The Monetary Authority of Singapore published a whitepaper, "Safeguards for Agentic Finance at Runtime (SAFR)," setting a minimum of four checkpoints financial firms must build into AI agents that act on customers' behalf, codifying practices already used by Ant, Mastercard, Visa, and Circle.

5. **Australia's ABC rolls out AI writing tools amid union trust warnings**
   - Publisher: ABC News (Australia)
   - URL: https://www.abc.net.au/news/2026-07-06/abc-new-ai-policies/106844364
   - Published: Sun, 05 Jul 2026 19:06:28 GMT (age 5.0h)
   - FreshnessCheck: ✅ within 24h
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (full article text)
   - Summary: The ABC is trialling AI tools to help staff turn regional radio bulletins into digital news articles, after striking a deal with Anthropic last month; the journalists' union welcomed the move cautiously but said management refused to commit to AI never replacing jobs, with an all-staff town hall set for July 28.

## Dropped
- https://www.theverge.com/ai-artificial-intelligence/961505/wealthy-ai-schools-alpha-forge-prep — lower significance/lifestyle feature, displaced by higher-scoring items
- https://www.theverge.com/ai-artificial-intelligence/961468/google-ai-commercial-founding-fathers-declaration-of-independence — opinion/culture commentary, not a news development
- https://www.tomshardware.com/tech-industry/atomic-semi-rebrands-as-fab2-and-shifts-operations-to-texas — funnel body was boilerplate/unusable and a stronger 5th pick (ABC, real body) was available
- https://news.google.com/rss/articles/...abc-new-ai-policies (GNews redirect) — resolved to the same abc.net.au URL cited in Story 5
- Remaining Tom's Hardware GPU/hardware-review and gaming items — off-scope (not AI/tech-significant)
- thestandard.co semiconductor-board retrospective, mgronline True/Big Data piece, and Thai stock-market/AI-bubble commentary pieces — lower significance/analysis rather than news, displaced to stay within STORY_COUNT max

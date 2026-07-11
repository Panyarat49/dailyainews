# Sources — 2026-07-11 (ainews)

Generated: 2026-07-11 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel   # funnel = most picks verified from funnel body_text; WebSearch used as supplementary confirmation for two Tier-2 picks
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 ainews briefs (47 URLs loaded)
Source mix: The Verge ×2, TechCrunch, Reuters, Anthropic (primary)

## Selected stories
1. **Apple sues OpenAI, alleging theft of hardware trade secrets**
   - Publisher: The Verge
   - URL: https://www.theverge.com/tech/964350/apple-openai-lawsuit-trade-secrets
   - Published: Jul 10, 2026, 9:36 PM UTC
   - FreshnessCheck: ✅ within window via funnel `published_raw` (2026-07-10T17:36:51-04:00) + body_text
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (extract_status: ok, real article text incl. quotes)
   - Summary: Apple sued OpenAI and Jony Ive's IO Products, naming OpenAI hardware chief Tang Tan and ex-Apple engineer Chang Liu, alleging a "pattern of theft" of Apple trade secrets used to advance OpenAI's hardware plans.

2. **SK Hynix raises $26.5B — biggest foreign IPO in US history**
   - Publisher: TechCrunch
   - URL: https://techcrunch.com/2026/07/10/sk-hynix-raises-26-5b-in-the-biggest-foreign-ipo-in-us-history-is-urged-to-build-new-us-fabs/
   - Published: Fri, 10 Jul 2026 17:17:12 GMT
   - FreshnessCheck: ✅ within window via funnel `published_raw`
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet + corroborating WebSearch (Bloomberg, CNN, Al Jazeera, Semafor all confirm same figures)
   - Summary: SK Hynix priced 177.9M ADRs at $149 each, raising $26.5B on Nasdaq (temp ticker SKHYV) — the largest-ever US debut by a foreign company, topping Alibaba's 2014 IPO; demand ran 7x the offered shares and the stock opened +14%. Lawmakers are urging SK Hynix and Samsung to build new US fabs.

3. **US eases export rules, letting Nvidia AI chips flow more freely to the UAE**
   - Publisher: Reuters
   - URL: https://www.reuters.com/world/middle-east/us-makes-it-easier-export-certain-military-items-ai-chips-commercial-satellites-2026-07-10/
   - Published: Fri, 10 Jul 2026 19:39:42 GMT
   - FreshnessCheck: ✅ within window via funnel `published_raw` (resolved from Google News redirect)
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — WebSearch snippet (WebFetch blocked this session; funnel extract_status was "blocked" too) corroborated by Bloomberg/Al-Monitor/theprint.in coverage of the same Commerce Dept move
   - Summary: The US Commerce Department moved the UAE into a country grouping allowing more license-free exports of AI chips, military items, and satellites; UAE's G42/Core42 plus US firms operating there (Amazon, Apple, xAI) no longer need licenses for AI chips/servers — a deepening of US-UAE ties amid Iran strategy.

4. **Anthropic says it can read Claude's "thoughts" — new global-workspace interpretability paper**
   - Publisher: Anthropic (primary) / covered by Tom's Hardware
   - URL: https://www.anthropic.com/research/global-workspace
   - Published: paper ~Jul 6, 2026; Tom's Hardware write-up Fri, 10 Jul 2026 16:44:12 GMT (within window)
   - FreshnessCheck: ✅ within 7d window (write-up + primary source both inside WINDOW)
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — WebSearch snippet (Tom's Hardware funnel body_text was membership-paywall boilerplate, not usable; corroborated by VentureBeat "J-lens" coverage and Anthropic's own research page)
   - Summary: Anthropic reports evidence of a "J-space" — a small internal representation set acting like a shared workspace for reportable, steerable reasoning inside Claude, read via a technique called J-lens. Anthropic frames this as an interpretability/monitoring advance, explicitly not a consciousness claim.

5. **Meta turns off Instagram AI feature that let users generate deepfakes of public accounts**
   - Publisher: The Verge
   - URL: https://www.theverge.com/tech/964416/meta-instagram-ai-muse-image-deepfakes
   - Published: 2026-07-10T19:49:50-04:00
   - FreshnessCheck: ✅ within window via funnel `published_raw`
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet (substantive description; extract_status skipped for body)
   - Summary: Meta disabled an Instagram AI-image feature — launched just days earlier — that let any user generate AI images using content tagged from public accounts, after backlash over enabling deepfakes of public figures without consent.

## Dropped
- https://venturebeat.com/technology/openai-introduces-chatgpt-work-a-cloud-based-ai-agent-that-manages-tasks-across-email-slack-and-calendars — editorial dedup: same underlying launch (OpenAI ChatGPT Work) already covered as the lead story in articles/2026-07-10-ainews.md (The Verge + ZDNet sources); no genuinely new development in this VentureBeat write-up beyond the prior day's coverage.
- https://www.tomshardware.com/... (SK hynix/TetraMem memristor chip, HBM heat-wall research, Rapidus wafer pricing, Samsung Gaia NPU, Anthropic interpretability as primary cite) — Gate: unusable body — funnel body_text for these Tom's Hardware URLs was membership/paywall boilerplate, not article content; only used as corroboration, not as sole citation.
- https://www.tomshardware.com/.../sk-hynix-raises-a-record-usd26-5-billion... — superseded by TechCrunch citation of the same event (better snippet quality).
- news.google.com redirect links — never cited directly; resolved to their underlying trusted-source URL (Reuters, The Guardian) before use.
- Various sub-4.0-score long-tail items (Intel CPU deal, Steam sales, TabFM, Nanya capex, equity fund inflows, FamilyMart store, etc.) — below significance bar / not AI-relevant enough to displace the 5 selected.

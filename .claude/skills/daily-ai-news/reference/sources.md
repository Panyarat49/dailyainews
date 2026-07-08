# Sources — 2026-07-08 (ainews)

Generated: 2026-07-08 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel   # items_enriched=11 in universe JSON — most picks verified from funnel body_text
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 ainews briefs (42 URLs loaded)
Universe pre-load: 40 candidates from universe_2026-07-08_ainews.json (generated_at 2026-07-08T06:56:47+07:00) — WebSearch skipped (≥ 8 candidates after gates)
Source mix: The Register ×2, The Verge ×2, Reuters ×1 — 3 distinct outlets, all international (no same-day Thai AI story survived the funnel pool this run).

## Selected stories
1. **GitHub AI agent leaks private repos when asked nicely ("GitLost")**
   - Publisher: The Register
   - URL: https://www.theregister.com/security/2026/07/07/github-ai-agent-leaks-private-repos-when-asked-nicely/5267924
   - Published: Tue, 07 Jul 2026 21:49:01 +0200 (~4.1h old at funnel generation)
   - FreshnessCheck: ✅ within last 24h via funnel body_text timestamp
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Noma Labs researchers found a prompt-injection flaw ("GitLost") in GitHub's Agentic Workflows letting an attacker trick a Claude- or Copilot-powered agent into pulling data from private repos and leaking it via a public comment; GitHub has no fix or documentation for it yet.

2. **Anthropic launches Claude Cowork on mobile and web**
   - Publisher: The Verge
   - URL: https://www.theverge.com/ai-artificial-intelligence/961978/anthropic-claude-cowork-mobile-web
   - Published: 2026-07-07T13:46:59-04:00 (~6.2h old at funnel generation)
   - FreshnessCheck: ✅ within last 24h via funnel body_text timestamp
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Claude Cowork, previously desktop-only, is now available on mobile and web (Max subscribers first, other plans "in the coming weeks") and now also runs in the cloud so tasks keep going after the laptop closes.

3. **China's DeepSeek reportedly developing its own AI chip**
   - Publisher: Reuters
   - URL: https://www.reuters.com/world/china/chinas-deepseek-developing-its-own-ai-chip-sources-say-2026-07-07/
   - Published: Tue, 07 Jul 2026 21:40:54 GMT (~2.3h old at funnel generation)
   - FreshnessCheck: ✅ within last 24h via funnel `published_raw`
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet (extract_status=blocked; WebFetch also WEBFETCH_BLOCKED this session, so per engine rule used funnel `description` + `published_raw` directly rather than a WebSearch fallback)
   - Summary: Reuters reports, citing sources, that DeepSeek is working on developing its own AI chip — a further sign of Chinese AI labs pushing to reduce dependence on foreign silicon amid export controls.

4. **Meta's new Muse Image model lets prompts pull in other Instagram users**
   - Publisher: The Verge
   - URL: https://www.theverge.com/tech/962485/meta-muse-image-ai-model-instagram
   - Published: 2026-07-07T16:31:58-04:00 (~3.9h old at funnel generation)
   - FreshnessCheck: ✅ within last 24h via funnel body_text timestamp
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Meta's Superintelligence Labs shipped Muse Image, its first in-house image model, now powering image generation in the Meta AI app, Instagram, and WhatsApp; users can "@mention" other Instagram accounts in prompts to pull them into generated photos.

5. **Cloud AI worm "CAI" steals rival malware's stolen credentials, mines crypto**
   - Publisher: The Register
   - URL: https://www.theregister.com/cyber-crime/2026/07/07/cai-cloud-worm-gives-competitors-malware-the-boot-then-steals-secrets-and-mines-for-coin/5267856
   - Published: Tue, 07 Jul 2026 19:15:00 +0200 (~7h old at funnel generation)
   - FreshnessCheck: ✅ within last 24h via funnel body_text timestamp
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: A new botnet worm, "Cloud AI Infrastructure Attack Framework" (CAI), targets cloud-native dev tools (Docker, Kubernetes, Redis, etcd, Kubelet, Ray) for credential theft and cryptomining, and kills off rival secret-stealing malware running on the same infected hosts.

## Dropped
- VentureBeat / Engadget / ZDNet / TechCrunch / second Verge writeup — all cover the same Claude Cowork mobile/web launch as Story 2; kept the highest-scored Verge article, dropped the rest as duplicates.
- Intel XBM memory architecture patent (Tom's Hardware) — solid Tier-1 candidate but not selected to keep the 5-story set topically diverse (already 2 chip/silicon-adjacent angles via DeepSeek + CAI).
- channelnewsasia.com "Commentary: How will SAF prepare for the age of AI-enabled warfare?" — Gate: opinion/commentary column, excluded per SCOPE ("always drop... pure opinion").
- techcrunch.com "Why the rise of open source AI isn't hurting Anthropic … yet" — Gate: analysis/opinion piece, not a reported event; excluded per SCOPE.
- reuters.com "Beijing looking at curbing overseas access to China's top AI models" — considered; DeepSeek-chip story (Story 3) chosen instead to avoid stacking two China-AI-policy angles.
- 25+ remaining candidates (data-center power/water stories, chip-market earnings, misc product tips) — lower funnel score; story cap of 5 reached.

# Sources — 2026-06-22 (watchlist)

Generated: 2026-06-22 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED (control probe https://example.com → 403; all live fetches 403)
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok); every selected item additionally within last 24h
Dedup against: last 6 watchlist briefs (30 URLs loaded; 2026-06-16 → 2026-06-21)
TIERS_USED: 1 (Tier 2 not invoked — no Tier-2 company surfaced a citeable story)
Companies with significant news today: Amazon, Apple, Alphabet
Universe pre-load: 20 candidates from RSS funnel (generated_at 2026-06-22T06:28:01+07:00, ~2.5h old). Verification forced to Tier-2 (funnel snippet) because this runtime's WebFetch is 403-blocked.
Count note: 3 slots (floor = 3; below the prefer target of 4). In blocked mode the citeable supply was thin: most Tier-1 funnel items were Tom's Hardware entries with image-only `description` (no paraphrasable snippet), `news.google.com` redirects with title-only snippets, or Bloomberg (screening). Did NOT pad with off-topic/redirect items per the engine's blocked-mode rule.

## Significance ledger (Company | Tier | Significant? | Reason | Selected)
- Amazon | 1 | Yes | Regulatory: US crackdown on Anthropic (Amazon's key model partner) — implications for the AI ecosystem | ✅ slot 1
- Apple | 1 | Yes (product) | iOS 27 practical AI features beyond Siri | ✅ slot 2
- Alphabet | 1 | Yes (product, ×2) | Google Workspace AI updates (AI note-taking, Thai AI Avatar) + Google Meet on Android Auto | ✅ slot 3 (roundup)
- Nvidia | 1 | Unverifiable | [17] LG–Nvidia talks = news.google.com redirect + title-only snippet; [6] SpaceX–Tesla "could rival Nvidia" = speculation + redirect; [3] NVK DLSS = image-only desc | ❌
- AMD | 1 | Unverifiable | [0]/[1] GMKtec EVO-X3 mini-PC = image-only desc / redirect | ❌
- Microsoft | 1 | Unverifiable/low | [15]/[16] "goats neural network" art project = image-only desc / redirect, low significance | ❌
- Tesla | 1 | No/weak | [6] merger speculation (drop); [7] robotaxi scorecard snippet is a newsletter intro, doesn't substantiate Tesla | ❌
- Tier 2 (all) | 2 | None surfaced | No Tier-2 company appeared with a citeable, substantive, direct-URL snippet | ❌

## Tier-descent record
Tier 1 yielded 3 company-slots (Amazon, Apple, Alphabet). Target prefer = 4. Per `tier_descent = top-up-to-target`, attempted descent to Tier 2 — but no Tier-2 candidate passed Gate W + substantive-snippet citeability in blocked mode. Shipped 3 (floor) rather than padding.

## Selected stories
1. **When the Trump administration cracks down on Anthropic, who benefits?**
   - Amazon · AMZN US · Tier 1 (matched via keyword "Anthropic")
   - URL: https://techcrunch.com/2026/06/21/when-the-trump-administration-cracks-down-on-anthropic-who-benefits/
   - Published: Sun, 21 Jun 2026 15:28:17 +0000 (age ~8.0h)
   - FreshnessCheck: ✅ within last 24h via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 2 — funnel snippet
   - Summary: A new episode of Equity discusses what actually prompted the administration's latest moves against Anthropic and what this could mean for the AI ecosystem. (Watchlist relevance: Amazon is a major Anthropic partner.)

2. **Beyond Siri: practical AI features coming to iPhone in iOS 27**
   - Apple · AAPL US · Tier 1 (matched via keywords "Apple", "Siri")
   - URL: https://techcrunch.com/2026/06/21/beyond-siri-here-are-the-practical-ai-features-coming-to-your-iphone-in-ios-27/
   - Published: Sun, 21 Jun 2026 14:40:28 +0000 (age ~8.8h)
   - FreshnessCheck: ✅ within last 24h via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Verification: Tier 2 — funnel snippet
   - Summary: Siri's AI overhaul grabbed the WWDC headlines, but some of Apple's most useful AI features in iOS 27 are arriving elsewhere across the OS.

3. **Alphabet roundup — Google Workspace AI updates + Google Meet on Android Auto**
   - Alphabet · GOOGL US · Tier 1 (matched via keyword "Google")
   - 3.1 URL: https://www.blognone.com/node/150952 — Published Sun, 21 Jun 2026 10:15:33 +0000 (age ~13.2h)
     - Summary: Google Workspace updates — AI note-taking on Google Voice calls, 200 calendar colors, Thai-language AI Avatar in Google Vid.
   - 3.2 URL: https://www.blognone.com/node/150953 — Published Sun, 21 Jun 2026 12:41:41 +0000 (age ~10.8h)
     - Summary: Google Meet now works in cars via Android Auto — join meetings from the car screen with upcoming-meeting reminders.
   - FreshnessCheck: ✅ both within last 24h via funnel published_raw
   - DedupCheck: ✅ neither URL in last-7-day watchlist set
   - Verification: Tier 2 — funnel snippet (both)

## Dropped
- https://thestandard.co/opinion-ai-modelers-market/ — Gate D/scope (opinion column).
- https://news.google.com/rss/...LG-Nvidia... , ...SpaceX-Tesla-rival-Nvidia... , ...Bloomberg Amazon Prime Day... — provenance (news.google.com redirect) + thin/title-only snippet or screening source.
- https://www.tomshardware.com/...evo-x3... , .../nvk-dlss... , .../goaty... , .../ice-machine-gpu... , .../keyboard... , RAM-tracking — Tier-2 not satisfiable: image-only `description` (no paraphrasable snippet) or non-AI/not significant.
- https://techcrunch.com/2026/06/21/techcrunch-mobility-a-new-robotaxi-scorecard... — Gate W/weak: snippet is a newsletter intro; does not substantiate a watchlist-company (Tesla) claim.
- https://news.google.com/rss/...blog.google startups accelerator (Kiwi/Australian)... — Gate D: low-significance PR + redirect.

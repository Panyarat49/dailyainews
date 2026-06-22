# Sources — 2026-06-22 (ainews)

Generated: 2026-06-22 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED (control probe https://example.com → 403; all live fetches 403)
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok); every selected item additionally within last 24h
Dedup against: last 7 ainews briefs (39 URLs loaded; 2026-06-15 → 2026-06-21)
Source mix: 2 international (The Register, TechCrunch) + 3 Thai (The Standard ×2, Blognone). International supply thin this run — most Tom's Hardware funnel items carried image-only descriptions (no substantive snippet), so were not Tier-2-citeable in blocked mode.
Universe pre-load: 25 candidates from RSS funnel (generated_at 2026-06-22T06:27:45+07:00, ~2.5h old). Verification forced to Tier-2 (funnel snippet) because this runtime's WebFetch is 403-blocked.

## Selected stories
1. **Anthropic's Mythos/Fable 5 ban keeps getting more complicated**
   - Publisher: The Register (theregister.com)
   - URL: https://www.theregister.com/ai-and-ml/2026/06/22/anthropics-mythos-mess-just-keeps-getting-more-complicated/5258577
   - Published: Mon, 22 Jun 2026 01:00:00 +0200 (age ~0.5h at funnel build)
   - FreshnessCheck: ✅ within last 24h via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet
   - Summary: A week after the Trump administration imposed a de facto ban on Anthropic's Mythos derivative Fable 5, more details emerging about the move suggest internal Anthropic concerns were warranted; the piece questions the government's rationale.

2. **Beyond Siri: practical AI features coming to iPhone in iOS 27**
   - Publisher: TechCrunch (techcrunch.com)
   - URL: https://techcrunch.com/2026/06/21/beyond-siri-here-are-the-practical-ai-features-coming-to-your-iphone-in-ios-27/
   - Published: Sun, 21 Jun 2026 14:40:28 +0000 (age ~8.8h)
   - FreshnessCheck: ✅ within last 24h via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet
   - Summary: Siri's AI overhaul grabbed the WWDC headlines, but some of Apple's most useful AI features in iOS 27 are arriving elsewhere across the OS.

3. **Thailand–IMEC: deepening photonics/semiconductor cooperation (Netherlands & Belgium mission)**
   - Publisher: The Standard (thestandard.co)
   - URL: https://thestandard.co/yoschanan-imec-thailand-chip-hub/
   - Published: Sun, 21 Jun 2026 05:57:31 +0000 (age ~17.5h)
   - FreshnessCheck: ✅ within last 24h via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet
   - Summary: Deputy PM and MHESI minister Yoschanan Wongsawat summarized a 13–20 June mission to the Netherlands and Belgium seeking science/tech cooperation, with IMEC ties aimed at positioning Thailand as a photonics-chip hub.

4. **Google Workspace AI updates — AI note-taking in Voice, Thai-language AI Avatar in Google Vid**
   - Publisher: Blognone (blognone.com)
   - URL: https://www.blognone.com/node/150952
   - Published: Sun, 21 Jun 2026 10:15:33 +0000 (age ~13.2h)
   - FreshnessCheck: ✅ within last 24h via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet
   - Summary: Google Workspace rolled out updates including AI note-taking on Google Voice calls, 200 calendar colors in Google Calendar, and Thai-language support for the AI Avatar in Google Vid.

5. **Opposition leader urges NACC to probe the TH-AI Passport project**
   - Publisher: The Standard (thestandard.co)
   - URL: https://thestandard.co/natthaphong-pacc-th-ai-passport-probe/
   - Published: Sun, 21 Jun 2026 11:30:55 +0000 (age ~11.9h)
   - FreshnessCheck: ✅ within last 24h via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet
   - Summary: Opposition leader Natthaphong Ruangpanyawut said he asked the NACC to investigate the TH-AI Passport project on its own initiative, citing anti-collusion-bidding law and warning that inaction could constitute dereliction of duty.

## Dropped
- https://thestandard.co/opinion-ai-modelers-market/ — Scope (pure opinion/investment column).
- https://www.tomshardware.com/...evo-x3... , .../goaty... , .../nvk-dlss... , .../bank-of-korea-...-bonuses... — Tier-2 not satisfiable in blocked mode: funnel `description` was an image-URL only (no substantive snippet to paraphrase). Kept off rather than padded.
- https://news.google.com/rss/articles/...True IDC... — Gate (provenance): news.google.com redirect; no direct bangkokbiznews URL fetchable in blocked mode + thin snippet.
- https://techcrunch.com/2026/06/21/ubisoft-co-founder-claude-guillemot... , https://www.blognone.com/node/150950 — Scope: not AI/tech (keyword "claude" matched a person's name).
- https://news.google.com/rss/articles/...Bloomberg... — Screening source (discovery only) + redirect; not citeable.
- https://news.google.com/rss/articles/...BBC/Guardian/livemint... — thin (title-only) snippet via news.google.com redirect; not Tier-2-citeable in blocked mode.

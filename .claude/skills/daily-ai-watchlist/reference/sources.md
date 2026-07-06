# Sources — 2026-07-06 (watchlist)

Generated: 2026-07-06 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel   # majority verified from funnel body_text (Tier 1); 1 headline-only Tier 2
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok); all selected within 24h (funnel's own 24h pre-filter)
Dedup against: last 7 watchlist briefs (2026-06-30 → 2026-07-05; 27 URLs loaded)
Tiers used: 1 (no Tier-2 descent needed/possible — see ledger)
Universe pre-load: 20 candidates from universe_2026-07-06_watchlist.json (generated_at 2026-07-06T07:05:01+07:00), items_enriched=12 > 0 — WebSearch skipped (≥ 8 candidates after gates)

## Significance ledger (Tier 1)
| Company | Tier | Significant AI/tech news today? | Reason | Selected |
|---|---|---|---|---|
| Nvidia | 1 | Candidate existed (Hon Hai/Foxconn earnings beat on AI demand) | Bloomberg = screening-only, body_text was a robot-check wall (unusable), no open-citation cross-match found in pool | ❌ dropped — unciteable |
| Tesla | 1 | Candidates existed (AI-cost cap on staff spending; stock re-rating) | Both only had a `news.google.com` redirect with empty `resolved_url` — no real citeable article URL available | ❌ dropped — unciteable |
| Microsoft | 1 | Yes — Ayman AlGhamdi appointed President, Microsoft Arabia | Primary source (news.microsoft.com), real body confirming Saudi AI/cloud strategy tie-in | ✅ selected |
| Amazon | 1 | Yes — AWS closes Mechanical Turk to new customers | Real body (TechCrunch); MTurk is the human-labeling backbone behind many "AI" products/SageMaker | ✅ selected |
| Oracle | 1 | No candidate surfaced | — | — |
| Alphabet | 1 | Candidate existed (Google Workspace/Gemini ad) | Opinion/culture commentary on an ad, not a news development — dropped per "always drop: opinion" | ❌ dropped |
| Apple | 1 | Yes — EU says Apple responsible for Siri AI delay in Europe | AP News headline confirmed via GNews-resolved apnews.com URL; body was AP's generic video-roundup filler (unusable) so summary is headline-only (Tier 2) | ✅ selected |
| Alibaba | 1 | Yes — bans Claude Code over alleged China-detection backdoor | Rich real body (Tom's Hardware, corroborated by France 24): backdoor allegation, Anthropic distillation-attack accusation, Qoder switch, July 10 effective date | ✅ selected |
| Meta Platforms | 1 | No candidate surfaced | — | — |
| AMD | 1 | Candidates existed (GPU reviews, Windows/Scattered Spider story mismatched to AMD) | Not genuine AMD-company AI news — hardware reviews / unrelated security story | ❌ dropped |

**Tier-descent record:** Not triggered. 4 Tier-1 stories cleared all gates with real citations, meeting the `prefer` (4) target; the two open slots (Nvidia, Tesla) had real candidates but no citeable, verifiable URL, and no genuine Tier-2 company story surfaced (only tangential DARPA/Oklo drone-battery item, dropped for weak AI/company relevance) — so the brief ships at 4 rather than padding with unciteable or off-topic filler.

## Selected stories
1. **Alibaba bans Anthropic's Claude Code after alleged hidden China-detection backdoor uncovered**
   - Company · Ticker · Tier: Alibaba · BABA US / 9988 HK · Tier 1
   - URL: https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-bans-anthropics-claude-code-after-an-alleged-hidden-china-detection-backdoor-is-uncovered-employees-told-to-switch-to-qoder-as-the-rift-between-the-firms-widens
   - Published: Sun, 05 Jul 2026 12:20:00 +0000 (age 11.7h)
   - FreshnessCheck: ✅ within 24h
   - DedupCheck: ✅ new URL — a genuine new development (specific backdoor allegation, July 10 effective date, distillation-attack context, Qoder + full Anthropic-product uninstall directive) beyond the 2026-07-05 watchlist brief's techcrunch.com report, which had none of this detail
   - Verification: Tier 1 — funnel body (the GNews-resolved duplicate of this URL carried real article text, unlike the direct-feed entry which returned subscription boilerplate; corroborated by France 24's independent write-up of the same event)
   - Summary: Alibaba banned staff from using Anthropic's Claude Code for all work, effective July 10, after researchers alleged it contained code that detects users connecting from China; per a July 3 SCMP report Alibaba added it to a "high-risk software" list over back-door concerns. Staff were told to switch to Alibaba's own Qoder and reportedly to uninstall all Anthropic products (Sonnet, Opus, Fable). The ban follows Anthropic's own accusation that Alibaba's Qwen lab ran a large-scale "distillation" attack on Claude using ~25,000 fake accounts.

2. **EU says Apple is responsible for Siri AI delay in Europe**
   - Company · Ticker · Tier: Apple · AAPL US · Tier 1
   - URL: https://apnews.com/video/eu-says-apple-is-responsible-for-siri-ai-delay-in-europe-0cde1ca0a58041038b42f3fd806950b2
   - Published: Sun, 05 Jul 2026 12:21:17 GMT (age 11.7h)
   - FreshnessCheck: ✅ within 24h
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet (headline only). AP's `body_text` for this entry was a generic "AP top stories" video-roundup list unrelated to the Siri story, so the summary paraphrases only the headline itself; no further specifics invented.
   - Summary: According to AP News, the European Union has said Apple bears responsibility for the delay in bringing Siri's AI-enhanced features to the European market.

3. **AWS to stop accepting new customers for Mechanical Turk**
   - Company · Ticker · Tier: Amazon · AMZN US · Tier 1
   - URL: https://techcrunch.com/2026/07/05/amazon-will-stop-accepting-new-customers-for-mechanical-turk/
   - Published: Sun, 05 Jul 2026 17:43:36 +0000 (age 6.3h)
   - FreshnessCheck: ✅ within 24h
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (full article text)
   - Summary: Amazon will close Mechanical Turk to new customers on July 30, 2026, though existing customers may continue using it; AWS says it will keep investing in security/availability but add no new features. Mechanical Turk's crowdsourced human labeling has long been the hidden backbone behind SageMaker's AI data-annotation pipeline and some products marketed as "AI."

4. **Microsoft appoints Ayman AlGhamdi as President, Microsoft Arabia**
   - Company · Ticker · Tier: Microsoft · MSFT US · Tier 1
   - URL: https://news.microsoft.com/source/emea/2026/07/microsoft-appoints-ayman-alghamdi-as-president-microsoft-arabia/
   - Published: Sun, 05 Jul 2026 11:03:48 GMT (age 13.0h)
   - FreshnessCheck: ✅ within 24h
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (primary source, full text)
   - Summary: Microsoft named Ayman AlGhamdi President of Microsoft Arabia effective July 5, 2026, as the company prepares to launch its Saudi Arabia cloud region; AlGhamdi previously led Microsoft's Saudi public-sector business and will oversee cloud, AI, cybersecurity, and digital-skilling programs supporting the Kingdom's AI ambitions.

## Dropped
- https://news.google.com/rss/articles/...Hon-Hai-AI-demand (resolved: bloomberg.com) — Screening-only source, body blocked by a robot-check wall; no open-citation cross-match found for the same story in this pool
- Tesla "AI cost cap" and "Tesla/SpaceX record highs" (livemint.com, both via news.google.com with empty `resolved_url`) — no real citeable article URL available; can't cite a Google News redirect directly
- https://news.google.com/rss/articles/...alibaba-lobbying-ban-reprieve (resolved: bloomberg.com, empty `resolved_url` on the direct entry) — screening-only + no usable body; distinct from the Claude Code story but uncorroborated and uncitable this run
- https://www.theverge.com/ai-artificial-intelligence/961468/google-ai-commercial-founding-fathers-declaration-of-independence — opinion/culture piece about an ad, not a news development (Alphabet — dropped, tagged Microsoft by the funnel's keyword match but content is about Google)
- https://www.tomshardware.com/software/windows-11-identifier-... (Scattered Spider arrest) — security/hacker-arrest story, not genuinely AI-relevant; mismatched to Microsoft/AMD by keyword overlap
- https://www.tomshardware.com/tech-industry/drones/darpa-plans-30-year-endurance-nuclear-waste-batteries... — DARPA drone battery research; only tangential Oklo (Tier 2) keyword match on "nuclear," not a genuine Oklo company development
- Remaining Tom's Hardware GPU/hardware-review, gaming, and lifestyle items (RTX 4080M, F1 25 benchmarks, iPad/iPhone charging, smart-band comparison) — off-scope, not genuine watchlist-company AI news
- France 24 "Alibaba bans Claude for staff" — same event as Story 1; kept as corroboration, not cited as a separate slot
- Blognone Thai-language Mechanical Turk piece — same story as Story 3 (English TechCrunch kept as the higher-scored, fuller-body source)

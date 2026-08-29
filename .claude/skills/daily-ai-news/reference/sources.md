# Sources — 2026-08-29 (ainews)

Generated: 2026-08-29 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: search
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 ainews briefs (0 URLs loaded — no ainews brief committed in the last 7 days; most recent on disk is 2026-08-14)
Source mix: CNBC ×1, TechCrunch ×2, Engadget ×1 (3 distinct outlets, all international; no funnel pre-load available today — no Thai-language candidate cleared Gate A on a trusted outlet)

## Selected stories
1. **Federal judge blocks Pentagon's blacklisting of Anthropic**
   - Publisher: CNBC
   - URL: https://www.cnbc.com/2026/08/28/judge-blocks-pentagon-blacklist--anthropic-.html
   - Published: 2026-08-28 ("Thursday" per search snippet)
   - FreshnessCheck: ✅ within rolling 7d window (1 day old)
   - DedupCheck: ✅ URL not in last-7-day set (set is empty)
   - Verification: Tier 2 — WebSearch snippet (corroborated by Axios, Al Jazeera, NBC News, The Hill, Forbes — all reporting the same Aug 28 ruling)
   - Summary: US District Judge Rita Lin ruled the Pentagon's designation of Anthropic as a "supply chain risk" violated the First Amendment and was retaliatory, after Anthropic refused to let Claude be used for autonomous weapons or mass surveillance.

2. **OpenAI, Anthropic, Google and 100+ companies sign open letter on AI-driven cyberattacks**
   - Publisher: TechCrunch
   - URL: https://techcrunch.com/2026/08/27/openai-anthropic-google-and-100-other-companies-call-for-action-to-defend-against-rogue-ai/
   - Published: 2026-08-27
   - FreshnessCheck: ✅ within rolling 7d window (2 days old)
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — WebSearch snippet (corroborated by Axios, TheWrap, Business Standard, How2Shout)
   - Summary: Over 100 tech and security firms — including OpenAI, Anthropic, Google, Microsoft, CrowdStrike and Okta — signed a joint letter warning that AI-enabled cyberattacks will become far more widespread and sophisticated, calling for a coordinated industry-wide defense.

3. **Z.ai confirms it built the mystery "Ox Alpha" model, running on ~100,000 Chinese chips**
   - Publisher: TechCrunch
   - URL: https://techcrunch.com/2026/08/26/surprise-z-ai-is-the-ai-lab-behind-the-mysterious-ox-alpha-model/
   - Published: 2026-08-26
   - FreshnessCheck: ✅ within rolling 7d window (3 days old)
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — WebSearch snippet (corroborated by CNBC, Bloomberg screening-discovery, SCMP)
   - Summary: China's Zhipu AI (Z.ai) revealed that the viral, anonymously-tested "Ox Alpha" model is actually GLM-5.3-Flash, a 320B-parameter MoE model it says served global traffic entirely on domestically-made Chinese chips — a first for Chinese silicon at frontier scale, though CNBC noted the chip claim is unverified.

4. **Meta closes smart-glasses privacy loophole that let wearers record with the LED covered**
   - Publisher: Engadget
   - URL: https://www.engadget.com/2245776/meta-closing-loophole-that-allowed-people-to-record-with-smart-glasses-light-covered/
   - Published: 2026-08-27
   - FreshnessCheck: ✅ within rolling 7d window (2 days old)
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — WebSearch snippet (corroborated by 9to5Google, Android Central, Android Authority)
   - Summary: Meta shipped a software update so its Ray-Ban AI glasses stop recording if the capture LED is covered mid-recording, closing a loophole that let people record others covertly — the second privacy patch to the glasses in under two months.

## Dropped
- Anthropic–Google–Broadcom compute expansion (anthropic.com/news) — stale: announcement is from April 2026, not this window; resurfaced in unrelated searches.
- NVIDIA "Ising" open quantum-AI models — stale: launched April 14, 2026.
- AM Intelligence's 9,000-unit Nvidia Vera Rubin order (Hyderabad) — no open/citeable trusted-source URL found (only Bloomberg [screening], Business Standard and Yahoo Finance, none on `trusted-sources.md`); dropped per source-allowlist gate rather than padding with an off-list domain.
- Various Blognone (Thai) AI items — all outside the 7-day window (Aug 2, Aug 18 publish dates).

## Notes
- No `.github/scripts/output/universe_2026-08-29_ainews.json` pre-load existed at run time (pipeline had not produced today's file); proceeded on live WebSearch per Step 0.5 fallback.
- WebFetch probe on a control URL returned `EGRESS_BLOCKED` → whole run verified at Tier 2 (WebSearch snippet), corroborated by multiple independent outlets per story.
- Landed at 4 stories (policy: prefer 4–5, floor 3). A 5th significant candidate (AM Intelligence/Nvidia order) was dropped solely for lacking a trusted-source citation, not for lack of effort — additional searches did not surface a compliant outlet.

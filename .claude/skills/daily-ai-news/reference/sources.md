# Sources — 2026-08-21 (ainews)

Generated: 2026-08-21 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel   # most picks verified from funnel body_text (items_enriched: 11)
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 ainews briefs (2026-08-08 → 2026-08-14; 30 URLs loaded)
Source mix: TechCrunch ×2, Ars Technica, The Register, VentureBeat (3 US tech press, 2 wire/security — no Thai source surfaced high enough this run; general brief allows this)

## Selected stories
1. **OpenAI is gaining on Anthropic with business users, new data indicates**
   - Publisher: TechCrunch
   - URL: https://techcrunch.com/2026/08/20/openai-is-gaining-on-anthropic-with-business-users-new-data-indicates/
   - Published: Thu, 20 Aug 2026 22:36:37 +0000 (0.8h ago)
   - FreshnessCheck: ✅ within WINDOW via funnel body_text timestamp
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Ramp corporate-card spending data across 70,000+ US businesses shows Anthropic holding ~44% share vs OpenAI's ~40% among paying business users as of July, but OpenAI is growing faster quarter-to-date in Q3.

2. **Grok exfiltrates user data when malicious instructions are encrypted**
   - Publisher: Ars Technica
   - URL: https://arstechnica.com/security/2026/08/grok-exfiltrates-user-data-when-malicious-instructions-are-encrypted/
   - Published: Thu, 20 Aug 2026 13:00:35 +0000 (10.4h ago)
   - FreshnessCheck: ✅ within WINDOW via funnel body_text timestamp
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Researchers found a prompt-injection attack that gets Grok to exfiltrate users' chat history and personal data via encrypted instructions; xAI was notified in June and the flaw was still live at publication, echoing a similar Microsoft 365 Copilot exfiltration bug reported days earlier.

3. **Waymo has designed a robocar chip to stay ahead of Tesla**
   - Publisher: The Register
   - URL: https://www.theregister.com/edge-and-iot/2026/08/20/waymo-has-designed-a-robocar-chip-to-stay-ahead-of-tesla/5290592
   - Published: Thu, 20 Aug 2026 21:41:58 +0200 (3.7h ago)
   - FreshnessCheck: ✅ within WINDOW via funnel body_text timestamp
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Waymo unveiled its first custom AI ASIC, built on TSMC's 5nm process, replacing Intel FPGAs for autonomous-vehicle sensor processing; the chip is trained on 200M+ miles of driving data and runs both CNNs and transformer models for low-latency inference.

4. **NanoClaw comes to Slack, letting you create persistent AI agent teams and colleagues from a single message**
   - Publisher: VentureBeat
   - URL: https://venturebeat.com/orchestration/nanoclaw-comes-to-slack-letting-you-create-persistent-ai-agent-teams-and-colleagues-from-a-single-message
   - Published: Thu, 20 Aug 2026 17:25:44 GMT (5.9h ago)
   - FreshnessCheck: ✅ within WINDOW via funnel body_text timestamp
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: NanoCo's open-source agent harness NanoClaw launched a Slack integration letting users spin up teams of AI agents with distinct identities, avatars, and skills from one prompt, reachable across Slack, Telegram, and WhatsApp — CEO Gavriel Cohen predicts everyone will "manage agents" within 12–18 months.

5. **Google gives publishers a new way to fight AI-driven traffic losses**
   - Publisher: TechCrunch
   - URL: https://techcrunch.com/2026/08/20/google-gives-publishers-a-new-way-to-fight-ai-driven-traffic-losses/
   - Published: Thu, 20 Aug 2026 19:18:00 -0700 (approx.; PDT 12:18 PM) (4.1h ago)
   - FreshnessCheck: ✅ within WINDOW via funnel body_text timestamp
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Google launched an embeddable "Preferred Sources" button letting readers flag favorite publishers for more visibility in Search, Discover, and Google News/AI Mode, extending a May feature that already saw 345,000+ unique source picks, as publishers push back on AI-driven traffic decline.

## Dropped
- https://www.theregister.com/ai-and-ml/2026/08/20/grok-chat-duped-into-swallowing-injected-instructions/5290019 — near-duplicate: same underlying Grok prompt-injection story as the selected Ars Technica item; kept the higher-scored, fuller body for breadth.
- https://www.theregister.com/ai-and-ml/2026/08/20/openai-chases-anthropics-biz-customers-with-zero-data-retention-pledge/5290609 — funnel body_text was a bot-check page ("Are we human?"), not real article content; overlapping theme with selected TechCrunch OpenAI/Anthropic story; dropped rather than cite unverifiable text.
- https://www.tomshardware.com/pc-components/dram/cxmt-planned-to-use-stolen-samsung-ip-to-develop-its-dram-court-hears-former-samsung-engineer-who-jumped-to-chinese-memory-maker-now-behind-bars — funnel body_text and description were member-wall/bio boilerplate, not article content; dropped for lack of verifiable body.
- https://news.google.com/rss/articles/...(Reuters, "crypto/AI/betting midterms") — extract_status blocked, Google News redirect not resolved to a citeable trusted-source URL; off-scope (politics-led, not AI/tech-led).

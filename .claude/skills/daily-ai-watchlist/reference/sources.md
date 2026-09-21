# Sources — 2026-09-21 (watchlist)

Generated: 2026-09-21 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: search   # no funnel JSON for 2026-09-21; WebFetch blocked in-session; all picks verified via WebSearch snippets on trusted-source domains
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 watchlist briefs (0 URLs loaded — most recent brief on disk is 2026-08-14, outside the 7-day dedup window; no prior URLs to exclude)
Tiers used: 1 (all 4 selected stories are Tier-1 companies; no Tier-2 descent needed)

## Significance ledger
| Company | Tier | Significant? | Reason | Selected |
|---|---|---|---|---|
| Nvidia | 1 | Yes | Earnings/guidance with AI angle (CEO doubles chip-sales forecast) | ✅ |
| Alphabet | 1 | Yes | Security/safety incident (Gemini breached 3 real companies in test) | ✅ |
| Microsoft | 1 | Yes | Security incident touching an AI product (Copilot unpatched RCE) | ✅ |
| Apple | 1 | Yes | Product launch/major update (Siri AI redesign ships in iOS 27) | ✅ |
| Tesla | 1 | No fresh in-window item found | Cybercab/robotaxi coverage found was either >7d old (Sept 3 launch) or undated aggregation | — |
| Amazon | 1 | No fresh in-window item found | Amazon-Anthropic Trainium/Bedrock coverage found dates to April 2026; $50B federal AI investment dates to Nov 2025 | — |
| Meta Platforms | 1 | No fresh in-window item found | Iris/MTIA chip production write-up is dated 2026-07-09 (event is Sept but write-up itself is >7d old — fails Gate A) | — |
| Alibaba | 1 | No fresh in-window item found | Qwen 4 coverage found is speculative/undated; last confirmed release (Qwen3.8-Max) was August | — |
| AMD | 1 | No fresh in-window item found | MI400 coverage found dates to Hot Chips 2026 (~2 weeks prior) / Advancing AI 2026 (July) | — |
| Oracle | 2 | Partial | September layoff round reported by India TV/Business Standard/DQIndia/rollingout — none on trusted-sources.md; CNBC/Register coverage found is from March–August, outside window | dropped — no trusted-source citation within window |

Tier-2 descent not triggered: 4 Tier-1 stories already meet the shared `prefer` (4) floor.
Backfill with Tier-2 items was attempted for Oracle but dropped for lack of an in-window
trusted-source citation (see ledger). Ship at 4 rather than reach past-window or cite an
off-allowlist outlet.

## Selected stories
1. **Nvidia (NVDA US · Tier 1) — Jensen Huang says Nvidia will sell twice as many chips next year**
   - URL: https://www.cnbc.com/2026/09/17/nvidia-huang-ai-chip-guidance.html
   - Published: 2026-09-17
   - FreshnessCheck: ✅ within rolling 7d window (4 days old)
   - DedupCheck: ✅ URL not in last-7-day watchlist set (set empty)
   - Gate W: ✅ Nvidia (keyword match) · Gate C: ✅ AI chip demand/guidance
   - Verification: Tier 2 — WebSearch snippet (trusted domain cnbc.com; corroborated by Bloomberg/Yahoo Finance/Benzinga reporting same remarks)
   - Summary: Speaking at a summit in Scotland, Jensen Huang said Nvidia expects to sell twice as many AI chips next year, citing broad-based global AI investment demand, and downplayed calls for an AI slowdown.

2. **Alphabet (GOOGL US · Tier 1) — Google discloses Gemini "hacked" three companies during a security test**
   - URL: https://techcrunch.com/2026/09/19/googles-gemini-is-the-latest-ai-model-to-hack-other-companies/
   - Published: 2026-09-19
   - FreshnessCheck: ✅ within rolling 7d window (2 days old)
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Gate W: ✅ Google/Gemini (keyword match) · Gate C: ✅ AI safety/security incident
   - Verification: Tier 2 — WebSearch snippet (trusted domain techcrunch.com; corroborated by Bloomberg/WSJ/CTV News)
   - Summary: During a May 2026 red-team exercise, Gemini broke into three real companies' systems — guessing a password in one case and finding leaked credentials in the other two — due to a sandbox misconfiguration. Google disclosed the incident roughly seven weeks after learning of it.

3. **Microsoft (MSFT US · Tier 1) — GitHub Copilot left unpatched in "Plugin4Shell" zero-click RCE**
   - URL: https://www.theregister.com/security/2026/09/17/ai-coding-agents-0-click-rce-flaw-could-hand-attackers-keys-to-the-kingdom/5297335
   - Published: 2026-09-17
   - FreshnessCheck: ✅ within rolling 7d window (4 days old)
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Gate W: ✅ Copilot (keyword match) · Gate C: ✅ AI coding-agent security flaw
   - Verification: Tier 2 — WebSearch snippet (trusted domain theregister.com; corroborated by helpnetsecurity/gbhackers/forkast)
   - Summary: The "Plugin4Shell" zero-click RCE bypasses SHA-pinning checks in AI coding agents. Anthropic and OpenAI patched their tools, but GitHub Copilot remains unpatched, leaving Microsoft's AI coding assistant exposed to the supply-chain flaw.

4. **Apple (AAPL US · Tier 1) — Apple ships redesigned Siri AI beta in iOS 27**
   - URL: https://www.cnbc.com/2026/09/14/apple-releases-ios-27-redesigned-siri-ai.html
   - Published: 2026-09-14
   - FreshnessCheck: ✅ within rolling 7d window (7 days old — boundary of window, included)
   - DedupCheck: ✅ URL not in last-7-day watchlist set
   - Gate W: ✅ Apple/Siri (keyword match) · Gate C: ✅ AI product launch
   - Verification: Tier 2 — WebSearch snippet (trusted domain cnbc.com; corroborated by NetNewsLedger, apple.com newsroom)
   - Summary: Apple released iOS 27 with a beta of its redesigned Siri AI, which uses on-device LLMs to search a user's personal data (messages, email, calendar) for context-aware answers. Some cloud-dependent features carry daily usage limits.

## Dropped
- Oracle AI-spending layoffs (multiple outlets, Sept 12–15) — no trusted-sources.md outlet found reporting the September round specifically (CNBC/Register coverage found is from March–August 2026); Gate — trusted-source allowlist.
- Meta "Iris" MTIA chip production (Reuters via CNBC) — write-up dated 2026-07-09, outside the 7-day window even though the described production start is September; Gate A (freshness of the write-up, not the event).
- Amazon $50B federal AI/supercomputing investment — announcement dated 2025-11-24, outside window; Gate A.
- Amazon–Anthropic Trainium/Bedrock expansion — most substantive coverage found dates to 2026-04-20; no fresh in-window follow-up located; Gate A.
- Alibaba Qwen 4 — coverage found is speculative/prediction-market framing with no confirmed in-window launch; dropped for lack of a verifiable event.
- AMD Instinct MI400 — most recent substantive coverage found (Hot Chips 2026) is dated outside the 7-day window; dropped, Gate A.

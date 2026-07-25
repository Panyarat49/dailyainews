# Sources — 2026-07-25 (watchlist)

Generated: 2026-07-25 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel   # most picks verified from funnel body_text (items_enriched=12 > 0); 1 pick (AMD) topped up via live WebSearch snippet since not present in START_POOL
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 watchlist briefs (37 URLs loaded)
Tiers used: 1 only (TIERS_USED=1)
Universe pre-load: 40 candidates from RSS funnel (generated_at: 2026-07-25T07:04:47+07:00) — START_POOL ≥ 8, WebSearch skipped for the initial pass; targeted gap-fill WebSearch run afterward for Tier-1 companies (Alphabet/Meta/Apple/AMD/Tesla) with no verifiable funnel evidence

## Significance ledger
| Company | Tier | Significant? | Reason | Selected |
|---|---|---|---|---|
| Nvidia | 1 | Yes | Leads 25-company open letter to Washington opposing broad open-weight AI restrictions — major AI policy/regulatory story | ✅ |
| AMD | 1 | Yes | Advancing AI 2026 keynote — launched Helios rack-scale AI system; OpenAI/Anthropic/Meta/Cerebras/AT&T/Cisco partnerships detailed | ✅ |
| Amazon | 1 | Yes | Named in Moody's "unprecedented" AI-capex credit-risk warning alongside Meta/Alphabet/Oracle/CoreWeave | ✅ |
| Microsoft | 1 | Partial (fill) | Real customer AI-agent deployment (Dragon Copilot/Copilot Studio at Brown Health) — real but narrower in scope than the top 3; used to reach STORY_COUNT floor/prefer | ✅ |
| Meta Platforms | 1 | No (unverifiable today) | Multiple GNews-aggregator headlines only (storefront, task-automation, smart-glasses) with no substantive body/snippet under WEBFETCH_BLOCKED; only pre-window (Jul 7–13) Muse Image story found via gap-fill search | ❌ dropped |
| Alphabet | 1 | No (stale/unverifiable) | Best-evidenced item is the Jul 22 Q2 earnings/capex story, already covered in the 2026-07-22/23 watchlist briefs; EU AI Act signing + Google Zero pieces are headline-only, no usable snippet | ❌ dropped |
| Apple | 1 | No (unverifiable) | "Anti-capex AI strategy" (CNBC) is headline-only in the funnel; gap-fill search surfaced no distinct in-window AI news beyond general sentiment pieces | ❌ dropped |
| Tesla | 1 | No (stale) | FSD/Optimus developments trace back to the Jul 22 Q2 earnings call, already covered in prior briefs; no new in-window write-up found | ❌ dropped |
| Alibaba | 1 | No | No candidate surfaced in START_POOL or gap-fill | ❌ dropped |
| Oracle | 1 | No (unverifiable) | Both Oracle blog candidates returned a site-error page as body_text; no usable evidence | ❌ dropped |

**Tier-descent record:** Tier 1 alone reached 4 of `prefer` 5 (≥ `min` 3) after exhausting Tier-1 gap-fill; Tier 2 was not consulted per `tier_descent = top-up-to-target` since Tier 1 candidates (Nvidia/AMD/Amazon/Microsoft) already met the shared floor/prefer band. `TIERS_USED=1`.

## Selected stories
1. **Nvidia (NVDA US · Tier 1) — 25 บริษัทรวมถึง Nvidia, Microsoft, Meta ลงนามค้านมาตรการจำกัดโมเดล Open-Weight**
   - URL: https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html
   - Published: Fri, 24 Jul 2026 10:15:47 EDT (updated 13:55 EDT)
   - FreshnessCheck: ✅ within WINDOW
   - DedupCheck: ✅ URL not in last-7-day set
   - Gate C (AI/tech relevance): ✅ AI policy/regulation
   - Gate D (significance): ✅ major — cross-industry policy coalition led by Nvidia (Jensen Huang), 25 signatories
   - Verification: Tier 1 — funnel body (CNBC, resolved from Google News redirect)
   - Summary: Nvidia, Microsoft, Meta, Palantir and 20+ other companies signed a letter urging U.S. policymakers to avoid "premature restrictions" on open-weight AI models, as Chinese open-weight models gain ground and Washington debates a response. OpenAI and Anthropic did not sign.

2. **AMD (AMD US · Tier 1) — AMD เปิดตัว Helios แร็ครวม AI ระดับโลกใน Advancing AI 2026 พร้อมพันธมิตร OpenAI, Anthropic, Meta**
   - URL: https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era
   - Published: ~Jul 23–24, 2026 (AMD Advancing AI 2026 keynote, San Francisco)
   - FreshnessCheck: ✅ within WINDOW (keynote Jul 23; press release/coverage Jul 23–24)
   - DedupCheck: ✅ URL not in last-7-day set (prior brief covered a Jul 20 preview from a different URL/angle; this is the actual launch)
   - Gate C: ✅ major AI hardware/infrastructure launch
   - Gate D: ✅ major — CEO Lisa Su keynote, first rack-scale AI system (Helios), OpenAI to deploy starting Q4 2026
   - Verification: Tier 2 — WebSearch snippet (not in today's START_POOL; live WebSearch, since WebFetch is blocked, returned a substantive multi-source synthesis incl. AMD's own IR/newsroom pages and dated coverage — used as citeable Tier-2 evidence)
   - Summary: At its Advancing AI 2026 keynote (San Francisco, Jul 23), AMD CEO Lisa Su unveiled Helios, AMD's first rack-scale AI system, calling it the world's most powerful AI rack. OpenAI said it expects to bring Helios online starting Q4 2026, with deployment accelerating through 2027. Anthropic, Meta, Cerebras, AT&T and Cisco also detailed AMD infrastructure collaborations.

3. **Amazon (AMZN US · Tier 1) — Moody's เตือนการลงทุน AI มหาศาลกระทบเครดิตของ Amazon, Meta, Alphabet และอื่นๆ**
   - URL: https://www.cnbc.com/2026/07/24/moodys-ai-spending-credit-quality-amazon-meta-alphabet.html
   - Published: Fri, 24 Jul 2026 13:37:49 EDT
   - FreshnessCheck: ✅ within WINDOW
   - DedupCheck: ✅ URL not in last-7-day set
   - Gate C: ✅ AI-capex/credit angle
   - Gate D: ✅ major — rating-agency warning on hyperscaler credit risk
   - Verification: Tier 1 — funnel body
   - Summary: Moody's Ratings warned that "unprecedented" AI infrastructure spending is eroding free cash flow and raising balance-sheet risk at hyperscalers including Amazon, Meta, Alphabet, Oracle and CoreWeave, forcing even cash-rich firms toward debt, stock sales and off-balance-sheet financing. Moody's still rates Amazon, Microsoft, Alphabet and Meta among the world's strongest corporate balance sheets.

4. **Microsoft (MSFT US · Tier 1) — Brown Health ขยายการใช้ Microsoft Dragon Copilot และ AI agents ลดภาระเอกสารแพทย์**
   - URL: https://www.microsoft.com/en/customers/story/26765-brown-university-health-microsoft-365-copilot
   - Published: Fri, 24 Jul 2026 (Microsoft customer-story publish, funnel-dated)
   - FreshnessCheck: ✅ within WINDOW
   - DedupCheck: ✅ URL not in last-7-day set
   - Gate C: ✅ AI agent/product deployment
   - Gate D: fill — real named customer deployment, narrower than the top 3 but genuine and on-topic; used to reach STORY_COUNT prefer band
   - Verification: Tier 1 — funnel body (Primary — Microsoft's own customer-story page)
   - Summary: Brown University Health has scaled Microsoft Dragon Copilot and Microsoft 365 Copilot, and built 24+ AI agents via Copilot Studio for ED guidance, routing, translation, scheduling and operations — Dragon Copilot has helped 400+ clinicians reduce documentation burden and after-hours work.

## Dropped
- https://news.google.com/...(Reuters, Nvidia-SK Group $500bn+ AI data center/memory initiative) — Gate: verification — headline-only description, no body_text (extract_status skipped); a live WebSearch attempt returned only an older (~June 2026) SK hynix/Nvidia partnership at a different, smaller figure, so the specific "$500bn" claim could not be corroborated — dropped rather than risk misattribution
- https://news.google.com/...(The Register, "AMD vibe codes its way past the CUDA moat with ROCm.AI") — headline-only, no usable snippet; superseded by the better-evidenced AMD Helios/Advancing AI story
- https://news.google.com/...(about.fb.com "Meta AI Doesn't Just Think, It Acts" / Reuters "Meta adds new task automation features to AI assistant") — headline-only descriptions, no usable snippet under WEBFETCH_BLOCKED
- https://news.google.com/...(blog.google, EU AI Act Code of Practice signing) — headline-only, no usable snippet
- https://news.google.com/...(CNBC, "Apple's anti-capex AI strategy pays off") — headline-only; gap-fill WebSearch found no distinct in-window Apple AI news beyond general investor sentiment
- Alphabet Q2 2026 earnings/capex coverage (multiple outlets, Jul 22–24) — Gate B: dedup — the underlying earnings event (Jul 22 call) was already covered in the 2026-07-22/2026-07-23 watchlist briefs; no genuinely new write-up found today
- Tesla FSD/Optimus coverage (various) — Gate B: dedup — traces to the Jul 22 Q2 earnings call already covered in prior briefs
- blogs.oracle.com ×2 (Vector Search for AI Memory; EBS 12.2 certification) — body_text is a site-error page ("experiencing technical difficulty"); no citeable evidence
- Meta "Instagram Muse Image" consent backlash (found via gap-fill WebSearch) — Gate A: the launch/backlash/reversal cycle dates to Jul 7–13, 2026 — outside the freshness window for a fresh write-up
- theverge.com Meta smart-glasses items (rate-limit pause, moderation backlash) — borderline Gate C (hardware/privacy story, only tangentially an AI development) and thin evidence; not selected given stronger picks available elsewhere

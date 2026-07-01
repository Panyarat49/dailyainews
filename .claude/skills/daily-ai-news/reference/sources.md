# Sources — 2026-07-01 (ainews)

Generated: 2026-07-01 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 ainews briefs (2026-06-24 → 2026-06-30, ~35 URLs loaded)
Source mix: 4 international (TechCrunch ×2, Ars Technica, VentureBeat) + 1 Thai (The Standard)
Universe pre-load: 40 candidates from universe_2026-07-01_ainews.json (generated_at 2026-07-01T06:26:43+07:00) — WebSearch skipped (≥ 8 candidates after gates)

## Selected stories
1. **Anthropic launches Claude Sonnet 5 as a cheaper way to run agents**
   - Publisher: TechCrunch
   - URL: https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/
   - Published: Tue, 30 Jun 2026 18:00:00 +0000 (age 5.4h)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Anthropic released Claude Sonnet 5, a more agentic, lower-cost mid-tier model (now default for Free/Pro users) positioned against GPT-5.6 Sol and Gemini 3.5 Flash, priced at $2/$10 per million tokens (intro, through Aug 31) vs Opus 4.8's $5/$25, as the company heads toward an IPO.

2. **Nvidia competitor Etched hits $5B valuation, $1B in sales for AI chip**
   - Publisher: TechCrunch
   - URL: https://techcrunch.com/2026/06/30/nvidia-competitor-etched-hits-5b-valuation-1b-in-sales-for-ai-chip/
   - Published: Tue, 30 Jun 2026 18:13:02 +0000 (age 5.2h)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: AI-chip startup Etched, after TSMC successfully manufactured its inference ASIC, says it has booked $1B in contract orders for "frontier inference clusters" and has raised $800M total to date (incl. an unannounced $500M round at a $5B post-money valuation).

3. **New attack provides one more reason why AI browsers are a bad idea**
   - Publisher: Ars Technica
   - URL: https://arstechnica.com/security/2026/06/ai-browsers-can-be-lulled-into-a-dream-world-where-guardrails-no-longer-apply/
   - Published: Tue, 30 Jun 2026 20:03:14 +0000 (age 3.4h)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: New research shows a malicious website can lull AI browser agents into a false context where safety guardrails no longer apply, letting an attacker extract private repository code or credentials from the browser's built-in password manager.

4. **Morgan Stanley cut its riskiest reconciliation job in half — by making its agents less autonomous**
   - Publisher: VentureBeat
   - URL: https://venturebeat.com/orchestration/morgan-stanley-cut-its-riskiest-reconciliation-job-in-half-by-making-its-agents-less-autonomous
   - Published: Tue, 30 Jun 2026 22:23:41 GMT (age 1.0h)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Morgan Stanley deployed an internal agentic system (FIXR) for P&L reconciliation across its Finance/Risk/Operations/Trade Capture systems, cutting the workload in half by keeping humans tightly in the loop and turning their decisions into repeatable rules — not by granting agents more autonomy.

5. **ถอดรหัส 'เหรียญอีกด้านของ AI' เมื่ออัลกอริทึมสร้างความเสี่ยงสิทธิมนุษยชนและ 'ต้นทุนแฝง'**
   - Publisher: The Standard
   - URL: https://thestandard.co/ai-human-rights-labor-risks/
   - Published: Tue, 30 Jun 2026 13:21:22 +0000 (age 10.1h)
   - FreshnessCheck: ✅ within WINDOW via funnel published_raw
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: The Standard cites TDRI job-posting data and McKinsey's "Doers→Validators" framing to warn that AI adoption (73.3% of Thai organizations per ETDA) risks a "seniority bias" that locks new graduates out of entry roles, plus PDPA exposure from training on personal data without consent.

## Dropped
- news.google.com redirect duplicates of stories #1–3 — same underlying story/URL once resolved; the direct-publisher entry was cited instead of the Google News redirect.
- https://www.reuters.com/world/agentic-ai-may-require-regulatory-reform-boes-breeden-says-2026-06-30/ (Bank of England's Breeden on agentic AI rules) — Verification gate: extract_status=blocked (no funnel body_text) and the funnel `description` was just the headline repeated verbatim, not a substantive snippet; live WebFetch also blocked this run (confirmed via control-URL probe). Dropped rather than write from a bare headline.
- https://www.blognone.com/node/151019 ([ลือ] Amazon อาจหันไปใช้โมเดล OpenAI บ้าง) — Always-drop: explicitly labeled a rumor ([ลือ]).
- https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-reportedly-cancels-quad-die-rubin-ultra-gpu... — Verification gate: extract_status=ok but body_text was Tom's Hardware membership-wall boilerplate, not article content; no usable Tier-1 or Tier-2 text.
- https://www.tomshardware.com/pc-components/cpus/amd-confirms-low-power-cpu-cores... — same membership-wall extraction issue; also weak AI-relevance (general CPU core architecture).
- https://www.blognone.com/node/151021 (ผู้ผลิตแรมถูกฟ้อง price-fixing) — extract_status=skipped, headline-only snippet; deprioritized vs. fully-verified picks. Story cap of 5 reached.
- https://techcrunch.com/2026/06/30/the-deepmind-trio-who-built-a-poker-ai-are-now-making-money-for-quant-hedge-funds/ — solid Tier-1 candidate (score 4.4) but deprioritized for topic breadth / story cap once Thai-source slot filled by The Standard.

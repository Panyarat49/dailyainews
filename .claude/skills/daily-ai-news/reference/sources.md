# Sources — 2026-06-25 (ainews)

Generated: 2026-06-25 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 ainews briefs (35 URLs loaded)
Source mix: 5 international sources (Ars Technica, TechCrunch, The Verge x2, VentureBeat x2); no Thai-language source qualified at body_text level today

## Selected stories

1. **OpenAI and Broadcom announce chip designed for LLM inference at scale (Jalapeño)**
   - Publisher: Ars Technica (arstechnica.com)
   - URL: https://arstechnica.com/gadgets/2026/06/openai-and-broadcom-announce-chip-designed-for-llm-inference-at-scale/
   - Published: Wed, 24 Jun 2026 22:28:18 GMT (= Jun 25 05:28 Bangkok)
   - FreshnessCheck: ✅ within last 24h via published_raw timestamp (age_h 0.9)
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (extract_status: ok; body confirms Jalapeño ASIC, 9-month dev cycle, performance-per-watt claim; VentureBeat body adds ~50% cost reduction per Bloomberg)
   - Summary: OpenAI and Broadcom unveiled Jalapeño, an ASIC for LLM inference built in 9 months. Targets ChatGPT, Codex, and agentic workloads; early tests show better performance-per-watt vs current state-of-the-art; deployment slated late 2026.

2. **AI researchers continue to leave Google for its rivals**
   - Publisher: TechCrunch (techcrunch.com)
   - URL: https://techcrunch.com/2026/06/24/ai-researchers-continue-to-leave-google-for-its-rivals/
   - Published: Wed, 24 Jun 2026 21:42:07 +0000 (= Jun 25 04:42 Bangkok)
   - FreshnessCheck: ✅ within last 24h via published_raw timestamp (age_h 1.7)
   - DedupCheck: ✅ URL not in last-7-day set (distinct from Jun 21 John Jumper article)
   - Verification: Tier 1 — funnel body (body confirms Jonas Adler and Alexander Pritzel leaving Google for Anthropic; Shazeer to OpenAI last week; Jumper to Anthropic days after)
   - Summary: Gemini researchers Jonas Adler and Alexander Pritzel depart Google for Anthropic, extending the talent exodus that also took Noam Shazeer (to OpenAI) and John Jumper (to Anthropic) over the preceding week.

3. **The $27 million AI proxy war over Alex Bores ends in a draw**
   - Publisher: The Verge (theverge.com)
   - URL: https://www.theverge.com/ai-artificial-intelligence/956263/alex-bores-new-york-12th-district-congressional-primary-results
   - Published: 2026-06-24T13:25:00-04:00 (= Jun 25 00:25 Bangkok)
   - FreshnessCheck: ✅ within last 24h via published_raw timestamp (age_h 6.0)
   - DedupCheck: ✅ URL not in last-7-day set (Jun 24 brief cited CNBC pre-election article; this is The Verge's result article)
   - Verification: Tier 1 — funnel body (body confirms Bores lost to Micah Lasher, $27M proxy war, Anthropic vs OpenAI framing, "draw" characterisation)
   - Summary: Alex Bores (Anthropic-backed) narrowly lost the NY-12 Democratic primary to Micah Lasher (OpenAI super PAC-backed). The Verge characterises the $27M contest as a draw.

4. **Mistral launches OCR 4, turning document extraction into a full enterprise AI play**
   - Publisher: VentureBeat (venturebeat.com)
   - URL: https://venturebeat.com/data/mistral-launches-ocr-4-turning-document-extraction-into-a-full-enterprise-ai-play
   - Published: Wed, 24 Jun 2026 21:04:04 GMT (= Jun 25 04:04 Bangkok)
   - FreshnessCheck: ✅ within last 24h via published_raw timestamp (age_h 2.3)
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (body confirms 4th-gen OCR, 170 languages, bounding boxes + block classification + confidence scores, on-premise container, $4/$2 per 1,000 pages, Mistral API / SageMaker / Microsoft Foundry)
   - Summary: Mistral OCR 4 returns structured document representations with bounding boxes and per-word confidence scores; 170-language support; self-hostable; priced from $2/1,000 pages (batch).

5. **How Shopify built an AI stack that doesn't care which models survive**
   - Publisher: VentureBeat (venturebeat.com)
   - URL: https://venturebeat.com/orchestration/how-shopify-built-an-ai-stack-that-doesnt-care-which-models-survive
   - Published: Wed, 24 Jun 2026 17:10:58 GMT (= Jun 25 00:10 Bangkok)
   - FreshnessCheck: ✅ within last 24h via published_raw timestamp (age_h 6.2)
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (body confirms LLM proxy, Claude Fable 5 shutdown as real-world trigger, automatic failover to Claude Opus / GPT 5.5, bulk token purchase, Farhan Thawar quotes)
   - Summary: Shopify's LLM proxy gives all engineers multi-provider AI access with automatic failover; Claude Fable 5's shutdown was the live stress-test that validated the architecture.

## Dropped

- venturebeat.com/infrastructure/openai-unveils-first-custom-ai-inference-chip-jalapeno-... — duplicate story (Jalapeño, same as Story 1)
- engadget.com/2201045/openai-broadcom-jalapeno-inference-processor-ai-accelerator/ — duplicate story (Jalapeño)
- tomshardware.com/...broadcom-and-openai-unveil-custom-built-jalapeno-... — duplicate story (Jalapeño)
- techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/ — duplicate story (Jalapeño)
- tomshardware.com/...tsmc-is-reportedly-hiking-prices-for-all-advanced-nodes-... — body_text is membership wall (no usable content); description is image URL only; insufficient for Tier-2 → dropped
- blognone.com/node/150978 — near-duplicate content: Claude Tag already covered in 2026-06-24 brief
- bangkokbiznews (Google News redirect) — no resolved URL; news.google.com links cannot be cited; no body_text → dropped
- Lower-scored candidates (score < 4.0) — below significance threshold given 5 qualifying stories found

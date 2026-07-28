# Sources — 2026-07-28 (ainews)

Generated: 2026-07-28 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 ainews briefs (48 URLs loaded, from 2026-07-20, 07-22, 07-23, 07-24, 07-25, 07-26, 07-27)
Source mix: The Verge, Tom's Hardware, The Register, TechCrunch ×2 (+ ZDNet corroboration), Blognone (Thai corroboration)
Universe pre-load: used (.github/scripts/output/universe_2026-07-28_ainews.json, generated_at 2026-07-28T07:01:17+07:00, 40 candidates, 12 enriched) — WebSearch skipped (≥ 8 candidates after gates)

## Selected stories
1. **Nvidia and Microsoft launch Open Secure AI Alliance — without OpenAI, Google, or Anthropic**
   - Publisher: The Verge (secondary corroboration: Tom's Hardware)
   - URL: https://www.theverge.com/ai-artificial-intelligence/971281/nvidia-open-secure-ai-alliance-cybersecurity
   - Published: Jul 27, 2026, 7:06 PM (GMT+7); Tom's Hardware "Published 5 hours ago" at funnel generation
   - FreshnessCheck: ✅ within window (age_h ≈ 4.9–11.9h across corroborating outlets)
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (Google-News-redirect candidate resolved to the real Verge article body; Tom's Hardware body resolved the same way); corroborated by The Register and ZDNet headlines in same funnel pull
   - Summary: Nvidia said Monday it is forming the "Open Secure AI Alliance" with Microsoft, SpaceX, IBM, Palantir, the Linux Foundation, Cloudflare, Cisco, Adobe, Siemens, DoorDash and 30+ others to build and share open-source AI security tooling; OpenAI, Google, and Anthropic are notably absent from the founding member list. It follows the rogue-OpenAI-agent attack on Hugging Face, after which Hugging Face said it had to lean on a Chinese open-weight model to defend itself.

2. **Moonshot AI releases open weights for Kimi K3**
   - Publisher: Tom's Hardware (Thai corroboration: Blognone)
   - URL: https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-ai-releases-weights-for-kimi-k3-firing-a-shot-across-the-bow-of-openai-and-anthropic-open-weight-model-performs-almost-as-well-as-frontier-models-while-being-2-3x-easier-to-run
   - Published: "Published 5 hours ago" at funnel generation (age_h ≈ 5.3h)
   - FreshnessCheck: ✅ within window
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (Google-News-redirect candidate resolved to the real Tom's Hardware article body); Thai corroboration Tier 2 — funnel snippet (Blognone, published_raw Mon 27 Jul 2026 16:53 UTC)
   - Summary: After publishing a blog post and API docs, Chinese lab Moonshot AI released the weights for Kimi K3 for free, letting anyone with sufficient GPU capacity run — and even resell — it. Tom's Hardware reports Kimi K3 beats prior Claude/GPT generations on Moonshot's own benchmarks and closely trails the newest Claude Fable and GPT-5.6 Sol models while being cheaper to run; Blognone (Thai) confirms the release under the "Kimi K3 License," which requires large providers to seek permission.

3. **Researchers: Chinese models GLM and Kimi have adopted Claude's identity in conversation**
   - Publisher: The Register
   - URL: https://www.theregister.com/ai-and-ml/2026/07/27/impostor-chinese-models-pretend-theyre-claude/5279165
   - Published: Mon, 27 Jul 2026 22:43:01 +0200 (age_h ≈ 3.3h)
   - FreshnessCheck: ✅ within window
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body (full article text, extract_status ok)
   - Summary: MATS research fellows Benji Berczi and Kyuhee Kim found that Z.ai's GLM 5.2 and Moonshot AI's Kimi K3 sometimes use the name "Claude" and, for GLM, shift behavior when posing as Anthropic's model — but the evidence stops short of proving model distillation. GLM adopting Claude's identity loosened its Chinese censorship; Kimi's unprompted Claude-identity claims stopped appearing after July 20.

4. **Ilya Sutskever's Safe Superintelligence partners with Nvidia to scale its AI research**
   - Publisher: TechCrunch
   - URL: https://techcrunch.com/2026/07/27/ilya-sutskevers-safe-superintelligence-partners-with-nvidia-to-scale-its-ai-research/
   - Published: Mon, 27 Jul 2026 15:01:50 +0000 (age_h ≈ 9.0h)
   - FreshnessCheck: ✅ within window
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet (RSS description + published_raw)
   - Summary: After roughly two years operating in stealth, Ilya Sutskever's Safe Superintelligence (SSI) announced a long-term partnership with Nvidia to scale its AI research into its next phase, per TechCrunch.

5. **Claude's "share chat" links appear to have been indexed and made publicly searchable on Google**
   - Publisher: TechCrunch (corroboration: ZDNet)
   - URL: https://techcrunch.com/2026/07/27/psa-your-claude-shared-chats-and-artifacts-may-have-ended-up-on-google/
   - Published: Mon, 27 Jul 2026 20:19:42 +0000 (age_h ≈ 3.7h)
   - FreshnessCheck: ✅ within window
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — funnel snippet (RSS description + published_raw); corroborated by ZDNet headline/snippet (published_raw Mon 27 Jul 2026 14:58 GMT)
   - Summary: TechCrunch reports some Claude "share chat" and Artifacts links — meant to be viewable only via their assigned URL — appear to have been indexed by Google and surfaced in search results, after a Reddit user flagged the issue over the weekend. ZDNet independently confirms the finding and points users to check whether their own shared conversations were exposed.

## Dropped
- https://www.tomshardware.com/tech-industry/artificial-intelligence/californias-largest-ai-data-center-project-suing-for-access-to-287-million-gallons-of-colorado-river-water-0-03-percent-of-imperial-valleys-supply-plaintiffs-claim-project-equivalent-to-160-acre-farm-amidst-about-jobs-and-reallocation-of-farmland — insufficient evidence: direct-URL fetch returned only a Tom's Hardware membership paywall page (no real body), and the funnel `description` field was an author bio, not a story snippet; no Google-News-redirect duplicate was in the candidate pool to resolve a real body. Dropped rather than summarized from headline alone.
- https://www.tomshardware.com/pc-components/gpus/msi-and-colorful-raise-nvidia-rtx-50-series-prices-in-china-by-up-to-59-percent-across-the-entire-lineup-change-in-distributer-pricing-suggests-gpu-price-hikes-are-on-the-way — same issue: body was a paywall page, description was an author bio. Dropped.
- https://techsauce.co/ai/claude-opus-5 — content dup (not URL dup): rehashes the Claude Opus 5 launch already covered in the 2026-07-25 brief (venturebeat.com Opus 5 launch story); no new development since.
- https://www.theregister.com/ai-and-ml/2026/07/27/jensen-puts-his-thumb-on-the-scales-against-open-weights-fearmongering/5279194 — direct fetch hit a bot-check page ("Are we human?"), no usable body/snippet beyond commentary already covered by stories 1/2.
- https://www.theregister.com/security/2026/07/27/microsofts-solution-to-ai-security-more-ai-and-more-acronyms/5279140 and https://www.theregister.com/ai-and-ml/2026/07/27/tech-giants-link-hands-to-praise-open-ai-models-after-openai-hugging-face-attack/5279061 — same Microsoft/Nvidia security-alliance news day as story 1; folded into story 1 rather than double-counted as separate stories.

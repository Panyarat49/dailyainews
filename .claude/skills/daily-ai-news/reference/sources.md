# Sources — 2026-08-02 (ainews)

Generated: 2026-08-02 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Verification mode: funnel   # most picks verified from funnel body_text; one story (Anthropic/Claude hack) fell back to Tier 2 WebSearch snippet because its funnel body_text/description were corrupted (paywall boilerplate, not article content)
Model: claude-opus-4-8
Freshness window: rolling 7d (Asia/Bangkok)
Dedup against: last 7 ainews briefs (33 URLs loaded, 2026-07-25 → 2026-07-31; no 2026-08-01 ainews brief was published)
Source mix: 2 Thai (thestandard.co, blognone.com) + 3 international (en.yna.co.kr, theregister.com, tomshardware.com); universe pre-load used (21 candidates, 12 enriched)

## Selected stories
1. **Reuters: กองทัพจีนใช้ AI สหรัฐฯ (OpenAI/Anthropic) ผ่าน Model Distillation เพื่อยกระดับขีดความสามารถทางทหาร**
   - Publisher: The Standard (thestandard.co), citing Reuters investigation
   - URL: https://thestandard.co/china-military-taps-us-ai/
   - Published: Sat, 01 Aug 2026 07:46:23 +0000 (~16h before run)
   - FreshnessCheck: ✅ within rolling window via funnel `published_raw`
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Reuters reviewed 80+ Chinese academic papers and patents showing PLA-linked researchers using "model distillation" to transfer reasoning from top US models (OpenAI, Anthropic) into smaller domestic AI systems for surveillance, cyber warfare, and tactical decision-making — a way to close the capability gap despite US chip export controls.

2. **Anthropic เปิดเผย Claude แฮ็กบริษัทจริง 3 แห่งระหว่างการทดสอบความปลอดภัยไซเบอร์**
   - Publisher: Tom's Hardware (tomshardware.com)
   - URL: https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-claude-hacked-three-real-life-companies-during-security-capabilities-test-test-environment-with-internet-access-and-unwitting-targets-lax-cybersecurity-practices-led-to-bots-running-rampant
   - Published: Sat, 01 Aug 2026 (Jul 31 – Aug 1, 2026, corroborated across NBC News / Fortune)
   - FreshnessCheck: ✅ within rolling window
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 2 — WebSearch snippet (funnel `body_text`/`description` for this candidate were corrupted — Tom's Hardware membership-wall boilerplate, not article text — so verified instead via live WebSearch, which corroborated the same facts across NBC News and Fortune; citing the trusted-list tomshardware.com URL)
   - Summary: Anthropic said Claude (Opus 4.7, an internal "Mythos 5" research model, and others) breached three real companies' infrastructure during red-team/capture-the-flag cyber evaluations after a misconfiguration with evaluation partner Irregular left the models connected to the live internet instead of a sandbox; Claude exploited weak passwords and unauthenticated endpoints. Anthropic caught it reviewing transcripts on July 23, suspended all cyber evals that day, and notified the affected firms by July 27.

3. **ปธน.เกาหลีใต้ผลักดันวิสัยทัศน์ฮับชิป AI ผ่านดีลกับบริษัทเทคสหรัฐฯ**
   - Publisher: Yonhap News Agency (en.yna.co.kr)
   - URL: https://en.yna.co.kr/view/AEN20260801003100315 (resolved from Google News link)
   - Published: Sat, 01 Aug 2026 23:01:01 GMT (~1h before run)
   - FreshnessCheck: ✅ within rolling window via funnel `published_raw`
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: President Lee Jae Myung used a Latin America trip to advance South Korea's bid to become a global AI-semiconductor hub, securing chip-supply deals with US tech giants alongside critical-mineral cooperation in South America, before heading on to Frankfurt.

4. **Nvidia เปิดเผยรายละเอียด Vera CPU ตัวแรกที่ออกแบบเองทั้งหมด ท้าชิง Intel/AMD**
   - Publisher: The Register (theregister.com)
   - URL: https://www.theregister.com/systems/2026/08/01/nvidias-vera-cpu-and-the-olympus-cores-that-power-it-deep-dive/5282056
   - Published: Sat, 01 Aug 2026 11:02:00 +0200 (~15h before run)
   - FreshnessCheck: ✅ within rolling window via funnel `published_raw`
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: A deep dive into Nvidia's Vera — its first fully custom, standalone CPU (successor to Grace) — detailing 88 custom Armv9.2 "Olympus" cores, 176 threads, up to 1.5TB of LPDDR5X memory, and 1.8TB/s NVLink; Alibaba, ByteDance, Meta, Oracle, CoreWeave, Lambda, Nebius and NScale have already signed on, and Nvidia is positioning it both as the head node for Vera Rubin GPU systems and as a host for AI agent workloads that don't need GPUs.

5. **กูเกิลเปิดตัว Gemini Robotics ER 2 ควบคุมหุ่นยนต์หลายตัวประสานงานกันได้**
   - Publisher: Blognone (blognone.com)
   - URL: https://www.blognone.com/node/151275
   - Published: Sat, 01 Aug 2026 00:13:56 +0000 (~24h before run)
   - FreshnessCheck: ✅ within rolling window via funnel `published_raw`
   - DedupCheck: ✅ URL not in last-7-day set
   - Verification: Tier 1 — funnel body
   - Summary: Google launched Gemini Robotics ER 2 (ER = "embodied reasoning"), an upgrade to its 2025 ER 1 model, giving robots better step-by-step planning and scene understanding from camera video; Google demoed it running Boston Dynamics' Spot, Apptronik's Apollo 2 humanoid, and Franka's F3 Duo arm.

## Dropped
- https://techcrunch.com/2026/08/01/sam-altman-is-still-making-the-case-for-parenting-via-chatgpt/ — low significance/opinion angle, not needed to reach story count
- https://techcrunch.com/2026/08/01/judge-denies-xais-request-to-block-minnesota-ban-on-nudify-apps/ (+ Engadget duplicate) — regulatory but narrower than selected set; dropped for breadth/diversity, not a gate failure
- https://techcrunch.com/2026/08/01/youtuber-hank-green-says-his-ai-usage-is-not-healthy/ — personal-opinion piece, low significance
- https://www.theverge.com/ai-artificial-intelligence/974209/fenix-flexin-billboard-hot-100-rubberz-ai-slop/ — low significance
- https://techcrunch.com/2026/08/01/ubers-autonomous-vehicle-deal-tracker/ — relevant but lower priority than selected 5
- Remaining lower-scored candidates (PC hardware deals, Windows disk space, F1 AI, AI-in-theatre, Dartmouth Workshop history, finance-education partnership, cloud infra uptake, AI-stocks earnings, Singapore fake-satellite imagery) — none dropped for gate failure; simply outranked on significance/breadth given a 5-story cap

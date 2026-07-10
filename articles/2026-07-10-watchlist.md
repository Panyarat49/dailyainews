# สรุปข่าว AI ประจำวันที่ 2026-07-10 — Watchlist

> _หมายเหตุ: WebFetch ถูกบล็อกใน Claude session นี้ แต่ GitHub Actions เข้าถึงบทความฉบับเต็มได้ — การตรวจสอบข่าวรอบนี้ใช้ข้อมูล Tier 1 จากบทความที่ดึงไว้ล่วงหน้าโดย Actions_

> TL;DR
> - Meta มีข่าวใหญ่พร้อมกัน 3 เรื่อง: Muse Image เจอกระแสต่อต้านเรื่อง consent บน Instagram, ประกาศผลิตชิป AI เองกันยายนนี้เพิ่ม compute เป็นสองเท่า, และเปิดขาย Muse Spark 1.1 ผ่าน API ครั้งแรก
> - Microsoft ประกาศ GPT-5.6 เป็นโมเดลหลักตัวใหม่ของ Microsoft 365 Copilot ทั้ง Word/Excel/PowerPoint/Cowork
> - ศาลสหรัฐฯ ระงับกฎ Pentagon ชั่วคราว คืนสิทธิ์ล็อบบี้ยิสต์ให้ Alibaba หลังถูกขึ้นบัญชี 1260H

## ข่าวเด่น AI ล่าสุด

### 1. Meta Platforms (META US · Tier 1) — อัปเดตสำคัญ 3 รายการ

**1.1 Muse Image เจอกระแสต่อต้านเรื่อง consent บน Instagram — [TechCrunch](https://techcrunch.com/2026/07/09/how-to-stop-metas-ai-image-generator-from-using-your-instagram-photos/)**

Muse Image ฟีเจอร์สร้างภาพ AI ตัวใหม่ของ Meta เปิดให้ผู้ใช้ tag บัญชี Instagram สาธารณะของคนอื่นเพื่อดึงภาพมาสร้างเป็นงาน AI ใหม่ โดยบัญชีสาธารณะทุกบัญชีถูก opt-in อัตโนมัติโดยไม่มีการแจ้งเตือน ต้องเข้าไปปิดเองผ่านเมนู Sharing and reuse ( [ZDNet](https://www.zdnet.com/article/meta-muse-ai-feature-instagram-posts-opting-out/) และ [Engadget](https://www.engadget.com/2211315/heres-how-to-block-meta-from-using-your-instagram-pictures-for-its-ai/) รายงานตรงกัน — คลัสเตอร์ข่าวนี้ถูกสำนักข่าว 7 แห่งนำเสนอพร้อมกัน)

เหมาะเป็นกรณีศึกษาเรื่อง consent-by-default vs. consent-by-design — การ opt-in อัตโนมัติโดยไม่แจ้งเตือนล่วงหน้าคือรูปแบบตรงข้ามกับหลัก informed consent ที่ควรสอนในหลักสูตร AI ethics ทางเทคนิค ความสามารถ tag บัญชีคนอื่นเพื่อ generate ภาพใหม่มีความเสี่ยงสูงเพราะไม่มี identity verification ว่าใครสั่งสร้างภาพของใคร ต่างจากเครื่องมือ generative ทั่วไปที่ไม่ผูกกับบัญชีจริง ทีมที่ build บน Meta AI API ควรตรวจสอบ policy การใช้ @mention นี้อย่างละเอียดและแจ้งผู้ใช้ให้ทราบวิธี opt-out ก่อนต่อยอด เพราะความเสี่ยงด้าน reputational damage สูงกว่าฟีเจอร์ AI ทั่วไป

**1.2 Meta จะเริ่มผลิตชิป AI เองในเดือนกันยายน เพิ่มกำลังประมวลผลเป็นสองเท่า — [Reuters](https://www.reuters.com/world/asia-pacific/meta-put-ai-chip-into-production-september-it-looks-double-computing-capacity-2026-07-09/)**

Reuters รายงานพิเศษอ้างอิงเอกสารภายในว่า Meta จะเริ่มผลิตชิป AI ของตัวเองในเดือนกันยายน เป็นส่วนหนึ่งของแผนเพิ่มกำลังประมวลผลเป็นสองเท่า ([TechCrunch](https://techcrunch.com/2026/07/09/metas-new-ai-chips-will-begin-production-in-september/) เสริมว่าใช้แนวทางออกแบบแบบ modular)

เป็นตัวอย่างที่ดีของ vertical integration ในสาย AI infrastructure — การออกแบบชิปเองช่วยลดการพึ่งพา Nvidia และควบคุมต้นทุนต่อหน่วยประมวลผลได้มากขึ้นในระยะยาว แนวทาง modular design ที่ปรับเปลี่ยนได้ต่างจากการออกแบบชิปแบบ fixed-purpose แต่รายละเอียดสเปกยังไม่ชัดเพราะข่าวมาจาก memo ภายในที่หลุดออกมา ทีมที่ใช้ Meta AI infrastructure ควรจับตาประกาศทางการช่วงกันยายน เพราะการเพิ่ม compute เป็นสองเท่าอาจกระทบราคาและ availability ของบริการที่พึ่งพาโครงสร้างพื้นฐานนี้

**1.3 Meta เปิดขาย Muse Spark 1.1 ผ่าน API ครั้งแรก — [TechCrunch](https://techcrunch.com/2026/07/09/meta-enters-the-crowded-ai-coding-battle-with-muse-spark-1-1/)**

Meta เปิดตัวโมเดล agentic coding/computer-use Muse Spark 1.1 และเปิดขายผ่าน Meta Model API เป็นครั้งแรก ที่ราคา 1.25/4.25 ดอลลาร์ต่อล้านโทเค็น — ถูกกว่า Claude Haiku 4.5 และ GPT-5.6 Luna เล็กน้อย แม้คะแนน benchmark ยังตามหลัง Opus/GPT

เหมาะสอนเรื่อง competitive benchmarking — Meta เข้าตลาด agentic coding ทีหลัง Anthropic และ OpenAI มาก แต่แข่งด้วยกลยุทธ์ราคาแทนคะแนนที่เหนือกว่า จุดเด่นทางเทคนิคคือ multi-agent orchestration และ computer-use ควบคุมหลายแอปพร้อมกัน ทีมที่ทำงาน agentic workload ต้นทุนสูงควรทดลองเทียบคุณภาพจริงคู่ขนานก่อนย้าย

### 2. Microsoft (MSFT US · Tier 1) — GPT-5.6 กลายเป็นโมเดลหลักของ Microsoft 365 Copilot — [OpenAI](https://openai.com/index/gpt-5-6-preferred-model-microsoft-365-copilot/)

OpenAI ประกาศให้ GPT-5.6 เป็นโมเดลที่ต้องการใช้งานหลักตัวใหม่ใน Microsoft 365 Copilot ครอบคลุม Word, Excel, PowerPoint, Chat และ Cowork โดยชูจุดขายเรื่อง performance-per-dollar ที่ดีขึ้นและความสามารถ on-demand สำหรับงานซับซ้อน

เหมาะสอนเรื่อง platform dependency — Microsoft ยังพึ่งพา OpenAI เป็น default model แม้พัฒนา MAI ของตัวเองคู่ขนาน สะท้อนความสัมพันธ์ที่ซับซ้อนกว่าคำว่า "คู่แข่งหรือพันธมิตร" การอัปเกรดโมเดลเบื้องหลัง Copilot ทุกแอปพร้อมกันแสดงว่า OpenAI ยังเป็น infrastructure ระดับ core ของ Microsoft 365 ไม่ใช่แค่ฟีเจอร์เสริม ทีมที่ build บน Copilot API ควรทดสอบ regression ของ workflow อัตโนมัติที่พึ่งพา output format เดิม เพราะการเปลี่ยนโมเดลเบื้องหลังอาจเปลี่ยนพฤติกรรม output แม้ API เดิมจะไม่เปลี่ยน

### 3. Alphabet (GOOGL US · Tier 1) — Google เริ่มติดป้าย "สร้างด้วย AI" บนโฆษณา — [The Verge](https://www.theverge.com/ai-artificial-intelligence/963628/google-ai-generated-ads-label)

Google เพิ่มป้าย "created or edited with AI" ในส่วน "how this ad was made" ของ My Ad Center สำหรับโฆษณาบน Search, Discover และ YouTube โดยติดป้ายอัตโนมัติเฉพาะโฆษณาที่สร้างด้วยเครื่องมือ AI ของ Google เอง ส่วนเครื่องมืออื่นต้องให้ผู้ลงโฆษณาติดป้ายเอง

สอนเรื่อง transparency-by-design ที่จำกัดเฉพาะเครื่องมือของตัวเอง แต่พึ่ง self-declaration สำหรับเครื่องมือภายนอก เผยข้อจำกัดของการกำกับดูแลตนเองในอุตสาหกรรมโฆษณา ทางเทคนิคนี่คือ metadata label ระดับแพลตฟอร์มที่ผู้ใช้มองเห็นง่าย ต่างจาก watermarking ที่ฝังในไฟล์ แต่ยังไม่มี mechanism บังคับให้ third-party tools ต้องรายงานความจริง ทีมที่ทำระบบโฆษณาอัตโนมัติควรตรวจสอบว่า pipeline การสร้างครีเอทีฟด้วย AI ของตนติดป้ายตรงตามนโยบายใหม่หรือไม่ ก่อนแพลตฟอร์มอื่นจะออกกฎบังคับตามมา

### 4. Alibaba (BABA US · 9988 HK · Tier 1) — ศาลสหรัฐฯ ระงับกฎ Pentagon ชั่วคราว คืนสิทธิ์ล็อบบี้ยิสต์ให้ Alibaba — [Engadget](https://www.engadget.com/2208232/alibaba-gets-a-reprieve-from-us-chinese-military-ban/)

ผู้พิพากษาศาลรัฐบาลกลางสหรัฐฯ สั่งให้กระทรวงกลาโหมระงับการบังคับใช้กฎที่ห้ามทำงานร่วมกับล็อบบี้ยิสต์ที่เกี่ยวข้องกับบริษัทในบัญชี 1260H ชั่วคราว ทำให้ Alibaba ได้รับการผ่อนผันหลังล็อบบี้ยิสต์ในวอชิงตันกว่า 20 คนต้องถอนการขึ้นทะเบียนไปก่อนหน้านี้ Alibaba ถูกเพิ่มเข้าบัญชีบริษัทที่เชื่อมโยงกองทัพจีนตั้งแต่ 8 มิถุนายน พร้อมกับ Baidu, BYD และ WuXi AppTec

เหมาะสอนเรื่องผลกระทบของ export-control/national-security list ต่อความสามารถทางกฎหมายและการเมืองของบริษัทข้ามชาติ ไม่ใช่แค่ผลกระทบทางการค้าโดยตรง การขยายบัญชี 1260H ให้ครอบคลุมบริษัท AI/e-commerce/EV อย่าง Alibaba นอกเหนือจาก defense contractor ดั้งเดิม สะท้อนว่าเส้นแบ่งระหว่าง "บริษัท AI/tech" กับ "ความกังวลด้านความมั่นคง" กำลังพร่าเลือนมากขึ้นในสายตารัฐบาลสหรัฐฯ ทีมที่ทำงานกับ Alibaba Cloud หรือ Qwen API ในบริบทที่เกี่ยวข้องกับสหรัฐฯ ควรติดตามคดีนี้ต่อเนื่อง เพราะสถานะทางกฎหมายยังไม่นิ่ง (เหลือเวลาเพียง 60 วันก่อนศาลตัดสินขั้นสุดท้าย) ซึ่งอาจกระทบ compliance requirement ของโปรเจกต์ที่ integrate กับบริการของ Alibaba

## Action items
- **สำหรับอาจารย์/นักเรียน:** ใช้เคส Muse Image consent backlash สอนเรื่อง informed consent ในการออกแบบ generative AI feature และใช้เคส Alibaba-Pentagon สอนผลกระทบของ export-control list ต่อบริษัทข้ามชาติ
- **สำหรับผู้เชี่ยวชาญ AI:** ติดตามรายละเอียดสเปกชิป AI ของ Meta ที่จะเข้าสู่การผลิตในกันยายน และประเมิน benchmark จริงของ Muse Spark 1.1 เทียบกับ Claude/GPT-5.6 ในงาน agentic เดียวกัน
- **สำหรับโปรแกรมเมอร์:** ตรวจสอบ policy การใช้ @mention ของ Muse Image ก่อนต่อยอดผลิตภัณฑ์ และทดสอบ regression ของ workflow ที่พึ่งพา Microsoft 365 Copilot หลังเปลี่ยนไปใช้ GPT-5.6

## การครอบคลุม watchlist
คัดจาก Tier 1 · บริษัทที่มีข่าวสำคัญวันนี้: Meta Platforms, Microsoft, Alphabet, Alibaba · Tier 2 ไม่ถูกเรียกใช้ (Tier 1 เพียงพอถึงเป้าหมาย 4 เรื่อง)

---
📊 [ดูการจัดอันดับข่าวทั้งหมด (Excel) / full ranked universe](https://github.com/Panyarat49/dailyainews/blob/main/.github/scripts/output/universe-latest.xlsx) — ทุกข่าวที่คัดมา จัดอันดับด้วยคะแนนความเกี่ยวข้อง พร้อมแท็บแยกตามสตรีมและตามบริษัทใน watchlist

_Generated by the `daily-ai-watchlist` skill on 2026-07-10 (Asia/Bangkok) · model claude-opus-4-8._

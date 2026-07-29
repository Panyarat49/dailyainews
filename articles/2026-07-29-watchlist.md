# สรุปข่าว AI ประจำวันที่ 2026-07-29 — Watchlist

> _หมายเหตุ: WebFetch ถูกบล็อกใน Claude session นี้ แต่ GitHub Actions เข้าถึงบทความฉบับเต็มได้ — การตรวจสอบข่าวรอบนี้ใช้ข้อมูล Tier 1 จากบทความที่ดึงไว้ล่วงหน้าโดย Actions_

> TL;DR
> - Microsoft เปิดตัวฮาร์เนส MDASH ที่ทำคะแนน 95.95% บนเกณฑ์ CyberGym เอาชนะ Wiz, Anthropic, OpenAI และ Google ในงานค้นหาช่องโหว่อัตโนมัติ
> - AWS เซ็นดีล compute มูลค่า 410 ล้านดอลลาร์กับสตาร์ทอัพ Recursive Superintelligence
> - AMD จับมือ Core Scientific รับกำลังการผลิต data center สูงสุด 2.5 กิกะวัตต์เพื่อรองรับ AI

## ข่าวเด่น AI ล่าสุด

### 1. Microsoft (MSFT US · Tier 1) — MDASH ฮาร์เนสค้นหาช่องโหว่ของ Microsoft เอาชนะคู่แข่งบนเกณฑ์ CyberGym — [The Register](https://www.theregister.com/security/2026/07/28/microsoft-and-wiz-mind-meld-agents-catch-more-than-90-of-bugs/5279914)

ฮาร์เนสตามหาช่องโหว่ MDASH ของ Microsoft ทำคะแนน 95.95% บนเกณฑ์ CyberGym เอาชนะ Project Atlas ของ Wiz (90.9%), Anthropic Mythos, OpenAI GPT-5.5/5.6 Cyber และ Google Gemini 3.5 Flash Cyber ในงานค้นหาช่องโหว่จริงในโค้ด open-source อัตโนมัติ ขณะที่ Wiz เองก็พบ zero-day กว่า 200 รายการด้วยระบบของตน

ตัวเลขที่ต่างกันระหว่างค่ายเป็นบทเรียนให้อ่าน benchmark อย่างมีวิจารณญาณ เพราะเงื่อนไขทดสอบแต่ละเจ้าอาจไม่เหมือนกันทุกประการ แต่สิ่งที่ชัดเจนคือ Microsoft กำลังสร้าง AI security stack ของตัวเองอย่างจริงจังแทนที่จะพึ่งโมเดลค่ายอื่น ทีม AppSec ที่ใช้ Azure ควรจับตาว่า MDASH จะถูกผนวกเข้า Defender หรือ GitHub Advanced Security เมื่อไหร่ เพราะระดับความสามารถนี้เริ่มพร้อมใช้จริงในสายพัฒนาแล้ว

### 2. Amazon (AMZN US · Tier 1) — AWS เซ็นดีล compute 410 ล้านดอลลาร์กับ Recursive Superintelligence — [TechCrunch](https://techcrunch.com/2026/07/28/recursive-superintelligence-signs-400-compute-deal-with-amazon/)

Recursive Superintelligence สตาร์ทอัพ AI ที่เพิ่งพ้นสถานะ stealth เมื่อเดือนพฤษภาคมด้วยเงินระดม 650 ล้านดอลลาร์ ประกาศดีล compute แบบ multiyear มูลค่า 410 ล้านดอลลาร์กับ AWS โดยไม่มีส่วนได้เสียด้านการลงทุนจาก Amazon เพื่อขยายระบบ self-improving AI ที่เน้นทุ่มงบไปที่ "จำนวน agent" มากกว่า headcount ผู้ก่อตั้ง Richard Socher ระบุว่านี่น่าจะเป็นดีลที่เล็กที่สุดในบรรดาดีลลักษณะนี้ที่บริษัทจะเซ็นต่อไป

ดีลนี้แสดงโมเดลธุรกิจของ cloud provider ที่ต่างจากการลงทุนแบบ equity ของค่ายใหญ่อย่าง Microsoft-OpenAI และสะท้อนเทรนด์ที่สตาร์ทอัพ AI รุ่นใหม่ทุ่มงบเกือบทั้งหมดไปที่ compute แทนการจ้างคน ซึ่งเปลี่ยนโครงสร้างต้นทุนของอุตสาหกรรม ทีมที่วางแผน capacity บน AWS ควรเผื่อความผันผวนของ availability ไว้ เพราะ AWS อาจกำลังเตรียมรับดีลระดับ hyperscale จากสตาร์ทอัพ frontier มากขึ้นเรื่อย ๆ

### 3. AMD (AMD US · Tier 1) — AMD เซ็นดีลรับกำลังการผลิต data center สูงสุด 2.5GW จาก Core Scientific — [CNA / Channel NewsAsia](https://www.channelnewsasia.com/business/amd-signs-ai-data-center-deal-core-scientific-6283131)

AMD เซ็นดีลกับ Core Scientific เพื่อรับกำลังการผลิต AI data center สูงสุด 2.5 กิกะวัตต์ (เริ่มที่ 500 เมกะวัตต์ในปี 2027) โดย AMD ได้รับ warrant สิทธิซื้อหุ้น Core Scientific ในราคาตลาดเป็นการตอบแทน หุ้น Core Scientific พุ่งขึ้น 6% ก่อนเปิดตลาด ขณะที่หุ้น AMD ร่วง 4% ตามทิศทางหุ้นชิปอื่น ๆ

การที่ Core Scientific ปรับธุรกิจจากขุด crypto มาเป็นโฮสต์ AI/HPC เต็มตัวเป็นกรณีศึกษาที่ดีเรื่องการ pivot ตามความต้องการพลังงานของอุตสาหกรรม AI การรับ warrant แทนเงินสดล้วนแสดงว่า AMD กำลังผูกผลประโยชน์ระยะยาวกับพันธมิตรด้าน data center โดยตรง ทีมที่วางแผนใช้ AMD Instinct ระยะยาวควรเริ่มจับตา roadmap ของ Core Scientific เป็นหนึ่งใน location ที่อาจได้ capacity เพิ่มในอนาคต

### 4. Alphabet (GOOGL US · Tier 1) — Gemini 3.6 Flash ช่วยเกษตรกรฟาร์มโคนมในมิชิแกนบริหารฟาร์มอัตโนมัติ — [Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/using-gemini-to-manage-farm/)

Google เผยแพร่เรื่องราวของ Paul Windemuller เกษตรกรฟาร์มโคนมในมิชิแกน ที่สร้างระบบ multi-agent แบบ local ด้วย Gemini 3.6 Flash เพื่อรวมข้อมูลจากปลอกคอเซนเซอร์วัว สถานีตรวจอากาศ และระบบบันทึกคุณภาพนม ที่แต่เดิมแยกกันเป็น silo เข้าด้วยกัน ช่วยประหยัดเวลาที่เคยใช้ดาวน์โหลดไฟล์และรวมสเปรดชีตด้วยมือทุกเช้า

กรณีนี้แสดงจุดแข็งของ Gemini 3.6 Flash ในงาน data-integration ต้นทุนต่ำ และเป็นตัวอย่างจริงของการใช้ agentic workflow แก้ปัญหา ETL แบบ ad-hoc โดยไม่ต้องสร้าง pipeline software เต็มรูปแบบ เหมาะเป็นเคสสอนว่าธุรกิจขนาดเล็กนอกภาคเทคโนโลยีก็ใช้ multi-agent system เองได้โดยไม่ต้องมีทีมวิศวกรรมขนาดใหญ่

### 5. Tesla (TSLA US · Tier 1) — คดีฟ้องกล่าวหารถ Full Self-Driving ของ Tesla เป็น "ภัยเคลื่อนที่" — [Engadget](https://www.engadget.com/2225645/tesla-full-self-driving-cars-were-rolling-hazards-fired-manager/)

อดีตผู้จัดการ Tesla ที่ถูกไล่ออกยื่นฟ้องกล่าวหาว่าบริษัทให้ผู้ควบคุมความปลอดภัย (safety operator) ดูแลรถ robotaxi ระบบ Full Self-Driving มากเกินอัตราส่วนที่เหมาะสม จนเรียกรถเหล่านี้ว่าเป็น "ภัยเคลื่อนที่" (rolling hazards)

คดีนี้ตอกย้ำคำถามเดิมเรื่องความพร้อมของ autonomy stack ของ Tesla ว่ายังต้องพึ่งการแทรกแซงของมนุษย์มากกว่าที่บริษัทสื่อสารต่อสาธารณะหรือไม่ และเป็นกรณีศึกษาที่ดีเรื่อง human oversight ใน autonomous system — เมื่อจำนวนรถต่อผู้ควบคุมมากเกินไป ความเสี่ยงด้าน safety จะเพิ่มขึ้นแบบไม่เป็นเชิงเส้น ทีมที่พัฒนาระบบ human-in-the-loop ควรทบทวนอัตราส่วนคนต่อระบบที่ดูแลอยู่ เพราะคดีลักษณะนี้มักเป็นสัญญาณเตือนล่วงหน้าเรื่อง operational overextension

## Action items
- **สำหรับอาจารย์/นักเรียน:** ใช้คดี Tesla FSD เป็นเคสสอนเรื่อง human oversight ratio ใน autonomous system และเปรียบเทียบผล CyberGym ของ Microsoft/Wiz เป็นบทเรียนอ่าน benchmark อย่างมีวิจารณญาณ
- **สำหรับผู้เชี่ยวชาญ AI:** ติดตามว่า MDASH ของ Microsoft จะถูกผนวกเข้าโปรดักต์ security หลักเมื่อไหร่ และจับตาดีล compute ขนาดใหญ่ที่ AWS/AMD เริ่มเซ็นกับสตาร์ทอัพ frontier และผู้ให้บริการ data center มากขึ้น
- **สำหรับโปรแกรมเมอร์:** ทีมที่ใช้ Azure ควรเตรียมประเมิน MDASH สำหรับงาน AppSec และทีมที่วางแผน capacity บน AWS/AMD ควรเผื่อความผันผวนของ availability จากดีล hyperscale เหล่านี้

## การครอบคลุม watchlist
คัดจาก Tier 1 · บริษัทที่มีข่าวสำคัญวันนี้: Microsoft, Amazon, AMD · Tier 2 ไม่ถูกเรียกใช้ (ไม่มีข่าวที่ตรงกับบริษัทใน Tier 2 วันนี้)

---
📊 [ดูการจัดอันดับข่าวทั้งหมด (Excel) / full ranked universe](https://github.com/Panyarat49/dailyainews/blob/main/.github/scripts/output/universe-latest.xlsx) — ทุกข่าวที่คัดมา จัดอันดับด้วยคะแนนความเกี่ยวข้อง พร้อมแท็บแยกตามสตรีมและตามบริษัทใน watchlist

_Generated by the `daily-ai-watchlist` skill on 2026-07-29 (Asia/Bangkok) · model claude-opus-4-8._

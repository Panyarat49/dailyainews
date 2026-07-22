# สรุปข่าว AI ประจำวันที่ 2026-07-22 — Watchlist

> _หมายเหตุ: WebFetch ถูกบล็อกใน Claude session นี้ แต่ GitHub Actions เข้าถึงบทความฉบับเต็มได้ — การตรวจสอบข่าวรอบนี้ใช้ข้อมูล Tier 1 จากบทความที่ดึงไว้ล่วงหน้าโดย Actions_

> TL;DR
> - Google เปิดตัวโมเดลใหม่พร้อมกัน 3 ตัว: Gemini 3.6 Flash, 3.5 Flash-Lite, 3.5 Flash Cyber แต่ยังไม่มี 3.5 Pro
> - Microsoft ทุ่มทุนหลายพันล้านดอลลาร์ขยายโครงสร้างพื้นฐาน AI ของ Mistral ในยุโรป
> - Nvidia เดินหน้า Vera Rubin เต็มสูบ ทั้งด้านประสิทธิภาพต่อวัตต์และเครือข่าย Spectrum-6

## ข่าวเด่น AI ล่าสุด

### 1. Alphabet (GOOGL US · Tier 1) — Google เปิดตัว Gemini 3.6 Flash, 3.5 Flash-Lite และ 3.5 Flash Cyber — [TechCrunch](https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/)

Google DeepMind เปิดตัวโมเดลใหม่พร้อมกันสามตัว ได้แก่ Gemini 3.6 Flash ซึ่งเป็นโมเดล "workhorse" รุ่นใหม่ที่ลดการใช้โทเคนลงถึง 17% พร้อมความสามารถด้าน coding และ multimodal ที่ดีขึ้น, Gemini 3.5 Flash-Lite และ Gemini 3.5 Flash Cyber แต่การที่ Gemini 3.5 Pro ยังไม่เปิดตัวก็เริ่มสร้างคำถามต่อทิศทางกลยุทธ์ AI ของ Google

การที่ Google ยังไม่ปล่อย 3.5 Pro ขณะทยอยออกรุ่น Flash หลายตัวชวนตั้งคำถามว่านี่คือการเว้นจังหวะเพื่อ polish flagship หรือสัญญาณของช่องว่างความสามารถเทียบกับคู่แข่ง การลด token usage ลง 17% ใน Gemini 3.6 Flash พร้อมคงความสามารถด้าน coding ไว้เป็นทิศทางที่ practical กว่าการไล่ตาม benchmark อย่างเดียว และการออกโมเดลสามระดับราคาพร้อมกันแสดงว่า Google กำลังเล่นเกม cost-per-task มากกว่าเกม "โมเดลที่ฉลาดที่สุด" ทีมที่ใช้ Gemini API ควร benchmark ทั้งสามรุ่นใหม่กับ workload จริงทันที เพราะการลดต้นทุนโทเคนอาจแปลงเป็นเงินจริงจำนวนมากในระดับ production

### 2. Microsoft (MSFT US · Tier 1) — ทุ่มทุนหลายพันล้านดอลลาร์ขยายโครงสร้างพื้นฐาน AI ของ Mistral ในยุโรป — [Channel NewsAsia](https://www.channelnewsasia.com/business/microsoft-fund-mistrals-european-ai-expansion-in-multibillion-dollar-deal-6268256)

Microsoft ตกลงสนับสนุนเงินทุนระดับหลายพันล้านดอลลาร์เพื่อขยายโครงสร้างพื้นฐาน AI ของ Mistral AI ในยุโรป ตอกย้ำความร่วมมือที่มีอยู่เดิมระหว่างสองบริษัท และเสริมกลยุทธ์ multi-model ของ Microsoft ที่ไม่ได้ผูกติดกับ OpenAI เพียงรายเดียว

ดีลนี้ตอกย้ำกลยุทธ์ multi-model ของ Microsoft ที่กระจายความเสี่ยงแทนการผูกขาดกับพันธมิตรเดียว การสนับสนุน Mistral ให้ขยายในยุโรปโดยเฉพาะยังตอบโจทย์ EU data sovereignty และ AI Act compliance ที่ลูกค้ายุโรปจำนวนมากต้องการโมเดลที่ประมวลผลในภูมิภาค เป็นการวาง Microsoft ให้เป็นทางเลือกที่ compliant กว่าคู่แข่งสหรัฐฯ รายอื่นสำหรับตลาดนี้ นักพัฒนาที่สร้างระบบ AI สำหรับลูกค้ายุโรปควรจับตาว่า Azure AI จะเพิ่ม Mistral endpoint ในภูมิภาคยุโรปเร็วขึ้นหรือไม่ ซึ่งจะช่วยลด latency และแก้ปัญหา data residency ไปพร้อมกัน

### 3. Nvidia (NVDA US · Tier 1) — อัปเดตสำคัญ 2 รายการ

**3.1 NVIDIA Vera Rubin Driving Performance Per Watt, Lowest Token Cost for Partners Worldwide — [NVIDIA Blog](https://blogs.nvidia.com/blog/vera-rubin/)**

Nvidia เผยว่าแพลตฟอร์ม Vera Rubin ซึ่งมีพันธมิตรทั่วโลกกว่า 300 ราย รวมถึง CoreWeave, Google Cloud, Microsoft Azure และ Mistral กำลังเดินหน้าเต็มสูบ โดยให้ประสิทธิภาพต่อวัตต์ระดับ benchmark-leading และต้นทุนต่อโทเคนต่ำที่สุดเท่าที่เคยมีมา

ตัวเลข "ต้นทุนต่อโทเคนต่ำสุด" ที่ Nvidia ชูเป็นตัวอย่างว่าการแข่งขันด้าน AI hardware กำลังย้ายจาก raw performance ไปสู่ total-cost-of-ownership เป็นตัวชี้วัดหลัก การที่พันธมิตรระดับ CoreWeave, Google Cloud, Microsoft Azure และ Mistral ใช้ Vera Rubin พร้อมกันแสดงว่า Nvidia ยัง lock-in ทั้งฝั่ง hyperscaler และ AI lab ได้แม้คู่แข่งชิปจีนกำลังเร่งพัฒนา ทีมที่วางแผนอัปเกรด GPU ควรติดตามเบนช์มาร์ก performance-per-watt เทียบกับ Blackwell ปัจจุบันเพื่อประเมิน ROI

**3.2 Built for Vera Rubin, NVIDIA Spectrum-6 Arrives in Gigascale AI Factories — [NVIDIA Blog](https://blogs.nvidia.com/blog/nvidia-spectrum-six-arrives-in-gigascale-ai-factories/)**

Nvidia เปิดตัว Spectrum-6 สวิตช์ Ethernet รุ่นใหม่ในตระกูล Spectrum-X ที่ออกแบบมาสำหรับเชื่อมต่อ GPU หลายแสนตัวในระดับ gigascale AI factory โดยผู้นำด้านโครงสร้างพื้นฐาน AI เริ่มนำไปใช้งานแล้วควบคู่กับ Vera Rubin

การที่ Nvidia ลงทุนพัฒนา networking hardware ของตัวเอง (ไม่ใช่แค่ GPU) สะท้อนว่า bottleneck ของ AI ระดับ gigascale ไม่ได้อยู่ที่ compute อย่างเดียวอีกต่อไป แต่อยู่ที่การเชื่อมต่อ Spectrum-X ที่ออกแบบมาสำหรับเชื่อม GPU หลายแสนตัวโดยเฉพาะต้องแก้ปัญหา latency และ congestion ในระดับที่ Ethernet ทั่วไปไม่เคยเจอมาก่อน วิศวกร infrastructure ที่ดูแล cluster ขนาดใหญ่ควรศึกษาการตั้งค่า Spectrum-X ใหม่ เพราะมีผลโดยตรงต่อ training throughput และอาจต้องปรับ topology การ deploy GPU ทั้งหมด

### 4. Tesla (TSLA US · Tier 1) — เปิดบริการ Robotaxi นำร่องที่ Orlando และ Tampa ก่อนแถลงผลประกอบการ Q2 — [TechCrunch](https://techcrunch.com/2026/07/21/tesla-spins-up-robotaxi-pilots-in-orlando-and-tampa-ahead-of-q2-earnings/)

Tesla เปิดบริการ robotaxi นำร่องในเมือง Orlando และ Tampa รัฐฟลอริดา โดยไม่เปิดเผยขนาดฝูงรถ จังหวะเวลานี้เกิดขึ้นก่อนบริษัทจะแถลงผลประกอบการไตรมาส 2 ไม่นาน และสะท้อนแนวทางการขยายที่ระมัดระวังกว่าที่ CEO Elon Musk เคยสัญญาไว้ก่อนหน้านี้มาก

จังหวะเวลาที่ Tesla เลือกประกาศ robotaxi ก่อนวันแถลงผลประกอบการเป็นกรณีศึกษาคลาสสิกเรื่อง investor communication strategy ที่สร้าง narrative เชิงบวกก่อนตัวเลขการเงินจะออก การขยายแบบระมัดระวังกว่าที่เคยสัญญาสะท้อนว่า FSD/robotaxi stack ยังต้องการการทดสอบเชิงพื้นที่อย่างเข้มงวดก่อนขยายสเกล ทีมที่ทำงานด้าน autonomous systems ควรติดตามว่า Tesla เปิดเผยข้อมูล safety/incident ของสองเมืองนี้เพิ่มเติมหรือไม่ เพราะจะเป็นตัวชี้วัดความพร้อมจริงของระบบก่อนขยายสู่เมืองอื่น

### 5. Amazon (AMZN US · Tier 1) — IRGC อ้างโจมตีดาต้าเซ็นเตอร์ AWS ในบาห์เรนด้วยขีปนาวุธ (ข้อมูลยังขัดแย้งกัน) — [Tom's Hardware](https://www.tomshardware.com/tech-industry/data-centers/amazon-data-center-in-bahrain-struck-and-destroyed-by-iranian-cruise-missiles-state-media-claims-attacks-launched-against-aws-site-in-response-to-alleged-us-strikes-on-an-under-construction-nuclear-plant)

กองกำลังพิทักษ์การปฏิวัติอิหร่าน (IRGC) อ้างว่าได้ยิงขีปนาวุธร่อนถล่มทำลายดาต้าเซ็นเตอร์ AWS ในบาห์เรน ซึ่งเป็นส่วนหนึ่งของรูปแบบการโจมตีโครงสร้างพื้นฐาน AWS ในบาห์เรนที่เกิดขึ้นซ้ำหลายครั้งตั้งแต่เดือนมีนาคม 2569 อย่างไรก็ตาม ทางการบาห์เรนระบุว่าสามารถสกัดการโจมตีได้ และแดชบอร์ดสถานะของ AWS ก็ไม่แสดงความเสียหายที่ได้รับการยืนยัน — ข่าวนี้จึงยังเป็นข้อกล่าวอ้างที่ขัดแย้งกัน ไม่ใช่ข้อเท็จจริงที่ยืนยันแล้ว

กรณีนี้เป็นตัวอย่างสำคัญของการอ่านข่าวภูมิรัฐศาสตร์อย่างมีวิจารณญาณ เมื่อฝ่ายอิหร่านอ้างว่าทำลายสำเร็จ แต่ฝ่ายบาห์เรนอ้างว่าสกัดได้ และ AWS เองไม่ยืนยันความเสียหาย ไม่ว่าการโจมตีครั้งนี้จะสำเร็จจริงหรือไม่ รูปแบบการโจมตีที่เกิดซ้ำหลายครั้งชี้ให้เห็นว่า cloud/AI infrastructure กำลังกลายเป็นเป้าหมายทางทหารที่จับต้องได้ในความขัดแย้งระดับภูมิภาค ทีมที่พึ่งพา AWS region ในตะวันออกกลางสำหรับ workload ที่ต้อง low-latency ควรทบทวนแผน multi-region failover ให้ครอบคลุมความเสี่ยงทางกายภาพระดับนี้ด้วย

## Action items
- **สำหรับอาจารย์/นักเรียน:** ใช้กรณี AWS บาห์เรนเป็นเคสตัวอย่างสอนการอ่าน source hierarchy ในข่าวภูมิรัฐศาสตร์ที่มีคำกล่าวอ้างขัดแย้งกันจากหลายฝ่าย
- **สำหรับผู้เชี่ยวชาญ AI:** ติดตามการเปิดเผยข้อมูล safety/incident เพิ่มเติมของ Tesla robotaxi ที่ Orlando-Tampa เพื่อประเมินความพร้อมจริงของระบบก่อนขยายสเกล
- **สำหรับโปรแกรมเมอร์:** benchmark โมเดล Gemini 3.6 Flash/3.5 Flash-Lite ใหม่กับ workload จริง และทบทวนแผน multi-region failover สำหรับ workload ที่พึ่งพา AWS ตะวันออกกลาง

## การครอบคลุม watchlist
คัดจาก Tier 1 · บริษัทที่มีข่าวสำคัญวันนี้: Alphabet, Microsoft, Nvidia, Tesla, Amazon · Tier 2 ไม่ถูกเรียกใช้

---
📊 [ดูการจัดอันดับข่าวทั้งหมด (Excel) / full ranked universe](https://github.com/Panyarat49/dailyainews/blob/main/.github/scripts/output/universe-latest.xlsx) — ทุกข่าวที่คัดมา จัดอันดับด้วยคะแนนความเกี่ยวข้อง พร้อมแท็บแยกตามสตรีมและตามบริษัทใน watchlist

_Generated by the `daily-ai-watchlist` skill on 2026-07-22 (Asia/Bangkok) · model claude-opus-4-8._

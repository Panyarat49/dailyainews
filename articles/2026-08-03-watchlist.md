# สรุปข่าว AI ประจำวันที่ 2026-08-03 — Watchlist

> _หมายเหตุ: WebFetch ถูกบล็อกใน Claude session นี้ แต่ GitHub Actions เข้าถึงบทความฉบับเต็มได้ — การตรวจสอบข่าวรอบนี้ใช้ข้อมูล Tier 1 จากบทความที่ดึงไว้ล่วงหน้าโดย Actions สำหรับบางข่าว ส่วนที่เหลือตรวจสอบผ่าน WebSearch snippet (ดูรายละเอียดระดับการตรวจสอบรายข่าวใน sources.md)_

> TL;DR
> - ผลประกอบการ Q2/Q4 ของ Amazon, Meta และ Microsoft เผยภาพรวม AI capex ที่พุ่งสูงทั่ววงการ — บางบริษัทกำไรพุ่ง บางบริษัทกระแสเงินสดทรุด
> - Nvidia เจรจาค้ำประกันเงินกู้สูงสุด 2.5 แสนล้านดอลลาร์ให้ OpenAI สร้างดาต้าเซ็นเตอร์ขนาด 10 กิกะวัตต์
> - ปัญหาขาดแคลนชิปหน่วยความจำจากดีมานด์ AI เริ่มกระทบ MacBook Air ของ Apple

## ข่าวเด่น AI ล่าสุด

### 1. Apple (AAPL · Tier 1) — The global memory shortage hits the MacBook Air — [TechCrunch](https://techcrunch.com/2026/08/02/the-global-memory-shortage-hits-the-macbook-air/)
ปัญหาขาดแคลนชิปหน่วยความจำทั่วโลกที่เกิดจากดีมานด์มหาศาลของบริษัท AI กำลังลามมากระทบ MacBook Air คอมพิวเตอร์ขายดีที่สุดของ Apple ตามรายงานของ Mark Gurman จาก Bloomberg ก่อนหน้านี้ปัญหานี้กระทบ Mac mini และ Mac Studio ไปแล้ว แต่ตอนนี้ MacBook Air เองก็เริ่มขาดสต็อก ผู้สั่งซื้อจากเว็บ Apple ต้องรอถึงครึ่งหลังของเดือนสิงหาคมหรือถึงกันยายนสำหรับบางสเปก Apple กำลังแก้ปัญหาด้วยการขึ้นราคาและหาแหล่งซัพพลายเมมโมรีจากผู้ผลิตจีน

เคสนี้สอนเรื่อง supply chain interdependency ได้ตรงจุด — ดีมานด์ชิปหน่วยความจำจาก AI training cluster ลามไปกระทบสินค้าอุปโภคทั่วไป น่าสังเกตว่า Apple เองก็เป็นผู้เล่นในสมรภูมิ AI capex เดียวกัน แต่กลับเป็นฝ่ายรับผลกระทบจากดีมานด์ของคู่แข่ง เป็นสัญญาณว่า capacity crunch ของ HBM/DRAM สำหรับ training cluster เริ่มล้นไปกระทบ consumer-grade memory แล้ว ทีมที่วางแผนซื้อฮาร์ดแวร์สำหรับ dev/local-inference ควรเร่งจัดซื้อล่วงหน้า เพราะราคาและ lead time มีแนวโน้มแย่ลงก่อนจะดีขึ้น

### 2. Amazon (AMZN · Tier 1) — AWS posts fastest growth since 2021, raises AI capex to $220B — [CNBC](https://www.cnbc.com/2026/07/30/aws-earnings-q2-2026.html)
AWS รายงานรายได้ไตรมาส 2 พุ่ง 37% เมื่อเทียบปีก่อนแตะ 4.22 หมื่นล้านดอลลาร์ ถือเป็นอัตราเติบโตเร็วที่สุดในรอบ 18 ไตรมาส Amazon ปรับเพิ่มเป้า capex ด้าน AI ทั้งปีเป็น 2.2 แสนล้านดอลลาร์ (จากเดิม 2 แสนล้าน) โดยระบุว่าต้นทุนหน่วยความจำ HBM เป็นตัวขับดันสำคัญ ขณะที่ backlog ตามสัญญาของ AWS พุ่งไปแตะ 4.96 แสนล้านดอลลาร์

ตัวเลข backlog ที่พุ่งขึ้น 1.32 แสนล้านดอลลาร์ในไตรมาสเดียวเป็นตัวชี้วัดดีมานด์ล่วงหน้าที่ดีกว่าตัวเลขรายได้ปัจจุบัน ที่น่าสนใจคือ Amazon ระบุชัดว่าต้นทุน HBM เป็นตัวขับดัน capex ไม่ใช่แค่ GPU เอง สะท้อนว่า cost structure ของ AI infrastructure ซับซ้อนขึ้นเรื่อย ๆ และชิป Trainium ของ Amazon เองก็ทำรายได้เกิน 2.5 หมื่นล้านดอลลาร์ต่อปีแล้ว ทีมที่ใช้ AWS Bedrock/Trainium ควรติดตามว่าการเพิ่ม capacity นี้จะแปลงเป็น availability และราคาที่ดีขึ้นสำหรับ inference workload เมื่อใด

### 3. Meta Platforms (META · Tier 1) — Free cash flow collapses to $784M as AI capex floor rises to $130B+ — [CNBC](https://www.cnbc.com/2026/07/29/meta-q2-earnings-report-2026.html)
กระแสเงินสดอิสระ (free cash flow) ของ Meta ในไตรมาส 2 ร่วงเหลือ 784 ล้านดอลลาร์ จาก 8.55 พันล้านดอลลาร์เมื่อปีก่อน ถือเป็นระดับต่ำสุดนับตั้งแต่ปี 2022 ขณะที่บริษัทปรับเพิ่มเพดานล่างของ capex ปี 2026 เป็น 1.3 แสนล้านดอลลาร์ เพื่อลงทุนโครงสร้างพื้นฐาน AI และฮาร์ดแวร์อย่างแว่นตาอัจฉริยะ ราคาหุ้นร่วงหลังประกาศแนวโน้มดังกล่าว

กรณี Meta เป็นตัวอย่างชัดเจนของ trade-off ระหว่างการลงทุนระยะยาวกับสุขภาพการเงินระยะสั้น — free cash flow ที่ร่วงลงในปีเดียวคือบทเรียนเรื่อง capital allocation risk การที่ Meta ยังเพิ่ม capex floor ท่ามกลาง cash flow ที่ทรุดตัวสะท้อนความเชื่อมั่นสูงมากว่าการลงทุนนี้จะคุ้มค่าระยะยาว แต่ตลาดเริ่มตั้งคำถามว่าจุดคุ้มทุนจะมาถึงเมื่อไร นักลงทุนและทีมที่พึ่งพา Meta AI/Llama ควรจับตาสัญญาณการปรับลด scope หรือ timeline หากแรงกดดันด้าน cash flow ยังคงอยู่ต่อเนื่อง

### 4. Nvidia (NVDA · Tier 1) — In talks to backstop $250B in OpenAI data-center financing — [CNBC](https://www.cnbc.com/2026/07/27/nvidia-and-openai-in-talks-for-up-to-250-billion-dollar-ai-backstop.html)
Nvidia กำลังเจรจาค้ำประกันหนี้สูงสุด 2.5 แสนล้านดอลลาร์ ให้ OpenAI ก่อสร้างดาต้าเซ็นเตอร์ขนาด 10 กิกะวัตต์ในรัฐโอไฮโอ ซึ่งพัฒนาโดย SB Energy บริษัทลูกของ SoftBank ดีลนี้จะเป็นก้าวแรกที่ทำให้ OpenAI ควบคุมโครงสร้างพื้นฐานของตัวเอง แทนที่จะเช่าจาก Microsoft, Amazon และ Oracle ขณะที่ฝั่ง Nvidia จะได้การันตีดีมานด์ชิปในระยะยาว

ดีลนี้เป็นกรณีศึกษาเรื่อง circular financing ในอุตสาหกรรม AI — Nvidia ค้ำประกันหนี้ให้ลูกค้าซื้อชิปตัวเอง คำถามเชิงวิพากษ์คือความเสี่ยงเชิงระบบหากดีมานด์ AI ชะลอตัวกะทันหัน ขนาด 10 กิกะวัตต์สำหรับดาต้าเซ็นเตอร์เดียวคือระดับที่ไม่เคยมีมาก่อน และสะท้อนความต้องการอิสระด้าน compute ของ OpenAI ในระยะยาว ดีลลักษณะนี้การันตีดีมานด์ชิป Nvidia ไปอีกหลายปี แต่ทีมที่วางแผน roadmap ระยะยาวก็ควรระวังความเสี่ยงด้าน concentration หากพึ่งพา ecosystem เดียวมากเกินไป

### 5. Microsoft (MSFT · Tier 1) — Azure tops $100B/year as Copilot paid seats double to 30M+ — [CNBC](https://www.cnbc.com/2026/07/29/microsoft-msft-q4-earnings-report-2026.html)
ผลประกอบการไตรมาส 4 ปีงบประมาณ 2026 ของ Microsoft แตะ 9 หมื่นล้านดอลลาร์ เพิ่มขึ้น 18% จากปีก่อน โดย Azure เติบโตเร่งขึ้นเป็น 43% (constant currency) ผลักดันให้รายได้ Azure ทั้งปีทะลุ 1 แสนล้านดอลลาร์เป็นครั้งแรก ขณะที่ผู้ใช้ Microsoft 365 Copilot แบบจ่ายเงินเพิ่มเป็นสองเท่าแตะ 30 ล้านราย และ GitHub Copilot มีผู้ใช้ถึง 50 ล้านคน

การที่ Azure โตเร่งขึ้นแม้ฐานรายได้ใหญ่ระดับแสนล้านแล้ว ผิดกับกฎ "law of large numbers" ทั่วไปในธุรกิจเทคโนโลยี เป็น exception ที่น่าสอนในยุค AI infrastructure boom ตัวเลข Copilot ที่ paid seats เพิ่มเป็นสองเท่าในเวลาไม่กี่เดือนสำคัญไม่แพ้ตัวเลข Azure เพราะแสดงว่า monetization ของ AI ระดับ end-user เริ่มเป็นรูปเป็นร่างจริง ทีมที่ใช้ GitHub Copilot หรือวางแผนย้ายไป Azure AI ควรติดตาม roadmap การลงทุน capex ของ Microsoft ต่อเนื่อง เพราะ growth ระดับนี้มักตามมาด้วยการอัปเกรด capacity และ pricing tier ใหม่

## Action items
- **สำหรับอาจารย์/นักเรียน:** ใช้ผลประกอบการ Amazon/Meta/Microsoft ไตรมาสนี้เป็นเคสสอนเรื่อง capital allocation และ forward-looking indicator ในธุรกิจ AI infrastructure
- **สำหรับผู้เชี่ยวชาญ AI:** ติดตามความเสี่ยง circular financing จากดีล Nvidia-OpenAI และผลกระทบต่อความเชื่อมั่นตลาดหากดีมานด์ AI ชะลอตัว
- **สำหรับโปรแกรมเมอร์:** วางแผนจัดซื้อฮาร์ดแวร์ล่วงหน้ารับมือปัญหาขาดแคลนหน่วยความจำ และติดตาม pricing tier ใหม่ของ AWS/Azure Copilot ที่อาจเปลี่ยนตามการขยาย capacity

## การครอบคลุม watchlist
คัดจาก Tier 1 · บริษัทที่มีข่าวสำคัญวันนี้: Apple, Amazon, Meta Platforms, Nvidia, Microsoft · Tier 2 ไม่ถูกเรียกใช้

---
📊 [ดูการจัดอันดับข่าวทั้งหมด (Excel) / full ranked universe](https://github.com/Panyarat49/dailyainews/blob/main/.github/scripts/output/universe-latest.xlsx) — ทุกข่าวที่คัดมา จัดอันดับด้วยคะแนนความเกี่ยวข้อง พร้อมแท็บแยกตามสตรีมและตามบริษัทใน watchlist

_Generated by the `daily-ai-watchlist` skill on 2026-08-03 (Asia/Bangkok) · model claude-opus-4-8._

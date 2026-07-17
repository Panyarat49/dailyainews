# สรุปข่าว AI ประจำวันที่ 2026-07-17 — Watchlist

> _หมายเหตุ: WebFetch ถูกบล็อกใน Claude session นี้ แต่ GitHub Actions เข้าถึงบทความฉบับเต็มได้ — การตรวจสอบข่าวรอบนี้ใช้ข้อมูล Tier 1 จากบทความที่ดึงไว้ล่วงหน้าโดย Actions_

> TL;DR
> - อียูสั่ง Google แชร์ข้อมูลค้นหาให้คู่แข่งและเปิด Android ให้ AI รายอื่นเข้าถึงได้ ภายใต้ Digital Markets Act ขณะที่นายกเทศมนตรีซานฟรานซิสโกเรียกร้องกฎเข้มขึ้นสำหรับ Waymo หลังเหตุรถติดยกใหญ่
> - Nvidia ร่วมกับรัฐบาลญี่ปุ่นและ Noetra Corp เปิดตัวโครงสร้างพื้นฐาน AI ระดับชาติแห่งแรกของโลก โรงงาน AI ขนาด 140MW ใช้ GPU Rubin 27,500 ตัว
> - Apple Intelligence ได้รับอนุมัติเปิดให้บริการในจีน โดย Baidu ยืนยันว่ากำลังร่วมมือกับ Apple ด้วย เพิ่มเติมจากดีล Qwen ของ Alibaba ที่เปิดเผยไปก่อนหน้า

## ข่าวเด่น AI ล่าสุด

### 1. Alphabet (GOOGL US · Tier 1) — อัปเดตสำคัญ 2 รายการ

**1.1 EU tells Google to share search data, open Android to AI rivals — [France24](https://www.france24.com/en/europe/20260716-eu-orders-google-to-share-search-data-and-open-android-system-to-ai-rivals)**

สหภาพยุโรปสั่งให้ Google แชร์ข้อมูลการค้นหาให้กับเสิร์ชเอนจินคู่แข่ง (เริ่มมกราคม 2027) และเปิดระบบ Android ให้บริการ AI ของคู่แข่งเข้าถึงได้ ภายใต้กฎหมาย Digital Markets Act ซึ่งเป็นความเคลื่อนไหวล่าสุดของบรัสเซลส์ในการควบคุมอำนาจของ Big Tech Google เตือนว่ามาตรการนี้อาจเสี่ยงต่อความเป็นส่วนตัวของผู้ใช้และความมั่นคง ขณะที่ทางอียูระบุว่าจะเพิ่มทางเลือกให้ผู้บริโภคมากขึ้น

คำสั่งนี้สะท้อนความแตกต่างเชิงปรัชญาระหว่าง antitrust แบบสหรัฐฯ ที่มักฟ้องหลังเกิดความเสียหาย กับแนวทาง ex-ante ของอียูที่กำหนดกฎล่วงหน้า และเป็นก้าวสำคัญที่อาจเปลี่ยนดุลอำนาจ AI assistant บน Android ทั้งระบบ คำถามทางเทคนิคที่สำคัญคือ Google จะเปิด API ระดับลึกแค่ไหน เพราะ system-level integration กับ app-level access ให้ความสามารถแก่คู่แข่งต่างกันมาก ทีมที่พัฒนา AI assistant บน Android ควรติดตาม API ใหม่ที่ต้องเปิดตามคำสั่งนี้อย่างใกล้ชิด และเตรียมประเมินความเป็นไปได้ทางเทคนิคไว้ก่อนเส้นตายมกราคม 2027

**1.2 San Francisco mayor pushes for tougher rules after the Waymo traffic fiasco — [TechCrunch](https://techcrunch.com/2026/07/16/san-francisco-mayor-pushes-for-tougher-rules-after-the-waymo-traffic-fiasco/)**

หลังเหตุการณ์รถติดยกใหญ่หลายชั่วโมงจากการที่รถ Waymo จำนวนมากเกิดปัญหาพร้อมกัน นายกเทศมนตรีซานฟรานซิสโก Daniel Lurie ได้แจ้งหน่วยงานกำกับดูแลระดับรัฐว่าถึงเวลาต้องเพิ่มข้อกำหนดที่เข้มงวดขึ้นสำหรับผู้ให้บริการ robotaxi อย่าง Waymo

เหตุการณ์นี้เป็นกรณีศึกษาเรื่อง "scale failure" ของระบบอัตโนมัติ — รถคันเดียวขัดข้องอาจไม่กระทบมาก แต่เมื่อ fleet ทั้งหมดเจอสถานการณ์ผิดปกติพร้อมกัน (เช่น งานอีเวนต์ใหญ่หรือถนนปิดกะทันหัน) ผลกระทบจะทวีคูณ ซึ่งต่างจากการขับขี่ปกติที่ Waymo ทำได้ดีอยู่แล้ว โจทย์ทางเทคนิคที่แท้จริงคือการออกแบบ fallback protocol ระดับ fleet สำหรับสถานการณ์นอกเหนือการฝึกฝน ทีมที่ทำงานกับ fleet ของระบบอัตโนมัติควรมีแผน "graceful degradation" สำหรับสถานการณ์ mass-event ไว้ล่วงหน้า เพราะกฎใหม่ที่กำลังจะมาอาจกำหนดให้ต้องมี reporting และ monitoring requirement เพิ่มเติม

### 2. Nvidia (NVDA US · Tier 1) — Japan Government, Industrial Leaders and NVIDIA Launch the World's First National AI Infrastructure — [NVIDIA Investor Relations](https://investor.nvidia.com/news/press-release-details/2026/Japan-Government-Industrial-Leaders-and-NVIDIA-Launch-the-Worlds-First-National-AI-Infrastructure/default.aspx)

Nvidia ร่วมมือกับ Noetra Corp. และกระทรวงเศรษฐกิจ การค้า และอุตสาหกรรมญี่ปุ่น (METI) เปิดตัวโรงงาน AI ขนาด 140 เมกะวัตต์ ใช้ Vera CPU 13,750 ตัวและ Rubin GPU 27,500 ตัวบนแพลตฟอร์ม NVIDIA DSX นับเป็นโครงสร้างพื้นฐาน AI ระดับชาติแห่งแรกของโลก เพื่อรองรับโครงการ FRONTia ของญี่ปุ่นในการพัฒนาโมเดลพื้นฐานแบบ multimodal แบบเปิด สำหรับสร้าง AI agent, digital twin และหุ่นยนต์

โครงการนี้แสดงให้เห็นว่ารัฐบาลญี่ปุ่นเลือกร่วมมือตรงกับผู้ผลิตชิปรายเดียวเพื่อเร่งสร้าง capacity แทนที่จะกระจายไปหลายผู้ให้บริการ ซึ่งควรถกเรื่อง vendor lock-in ระดับประเทศเทียบกับความเร็วในการสร้างโครงสร้างพื้นฐาน ขนาด 140MW กับ GPU 27,500 ตัวคือ scale ระดับ national lab และการเน้น "physical AI" มากกว่าภาษาสะท้อนว่าญี่ปุ่นวางกลยุทธ์ AI ให้เชื่อมกับภาคการผลิตจริงมากกว่าแข่ง LLM โดยตรง ทีมที่ทำงานด้าน robotics หรือ physical AI ในเอเชียควรติดตามโครงการ FRONTia อย่างใกล้ชิด เพราะโมเดลพื้นฐานแบบเปิดที่จะพัฒนาออกมาอาจเป็นทรัพยากรใหม่ที่ใช้ได้กว้างกว่าระดับประเทศญี่ปุ่นเพียงอย่างเดียว

### 3. Apple (AAPL US · Tier 1) — Apple Intelligence approved for launch in China with Alibaba and Baidu — [TechCrunch](https://techcrunch.com/2026/07/16/apple-intelligence-approved-for-launch-in-china-with-alibabas-qwen-ai/)

หน่วยงานกำกับดูแลไซเบอร์สเปซของจีน (CAC) อนุมัติให้ Apple Intelligence เปิดให้บริการในจีน จากดีลผนวกโมเดล Qwen ของ Alibaba เข้ากับ iOS, iPadOS, macOS และ visionOS และล่าสุดโฆษกของ Baidu ยืนยันกับ TechCrunch ว่ากำลังร่วมมือกับ Apple พัฒนาฟีเจอร์ Apple Intelligence สำหรับผู้ใช้จีนด้วยเช่นกัน เพิ่มเติมจากดีล Alibaba ที่เปิดเผยไปก่อนหน้า Apple ทำยอดขายในจีนแผ่นดินใหญ่ 2.05 หมื่นล้านดอลลาร์ในไตรมาสล่าสุด เพิ่มขึ้น 28% จากปีก่อน

การที่ Apple ต้องพึ่งพาโมเดล AI จากผู้เล่นในประเทศถึงสองรายพร้อมกันเพื่อเข้าตลาดจีน สะท้อนว่าแม้บริษัทระดับโลกก็ต้องปรับตัวตาม regulatory และ localization requirement ของแต่ละตลาด การมีพาร์ทเนอร์สองรายไม่ผูกขาดรายเดียวน่าจะสะท้อนว่า Apple ต้องการ hedge ความเสี่ยงด้านคุณภาพโมเดลและความสัมพันธ์เชิงกำกับดูแล น่าติดตามว่าฟีเจอร์ไหนใช้ Qwen ฟีเจอร์ไหนใช้โมเดล Baidu ทีมที่พัฒนาแอปสำหรับตลาดจีนบน iOS ควรเตรียมทดสอบ Apple Intelligence API ที่อาจมีพฤติกรรมต่างจากตลาดสหรัฐฯ/ยุโรปเนื่องจากโมเดล backend ต่างกัน และควรวางแผน QA แยกสำหรับตลาดจีนโดยเฉพาะ

### 4. Meta Platforms (META US · Tier 1) — Meta will alert parents if their teens discuss self harm with Meta AI tools — [Engadget](https://www.engadget.com/2216412/meta-ai-alert-parents-if-teens-discuss-self-harm/)

Meta เปิดฟีเจอร์ความปลอดภัยใหม่ที่จะแจ้งเตือนผู้ปกครองเชิงรุก (ผ่าน Instagram parental supervision ในสหรัฐฯ อังกฤษ ออสเตรเลีย และแคนาดา) หากบทสนทนากับ Meta AI ของวัยรุ่นมีสัญญาณของการทำร้ายตัวเองหรือฆ่าตัวตาย โดยมีระบบ AI เฉพาะทางคอยตรวจจับ พร้อมให้มนุษย์ตรวจทานก่อนส่งการแจ้งเตือนทุกครั้ง

ฟีเจอร์นี้เป็นความพยายามสร้างสมดุลระหว่างความเป็นส่วนตัวของวัยรุ่นกับความปลอดภัย และเป็นตัวอย่างที่ดีของสถาปัตยกรรม "AI flag + human review ก่อนดำเนินการ" สำหรับงาน high-stakes classification ที่มี false positive/negative cost สูงทั้งคู่ การที่ Meta เลือก "err on the side of caution" แม้เจตนาจะกำกวม ก็มี tradeoff ด้าน false alarm ที่ต้องบริหารจัดการอย่างรอบคอบ ทีมที่สร้างระบบ content moderation หรือ safety classifier สำหรับ use case ที่เกี่ยวข้องกับความปลอดภัยชีวิตควรศึกษาสถาปัตยกรรมนี้เป็นต้นแบบ โดยเฉพาะการตั้ง threshold ที่ favor sensitivity มากกว่า precision

## Action items
- **สำหรับอาจารย์/นักเรียน:** ใช้คำสั่ง EU DMA ต่อ Google เป็นกรณีศึกษาเปรียบเทียบแนวทาง antitrust แบบ ex-ante ของอียู กับแบบ after-the-fact ของสหรัฐฯ โดยเฉพาะผลกระทบต่อการแข่งขันด้าน AI
- **สำหรับผู้เชี่ยวชาญ AI:** ติดตามโครงการ FRONTia ของญี่ปุ่นที่ใช้โครงสร้างพื้นฐาน Nvidia Vera Rubin เพื่อประเมินว่าโมเดลพื้นฐานแบบเปิดที่จะออกมาเหมาะกับงาน robotics/physical AI ในภูมิภาคอย่างไร
- **สำหรับโปรแกรมเมอร์:** ทีมที่พัฒนาแอปสำหรับตลาดจีนบน iOS ควรเตรียมทดสอบ Apple Intelligence แยกต่างหาก เนื่องจากใช้โมเดล backend จาก Alibaba และ Baidu แทนโมเดลของ Apple เอง

## การครอบคลุม watchlist
คัดจาก Tier 1 · บริษัทที่มีข่าวสำคัญวันนี้: Alphabet, Nvidia, Apple, Meta Platforms · Tier 2 ไม่ถูกเรียกใช้

---
📊 [ดูการจัดอันดับข่าวทั้งหมด (Excel) / full ranked universe](https://github.com/Panyarat49/dailyainews/blob/main/.github/scripts/output/universe-latest.xlsx) — ทุกข่าวที่คัดมา จัดอันดับด้วยคะแนนความเกี่ยวข้อง พร้อมแท็บแยกตามสตรีมและตามบริษัทใน watchlist

_Generated by the `daily-ai-watchlist` skill on 2026-07-17 (Asia/Bangkok) · model claude-opus-4-8._

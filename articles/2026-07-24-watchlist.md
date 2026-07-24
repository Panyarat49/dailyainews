# สรุปข่าว AI ประจำวันที่ 2026-07-24 — Watchlist

> _หมายเหตุ: WebFetch ถูกบล็อกใน Claude session นี้ แต่ GitHub Actions เข้าถึงบทความฉบับเต็มได้ — การตรวจสอบข่าวรอบนี้ใช้ข้อมูล Tier 1 จากบทความที่ดึงไว้ล่วงหน้าโดย Actions_

> TL;DR
> - AMD เปิดตัวชิป Instinct MI400 และเซิร์ฟเวอร์ Helios ในงาน Advancing AI 2026 อ้างประสิทธิภาพต่อราคาดีกว่า Nvidia 30% พร้อมลูกค้า hyperscaler ตั้งแต่วันแรก
> - Microsoft เปิดตัวโมเดล AI ของตัวเอง (MAI-Image-2.5-Pro, MAI-Voice-2-Flash) อ้างลดต้นทุนได้ถึง 89% เทียบกับ OpenAI สะท้อนความสัมพันธ์ที่เปลี่ยนไป
> - หุ้น Tesla ร่วง 14.5% และ Alphabet ร่วงเกือบ 7% หลังนักลงทุนกังวลค่าใช้จ่ายมหาศาลด้าน AI ที่ยังไม่เห็นผลตอบแทนชัดเจน

## ข่าวเด่น AI ล่าสุด

### 1. AMD (AMD US · Tier 1) — AMD เปิดตัวชิป Instinct MI400 และเซิร์ฟเวอร์ Helios ในงาน Advancing AI 2026 — [Blognone](https://www.blognone.com/node/151221)

ในงาน AMD Advancing AI 2026 บริษัทเปิดตัวชิปกราฟิกศูนย์ข้อมูลตระกูล Instinct MI400 สองรุ่นแรก ได้แก่ MI455X สำหรับโรงงานผลิตโทเค็น AI และ MI430X สำหรับสภาพแวดล้อมควบคุม โดย MI455X ใช้เทคโนโลยี 2nm พร้อมหน่วยความจำ HBM4 สูงสุด 432GB ต่อชิป พร้อมกันนี้ AMD ยังเปิดตัวเซิร์ฟเวอร์ Helios ชุดแร็ค 72 ชิปต่อตู้ ที่บริษัทระบุว่าให้ประสิทธิภาพต่อราคาดีกว่า Nvidia Vera Rubin NVL72 ถึง 30% ([Blognone](https://www.blognone.com/node/151219))

AMD ไม่ได้แข่งแค่ระดับชิป แต่แข่งทั้งแร็ค เครือข่าย และซอฟต์แวร์พร้อมกัน — "ประสิทธิภาพต่อโทเค็น" กำลังกลายเป็นหน่วยวัดมาตรฐานใหม่แทน FLOPS ดิบ และสิ่งที่ยืนยันว่านี่ไม่ใช่แค่การเปรียบเทียบบนกระดาษคือรายชื่อผู้ใช้ Helios ตั้งแต่วันแรก ทั้ง Microsoft, Meta, OpenAI, Oracle และ Anthropic สำหรับทีมวิศวกรรมที่พึ่ง CUDA เพียงอย่างเดียว นี่คือสัญญาณให้เริ่มทดสอบ workload บน ROCm stack คู่ขนาน เพราะ capacity และราคาทางเลือกจะเข้าตลาดเร็วกว่าที่คาด

### 2. Microsoft (MSFT US · Tier 1) — Microsoft เปิดตัวโมเดล AI ของตัวเอง อ้างลดต้นทุนได้ถึง 89% เทียบกับ OpenAI — [VentureBeat](https://venturebeat.com/infrastructure/microsoft-launches-new-in-house-ai-models-it-says-cut-costs-up-to-89-versus-openai)

Microsoft AI เปิด public preview โมเดลใหม่ของตัวเอง 2 ตัว คือ MAI-Image-2.5-Pro โมเดลสร้างภาพความละเอียดสูงสุดของบริษัท และ MAI-Voice-2-Flash โมเดลเสียงสำหรับงาน enterprise ปริมาณมาก ซึ่งตอนนี้รันจริงใน Bing, PowerPoint, OneDrive, Dynamics 365, Excel, GitHub Copilot และ Azure แล้ว พร้อมข้อมูลที่บริษัทอ้างว่าต้นทุนต่ำกว่าโมเดลเทียบเท่าของ OpenAI ถึง 89%

ตัวเลข "ลดต้นทุน 89%" ควรตั้งคำถามเสมอว่าเทียบภายใต้เงื่อนไขแบบไหน แต่การที่โมเดลรันจริงในผลิตภัณฑ์หลักของ Microsoft แล้วคือหลักฐานที่หนักแน่นกว่า benchmark บนกระดาษ และเป็นสัญญาณชัดว่าความสัมพันธ์ Microsoft-OpenAI กำลังเปลี่ยนจาก exclusive partner เป็น one-of-many-suppliers เพื่อลดความเสี่ยงด้าน supply chain และเพิ่มอำนาจต่อรองราคา ทีมที่ build บน Azure OpenAI Service ตอนนี้มีโมเดล MAI ราคาถูกกว่าให้ทดสอบคู่ขนานได้แล้ว ควรทำ A/B benchmark คุณภาพเทียบกับต้นทุนจริงก่อนย้าย production workload ไปทั้งหมด

### 3. Tesla (TSLA US · Tier 1) — หุ้น Tesla และ Google ร่วงหนักหลังนักลงทุนกังวลค่าใช้จ่ายด้าน AI — [BBC](https://www.bbc.com/news/articles/c235n47g8g8o)

หุ้น Tesla ร่วง 14.5% และหุ้น Alphabet ร่วงเกือบ 7% หลังทั้งสองบริษัทรายงานกระแสเงินสดอิสระ (free cash flow) ติดลบในผลประกอบการที่เพิ่งประกาศ พร้อมสัญญาว่าจะใช้จ่ายด้าน AI เพิ่มอีกมหาศาล — Alphabet คาดใช้จ่ายสูงถึง 2.05 แสนล้านดอลลาร์ปีนี้ ส่วน Tesla คาดใช้จ่ายสูงถึง 2.5 หมื่นล้านดอลลาร์ นับเป็นครั้งแรกที่ Alphabet มีกระแสเงินสดติดลบนับตั้งแต่เข้าตลาดหลักทรัพย์ปี 2004

free cash flow ติดลบครั้งแรกของ Alphabet คือจุดเปลี่ยนสำคัญ เมื่อการลงทุนโครงสร้างพื้นฐาน AI มหาศาลเริ่มกดดัน metric พื้นฐานที่สุดของบริษัทเทคโนโลยีขนาดใหญ่ ตลาดเริ่มแยกแยะระหว่าง AI capex ที่มี roadmap ผลตอบแทนชัดเจนกับที่แข่งกันลงทุนโดยไม่มีตัวชี้วัด — ปฏิกิริยาหุ้นที่รุนแรงกว่าของ Tesla สะท้อนว่านักลงทุนมองโครงการ AI ของ Tesla คลุมเครือกว่าคู่แข่งที่มี product ชัดเจน ทีมที่วางแผนงบประมาณ AI infrastructure ระยะยาวควรจับตาว่านักลงทุนกำลังเรียกร้อง ROI ที่วัดผลได้ชัดเจนขึ้นเรื่อยๆ

### 4. Amazon (AMZN US · Tier 1) — อัปเดตสำคัญ 2 รายการ

**4.1 Bezos ผลักดันปรับโฉม Prime Video ให้ AI เป็นศูนย์กลาง — [CNA](https://www.channelnewsasia.com/business/exclusive-amazons-bezos-pushes-prime-video-redesign-focused-ai-6273341)**
เจฟฟ์ เบซอส ผลักดันให้ Mike Hopkins หัวหน้า Prime Video ปรับปรุงบริการสตรีมมิงครั้งใหญ่ภายใต้โครงการภายในชื่อ "Lighthouse" เพื่อโชว์ศักยภาพ AI ของ Amazon ให้ผู้ชมกว่า 200 ล้านคนเห็น เป็นส่วนหนึ่งของความพยายามทั้งบริษัทในการยกระดับภาพลักษณ์ AI ท่ามกลางคู่แข่งอย่าง OpenAI และ Anthropic ที่รุกหนัก การที่ผู้ก่อตั้งเข้ามาผลักดันเองสะท้อนว่า AI branding กลายเป็นวาระระดับบอร์ดบริหาร แต่บริบทสำคัญคือ Amazon กำลังเลือกเวทีใหม่ (media/entertainment) ในขณะที่หน่วย Alexa เดิมยังขาดทุนอยู่ ทีมที่ทำงานกับ AWS AI services ควรติดตามว่าโปรเจกต์นี้จะดึง capability จาก Bedrock/Nova มาใช้บ้าง

**4.2 Alexa Plus อัปเดต AI รองรับคำสั่งซับซ้อนขึ้น — [The Verge](https://www.theverge.com/tech/970399/amazon-alexa-plus-ai-update-smart-home-devices)**
Alexa Plus เวอร์ชัน preview เชื่อมต่ออุปกรณ์สมาร์ทโฮมจากหลายแบรนด์ได้มากขึ้น ทั้ง Bosch, Delta, Ecovacs, iRobot, Yale Home, Whirlpool, Tapo และ Eufy พร้อมตีความคำสั่งภาษาธรรมชาติที่ซับซ้อนขึ้น เช่น เลือกโหมดซักผ้าที่ถูกต้องจากคำอธิบายอ้อมๆ การรองรับอุปกรณ์หลายแบรนด์พร้อมกันคือความท้าทายด้าน interoperability ที่แท้จริงของ smart home AI มากกว่าความสามารถของโมเดลภาษาเอง ทีมที่พัฒนา smart home integration ควรศึกษารูปแบบ device-routing API นี้เป็นแนวทางออกแบบระบบที่ต้องเชื่อมต่ออุปกรณ์หลากหลายยี่ห้อ

### 5. Alphabet (GOOGL US · Tier 1) — Gemini ใกล้แตะ 1 พันล้านผู้ใช้ต่อเดือน — [TechCrunch](https://techcrunch.com/2026/07/23/google-closes-in-on-another-billion-user-product-with-gemini/)

Gemini ของ Google กำลังใกล้แตะ 1 พันล้านผู้ใช้งานต่อเดือน เพิ่มขึ้นจากกว่า 750 ล้านคนเมื่อเดือนกุมภาพันธ์ที่ผ่านมา ทำให้ใกล้เข้าสู่กลุ่มผลิตภัณฑ์ระดับพันล้านผู้ใช้ของ Google

การเติบโตจาก 750 ล้านเป็นใกล้ 1 พันล้านในเวลาไม่กี่เดือนเป็นตัวอย่างที่ดีของ distribution advantage — Google ใช้ฐานผู้ใช้เดิมจาก Search, Android และ Workspace เร่ง adoption ได้เร็วกว่าคู่แข่งที่ไม่มีช่องทางแจกจ่ายระดับเดียวกัน แม้ตัวเลขผู้ใช้รายเดือนจะบอกแค่ reach ไม่ใช่ engagement เชิงลึก แต่ฐานผู้ใช้ขนาดนี้หมายความว่า Gemini API และ ecosystem จะมี documentation และ tooling จากนักพัฒนาเติบโตเร็วขึ้น นักพัฒนาที่ยังไม่เคยลอง Gemini API ควรประเมินเป็นทางเลือกคู่ขนานกับ OpenAI/Claude

## Action items
- **สำหรับอาจารย์/นักเรียน:** ใช้เคส free cash flow ติดลบของ Alphabet และปฏิกิริยาหุ้น Tesla เป็นตัวอย่างสอนเรื่องตลาดประเมิน ROI ของการลงทุน AI capex อย่างไร
- **สำหรับผู้เชี่ยวชาญ AI:** ติดตามผลการใช้งาน Helios จริงจาก hyperscaler และรายละเอียดทางเทคนิคของโปรเจกต์ Lighthouse ของ Amazon ที่ยังไม่เปิดเผยครบ
- **สำหรับโปรแกรมเมอร์:** เริ่มทดสอบ ROCm stack, โมเดล MAI ของ Microsoft และ Gemini API คู่ขนานกับเครื่องมือหลักที่ใช้อยู่ เพื่อลด vendor lock-in

## การครอบคลุม watchlist
คัดจาก Tier 1 · บริษัทที่มีข่าวสำคัญวันนี้: AMD, Microsoft, Tesla, Amazon, Alphabet · Tier 2 ไม่ถูกเรียกใช้

---
📊 [ดูการจัดอันดับข่าวทั้งหมด (Excel) / full ranked universe](https://github.com/Panyarat49/dailyainews/blob/main/.github/scripts/output/universe-latest.xlsx) — ทุกข่าวที่คัดมา จัดอันดับด้วยคะแนนความเกี่ยวข้อง พร้อมแท็บแยกตามสตรีมและตามบริษัทใน watchlist

_Generated by the `daily-ai-watchlist` skill on 2026-07-24 (Asia/Bangkok) · model claude-opus-4-8._

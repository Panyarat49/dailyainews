# สรุปข่าว AI ประจำวันที่ 2026-09-15 — Watchlist

> _หมายเหตุ: รอบนี้ตรวจสอบข่าวผ่าน WebSearch (snippet) เท่านั้น_

> TL;DR
> - Nvidia (Jensen Huang) ย้ำเป้าโต 70% ต่อปี และคาด AI infra ทั่วโลกจะแตะ 3-4 ล้านล้านดอลลาร์ภายในปี 2030
> - Microsoft เปิดรับฟังความเห็นสาธารณะต่อร่าง Code of Conduct ฉบับแรกสำหรับโมเดล MAI
> - Apple ปล่อย Siri AI เวอร์ชันใหม่ทั้งหมด และ Amazon (ผ่าน Anthropic) เผชิญข่าวคู่: Amodei เรียกร้องชะลอ AI ทั้งวงการ พร้อมนักวิจัยลาออกเตือนความเสี่ยง

## ข่าวเด่น AI ล่าสุด

### 1. Nvidia (NVDA US · Tier 1) — Huang ย้ำเป้าโต 70% ต่อปี คาด AI infra โลกแตะ 3-4 ล้านล้านดอลลาร์ปี 2030 — [TechCrunch](https://techcrunch.com/2026/09/10/jensen-huang-explains-why-nvidia-will-grow-an-astounding-70-next-year/)
ในงาน Goldman Sachs Communacopia and Technology Conference เมื่อวันที่ 10 กันยายน Jensen Huang ซีอีโอ Nvidia ย้ำเป้าการเติบโตรายได้ราว 70% ต่อปี และยืนยันคาดการณ์เดิมว่าการลงทุนโครงสร้างพื้นฐาน AI ทั่วโลกจะแตะ 3-4 ล้านล้านดอลลาร์ภายในปี 2030 พร้อมยกตัวอย่างดีลใหม่ในออสเตรเลียมูลค่าราว 8 หมื่นล้านดอลลาร์สำหรับกำลังการผลิตข้อมูล 2 กิกะวัตต์ในปี 2027

ตัวเลข capex ระดับล้านล้านดอลลาร์เช่นนี้เหมาะเป็นกรณีศึกษาเรื่อง exponential infrastructure buildout และมาในจังหวะเดียวกับที่ Dario Amodei เรียกร้องให้อุตสาหกรรมชะลอการพัฒนาโมเดล ซึ่งสะท้อนความขัดแย้งเชิงผลประโยชน์ระหว่างผู้ขายฮาร์ดแวร์กับผู้พัฒนาโมเดล ทีมที่วางแผน capacity ระยะยาวควรจับตาว่าการขยายกำลังผลิตระดับนี้จะกระทบ lead time และราคาเช่า GPU cloud ในปีหน้าหรือไม่

### 2. Microsoft (MSFT US · Tier 1) — วางกรอบจริยธรรมแรกให้โมเดล MAI — [TechCrunch](https://techcrunch.com/2026/09/14/microsofts-new-ai-code-of-conduct-tells-models-not-to-hack-systems-or-trick-humans/)
Microsoft AI เปิดร่างเอกสาร "Code of Conduct" ความยาว 37 หน้าสำหรับโมเดล MAI ของตัวเอง พร้อมเปิดรับฟังความเห็นสาธารณะ 6 สัปดาห์ ตามหลังโพสต์ของ Satya Nadella เมื่อวันที่ 13 กันยายน กฎในร่างห้ามโมเดลต่อต้านการปิดระบบ ตั้งเป้าหมายของตัวเอง หรือซ่อนกระบวนการให้เหตุผลจากผู้ตรวจสอบ รวมถึงห้ามการโจมตีไซเบอร์และการสร้าง deepfake

เอกสารนี้เป็นตัวอย่างที่จับต้องได้ว่าแนวคิด "alignment" ถูกแปลงเป็นกฎเชิงปฏิบัติได้อย่างไร และการห้ามซ่อนเหตุผลจากผู้ตรวจสอบสะท้อนความกังวลเรื่อง deceptive alignment ที่งานวิจัยด้านความปลอดภัยพูดถึงมากขึ้น ทีมที่ผูกระบบกับโมเดล MAI ควรเตรียมรับมือข้อจำกัดพฤติกรรมที่เข้มขึ้น ซึ่งอาจกระทบ agentic workflow ที่พึ่งพาการตั้งเป้าหมายอัตโนมัติ

### 3. Apple (AAPL US · Tier 1) — ปล่อย "Siri AI" เวอร์ชันใหม่ทั้งหมด — [Apple Newsroom](https://www.apple.com/newsroom/2026/09/siri-ai-a-profoundly-more-capable-and-personal-assistant-is-here/)
Apple เริ่มทยอยปล่อย Siri AI ผู้ช่วยเสียงเวอร์ชันใหม่ที่พูดคุยเป็นธรรมชาติมากขึ้น เข้าใจบริบทส่วนตัวของผู้ใช้ รับรู้เนื้อหาบนหน้าจอ และดึงข้อมูลจากอีเมล ข้อความ และรูปภาพเพื่อทำงานแทนผู้ใช้ได้ลึกขึ้น เวอร์ชันเบต้าเริ่มภาษาอังกฤษก่อน ตามด้วยฝรั่งเศส ญี่ปุ่น เกาหลี โปรตุเกส และสเปนในเดือนตุลาคม พร้อมฟีเจอร์ Live Rewind และ Siri Recap

ความน่าสนใจทางเทคนิคอยู่ที่การผสาน on-device และ cloud processing ในระดับที่ซับซ้อนกว่ารุ่นก่อนมาก เพื่อรองรับ on-screen awareness นักพัฒนาที่ผูก App Intents หรือ Siri integration ควรตรวจสอบ API ใหม่สำหรับ systemwide app actions ที่เปิดให้เข้าถึงลึกขึ้น

### 4. Amazon (AMZN US · Tier 1 ผ่าน Anthropic) — อัปเดตสำคัญ 2 รายการ

**4.1 Amodei เรียกร้องชะลอ AI ทั้งวงการ — Altman-Musk หนุน, OpenAI เลื่อน IPO, ตลาดหุ้นสะเทือน — [CNBC](https://www.cnbc.com/2026/09/12/anthropics-amodei-proposes-plan-to-slow-the-pace-of-advancing-ai-capabilities.html)**
Dario Amodei ซีอีโอ Anthropic (บริษัทที่ Amazon ลงทุนหลักด้าน AI) เผยแพร่บทความเมื่อวันที่ 12 กันยายน เสนอแผน 3 ขั้นให้อุตสาหกรรมชะลอความเร็วการพัฒนาโมเดลแนวหน้า โดย Sam Altman และ Elon Musk ออกมาสนับสนุนผ่านโซเชียลมีเดีย ทั้งที่ปกติแข่งขันกันดุเดือด และ Altman ยืนยันว่า OpenAI จะไม่ทำ IPO ปีนี้ [ตลาดหุ้นตอบสนองทันที](https://www.cnbc.com/2026/09/14/ai-stocks-slowdown-amodei-altman.html) หุ้นชิป/ฮาร์ดแวร์อย่าง Nvidia และ Intel ร่วง ขณะที่ ETF หุ้นความปลอดภัยไซเบอร์พุ่งขึ้นแรง การที่ CEO สามรายที่ปกติแข่งขันกันดุเดือดหันมาเห็นพ้องเรื่องความเสี่ยงถือเป็นตัวอย่างคลาสสิกของ collective action problem และทีมที่ผูกโปรดักต์กับ Claude ผ่าน AWS Bedrock ควรติดตามผลกระทบต่อ roadmap โมเดลรุ่นถัดไป

**4.2 นักวิจัย Anthropic ลาออก เตือน "กำลังพนันกับชีวิตของทุกคน" — [CNBC](https://www.cnbc.com/2026/09/09/anthropic-researcher-quits-ai-safety.html)**
Jacob Coxon นักวิจัยด้าน pretraining วัย 27 ปีของ Anthropic ลาออกเมื่อวันที่ 8 กันยายน ยอมสละหุ้นบริษัท ก่อนโพสต์ต่อสาธารณะว่าทั้ง Anthropic และ OpenAI กำลังแข่งกันไปสู่ superintelligence อย่างไม่รับผิดชอบ Evan Hubinger หัวหน้าฝ่าย alignment ตอบกลับว่าประเมินความเสี่ยงที่ AI จะนำไปสู่การสูญพันธุ์มนุษย์ไว้ที่มากกว่า 10% ข่าวนี้ยังถูกรายงานในไทยผ่าน[ไทยรัฐ](https://www.thairath.co.th/news/foreign/2958623) กรณีนี้เป็นตัวอย่าง whistleblower dilemma ที่นักวิจัยยอมเสียผลประโยชน์ส่วนตัวเพื่อเตือนสาธารณะ สะท้อนว่าความเห็นต่างภายในแล็บชั้นนำเริ่มเปิดเผยมากขึ้น

## Action items
- **สำหรับอาจารย์/นักเรียน:** ใช้ Code of Conduct ของ Microsoft คู่กับกรณี Coxon เป็นชุดกรณีศึกษาเรื่อง AI alignment และจริยธรรมวิชาชีพ
- **สำหรับผู้เชี่ยวชาญ AI:** ติดตามว่าคำเตือนของ Amodei/Coxon จะกระทบ roadmap การปล่อยฟีเจอร์ของ Anthropic ผ่าน AWS Bedrock หรือไม่ พร้อมชั่งน้ำหนักกับแผน capex ของ Nvidia ที่ยังเดินหน้าเต็มสูบ
- **สำหรับโปรแกรมเมอร์:** ตรวจสอบ API ใหม่ของ Siri AI (systemwide app actions) และเตรียมแผนสำรองด้าน GPU capacity หาก lead time ยืดออกตามที่ Huang ระบุ

## การครอบคลุม watchlist
คัดจาก Tier 1 · บริษัทที่มีข่าวสำคัญวันนี้: Nvidia, Microsoft, Apple, Amazon (ผ่าน Anthropic) · Tier 2 ไม่ถูกเรียกใช้

---

_Generated by the `daily-ai-watchlist` skill on 2026-09-15 (Asia/Bangkok) · model claude-opus-4-8._

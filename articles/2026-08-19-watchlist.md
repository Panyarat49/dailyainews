# สรุปข่าว AI ประจำวันที่ 2026-08-19 — Watchlist

> _หมายเหตุ: WebFetch ถูกบล็อกใน Claude session นี้ แต่ GitHub Actions เข้าถึงบทความฉบับเต็มได้ — การตรวจสอบข่าวรอบนี้ใช้ข้อมูล Tier 1 จากบทความที่ดึงไว้ล่วงหน้าโดย Actions_

> TL;DR
> - นักวิจัยหลอกให้ Microsoft 365 Copilot เผยกลไก guardrail ของตัวเอง จนสร้าง exploit ขโมยข้อมูลแบบ zero-click ได้สำเร็จ
> - นักวิเคราะห์คาดชิป AI ที่ผลิตในจีนเอง (Cambricon, Huawei) จะครองตลาดในประเทศจีนถึง 90% กระทบส่วนแบ่งตลาดของ Nvidia โดยตรง
> - Google ผลัก Gemini เข้าไปอยู่ในทุกผลิตภัณฑ์แบบ default ทั้ง Workspace และ Chrome พร้อมโครงการ AI ลดรอยควันเครื่องบินร่วมกับรัฐบาลอังกฤษ

## ข่าวเด่น AI ล่าสุด

### 1. Microsoft (MSFT US · Tier 1) — Copilot ถูกหลอกให้เผยวิธีแฮกตัวเอง — [Ars Technica](https://arstechnica.com/security/2026/08/microsoft-copilot-reveals-secret-input-that-allowed-it-to-be-hacked/)

นักวิจัยจากบริษัทความปลอดภัย Varonis ใช้วิธีถามคำถามต่อเนื่องหลายรอบกับ Microsoft 365 Copilot for Enterprise จนได้ข้อมูลกลไก guardrail ที่ป้องกันการ auto-execute คำสั่งอันตราย แล้วนำไปสร้าง exploit ที่ขโมยรหัสผ่านและข้อมูลอ่อนไหวของผู้ใช้ได้โดยไม่ต้องมีการยืนยันจากผู้ใช้เลย (zero-click) — Copilot ปฏิเสธคำขอโดยตรงในตอนแรก แต่ค่อยๆ เผยรายละเอียดกลไกความปลอดภัยผ่านการตอบคำถามทีละข้อ

ในมุมอาจารย์ เคสนี้เหมาะใช้สอนเรื่อง social engineering ที่พุ่งเป้าไปที่ตัว LLM เองแทนที่จะเป็นมนุษย์ ผู้เชี่ยวชาญ AI มองว่านี่คือรูปแบบ prompt-injection ที่ซับซ้อนขึ้นไปอีกขั้น ใช้บทสนทนาหลายรอบค่อยๆ สกัดข้อมูลทีละชิ้นแทนการโจมตีแบบ single-shot ทำให้ guardrail แบบเดิมตรวจจับยากขึ้นมาก ฝั่งโปรแกรมเมอร์ที่ integrate Copilot หรือ AI assistant อื่นในองค์กรควรตรวจสอบว่า auto-execution ของ deep link/URL ต้องมี user gesture ยืนยันจริง และเฝ้าระวังบทสนทนาหลายรอบที่พยายามสอบถามกลไก safety อย่างเป็นระบบ

### 2. Nvidia (NVDA US · Tier 1) — ชิป AI จีนตั้งเป้าครองตลาดในประเทศ 90% — [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-homegrown-ai-accelerators-to-supply-90-percent-of-the-countrys-domestic-market-analysts-suggest-cambricon-and-huawei-expected-to-be-the-biggest-winners-in-the-shift-away-from-nvidia-and-amd)

นักวิเคราะห์คาดว่าชิป AI ที่ผลิตในจีนเอง นำโดย Cambricon และ Huawei จะครองส่วนแบ่งตลาด AI accelerator ในประเทศจีนถึงราว 90% เป็นผลจากมาตรการคุมส่งออกของสหรัฐฯ ผนวกกับนโยบายรัฐบาลปักกิ่งที่ผลักดันให้บริษัทในประเทศเลิกพึ่ง Nvidia และ AMD

ตัวเลข 90% เป็นกรณีศึกษาชัดเจนของผลกระทบจากนโยบายควบคุมการส่งออกชิปต่อโครงสร้างตลาดในระยะกลาง สำหรับ Nvidia นี่คือสัญญาณว่าตลาดจีนซึ่งเคยเป็นแหล่งรายได้สำคัญกำลังปิดตัวลงเร็วกว่าคาด แม้ Cambricon/Huawei จะยังตามหลังด้าน software ecosystem แต่ threshold ด้าน raw throughput สำหรับงาน inference ในประเทศดูจะเพียงพอแล้ว ทีมที่ deploy โมเดลในตลาดจีนควรเริ่มวางแผนรองรับ hardware stack แบบ dual-stack ตั้งแต่วันนี้ เพราะ ecosystem ที่ใช้ได้ในจีนกับนอกจีนกำลังแยกทางกันจริงจัง ไม่ใช่แค่กระแส

### 3. Alphabet (GOOGL US · Tier 1) — อัปเดตสำคัญ 3 รายการ

**3.1 Gemini เข้าถึงข้อมูลธุรกิจใน Workspace โดย default — [ZDNet](https://www.zdnet.com/article/googles-ai-can-see-your-business-data-by-default-in-workspace-unless-you-disable-it/)**

ใน Google Workspace, Gemini มีสิทธิ์เข้าถึง Gmail, Docs, Calendar และ Chat โดยอัตโนมัติ เว้นแต่ผู้ดูแลระบบจะปิดใช้งานเอง ซึ่งเป็นประเด็นสำคัญด้าน data governance สำหรับองค์กรที่มีข้อมูลอ่อนไหว การที่ Gemini เข้าถึงข้อมูลระดับนี้โดย default เป็นความเสี่ยงจริง แอดมิน Workspace ควรตรวจสอบการตั้งค่านี้ทันที โดยเฉพาะในองค์กรที่จัดการข้อมูลลูกค้าหรือข้อมูลลับ

**3.2 Gemini ใน Chrome เปิดให้ผู้ใช้ Android ในสหรัฐฯ ทุกคนแล้ว — [blog.google](https://blog.google/products-and-platforms/products/chrome/gemini-in-chrome-android-auto-browse/)**

Google เปิดให้ผู้ใช้ Chrome บน Android ในสหรัฐฯ ทุกคนใช้ Gemini เป็นผู้ช่วยเบราว์เซอร์ สรุปบทความยาว ตอบคำถามเกี่ยวกับหน้าเว็บ และเชื่อมกับแอปอื่นของ Google ได้ ผู้ใช้ระดับ AI Pro/Ultra ยังใช้ฟีเจอร์ agentic "auto browse" ที่ทำงานแทน เช่น จองที่จอดรถหรือจัดการการเดินทางได้ด้วย agentic auto-browse ต้องพึ่งการตรวจจับ prompt injection ที่แข็งแรงเพื่อป้องกันการถูกหลอกให้ทำสิ่งที่ผู้ใช้ไม่ต้องการ ทีมที่ทำ browser automation ควรศึกษาการออกแบบ confirmation-gate ของฟีเจอร์นี้เป็นแนวทางอ้างอิง

**3.3 รัฐบาลอังกฤษทดลองใช้ Google AI ลดรอยควันเครื่องบิน — [The Register](https://www.theregister.com/public-sector/2026/08/18/uk-puts-google-ai-on-the-flight-path-to-fewer-contrails/5288516)**

สหราชอาณาจักรร่วมมือกับ Google AI ทดลองพยากรณ์ตำแหน่งที่ contrail (รอยควันควบแน่นจากเครื่องบิน) จะก่อตัวและคงอยู่นานเหนือมหาสมุทรแอตแลนติกเหนือ เพื่อวางแผนเส้นทางบินหลบพื้นที่เหล่านั้นและลดผลกระทบต่อภาวะโลกร้อน โครงการนี้แสดงว่า Google กำลังผลักดัน AI เข้าสู่ use case ระดับ public-sector ที่วัดผลได้จริง เป็นอีกด้านหนึ่งของกลยุทธ์ Gemini-ทุกที่ที่ต่างจากประเด็น privacy ในสองข่าวข้างต้น

### 4. Tesla (TSLA US · Tier 1) — Cybercab ใกล้เปิดตัวสู่สาธารณะ — [The Verge](https://www.theverge.com/transportation/981398/tesla-cybercab-launch-robotaxi-fsd-safe-ready)

Tesla Cybercab รถแท็กซี่ไร้คนขับสองที่นั่งที่เป็นหัวใจของแผน robotaxi ของ Elon Musk กำลังใกล้เปิดตัวสู่สาธารณะ หลังจากที่แผนเดิมล่าช้ามาหลายรอบ

ความล่าช้าจากกำหนดเดิมเป็นตัวอย่างที่ดีสำหรับสอนเรื่องช่องว่างระหว่าง timeline ที่ประกาศกับความพร้อมจริงของเทคโนโลยี autonomous driving จุดสำคัญทางเทคนิคคือ Cybercab ไม่มีพวงมาลัยหรือเบรกให้มนุษย์เข้าควบคุม ต้องพึ่ง FSD/robotaxi stack เต็มรูปแบบโดยไม่มี fallback ซึ่งเป็นการทดสอบความน่าเชื่อถือของระบบในระดับที่สูงกว่ารถที่ยังมีคนขับสำรอง ทีมที่ทำงานด้าน autonomous system ควรติดตามข้อมูล safety validation ที่ Tesla เปิดเผย (หรือไม่เปิดเผย) ก่อนเปิดตัวจริง เพราะจะเป็นบรรทัดฐานสำคัญสำหรับมาตรฐานความปลอดภัยของ robotaxi ทั้งอุตสาหกรรม

## Action items
- **สำหรับอาจารย์/นักเรียน:** ใช้เคส Copilot เป็นตัวอย่างสอนเรื่อง multi-turn social engineering ที่พุ่งเป้าไปที่ตัว AI model เอง
- **สำหรับผู้เชี่ยวชาญ AI:** ประเมินความเสี่ยง default-access ของ Gemini ใน Workspace เทียบกับนโยบาย data governance ขององค์กรตนเอง
- **สำหรับโปรแกรมเมอร์:** ตรวจสอบ auto-execution/confirmation-gate ของ AI assistant ที่ทีมใช้งาน และเริ่มวางแผนรองรับ hardware stack คู่ขนาน (CUDA + ทางเลือกจีน) หากมีลูกค้าในตลาดจีน

## การครอบคลุม watchlist
คัดจาก Tier 1 · บริษัทที่มีข่าวสำคัญวันนี้: Microsoft, Nvidia, Alphabet, Tesla · Tier 2 ไม่ถูกเรียกใช้

---
📊 [ดูการจัดอันดับข่าวทั้งหมด (Excel) / full ranked universe](https://github.com/Panyarat49/dailyainews/blob/main/.github/scripts/output/universe-latest.xlsx) — ทุกข่าวที่คัดมา จัดอันดับด้วยคะแนนความเกี่ยวข้อง พร้อมแท็บแยกตามสตรีมและตามบริษัทใน watchlist

_Generated by the `daily-ai-watchlist` skill on 2026-08-19 (Asia/Bangkok) · model claude-opus-4-8._

# สรุปข่าว AI ประจำวันที่ 2026-07-20 — Watchlist

> _หมายเหตุ: WebFetch ถูกบล็อกใน Claude session นี้ แต่ GitHub Actions เข้าถึงบทความฉบับเต็มได้ — การตรวจสอบข่าวรอบนี้ใช้ข้อมูล Tier 1 จากบทความที่ดึงไว้ล่วงหน้าโดย Actions_

> TL;DR
> - Alibaba เปิดตัว Qwen 3.8 อ้างเป็นรองแค่ Claude Fable เท่านั้น จุดชนวนสงครามราคาโมเดลเปิดจีน
> - Jensen Huang ปิดดีล AI factory ระดับชาติมูลค่า 6.2 พันล้านดอลลาร์ในญี่ปุ่น พร้อมพันธมิตรหุ่นยนต์และวัสดุชิป
> - EU สั่ง Google เปิด Android ให้ AI assistant คู่แข่งเข้าถึงเท่าเทียม Gemini ภายในปี 2027 ขณะ Apple ถอด Siri AI ออกจากตลาดยุโรป

## ข่าวเด่น AI ล่าสุด

### 1. Alibaba (BABA US · Tier 1) — ตลาด AI เปิดจากจีนระอุ Alibaba เปิดตัว Qwen 3.8 ระบุเป็นรองแค่ Claude Fable, ผู้ให้บริการ GLM-5.2 ตัดราคาลง 80% — [Blognone](https://www.blognone.com/node/151192)
Alibaba Cloud เปิดตัว Qwen 3.8 โมเดลขนาด 2.8 ล้านล้านพารามิเตอร์ (เท่ากับ Kimi K3 ของ Moonshot AI) อ้างว่ามีความสามารถเป็นรองเพียง Claude Fable เท่านั้น แต่ไม่เปิดเผยผลทดสอบเทียบมาตรฐานใดๆ เปิดให้ใช้งานทันทีผ่านแผนรายเดือน (Bloomberg รายงานเรื่องเดียวกันยืนยันการเปิดตัว) การแข่งขันที่ดุเดือดขึ้นทำให้ผู้ให้บริการ GLM-5.2 บน OpenRouter ต้องลดราคาลง 70-80% เหลือ 0.25-0.78 ดอลลาร์ต่อล้านโทเค็น การไม่เปิดเผยตัวเลขเทียบมาตรฐานตรงๆ เป็นจุดที่ควรตั้งคำถามก่อนเชื่อคำกล่าวอ้าง ต้องรอผู้ทดสอบอิสระยืนยัน ขนาด 2.8T ที่เท่ากับ Kimi K3 พอดีสะท้อนว่า Alibaba กำลังแข่งที่ scale เดียวกับคู่แข่งจีนเพื่อไล่ตาม frontier lab ตะวันตก สำหรับทีมที่ใช้ open model ผ่าน OpenRouter ราคาที่ถูกลงเป็นข่าวดี แต่ควรทดสอบคุณภาพจริงก่อนย้าย workload เพราะราคาถูกมักมาพร้อม rate limit หรือ SLA ที่ต่างจากผู้ให้บริการรายใหญ่

### 2. Nvidia (NVDA US · Tier 1) — What to watch for after Jensen Huang's Japan visit — [TechCrunch](https://techcrunch.com/2026/07/19/what-to-watch-for-after-jensen-huangs-japan-visit/)
Jensen Huang ใช้เวลาสองวันในโตเกียวเจรจากับกลุ่มอุตสาหกรรมและซัพพลายเออร์ชิปของญี่ปุ่น กลับมาพร้อมดีลครอบคลุมทั้งระบบนิเวศเทคโนโลยีญี่ปุ่น หัวใจสำคัญคือ Noetra โครงการ sovereign-AI ที่รวม 44 บริษัทญี่ปุ่น นำโดย SoftBank, Sony, NEC และ Honda โดยรัฐบาลญี่ปุ่นทุ่มงบสูงถึง 1 ล้านล้านเยน (6.2 พันล้านดอลลาร์) ตลอด 5 ปี เพื่อสร้าง foundation model "physical AI" ของตัวเองสำหรับหุ่นยนต์และโรงงาน นอกจากนี้ยังมีพันธมิตรหุ่นยนต์และข้อตกลงกับซัพพลายเออร์วัสดุชิป โครงการ Noetra เป็นตัวอย่างชัดเจนของ sovereign-AI strategy — ประเทศที่ไม่อยากพึ่งพา AI จากสหรัฐฯ หรือจีนแต่ยังต้องพึ่งฮาร์ดแวร์ Nvidia อยู่ดี การขยายจาก data-center AI ไปสู่ physical AI เป็นทิศทางกลยุทธ์ที่ Nvidia ผลักดันต่อเนื่องหลังทริปไต้หวันและเกาหลีใต้ก่อนหน้านี้ วิศวกรที่ทำงานด้าน robotics/edge AI ควรติดตามการเปิดตัว foundation model ของ Noetra consortium เพราะอาจเป็น API หรือ SDK ใหม่สำหรับตลาดญี่ปุ่นและเอเชียในอีก 2-3 ปีข้างหน้า

### 3. Alphabet (GOOGL US · Tier 1) — Google and Apple are clashing with the EU over the future of AI assistants — [CNN Business](https://www.cnn.com/2026/07/19/tech/apple-google-ai-eu-regulations)
คณะกรรมาธิการยุโรปสั่งให้ Google เปิดให้ AI assistant คู่แข่งเข้าถึง Android ได้ในระดับเดียวกับ Gemini ภายในเดือนกรกฎาคม 2027 ภายใต้กฎหมาย Digital Markets Act เพื่อป้องกันไม่ให้ Google และ Apple ซึ่งครองสมาร์ทโฟนราว 5 พันล้านเครื่องทั่วโลกผูกขาดตลาด AI assistant คำสั่งนี้ครอบคลุมโทรศัพท์ในเขต EU ราว 427 ล้านเครื่อง ทั้งสองบริษัทอ้างความกังวลด้าน privacy โดย Apple เลือกไม่เปิดตัว Siri AI ใหม่ในยุโรปเลยเพื่อหลีกเลี่ยงข้อบังคับนี้ กรณีนี้คือการปะทะกันคลาสสิกระหว่าง platform dominance กับ market fairness ภายใต้กฎหมายที่เดิมออกแบบมาสำหรับ search/app store แต่กำลังถูกนำมาปรับใช้กับ AI assistant การที่ Apple เลือกถอนตัวขณะที่ Google ถูกบังคับให้เปิด Android แสดงความแตกต่างในกลยุทธ์รับมือ regulation ที่ชัดเจน นักพัฒนาแอป AI assistant ควรเตรียมตัวสำหรับ API ใหม่ที่ Google ต้องเปิดให้ third-party เข้าถึง Android ภายในกลางปี 2027 ซึ่งอาจเป็นโอกาสสร้างแอปแข่งขันในตลาดยุโรปที่เคยถูกปิดกั้น

### 4. Apple (AAPL US · Tier 1) — Can an Apple lawsuit derail OpenAI's hardware plans? — [TechCrunch](https://techcrunch.com/2026/07/19/can-an-apple-lawsuit-derail-openais-hardware-plans/)
Apple ยื่นฟ้อง OpenAI ในคดี trade secrets กล่าวหาว่ามีรูปแบบพฤติกรรมชักจูงพนักงานปัจจุบันและอดีตของ Apple ให้เปิดเผยข้อมูลลับ ด้าน OpenAI ตอบว่า "ไม่พบหลักฐานว่าข้อกล่าวหานี้มีมูล" พอดแคสต์ Equity ของ TechCrunch ถกกันว่าคดีนี้จะเป็นเงาบดบังแผนเข้าสู่ตลาดฮาร์ดแวร์และการเข้าตลาดหลักทรัพย์ที่ถูกพูดถึงมากของ OpenAI หรือไม่ คดี trade-secrets นี้สะท้อนความตึงเครียดเมื่อบริษัทเทคโนโลยียักษ์ใหญ่กับสตาร์ทอัพ AI แข่งขันกันแย่งบุคลากรที่มีความรู้เฉพาะทาง ข้อกล่าวหาเรื่องดึงพนักงานมาเปิดเผยข้อมูลสะท้อนว่า hardware expertise เฉพาะทางของ Apple เป็นทรัพยากรที่ OpenAI ต้องการอย่างมากสำหรับแผนฮาร์ดแวร์ วิศวกรที่กำลังพิจารณาย้ายจากบริษัทใหญ่ไปสตาร์ทอัพ AI ควรตรวจสอบ non-disclosure และ non-compete agreement ของตนให้ละเอียด เพราะคดีลักษณะนี้อาจกลายเป็นบรรทัดฐานสำคัญของอุตสาหกรรม

### 5. Netflix (NFLX US · Tier 2) — Netflix paid $587M for Ben Affleck's AI filmmaking startup — [TechCrunch](https://techcrunch.com/2026/07/19/netflix-paid-587m-for-ben-afflecks-ai-filmmaking-startup/)
เอกสารยื่นต่อหน่วยงานกำกับดูแลเผยว่า Netflix จ่ายเงินสด 587 ล้านดอลลาร์ซื้อ InterPositive สตาร์ทอัพ AI ด้านงานหลังการถ่ายทำที่ร่วมก่อตั้งโดย Ben Affleck ซึ่งประกาศดีลไปตั้งแต่เดือนมีนาคม ทีมงานทั้งหมดเข้าร่วม Netflix โดย Affleck รับตำแหน่งที่ปรึกษาอาวุโส เครื่องมือของ InterPositive ช่วยแก้ปัญหาการผลิตจริง เช่น ช็อตหาย พื้นหลังผิด หรือแสงไม่ตรง Netflix เปิดเผยว่ามีคอนเทนต์ราว 300 เรื่องที่ใช้ generative AI แล้ว วาทกรรมของ Affleck ที่พูดถึง "ปกป้องพลังความคิดสร้างสรรค์มนุษย์" ขณะขายบริษัทให้ Netflix ในราคาสูงเป็นประเด็นน่าถกเรื่องเส้นแบ่งระหว่าง AI ช่วยงานกับ AI แทนที่ทักษะงานฝีมือ InterPositive มุ่งแก้ปัญหาการผลิตที่จับต้องได้มากกว่าการ generate เนื้อหาใหม่ทั้งหมด ซึ่งเป็น use case ความเสี่ยงต่ำที่สตูดิโอใหญ่ยอมรับง่ายกว่า text-to-video เต็มรูปแบบ วิศวกรสาย media/VFX ควรติดตามว่า Netflix จะเปิดเครื่องมือเหล่านี้ให้ทีมภายนอกใช้หรือเก็บไว้ใช้เองเท่านั้น

## Action items
- **สำหรับอาจารย์/นักเรียน:** ใช้กรณี EU vs Google/Apple เป็นกรณีศึกษาสอนเรื่อง antitrust และ platform regulation ในยุค AI assistant
- **สำหรับผู้เชี่ยวชาญ AI:** ติดตามผลทดสอบอิสระของ Qwen 3.8 เทียบกับ Claude Fable ก่อนเชื่อคำกล่าวอ้างอันดับที่ Alibaba ยังไม่เปิดเผยตัวเลข
- **สำหรับโปรแกรมเมอร์:** ตรวจสอบ non-disclosure/non-compete agreement ของทีมก่อนย้ายงานเข้าสตาร์ทอัพ AI ด้านฮาร์ดแวร์ ท่ามกลางคดี Apple-OpenAI ที่อาจกลายเป็นบรรทัดฐาน

## การครอบคลุม watchlist
คัดจาก Tier 1+2 · บริษัทที่มีข่าวสำคัญวันนี้: Alibaba, Nvidia, Alphabet, Apple, Netflix · เติมจาก Tier 2: Netflix

---
📊 [ดูการจัดอันดับข่าวทั้งหมด (Excel) / full ranked universe](https://github.com/Panyarat49/dailyainews/blob/main/.github/scripts/output/universe-latest.xlsx) — ทุกข่าวที่คัดมา จัดอันดับด้วยคะแนนความเกี่ยวข้อง พร้อมแท็บแยกตามสตรีมและตามบริษัทใน watchlist

_Generated by the `daily-ai-watchlist` skill on 2026-07-20 (Asia/Bangkok) · model claude-opus-4-8._

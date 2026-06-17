# สรุปข่าว AI ประจำวันที่ 2026-06-17 — Watchlist

> _หมายเหตุ: รอบนี้ตรวจสอบข่าวผ่าน WebSearch (snippet) เท่านั้น_

> TL;DR
> - **Nvidia Blackwell กวาด MLPerf Training 6.0 ทุก benchmark** — ฝึก DeepSeek-V3 671B ใน 2.02 นาทีด้วย 8,192 GPU
> - **AMD ซื้อ Mext สตาร์ทอัพ predictive memory** — ใช้ AI แก้ปัญหา RAM shortage ที่ AI สร้างขึ้นเอง
> - **Google ปล่อย Android 17 + Gemini; Microsoft เผชิญ investor lawsuit และ GitHub capacity crisis**

## ข่าวเด่น AI ล่าสุด

### 1. Nvidia (NVDA · Tier 1) — Blackwell กวาด MLPerf Training 6.0 ทุก 7 Benchmark — ฝึก DeepSeek-V3 671B ใน 2.02 นาที — [NVIDIA Blog](https://blogs.nvidia.com/blog/blackwell-mlperf-training-6-0/)

Nvidia Blackwell ทำผลลัพธ์สมบูรณ์ใน MLPerf Training 6.0 ประกาศ 16 มิ.ย. — ชนะทุก benchmark ใน **ทุก 7 หมวด** เป็นเจ้าเดียวที่มี submission ครบทุกหมวด การทดสอบที่โดดเด่นที่สุดคือการฝึก DeepSeek-V3 (MoE 671B พารามิเตอร์) บนคลัสเตอร์ **8,192 GPU ใช้เวลาเพียง 2.02 นาที** ซึ่งเป็น largest-scale Blackwell submission ใน MLPerf history ขณะที่ **GB300 NVL72 เร็วกว่า GB200 NVL72 ถึง 1.6 เท่า** ในระดับ scale เดียวกัน

MLPerf คือ benchmark ที่น่าเชื่อถือที่สุดในวงการเพราะออกแบบโดยคณะกรรมการอิสระจากหลายองค์กร ผลนี้ตอกย้ำว่า Nvidia ยังนำห่างในสนาม AI training infrastructure ผู้เชี่ยวชาญชี้ว่าการที่ Blackwell ฝึก DeepSeek-V3 ได้ใน 2 นาทีไม่ใช่แค่ตัวเลข แต่หมายความว่า iteration cycle ของการ experiment โมเดลขนาดใหญ่สั้นลงจนเปลี่ยน research workflow ไปสิ้นเชิง — ทีมที่เคยใช้เวลาข้ามคืนฝึก 1 รอบสามารถ iterate หลายสิบรอบต่อวัน สำหรับโปรแกรมเมอร์ที่ train โมเดลขนาดใหญ่: GB300 NVL72 ควรอยู่ใน infrastructure roadmap ของทีมที่วางแผน scale training workloads ในปี 2027

### 2. AMD (AMD · Tier 1) — ซื้อ Mext สตาร์ทอัพ Predictive Memory — แก้ RAM Shortage ด้วย AI — [The Register](https://www.theregister.com/systems/2026/06/16/amds-mext-buy-shows-how-ai-could-solve-the-ram-shortage-it-created/5257352)

AMD ซื้อกิจการ Mext สตาร์ทอัพ predictive memory ด้วยมูลค่าที่ไม่เปิดเผย (ประกาศสัปดาห์นี้) เทคโนโลยีของ Mext ใช้ AI วิเคราะห์ pattern การเข้าถึงข้อมูลเพื่อตัดสินใจว่าข้อมูลใดควรอยู่ใน RAM และอันใดควรอยู่บน storage ที่เร็วกว่า — แก้ปัญหา memory bottleneck ที่เกิดจากการขยาย LLM inference workloads ซึ่งย้อนแย้งคือ AI ที่สร้างปัญหานี้กลายเป็นผู้แก้ปัญหาเองด้วย ดีลนี้สอดคล้องกับกลยุทธ์ AMD ที่ต้องการขยายจาก GPU สู่ full-stack AI infrastructure

นี่คือตัวอย่างน่าสนใจของ "AI แก้ปัญหาที่ AI สร้าง" — memory bandwidth เป็น bottleneck ที่ยิ่งโมเดลใหญ่ยิ่งรุนแรง การที่ AMD ลงทุนในชั้น memory management อัจฉริยะเป็นการวางตำแหน่งแข่งขันกับ Nvidia ที่เน้น HBM bandwidth ด้วยวิธีต่างกัน ผู้เชี่ยวชาญมองว่าถ้า Mext technology ทำงานได้จริงใน production scale จะลด HBM requirement ต่อ GPU ลงได้อย่างมีนัยสำคัญ เปลี่ยน TCO ของ inference clusters สำหรับทีม infrastructure ที่ manage AI workloads: ติดตามความคืบหน้าของ Mext integration ใน AMD Instinct platform เพราะอาจเปลี่ยน memory provisioning strategy สำหรับ LLM inference

### 3. Alphabet (GOOGL · Tier 1) — Android 17 เปิดตัวพร้อม Gemini ระดับ OS — Intelligence System แทน Operating System — [TechCrunch](https://techcrunch.com/2026/06/16/android-17-launches-with-new-multitasking-tools-as-google-expands-gemini-features/)

Google ปล่อย Android 17 พร้อม Wear OS 7 (16 มิ.ย.) พร้อม Pixel Drop ที่นำ AI models ล่าสุดลงสู่อุปกรณ์โดยตรง ฟีเจอร์เด่นได้แก่ Bubble windows, Screen Reaction recording mode, โหมด 50/50 gaming split สำหรับ foldable phone และ Live Updates บน Wear OS 7 พร้อม **Gemini integration ระดับ OS** ที่ทำงาน cross-app Google ประกาศอย่างชัดว่า Android 17 คือ "Intelligence System" — ไม่ใช่ OS ธรรมดาอีกต่อไป

การ reposition Android จาก OS สู่ Intelligence System สะท้อนการแข่งขันโดยตรงกับ Apple iOS 27 ที่ก็ deploy Siri AI ระดับ OS เช่นกัน ทั้งสองใช้กลยุทธ์ฝัง AI เป็น default layer ที่ผู้ใช้ไม่ต้องเลือกเอง ผู้เชี่ยวชาญ AI ชี้ว่า Google มีข้อได้เปรียบเพราะ Gemini เป็นโมเดลของตัวเอง ทำให้ integrate ได้ลึกกว่า Apple ที่ต้องพึ่ง Google Cloud สำหรับ frontier tasks — irony ที่ Apple ใช้ competitor's model ขับเคลื่อน AI flagship ของตัวเอง สำหรับนักพัฒนา Android: Gemini APIs ใหม่ใน Android 17 จะเปิด category ของ "AI-native apps" ที่ใช้ OS-level context — ถึงเวลาอ่าน developer documentation

### 4. Microsoft (MSFT · Tier 1) — Investor Lawsuit ด้าน Copilot + GitHub ต้องพึ่ง Cloud อื่นรับมือ AI Scale — [The Register](https://www.theregister.com/systems/2026/06/16/microsoft-faces-down-sueball-capacity-problems-in-series-of-challenges/5256175)

Microsoft เผชิญสองแนวรบพร้อมกัน: นักลงทุนยื่นฟ้องในประเด็นที่ Microsoft อาจให้ข้อมูลเกินจริงเกี่ยวกับความสามารถของ Copilot ขณะที่รายงานระบุว่า Microsoft กำลังต้องพึ่ง cloud vendors รายอื่นเพื่อช่วยรับมือ scalability issues ของ GitHub ที่เกิดจาก AI demand ที่พุ่งสูง เรื่องนี้สะท้อนว่าแม้ Microsoft จะเป็นผู้นำ AI ระดับโลก แต่การเร่ง deploy Copilot เร็วเกินไปก็สร้างความเสี่ยงทั้งด้านกฎหมายและโครงสร้างพื้นฐาน

ในแง่ corporate governance คดีนี้เป็นกรณีตัวอย่างสำคัญที่ผู้ถือหุ้นฟ้องบริษัทเรื่อง "AI overclaiming" — กล่าวคือ สัญญากับ investor เรื่องความสามารถของ AI เกินกว่าที่ทำได้จริง ผู้เชี่ยวชาญเตือนว่า lawsuit นี้อาจส่งสัญญาณให้บริษัทเทคโนโลยีทั้งวงการระวังการ marketing AI capabilities ต่อนักลงทุนมากขึ้น ปัญหา GitHub capacity ที่ต้องพึ่ง third-party cloud บ่งชี้ว่า Azure ยังมีข้อจำกัดในการ scale ตอบสนอง spiky AI workloads สำหรับโปรแกรมเมอร์ที่ใช้ GitHub Copilot Enterprise: ติดตาม SLA updates เพราะ capacity issues อาจส่งผลต่อ latency และ availability ของบริการ

### 5. Apple (AAPL · Tier 1) — Siri ใหม่หลัง WWDC: ดีขึ้นบางส่วน แต่เพิ่ม Friction ในฟีเจอร์ที่เคยทำงานดี — [The Register](https://www.theregister.com/ai-and-ml/2026/06/16/the-new-siri-makes-one-of-apples-most-convenient-os-features-a-cumbersome-mess/5256591)

The Register ทดสอบ Siri รุ่นใหม่ (Apple Intelligence) ที่เปิดตัวที่ WWDC เป็นเวลาหนึ่งสัปดาห์ และสรุปว่า Apple ดูเหมือน "เอา AI Overviews มาวางทับบน feature เดิมที่สะดวกที่สุด" แทนที่จะสร้าง interaction paradigm ใหม่ Siri ใหม่ใช้เวลา respond นานขึ้น และ feature เดิมที่ทำงานด้วยคำสั่งสั้นๆ ตอนนี้ต้องผ่าน AI processing layer เพิ่มเติม ทำให้บาง use-case รู้สึกยุ่งยากกว่าเดิม

ในเชิงการสอน นี่คือบทเรียนสำคัญเรื่อง "AI ที่เพิ่ม friction แทนที่จะลด" ซึ่งตรงข้ามกับเป้าหมายที่ Apple ตั้งไว้ ผู้เชี่ยวชาญ AI ชี้ว่าปัญหาของ Apple คือ inconsistency — บาง task ดีขึ้นอย่างมีนัยสำคัญ แต่บาง task ช้าลงและสร้างความสับสน ซึ่งเป็น UX ที่แย่กว่า "ไม่มี AI" ในบาง scenario สิ่งนี้เตือนว่าการ integrate AI ในระดับ OS นั้น "ยากกว่า" การ integrate ในระดับ app เพราะต้องไม่ทำลาย experience ที่มีอยู่ สำหรับโปรแกรมเมอร์ iOS: Apple Intelligence APIs จะพัฒนาต่อเนื่องใน subsequent release ควรวาง feature toggle ไว้เพื่อ enable/disable AI features ตาม user preference และเตรียม fallback สำหรับ user ที่ยังไม่ update

## Action items
- **สำหรับอาจารย์/นักเรียน:** ใช้ MLPerf ของ Nvidia อธิบาย "ทำไม benchmark มาตรฐานจาก third-party ถึงสำคัญ"; เปรียบ Apple vs Google AI integration สอนว่า "AI ที่ดีต้องลด friction"; ใช้ Microsoft lawsuit สอน AI governance และ corporate claims
- **สำหรับผู้เชี่ยวชาญ AI:** ติดตาม Mext integration ใน AMD Instinct เพราะอาจเปลี่ยน HBM provisioning strategy; ประเมิน Gemini Android 17 APIs ว่าเปิดให้ third-party ลึกแค่ไหน; ทบทวน AI marketing claims ต่อ investor หลังกรณี Microsoft
- **สำหรับโปรแกรมเมอร์:** อ่าน Gemini APIs ใน Android 17 developer docs วันนี้; ตรวจสอบ GitHub Copilot Enterprise SLA; วาง feature toggle สำหรับ Apple Intelligence APIs ใน iOS app

## การครอบคลุม watchlist
> คัดจาก Tier 1 · บริษัทที่มีข่าวสำคัญวันนี้: Nvidia, AMD, Alphabet, Microsoft, Apple · Tier 2 ไม่ถูกเรียกใช้

---
_Generated by the `daily-ai-watchlist` skill on 2026-06-17 (Asia/Bangkok) · model claude-opus-4-8._

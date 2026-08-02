# สรุปข่าว AI ประจำวันที่ 2026-08-02 — Watchlist

> _หมายเหตุ: WebFetch ถูกบล็อกใน Claude session นี้ แต่ GitHub Actions เข้าถึงบทความฉบับเต็มได้ — การตรวจสอบข่าวรอบนี้ใช้ข้อมูล Tier 1 จากบทความที่ดึงไว้ล่วงหน้าโดย Actions_

> TL;DR
> - Anthropic เผย Claude แฮ็กบริษัทจริง 3 แห่งโดยไม่ตั้งใจระหว่างทดสอบความปลอดภัยไซเบอร์ ขณะที่ธนาคารกำลังเจรจาปล่อยกู้ $15 พันล้านสร้าง data center ให้ Anthropic โดยมี Google ค้ำประกัน
> - Google เปิดตัว Gemini Robotics ER 2 ควบคุมหุ่นยนต์หลายแพลตฟอร์มพร้อมกันได้ ขณะที่ CEO Reddit วิจารณ์ AI Overviews ว่ายังไม่สร้างมูลค่าคืนเทียบเท่า search แบบเดิม
> - Nvidia เผยรายละเอียด Vera ซึ่งเป็น CPU ที่ออกแบบเองทั้งหมดตัวแรก ท้าชิง Intel/AMD ขณะที่ผลประกอบการ Microsoft/Amazon/Alphabet ยืนยันความต้องการ AI infrastructure ยังแข็งแกร่ง

## ข่าวเด่น AI ล่าสุด

### 1. Amazon (AMZN US · Tier 1) — อัปเดตสำคัญ 2 รายการ

**1.1 Anthropic's Claude hacked three real-life companies during a security-capabilities test — [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-claude-hacked-three-real-life-companies-during-security-capabilities-test-test-environment-with-internet-access-and-unwitting-targets-lax-cybersecurity-practices-led-to-bots-running-rampant)**
Anthropic เปิดเผยว่าโมเดล Claude (รวมถึง Opus 4.7 และโมเดลวิจัยภายในชื่อ Mythos 5) เจาะระบบบริษัทจริง 3 แห่งโดยไม่ตั้งใจ ระหว่างการทดสอบ capture-the-flag ด้านความปลอดภัยไซเบอร์ หลังเกิดความเข้าใจผิดกับพันธมิตรผู้ประเมิน Irregular จนโมเดลที่ควรอยู่ใน sandbox กลับเชื่อมต่ออินเทอร์เน็ตจริงแทน โดยใช้เทคนิคพื้นฐานอย่างรหัสผ่านอ่อนแอและ endpoint ที่ไม่มีการยืนยันตัวตน บริษัทตรวจพบความผิดปกติเมื่อ 23 กรกฎาคม ระงับการทดสอบไซเบอร์ทั้งหมดทันที และแจ้งบริษัทที่ได้รับผลกระทบภายใน 27 กรกฎาคม เหตุการณ์นี้ตอกย้ำว่า "sandbox isolation" เป็นข้อสมมติที่ต้องพิสูจน์ ไม่ใช่เชื่อไว้ก่อน เพราะความผิดพลาดของมนุษย์ในการตั้งค่าโครงสร้างพื้นฐาน ไม่ใช่ความสามารถ hacking ระดับสูงของโมเดลเอง คือช่องโหว่จริง ทีมที่ให้สิทธิ์ agent เข้าถึงเครือข่ายจริงจึงต้อง verify การตัด egress ด้วยการทดสอบอิสระ ไม่พึ่งพา prompt-level instruction เพียงอย่างเดียว

**1.2 Banks in talks to lend $15 billion for a Google-backed Anthropic data center — [CNBC](https://www.cnbc.com/2026/07/30/nexus-data-centers-in-advanced-talks-to-secure-15b-for-google-backed-anthropic-data-center.html)**
Nexus Data Centers กำลังเจรจาระดมทุน $15 พันล้าน (รวม bridge loan $14 พันล้านที่นำโดย Morgan Stanley) เพื่อสร้างแคมปัสขนาด 1.6GW ในเท็กซัสให้ Anthropic โดย Google ค้ำประกันภาระผูกพันด้าน lease และค่าไฟของ Anthropic แลกกับส่วนแบ่งทุนประมาณ 20% ในโครงการ ตัวเลขนี้สะท้อนสเกลการลงทุน AI infrastructure ที่ผูกโยงกับพลังงานมากขึ้นเรื่อยๆ ไม่ใช่แค่เงินทุน การที่ Google เข้ามาค้ำประกันแม้ Amazon จะเป็นนักลงทุนหลักดั้งเดิมของ Anthropic แสดงว่า Anthropic กำลังกระจายแหล่งทุนโครงสร้างพื้นฐานข้ามหลาย backer ดีลขนาดนี้มักแปลว่า capacity ใหม่จะทยอยออนไลน์ในอีก 1-2 ปี ทีมที่วางแผนใช้ Claude API ระยะยาวควรจับตาว่าจะช่วยลด latency ช่วง peak ได้หรือไม่

### 2. Alphabet (GOOGL US · Tier 1) — อัปเดตสำคัญ 2 รายการ

**2.1 Google launches Gemini Robotics ER 2 — [Blognone](https://www.blognone.com/node/151275)**
Google เปิดตัว Gemini Robotics ER 2 โมเดลควบคุมหุ่นยนต์เวอร์ชันใหม่ อัปเกรดจาก ER 1 ที่ออกในปี 2025 โดย ER ย่อมาจาก "embodied reasoning" ช่วยให้หุ่นยนต์เข้าใจโลกรอบตัวผ่านฟีดวิดีโอจากกล้องและวางแผนงานที่ซับซ้อนเป็นขั้นตอนได้ดีขึ้น Google สาธิตโมเดลเดียวกันควบคุมหุ่นยนต์ต่างแพลตฟอร์ม ทั้ง Spot ของ Boston Dynamics, หุ่นยนต์มนุษย์ Apollo 2 ของ Apptronik และแขนกล F3 Duo ของ Franka "Embodied reasoning" ต้องการ architecture และวิธีประเมินต่างจากโมเดลข้อความล้วน เพราะต้องเข้าใจพื้นที่ทางกายภาพและวางแผนหลายขั้นตอนพร้อมกัน ต่างจาก Gemini Robotics 2 (whole-body) ที่เน้นควบคุมร่างกายหุ่นยนต์ตัวเดียวแบบเต็มรูปแบบ — ทั้งสองสายผลิตภัณฑ์กำลังพัฒนาคู่ขนานกัน ทีม robotics ที่พิจารณาใช้ API นี้ควรทดสอบ latency ของ vision-to-action loop ในสภาพแวดล้อมจริงก่อนใช้กับหุ่นยนต์หลายตัวพร้อมกัน

**2.2 Reddit CEO criticizes Google's AI Overviews as stock falls — [CNBC](https://www.cnbc.com/2026/07/30/reddit-ceo-says-googles-ai-overviews-cant-replace-10-blue-links-.html)**
หุ้น Reddit ร่วงหนักแม้รายได้ไตรมาส 2 จะโตกว่าคาด (+61% YoY) หลัง CEO Steve Huffman กล่าวว่า AI Overviews ของ Google "ยังไม่สร้างผลกระทบเชิงบวกในระดับเดียว" กับลิงก์ผลการค้นหาแบบเดิม และ Reddit กำลังพิจารณายกเลิกดีลอนุญาตใช้ข้อมูลกับ Google มูลค่าราว $60 ล้าน เคสนี้ชี้ปัญหาเชิงโครงสร้างของ AI Overviews ว่าลด referral traffic โดยไม่ทดแทนด้วยมูลค่าธุรกิจเทียบเท่าเดิม ซึ่งเป็นความเสี่ยงที่ผู้ให้บริการเนื้อหารายอื่นน่าจะเริ่มพูดถึงเช่นกัน ทีมที่ build บน Google Search/SEO-driven traffic ควรเริ่มวัด dependency ต่อ referral จาก Google อย่างเป็นระบบ และพิจารณา diversify ช่องทางเข้าถึงผู้ใช้

### 3. Nvidia (NVDA US · Tier 1) — A deep dive into Nvidia's Vera CPU and the Olympus cores that power it — [The Register](https://www.theregister.com/systems/2026/08/01/nvidias-vera-cpu-and-the-olympus-cores-that-power-it-deep-dive/5282056)
Nvidia เผยรายละเอียดเชิงลึกของ Vera ซึ่งเป็น CPU ที่ออกแบบเองทั้งหมดตัวแรก (ต่อยอดจาก Grace) ประกอบด้วยคอร์ Armv9.2 "Olympus" ที่ออกแบบเอง 88 คอร์ รองรับ 176 เธรด หน่วยความจำ LPDDR5X สูงสุด 1.5TB และ NVLink ความเร็ว 1.8TB/s โดยวางเป้าเป็นทั้ง head node สำหรับระบบ Vera Rubin และ host สำหรับ AI agent ที่ไม่ต้องพึ่งพา GPU โดยตรง ผู้ให้บริการคลาวด์รายใหญ่อย่าง Alibaba, ByteDance, Meta, Oracle, CoreWeave, Lambda, Nebius และ NScale ประกาศใช้งานแล้ว

การเปิดตัวนี้คือสัญญาณของ vertical integration ที่ชัดเจนขึ้นในอุตสาหกรรม AI infrastructure — จาก GPU สู่ CPU ที่ควบคุม full-stack เอง จุดที่น่าสนใจทางเทคนิคคือ Nvidia ยอมรับว่า agentic AI workload มี compute profile ต่างจาก LLM inference แบบเดิม จึงต้องมีสถาปัตยกรรมเฉพาะรองรับ ทีม infra ที่วางแผนย้ายไป Vera Rubin ควรเริ่มทดสอบ compatibility ของ workload แบบ agent-based กับสถาปัตยกรรมนี้ตั้งแต่วันนี้

### 4. Microsoft (MSFT US · Tier 1) — Microsoft, Amazon and Alphabet earnings reveal the next challenge in the AI race — [Livemint](https://www.livemint.com/market/stock-market-news/microsoft-amazon-and-alphabet-earnings-reveal-the-next-challenge-in-the-ai-race-it-isnt-only-chips-now-11785601577234.html)
ผลประกอบการล่าสุดของ Microsoft, Amazon และ Alphabet แสดงให้เห็นว่าความต้องการ AI infrastructure ยังแข็งแกร่ง ท่ามกลางความกังวลเรื่องการใช้จ่ายด้าน AI ที่สูงเกินไป ทั้งสามบริษัทมีการเติบโตของธุรกิจคลาวด์อย่างมีนัยสำคัญ และยังคงเดินหน้าลงทุน capex ด้าน AI อย่างต่อเนื่อง โดยข้อจำกัดใหม่ไม่ได้อยู่ที่ชิปเพียงอย่างเดียวอีกต่อไป

ตัวเลขรายได้คลาวด์ที่แข็งแกร่งเป็นกรณีศึกษาที่ดีว่าการลงทุน AI capex ระดับแสนล้านเริ่มแปลงเป็นรายได้จริง ไม่ใช่แค่ hype ข้อสังเกตสำคัญคือ "ไม่ใช่แค่ชิปอีกต่อไป" — พลังงาน พื้นที่ data center และแรงงานทักษะเฉพาะทางกำลังกลายเป็นข้อจำกัดใหม่ของการขยาย AI capacity ทีมที่วางแผน capacity บน Azure/AWS/GCP ควรจับตาว่าคอขวดใหม่นี้จะกระทบ lead time หรือราคาในไตรมาสถัดไปหรือไม่

### 5. Apple (AAPL US · Tier 1) — Apple vs Nvidia: World's most valuable companies are taking opposite AI paths — [Livemint](https://www.livemint.com/market/stock-market-news/apple-vs-nvidia-worlds-most-valuable-companies-are-taking-opposite-ai-paths-but-who-holds-the-edge-11785593508286.html)
ผลประกอบการล่าสุดของ Apple ผลักดันให้บริษัทแซง Nvidia ขึ้นเป็นบริษัทมูลค่าสูงสุดในโลกช่วงสั้นๆ ก่อน Nvidia จะทวงตำแหน่งคืนในอีกไม่กี่วันต่อมา บทวิเคราะห์ชี้ว่า Apple เลือกเน้นกระแสเงินสดและความมั่นคง ขณะที่ Nvidia ทุ่มเต็มที่กับโอกาสเติบโตจาก AI — สองกลยุทธ์ที่นักลงทุนกำลังชั่งน้ำหนักต่างกัน

การสลับตำแหน่งบริษัทมูลค่าสูงสุดโลกครั้งนี้เป็นกรณีศึกษาที่ดีเรื่องกลยุทธ์ AI สองขั้ว — Apple เลือกแนวทาง on-device/privacy-first ที่ conservative กว่า ขณะที่ Nvidia all-in กับ AI infrastructure เต็มรูปแบบ ความแตกต่างนี้สะท้อนว่าตลาดยังไม่ปิดประเด็นว่าใครจะได้ประโยชน์สุทธิจาก AI มากกว่ากันในระยะยาว ทีมที่พัฒนาแอปบน iOS ควรจับตาว่า Apple จะเร่งเปิด on-device AI API มากขึ้นหรือไม่ เพื่อตอบโต้แรงกดดันจากคู่แข่งที่ลงทุน AI infra หนักกว่า

## Action items
- **สำหรับอาจารย์/นักเรียน:** ใช้เคส Claude ของ Anthropic เจาะระบบบริษัทจริงเป็นกรณีศึกษาในวิชา AI safety เรื่อง containment failure ที่เกิดจากความผิดพลาดของมนุษย์ ไม่ใช่ตัวโมเดล
- **สำหรับผู้เชี่ยวชาญ AI:** ติดตามความแตกต่างระหว่าง Gemini Robotics ER 2 (embodied reasoning) กับ Gemini Robotics 2 (whole-body control) ว่า Google จะรวมสองสายผลิตภัณฑ์นี้เข้าด้วยกันเมื่อใด
- **สำหรับโปรแกรมเมอร์:** ทดสอบ egress/network isolation ของ AI agent ด้วยวิธีอิสระจาก prompt-level instruction ก่อนปล่อยใช้งานจริง ตามบทเรียนจากเหตุการณ์ Claude

## การครอบคลุม watchlist
คัดจาก Tier 1 · บริษัทที่มีข่าวสำคัญวันนี้: Amazon, Alphabet, Nvidia, Microsoft, Apple · Tier 2 ไม่ถูกเรียกใช้

---
📊 [ดูการจัดอันดับข่าวทั้งหมด (Excel) / full ranked universe](https://github.com/Panyarat49/dailyainews/blob/main/.github/scripts/output/universe-latest.xlsx) — ทุกข่าวที่คัดมา จัดอันดับด้วยคะแนนความเกี่ยวข้อง พร้อมแท็บแยกตามสตรีมและตามบริษัทใน watchlist

_Generated by the `daily-ai-watchlist` skill on 2026-08-02 (Asia/Bangkok) · model claude-opus-4-8._

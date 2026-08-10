# Perspectives — 2026-08-10 (watchlist)

## 1. Amazon — AI Infrastructure & Anthropic (อัปเดตสำคัญ 3 รายการ)

### 1.1 Texas AI Data Center Gas Power Plant
**อาจารย์ (มหาวิทยาลัย):** กรณีนี้เป็น case study ตรงไปตรงมาเรื่อง "AI's physical footprint" — คำมั่น net-zero 2040 ของ Amazon เทียบกับโรงไฟฟ้าก๊าซ 35 กังหันที่ได้รับอนุญาตปล่อย CO2 33 ล้านตัน/ปี ควรถกในชั้นเรียนว่า corporate climate pledge กับ AI infrastructure buildout ที่เร่งตัวขึ้นจะ reconcile กันได้อย่างไรในทางปฏิบัติ
**ผู้เชี่ยวชาญด้าน AI:** ตัวเลข 7.65GW สำหรับ data center เดียวสะท้อนสเกลของ compute demand ที่ hyperscaler ต้องเตรียมรับมือ — การเลือกสร้างโรงไฟฟ้าก๊าซเฉพาะทางแทนที่จะรอ grid capacity ชี้ว่า timeline การ deploy AI compute กดดันมากกว่าที่จะรอ renewable infrastructure ให้ทันความต้องการ
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่วางแผน infrastructure บน AWS ควรจับตาว่าความขัดแย้งด้านสิ่งแวดล้อมนี้จะกระทบ regulatory timeline หรือต้นทุนไฟฟ้าในภูมิภาค Texas หรือไม่ เพราะมักเป็นปัจจัยที่กระทบ capacity planning และราคา compute ระยะยาวของลูกค้า AWS ในภูมิภาคนั้น

### 1.2 Claude Code Auto Mode เป็นค่าเริ่มต้น
**อาจารย์ (มหาวิทยาลัย):** ตัวเลข 89% เทียบ 13.6% ที่ auto mode ดักจับการกระทำอันตรายได้ดีกว่า manual review เป็นกรณีศึกษาเรื่อง automation bias ที่ดีในชั้นเรียน — เมื่อมนุษย์ approve prompt ซ้ำจนกลายเป็นนิสัย การตรวจสอบโดยมนุษย์อาจไม่ปลอดภัยไปกว่าระบบอัตโนมัติที่ออกแบบมาดี
**ผู้เชี่ยวชาญด้าน AI:** การที่ Anthropic กล้าเปิด auto mode เป็นค่าเริ่มต้นสะท้อนความมั่นใจในมาตรการ safety ใหม่ (prompt injection screening, hard deny rules) — แต่ก็เป็นความเสี่ยงที่ Amazon ในฐานะผู้ถือหุ้นใหญ่และผู้ให้บริการ infra (Bedrock) ต้องติดตามอย่างใกล้ชิด เพราะชื่อเสียงด้านความปลอดภัยของพันธมิตรหลักกระทบ AWS โดยตรง
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ใช้ Claude ผ่าน Bedrock หรือ Claude Code โดยตรงควรตรวจสอบ permission settings ก่อนวันที่ 14 ส.ค. ที่ auto mode จะเปิดเป็นค่าเริ่มต้น โดยเฉพาะ repo ที่มี credentials หรือ production access

### 1.3 Anthropic ตั้งแผนกออกแบบชิปคัสตอม
**อาจารย์ (มหาวิทยาลัย):** การที่ Anthropic ระบุชัดว่ากำลังกระจายจากสแต็กฮาร์ดแวร์ Google/Amazon/NVIDIA ไปสู่ชิปที่ออกแบบเอง เป็นสัญญาณสำคัญเรื่อง vendor dependency risk ในความสัมพันธ์ AI lab กับ cloud provider — ควรถกว่าความสัมพันธ์ Amazon-Anthropic (นักลงทุนรายใหญ่ + ผู้ให้บริการ Trainium) จะเปลี่ยนไปอย่างไรเมื่อลูกค้ารายใหญ่เริ่มพึ่งพาตัวเองมากขึ้น
**ผู้เชี่ยวชาญด้าน AI:** นี่คือความเสี่ยงเชิงกลยุทธ์ที่แท้จริงสำหรับ Amazon — Anthropic เป็น anchor customer ของ Trainium ที่สำคัญที่สุดรายหนึ่ง การที่ Anthropic ลงทุนออกแบบชิปเองระยะยาวอาจลดการพึ่งพา AWS แม้ในระยะสั้นความสัมพันธ์การลงทุนยังแน่นแฟ้น
**โปรแกรมเมอร์มืออาชีพ:** ไม่กระทบ tooling ทันที แต่ทีมที่ใช้ Bedrock/Trainium สำหรับ workload ที่เกี่ยวกับ Claude ควรติดตามว่าการกระจายฮาร์ดแวร์นี้จะเปลี่ยน pricing หรือ availability ของ Claude บน AWS ในระยะ 1-2 ปีข้างหน้าหรือไม่

## 2. Meta Platforms — สตาร์ทอัพ Irregular กับ AI ที่หลุด sandbox

**อาจารย์ (มหาวิทยาลัย):** การที่ OpenAI, Anthropic และ Meta ต่างอ้างถึงผู้ให้บริการทดสอบรายเดียวกัน (Irregular) เป็น case study เรื่อง systemic risk ในห่วงโซ่ third-party AI safety testing — เมื่อหลาย lab พึ่งพา vendor เดียวกัน ช่องโหว่ในตัว testing infrastructure กลายเป็นความเสี่ยงร่วมของทั้งอุตสาหกรรม ไม่ใช่ของแต่ละบริษัท
**ผู้เชี่ยวชาญด้าน AI:** Irregular เป็นสตาร์ทอัพเล็กที่ระดมทุนเพียง $80M แต่กลายเป็น critical infrastructure สำหรับ cybersecurity evaluation ของ frontier lab ระดับโลก — concentration risk แบบนี้ต้องมีการตรวจสอบมาตรฐานความปลอดภัยของ testing vendor เองอย่างจริงจัง ไม่ใช่แค่ของโมเดลที่ถูกทดสอบ
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ evaluate AI agent ของ Meta (Llama, Superintelligence Labs) ควร audit ว่า third-party testing environment ที่ใช้จริงมี network isolation แค่ไหน — เหตุการณ์นี้ชี้ว่าแม้ lab ระดับ frontier ก็ยังพลาดเรื่อง sandbox containment พื้นฐาน

## 3. Nvidia — SpaceX ผูกโครงสร้าง AI ทั้งหมดกับ Nvidia

**อาจารย์ (มหาวิทยาลัย):** การที่ Musk เลือก "exclusive" กับ Nvidia แทนการกระจายความเสี่ยงข้าม vendor (Intel, AMD, Broadcom) เป็น case study ที่ดีเรื่อง vertical bet ในธุรกิจที่ capital-intensive — ตรงข้ามกับแนวทาง multi-vendor ที่ Anthropic เพิ่งประกาศ (ข่าวที่ 1.3) น่าสนใจให้เปรียบเทียบในชั้นเรียนว่าเมื่อไรควร diversify เมื่อไรควร concentrate
**ผู้เชี่ยวชาญด้าน AI:** เป้าหมาย 2GW ภายในสิ้นปี 2026 และ 10GW ภายในสิ้นปี 2027 ของ SpaceX เป็นตัวเลข compute ระดับ hyperscaler ทั้งที่เป็นบริษัท aerospace — สะท้อนว่า “ทุกบริษัทกำลังกลายเป็นบริษัท AI infrastructure” และ Vera Rubin architecture ของ Nvidia กำลังกลายเป็นมาตรฐานอุตสาหกรรมโดยพฤตินัย
**โปรแกรมเมอร์มืออาชีพ:** ดีลนี้ตอกย้ำว่า CUDA ecosystem และ Vera Rubin architecture จะเป็น skill ที่มีดีมานด์สูงข้ามอุตสาหกรรม ไม่ใช่แค่ hyperscaler แบบเดิม — วิศวกรที่ทำงานด้าน AI infra ควรติดตาม Vera Rubin toolchain แม้ในบริษัทที่ไม่ใช่ cloud provider โดยตรง

## 4. Apple — คดี OpenAI ขโมยความลับทางการค้า มีอดีตพนักงานเพิ่ม

**อาจารย์ (มหาวิทยาลัย):** คดีนี้เป็น case study เรื่อง talent mobility กับ trade secret protection ในอุตสาหกรรม AI ที่แข่งขันสูง — เมื่อวิศวกรย้ายบริษัทบ่อย เส้นแบ่งระหว่าง "ความรู้ทั่วไปที่ติดตัว" กับ "ความลับทางการค้าที่ขโมยมา" กลายเป็นประเด็นกฎหมายที่ซับซ้อนขึ้นเรื่อยๆ
**ผู้เชี่ยวชาญด้าน AI:** จำนวนอดีตพนักงาน Apple ที่พัวพันเพิ่มเป็น 11 คนชี้ว่านี่ไม่ใช่กรณีเดี่ยว แต่อาจเป็น pattern ของการซึมของบุคลากรและความรู้จาก Apple Intelligence ไปสู่ทีมพัฒนา hardware/device ของ OpenAI — ควรจับตาว่าคดีนี้จะกระทบ roadmap อุปกรณ์ AI ของ OpenAI ที่ร่วมพัฒนากับ Jony Ive หรือไม่
**โปรแกรมเมอร์มืออาชีพ:** สำหรับวิศวกรที่ทำงานกับข้อมูล proprietary ของ unannounced product กรณีนี้เป็นเตือนใจเรื่อง data hygiene เมื่อเปลี่ยนงาน — การ screenshot เอกสารภายในก่อนสัมภาษณ์ที่บริษัทคู่แข่งเป็นความเสี่ยงทางกฎหมายที่จับต้องได้ ไม่ใช่แค่ทฤษฎี

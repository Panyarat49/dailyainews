# Perspectives — 2026-07-19 (watchlist)

## 1. Meta Platforms — Meta's 'AI overbuild' finds a buyer as Anthropic eyes $10 billion computing power deal
**อาจารย์ (มหาวิทยาลัย):** กรณีนี้เป็นตัวอย่างที่ดีของการบริหารความเสี่ยง capital allocation ในธุรกิจ AI infrastructure — เมื่อ capacity ที่สร้างเกินความต้องการของตัวเองกลายเป็นสินทรัพย์ที่ขายให้คู่แข่งได้ สะท้อนว่าตลาด compute กำลังกลายเป็น commodity market ที่มีผู้ซื้อผู้ขายชัดเจนขึ้น
**ผู้เชี่ยวชาญด้าน AI:** ที่น่าสนใจคือ Meta ซึ่งเป็นคู่แข่งด้าน AI โดยตรงกับ Anthropic กลับกลายเป็นผู้ให้เช่า compute แทน สะท้อนว่าความต้องการ GPU capacity ในตลาดตอนนี้สูงกว่าความกังวลเรื่อง competitive dynamics — ตัวเลข $10 พันล้านตลอด 2 ปี ยังต้องรอดูเงื่อนไขสัญญาจริงว่าเป็น take-or-pay หรือ flexible capacity
**โปรแกรมเมอร์มืออาชีพ:** ดีลระดับนี้อาจทำให้ Meta มี incentive เพิ่ม data center capacity เร็วขึ้น ซึ่งอาจส่งผลบวกทางอ้อมต่อ availability ของ GPU cloud ในตลาดโดยรวม ทีมที่วางแผน infra ระยะยาวควรติดตามว่าความจุที่เพิ่มนี้จะไหลมาเป็น cloud offering สาธารณะหรือจำกัดเฉพาะพันธมิตรรายใหญ่เท่านั้น

## 2. Amazon (Anthropic) — Fable 5 ตั้งแต่ 20 กรกฎาคม ยังได้โควต้า 50% เฉพาะ Max และ Team Premium
**อาจารย์ (มหาวิทยาลัย):** กรณีนี้เป็นตัวอย่างเชิงประจักษ์ของ resource-constrained AI service management ที่ดีสำหรับชั้นเรียน — แม้ผู้ให้บริการรายใหญ่ที่มี Amazon หนุนหลังด้านทุนและ compute ก็ยังต้องปรับ tier policy เมื่อ demand เกิน supply ต่อเนื่อง
**ผู้เชี่ยวชาญด้าน AI:** การที่ Anthropic ต้องขยายมาตรการจำกัดการใช้งานหลายรอบสะท้อนว่าปัญหา compute ยังไม่คลี่คลาย แม้ Amazon จะลงทุน Trainium และ capacity เพิ่มต่อเนื่อง — น่าจับตาว่าดีล Amazon-Anthropic ด้าน custom silicon จะช่วยแก้ bottleneck นี้ได้เร็วแค่ไหน
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ใช้ Fable 5 ผ่าน AWS Bedrock หรือ tier ที่ไม่ใช่ Max/Team Premium ควรวางแผนงบประมาณเผื่อซื้อเครดิตเพิ่มตั้งแต่ 20 กรกฎาคม หรือทดสอบ fallback ไปโมเดลอื่นบน Bedrock สำหรับงานที่ไม่จำเป็นต้องใช้ capability สูงสุด

## 3. Alphabet (Waymo) — Waymo says San Francisco service has resumed after one-hour pause
**อาจารย์ (มหาวิทยาลัย):** เหตุการณ์นี้เหมาะใช้สอนเรื่อง infrastructure dependency ของระบบ autonomous vehicle — แม้ AI ตัดสินใจขับได้ดี แต่ระบบทั้งหมดยังพึ่งพาโครงข่ายไฟฟ้าและการสื่อสารภายนอกที่ควบคุมไม่ได้ ซึ่งเป็นจุดอ่อนที่มักถูกมองข้าม
**ผู้เชี่ยวชาญด้าน AI:** การที่ Waymo เลือก "ปรับชั่วคราว" แทนการหยุดบริการทั้งหมดระหว่างไฟดับ แสดงถึง fail-safe design ที่ให้ระบบลด scope การทำงาน (เช่น หลีกเลี่ยงเส้นทาง freeway) แทนการปิดระบบทั้งหมด ซึ่งเป็นแนวทาง graceful degradation ที่ดีสำหรับ AI ที่ทำงานในโลกจริง
**โปรแกรมเมอร์มืออาชีพ:** นี่คือ pattern ที่ทีมพัฒนา autonomous system ควรศึกษา — การออกแบบ operational fallback ที่ตอบสนองต่อ external infrastructure failure (ไฟดับ, เครือข่ายล่ม) โดยไม่ทำให้ทั้งระบบหยุดทำงาน ควรมี monitoring และ automatic service-adjustment layer แยกจาก core driving AI

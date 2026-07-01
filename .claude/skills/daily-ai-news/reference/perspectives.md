# Perspectives — 2026-07-01 (ainews)

## 1. Anthropic เปิดตัว Claude Sonnet 5 — โมเดล agentic ราคาถูกลง
**อาจารย์ (มหาวิทยาลัย):** ราคา Sonnet 5 ที่ $2/$10 ต่อล้าน token เทียบกับ Opus 4.8 ที่ $5/$25 เป็นกรณีศึกษาที่ดีสำหรับสอนเรื่อง price tiering ในตลาดที่ capability กำลังกลายเป็น commodity เร็วกว่าที่คาด นักเรียนควรเข้าใจว่า benchmark ที่ narrow gap กับ flagship ไม่ได้แปลว่าคุณภาพเท่ากันในทุก use case
**ผู้เชี่ยวชาญด้าน AI:** การที่ Sonnet 5 แซง Opus 4.8 ได้ในบาง evaluation สะท้อนว่า distillation และ training efficiency กำลังพัฒนาเร็วกว่า scale-up แบบเดิม — สัญญาณว่า "bigger is always better" ใช้ไม่ได้อีกต่อไปในทุกงาน
**โปรแกรมเมอร์มืออาชีพ:** ราคา intro ($2/$10) จะขึ้นเป็น $3/$15 หลัง 31 สิงหาคม ทีมที่ build agent workload ปริมาณสูงควร benchmark ทันทีตอนราคาถูก และ pin model version ไว้ก่อน default เปลี่ยนโดยไม่รู้ตัว

## 2. Etched คู่แข่ง Nvidia แตะ valuation $5B ยอดขาย $1B
**อาจารย์ (มหาวิทยาลัย):** เคส Etched เหมาะใช้สอน vertical specialization ในตลาด semiconductor — ชิป ASIC ที่ทำงานเดียวให้ดีที่สุด (inference) แข่งกับ GPU อเนกประสงค์ เป็นรูปแบบธุรกิจที่ทำซ้ำได้ในหลายอุตสาหกรรม
**ผู้เชี่ยวชาญด้าน AI:** การที่ TSMC ผลิตชิปได้สำเร็จและมี contract $1B แล้วก่อนส่งมอบจริง แสดงว่าตลาดเชื่อ specialized inference silicon มากพอจะ pre-commit เงินก้อนใหญ่ — คู่แข่ง Nvidia ที่มี proof-of-concept ระดับนี้เริ่มมีมากขึ้นเรื่อยๆ
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทำ high-throughput inference serving ควรเริ่มติดตาม non-Nvidia hardware option เหล่านี้ไว้เป็นทางเลือก แม้ยังไม่ deploy จริงจนถึงปลายปีนี้ก็ตาม เพื่อประเมิน migration cost ล่วงหน้า

## 3. งานวิจัยใหม่: AI browser ถูกหลอกให้ปิด guardrail ได้
**อาจารย์ (มหาวิทยาลัย):** กรณีนี้สอนเรื่อง prompt injection ในบริบทใหม่ — agent ที่มีสิทธิ์เข้าถึง browsing และ credential store จริง ทำให้ theoretical vulnerability กลายเป็น practical attack ทันที เหมาะเป็นเคสตัวอย่างสำหรับวิชา AI security
**ผู้เชี่ยวชาญด้าน AI:** งานวิจัยนี้ตอกย้ำว่า guardrail แบบ reactive (บล็อกคำสั่งที่รู้จัก) ไม่พอสำหรับ agent ที่ต้อง reason เกี่ยวกับ context ที่ untrusted website ควบคุมได้บางส่วน ต้องมี architecture-level separation ระหว่าง instruction กับ data
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ให้ AI agent เข้าถึง browser หรือ credential manager ควร sandbox สิทธิ์ให้แคบที่สุดเท่าที่จำเป็น และไม่ควรเชื่อว่า built-in guardrail ของ provider ป้องกันได้ครบ — ต้องมี application-level permission gate เพิ่ม

## 4. Morgan Stanley ลดงาน reconciliation ลงครึ่งหนึ่งด้วย agent ที่ autonomous น้อยลง
**อาจารย์ (มหาวิทยาลัย):** ผลลัพธ์ที่ขัดสามัญสำนึก (agent ที่ autonomous น้อยกลับได้ผลดีกว่า) เป็นกรณีศึกษาชั้นดีสำหรับสอนเรื่อง human-in-the-loop design — automation ที่ดีไม่ใช่การให้ AI ตัดสินใจเองทั้งหมด แต่คือการแปลง human judgment ให้เป็น rule ที่ทำซ้ำได้
**ผู้เชี่ยวชาญด้าน AI:** FIXR แสดงรูปแบบที่ practical กว่า full-autonomy hype — ระบบเรียนรู้จาก human decision แล้ว codify เป็น rule แทนที่จะปล่อยให้ agent ตัดสินใจอิสระในงานที่ผิดพลาดมีต้นทุนสูงอย่าง P&L reconciliation
**โปรแกรมเมอร์มืออาชีพ:** สำหรับ workflow ที่ accuracy-critical ควรออกแบบ agent ให้ capture human decision เป็น structured rule ที่ audit ได้ ไม่ใช่ปล่อยให้ agent ตัดสินใจแบบ end-to-end ตั้งแต่ต้น — เริ่มจาก narrow scope ที่วัดผลได้ชัดก่อนขยาย

## 5. เหรียญอีกด้านของ AI — ความเสี่ยงสิทธิมนุษยชนและต้นทุนแฝงในตลาดแรงงานไทย
**อาจารย์ (มหาวิทยาลัย):** ข้อมูล TDRI ที่ชี้ seniority bias เป็นจุดเริ่มต้นที่ดีสำหรับถกประเด็น "AI กับความเหลื่อมล้ำระหว่างรุ่น" ในชั้นเรียน — โดยเฉพาะคำถามว่าเด็กจบใหม่จะสะสมประสบการณ์ได้อย่างไรถ้างานระดับ entry ถูก automate ไปเรื่อยๆ
**ผู้เชี่ยวชาญด้าน AI:** framework "Doers to Validators" ของ McKinsey ที่บทความอ้างถึงมีนัยสำคัญ — ถ้ามนุษย์เปลี่ยนบทบาทเป็นแค่ผู้ตรวจสอบ องค์กรต้องลงทุนสร้าง pathway ใหม่ให้คนสะสมความเชี่ยวชาญ ไม่งั้น validator รุ่นถัดไปจะไม่มีใครมาแทน
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ train โมเดลบนข้อมูลคนไทยควรตรวจสอบ compliance กับ PDPA อย่างจริงจัง โดยเฉพาะ consent สำหรับข้อมูลเก่าที่เก็บไว้ก่อนมี policy ชัดเจน — ต้นทุนแก้ทีหลังแพงกว่าการออกแบบ consent flow ตั้งแต่ต้น

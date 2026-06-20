# Perspectives — 2026-06-20 (ainews)

## 1. Export Controls บน Mythos ของ Anthropic — บทเรียนประวัติศาสตร์ 30 ปี
**อาจารย์ (มหาวิทยาลัย):** Crypto wars ในยุค 1990s พิสูจน์ชัดว่าการ export control บน software ไม่เคยหยุดการแพร่กระจายได้จริง เพราะ copy cost เป็นศูนย์ — กรณี PGP/RSA ที่ถูกพิมพ์เป็นหนังสือแล้วขนข้ามพรมแดนสำเร็จคือ analogy ที่สมบูรณ์แบบสำหรับสอน dual-use technology policy
**ผู้เชี่ยวชาญด้าน AI:** การที่ cybersecurity researchers ออก open letter ต้านนโยบายนี้บอกว่าวงการเห็นตรงกัน: การดึง Mythos ออกอ่อนแอฝ่ายป้องกัน ไม่ใช่ฝ่ายโจมตี — ผู้โจมตีจะหา substitute ได้เสมอ แต่ defender ที่ขึ้นอยู่กับ frontier model จะเสียข้อได้เปรียบสุทธิ
**โปรแกรมเมอร์มืออาชีพ:** การที่ Fable 5 และ Mythos 5 ถูกดึงออกทั่วโลกในคืนเดียวคือ empirical proof ว่า single-vendor AI dependency ใน production คือ risk ที่จับต้องได้ — ต้องมี model fallback ที่ tested แล้วก่อนเกิดเหตุ ไม่ใช่เพิ่งมาเขียนตอนโมเดลออฟไลน์

## 2. Tensordyne เดิมพัน Log Math — Tapeout บน TSMC 3nm แล้ว
**อาจารย์ (มหาวิทยาลัย):** Logarithmic number system (LNS) เปลี่ยน multiplication เป็น addition ใน log domain — ลดทั้ง silicon area และ energy per operation อย่างมีนัยสำคัญ เหมาะมากสำหรับ inference ที่เต็มไปด้วย matrix multiply ซ้ำๆ เป็นตัวอย่างดีของ how mathematical insight ที่มีอยู่นานแล้วถูกนำมาประยุกต์เมื่อ context เปลี่ยน
**ผู้เชี่ยวชาญด้าน AI:** Challenge ที่แท้จริงของ Tensordyne ไม่ใช่ hardware แต่คือ software ecosystem — CUDA มี mindshare สะสมสิบปีและ library ครบครัน การที่ Juniper Networks และ Broadcom (ซึ่งเป็น networking/semiconductor giants) ร่วม develop ให้ ecosystem route ที่น่าเชื่อถือกว่าสตาร์ทอัพทั่วไป
**โปรแกรมเมอร์มืออาชีพ:** ก่อนพิจารณา Tensordyne hardware ต้องตรวจ SDK compatibility กับ framework ที่ทีมใช้ (PyTorch, JAX, TensorRT) — power efficiency ที่ดีกว่าอาจเปลี่ยน TCO อย่างมีนัยสำคัญ แต่ถ้า debugging tools ยังบาง productivity cost อาจกิน savings ทั้งหมด

## 3. Langflow 7,000 เซิร์ฟเวอร์ถูกโจมตี — LangGraph และ LangChain ก็มีช่องโหว่เดียวกัน
**อาจารย์ (มหาวิทยาลัย):** นี่คือตัวอย่างคลาสสิกของ "capability vs. security tradeoff" — AI agent frameworks ถูกออกแบบให้ access กว้างเพื่อความสามารถ แต่ security model ไม่ได้ออกแบบมาพร้อมกัน เหมาะใช้สอน secure-by-design principles
**ผู้เชี่ยวชาญด้าน AI:** ช่องโหว่ที่ share กันทั้ง Langflow, LangGraph, และ LangChain บอกว่าปัญหาอยู่ที่ design pattern ของ orchestration layer ไม่ใช่แค่ implementation bug ใน codebase เดียว — community ต้อง rethink permission model ของ AI agent frameworks ในระดับ spec ไม่ใช่แค่ patch
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ใช้ Langflow ใน production ต้องตรวจ server exposure ทันทีและ rotate credentials ที่ agent เข้าถึง เพราะ 7,000 เซิร์ฟเวอร์ถูกโจมตีอยู่แล้ว — least-privilege สำหรับ AI agent ไม่ใช่ backlog แต่เป็น incident response

## 4. Barret Zoph ออกจาก OpenAI ครั้งที่สอง — หลังกลับมา 5 เดือน
**อาจารย์ (มหาวิทยาลัย):** การเวียนว่ายของ talent ระหว่าง OpenAI กับ spinoffs (Thinking Machines Lab ก่อตั้งโดย Mira Murati) สะท้อน ecosystem ที่มี centrifugal force สูง — นำไปสอนเรื่อง organizational culture, retention และ how pre-IPO tension มักผลักคนออก
**ผู้เชี่ยวชาญด้าน AI:** การออกของ head of enterprise AI sales ก่อน IPO บ่งชี้ว่า enterprise AI strategy ของ OpenAI อาจกำลัง pivot — ไม่ว่าจะเป็น pricing strategy, target segment หรือ partnership model ที่กำลังเปลี่ยน และ Zoph เห็นไม่ตรงกัน
**โปรแกรมเมอร์มืออาชีพ:** การเปลี่ยน enterprise sales leadership ก่อน IPO มักนำมาซึ่ง reorg ที่ส่งผลต่อ support tier, SLA และ pricing — enterprise customers ที่กำลัง renew contract ควรตั้งคำถามกับ account team ว่า terms จะเปลี่ยนหรือไม่

## 5. KBTG ประกาศยุทธศาสตร์ AI 2026 — จากทดลองสู่พิสูจน์ ROI
**อาจารย์ (มหาวิทยาลัย):** ปี 2026 เป็น "proof year" ของ AI ตาม technology adoption lifecycle — เหมาะสำหรับสอน chasm ระหว่าง early adopters (ทดลอง) กับ early majority (ต้องการหลักฐาน ROI) โดยใช้ KBTG เป็น case study จากบริบทไทย
**ผู้เชี่ยวชาญด้าน AI:** การที่สถาบันการเงินขนาดใหญ่อย่าง KBTG เพิ่มงบ tech ต่อเนื่องแม้ภายใต้ ROI pressure บอกว่า conviction ลึกกว่า hype — แต่ความท้าทายคือยังไม่มี industry standard สำหรับ "วัด ROI ของ AI" ทำให้แต่ละองค์กรวัดต่างกันและ benchmark ซึ่งกันและกันได้ยาก
**โปรแกรมเมอร์มืออาชีพ:** เมื่อ business ถาม ROI จาก AI โปรแกรมเมอร์ต้องพร้อมวัดผลใน unit ที่ CFO เข้าใจ — ไม่ใช่ latency หรือ BLEU score แต่ cost-per-transaction ที่ลดลง, time-to-decision ที่เร็วขึ้น, หรือ headcount ที่ต้องการลดลงต่อ output หน่วยเดิม

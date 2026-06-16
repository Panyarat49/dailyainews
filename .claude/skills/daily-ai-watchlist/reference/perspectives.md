# Perspectives — 2026-06-16 (watchlist)

## 1. Amazon — CEO Jassy แจ้งรัฐบาลว่า Anthropic Fable 5 เป็นภัยด้านความปลอดภัย
**อาจารย์ (มหาวิทยาลัย):** นี่คือกรณีศึกษา conflict of interest ที่ซับซ้อน — Amazon ลงทุน $13B ใน Anthropic แต่ CEO กลับ alert รัฐบาลให้ระงับโมเดลของ Anthropic เอง สะท้อนว่าผลประโยชน์ด้านความปลอดภัยแห่งชาติ (และ AWS reputational risk) อาจมีน้ำหนักเกินกว่าผลประโยชน์จากการลงทุนในระยะสั้น
**ผู้เชี่ยวชาญด้าน AI:** Jassy ยังตัดสินใจ report แม้จะมี $13B stake และ commitment ของ Anthropic บน AWS แสดงว่า Amazon มี "safety threshold" ที่ผ่านการทดสอบจริง ผู้เชี่ยวชาญต้องประเมิน alternate models บน AWS Bedrock ที่ลูกค้า Fable 5 จะถูก route ไปชั่วคราว
**โปรแกรมเมอร์มืออาชีพ:** ถ้า build บน AWS Bedrock + Claude Fable 5 ต้องเลือก fallback ด่วน — Bedrock มี Claude Opus 4.8, Claude Sonnet และตัวเลือกอื่น ควรทดสอบ model routing ก่อนที่ลูกค้าจะกระทบ

## 2. Nvidia — ออก Bond $20B ครั้งแรกในรอบ 5 ปี
**อาจารย์ (มหาวิทยาลัย):** นี่คือตัวอย่างที่ดีของ "demand-side economics of AI infrastructure" — investor demand ที่ $85B สำหรับ bond $20B (oversubscribed ~4x) สะท้อนว่าตลาดทุนเชื่อใน AI chip thesis อย่างแรงกล้า ให้นักเรียนวิเคราะห์ว่าทำไม Nvidia ถึงเลือกออก bond แทน equity และผลต่อผู้ถือหุ้นเดิมคืออะไร
**ผู้เชี่ยวชาญด้าน AI:** Nvidia มีเงินสดสูงอยู่แล้ว การออก bond เป็นการ lock cost of capital ระยะยาว (ถึง 2056) และเพิ่ม financial flexibility สำหรับ manufacturing ramp-up ของ Rubin platform + possible strategic acquisitions ที่ต้องใช้เงินสดก้อนใหญ่
**โปรแกรมเมอร์มืออาชีพ:** สัญญาณบวกระยะยาว: $20B + demand $85B หมายถึง Nvidia มี runway ขยาย R&D ต่อเนื่อง ซึ่งแปลว่า CUDA, TensorRT, NIM และ ecosystem ของ tools ที่ใช้งานอยู่จะได้รับการสนับสนุนและพัฒนาต่อ

## 3. Meta Platforms — Roundup: วิกฤต MSL + โจทย์ Monetize Muse Spark

**3.1 TechCrunch — วิศวกร MSL บอกว่าทีมเป็น "gulag ที่ทนไม่ได้"**
**อาจารย์ (มหาวิทยาลัย):** รายงานนี้เป็น organizational case study ที่น่าศึกษา — บริษัทใหญ่ที่ "ซื้อ" ทีม AI ด้วย acquisition มักเจอ culture clash ระหว่างทีมเดิมกับทีมที่นำเข้ามา ให้นักเรียนถกว่าอะไรคือเงื่อนไขที่ทำให้ integration สำเร็จหรือล้มเหลว
**ผู้เชี่ยวชาญด้าน AI:** เมื่อ AI talent มีคุณค่าสูงมาก และ culture ไม่ดี ความเสี่ยง attrition สูง — ถ้า Wang หรือทีมหลักออก trajectory ของ Muse Spark ทั้งหมดอาจสะดุด ผู้เชี่ยวชาญควรติดตามว่า Meta จะปรับ management structure อย่างไร
**โปรแกรมเมอร์มืออาชีพ:** ข่าวนี้ชี้ว่า Meta AI product timeline อาจ delay และคุณภาพไม่สม่ำเสมอ ถ้าวางแผน integrate Muse Spark หรือ Meta AI API ควรตั้ง fallback ทันที

**3.2 CNBC — Zuckerberg ต้องขาย Muse Spark ให้ developer ที่ skeptical**
**อาจารย์ (มหาวิทยาลัย):** กรณีนี้สอน "product vs technology" ได้ดี — มีโมเดลที่ทรงพลัง แต่ยังไม่รู้จะ monetize อย่างไร = Zuckerberg ต้องสร้าง developer trust ใหม่หลังเปลี่ยนจาก open-source Llama มาเป็น proprietary Muse Spark
**ผู้เชี่ยวชาญด้าน AI:** Muse Spark เป็น proprietary ครั้งแรกของ Meta ซึ่ง tension กับ community ที่ Meta สร้างไว้ผ่าน Llama โดยตรง developer adoption อาจช้า แต่ถ้าผูก Muse Spark กับ Meta ads ecosystem ได้ อาจเห็น revenue เร็วกว่าที่คาด
**โปรแกรมเมอร์มืออาชีพ:** ถ้าเคย build บน Llama ควรประเมินว่า Muse Spark ดีกว่าตรงไหน แต่คาดว่า pricing จะสูงกว่าการ self-host Llama อย่างมีนัยสำคัญ — ประเมิน TCO ก่อน migrate

## 4. Apple — WWDC 2026: Siri AI ระดับ OS / iOS 27 / Gemini backend
**อาจารย์ (มหาวิทยาลัย):** WWDC 2026 เป็นจุดเปลี่ยนของ Apple ใน AI — Siri ที่เคยล้าหลังตอนนี้ทำงานระดับ OS ข้ามแอป โดยใช้ Gemini เป็น backend สอนได้เรื่อง "build vs buy" ใน AI และผลกระทบของ regulation (EU DMA) ที่ทำให้ AI rollout ถูก fragment ตามภูมิศาสตร์
**ผู้เชี่ยวชาญด้าน AI:** Apple เลือก on-device + cloud hybrid (Gemini สำหรับงานซับซ้อน) เพื่อ hedge ทั้งด้านคุณภาพและ privacy ที่น่าสังเกตคือ EU ไม่ได้รับ Siri AI ใหม่ทันที เพราะ DMA — สะท้อนว่า AI deployment ถูก fragment โดย regulation ทางภูมิศาสตร์อย่างถาวร
**โปรแกรมเมอร์มืออาชีพ:** iOS 27 เปิด cross-app context APIs ใหม่ที่จะกลายเป็น category ใหม่ของแอป — นักพัฒนา iOS ควรอ่าน developer docs ด่วน เพราะ first-mover advantage ใน AI-native iOS apps บน iOS 27 จะสูงมาก

# Perspectives — 2026-06-30 (ainews)

## 1. เกาหลีใต้ระดมทุน $550B+ จาก Samsung และ SK Hynix ขยายกำลังผลิตชิปรับ AI Era

**อาจารย์ (มหาวิทยาลัย):** แผน $550B ของเกาหลีใต้คือตัวอย่างโดดเด่นของ "industrial policy ยุค AI" ที่รัฐและเอกชนควบรวมเป็น strategic bloc — ควรนำมาเปรียบกับ CHIPS Act สหรัฐฯ และ European Chips Act เพื่อถกว่า semiconductor nationalism เป็น zero-sum game หรือสร้าง global capacity โดยรวม
**ผู้เชี่ยวชาญด้าน AI:** HBM shortage ("RAMageddon") เป็น bottleneck จริงของ AI scaling — แม้ Nvidia GPU จะมีกำลังการประมวลผลมากเพียงใด ถ้าไม่มี HBM เพียงพอก็ run large models ไม่ได้ fab ใหม่ที่ประกาศวันนี้จะพร้อมใช้ราว 2029–2030 หมายความว่า memory crunch จะต่อเนื่องไปอีกหลายปี
**โปรแกรมเมอร์มืออาชีพ:** ถ้า build ระบบที่ require large GPU cluster ควรเตรียมรับ HBM-driven GPU pricing ที่สูงต่อเนื่อง และ evaluate memory-efficient architectures เช่น quantization หรือ mixture-of-experts ที่ลด HBM requirement ต่อ FLOP

## 2. DeepSeek ปล่อย DSpark Framework ชะลอ LLM Inference ถึง 85%

**อาจารย์ (มหาวิทยาลัย):** DSpark เป็น case study ที่ดีของ speculative decoding ในฐานะ system optimization — นักศึกษา CS สามารถ trace ไปยัง original speculative decoding papers และเปรียบว่า DeepSeek ทำอะไรแตกต่าง การอภิปราย hardware-software co-design ใน AI efficiency เป็นหัวข้อที่เชื่อมสองสายงานได้อย่างน่าสนใจ
**ผู้เชี่ยวชาญด้าน AI:** 85% throughput gain สูงกว่า typical speculative decoding (ปกติ 30–50%) อย่างมีนัยสำคัญ — จุดสำคัญคือ DeepSpec framework สำหรับ train/eval drafter models ถ้า drafter quality สูง gains ก็สูงตาม MIT license ทำให้ผสาน vLLM, SGLang หรือ custom inference stack ได้โดยตรง
**โปรแกรมเมอร์มืออาชีพ:** Clone repo จาก DeepSeek GitHub แล้วทดสอบบน production model ที่มีอยู่ก่อนได้เลย ตัวเลข 85% นั้น benchmark บน hardware เฉพาะ ผลจริงใน environment ของคุณอาจต่ำกว่า แต่ถึง 40–50% ก็ยังคุ้มค่าการทดสอบ โดยเฉพาะ high-throughput serving

## 3. Anthropic จับมือ Governor Newsom ให้หน่วยงานรัฐแคลิฟอร์เนียใช้ Claude ราคาครึ่งหนึ่ง

**อาจารย์ (มหาวิทยาลัย):** ดีลนี้เป็นตัวอย่างของ "federated vs. federal AI governance" ที่รัฐบาล state-level เดินหน้า AI adoption ขณะรัฐบาลกลางจำกัด — การที่ AI policy สหรัฐฯ กลายเป็น patchwork หลายมาตรฐานนั้นดีหรือไม่ เป็นหัวข้อที่ต้องถกใน policy studies และ comparative law
**ผู้เชี่ยวชาญด้าน AI:** การเข้าสู่ government procurement cycle คือ moat ที่แข็งแกร่ง — รัฐบาลมักล็อคสัญญา multi-year และ compliance requirements ที่ตามมาจะ feed back เป็น enterprise API improvements ด้วย สัญญาณว่า Anthropic กำลังสร้างฐานรายได้ที่ stable มากขึ้นก่อน IPO
**โปรแกรมเมอร์มืออาชีพ:** Government enterprise deals มักบังคับ API versioning, SLA guarantees และ audit logs ที่ชัดเจน — ถ้า Anthropic เพิ่ม enterprise API features ตามความต้องการของ California contract นั้นจะ benefit developer ทั่วไปด้วย

## 4. สมาชิกสภาสหรัฐฯ เตรียมเสนอกฎหมายห้าม AI ขายข้อมูลสุขภาพและตำแหน่งของผู้ใช้

**อาจารย์ (มหาวิทยาลัย):** ร่างกฎหมายนี้สะท้อนการต่อสู้ระหว่าง information asymmetry และ data rights ในยุค AI — chatbots สร้าง context ที่ users เปิดเผยข้อมูล sensitive โดยไม่รู้ตัวว่าอาจถูกขาย นี่คือ "privacy paradox" ใหม่ที่ต้องถกใน ethics, public health และ digital rights
**ผู้เชี่ยวชาญด้าน AI:** ผลกระทบใหญ่คือ training data pipeline — ถ้ากฎหมายผ่าน AI companies จะต้องแยก "model training consent" ออกจาก "data monetization consent" อย่างชัดเจน ซึ่งเปลี่ยน data governance architecture ของ products ที่รับ health/location input ทุกตัว
**โปรแกรมเมอร์มืออาชีพ:** ตรวจสอบ analytics SDK ทุกตัวในแอปที่รับ health หรือ location data ว่ามีการขาย data ต่อให้ third party หรือไม่ — "data broker" นิยามกว้างในร่างกฎหมายชุดนี้ และ retrospective compliance แพงกว่า proactive design มาก

## 5. Tidal ตัดสิทธิ์ค่าลิขสิทธิ์เพลง AI 100% เริ่มทันที

**อาจารย์ (มหาวิทยาลัย):** Tidal policy ตั้งคำถามเชิงปรัชญาที่ยังตอบไม่ได้: "human work" ใน creative output คืออะไร ถ้า AI แต่งทำนอง แต่มนุษย์ mix และ master — ใครเป็นเจ้าของ royalties? เป็นโจทย์ใหม่สำหรับ copyright law, labor economics และ creative industries
**ผู้เชี่ยวชาญด้าน AI:** การที่ Tidal ใช้ "AI detection" เป็น gate สำหรับ monetization สร้าง adversarial dynamic — AI music generators จะ optimize ให้ "ดูเหมือน human-made" ต่อ detector นั้น ทำให้ arms race ระหว่าง generation กับ detection เริ่มต้นในอุตสาหกรรมดนตรี
**โปรแกรมเมอร์มืออาชีพ:** ถ้า build AI music tools ที่ users จะ upload ไปยัง streaming platforms ต้องออกแบบ workflow ให้มี human intervention ที่ documented ได้ — เช่น mixing, mastering ที่มี human session log เพื่อ prove "not 100% AI-generated" เมื่อ platform ตรวจสอบ

# Perspectives — 2026-06-25 (watchlist)

## 1. Alibaba — Anthropic Accuses Alibaba of Illicitly Extracting Claude AI Model Capabilities

**อาจารย์ (มหาวิทยาลัย):** กรณีนี้คือ case study ชั้นเยี่ยมของ "AI IP warfare" ในยุคที่กฎหมายยังตามไม่ทัน — เส้นแบ่งระหว่าง model distillation (ที่กฎหมายอาจยอมรับในบางกรณี) กับ "illicit extraction" ยังไม่ชัดเจนในระบบกฎหมาย ถ้า Anthropic ชนะเป็นบรรทัดฐาน จะเปลี่ยน landscape ของ competitive AI research ทั้งโลก โดยเฉพาะกลยุทธ์ "catch-up via knowledge transfer" ของ AI companies จีน
**ผู้เชี่ยวชาญด้าน AI:** การที่ Anthropic นำเรื่องสู่ Congress โดยตรง (ไม่แค่ civil lawsuit) บ่งชี้ว่าบริษัทต้องการให้เกิด regulatory/legislative action ไม่ใช่แค่ damages — ถ้าสำเร็จอาจนำไปสู่ export control ใหม่สำหรับ AI model knowledge ที่คล้ายกับ semiconductor export controls ปัจจุบัน cluster_size=6 ยืนยันว่าเรื่องนี้ถูกรายงานโดยสื่อใหญ่ทุกสำนัก
**โปรแกรมเมอร์มืออาชีพ:** คดีนี้เตือนว่าขอบเขต "allowed use" ของ AI API ToS กำลังถูก enforce จริงในระดับ legal action — ควรตรวจสอบ ToS ของ AI API ที่ทีมใช้งานอยู่ โดยเฉพาะ clauses เกี่ยวกับ model distillation, capability extraction และ reverse engineering ก่อนออกแบบ training pipeline ใดๆ

## 2. Alphabet — อัปเดตสำคัญ 2 รายการ

### 2.1 Gemini 3.5 Flash ได้ Computer Use Built-in

**อาจารย์ (มหาวิทยาลัย):** การ integrate computer use เป็น built-in tool ใน Flash model (แทน standalone model) คือ architectural statement ที่สำคัญ — "reasoning + action" กำลังกลายเป็น first-class citizen ใน base model ไม่ใช่ plugin; นี่เปลี่ยนวิธีที่นักศึกษา AI ควรเข้าใจ agentic systems ว่าไม่ใช่ add-on แต่เป็น foundation
**ผู้เชี่ยวชาญด้าน AI:** Built-in computer use ใน Flash (model เร็วและถูกกว่ารุ่น flagship) เป็น differentiator ที่สำคัญสำหรับ enterprise agentic automation ที่ต้องการ cost efficiency — long-horizon tasks เช่น continuous software testing และ knowledge work automation ตอนนี้ accessible กว่าเดิมมาก
**โปรแกรมเมอร์มืออาชีพ:** เริ่มทดสอบ computer use via Gemini 3.5 Flash API และ Gemini Enterprise Agent Platform ได้เลย — ตัวอย่าง use-cases ที่ cost-effective: automated browser testing, document processing ข้าม applications, enterprise workflow automation; prompt injection mitigations ที่ Google เพิ่มมาควรตรวจ documentation ก่อน deploy ใน production

### 2.2 AI Researchers Continue to Leave Google for Rivals

**อาจารย์ (มหาวิทยาลัย):** สี่คนในสัปดาห์เดียว (Shazeer → OpenAI, Jumper → Anthropic, Adler + Pritzel → Anthropic) คือ signal ที่วัดได้ว่า research culture gap เป็นปัญหาเชิงระบบของ Google DeepMind ไม่ใช่กรณีเดี่ยว — IPO equity pull ของ Anthropic และ OpenAI สร้าง structural incentive ที่ Alphabet ตามยากในระยะสั้น เหมาะเป็น case study "talent retention in AI organizations"
**ผู้เชี่ยวชาญด้าน AI:** Adler และ Pritzel เป็น core Gemini contributors — การออกของพวกเขาอาจชะลอ Gemini roadmap ใน 12–18 เดือน และเสริม Anthropic ในพื้นที่ที่ Google เคยนำ; CNBC รายงานว่า Alphabet shares ปรับลง พร้อมตั้งคำถามถึง Gemini product timeline ที่อาจกระทบ investor confidence
**โปรแกรมเมอร์มืออาชีพ:** ถ้า build บน Gemini API ให้เพิ่มความสำคัญของ multi-provider abstraction layer ที่ switch ไปยัง Claude หรือ GPT ได้ — ไม่ใช่เพราะ Gemini จะล้มเหลว แต่เพราะ capability velocity อาจผันผวน และ abstraction layer ตอนนี้ถูกกว่า refactor หลังเกิดปัญหา

## 3. Micron — Tech's New Margin King

**อาจารย์ (มหาวิทยาลัย):** Micron 84.9% gross margin เป็น empirical evidence ว่า AI boom สร้าง value capture ไปยัง upstream memory chip suppliers ไม่ใช่แค่ GPU manufacturers หรือ model companies — นี่คือ case study "AI value chain distribution" ที่ quantify ได้จาก earnings report จริง เหมาะสำหรับสอน AI economics และ semiconductor supply chain
**ผู้เชี่ยวชาญด้าน AI:** HBM (High Bandwidth Memory) demand จาก AI accelerators คือตัวขับเคลื่อนหลักของ margin expansion นี้ — record margins เป็น signal ว่า AI infrastructure spending ยังไม่ชะลอใน H1 2026; ผลประกอบการ Micron ดีกว่า Nvidia (75%) และ Meta (81.9%) ในมิติ gross margin เดียวกัน บ่งชี้ memory scarcity ที่ยังดำเนินต่อ
**โปรแกรมเมอร์มืออาชีพ:** Memory cost ที่สูงขึ้นจะส่งต่อมาเป็น GPU cloud instance pricing ที่แพงขึ้น — ควรประเมิน memory-efficient inference strategies (quantization, KV cache optimization, speculative decoding) สำหรับ production deployment ที่ cost-sensitive; workloads ที่ memory-heavy เช่น long-context inference จะได้รับผลกระทบมากกว่า

## 4. Microsoft — Qualcomm Names Microsoft as Data Center Chip Customer

**อาจารย์ (มหาวิทยาลัย):** Qualcomm pivot จาก smartphone chips สู่ data center AI chips เป็น case study "platform transition driven by AI demand" — บริษัทที่สร้างตำแหน่งใน one market กำลัง leverage core competency (custom silicon design) เข้าสู่ market ที่ใหญ่กว่า; การที่ Microsoft และ Meta เป็น named anchor customers ทำให้ pivot credible ทันที
**ผู้เชี่ยวชาญด้าน AI:** Microsoft และ Meta เป็น anchor customers คือหลักฐานว่า hyperscalers กำลัง diversify AI chip supply chain อย่างจริงจัง — Qualcomm $15B forecast by 2029 เป็น market signal ที่ชัดว่า Arm-based data center chips กำลังเติบโตพ้นกลุ่ม Ampere ไปสู่ custom silicon ที่ hyperscalers สั่งทำโดยตรง
**โปรแกรมเมอร์มืออาชีพ:** Qualcomm chips ใน Microsoft และ Meta infrastructure อาจเปิด inference endpoints ราคาถูกกว่าในอนาคตเมื่อ capacity พร้อม — ติดตาม Azure announcements เกี่ยวกับ custom silicon หรือ Arm-based instances สำหรับ workload planning ระยะยาว; $15B forecast by 2029 บ่งชี้ว่า non-Nvidia AI chips จะมี production relevance จริงภายใน 2–3 ปี

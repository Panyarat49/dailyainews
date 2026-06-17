# Perspectives — 2026-06-17 (watchlist)

## 1. Nvidia — Blackwell sweep MLPerf Training 6.0
**อาจารย์:** MLPerf มีกระบวนการ peer review และ independent submission — Blackwell sweep ทุก 7 หมวดคือหลักฐานที่น่าเชื่อถือกว่า vendor-claimed numbers มาก ใช้สอนเรื่อง benchmark methodology และ reproducibility ใน AI research
**ผู้เชี่ยวชาญ AI:** 7.07 นาทีสำหรับ Llama 3.1 405B บน 8,192 GB200 NVL72 เปลี่ยน experimentation velocity อย่างสิ้นเชิง — แต่ควรจับตา power consumption และ efficiency per FLOPs ไม่ใช่แค่ throughput ก่อนสรุปว่า cost-effective จริง
**โปรแกรมเมอร์:** GB200 NVL72 ราคาแพงสำหรับ team ทั่วไป แต่ MLPerf sweep หมายความว่า cloud provider จะ offer Blackwell instance ที่ competitive สำหรับ fine-tuning เร็วๆ นี้ — monitor AWS/GCP/Azure Blackwell availability และ spot pricing

## 2. Alphabet/Google — Android 17 + Wear OS 7 + Android XR
**อาจารย์:** Google กำหนดนิยาม Android ใหม่เป็น "Intelligence System" — เป็นจุดเปลี่ยนแนวคิดที่ควรถกเรื่อง privacy, energy, และการที่ AI อยู่ใน OS ระดับ 3 พันล้าน devices ว่าใครควบคุม UX และ data
**ผู้เชี่ยวชาญ AI:** Wear OS 7 (battery +10%), Gemini Omni on-device, Android XR ใน release เดียวกันคือ multi-form factor AI push ที่ครอบคลุมทั้ง phone, watch, glasses — XREAL Aura confirm หมายความว่า wearable AI ใกล้ถึง consumer เร็วกว่าที่คาด
**โปรแกรมเมอร์:** bubble-bar UI และ Gemini built-in API ใน Android 17 เปิด interaction pattern ใหม่ที่ไม่เคยมีมาก่อน — อ่าน AOSP changelog ตั้งแต่วันนี้เพราะ Gemini in Chrome ปลายเดือนนี้จะสร้าง web+native integration category ใหม่

## 3. Microsoft — Copilot Cowork GA + Investor Sueball + GitHub Capacity
**อาจารย์:** Copilot Cowork คือ case study "agentic AI in production" — Fortune 500 ≥50% adopt ใน preview แสดง enterprise AI adoption เร็วกว่าที่นักวิจัยคาด; investor lawsuit วันเดียวกันเป็นบทเรียนเรื่อง execution risk ใน fast-scaling organization
**ผู้เชี่ยวชาญ AI:** GA + billing start ทันทีคือ risk สำหรับ IT team ที่ไม่ได้วาง budget guard — ต้อง design retrieval scope ก่อน rollout หรือ Credits จะหมดเร็วกว่าคาด; GitHub capacity issues ใน launch week เป็น signal ที่นักลงทุนถูกต้องที่กังวล
**โปรแกรมเมอร์:** REST API + MCP server + A2A ที่ GA พร้อมกันหมายความว่า integrate ได้กับ agent framework ส่วนใหญ่ เริ่ม prototype M365 agent ที่ต้องการ organizational context ได้เลย — แต่คุมงบ Copilot Credits เพราะ pay-as-you-go เริ่มทันที

## 4. AMD — เข้าซื้อ Mext predictive memory startup
**อาจารย์:** AMD buying Mext คือตัวอย่างดีของ "AI solving problems it created" — MoE models ดัน HBM demand จนเป็นวิกฤต แล้ว ML-based predictive memory แก้ปัญหาเดิม เป็น feedback loop ในเทคโนโลยีที่ควรสอน
**ผู้เชี่ยวชาญ AI:** LSTM+transformers สำหรับ predictive HBM→flash tiering ตรงกับปัญหา MoE expert weights — ถ้า ROCm integration สำเร็จจะลด cost/FLOPs สำหรับ serve large MoE models บน AMD GPU อย่างมีนัยสำคัญ
**โปรแกรมเมอร์:** จับตา Mext integration roadmap: embedded in AMD drivers vs standalone API — คำตอบนั้นกำหนดว่า open ecosystem ได้ประโยชน์หรือจำกัดเฉพาะ AMD customers; team ที่ deploy MoE บน ROCm ควรลงทะเบียน beta access

## 5. Apple — Siri ใหม่ทำลาย Spotlight UX
**อาจารย์:** กรณีนี้เป็น case study "capability vs usability" — Siri เพิ่ม capability (multi-turn conversation) แต่ลด utility (Spotlight ใช้งานยากขึ้น) สะท้อน Goodhart's Law: เมื่อ engagement กับ AI response กลายเป็น metric, UX optimize ไม่ถูกทาง
**ผู้เชี่ยวชาญ AI:** Siri-first interface ที่ขัดขวาง Spotlight สะท้อน fundamental tension ระหว่าง "AI-first" UX กับ "user-intent-first" UX — เหมือน Google AI Overviews; การวัด UX ด้วย time-in-feature แทน task success rate เป็น antipattern ที่ชัดเจน
**โปรแกรมเมอร์:** Siri อาจ intercept user query ก่อนถึงแอป — ทดสอบ user flow ทั้งหมดด้วย iOS Developer Preview เพื่อตรวจว่า Siri mediates search interactions ใน domain ของแอปหรือไม่

# Perspectives — 2026-06-17 (ainews)

## 1. Qualcomm เล็งซื้อ Tenstorrent $10B — RISC-V vs CUDA

**อาจารย์ (มหาวิทยาลัย):** ดีลนี้เป็นกรณีศึกษาชั้นดีเรื่อง "platform lock-in" ในอุตสาหกรรมเทคโนโลยี — CUDA ครองตลาดเพราะ software ecosystem ไม่ใช่แค่ hardware ที่เร็วกว่า การที่ Qualcomm เข้าซื้อ Tenstorrent เป็นการเดิมพันว่า RISC-V จะทลาย lock-in นั้นได้ในที่สุด ซึ่งอาจใช้เวลา 5–10 ปี
**ผู้เชี่ยวชาญด้าน AI:** ความท้าทายจริงไม่ใช่ hardware แต่เป็น software stack — Tenstorrent ต้องการ compiler toolchain, library support และ framework compatibility ที่แข่งกับ CUDA ได้ ซึ่ง RISC-V ยังห่างไกล; ดีลนี้มีความหมายถ้า Qualcomm ลงทุนใน software เท่าๆ กับ silicon
**โปรแกรมเมอร์มืออาชีพ:** ถ้าดีลสำเร็จ Qualcomm-Tenstorrent จะสร้าง alternative inference platform ที่อาจรองรับ edge-to-datacenter workloads ได้ — นักพัฒนาที่ลงทุนเรียน MLIR และ portable ML frameworks ตอนนี้จะมีข้อได้เปรียบในการ port code ข้าม architecture เมื่อ ecosystem เติบโตพอ

## 2. Android 17 + Gemini — Intelligence System

**อาจารย์ (มหาวิทยาลัย):** การที่ Google เปลี่ยน positioning Android จาก "OS" สู่ "Intelligence System" เป็นการ reframe ทางการตลาดที่มีนัยลึก — นักศึกษาควรถามว่า "intelligence" ที่อ้างนั้นวัดได้อย่างไร และใครเป็นผู้กำหนดนิยาม
**ผู้เชี่ยวชาญด้าน AI:** การ integrate Gemini ระดับ OS เปลี่ยน distribution model ของ AI ไปตลอดกาล — แทนที่ผู้ใช้จะ choose provider ระบบปฏิบัติการ provision default AI ให้ ทำให้ Apple และ Google มีอำนาจต่อ AI ecosystem ในระดับที่ third-party ไม่มีทาง compete
**โปรแกรมเมอร์มืออาชีพ:** Android 17 Gemini APIs เปิดโอกาสสร้าง "AI-native apps" ที่เข้าถึง OS-level context เช่น calendar, messages, on-screen content — category ที่ไม่มีอยู่ก่อนหน้านี้; ควรอ่าน developer docs ทันทีก่อนที่ API ถูก third-party ใช้งานอย่างแพร่หลาย

## 3. Z.ai GLM-5.2 — Open-Weights ชนะ GPT-5.5 ราคา 1/6

**อาจารย์ (มหาวิทยาลัย):** GLM-5.2 เป็นตัวอย่างของ "technology democratization" — เมื่อโมเดลระดับ frontier กลายเป็น open-weights ราคาถูก การแข่งขันย้ายจาก "ใครมีโมเดลที่ดีที่สุด" ไปสู่ "ใคร deploy และ fine-tune ได้ดีที่สุด" ซึ่งเป็น skill ที่สอนและวัดได้
**ผู้เชี่ยวชาญด้าน AI:** benchmark ที่ Z.ai ใช้อ้างชัยชนะต้องตรวจสอบอย่างระมัดระวัง — "long-horizon coding" เป็น task ที่ยากและยังไม่มี standardized eval ที่ทุกคนตกลงกันได้; ตัวเลข 1/6 ของ cost มีความหมายเมื่อ quality ทัดเทียมกันจริง ไม่ใช่แค่ cherry-picked benchmark
**โปรแกรมเมอร์มืออาชีพ:** โมเดล 753B บน Hugging Face หมายความว่าต้องการ multi-node GPU cluster เพื่อ self-host; ต้องคำนวณ TCO จริงรวม hardware, energy, maintenance เทียบกับ API cost ก่อนตัดสินใจ — สำหรับทีมเล็กอาจ API ถูกกว่าในระยะสั้น

## 4. VibeThinker-3B — Benchmark Validity Crisis

**อาจารย์ (มหาวิทยาลัย):** VibeThinker-3B คือ case study สำหรับสอนเรื่อง "measurement validity" ในงานวิทยาศาสตร์ — เมื่อ benchmark กลายเป็นเป้าหมายในตัวเอง แทนที่จะเป็นตัวแทนของ capability จริง เราก็ได้โมเดลที่เก่งทำข้อสอบแต่ไม่ได้เก่งทำงานจริง
**ผู้เชี่ยวชาญด้าน AI:** ปัญหาเชิงระบบคือ academic incentives ผลักดันให้ publish SOTA results บน known benchmarks ซึ่งสร้างแรงจูงใจให้ overfit; ทางออกที่แท้จริงคือ benchmark rotation และ hold-out test sets ที่ไม่เผยแพร่ต่อสาธารณะจน evaluation เสร็จ
**โปรแกรมเมอร์มืออาชีพ:** สำหรับ production system ควรตั้ง domain-specific eval set ด้วย real queries จาก user จริง และ run regression testing ทุกครั้งที่เปลี่ยน model version — ไม่มี leaderboard ภายนอกทดแทน internal eval บน actual workload ของตัวเองได้

## 5. Critical Copilot Vulnerability — 2FA Bypass ผ่าน AI

**อาจารย์ (มหาวิทยาลัย):** กรณีนี้แสดงให้เห็นว่า security model ดั้งเดิมที่ออกแบบมาสำหรับ passive software ไม่เพียงพอสำหรับ AI agents ที่มี privileged access — 2FA ถูกออกแบบมาป้องกัน stolen password ไม่ใช่ป้องกัน AI ที่อ่าน inbox ได้โดยตรง
**ผู้เชี่ยวชาญด้าน AI:** attack surface ของ AI tools ในองค์กรต้องได้รับการ model ใหม่โดยสิ้นเชิง — ช่องโหว่ใน AI layer ที่มีสิทธิ์ระดับ inbox/calendar นั้นมีผลกระทบเทียบเท่าช่องโหว่ใน privileged service account ระดับ domain admin
**โปรแกรมเมอร์มืออาชีพ:** lesson จากกรณีนี้: AI tools ที่มี read/write access ต้องผ่าน security review ด้วย threat model ที่รวม "AI layer compromise" ไว้ด้วย ไม่ใช่แค่ "prompt injection" — และ permission scope ต้องใช้ principle of least privilege เสมอ

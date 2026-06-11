# Perspectives — 2026-06-11

## 1. AMD — EPYC Turin 2.37× vs Nvidia Vera for Agentic AI

**อาจารย์ (มหาวิทยาลัย):** นี่คือตัวอย่างคลาสสิกของ "workload-dictates-architecture" — training/inference ต้องการ massive parallelism ของ GPU แต่ orchestration layer ของ agentic system มี access pattern ที่ CPU ถนัดกว่า เช่น context switching, memory bandwidth, system calls เป็นหัวข้อที่ควรสอนควบคู่กับ GPU programming ใน AI systems course

**ผู้เชี่ยวชาญด้าน AI:** AMD ใช้การวัดระดับ rack (throughput per kW) แทน single-chip เป็น framing ที่ชาญฉลาดเพราะตรงกับวิธีที่ data center operator คิดต้นทุน แต่ benchmark เหล่านี้เป็น vendor-generated projections — ต้องรอ third-party validation จาก MLPerf หรือ SemiAnalysis ก่อนตัดสินใจย้าย workload

**โปรแกรมเมอร์มืออาชีพ:** ถ้า build agentic pipeline แยก orchestration layer (CPU instance) ออกจาก inference layer (GPU instance) และ benchmark workload จริงบน EPYC instance ก่อน — อาจประหยัด cost ได้อย่างมีนัยสำคัญสำหรับ workload ที่ memory-bound

## 2. Oracle — OpenAI Models and Codex on OCI

**อาจารย์ (มหาวิทยาลัย):** Oracle กำลังใช้ existing enterprise relationships เป็น distribution lever สำหรับ AI adoption — คล้ายกับที่ Microsoft ใช้ M365 base ผลักดัน Copilot เป็นเคส channel leverage strategy ที่ดีสำหรับวิชา technology marketing และ platform strategy

**ผู้เชี่ยวชาญด้าน AI:** enterprise procurement cycle ยาว 6–18 เดือน การที่ Oracle Universal Credits ครอบ OpenAI models ลด time-to-first-use ลงอย่างมีนัยสำคัญ — แต่ยังต้องติดตาม pricing ผ่าน OCI เทียบ direct OpenAI pricing ว่าต่างกันอย่างไร และ model tier ไหนบ้างที่ครอบคลุม

**โปรแกรมเมอร์มืออาชีพ:** ถ้าทำงานในองค์กรที่มี Oracle Cloud commitment ตรวจสอบ Universal Credits ที่เหลือและทดสอบ Codex API ทันที — อาจ unlock capacity ที่มีอยู่แล้วโดยไม่ต้องรอ procurement ใหม่หลายเดือน

## 3. TSMC — May 2026 Record Revenue on AI Chip Demand

**อาจารย์ (มหาวิทยาลัย):** TSMC monthly revenue เป็น leading indicator ที่ดีที่สุดตัวหนึ่งของ AI investment cycle — ทุก AI chip ล้วนผ่าน TSMC ใช้สอนเรื่อง supply chain concentration risk และ technology bottleneck ในวิชา tech economics ได้ทันที

**ผู้เชี่ยวชาญด้าน AI:** สถิติรายเดือนใหม่ต่อเนื่องบ่งบอกว่า demand ยังนำ supply อย่างชัดเจน ยังไม่มี inventory correction — GPU/AI chip supply จะตึงตัวต่อไปอีก 2–4 ไตรมาส เป็น signal สำคัญสำหรับการวางแผน infrastructure

**โปรแกรมเมอร์มืออาชีพ:** TSMC revenue signal หมายถึง GPU availability บน cloud จะยังไม่ง่ายขึ้น → ควร lock-in committed use discount หรือ spot reservation ล่วงหน้าก่อน demand พุ่งในครึ่งปีหลัง 2026

# Perspectives — 2026-06-17 (watchlist)

## 1. Amazon — AWS Summit NYC: Kiro, Bedrock AgentCore, Amazon Quick
**อาจารย์ (มหาวิทยาลัย):** AWS Summit 2026 เป็นตัวอย่างดีสำหรับสอน "full-stack agentic platform" — ทำให้นักเรียนเห็นว่า hyperscaler ไม่ได้แข่งที่โมเดลเพียงอย่างเดียว แต่แข่งที่ tooling, runtime, และ developer experience ทั้งระบบ
**ผู้เชี่ยวชาญด้าน AI:** AgentCore แก้ปัญหาจริงที่ enterprise พบ — memory, identity, observability ที่ต้องสร้างเองในปัจจุบัน; spec-first approach ของ Kiro ลด hallucinated architecture จาก agentic coding ที่เป็นปัญหาหลักในการ deploy agent ระดับ production
**โปรแกรมเมอร์มืออาชีพ:** Kiro Pro Max เพิ่ม frontier model access และ higher usage limits — ถ้า build บน AWS ให้ evaluate AgentCore สำหรับ production agent runtime ทันที เพราะ memory/identity ที่ managed จะลด engineering overhead ได้มาก

## 2. Nvidia — Jensen Huang GTC Paris Keynote ที่ VivaTech 2026
**อาจารย์ (มหาวิทยาลัย):** Jensen Huang กลับปารีสพร้อม progress report บน 20+ AI factories ที่สัญญาไว้ปีที่แล้ว — ให้นักเรียนถาม "sovereign AI คืออะไร และทำไมยุโรปจึงต้องการ?" เพื่อเข้าใจ geopolitics ของ AI infrastructure
**ผู้เชี่ยวชาญด้าน AI:** "Physical AI" ที่ Huang เน้นที่ VivaTech ครอบคลุม robotics, autonomous vehicles, industrial AI — เป็น convergence ระหว่าง software AI และ hardware ecosystem ที่ต้องการ GPU inferencing; สำหรับยุโรปที่มี EU AI Act, sovereign AI stack จะสำคัญมากกว่าตลาดอื่น
**โปรแกรมเมอร์มืออาชีพ:** ถ้า build AI application สำหรับตลาดยุโรป ควรติดตาม sovereign AI tools และ EU AI Act compliance frameworks ที่ Nvidia จะประกาศที่ VivaTech — CUDA ecosystem ในยุโรปกำลังได้รับ investment เพิ่มขึ้นอย่างมีนัยสำคัญ

## 3. Meta Platforms — AI Mode บน Facebook ด้วย Muse Spark
**อาจารย์ (มหาวิทยาลัย):** AI Mode คือตัวอย่าง RAG บน social graph จริง — ให้นักเรียนวิเคราะห์ว่า community-generated knowledge ที่ Meta ดึงมาตอบคำถามมีคุณภาพและ bias อย่างไรเมื่อเทียบกับ curated knowledge base
**ผู้เชี่ยวชาญด้าน AI:** นี่คือ consumer proof point ที่ Muse Spark ต้องการ — Meta มีข้อได้เปรียบเฉพาะตัว: 3 พันล้าน user สร้าง retrieval corpus แบบ real-time ที่คู่แข่งไม่มี แต่ information quality จาก public posts คือ risk ที่ต้องจัดการ
**โปรแกรมเมอร์มืออาชีพ:** สำหรับผู้พัฒนา Meta API ควรประเมิน data governance ของ public content ที่ชุมชนสร้าง เพราะ AI Mode อาจใช้ content เหล่านั้นเป็น retrieval source; ติดตาม API terms of service update จาก Meta ด้วย

## 4. Microsoft — Work IQ APIs Go GA
**อาจารย์ (มหาวิทยาลัย):** Work IQ ทำให้ "organizational intelligence" กลายเป็น programmable API — เป็นก้าวจาก "AI ที่ตอบคำถาม" สู่ "AI ที่รู้จักองค์กรจากข้างใน" เป็นวัตถุดิบดีสำหรับสอน context-aware AI
**ผู้เชี่ยวชาญด้าน AI:** Work IQ ใช้ consumption-based billing ผ่าน Copilot Credits — agent ที่ดึง organizational context จำนวนมากจะ consume credits สูง; ต้องวาง context retrieval strategy ก่อน scale เพื่อ manage ต้นทุน
**โปรแกรมเมอร์มืออาชีพ:** Work IQ เปิด A2A protocol, remote MCP server, และ REST API พร้อมกัน — standard interfaces เหล่านี้หมายความว่า integrate ได้กับ agent framework ส่วนใหญ่; เริ่ม prototype M365 agent ที่ต้องการ organizational context ได้เลยวันนี้

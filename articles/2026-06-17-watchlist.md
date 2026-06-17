# สรุปข่าว AI ประจำวันที่ 2026-06-17 — Watchlist

> _หมายเหตุ: รอบนี้ตรวจสอบข่าวผ่าน WebSearch (snippet) เท่านั้น_

> TL;DR
> - **Amazon (AMZN):** AWS Summit NYC วันนี้ — เปิดตัว Kiro (agentic IDE), Bedrock AgentCore และ Amazon Quick ประกาศ full-stack agentic platform ระดับองค์กร
> - **Nvidia (NVDA):** Jensen Huang เปิด GTC Paris keynote ที่ VivaTech ปารีสวันนี้ — AI factories, sovereign AI, physical AI สำหรับยุโรป
> - **Meta (META) + Microsoft (MSFT):** Meta เปิด AI Mode บน Facebook ด้วย Muse Spark; Microsoft Work IQ APIs go GA

## ข่าวเด่น AI ล่าสุด

### 1. Amazon (AMZN · Tier 1) — AWS Summit NYC: Kiro, Bedrock AgentCore และ Amazon Quick — Full-Stack Agentic Platform ครบวงจร — [AWS](https://aws.amazon.com/events/summits/new-york/)

AWS Summit New York 2026 เปิดวันนี้ (17 มิ.ย.) ที่ Javits Center, NYC พร้อมเปิดตัว agentic AI platform ถึง 3 ผลิตภัณฑ์พร้อมกัน ได้แก่ **Kiro** คือ agentic IDE บน VS Code ที่ใช้ formal specification (requirements.md, design.md, tasks.md) นำหน้าก่อนเขียนโค้ด ถือเป็น successor ของ Amazon Q Developer โดย Kiro Pro Max เพิ่ม frontier model access และ higher usage limits; **Bedrock AgentCore** เป็น enterprise agent runtime ที่รวม memory management, identity verification, code-interpreter, browser tools และ observability ไว้ใน managed service ครบชุด; **Amazon Quick** เป็น AI work assistant สำหรับองค์กรที่เชื่อมกับทุก context ในงานและสามารถ take action แทนผู้ใช้ได้ แนวทางนี้สะท้อนว่า Amazon กำลังสร้าง "moat" ผ่าน platform integration มากกว่าการแข่งตัวโมเดลโดยตรง — ถ้า enterprise ใช้ AWS infrastructure อยู่แล้ว AgentCore ลด switching cost เพราะ memory/identity/audit อยู่ใน same ecosystem ผู้เชี่ยวชาญมองว่า spec-first approach ของ Kiro เป็นนวัตกรรมที่แก้ปัญหาจริง: agent ที่เขียนโค้ดโดยไม่มี formal spec มักสร้าง code debt ทันที สำหรับโปรแกรมเมอร์ที่ build บน AWS ถึงเวลา evaluate Kiro Pro Max และ AgentCore สำหรับ production agent pipeline แล้ว

### 2. Nvidia (NVDA · Tier 1) — Jensen Huang เปิด GTC Paris Keynote ที่ VivaTech 2026 — AI Factories, Sovereign AI, Physical AI สำหรับยุโรป — [Nvidia](https://www.nvidia.com/en-eu/events/vivatech/)

Jensen Huang CEO ของ Nvidia กลับสู่กรุงปารีส (17 มิ.ย.) เพื่อเปิด GTC Paris keynote ที่งาน **VivaTech 2026** (17–20 มิ.ย. ที่ Paris Expo Porte de Versailles) — keynote ที่ถูกวาง positioning ไว้เป็น progress report สำหรับคำมั่นสัญญาที่เวที VivaTech 2025 ซึ่ง Huang สัญญาว่ายุโรปจะมี **AI factories มากกว่า 20 แห่ง** พร้อมยก Mistral AI เป็นผู้นำ sovereign compute ของทวีป ปีนี้ keynote ครอบคลุมสาม "frontiers" ได้แก่ AI factories (data centers ที่ผลิต intelligence เหมือนโรงงานผลิตไฟฟ้า), agentic AI (ระบบที่วางแผนและลงมือหลายขั้นตอนแทนมนุษย์), และ physical AI (โมเดลที่ขับหุ่นยนต์, ยานพาหนะ, เครื่องจักรอุตสาหกรรม) นอกจากนี้ AWS และ Nvidia ยังร่วมจัด Startup Village ที่รวม 7 French AI startups ที่สร้าง production-ready solutions ด้าน predictive AI, voice, robotics และ decision intelligence VivaTech 2026 เป็น geo-political statement สำหรับ Nvidia เช่นกัน — ยุโรปมี EU AI Act, Digital Markets Act และ GDPR ซึ่งสร้าง compliance burden พิเศษ; sovereign AI stack ที่ Nvidia ลงทุนจะช่วยให้ผู้ใช้ยุโรปใช้ GPU infrastructure ได้โดยไม่ต้องข้าม data residency boundaries ผู้เชี่ยวชาญมองว่า "Physical AI" คือ frontier สำคัญหลัง LLM สำหรับโปรแกรมเมอร์ที่ build สำหรับตลาดยุโรป ควรติดตาม EU AI Act compliance frameworks + Nvidia sovereign AI tools ที่จะประกาศที่งานนี้

### 3. Meta Platforms (META · Tier 1) — AI Mode บน Facebook เปิดตัว ดึงคำตอบ AI จาก Public Posts ด้วย Muse Spark — [TechCrunch](https://techcrunch.com/2026/06/15/metas-new-ai-mode-on-facebook-pulls-from-public-info-across-its-platforms/)

Meta ประกาศ (15 มิ.ย.) เปิดตัว **AI Mode** บน Facebook — รูปแบบใหม่ของการค้นหาที่ใช้ Meta AI synthesize คำตอบจาก public posts ทั่วแพลตฟอร์ม ทั้ง Groups และ Reels ผู้ใช้ถามคำถามภาษาพูดธรรมชาติและได้คำตอบที่รวบรวมจาก discussion จริงของ community แทนที่จะต้องเลื่อนดูผลลัพธ์ search AI Mode ขับเคลื่อนด้วย **Muse Spark** โมเดล proprietary ตัวแรกของ Meta (เปิดตัว เม.ย. 2026) พร้อมฟีเจอร์เสริมอย่าง intelligent camera suggestions, generative photo presets, virtual wardrobe tool และ hardware device ราคา **$799** นี่คือ consumer proof point ที่ Muse Spark ต้องการ หลังจาก Zuckerberg ยังต้องพิสูจน์ให้ developer community เชื่อว่า Meta สามารถดึง paying users และ enterprise clients ได้ในตลาดที่ OpenAI, Anthropic และ Google ครองก่อน ผู้เชี่ยวชาญมองว่า Meta มีข้อได้เปรียบที่ไม่มีคู่แข่งรายใดทัดเทียมได้: 3 พันล้าน user สร้าง real-time retrieval corpus อยู่ตลอดเวลา การที่ Muse Spark ทำงาน on Facebook คือ proof point ที่ Zuckerberg จะนำไปขาย B2B ด้วย สำหรับโปรแกรมเมอร์ที่ integrate Meta APIs ควรพิจารณา data governance ของ public community content เพราะ AI Mode อาจ retrieve เนื้อหาเหล่านั้น

### 4. Microsoft (MSFT · Tier 1) — Work IQ APIs Go GA (16 มิ.ย.) — Agentic Intelligence Layer สำหรับ M365 พร้อม Deploy — [Microsoft](https://www.microsoft.com/en-us/licensing/news/work-iq-general-availability)

Microsoft ประกาศ Work IQ APIs เปิดให้ใช้งานทั่วไป (GA) อย่างเป็นทางการเมื่อ **16 มิ.ย. 2026** หลังจากประกาศที่ Microsoft Build 2026 เมื่อ 2 มิ.ย. Work IQ คือ "workplace intelligence layer" ที่สร้าง semantic understanding ขององค์กรโดยการ process content จาก email, calendar, meetings, chats, files, people, collaboration patterns และ line-of-business systems อย่างต่อเนื่อง ทำให้ agent รู้ว่าใคร-ทำ-อะไร-กับใคร-เมื่อไหร่ API endpoints ที่ GA พร้อมกัน ได้แก่ A2A protocol, remote MCP server และ REST API ทั้งหมด billing ผ่าน **Copilot Credits** (consumption-based, no separate subscription) ความสำคัญเชิง platform: Work IQ ทำให้ agent "รู้จักองค์กรจากข้างใน" ซึ่งต่างจาก RAG บน document เพราะเข้าใจ relationship และ workflow pattern จริง ไม่ใช่แค่ text content ผู้เชี่ยวชาญเตือนให้วาง context retrieval strategy ก่อน scale เพราะ Copilot Credits จะถูก consume ตามปริมาณ organizational context ที่ดึง; ต้องออกแบบ retrieval scope ตั้งแต่ต้นเพื่อ manage ต้นทุน สำหรับโปรแกรมเมอร์: standard interfaces (REST API, MCP server, A2A) หมายความว่า integrate ได้กับ agent framework ส่วนใหญ่ที่ใช้อยู่แล้ว เริ่ม prototype M365 agent ที่ต้องการ organizational context ได้เลยวันนี้

## Action items
- **สำหรับอาจารย์/นักเรียน:** ใช้ AWS Summit เป็น case study "full-stack agentic platform" เทียบกับ "single-model API strategy"; ถาม Jensen Huang's vision ด้าน "physical AI" ที่ VivaTech สอน AI นอกเหนือจากงานข้อความ
- **สำหรับผู้เชี่ยวชาญ AI:** ทดลอง Bedrock AgentCore สำหรับ production agent runtime; ออกแบบ Work IQ Copilot Credits budget ก่อน deploy M365 agents; ติดตามการประกาศ sovereign AI เพิ่มเติมจาก Nvidia ที่ VivaTech
- **สำหรับโปรแกรมเมอร์:** ทดลอง Kiro เพื่อ spec-first development วันนี้; prototype Work IQ REST API หรือ MCP server สำหรับ M365 agent; ถ้าสร้าง app สำหรับตลาดยุโรป ศึกษา EU AI Act + Nvidia sovereign AI tools จาก VivaTech 2026

## การครอบคลุม watchlist
> คัดจาก Tier 1 · บริษัทที่มีข่าวสำคัญวันนี้: Amazon, Nvidia, Meta Platforms, Microsoft · Tier 2 ไม่ถูกเรียกใช้

---
_Generated by the `daily-ai-watchlist` skill on 2026-06-17 (Asia/Bangkok) · model claude-opus-4-8._

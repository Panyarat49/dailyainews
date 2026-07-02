# Perspectives — 2026-07-02 (watchlist)

## 1. Meta Platforms — เตรียมทำธุรกิจคลาวด์ขาย Compute AI ส่วนเกิน
**อาจารย์ (มหาวิทยาลัย):** การที่ hyperscaler อย่าง Meta กลายมาเป็นผู้ขาย compute แข่งกับ AWS/Google Cloud/Azure สะท้อนว่าการลงทุน AI infrastructure มหาศาลได้สร้าง capacity เกินความต้องการภายในของตัวเอง เหมาะเป็นกรณีศึกษาเศรษฐศาสตร์เรื่อง capital allocation ในวงจร AI boom
**ผู้เชี่ยวชาญด้าน AI:** การขาย excess compute พร้อมโมเดลของตัวเองอาจเป็นกลยุทธ์สร้างรายได้จาก sunk cost ของ data center ที่สร้างไว้เกิน demand จริง — ต้องติดตามว่า Meta จะเปิดให้ใช้ Llama รุ่นใหม่ผ่านช่องทางนี้ด้วยหรือไม่ และจะ pricing แข่งกับผู้เล่นรายเดิมอย่างไร
**โปรแกรมเมอร์มืออาชีพ:** ถ้า Meta เข้าตลาด cloud compute จริง จะเพิ่มตัวเลือกผู้ให้บริการ GPU/AI compute ให้ทีม dev ที่กำลังเจอปัญหา capacity ขาดแคลนหรือราคาสูง ควรติดตามราคาที่ประกาศเทียบกับ AWS/Azure/GCP เมื่อเปิดตัวจริงก่อนตัดสินใจย้าย workload

## 2. Alphabet — Gemini Spark เปิดให้ใช้งานบน Mac แล้ว
**อาจารย์ (มหาวิทยาลัย):** การขยาย agentic assistant จาก mobile สู่ desktop สะท้อนว่า Google กำลังผลัก Gemini เข้าสู่ workflow ประจำวันของผู้ใช้ทุก platform อย่างจริงจัง — ควรใช้เป็นตัวอย่างสอนเรื่อง cross-platform AI assistant strategy เทียบกับ Siri และ Copilot
**ผู้เชี่ยวชาญด้าน AI:** ความสามารถ real-time topic tracking และการเชื่อมต่อ Google Tasks/Keep ทำให้ Spark ขยับจาก "chatbot ตอบคำถาม" ไปสู่ "agent ที่ทำงานต่อเนื่องในชีวิตประจำวัน" ซึ่งเป็นทิศทางเดียวกับที่ Anthropic และ OpenAI กำลังผลักดัน agentic assistant ของตัวเอง
**โปรแกรมเมอร์มืออาชีพ:** นักพัฒนาที่ build บน Gemini API ควรติดตามว่า Spark macOS app เปิด extension/plugin API ให้ third-party เชื่อมต่อหรือไม่ เพราะจะเป็นช่องทางใหม่สำหรับ distribution บน desktop ที่ก่อนหน้านี้ Google ยังไม่มี

## 3. Amazon — Claude Fable 5 กลับมาบน Amazon Bedrock พร้อม Guardrail ที่แน่นขึ้น
**อาจารย์ (มหาวิทยาลัย):** การที่ Amazon Bedrock รีบนำ Fable 5 กลับมาทันทีหลังสหรัฐฯ ยกเลิกคำสั่งควบคุมส่งออก แสดงให้เห็นว่า cloud provider รายใหญ่มี incentive สูงในการ deploy โมเดล frontier ให้เร็วที่สุดเพื่อรักษาความสามารถแข่งขัน — น่าใช้สอนเรื่อง dependency ระหว่าง cloud platform กับ model provider รายเดียว
**ผู้เชี่ยวชาญด้าน AI:** การเพิ่ม safety classifier ที่ reroute query เสี่ยงสูงไปยัง Opus 4.8 แทนที่จะปฏิเสธตรงๆ เป็นแนวทาง graceful degradation ที่น่าสนใจ — ทำให้ user experience ไม่สะดุดขณะยังคง safety posture ตัวเลข trigger rate ต่ำกว่า 5% ของ session บ่งชี้ว่า guardrail ถูก tune ให้แม่นยำโดยไม่กระทบการใช้งานปกติมากนัก
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ใช้ Fable 5 ผ่าน Bedrock ควรตรวจสอบพฤติกรรม reroute-to-Opus นี้ในระบบ production เพราะอาจมีผลต่อ latency และ cost เมื่อ classifier trigger — ควร log และ monitor อัตรา refusal/reroute เพื่อประเมินผลกระทบต่อ user-facing feature

## 4. Microsoft — TeamDynamix ลดภาระงาน IT ลงถึง 70% ด้วย Azure AI
**อาจารย์ (มหาวิทยาลัย):** กรณีศึกษานี้แสดงให้เห็นการนำ agentic automation ไปใช้ในงาน IT service management ที่เป็น routine และวัดผลได้ชัดเจน เหมาะเป็นตัวอย่างสอนเรื่อง ROI ของ AI adoption ในองค์กรที่ไม่ใช่ AI-native
**ผู้เชี่ยวชาญด้าน AI:** ตัวเลขลดภาระงาน 70% เป็นตัวเลขที่สูงสำหรับ agent-led automation ในงาน ITSM — น่าติดตามว่าตัวเลขนี้วัดจากอะไร (ticket volume, resolution time, หรือ FTE) เพราะ metric ที่ต่างกันจะให้ภาพความสำเร็จที่ต่างกันมาก
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ดูแลระบบ ITSM ภายในองค์กรควรศึกษา pattern การผสาน Azure AI เข้ากับ no-code platform แบบ TeamDynamix เป็นแนวทางเริ่มต้น automation โดยไม่ต้องเขียนโค้ดจำนวนมาก

## 5. Palantir — CEO Karp วิจารณ์โมเดลราคา Token ของ OpenAI และ Anthropic
**อาจารย์ (มหาวิทยาลัย):** ข้อวิจารณ์ของ Karp เปิดประเด็นถกเถียงสำคัญเรื่อง pricing model ของ generative AI — ระหว่าง pay-per-token กับ pay-per-outcome ซึ่งเป็นคำถามเชิงเศรษฐศาสตร์ที่ยังไม่มีคำตอบชัดเจนในอุตสาหกรรม เหมาะเป็นหัวข้อถกในชั้นเรียน AI economics
**ผู้เชี่ยวชาญด้าน AI:** การที่ Karp เชื่อมโยงคำวิจารณ์นี้กับดีล Palantir-Nvidia ที่นำ Nemotron (open model) เข้าสู่หน่วยงานรัฐบาลสหรัฐฯ สะท้อนกลยุทธ์ "AI sovereignty" ที่ผลักองค์กรให้ควบคุม model และข้อมูลของตัวเองแทนพึ่งพา API ภายนอกที่ต้นทุนไม่แน่นอน
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ build บน API แบบ pay-per-token ควรเริ่มประเมิน cost model ทางเลือก เช่น self-host open-weight model หรือ outcome-based contract โดยเฉพาะงานที่ปริมาณ token สูงแต่ value ต่อ query ไม่สูงตาม เพื่อเตรียมรับมือหากตลาดเปลี่ยนทิศทางไปทาง pricing แบบใหม่จริง

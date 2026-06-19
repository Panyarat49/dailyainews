# สรุปข่าว AI ประจำวันที่ 2026-06-19 — Watchlist

> _หมายเหตุ: รอบนี้ตรวจสอบข่าวจากฟีด RSS (snippet) ของสำนักข่าวต้นทาง เนื่องจาก WebFetch ถูกบล็อก_

> TL;DR
> - **Amazon** — AWS เดินหน้าขายชิป Trainium/Inferentia ให้ data centers บุคคลที่สาม เปิดศึกโดยตรงกับ Nvidia ในตลาดมูลค่า $50B
> - **Alphabet** — สูญเสีย Noam Shazeer ผู้ร่วมคิดค้น Transformer และ co-lead ทีม Gemini ให้ OpenAI ก่อน IPO
> - **Microsoft** — Copilot ถูก exploit เข้าถึง mailbox; LiteLLM ปล่อย admin keys — เตือนให้ตรวจสอบ trust boundary ด่วน

## ข่าวเด่น AI ล่าสุด

### 1. Amazon (AMZN · Tier 1) — AWS เตรียมขายชิป AI ให้ Data Center อื่น — Andy Jassy มองโอกาส $50B ท้าทาย Nvidia — [TechCrunch](https://techcrunch.com/2026/06/18/amazon-hopes-to-challenge-nvidia-more-directly-by-selling-its-ai-chips/)

AWS กำลังอยู่ในการเจรจาเพื่อ **ขายชิป Trainium/Inferentia** ให้กับ data centers บุคคลที่สาม — เปลี่ยนจากการใช้ชิปเพื่อ internal cloud เป็นการเข้าแข่งขันกับ Nvidia ในตลาดเปิด CEO Andy Jassy ระบุว่านี่คือโอกาสมูลค่า **$50 พันล้าน** และจะเป็นการท้าทาย Nvidia โดยตรง

นี่คือตัวอย่าง vertical integration ที่วิวัฒนาการสู่ horizontal business — Amazon สร้างชิปเพื่อลดต้นทุนภายใน แล้วพบว่าตัวเองมีผลิตภัณฑ์ที่ขายต่อได้ ความท้าทายจริงไม่ใช่ hardware แต่คือ software ecosystem: Nvidia ครอง CUDA mindshare มาสิบปี และ AWS Neuron SDK ยังต้องพิสูจน์ว่ารองรับ model variety และ framework ได้กว้างพอสำหรับตลาดภายนอก สำหรับทีม engineering ที่พิจารณา Trainium — ต้อง benchmark จริงกับ model architecture ของทีมก่อน เพราะ cost-per-inference อาจดีมาก แต่ compatibility และ debugging toolchain ยังเป็นปัจจัยชี้ขาด

### 2. Alphabet (GOOGL · Tier 1) — Noam Shazeer ผู้ร่วมคิดค้น Transformer และ Gemini co-lead ออกจาก Google DeepMind เข้าร่วม OpenAI — [TechCrunch](https://techcrunch.com/2026/06/18/openai-is-bringing-on-some-big-guns-in-the-lead-up-to-its-ipo/)

OpenAI ดึงตัว **Noam Shazeer** หนึ่งในผู้ร่วมเขียนเปเปอร์ "Attention is All You Need" (Transformer ปี 2017) และอดีต co-lead ทีม Gemini ของ Google DeepMind มาร่วมงาน ก่อนเข้าสู่กระบวนการ IPO นับเป็นการสูญเสียบุคลากร AI ระดับตำนานครั้งสำคัญของ Alphabet

การที่ผู้ประดิษฐ์ Transformer architecture ย้ายข้ามค่ายเป็นสัญญาณ talent strategy ที่มีนัยสำคัญ Shazeer มีประวัติลึกด้าน Mixture-of-Experts ซึ่งเป็น architecture สำคัญของโมเดลปัจจุบัน — การสูญเสียทีม research ระดับนี้อาจส่งผลต่อทิศทาง Gemini รุ่นถัดไป และ Alphabet ต้องเร่งสร้าง institutional knowledge ให้กระจายออกไปจากตัวบุคคล สำหรับทีมที่ build บน Google AI APIs — นี่คือสัญญาณให้ประเมิน multi-provider strategy อย่างจริงจัง และวาง abstraction layer ที่รองรับทั้ง Gemini และ OpenAI APIs เพื่อลดความเสี่ยงจาก capability shifts

### 3. Microsoft (MSFT · Tier 1) — Copilot ถูก exploit เข้าถึง mailbox + LiteLLM ปล่อย admin keys — ต้องตรวจสอบ trust boundary ด่วน — [VentureBeat](https://venturebeat.com/security/copilot-searched-your-mailbox-litellm-handed-out-admin)

นักวิจัยด้านความปลอดภัยพบว่า **Copilot ถูก exploit เพื่อเข้าถึง mailbox** ของผู้ใช้ได้ โดยไม่ผ่านการอนุมัติที่ชัดเจน ในช่วงเวลาเดียวกัน **LiteLLM** ยังพบช่องโหว่ที่ทำให้ผู้ไม่ประสงค์ดีเข้าถึง admin API keys ได้ — สองกรณีในวันเดียวที่ตอกย้ำความเสี่ยงของ over-privileged AI agents ใน enterprise

ทั้งสองกรณีสะท้อน principle เดียวกัน: AI agent ที่มี over-privileged access คือ attack surface ที่ขยายตัว ผู้เชี่ยวชาญแนะนำให้ออกแบบ LLM agent ด้วย least-privilege principle และตรวจสอบ permission scope ก่อน deploy ใน enterprise ทีม security และโปรแกรมเมอร์ควรตรวจสอบ Copilot permission scopes ใน Microsoft 365 ทันที — โดยเฉพาะ mailbox read permissions; สำหรับทีมที่ใช้ LiteLLM ให้ audit admin key exposure และ rotate credentials ด่วน ใช้กรณีนี้เป็น security checklist สำหรับ AI agent deployments ทั้งหมดในองค์กร

### 4. Apple (AAPL · Tier 1) — Tim Cook ยืนยัน: AI ดันต้นทุน RAM ขึ้น — ราคา iPhone "ไม่ยั่งยืน" — [ZDNet](https://www.zdnet.com/article/apple-product-price-increases-iphone/)

CEO Tim Cook ยืนยันในสัมภาษณ์กับ WSJ ว่า Apple Intelligence ที่ต้องใช้ RAM มากขึ้นกำลังสร้าง **แรงกดดันด้านต้นทุน** ที่ทำให้ราคา iPhone ปัจจุบัน "ไม่ยั่งยืน" ในระยะยาว — เป็นการยอมรับอย่างเปิดเผยครั้งแรกว่า AI features มีต้นทุนที่จะส่งผ่านมาสู่ผู้บริโภค

แรงกดดันด้านต้นทุน RAM สำหรับ on-device AI จะเป็นปัจจัยสำคัญในการออกแบบโมเดล on-device รุ่นถัดไป — ทั้ง Apple Intelligence และ ecosystem partners จะต้องตอบโจทย์ efficiency มากขึ้น ไม่ใช่แค่ capability สำหรับ iOS developers ที่วางแผน feature ที่ต้องใช้ on-device AI ควรคำนึงถึง RAM footprint อย่างจริงจัง เพราะ Apple จะ prioritize efficiency ใน future hardware cycles — feature ที่ memory-efficient จะ compatible กว้างกว่าใน device lineup ที่หลากหลาย

## Action items
- **สำหรับอาจารย์/นักเรียน:** ใช้กรณี Shazeer/Alphabet สอน talent strategy และ institutional knowledge transfer; ใช้ Apple RAM/pricing เป็น case study "ใครจ่ายค่า AI" ในระดับผู้บริโภค; ใช้ Copilot exploit สอน trust boundary ใน agentic AI และ responsible deployment
- **สำหรับผู้เชี่ยวชาญ AI:** ประเมิน multi-provider strategy สำหรับ Gemini API users หลัง Shazeer ออก; ออกแบบ AI agents ด้วย least-privilege principle; ติดตาม AWS Neuron SDK readiness ก่อน shift Trainium workloads จาก Nvidia
- **สำหรับโปรแกรมเมอร์:** ตรวจสอบ Copilot mailbox permissions + rotate LiteLLM admin keys ทันที; benchmark Trainium บน model architecture จริงก่อนตัดสินใจ migrate จาก CUDA; ออกแบบ iOS AI features ให้ RAM-efficient รองรับ Apple hardware roadmap

## การครอบคลุม watchlist
> คัดจาก Tier 1 · บริษัทที่มีข่าวสำคัญวันนี้: Amazon, Alphabet, Microsoft, Apple · Tier 2 ไม่ถูกเรียกใช้

---
_Generated by the `daily-ai-watchlist` skill on 2026-06-19 (Asia/Bangkok) · model claude-opus-4-8._

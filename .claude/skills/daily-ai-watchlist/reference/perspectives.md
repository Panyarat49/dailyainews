# Perspectives — 2026-06-19 (watchlist)

## 1. Amazon — AWS ขายชิป AI ให้ Data Centers บุคคลที่สาม — $50B ท้าทาย Nvidia
**อาจารย์ (มหาวิทยาลัย):** นี่คือตัวอย่างของ vertical integration ที่วิวัฒนาการสู่ horizontal business — Amazon สร้างชิปเพื่อลดต้นทุนภายใน แล้วค้นพบว่าตัวเองมีผลิตภัณฑ์ที่ขายต่อได้ เป็นกรณีศึกษา platform economics และ "accidental competitor" ที่น่าสอนในบริบทยุค AI
**ผู้เชี่ยวชาญด้าน AI:** ความท้าทายจริงไม่ใช่ hardware แต่คือ software ecosystem — Nvidia ครอง CUDA mindshare มาสิบปี; AWS Neuron SDK ยังต้องพิสูจน์ว่ารองรับ model variety และ framework ได้กว้างพอสำหรับตลาดภายนอก อย่างไรก็ตาม ถ้า TCO ต่างกันมาก บริษัทจะลงทุนในการ port
**โปรแกรมเมอร์มืออาชีพ:** ก่อนพิจารณา Trainium สำหรับ production workloads ต้อง benchmark จริงกับ model architecture ของทีม — cost-per-inference อาจดีมาก แต่ compatibility กับ framework ที่ใช้อยู่และ debugging toolchain ยังเป็นปัจจัยชี้ขาด

## 2. Alphabet — Noam Shazeer (Gemini co-lead, Transformer co-inventor) ออกจาก Google DeepMind
**อาจารย์ (มหาวิทยาลัย):** การที่ผู้ประดิษฐ์ Transformer architecture ย้ายข้ามค่ายเป็นวัสดุสอน talent strategy, institutional knowledge transfer และ organizational signaling ที่หาได้ยาก — สะท้อนว่าใน AI อุตสาหกรรม บุคคลระดับ "ผู้สร้าง paradigm" ยังมีมูลค่าเชิงสัญลักษณ์และเชิงเทคนิคสูงมาก
**ผู้เชี่ยวชาญด้าน AI:** Shazeer มีประวัติลึกด้าน Mixture-of-Experts ซึ่งเป็น architecture สำคัญของโมเดลปัจจุบัน การสูญเสียทีม research ระดับนี้อาจส่งผลต่อทิศทาง Gemini รุ่นถัดไป — Alphabet ต้องเร่งสร้าง institutional knowledge ให้กระจายออกไปจากตัวบุคคล
**โปรแกรมเมอร์มืออาชีพ:** สำหรับทีมที่ build บน Google AI APIs (Vertex AI, Gemini API) นี่คือสัญญาณให้ประเมิน multi-provider strategy อย่างจริงจัง — การมี abstraction layer ที่รองรับทั้ง Gemini และ OpenAI APIs จะลดความเสี่ยงจาก talent-driven capability shifts

## 3. Microsoft — Copilot exploit เข้าถึง mailbox + LiteLLM ปล่อย admin keys
**อาจารย์ (มหาวิทยาลัย):** เรื่องนี้เป็นกรณีศึกษา trust boundary ใน agentic AI ที่ตรงไปตรงมา — เมื่อ AI agent มีสิทธิ์เข้าถึงข้อมูลส่วนตัว ช่องโหว่ด้านการออกแบบ scope กลายเป็น security incident ได้ทันที ควรนำไปสอนใน responsible AI deployment
**ผู้เชี่ยวชาญด้าน AI:** ทั้งสองกรณีสะท้อน principle เดียวกัน: AI agent ที่มี over-privileged access คือ attack surface ที่ขยายตัว ควรออกแบบ LLM agent ด้วย least-privilege principle และตรวจสอบ permission scope ก่อน deploy ใน enterprise
**โปรแกรมเมอร์มืออาชีพ:** ตรวจสอบ Copilot permission scopes ใน Microsoft 365 ทันที โดยเฉพาะ mailbox read permissions; สำหรับทีมที่ใช้ LiteLLM — audit admin key exposure และ rotate credentials ด่วน ใช้กรณีนี้เป็น checklist สำหรับ security review ของ AI agent deployments ทั้งหมดในองค์กร

## 4. Apple — Tim Cook ยืนยัน AI ดันต้นทุน RAM ขึ้นราคา iPhone "ไม่ยั่งยืน"
**อาจารย์ (มหาวิทยาลัย):** คำพูดของ Tim Cook เปิดการสนทนาเรื่อง "ใครจ่ายค่า AI" ในระดับผู้บริโภค — บทเรียนสำหรับนักเรียนว่า AI feature cost ไม่ใช่ invisible แต่ถ่ายโอนมาสู่ราคาสินค้าปลายทาง เป็น case study economics of AI consumer hardware ที่ตรงไปตรงมา
**ผู้เชี่ยวชาญด้าน AI:** แรงกดดันด้านต้นทุน RAM สำหรับ on-device AI จะเป็นปัจจัยสำคัญในการออกแบบโมเดล on-device รุ่นถัดไป — ทั้ง Apple Intelligence และ ecosystem partners จะต้องตอบโจทย์ efficiency มากขึ้น ไม่ใช่แค่ capability
**โปรแกรมเมอร์มืออาชีพ:** สำหรับ iOS developers ที่วางแผน feature ที่ต้องใช้ on-device AI — ให้คำนึงถึง RAM footprint อย่างจริงจัง เพราะ Apple จะ prioritize efficiency ใน future hardware cycles; feature ที่ memory-efficient จะ compatible กว้างกว่าใน device lineup ที่หลากหลาย

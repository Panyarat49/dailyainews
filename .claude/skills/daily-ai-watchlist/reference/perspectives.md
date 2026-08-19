# Perspectives — 2026-08-19 (watchlist)

## 1. Microsoft — Copilot social-engineered into revealing its own exploit
**อาจารย์ (มหาวิทยาลัย):** เคสนี้เหมาะใช้สอนเรื่อง social engineering ที่พุ่งเป้าไปที่ตัว LLM เองแทนที่จะเป็นมนุษย์ — นักวิจัยไม่ได้ reverse-engineer โค้ด แต่ "ถาม" Copilot จนมันเผยกลไก guardrail ของตัวเอง
**ผู้เชี่ยวชาญด้าน AI:** นี่คือรูปแบบ prompt-injection ที่ซับซ้อนขึ้นไปอีกขั้น — ใช้บทสนทนาหลายรอบ (multi-turn) ค่อยๆ สกัดข้อมูลเกี่ยวกับกลไกความปลอดภัยทีละชิ้น แทนการโจมตีแบบ single-shot ทำให้ guardrail แบบเดิมตรวจจับยากขึ้นมาก
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ integrate Copilot หรือ AI assistant อื่นในองค์กรควรตรวจสอบว่า auto-execution ของ deep link/URL ต้องมี user gesture ยืนยันจริง และเฝ้าระวัง multi-turn conversation ที่พยายามสอบถามกลไก safety อย่างเป็นระบบ

## 2. Nvidia — China's homegrown AI accelerators to hit 90% domestic share
**อาจารย์ (มหาวิทยาลัย):** ตัวเลข 90% เป็นกรณีศึกษาชัดเจนของผลกระทบจากนโยบายควบคุมการส่งออกชิปต่อโครงสร้างตลาดในระยะกลาง เหมาะสอนเรื่อง geopolitics กับห่วงโซ่อุปทานเทคโนโลยี
**ผู้เชี่ยวชาญด้าน AI:** สำหรับ Nvidia นี่คือสัญญาณว่าตลาดจีนซึ่งเคยเป็นแหล่งรายได้สำคัญกำลังปิดตัวลงเร็วกว่าคาด แม้ Cambricon/Huawei จะยังตามหลังด้าน software ecosystem แต่ threshold ด้าน raw throughput สำหรับงาน inference ในประเทศดูจะเพียงพอแล้ว
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ deploy โมเดลในตลาดจีนควรเริ่มวางแผน dual-stack (CUDA + CANN หรือเทียบเท่า) ตั้งแต่วันนี้ เพราะ hardware stack ที่ใช้ได้ในจีนกับนอกจีนกำลังแยกทางกันจริงจัง ไม่ใช่แค่กระแส

## 3. Alphabet — roundup: Workspace AI defaults, Gemini in Chrome, UK contrail-AI trial
**อาจารย์ (มหาวิทยาลัย):** สามข่าวนี้ฉายภาพกลยุทธ์ของ Google ได้ครบมิติ — ผลักดัน Gemini เข้าไปอยู่ในทุกผลิตภัณฑ์แบบ default (ทั้งเสี่ยงด้าน privacy และได้ประโยชน์ด้าน public good อย่างเรื่อง contrail) เหมาะใช้สอนเรื่อง trade-off ระหว่างการเข้าถึงข้อมูลของ AI กับประโยชน์ที่ได้
**ผู้เชี่ยวชาญด้าน AI:** การที่ Gemini เข้าถึง Gmail/Docs/Calendar โดย default ในองค์กรเป็นความเสี่ยงด้าน data governance ที่แท้จริง ขณะที่ agentic auto-browse ใน Chrome ต้องพึ่งการตรวจจับ prompt injection ที่แข็งแรง — ส่วนโปรเจกต์ contrail กับรัฐบาลอังกฤษแสดงว่า Google กำลังผลักดัน AI เข้าสู่ public-sector use case ที่วัดผลได้จริง
**โปรแกรมเมอร์มืออาชีพ:** แอดมิน Workspace ควรตรวจสอบการตั้งค่า Gemini default access ทันที โดยเฉพาะองค์กรที่มีข้อมูลอ่อนไหว ส่วนทีมที่ทำ browser automation ควรศึกษาการออกแบบ confirmation-gate ของ auto-browse เป็นแนวทางอ้างอิงสำหรับ agentic feature ของตัวเอง

## 4. Tesla — Cybercab nears public launch
**อาจารย์ (มหาวิทยาลัย):** ความล่าช้าของ Cybercab จากกำหนดเดิมเป็นตัวอย่างที่ดีสำหรับสอนเรื่องช่องว่างระหว่าง timeline ที่ประกาศกับความพร้อมจริงของเทคโนโลยี autonomous driving
**ผู้เชี่ยวชาญด้าน AI:** จุดสำคัญคือ Cybercab ไม่มีพวงมาลัยหรือเบรก ต้องพึ่ง FSD/robotaxi stack เต็มรูปแบบโดยไม่มี fallback ให้มนุษย์เข้าควบคุม ซึ่งเป็นการทดสอบความน่าเชื่อถือของระบบในระดับที่สูงกว่ารถที่ยังมีคนขับสำรอง
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ทำงานด้าน autonomous system ควรติดตามข้อมูล safety validation ที่ Tesla เปิดเผย (หรือไม่เปิดเผย) ก่อนเปิดตัวจริง เพราะจะเป็นบรรทัดฐานสำคัญสำหรับมาตรฐานความปลอดภัยของ robotaxi ทั้งอุตสาหกรรม

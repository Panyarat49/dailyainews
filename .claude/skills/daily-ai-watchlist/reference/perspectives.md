# Perspectives — 2026-06-29 (watchlist)

## 1. Alphabet (GOOGL) — Google จำกัดการใช้ Gemini Enterprise ของ Meta — Backlog $462B

**อาจารย์ (มหาวิทยาลัย):** กรณีนี้สะท้อน "scarcity ใน digital goods" ที่ดูเหมือนไม่จำกัด แต่ถูก bottleneck ด้วย physical infrastructure — data center, power และ cooling ที่ใช้เวลาหลายปีในการสร้าง backlog $462B ฉายภาพ supply-demand gap ที่ใหญ่มากและเป็น case study เรื่อง AI infrastructure economics ในระดับ enterprise ที่ดีมาก

**ผู้เชี่ยวชาญด้าน AI:** Alphabet ที่ไม่สามารถ serve ลูกค้าใหญ่อย่าง Meta ได้ครบ บ่งชี้ว่า infrastructure scale เป็น constraint จริง ไม่ใช่ model quality; $462B backlog กับ 24 เดือนเคลียร์ครึ่งหนึ่ง หมายความว่า enterprise AI demand เกิน supply ไปอีกอย่างน้อย 2 ปี — สำหรับทีมที่วางแผน enterprise AI: SLA ของ cloud providers ไม่ได้รับประกัน capacity จริงในภาวะ high demand

**โปรแกรมเมอร์มืออาชีพ:** ถ้า workload บน Gemini API สูง ควรมี fallback provider และ request caching เป็น engineering requirement ตั้งแต่ต้น ไม่ใช่ optional — กรณี Google-Meta พิสูจน์ว่า single-provider dependency คือ fragility ที่จับต้องได้ แม้แต่ Tier-1 hyperscaler ก็ rationing capacity ได้

## 2. Tesla (TSLA) — Tesla FSD ถูกตรวจสอบหนักขึ้น หลังอุบัติเหตุร้ายแรงเท็กซัส NHTSA+NTSB เปิดสอบ

**อาจารย์ (มหาวิทยาลัย):** Tesla FSD case คือ "AI accountability + information asymmetry" ในแบบตำรา — data logs อยู่กับ Tesla แต่ investigators ต้องการ access; กรณีนี้เป็น empirical evidence ว่า NHTSA ต้องการ standardized ADAS data access protocol เพื่อให้ independent verification ทำได้จริง ไม่ใช่แค่ trust manufacturer's word

**ผู้เชี่ยวชาญด้าน AI:** NHTSA+NTSB เปิดสอบทั้งคู่คือ escalation ที่มีนัยต่อ Tesla FSD timeline — regulatory pressure กำลังสูงขึ้นในช่วงที่ Tesla กำลัง push ให้ FSD autonomous มากขึ้น; การ settle คดี 2023 พร้อมกับคดีใหม่สะท้อนว่า liability framework ยังคลุมเครือและมีแนวโน้มจะมี regulation ตามมา

**โปรแกรมเมอร์มืออาชีพ:** กรณีนี้พิสูจน์ซ้ำว่า immutable, tamper-evident audit trail ของ AI decision chain (sensor → inference → actuator → outcome) เป็น engineering requirement สำหรับ safety-critical systems — data logs คือ primary evidence ทั้งใน legal และ technical investigation ต้อง implement ตั้งแต่ต้นไม่ใช่รอแก้ทีหลัง

## 3. Nvidia (NVDA) — Firmus Technologies (ออสเตรเลีย) ทำดีล AI กับ Nvidia รุกเข้า Southeast Asia

**อาจารย์ (มหาวิทยาลัย):** ดีล Nvidia-Firmus ใน Asia-Pacific เป็นตัวอย่าง "AI geography expanding" — compute infrastructure ไม่กระจุกแค่ US/EU/CN อีกต่อไป แต่กระจายไปยัง emerging markets ที่ demand AI infra ขยายตัวเร็ว Indonesia เป็น largest economy ใน Southeast Asia ที่มี digital transformation agenda ชัดเจน

**ผู้เชี่ยวชาญด้าน AI:** Nvidia กำลัง expand presence ใน Asia-Pacific อย่างจริงจังผ่าน partnership model กับ local AI startups — data center deal ใน Indonesia บ่งบอกว่า region กำลังกลายเป็น front ใหม่ของ AI infrastructure race; Jensen Huang's strategy ของการ "supply everywhere" กำลัง manifest ใน geographies ที่ยังไม่มี hyperscaler presence แน่น

**โปรแกรมเมอร์มืออาชีพ:** สำหรับทีมที่ build AI products สำหรับ Southeast Asia market — Nvidia-Firmus infrastructure อาจมีนัยต่อ local GPU cloud availability และ inference latency ใน Indonesia/regional markets ใน 12-24 เดือน ติดตาม Firmus และ Nvidia APAC partnerships เพื่อ plan regional infrastructure ล่วงหน้า

## 4. Micron (MU · Tier 2) — Wall Street มอง Micron เป็น "Nvidia รุ่นถัดไป" Market Cap แตะ $1.27T

**อาจารย์ (มหาวิทยาลัย):** Micron คือบทเรียน "derived demand" และ "AI value chain" ที่สอนได้ตรงไปตรงมา — ความต้องการ HBM memory ไม่ได้มาจากผู้บริโภคโดยตรง แต่จาก AI data centers ที่รัน training และ inference; 236% gain ในหนึ่งเดือนคือ sign ของ speculative premium ที่ควรถกเรื่อง semiconductor cycle ด้วย

**ผู้เชี่ยวชาญด้าน AI:** Micron HBM supply ยังถูก dominate โดยผู้ผลิตจำนวนจำกัด แต่ประวัติศาสตร์ semiconductor แสดงว่า demand surge มักตามด้วย oversupply ใน 2–3 ปี — ติดตาม Micron earnings เป็น leading indicator ของ GPU compute pricing trend และเตรียม budget ให้รองรับ volatility นี้ในระยะกลาง

**โปรแกรมเมอร์มืออาชีพ:** Memory scarcity จะ translate ไปเป็น GPU cloud pricing ที่สูงขึ้นในระยะกลาง — ควรลงทุนใน memory-efficient inference (quantization, KV cache optimization, speculative decoding) สำหรับ production workloads ที่ cost-sensitive; ติดตาม Micron earnings เป็น early signal ของ infrastructure cost ก่อน cloud providers ปรับ pricing

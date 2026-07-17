# Perspectives — 2026-07-17 (watchlist)

## 1. Alphabet — EU DMA Order + Waymo SF Gridlock Rules

### 1.1 EU orders Google to share search data, open Android to AI rivals
**อาจารย์ (มหาวิทยาลัย):** คำสั่งนี้คือตัวอย่างชัดเจนของ EU Digital Markets Act ที่ใช้บังคับ interoperability กับผู้เล่นที่ dominant ในตลาด — ควรใช้สอนเรื่องความแตกต่างระหว่าง antitrust แบบ US (หลัง fact, ฟ้องเมื่อเกิดความเสียหาย) กับ EU (ex-ante, กำหนดกฎก่อนเกิดปัญหา) และผลกระทบต่อ AI competition โดยเฉพาะ
**ผู้เชี่ยวชาญด้าน AI:** การบังคับให้เปิด Android ให้ AI rivals เข้าถึงได้ลึกยิ่งขึ้น อาจเปลี่ยนดุลอำนาจของ AI assistant บนมือถือ Android ทั้งระบบ ประเด็นทางเทคนิคที่ต้องจับตาคือ Google จะเปิด API ระดับไหน (system-level integration หรือแค่ app-level access) เพราะสองแบบนี้ต่างกันมากในแง่ความสามารถของคู่แข่ง
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่พัฒนา AI assistant บน Android ควรติดตาม API ใหม่ที่ Google ต้องเปิดตามคำสั่งนี้อย่างใกล้ชิด เพราะอาจเปิดโอกาสให้ integrate AI ของตัวเองเข้ากับฟีเจอร์ระดับระบบที่เคยทำไม่ได้ — ควรเตรียม technical evaluation ไว้ล่วงหน้าก่อนเส้นตายมกราคม 2027

### 1.2 San Francisco mayor pushes for tougher rules after Waymo gridlock
**อาจารย์ (มหาวิทยาลัย):** เหตุการณ์นี้เป็นกรณีศึกษาที่ดีเรื่อง "scale failure" ของระบบอัตโนมัติ — รถคันเดียวขัดข้องอาจไม่กระทบอะไร แต่เมื่อ fleet ทั้งหมดเจอสถานการณ์เดียวกันพร้อมกัน (เช่น งานอีเวนต์ใหญ่) ผลกระทบจะทวีคูณ ควรใช้สอนเรื่อง systemic risk ในระบบ AI ที่ทำงานพร้อมกันจำนวนมาก
**ผู้เชี่ยวชาญด้าน AI:** โจทย์ทางเทคนิคที่แท้จริงคือ fleet-level coordination ในสถานการณ์ผิดปกติ (mass event, ถนนปิดกะทันหัน) ซึ่งต่างจากการขับขี่ปกติที่ Waymo แข็งแรงอยู่แล้ว — regulator ที่กดดันตอนนี้น่าจะเรียกร้อง fallback protocol ที่ชัดเจนกว่านี้เมื่อระบบเจอสภาพแวดล้อมนอกเหนือการฝึกฝน
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ทำงานกับ fleet ของ autonomous system ควรมี "graceful degradation" plan สำหรับสถานการณ์ mass-event ไว้ล่วงหน้า ไม่ใช่แค่ per-vehicle safety — หาก regulator ออกกฎใหม่ตามที่นายกเทศมนตรีเรียกร้อง อาจต้องมี reporting/monitoring requirement เพิ่มเติมที่ทีม compliance ต้องเตรียมรับมือ

## 2. Nvidia — Japan National AI Infrastructure (Noetra)
**อาจารย์ (มหาวิทยาลัย):** โครงการนี้เป็นตัวอย่างของ "national AI infrastructure" ที่รัฐบาลร่วมมือโดยตรงกับผู้ผลิตชิปรายเดียว แทนที่จะกระจายไปหลายผู้ให้บริการ — ควรถกในชั้นเรียนเรื่อง vendor lock-in ระดับประเทศ เทียบกับความเร็วในการสร้าง capacity ที่ได้จากการทำงานตรงกับ Nvidia
**ผู้เชี่ยวชาญด้าน AI:** ขนาด 140MW กับ GPU 27,500 ตัวบน DSX platform คือ scale ระดับ national lab ไม่ใช่ enterprise ทั่วไป และการเน้น "physical AI" (หุ่นยนต์ digital twins) มากกว่าภาษา สะท้อนว่า Japan วางกลยุทธ์ AI ให้เชื่อมกับภาคการผลิตและอุตสาหกรรมจริงมากกว่าแข่ง LLM โดยตรง
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ทำงานด้าน robotics/physical AI ในเอเชียควรติดตามโครงการ FRONTia อย่างใกล้ชิด เพราะ open multimodal foundation model ที่จะพัฒนาออกมาอาจเป็นทรัพยากรใหม่สำหรับงาน AI agent, digital twin และ robotics ที่ใช้ได้กว้างกว่าระดับประเทศญี่ปุ่นเพียงอย่างเดียว

## 3. Apple — Apple Intelligence China Launch (Alibaba + Baidu)
**อาจารย์ (มหาวิทยาลัย):** การที่ Apple ต้องพึ่งพาโมเดล AI จากผู้เล่นในประเทศถึงสองราย (Alibaba และ Baidu) เพื่อเข้าตลาดจีน สะท้อนว่าแม้บริษัทระดับโลกก็ต้องปรับตัวตาม regulatory และ localization requirement ของแต่ละตลาด — กรณีนี้เป็นตัวอย่างดีเรื่อง "AI sovereignty" ที่แต่ละประเทศบังคับให้ใช้โมเดลท้องถิ่น
**ผู้เชี่ยวชาญด้าน AI:** การมีพาร์ทเนอร์สองรายพร้อมกัน (ไม่ใช่ exclusive deal) น่าจะสะท้อนว่า Apple ต้องการ hedge ความเสี่ยงด้านคุณภาพโมเดลและ regulatory relationship — น่าติดตามว่าฟีเจอร์ไหนใช้ Qwen ฟีเจอร์ไหนใช้โมเดล Baidu และผลลัพธ์ด้าน user experience จะต่างจากตลาดอื่นที่ใช้โมเดลของ Apple เองแค่ไหน
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่พัฒนาแอปสำหรับตลาดจีนบน iOS ควรเตรียมทดสอบ Apple Intelligence API ที่อาจมีพฤติกรรมต่างจากตลาดสหรัฐฯ/ยุโรป เนื่องจากโมเดล backend ต่างกัน (Qwen/Baidu แทน Apple's own models) — ควรวางแผน QA แยกสำหรับตลาดจีนโดยเฉพาะ

## 4. Meta — Teen Self-Harm Parental Alerts
**อาจารย์ (มหาวิทยาลัย):** ฟีเจอร์นี้เป็นความพยายามสร้างสมดุลระหว่าง privacy ของวัยรุ่นกับความปลอดภัย — ควรถกในชั้นเรียนเรื่อง AI ที่เข้ามาตัดสินใจแทนมนุษย์ในสถานการณ์ high-stakes เช่น self-harm risk และขอบเขตที่เหมาะสมของการแจ้งเตือนผู้ปกครองโดยไม่ทำลายความไว้วางใจของเด็ก
**ผู้เชี่ยวชาญด้าน AI:** การที่ Meta ใช้ AI ระบุการสนทนาเสี่ยงแล้วให้มนุษย์ทวนก่อนแจ้งเตือน (human-in-the-loop) เป็น design pattern ที่ถูกต้องสำหรับงาน high-stakes classification ที่มี false positive/negative cost สูงทั้งคู่ — แต่การเลือก "err on the side of caution" แม้เจตนาจะกำกวม ก็มี tradeoff ด้าน false alarm ที่ต้องบริหารจัดการอย่างรอบคอบ
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่สร้างระบบ content moderation หรือ safety classifier สำหรับ high-stakes use case ควรศึกษาสถาปัตยกรรม "AI flag + human review ก่อนดำเนินการ" ของ Meta เป็นต้นแบบ — โดยเฉพาะการตั้ง threshold ที่ favor sensitivity มากกว่า precision เมื่อผลลัพธ์เกี่ยวข้องกับความปลอดภัยชีวิต

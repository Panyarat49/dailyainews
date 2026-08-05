# Perspectives — 2026-08-05 (ainews)

## 1. Anthropic signs $10B deal with AI cloud startup Volta
**อาจารย์ (มหาวิทยาลัย):** ใช้ดีลนี้สอนเรื่อง vertical stack ของอุตสาหกรรม AI สมัยใหม่ — lab โมเดลไม่ได้ผูกกับ hyperscaler รายเดียวอีกต่อไป แต่กระจายไปหา neocloud รายใหม่ที่ผุดขึ้นเฉพาะสำหรับ workload AI
**ผู้เชี่ยวชาญด้าน AI:** การที่ Bitdeer (บริษัทขุดคริปโต) ผันตัวมาสร้างดาต้าเซ็นเตอร์ AI สะท้อนว่า capacity แย่งชิงหนักจนต้องดึงผู้เล่นนอกวงการมาช่วยสร้าง สัญญา 6 ปีระดับหมื่นล้านยังบ่งชี้ว่า Anthropic วางแผน compute ระยะยาวเกินกว่าจะพึ่ง Azure/AWS อย่างเดียว
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ผูก roadmap กับ Claude API ควรมองดีลนี้เป็นสัญญาณบวกต่อ capacity/availability ในอีก 1-2 ปี แต่ facility ที่นอร์เวย์ยังต้องใช้เวลาก่อสร้าง อย่าคาดหวังผลกระทบต่อ rate limit ทันที

## 2. AMD's data center business is booming while gaming takes a backseat
**อาจารย์ (มหาวิทยาลัย):** ตัวเลข Q2 ของ AMD เป็นกรณีศึกษาชั้นดีเรื่อง revenue mix shift ในบริษัทฮาร์ดแวร์ยุค AI — ธุรกิจเดิม (gaming) หดตัวขณะที่ธุรกิจใหม่ (data center) โตก้าวกระโดดจนกลายเป็นเสาหลักใหม่ของบริษัท
**ผู้เชี่ยวชาญด้าน AI:** การที่ Lisa Su การันตีว่า data center revenue จะโตเกินเท่าตัวอีกครั้งในปี 2027 คือสัญญาณว่า AMD มองเห็น demand จาก MI-series accelerator ต่อเนื่องอย่างน้อยอีก 1-2 ปี ไม่ใช่แค่ไตรมาสนี้
**โปรแกรมเมอร์มืออาชีพ:** ทีม infrastructure ที่พิจารณา AMD Instinct เป็นทางเลือกคู่ Nvidia ควรติดตามว่า supply และ software ecosystem (ROCm) จะตามทันดีมานด์ที่เพิ่มขึ้นนี้หรือไม่ ก่อนวางแผน production migration

## 3. SpaceX made more revenue as an AI company than a space company
**อาจารย์ (มหาวิทยาลัย):** เคสนี้เหมาะสอนเรื่อง diversification ของบริษัทที่ core business เดิมมั่นคงแต่ margin ต่ำ ขณะที่ธุรกิจใหม่ (ให้เช่า compute) โตเร็วกว่าแต่ยังขาดทุนหนัก
**ผู้เชี่ยวชาญด้าน AI:** SpaceX กลายเป็น neocloud โดยพฤตินัยผ่านดีลกับ Anthropic และ Google แข่งขันตรงกับ CoreWeave — สะท้อนว่าใครมีไฟฟ้า/โครงสร้างพื้นฐานเหลือใช้ก็กระโดดเข้าตลาด AI compute ได้ทันที
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ประเมิน compute provider ทางเลือกนอกเหนือจาก AWS/Azure/GCP ควรจับตา SpaceX/Starlink infrastructure เป็นตัวเลือกใหม่ แม้ยังขาดทุนและ track record ด้าน enterprise cloud ยังสั้น

## 4. Perplexity has successfully overturned Amazon's injunction on its AI shopping bot
**อาจารย์ (มหาวิทยาลัย):** คำตัดสินของศาลอุทธรณ์เขต 9 เป็นบรรทัดฐานสำคัญเรื่องขอบเขตกฎหมาย CFAA เมื่อ agent ทำงานแทนผู้ใช้ที่ authorize เอง ไม่ใช่ agent "เจาะระบบ" เอง — ประเด็นนี้เหมาะสอนในวิชากฎหมายเทคโนโลยี
**ผู้เชี่ยวชาญด้าน AI:** คำตัดสินแยกความรับผิดระหว่าง "ผู้ใช้สั่งให้ agent ทำงานแทน" กับ "agent เจาะระบบเอง" ได้ชัดเจน ซึ่งจะเป็นแนวทางสำคัญสำหรับคดี agentic-browsing ในอนาคตที่จะเกิดขึ้นอีกมาก
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่สร้าง AI agent/browser ที่กระทำการแทนผู้ใช้บนเว็บไซต์บุคคลที่สาม ควรศึกษาบรรทัดฐานนี้เพื่อออกแบบ consent flow ให้ชัดว่าผู้ใช้เป็นผู้สั่งการ ลดความเสี่ยงทางกฎหมายแบบเดียวกับที่ Amazon เคยยื่นฟ้อง

## 5. Nvidia doesn't mess around: a week after open AI industry group formed, it's already showing progress
**อาจารย์ (มหาวิทยาลัย):** ความเร็วที่ OSAA ออก working group และ draft proposal ภายในสัปดาห์เดียวเป็นตัวอย่างการทำงานร่วมกันข้ามอุตสาหกรรมแบบเร่งด่วน หลังเกิดเหตุการณ์ความปลอดภัยจริง (OpenAI hack ที่ Hugging Face)
**ผู้เชี่ยวชาญด้าน AI:** กรอบ "confidential incident reporting + blame-free analysis" เลียนแบบโมเดล aviation safety reporting ซึ่งพิสูจน์แล้วว่าได้ผลจริงในอุตสาหกรรมอื่น น่าจับตาว่าจะช่วยลดเหตุการณ์ agent หลุด sandbox ซ้ำได้จริงหรือไม่
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ deploy AI agent ควรติดตามมาตรฐานจาก SAFE working group เพราะ Linux Foundation เป็นผู้ดูแล มีโอกาสสูงที่จะกลายเป็น open standard ที่ tool/library หลักในอนาคตนำไปใช้อ้างอิง

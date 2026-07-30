# สรุปข่าว AI ประจำวันที่ 2026-07-30 — Watchlist

> _หมายเหตุ: WebFetch ถูกบล็อกใน Claude session นี้ แต่ GitHub Actions เข้าถึงบทความฉบับเต็มได้ — การตรวจสอบข่าวรอบนี้ใช้ข้อมูล Tier 1 จากบทความที่ดึงไว้ล่วงหน้าโดย Actions_

> TL;DR
> - Microsoft บันทึกกำไร $3.2B จากการลงทุนใน Anthropic ในไตรมาสล่าสุด พร้อมยืนยันเปิดตัว Copilot "super app" ปีนี้ แต่ก็ถูกสหราชอาณาจักรสอบสวนเรื่องการขึ้นราคา Copilot
> - หุ้น Meta ร่วง 11% หลังงบไตรมาสล่าสุด แม้ Zuckerberg จะยืนยันเดินหน้าทุ่มงบ AI และทำนายว่าคนนับพันล้านจะมี personal AI agent ภายใน 5 ปี
> - Google ยุบทีมวิจัย AlphaFold ที่เคยได้รางวัลโนเบล เพื่อทุ่มทรัพยากรให้ Gemini ขณะเดียวกันก็ขยาย Gemini Spark ไปอินเดีย

## ข่าวเด่น AI ล่าสุด

### 1. Microsoft (MSFT US · Tier 1) — อัปเดตสำคัญ 3 รายการ

**1.1 Microsoft logs $3.2B from Anthropic investment, but OpenAI was a mixed bag — [TechCrunch](https://techcrunch.com/2026/07/29/microsoft-logs-3-2b-from-anthropic-investment-but-openai-was-a-mixed-bag/)**

ผลประกอบการไตรมาสล่าสุดของ Microsoft (ปีงบการเงิน 2026 สิ้นสุด 30 มิ.ย.) เผยว่าบริษัทบันทึกกำไร $3.2 พันล้านจากการลงทุนใน Anthropic ช่วยดันกำไรต่อหุ้นขึ้น 33 เซ็นต์ ตรงข้ามกับการลงทุนใน OpenAI ที่ถูกปรับลดมูลค่าลงราว $600 ล้าน ฉุดกำไรต่อหุ้นลง 7 เซ็นต์ Microsoft ลงทุน $5 พันล้านใน Anthropic เมื่อพฤศจิกายน 2025 ซึ่งผูกกับดีลที่ Anthropic ต้องซื้อบริการ Azure คืนมูลค่า $30 พันล้าน ขณะที่ Microsoft ถือหุ้น OpenAI ราว 27%

ตัวเลขนี้เป็นกรณีศึกษาชั้นดีเรื่อง circular investment ที่ lab ลงทุนแล้วซื้อคลาวด์คืนจากผู้ลงทุนเอง ทำให้ตีความมูลค่าที่แท้จริงยากขึ้น ผลต่างระหว่างสองการลงทุนสะท้อนว่านักลงทุนเริ่มมองความเสี่ยงของสอง lab ต่างกัน และดีล $30 พันล้านที่ผูกกับการลงทุนนี้บ่งชี้ว่า capacity บน Azure ฝั่งโมเดล Claude จะขยายตัวต่อเนื่อง ทีมที่ใช้ Claude API บน Azure ควรติดตามผลกระทบต่อราคาและ availability ในปีหน้า

**1.2 Microsoft confirms Copilot 'super app' coming this year — [The Verge](https://www.theverge.com/tech/972927/microsoft-copilot-super-app-confirmed)**

Satya Nadella ยืนยันในการประชุมผลประกอบการว่า Microsoft กำลังรวม Copilot chat, GitHub Copilot สำหรับเขียนโค้ด และความสามารถ agentic ของ Autopilots เข้าเป็น "super app" เดียวสำหรับทั้งผู้ใช้ทั่วไปและองค์กร โดยจะเปิดตัวภายในปีนี้ ตามหลังรายงานก่อนหน้าของ Fortune ที่ระบุทิศทางเดียวกัน

การรวม chat, coding และ agentic capability ไว้ในแอปเดียวสะท้อนทิศทางที่ AI assistant กำลังเปลี่ยนจากเครื่องมือเฉพาะทางเป็นแพลตฟอร์มรวมศูนย์ และเป็นความพยายามลด friction ระหว่างโหมด "คุย" กับโหมด "ทำงานจริง" ของ agentic AI ที่ผู้ใช้บ่นกันมาก นักพัฒนาที่ใช้ GitHub Copilot อยู่แล้วควรจับตาว่าการรวมเข้า super app จะเปลี่ยน API หรือ licensing ที่ใช้อยู่หรือไม่

**1.3 Microsoft faces competition probe over Copilot subscription price hike — [The Register](https://www.theregister.com/software/2026/07/29/microsoft-faces-competition-probe-over-copilot-subscription-price-hike/5280474)**

หน่วยงานกำกับการแข่งขันของสหราชอาณาจักรเปิดการสอบสวนว่า Microsoft อาจทำให้ลูกค้าเข้าใจผิดหรือไม่ เมื่อเพิ่มฟีเจอร์ Copilot เข้าแพ็กเกจ Microsoft 365 สำหรับผู้บริโภคตั้งแต่มกราคม 2025 แล้วขึ้นราคาตอนต่ออายุสัญญา

กรณีนี้เป็นตัวอย่างเรื่อง consumer protection เมื่อฟีเจอร์ AI ถูก bundle เข้าสินค้าเดิมพร้อมขึ้นราคาโดยผู้บริโภคไม่ยินยอมชัดเจน และอาจกลายเป็นบรรทัดฐานสำหรับบริษัทอื่นที่ทำแบบเดียวกัน ทีมที่ดูแล subscription billing ของผลิตภัณฑ์ที่มีฟีเจอร์ AI ควรตรวจสอบความชัดเจนของการแจ้งราคาและ opt-in/opt-out ให้รัดกุมเพื่อลดความเสี่ยงด้าน regulatory

### 2. Meta Platforms (META US · Tier 1) — อัปเดตสำคัญ 2 รายการ

**2.1 Meta shares fall as frustration grows over AI spending plans — [BBC](https://www.bbc.com/news/articles/ckgd31l5yrdo)**

หุ้น Meta ร่วง 11% หลังผลประกอบการไตรมาส เม.ย.-มิ.ย. แสดงรายได้เติบโต 28% เป็น $61 พันล้าน แต่กำไรลดลง 14% เหลือ $6 พันล้าน ขณะที่บริษัทประกาศเพิ่มงบลงทุน AI ปีนี้เป็น $130-145 พันล้าน (จากเดิม $125 พันล้าน) และกระแสเงินสดอิสระของไตรมาสนี้อยู่ที่เพียง $784 ล้าน ต่ำสุดในรอบอย่างน้อย 5 ปี

ปฏิกิริยาตลาดสะท้อนความตึงเครียดคลาสสิกระหว่าง long-term AI bet กับ short-term profitability ที่นักลงทุนต้องการเห็น กระแสเงินสดที่ลดฮวบเป็นสัญญาณเตือนว่าการลงทุน AI infrastructure ระดับนี้เริ่มกดดันงบดุลจริง แม้ Meta จะยังไม่มีรายได้จากการขาย AI ให้ธุรกิจอื่นเป็นชิ้นเป็นอันตามที่สัญญาไว้ ทีมที่ใช้ Llama หรือโครงสร้างพื้นฐาน AI ของ Meta ควรจับตาว่าแรงกดดันนี้จะกระทบความต่อเนื่องของการลงทุน open-source model หรือไม่

**2.2 Mark Zuckerberg predicts that billions of people will have personal AI agents in five years — [TechCrunch](https://techcrunch.com/2026/07/29/mark-zuckerberg-predicts-that-billions-of-people-will-have-personal-ai-agents-in-five-years/)**

ในการประชุมนักลงทุนไตรมาสเดียวกัน Zuckerberg กล่าวว่าภายใน 5 ปี คนนับพันล้านจะมี personal AI agent ที่ทำงานให้ตลอด 24 ชั่วโมงเพื่อช่วยเรื่องการเงิน สุขภาพ ความสัมพันธ์ และการจัดการบ้าน โดยวาง WhatsApp เป็นช่องทางปฏิสัมพันธ์หลัก เพราะเป็นแพลตฟอร์มที่ผู้ใช้คุยกับ Meta AI มากที่สุดอยู่แล้ว

คำทำนายนี้เป็นตัวอย่างวิธีที่ผู้บริหารใช้ narrative ระยะยาวเพื่อพยุงความเชื่อมั่นนักลงทุนระหว่างช่วงที่ผลตอบแทนจาก AI capex ยังไม่ปรากฏชัดในบัญชี การวาง WhatsApp เป็นแกนหลักสอดคล้องกับฐานผู้ใช้มหาศาลที่ Meta มีอยู่ แต่ยังไม่มีรายละเอียดว่าจะจัดการ privacy และ permission อย่างไรในระดับ 24/7 นักพัฒนาที่สร้างแอปบน WhatsApp Business API ควรเตรียมรับมือกับการเปลี่ยนแปลงด้าน API เมื่อ personal agent เข้ามาเป็นชั้นกลาง

### 3. Alphabet (GOOGL US · Tier 1) — อัปเดตสำคัญ 2 รายการ

**3.1 Google shuts down its Nobel-prize winning AlphaFold project as it focuses on Gemini — [Engadget](https://www.engadget.com/2225849/google-shuts-down-alphafold/)**

ตามรายงานของ Financial Times, Google ได้ยุบทีม AlphaFold ของ DeepMind โดยย้ายบุคลากรหลักและผู้เขียนงานวิจัยดั้งเดิมไปทำงานอื่น ขณะที่บางคนลาออกจากบริษัทไปแล้ว เพื่อทุ่มทรัพยากรไปที่ Gemini แทน ทั้งที่ AlphaFold เคยพาผู้ร่วมก่อตั้ง DeepMind คว้ารางวัลโนเบลจากการทำนายโครงสร้างโปรตีนได้แม่นยำ

การยุบทีมวิจัยระดับโนเบลเพื่อโฟกัส Gemini เป็นกรณีศึกษาที่คมชัดเรื่อง opportunity cost ในองค์กรวิจัย แม้ผลงานจะทรงคุณค่าทางวิทยาศาสตร์ระดับโลกก็ไม่รอดจากการจัดสรรทรัพยากรใหม่ตามทิศทางธุรกิจ การย้ายบุคลากรหลักไปหนุน Gemini อาจกระทบความเร็วการพัฒนา domain-specific breakthroughs ในอนาคต ทีมที่พึ่งพา AlphaFold Database หรือ API ที่เกี่ยวข้องควรติดตามประกาศเรื่อง maintenance และ long-term support

**3.2 Introducing Gemini Spark: Your 24/7 personal AI agent — expanding to India — [Google Blog](https://blog.google/intl/en-in/company-news/technology/introducing-gemini-spark-your-247-personal-ai-agent-in-country/)**

Google ประกาศขยาย Gemini Spark ผู้ช่วย AI ที่ทำงานเบื้องหลังตลอด 24 ชั่วโมง (ขับเคลื่อนด้วย Gemini 3.6 Flash) ไปยังผู้ใช้ Google AI Pro/Ultra ในอินเดีย โดยเชื่อมต่อ Gmail, Docs และ Sheets แบบไม่ต้องตั้งค่าเพิ่ม และจะถามผู้ใช้ก่อนทำ high-stakes action อย่างการจ่ายเงินหรือส่งอีเมล

การขยาย Gemini Spark ไปอินเดียหลังเปิดตัวในสหรัฐฯ ก่อนหน้านี้แสดงกลยุทธ์ scale-by-market ของ Google ที่เลือกตลาดผู้ใช้ AI Pro/Ultra ขนาดใหญ่เป็นลำดับถัดไป จุดที่น่าสนใจทางเทคนิคคือ Spark ทำงาน background แบบ cloud-native ไม่ใช่ local process ซึ่งต้องอาศัย permission model ที่รัดกุม นักพัฒนาที่สร้าง integration กับ Google Workspace ควรศึกษาว่า Spark เข้าถึง API เดียวกับที่เปิดให้ third-party ใช้หรือเป็น internal-only capability

### 4. Nvidia (NVDA US · Tier 1) — อัปเดตสำคัญ 2 รายการ

**4.1 China's Moonshot AI reportedly used Nvidia Blackwell chips for training Kimi K3 — [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-moonshot-ai-reportedly-used-nvidia-blackwell-chips-for-training-kimi-k3-company-circumvented-both-u-s-export-and-chinese-import-controls-to-acquire-compute)**

The Information รายงานโดยอ้างแหล่งข่าวว่า Moonshot AI ของจีนใช้ชิป Nvidia Blackwell ฝึกโมเดล Kimi K3 ทั้งที่ชิปรุ่นนี้ถูกสหรัฐฯ ห้ามส่งออกไปจีน และจีนเองก็มีนโยบายกีดกันการนำเข้าเช่นกัน ผ่านบริษัทจีนสองแห่งที่มี Blackwell ในดาต้าเซ็นเตอร์ของตน พร้อมเช่าเวลาประมวลผลจากคลาวด์ต่างประเทศ และดูเหมือนกำลังหาทาง compute เพิ่มเติมสำหรับ Kimi K4

เคสนี้แสดงข้อจำกัดของนโยบายควบคุมการส่งออกเทคโนโลยีในโลกที่ compute เคลื่อนย้ายข้ามพรมแดนผ่านคลาวด์ได้ง่าย หากเป็นจริง ตัวเลขประสิทธิภาพของ Kimi K3 ที่เคยถูกมองว่าเป็นชัยชนะของโมเดล open-weight บน hardware จำกัด อาจต้องตีความใหม่ เพราะมี compute ระดับ Blackwell หนุนอยู่เบื้องหลัง ทีมที่ประเมินโมเดลจีนอย่าง Kimi สำหรับการใช้งานจริงควรระวังความเสี่ยงด้าน compliance หากมีมาตรการคว่ำบาตรเพิ่มเติมตามมา

**4.2 Nvidia partner ChipAgents raises $60 million to accelerate chip design with AI agents — [CNA / Channel NewsAsia](https://www.channelnewsasia.com/business/nvidia-partner-chipagents-raises-60-million-accelerate-chip-design-ai-agents-6285936)**

ChipAgents สตาร์ทอัพพันธมิตรของ Nvidia ขยายเงินระดมทุนรอบ Series A ด้วย $60 ล้าน เพื่อพัฒนาซอฟต์แวร์ที่ใช้ AI agent เร่งกระบวนการออกแบบและตรวจสอบความถูกต้องของชิป (verification) ซึ่งปกติต้องใช้เวลาและงบประมาณมหาศาลด้วยเครื่องมือดั้งเดิม ตามคำให้สัมภาษณ์ของ William Wang ซีอีโอ

ChipAgents เป็นตัวอย่างที่ดีของการนำ AI agent มาแก้ปัญหาที่ traditional tools ทำได้ช้าและแพง โดยเฉพาะการ verify ว่าชิปทำงานตามที่ออกแบบซึ่งเป็นคอขวดใหญ่ในกระบวนการออกแบบเซมิคอนดักเตอร์ การที่ startup กลุ่มนี้ยังระดมทุนได้ต่อเนื่องสะท้อนว่านักลงทุนยังเชื่อว่า agentic AI สำหรับงาน EDA เป็นตลาดที่มีช่องว่างจริง วิศวกรที่ทำงานด้าน chip verification ควรจับตาเครื่องมือประเภทนี้เป็นทางเลือกเสริม static verification แบบเดิม

## Action items
- **สำหรับอาจารย์/นักเรียน:** ใช้กรณี AlphaFold ถูกยุบทีมและปฏิกิริยาตลาดต่อ Meta capex เป็นเคสสอนเรื่อง opportunity cost และความตึงเครียดระหว่าง long-term AI bet กับ short-term profitability
- **สำหรับผู้เชี่ยวชาญ AI:** ติดตามการยืนยัน/ปฏิเสธเรื่องการใช้ชิป Blackwell ของ Moonshot AI อย่างใกล้ชิด เพราะกระทบการตีความ benchmark ของโมเดล open-weight จีนทั้งหมด และจับตาผลสอบสวน UK ต่อ Copilot bundling ว่าจะเป็นบรรทัดฐานสำหรับตลาดอื่นหรือไม่
- **สำหรับโปรแกรมเมอร์:** ทีมที่ใช้ GitHub Copilot ควรติดตามการเปลี่ยนแปลง API/licensing เมื่อถูกรวมเข้า super app และทีมที่ใช้ Claude API บน Azure ควรเตรียมรับมือความผันผวนของ availability และราคาตามความสัมพันธ์ Microsoft-Anthropic ที่ขยายตัว

## การครอบคลุม watchlist
คัดจาก Tier 1 · บริษัทที่มีข่าวสำคัญวันนี้: Microsoft, Meta Platforms, Alphabet, Nvidia · Tier 2 ไม่ถูกเรียกใช้ (ไม่มีข่าวที่ตรงกับบริษัทใน Tier 2 วันนี้)

---
📊 [ดูการจัดอันดับข่าวทั้งหมด (Excel) / full ranked universe](https://github.com/Panyarat49/dailyainews/blob/main/.github/scripts/output/universe-latest.xlsx) — ทุกข่าวที่คัดมา จัดอันดับด้วยคะแนนความเกี่ยวข้อง พร้อมแท็บแยกตามสตรีมและตามบริษัทใน watchlist

_Generated by the `daily-ai-watchlist` skill on 2026-07-30 (Asia/Bangkok) · model claude-opus-4-8._

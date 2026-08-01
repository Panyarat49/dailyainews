# สรุปข่าว AI ประจำวันที่ 2026-08-01 — Watchlist

> _หมายเหตุ: WebFetch ถูกบล็อกใน Claude session นี้ แต่ GitHub Actions เข้าถึงบทความฉบับเต็มได้ — การตรวจสอบข่าวรอบนี้ใช้ข้อมูล Tier 1 จากบทความที่ดึงไว้ล่วงหน้าโดย Actions_

> TL;DR
> - Amazon เผยธุรกิจชิปกำหนดเอง (Trainium/Graviton) ทะลุ $25 พันล้านต่อปี เติบโตสามหลักต่อเนื่อง หลังลงทุนมาสิบปี
> - Google ถอนฟีเจอร์สร้างภาพ AI ใน Google Earth หลังใช้งานเพียงวันเดียว จากความกังวลเรื่องข้อมูลบิดเบือน
> - Moonshot ผู้สร้าง Kimi K3 เข้าถึง Nvidia chip cluster 20,000 ตัวผ่านดีลคอมพิวต์กับ Alibaba สะท้อนช่องโหว่มาตรการควบคุมส่งออกชิป

## ข่าวเด่น AI ล่าสุด

### 1. Amazon (AMZN US · Tier 1) — How Amazon became one of the world's top chip companies in a decade — [aboutamazon.com](https://www.aboutamazon.com/news/aws/amazon-ai-chips-business-history)

ธุรกิจชิปออกแบบเองของ Amazon ซึ่งครอบคลุมทั้ง Trainium (สำหรับ training/inference AI) และ Graviton (คอมพิวต์ทั่วไปบนคลาวด์) เพิ่งทะลุ run rate รายได้ต่อปี 25,000 ล้านดอลลาร์ เติบโตระดับสามหลักเมื่อเทียบปีต่อปี Trainium3 ให้ price-performance ดีขึ้นถึง 40% จาก Trainium2 ขณะที่ Graviton ให้บริการลูกค้า EC2 รายใหญ่ที่สุด 1,000 รายถึง 98% จุดเริ่มต้นย้อนไปสิบปีก่อนเมื่อ Amazon ซื้อบริษัทออกแบบชิป Annapurna Labs ในปี 2015 — ตอนนั้นกระแส AI boom ยังไม่มา

ตัวเลข $25 พันล้าน run-rate จากธุรกิจชิปที่เริ่มจากการซื้อ Annapurna Labs เมื่อสิบปีก่อน เป็นกรณีศึกษาชั้นดีของ vertical integration ระยะยาว — การลงทุนวิจัยฮาร์ดแวร์ที่ดูเสี่ยงในวันนั้นกลายเป็นความได้เปรียบเชิงต้นทุนที่จับต้องได้ในวันนี้ ตัวเลข Trainium3 และ Graviton ที่ครองส่วนแบ่งลูกค้ารายใหญ่สะท้อนว่า Amazon กำลังลด dependency ต่อ Nvidia อย่างเป็นระบบด้วยชิปที่ออกแบบเฉพาะ workload ของตัวเอง ซึ่งสำคัญมากขึ้นเรื่อยๆ ในยุคที่ GPU ขาดตลาด ทีมที่รัน workload บน AWS ควรประเมิน Trainium/Bedrock เทียบกับ instance ที่ใช้ Nvidia อย่างจริงจัง โดยเฉพาะงาน inference ขนาดใหญ่ที่ต้นทุนต่อ token สำคัญ

### 2. Alphabet (GOOGL US · Tier 1) — Alphabet rolls back AI image generation in Google Earth over policy violations — [Channel NewsAsia](https://www.channelnewsasia.com/business/alphabet-rolls-back-ai-image-generation-in-google-earth-over-policy-violations-6292226)

Google ถอนฟีเจอร์สร้างภาพด้วย AI ที่เพิ่งเปิดตัวใน Google Earth ออกทันที หลังใช้งานได้เพียงวันเดียว เนื่องจากผู้ใช้แชร์ภาพที่ดูเหมือนละเมิดนโยบายของบริษัท ฟีเจอร์นี้ขับเคลื่อนด้วยโมเดล Nano Banana 2 ของ Google ที่ให้ผู้ใช้สร้างภาพสมจริงบนพื้นฐานข้อมูลดาวเทียมจริงของ Google Earth

การที่ Google ต้องถอนฟีเจอร์ AI ออกภายใน 24 ชั่วโมงหลังเปิดตัว เป็นตัวอย่างสอนเรื่อง pre-launch risk assessment ที่พลาดไป — ควรตั้งคำถามว่ากระบวนการ red-team/policy review ก่อนปล่อยฟีเจอร์ generative AI ที่กระทบข้อมูลภูมิศาสตร์ที่ดูน่าเชื่อถือควรเข้มงวดกว่าฟีเจอร์ทั่วไปแค่ไหน โมเดลที่สร้างภาพสมจริงบนพื้นฐานข้อมูลดาวเทียมจริงมี "ความน่าเชื่อถือเชิงภูมิศาสตร์" สูงกว่า image generator ทั่วไปมาก ทำให้ความเสี่ยงด้าน misinformation รุนแรงกว่าเดิม และเป็นเหตุผลที่ Google ต้องตัดสินใจถอนเร็วผิดปกติ ทีมที่กำลังสร้างฟีเจอร์ generative AI บนข้อมูล location/mapping ควรถอดบทเรียนนี้ทันที ทั้งการ label ผล output ที่สร้างจาก AI อย่างชัดเจน และเตรียม kill-switch พร้อม rollback ให้เร็วเมื่อ policy violation เริ่มปรากฏ

### 3. Nvidia (NVDA US · Tier 1) — Moonshot's Kimi Built on 20,000 Nvidia Chip Cluster From Alibaba — [Reuters](https://www.reuters.com/business/retail-consumer/moonshot-has-nvidia-chip-cluster-alibaba-computing-deal-bloomberg-news-reports-2026-07-31/)

Moonshot บริษัท AI จีนผู้สร้างโมเดล Kimi K3 มีข้อตกลงด้านคอมพิวต์กับ Alibaba สำหรับใช้งานชิป Nvidia ราว 20,000 ตัว ตามรายงานของ Bloomberg โดย Moonshot ยังเข้าถึงชิป Blackwell รุ่นใหม่ของ Nvidia ผ่านช่องทางในเอเชียตะวันออกเฉียงใต้ และกำลังหาคอมพิวต์เพิ่มสำหรับโมเดลรุ่นถัดไป สะท้อนว่าจีนยังคงพึ่งพาฮาร์ดแวร์ตะวันตกในการพัฒนา AI ต่อเนื่อง

กรณีนี้ตอกย้ำว่ามาตรการควบคุมการส่งออกชิปยังมีช่องโหว่เชิงโครงสร้าง — บริษัทจีนเข้าถึงชิป Nvidia ผ่านตัวกลางอย่าง Alibaba และช่องทางเอเชียตะวันออกเฉียงใต้ เหมาะเป็นกรณีศึกษาเรื่องช่องว่างระหว่างนโยบายกับ supply chain โลกที่เชื่อมโยงกันซับซ้อน การที่ Kimi K3 ทำผลงานแซง Qwen ของ Alibaba เอง ทั้งที่ใช้ทรัพยากรคอมพิวต์ใกล้เคียงกัน ยังเป็นสัญญาณว่าความได้เปรียบด้าน AI ในจีนกำลังเปลี่ยนจาก "ใครมีชิปเยอะกว่า" ไปสู่ "ใครออกแบบสถาปัตยกรรมได้ฉลาดกว่า" ทีมที่ประเมิน exposure ต่อ Nvidia ในพอร์ต hardware หรือ cloud vendor ควรติดตามว่าความต้องการชิปจากแล็บจีนที่หาทางเลี่ยงข้อจำกัดส่งออกจะยิ่งเพิ่มแรงกดดันด้าน supply/ราคาต่อ Nvidia GPU ทั่วโลกหรือไม่

## Action items
- **สำหรับอาจารย์/นักเรียน:** ใช้กรณี Google Earth AI rollback เป็นเคสสอนเรื่อง pre-launch policy review สำหรับฟีเจอร์ generative AI ที่กระทบข้อมูลที่ดูน่าเชื่อถือ
- **สำหรับผู้เชี่ยวชาญ AI:** ติดตามพัฒนาการของโมเดลจีน (Kimi K3 vs Qwen) ที่ได้เปรียบจาก architecture/data pipeline มากกว่าปริมาณคอมพิวต์ดิบ
- **สำหรับโปรแกรมเมอร์:** ประเมิน Trainium/Bedrock ของ Amazon เทียบกับ instance ที่ใช้ Nvidia สำหรับ workload inference ขนาดใหญ่ เพื่อลดต้นทุนต่อ token

## การครอบคลุม watchlist
คัดจาก Tier 1 · บริษัทที่มีข่าวสำคัญวันนี้: Amazon, Alphabet, Nvidia · Tier 2 ไม่ถูกเรียกใช้ (ค้นหาเพิ่มใน TSMC, Palantir, Micron แล้วแต่ไม่พบข่าวที่ผ่านเกณฑ์แหล่งข่าว/ความสดใหม่)

---
📊 [ดูการจัดอันดับข่าวทั้งหมด (Excel) / full ranked universe](https://github.com/Panyarat49/dailyainews/blob/main/.github/scripts/output/universe-latest.xlsx) — ทุกข่าวที่คัดมา จัดอันดับด้วยคะแนนความเกี่ยวข้อง พร้อมแท็บแยกตามสตรีมและตามบริษัทใน watchlist

_Generated by the `daily-ai-watchlist` skill on 2026-08-01 (Asia/Bangkok) · model claude-opus-4-8._

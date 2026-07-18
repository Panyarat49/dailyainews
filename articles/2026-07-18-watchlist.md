# สรุปข่าว AI ประจำวันที่ 2026-07-18 — Watchlist

> _หมายเหตุ: WebFetch ถูกบล็อกใน Claude session นี้ แต่ GitHub Actions เข้าถึงบทความฉบับเต็มได้ — การตรวจสอบข่าวรอบนี้ใช้ข้อมูล Tier 1 จากบทความที่ดึงไว้ล่วงหน้าโดย Actions_

> TL;DR
> - Apple แซง Nvidia ขึ้นเป็นบริษัทมูลค่าสูงสุดในโลกชั่วคราว ก่อน Nvidia จะดึงตำแหน่งกลับมาได้ก่อนปิดตลาด ท่ามกลางความกังวลผลตอบแทนการลงทุน AI
> - Nvidia เผยแพร่บล็อกเทคนิคเรื่องสถาปัตยกรรม Vera Rubin ที่เน้นลดต้นทุนต่อโทเคนสำหรับงาน post-training ต่อเนื่องในยุค agentic AI
> - Meta เจรจาดีลปล่อยเช่าศูนย์ข้อมูลมูลค่าอาจสูงถึง $10,000 ล้านให้ Anthropic ขณะที่ Apple และ Google ถูกซานฟรานซิสโกสั่งลบแอป AI "nudify" ออกจากสโตร์

## ข่าวเด่น AI ล่าสุด

### 1. Nvidia (NVDA US · Tier 1) — อัปเดตสำคัญ 2 รายการ

**1.1 Apple briefly overtakes Nvidia as world's most valuable company amid AI investment doubts — [Fox Business](https://www.foxbusiness.com/markets/apple-briefly-overtakes-nvidia-worlds-most-valuable-company-amid-ai-investment-doubts)**

Apple แซงหน้า Nvidia ขึ้นเป็นบริษัทมูลค่าสูงสุดในโลกชั่วคราวในวันศุกร์ หลังหุ้นกลุ่มชิปร่วงจากความกังวลว่าการลงทุน AI infrastructure มหาศาลจะให้ผลตอบแทนทันเวลาหรือไม่ มูลค่าตลาดของ Apple ขึ้นไปแตะกว่า $4.91 ล้านล้าน สูงกว่า Nvidia ที่ $4.9 ล้านล้านในขณะนั้น ก่อนที่หุ้น Apple จะย่อตัวลงบางส่วนจนทำให้ Nvidia ดึงตำแหน่งกลับมาได้ก่อนตลาดปิด

การที่ตำแหน่งบริษัทมูลค่าสูงสุดสลับมือกันภายในวันเดียวเป็นตัวอย่างชั้นดีของความผันผวนที่เกิดจาก narrative มากกว่าปัจจัยพื้นฐาน เหมาะใช้สอนเรื่อง market psychology และ concentration risk เมื่อมูลค่าอุตสาหกรรมทั้งหมดผูกกับสมมติฐานเรื่องผู้นำ AI compute การที่ Nvidia ดึงตำแหน่งกลับมาได้ก่อนปิดตลาดแสดงว่าความกังวลเรื่อง AI ROI ยังไม่ได้เปลี่ยนโครงสร้างดีมานด์ GPU จริง เป็นแค่ sentiment shift ระยะสั้น ต้องติดตามว่าความกังวลนี้จะกลายเป็นแรงกดดันต่อเนื่องหรือเป็นแค่ noise รายวัน ทีมที่ผูก budget โครงการกับราคาหุ้นหรือ credit ของ Nvidia รายเดียวควรมี contingency plan ไว้ล่วงหน้า

**1.2 NVIDIA Vera Rubin Maximizes Intelligence per Dollar for Post-Training Workloads — [NVIDIA Blog](https://blogs.nvidia.com/blog/nvidia-vera-rubin-post-training-intelligence-per-dollar/)**

Nvidia เผยแพร่บล็อกเทคนิคอธิบายว่าแพลตฟอร์ม Vera Rubin ถูกออกแบบมาเพื่อลดต้นทุนต่อโทเคนสำหรับ post-training ต่อเนื่อง ซึ่งเป็นรูปแบบการใช้ compute ที่ Nvidia ระบุว่าครองสัดส่วนหลักในยุค "agentic AI" ที่โมเดลต้องถูกปรับแต่งซ้ำ ๆ ตาม feedback จากการใช้งานจริง แทนที่จะฝึกครั้งเดียวจบเหมือนโมเดล generative ทั่วไป

การเปลี่ยนกรอบคิดจาก "training ครั้งเดียวแล้วจบ" ไปสู่ "post-training ต่อเนื่องตลอดเวลา" เป็นเนื้อหาที่ควรใส่ในหลักสูตร AI systems สมัยใหม่ เพราะมันเปลี่ยนทั้งวิธีคิดเรื่อง compute budgeting และ lifecycle ของโมเดลในการใช้งานจริง การที่ Nvidia ชู "intelligence per dollar" แทน raw FLOPS เป็นสัญญาณว่าตลาด AI infrastructure กำลังโตเข้าสู่ยุคที่ cost-efficiency ต่อ token สำคัญกว่าพลังดิบ โดยเฉพาะสำหรับ agentic AI ที่ต้อง post-train ต่อเนื่องจาก production feedback ตลอดเวลา ทีมที่ build agentic AI ใน production ควรวางแผน compute budget แบบ continuous post-training loop ตั้งแต่ต้น เพราะ cost ต่อ token ของรอบ fine-tune ซ้ำ ๆ จะกลายเป็นตัวแปรหลักของ TCO มากกว่า inference เดี่ยว ๆ

### 2. Meta Platforms (META US · Tier 1) — Meta is reportedly considering a multibillion-dollar data center deal with Anthropic — [Engadget](https://www.engadget.com/2217904/meta-is-reportedly-considering-a-multibillion-dollar-data-center-deal-with-anthropic/)

ตามรายงานของ New York Times, Meta อยู่ระหว่างเจรจาขั้นต้นเพื่อปล่อยเช่า capacity ศูนย์ข้อมูลบางส่วนให้ Anthropic ในดีลที่อาจมีมูลค่าสูงถึง $10,000 ล้านตลอด 2 ปี ต่อยอดจากรายงานก่อนหน้าของ Bloomberg ที่ระบุว่า Meta กำลังมองหาช่องทางเข้าสู่ธุรกิจ cloud services ซึ่งจะเป็นธุรกิจใหม่ทั้งหมดสำหรับ Meta ที่รายได้หลักมาจากโฆษณา ท่ามกลางแผนใช้จ่ายด้าน AI data center ของ Meta ที่คาดการณ์ไว้ $125,000-145,000 ล้านในปี 2026

ดีลนี้ท้าทายกรอบคิดเดิมที่มองบริษัท AI เป็นคู่แข่งกันตายตัว เพราะในความเป็นจริงห่วงโซ่ compute ทำให้แม้คู่แข่งก็ยังต้องพึ่งพากันเชิงโครงสร้าง เหมาะเป็นกรณีศึกษาเรื่อง coopetition ในอุตสาหกรรมเทคโนโลยี การที่ Meta ซึ่งลงทุนสร้าง data center มหาศาลเพื่อโมเดลของตัวเอง หันมาปล่อยเช่า capacity ให้ Anthropic สะท้อนว่าอุปทาน compute เริ่มเกินความต้องการของ Meta เอง หรือ Meta มองเห็นโอกาสธุรกิจใหม่ที่ทำกำไรได้เร็วกว่าการพัฒนาโมเดลของตัวเองในระยะสั้น หากดีลนี้เกิดขึ้นจริง อาจหมายถึง capacity คลาวด์ AI ใหม่เข้าสู่ตลาดในระยะ 1-2 ปีข้างหน้าซึ่งอาจกดราคา inference/training ลง ทีม engineering ที่วางแผนงบ compute ระยะยาวควรติดตามความคืบหน้าดีลนี้ก่อนล็อกสัญญาระยะยาวกับผู้ให้บริการรายเดียว

### 3. Alphabet (GOOGL US · Tier 1) — Apple and Google ordered to purge 'nudify' apps from App Stores — [TechCrunch](https://techcrunch.com/2026/07/17/apple-and-google-ordered-to-purge-nudify-apps-from-app-stores/)

ซานฟรานซิสโกสั่งให้ Apple และ Google ลบแอป "nudify" หลายสิบแอปที่ใช้ AI ดัดแปลงภาพให้ดูเหมือนถอดเสื้อผ้าคนในภาพออกจากแอปสโตร์ อัยการเมือง David Chiu ระบุว่าทั้งสองบริษัทรับรู้ปัญหานี้มาเกือบปีแล้วแต่ยังปล่อยให้แอปเหล่านี้สร้างรายได้อยู่ ทั้งที่กฎหมายแคลิฟอร์เนียกำหนดให้การสร้าง deepfake ภาพโป๊เปลือยแบบไม่ยินยอมเป็นความผิดทางอาญา

กรณีนี้เป็นตัวอย่างชัดเจนของช่องว่างระหว่างความสามารถ generative AI กับความรับผิดชอบของแพลตฟอร์มที่โฮสต์แอป เหมาะใช้สอนเรื่อง platform liability และจริยธรรมของการอนุญาตแอปที่มีความเสี่ยงสูงต่อการละเมิดสิทธิ แม้จะมีกฎหมายรองรับแล้วก็ตาม การที่ทั้ง Apple และ Google รับรู้ปัญหานี้มาเกือบปีแล้วแต่ยังปล่อยให้แอปเหล่านี้อยู่ในสโตร์ สะท้อนข้อจำกัดของระบบ content moderation อัตโนมัติที่ตรวจจับแอป AI-generated deepfake ได้ไม่ทันหรือไม่ครบถ้วน จำเป็นต้องมี human review process ที่เข้มงวดกว่าเดิมสำหรับแอปหมวดนี้โดยเฉพาะ ทีมที่ดูแล app review หรือ trust & safety สำหรับแพลตฟอร์มที่มี AI-generated content ควรทบทวน detection pipeline สำหรับแอปประเภทนี้โดยเฉพาะ เพราะกฎระเบียบด้าน non-consensual deepfake กำลังเข้มงวดขึ้นเรื่อย ๆ ทั่วโลก การตั้งรับหลังถูกสั่งจากหน่วยงานรัฐมีต้นทุนสูงกว่าการป้องกันเชิงรุก

## Action items
- **สำหรับอาจารย์/นักเรียน:** ใช้เคส Apple แซง Nvidia ชั่วคราวเป็นกรณีศึกษาสอนเรื่อง concentration risk และวิธีที่ narrative ตลาดเปลี่ยนราคาสินทรัพย์ได้เร็วกว่าปัจจัยพื้นฐาน
- **สำหรับผู้เชี่ยวชาญ AI:** ติดตามความคืบหน้าดีล Meta-Anthropic เพราะหากเกิดขึ้นจริงจะเพิ่ม capacity คลาวด์ AI ใหม่เข้าสู่ตลาดและอาจกดราคา inference/training ลงในระยะ 1-2 ปี
- **สำหรับโปรแกรมเมอร์:** ทีมที่ดูแล trust & safety หรือ content moderation สำหรับแพลตฟอร์มแอปควรทบทวน detection pipeline สำหรับแอป AI-generated deepfake โดยเฉพาะ ก่อนถูกหน่วยงานรัฐสั่งให้ตั้งรับ

## การครอบคลุม watchlist
คัดจาก Tier 1 · บริษัทที่มีข่าวสำคัญวันนี้: Nvidia, Meta Platforms, Alphabet · Tier 2 ไม่ถูกเรียกใช้ (ไม่มีผู้สมัคร Tier 2 ในพูลวันนี้ และค้นหาเพิ่มเติมสำหรับ AMD, Microsoft, Oracle, Tesla, Amazon, Alibaba ไม่พบข่าวใหม่ที่ผ่านเกณฑ์ — ข่าว Alibaba/Qwen ที่พบซ้ำกับที่รายงานไปแล้วในบรีฟวันที่ 15-16 กรกฎาคม จึงไม่นับรวม ทำให้บรีฟวันนี้มี 3 เรื่องแทนที่จะเป็น 4-5)

---
📊 [ดูการจัดอันดับข่าวทั้งหมด (Excel) / full ranked universe](https://github.com/Panyarat49/dailyainews/blob/main/.github/scripts/output/universe-latest.xlsx) — ทุกข่าวที่คัดมา จัดอันดับด้วยคะแนนความเกี่ยวข้อง พร้อมแท็บแยกตามสตรีมและตามบริษัทใน watchlist

_Generated by the `daily-ai-watchlist` skill on 2026-07-18 (Asia/Bangkok) · model claude-opus-4-8._

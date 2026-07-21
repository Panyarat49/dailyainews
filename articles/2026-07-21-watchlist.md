# สรุปข่าว AI ประจำวันที่ 2026-07-21 — Watchlist

> _หมายเหตุ: WebFetch ถูกบล็อกใน Claude session นี้ แต่ GitHub Actions เข้าถึงบทความฉบับเต็มได้ — การตรวจสอบข่าวรอบนี้ใช้ข้อมูล Tier 1 จากบทความที่ดึงไว้ล่วงหน้าโดย Actions_

> TL;DR
> - Google กำลังพัฒนาชิป "Frozen v2" เจาะจงรัน Gemini โดยเฉพาะ อ้างประสิทธิภาพดีขึ้น 6-10 เท่า คาดวางจำหน่ายปี 2028
> - Microsoft ประกาศนำ AMD Helios rack-scale AI accelerator ขึ้น Azure "ระดับสเกลใหญ่" ท้าทายการผูกขาดของ Nvidia
> - Alibaba เปิดตัว Qwen 3.8 ขนาด 2.4 ล้านล้านพารามิเตอร์ อ้างเป็นรองแค่ Claude Fable 5 เท่านั้น

## ข่าวเด่น AI ล่าสุด

### 1. Alphabet (GOOGL US · Tier 1) — Google กำลังพัฒนาชิป "Frozen v2" เจาะจงรัน Gemini — [TechCrunch](https://techcrunch.com/2026/07/20/google-is-working-on-a-new-ai-chip-designed-to-make-gemini-more-efficient/)
Alphabet กำลังออกแบบชิปเซิร์ฟเวอร์รุ่นใหม่ ชื่อภายในว่า "Frozen v2" ให้เข้ากับสถาปัตยกรรมโมเดล Gemini โดยเฉพาะ ตามรายงานของ The Information ที่อ้างแหล่งข่าวนิรนาม ระบุว่าอาจมีประสิทธิภาพดีขึ้น 6-10 เท่าเทียบกับชิป AI ปัจจุบันของ Google คาดวางจำหน่ายราวปี 2028 โดย Google ยังไม่ยืนยันหรือปฏิเสธอย่างเป็นทางการ แนวโน้มที่ AI lab ใหญ่ออกแบบฮาร์ดแวร์เฉพาะให้เข้ากับสถาปัตยกรรมโมเดลของตัวเอง (hardware/software co-design) กำลังกลายเป็นความได้เปรียบเชิงแข่งขันหลักของ lab ระดับบนสุดที่ควบคุมทั้ง stack ตัวเลขอ้างว่าเร็วกว่าเดิม 6-10 เท่าน่าตื่นเต้นมาก แต่ยังเป็นเพียงรายงานจากแหล่งข่าวนิรนามที่ต้องรอรายละเอียดสถาปัตยกรรมจริงก่อนประเมินความน่าเชื่อถือ นักพัฒนาที่ใช้ Gemini API ควรมองข่าวนี้เป็นสัญญาณว่าค่าใช้จ่ายต่อ token ของ Gemini อาจถูกลงมากในระยะ 2-3 ปีข้างหน้า ควรวางแผน cost modeling ระยะยาวให้สอดคล้อง

### 2. Microsoft (MSFT US · Tier 1) — Azure ขยายโครงสร้าง AI/HPC ด้วย AMD Helios "ระดับสเกลใหญ่" — [Microsoft Official Blog](https://blogs.microsoft.com/blog/2026/07/20/microsoft-expands-azure-ai-and-hpc-infrastructure-with-amd/)
Microsoft ประกาศอย่างเป็นทางการผ่าน official blog ว่าจะนำแพลตฟอร์ม Helios ของ AMD ซึ่งประกอบด้วยชิป Radeon Instinct MI455X และ CPU Epyc Venice มาให้บริการบน Azure ในระดับ "at scale" เพื่อรองรับ workload agentic AI ที่ growing เร็ว โดย Scott Guthrie (EVP, Cloud + AI) เป็นผู้ประกาศ แม้ยังไม่เปิดเผยตัวเลขปริมาณ compute ที่สั่งซื้อจริง ดีลนี้เป็นตัวอย่างชัดเจนของ multi-vendor strategy ในตลาด AI infrastructure — cloud รายใหญ่ไม่มีใครยอมพึ่ง GPU vendor เดียวอีกต่อไป การที่ Microsoft ประกาศเองผ่าน official blog (ไม่ใช่แค่ leak) สะท้อนความมั่นใจในดีลนี้ MI455X และ Epyc Venice ถูกออกแบบมาชนกับ Nvidia โดยตรงในระดับ rack-scale ไม่ใช่แค่ชิปเดี่ยว ทีมที่รัน workload บน Azure AI ควรจับตา instance type ใหม่ที่ใช้ MI455X เพราะราคาต่อ FLOP อาจถูกกว่า H100/B200 อย่างมีนัยสำคัญ แต่ต้องทดสอบ compatibility ของ framework (ROCm เทียบกับ CUDA) ก่อน migrate workload จริง

### 3. Nvidia (NVDA US · Tier 1) — AMD Helios ผงาดเป็นคู่แข่ง rack-scale รายแรก, Microsoft เข้าร่วมเป็นลูกค้า — [CNBC](https://www.cnbc.com/2026/07/20/amd-helios-microsoft-ai-nvidia.html)
AMD เปิดตัว Helios ระบบ AI ระดับ rack-scale ตัวแรกที่ท้าทาย Nvidia Vera Rubin โดยตรง พร้อมประกาศ Microsoft เป็นลูกค้ารายล่าสุดต่อจาก Meta, OpenAI และ Oracle ที่ใช้งานอยู่แล้ว กรณีนี้เหมาะสอนเรื่อง competitive dynamics ในตลาดผูกขาดบางส่วน (oligopoly) — เมื่อคู่แข่งเริ่มมีผลิตภัณฑ์ระดับเทียบเท่าและดึงลูกค้ารายใหญ่ได้ ตลาดที่เคย concentrate มากจะเริ่มกระจายตัว Helios คือความพยายามครั้งแรกของ AMD ที่ทำ rack-scale system เทียบชั้น Nvidia ไม่ใช่แค่ระดับชิป GPU เดี่ยวเหมือนที่ผ่านมา การที่ Microsoft เข้าร่วมเป็นลูกค้าเป็นสัญญาณว่า hyperscaler เริ่มกระจายความเสี่ยงด้าน supply จาก Nvidia อย่างจริงจัง ทีมที่วางแผน infrastructure ระยะยาวควรเริ่มประเมิน portability ของ workload ระหว่าง CUDA และ ROCm ตั้งแต่ตอนนี้ เพราะตลาด GPU/accelerator กำลังจะมีทางเลือกที่ใช้งานจริงได้มากขึ้นในอีก 1-2 ปีข้างหน้า

### 4. Alibaba (BABA US · Tier 1) — เปิดตัว Qwen 3.8 อ้างเป็นรองแค่ Claude Fable 5 — [Livemint](https://www.livemint.com/ai/artificial-intelligence/after-kimi-k3-alibaba-unveils-qwen-3-8-claims-its-second-only-to-claude-fable-5-11784530852451.html)
Alibaba เปิดตัว Qwen 3.8 โมเดลขนาด 2.4 ล้านล้านพารามิเตอร์ ตามหลังการเปิดตัว Kimi K3 ของ Moonshot AI โดยอ้างว่ามีความสามารถเป็นรองเพียง Claude Fable 5 เท่านั้น และมีแผนจะเปิด open-weight ในอนาคต การที่ Alibaba ประกาศ Qwen 3.8 ด้วยขนาดพารามิเตอร์เท่ากับ Kimi K3 พอดีสะท้อนว่าห้องแล็บจีนกำลังแข่งขันกันเองที่ scale เดียวกันเพื่อไล่ตาม frontier lab ตะวันตก การอ้างว่าเป็นรองเพียง Claude Fable 5 โดยไม่เปิดเผยผลทดสอบเทียบมาตรฐานที่ตรวจสอบได้เป็นจุดที่ควรตั้งคำถามก่อนเชื่อ ต้องรอผู้ทดสอบอิสระยืนยัน แผนเปิด open-weight ในอนาคตอาจเป็นปัจจัยสำคัญกว่าตัวเลข benchmark ที่ยังพิสูจน์ไม่ได้ ทีมที่ใช้โมเดลเปิดจากจีนใน production ควรเตรียมทดสอบ Qwen 3.8 เทียบกับ Kimi K3 และ GLM เมื่อเปิด weight จริง เพราะการแข่งขันด้านราคาที่ดุเดือดขึ้นอาจทำให้ต้นทุน inference ถูกลงต่อเนื่อง แต่ควรตรวจสอบคุณภาพและ SLA ก่อนย้าย workload จริง

## Action items
- **สำหรับอาจารย์/นักเรียน:** ใช้กรณี Frozen v2 และ AMD Helios เป็นตัวอย่างสอนเรื่อง hardware/software co-design และ multi-vendor supply chain strategy ในอุตสาหกรรม AI
- **สำหรับผู้เชี่ยวชาญ AI:** ติดตามผลทดสอบอิสระของ Qwen 3.8 เทียบกับ Claude Fable 5 ก่อนเชื่อคำกล่าวอ้างอันดับที่ Alibaba ยังไม่เปิดเผยตัวเลขเทียบมาตรฐาน
- **สำหรับโปรแกรมเมอร์:** ประเมิน portability ของ workload ระหว่าง CUDA และ ROCm ล่วงหน้า เตรียมรับมือ instance type ใหม่บน Azure ที่ใช้ AMD MI455X

## การครอบคลุม watchlist
คัดจาก Tier 1 · บริษัทที่มีข่าวสำคัญวันนี้: Alphabet, Microsoft, Nvidia, Alibaba · Tier 2 ไม่ถูกเรียกใช้

---
📊 [ดูการจัดอันดับข่าวทั้งหมด (Excel) / full ranked universe](https://github.com/Panyarat49/dailyainews/blob/main/.github/scripts/output/universe-latest.xlsx) — ทุกข่าวที่คัดมา จัดอันดับด้วยคะแนนความเกี่ยวข้อง พร้อมแท็บแยกตามสตรีมและตามบริษัทใน watchlist

_Generated by the `daily-ai-watchlist` skill on 2026-07-21 (Asia/Bangkok) · model claude-opus-4-8._

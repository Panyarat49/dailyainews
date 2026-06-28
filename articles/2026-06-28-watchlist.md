# สรุปข่าว AI ประจำวันที่ 2026-06-28 — Watchlist

> _หมายเหตุ: รอบนี้ตรวจสอบข่าวจากฟีด RSS พร้อม body_text ที่ GitHub Actions ดึงล่วงหน้า (12 รายการ enriched) เนื่องจาก WebFetch ถูกบล็อกในรอบนี้_

> TL;DR
> - **Apple เผชิญสามแรงกระแทกจาก AI RAM Shortage พร้อมกัน** — VP Vision Pro ลาออกไป OpenAI, ราคา Mac/iPad ขึ้น 15–25%, ล็อบบี้ขอซื้อชิปจากบริษัทจีนที่ถูก Pentagon แบน
> - **Tesla ยอมความคดี FSD ผู้เสียชีวิตทางเท้ารายแรก** — การยอมความโดยไม่เปิดเผยเงื่อนไขสะท้อน pattern ที่ Tesla เลือก settle แทนต่อสู้คดี ขณะ NHTSA ยังสอบสวนอิสระต่อ
> - **AMD ปล่อย FSR Upscaling 4.1 ให้ Radeon RX 7000 ก่อนกำหนด** — ขยาย ML upscaling จากเฉพาะ RDNA 4 สู่ RDNA 3 ทั้งหมด

## ข่าวเด่น Watchlist ล่าสุด

### 1. Apple (AAPL · Tier 1) — อัปเดตสำคัญ 3 รายการ

**1.1 Paul Meade VP Vision Pro ลาออกไปร่วม OpenAI Hardware Team — [TechCrunch](https://techcrunch.com/2026/06/27/apple-vision-pro-exec-is-reportedly-leaving-for-openai/)**

Paul Meade รองประธาน Apple ผู้ดูแล Vision Pro headset และ AI smart glasses รุ่นที่ Apple วางแผนเปิดตัวปีหน้า ออกไปร่วม OpenAI hardware team ตาม Bloomberg's Mark Gurman การออกเป็น byproduct ของ John Ternus ที่กำลังขึ้นเป็น Apple CEO และปรับโครงสร้าง hardware engineering team ที่ทำให้ VP บางส่วนรู้สึกถูกลด rank OpenAI ทำงานร่วมกับ Jony Ive อดีต Chief Design Officer ของ Apple บน AI device ที่ CEO Sam Altman บอกว่าจะ "peaceful and calm กว่า iPhone"

นักวิชาการมองว่า Meade ไม่ได้นำแค่ประสบการณ์ hardware ออกไป แต่นำ product roadmap knowledge ด้าน AI wearables ที่ Apple วางแผนสู่ตลาดใน 12 เดือนถัดไปออกไปด้วย — competitive intelligence ที่ OpenAI จะใช้ประโยชน์ได้โดยตรงในการออกแบบ AI device กับ Jony Ive ผู้เชี่ยวชาญ AI ชี้ว่า Meade รู้ Apple's exact next move ด้าน spatial computing ซึ่งมีค่ากว่าการ hire engineer ทั่วไปอย่างมาก developer ที่ build บน AR/XR platforms ควรติดตาม SDK ของ OpenAI device อย่างใกล้ชิดว่าจะ open API หรือ closed ecosystem เหมือน Vision Pro ในช่วงแรก ก่อนตัดสินใจ platform bet

**1.2 Apple ขึ้นราคา Mac, iPad, HomePod เพราะ AI RAM Shortage — [The Verge](https://www.theverge.com/report/958678/apple-consumer-price-increase-ai-big-tech)**

MacBook Pro 16-inch ราคาขึ้น $300, iPad Air จาก $599 เป็น $749, HomePod Mini ขึ้น $30 สู่ $129 Tim Cook ยอมรับว่าราคา "unavoidable" และ pricing "unsustainable" พร้อมโทษ AI industry ว่า memory manufacturers ย้าย production lines จาก consumer RAM ไปผลิต HBM สำหรับ AI data centers ก่อให้เกิด "RAMageddon" ที่กระทบทั้งอุตสาหกรรม Xbox ราคาขึ้น 25%, Nothing ยกเลิก phone launch

นักวิชาการเห็นว่านี่คือ "AI externality" ที่จับต้องได้ที่สุดในรอบปี — ผู้บริโภคที่ไม่ได้ใช้ AI service ก็ยังต้องจ่ายราคาแพงขึ้นเพราะ AI data center demand ดึง memory จาก consumer market โดยตรง ผู้เชี่ยวชาญ AI มองว่า RAMageddon จะกดดัน consumer hardware ทุก tier ต่อเนื่องอีก 12–18 เดือนจนกว่า HBM production capacity จะทัน AI demand developer ที่ build บน Apple hardware ควรปรับ test device budget และ hardware refresh cycle ให้สะท้อน price premium 15–25% ที่เพิ่มขึ้น

**1.3 Apple ล็อบบี้รัฐบาลสหรัฐขอซื้อ RAM จากบริษัทจีนที่ถูก Pentagon แบน — [The Verge](https://www.theverge.com/tech/958707/apple-ram-buy-memory-blacklisted-china-cxmt)**

Apple กำลังล็อบบี้ Trump administration ขอ exception เพื่อซื้อ RAM chips จาก CXMT บริษัทจีนที่ Pentagon ขึ้นบัญชีดำเนื่องจากมีความสัมพันธ์กับกองทัพปลดปล่อยประชาชน (PLA) ตาม Financial Times แรงกดดัน AI-driven RAM shortage บังคับ Apple ต้องหาแหล่ง supply ทางเลือกแม้จะมีความเสี่ยงด้านความมั่นคงชาติ

นักวิชาการเห็นว่าถ้า Trump administration อนุมัติ CXMT exception จะสร้าง precedent ที่ซับซ้อน: บริษัท tech ขนาดใหญ่สามารถ lobby around export controls ได้ถ้า economic need รุนแรงพอ — นี่คือ tension ระหว่าง national security policy กับ industrial policy ที่ทวีความสำคัญในยุค AI ผู้เชี่ยวชาญ AI ชี้ว่าการที่ Apple ต้องพึ่ง CXMT เพราะ Samsung/Micron ไม่มีพอสะท้อนว่า AI infrastructure demand กำลัง reshape global memory supply chain อย่างลึกซึ้ง developer และทีม procurement ควรติดตาม outcome ของ CXMT exception request เพราะผลลัพธ์จะส่งสัญญาณต่อ chip control policy ที่กว้างกว่า

---

### 2. Tesla (TSLA · Tier 1) — Tesla ยอมความคดี Full Self-Driving ผู้เสียชีวิตทางเท้ารายแรก — [Engadget](https://www.engadget.com/2203211/tesla-settles-lawsuit-over-fatal-pedestrian-crash-involving-full-self-driving/)

Tesla ยอมความคดีการเสียชีวิตของ Johna Story อายุ 71 ปี ในรัฐ Arizona ปี 2023 ซึ่งเป็น pedestrian fatality รายแรกที่ถูกบันทึกจาก Full Self-Driving — Story ออกมาจากรถเพื่อบอกทางรถคันอื่นที่ประสบอุบัติเหตุจากแสงแดด และถูกชนโดย Model Y ที่ใช้ FSD เงื่อนไขการยอมความไม่ถูกเปิดเผย NHTSA กำลังสอบสวนแยกต่างหากว่า FSD ทำงานอย่างไรในสภาวะ poor visibility; Tesla ยังเผชิญคดีใหม่จากครอบครัวผู้เสียชีวิตในเดือนนี้

นักวิชาการชี้ว่า pattern ของ Tesla ที่ settle ซ้ำๆ แทนต่อสู้คดีในชั้นศาลกำลัง shape AI liability doctrine นอกกระบวนการยุติธรรมสาธารณะ — ไม่มี formal precedent แต่มี de facto standard ที่ industry อ้างอิง ผู้เชี่ยวชาญ AI ย้ำว่า NHTSA investigation มีผลมากกว่าคดีแพ่งเพราะอาจสั่ง recall และกำหนด safety requirements ที่ผูกพัน AV ทุกรายในตลาด developer ที่สร้าง autonomous systems ควรศึกษา edge case "poor visibility + pedestrian directing traffic" ที่ FSD ล้มเหลว เป็นตัวอย่างว่า camera-primary sensor fusion ด้อยประสิทธิภาพอย่างไรและต้องออกแบบ fallback พร้อม immutable audit trail ตั้งแต่ต้น

---

### 3. Meta (META · Tier 1) — Instagram ทดสอบ Your Algorithm แบบ Customizable มากขึ้น — [TechCrunch](https://techcrunch.com/2026/06/27/instagram-is-testing-more-ways-for-users-to-customize-your-algorithm/)

Instagram head Adam Mosseri เปิดเผย UX patterns ใหม่สำหรับ "Your Algorithm" feature ที่ช่วยให้ users กำหนดเองว่าต้องการเห็น content ประเภทไหนมากหรือน้อย — รวมถึง pull-down ใน feed เพื่อเปิด Your Algorithm menu, swipe-up จาก Reel สำหรับ customization prompt, และปุ่มใต้ Reel เพื่อบอก preference Mosseri ระบุว่า "เราต้องการให้ Your Algorithm กลายเป็น central experience" แต่ comment ยอดนิยมจาก users ยังคือ "แค่อยากเห็น content จากคนที่ตามอยู่" สะท้อน tension ระหว่าง social graph กับ AI recommendation

นักวิชาการมองว่า Meta กำลัง reframe algorithmic curation ให้ users รู้สึก "in control" แต่ถ้า AI recommendation ยังเป็น default ผู้ใช้ส่วนใหญ่จะไม่เปลี่ยนพฤติกรรม คำถามคือ meaningful user agency ต้องการ opt-in จริงหรือแค่ option ที่มี ผู้เชี่ยวชาญ AI ชี้ว่า UX patterns ที่ Mosseri โชว์เป็น implicit continuous learning interface — user interaction ทุกครั้งกลายเป็น preference signal กลับเข้า recommendation model ทันที Meta กำลัง turn engagement เป็น real-time fine-tuning feedback developer ที่ build บน Meta platform ควรออกแบบ content strategy ให้ assume explicit user preferences จะมีน้ำหนักมากขึ้น และเตรียมรับ traffic distribution ที่อาจเปลี่ยนเมื่อ feature roll out กว้างขึ้น

---

### 4. AMD (AMD · Tier 1) — AMD ปล่อย FSR Upscaling 4.1 ให้ Radeon RX 7000 ก่อนกำหนด — [Blognone](https://www.blognone.com/node/151000)

AMD ออก driver Adrenalin Edition 26.6.2 พร้อมขยาย FSR Upscaling 4.1 ให้รองรับ Radeon RX 7000 series (RDNA 3) ทั้งหมด — เดิม FSR 4.1 จำกัดเฉพาะ RX 9000 series (RDNA 4) และ AMD สัญญาจะขยายในเดือนกรกฎาคม แต่ deliver ก่อนกำหนดเล็กน้อย FSR 4.1 ใช้ ML-based temporal upscaling และ frame generation ที่ให้ quality ดีกว่า FSR 3 อย่างชัดเจนในด้าน artifact reduction

นักวิชาการเปรียบ AMD FSR กับ Nvidia DLSS ในฐานะ case study platform strategy: AMD เลือก backward compatibility เพื่อ ecosystem ที่ใหญ่กว่า vs. Nvidia เลือก exclusivity เพื่อ upsell hardware ใหม่ ผู้เชี่ยวชาญ AI ชี้ว่า FSR 4.1 บน RDNA 3 ต้องรัน ML inference ผ่าน shader cores (ไม่มี dedicated AI accelerators เหมือน RDNA 4) — การที่ AMD ทำสำเร็จยืนยันว่า ML upscaling algorithm flexible พอสำหรับ hardware ที่หลากหลาย developer ที่ build games หรือ graphics apps บน Radeon ควรอัปเดต driver เป็น Adrenalin Edition 26.6.2 และทดสอบ FSR 4.1 บน RDNA 3 ได้เลย

---

## Action items
- **สำหรับอาจารย์/นักเรียน:** ใช้ Apple ทั้งสามเหตุการณ์วันนี้เป็น integrated case study: AI infrastructure demand → RAM shortage → price hikes + supply chain compromise + talent drain สู่ competitor; ใช้ Tesla FSD settlement ถก AI liability doctrine และ role ของ out-of-court settlement ในการ shape industry standards โดยไม่มี public precedent
- **สำหรับผู้เชี่ยวชาญ AI:** Monitor NHTSA investigation outcome สำหรับ Tesla FSD ใน poor visibility — regulatory finding จะมีผลต่อ autonomous system safety requirements อุตสาหกรรมกว้าง; ประเมิน Apple CXMT exception outcome เป็น indicator ของ direction ที่ chip control policy กำลังเดิน; ศึกษา Meta's implicit preference learning เป็น pattern ที่นำไปใช้ใน recommendation system ของตัวเองได้
- **สำหรับโปรแกรมเมอร์:** อัปเดต Radeon driver เป็น Adrenalin Edition 26.6.2 ถ้าพัฒนา graphics app บน RDNA 3; ปรับ Apple device procurement budget ให้คำนึงถึง 15–25% price premium; ติดตาม OpenAI AI device SDK ว่าจะ open ให้ developer หรือ closed platform ก่อนตัดสินใจ AR/XR platform bet

## การครอบคลุม watchlist
คัดจาก Tier 1 · บริษัทที่มีข่าวสำคัญวันนี้: Apple (AAPL), Tesla (TSLA), Meta (META), AMD (AMD) · Tier 2 ไม่ถูกเรียกใช้

---
_Generated by the `daily-ai-watchlist` skill on 2026-06-28 (Asia/Bangkok) · model claude-opus-4-8 · TIERS_USED: 1._

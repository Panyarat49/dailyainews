# Perspectives — 2026-06-28 (watchlist)

## 1. Apple (AAPL) — อัปเดตสำคัญ 3 รายการ

### 1.1 Paul Meade VP Vision Pro → OpenAI
**อาจารย์ (มหาวิทยาลัย):** การออกของ Meade ไม่ใช่แค่ talent drain แต่คือ roadmap drain — เขาดูแลทั้ง Vision Pro และ AI smart glasses รุ่นที่ Apple จะเปิดตัวปีหน้า ซึ่งหมายความว่า OpenAI ได้ competitive intelligence ด้าน product planning ที่ล้ำไปกว่าการ hire engineer ทั่วไป นี่คือ case study "human capital as strategic asset" ในยุค AI hardware race
**ผู้เชี่ยวชาญด้าน AI:** Meade นำ product roadmap knowledge ด้าน spatial computing และ AI wearables ออกไปโดยตรง — OpenAI และ Jony Ive ออกแบบ AI device ที่แข่งกับ Apple smart glasses พอดี การ hire คนที่รู้ Apple's exact next move คือ strategic advantage ที่ประเมินค่าไม่ได้
**โปรแกรมเมอร์มืออาชีพ:** developer ที่ build บน AR/XR platform ควรติดตาม SDK ของ OpenAI device อย่างใกล้ชิดว่าจะ open API หรือ closed ecosystem เหมือน Vision Pro ในช่วงแรก — ตัดสินใจ platform bet ได้ดีกว่าถ้ารู้ก่อน launch

### 1.2 Apple ขึ้นราคา Mac/iPad เพราะ AI RAM Shortage
**อาจารย์ (มหาวิทยาลัย):** นี่คือ "AI externality" ที่จับต้องได้ที่สุดในรอบปี — AI data center demand ดึง HBM memory จาก consumer market ทำให้ผู้บริโภคที่ไม่ได้ใช้ AI service ก็ยังจ่ายแพงขึ้น เป็นตัวอย่างที่ดีของ structural economic effect ที่เรียนรู้ได้จากทั้งมุม supply chain economics และ policy regulation
**ผู้เชี่ยวชาญด้าน AI:** Tim Cook บอกว่า pricing "unsustainable" — เป็น signal ว่าแม้บริษัทที่ต่อรองชิปได้ดีที่สุดในโลกยังเจ็บปวด RAMageddon จะกดดัน consumer hardware ทุก tier ต่อเนื่องอีก 12–18 เดือนจนกว่า HBM production capacity จะทัน AI demand
**โปรแกรมเมอร์มืออาชีพ:** Apple hardware refresh cycle ของทีมแพงขึ้น 15–25% — ควรวางแผน hardware budget ใหม่สำหรับ Q3/Q4 2026 และประเมินว่า existing RDNA3/M3 devices พอสำหรับ AI-assisted development workflow อีกกี่ปีก่อนต้อง upgrade

### 1.3 Apple ล็อบบี้รัฐบาลขอซื้อ RAM จาก CXMT บริษัทจีนที่ถูก Pentagon แบน
**อาจารย์ (มหาวิทยาลัย):** ถ้า Trump administration อนุมัติ CXMT exception จะสร้าง precedent ที่ซับซ้อน: บริษัท tech ขนาดใหญ่สามารถ lobby around export controls ได้ถ้า economic need รุนแรงพอ นี่คือ tension ระหว่าง national security policy กับ industrial policy ที่น่าถกในชั้นเรียน AI governance
**ผู้เชี่ยวชาญด้าน AI:** การที่ Apple ต้องพึ่ง CXMT เพราะ Samsung/Micron ไม่มีพอ สะท้อนว่า AI infrastructure demand กำลัง reshape global memory supply chain อย่างลึกซึ้ง — ผู้ผลิต memory กำลัง prioritize HBM สำหรับ AI data centers ซึ่งมี margin สูงกว่า consumer RAM มาก
**โปรแกรมเมอร์มืออาชีพ:** ติดตาม outcome ของ CXMT exception request — ถ้าผ่าน จะช่วยลด Apple hardware shortage ในช่วง 12 เดือนถัดไปและอาจทำให้ราคาผลิตภัณฑ์ใหม่ไม่พุ่งสูงเพิ่มขึ้นอีก; ถ้าไม่ผ่าน Apple จะต้องหา alternative ที่อาจกระทบ timeline ของ iPhone 18 และ AI smart glasses

## 2. Tesla (TSLA) — FSD Arizona Settlement (Johna Story)

**อาจารย์ (มหาวิทยาลัย):** การยอมความโดยไม่เปิดเผยเงื่อนไขในคดี "first pedestrian fatality from FSD" คือ missed opportunity สำหรับ public legal precedent — แต่ pattern ของ Tesla ที่ settle ซ้ำๆ กำลัง shape AI liability doctrine นอกศาลผ่านการสะสม de facto standards ที่ industry อ้างอิง ซึ่งนักกฎหมายและนักนโยบายต้องติดตามอย่างระมัดระวัง
**ผู้เชี่ยวชาญด้าน AI:** NHTSA investigation ยังดำเนินต่อแยกจากคดีแพ่ง — regulatory outcome อาจมีผลมากกว่า settlement เพราะ NHTSA มีอำนาจสั่ง recall และกำหนด safety standards ที่ผูกพัน AV ทุกรายในตลาด; ประเด็น "poor visibility" ที่ FSD ล้มเหลวจะถูก investigate อย่างละเอียดและผลลัพธ์จะมีผลต่อ edge case requirements ทั้งอุตสาหกรรม
**โปรแกรมเมอร์มืออาชีพ:** developer ที่ build safety-critical autonomous systems ควรศึกษา edge case "poor visibility + pedestrian directing traffic" ที่ FSD ล้มเหลว — เป็นตัวอย่างว่า sensor fusion ล้มเหลวอย่างไรในสภาวะที่ camera-primary systems ด้อยประสิทธิภาพ; ควรออกแบบ fallback mechanism ให้รองรับ scenario นี้ตั้งแต่ต้นและ implement immutable audit trail ก่อนเกิดเหตุ

## 3. Meta (META) — Instagram Your Algorithm Customization

**อาจารย์ (มหาวิทยาลัย):** Meta กำลัง reframe algorithmic curation ให้ users รู้สึก "in control" — แต่ถ้า AI recommendation ยังเป็น default และ opt-out ซับซ้อน ผู้ใช้ส่วนใหญ่จะไม่เปลี่ยนพฤติกรรม คำถามสำหรับชั้นเรียน AI ethics: การมี customization option เพียงพอสำหรับ meaningful user agency หรือต้องเป็น opt-in (ต้องเลือก recommendation เอง) จึงจะนับว่า autonomy-preserving
**ผู้เชี่ยวชาญด้าน AI:** UX pattern ที่ Mosseri โชว์ (pull-down, swipe-up, per-Reel buttons) ไม่ใช่แค่ UX feature — มันเป็น implicit continuous learning interface ที่ user interaction ทุกครั้งกลายเป็น preference signal กลับเข้า recommendation model ทันที Meta กำลัง turn engagement data เป็น real-time fine-tuning feedback ที่ improve accuracy โดยที่ user รู้สึกว่าตัวเองเป็นคนควบคุม
**โปรแกรมเมอร์มืออาชีพ:** หาก Meta เปิด API สำหรับ Your Algorithm preferences ในอนาคต developer จะ build personalization layer บนนั้นได้ — ตอนนี้ควรออกแบบ content strategy ให้ assume explicit user preferences จะมีน้ำหนักมากขึ้นใน Instagram algorithm; เตรียมรับ traffic distribution ที่อาจเปลี่ยนเมื่อ feature roll out กว้างขึ้น

## 4. AMD (AMD) — FSR Upscaling 4.1 สำหรับ RDNA 3

**อาจารย์ (มหาวิทยาลัย):** AMD เลือก backward compatibility (FSR 4.1 สำหรับ RDNA 3) ขณะ Nvidia ยัง lock DLSS 4 ไว้เฉพาะ RTX 50 series — นี่คือ platform strategy ที่ต่างกันชัดเจน: AMD เลือก wider ecosystem adoption vs. Nvidia เลือก hardware upsell exclusivity เป็น case study "platform openness vs. platform lock-in" ที่สอนได้
**ผู้เชี่ยวชาญด้าน AI:** FSR 4.1 บน RDNA 3 ต้องรัน ML inference ผ่าน shader cores แทน dedicated AI accelerators ที่ RDNA 4 มี — การที่ AMD ทำ software path ได้สำเร็จยืนยันว่า ML upscaling algorithm flexible พอสำหรับ hardware ที่หลากหลาย; นี่เป็น signal ว่า AI inference workloads จะ increasingly run บน general compute fabric ไม่ใช่เฉพาะ dedicated AI silicon
**โปรแกรมเมอร์มืออาชีพ:** หาก build games หรือ graphics apps บน Radeon ควรอัปเดต driver เป็น Adrenalin Edition 26.6.2 และทดสอบ FSR 4.1 บน RDNA 3 ได้เลย — quality ด้าน temporal stability และ ghost/artifact reduction ดีกว่า FSR 3 อย่างชัดเจน ก่อนหน้า deadline กรกฎาคมที่ AMD เคยสัญญาไว้

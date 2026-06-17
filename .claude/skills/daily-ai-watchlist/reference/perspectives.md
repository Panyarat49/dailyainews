# Perspectives — 2026-06-17 (watchlist)

## 1. Nvidia — Blackwell Sweeps MLPerf Training 6.0

**อาจารย์ (มหาวิทยาลัย):** MLPerf คือ benchmark ที่สอนได้ดีเพราะมี methodology ที่โปร่งใสและ reproducible — การที่ Nvidia ชนะทุก 7 หมวดโดยไม่มีคู่แข่งแม้แต่รายเดียว submit ครบ ควรถามนักศึกษาว่า "ตลาดที่มีผู้เล่นคนเดียวครองมีโครงสร้างแรงจูงใจแบบไหน"
**ผู้เชี่ยวชาญด้าน AI:** ตัวเลข 2.02 นาทีสำหรับ DeepSeek-V3 671B นั้นน่าตกใจ — การที่ iteration cycle สั้นลงถึงระดับนี้เปลี่ยน research workflow ไปสิ้นเชิง: hyperparameter tuning ที่เคยใช้เวลาข้ามคืนสามารถ run หลายสิบรอบต่อวัน ซึ่งเร่งความก้าวหน้าของ frontier AI อีกหลายเท่า
**โปรแกรมเมอร์มืออาชีพ:** GB300 NVL72 เป็น hardware ที่ควรอยู่ใน procurement roadmap ของทีมที่วางแผน scale LLM training ในปี 2027 แต่ต้องเตรียม software stack ให้พร้อม: NVLink topology, NCCL tuning, checkpointing strategy สำหรับ cluster ขนาด 8,192+ GPU แตกต่างจาก small-scale deployment อย่างสิ้นเชิง

## 2. AMD — Mext Acquisition: AI แก้ RAM Shortage ที่ AI สร้าง

**อาจารย์ (มหาวิทยาลัย):** กรณีนี้สอนเรื่อง "feedback loop" ในเทคโนโลยี — AI สร้าง memory shortage แล้ว AI กลายเป็นผู้แก้ปัญหานั้น ซึ่งเป็น pattern ที่เกิดซ้ำในประวัติศาสตร์เทคโนโลยีเสมอ นักศึกษาควรถามว่า "solution ใหม่จะสร้างปัญหาอะไรต่อไป"
**ผู้เชี่ยวชาญด้าน AI:** predictive memory placement เป็น problem ที่ยากเพราะ LLM attention pattern นั้น unpredictable — Mext ต้องพิสูจน์ว่า model ของตัวเองแม่นยำพอที่จะไม่สร้าง cache miss ที่แย่กว่า heuristic เดิม; การทดสอบ production scale จะเป็นบทพิสูจน์จริง
**โปรแกรมเมอร์มืออาชีพ:** ถ้า Mext integration ใน AMD Instinct ทำงานได้จริง ผลที่ตามมาคือ inference workload บน AMD hardware อาจต้องการ HBM น้อยลง ซึ่งลด hardware cost ต่อ token ได้มีนัยสำคัญ — ควรติดตาม benchmark ที่ AMD จะออกมาพิสูจน์ใน 6–12 เดือนข้างหน้า

## 3. Alphabet — Android 17 + Gemini: Intelligence System

**อาจารย์ (มหาวิทยาลัย):** การ reposition "Operating System" เป็น "Intelligence System" เป็นการเปลี่ยน mental model ของผู้ใช้และนักพัฒนาอย่างมีนัย — ควรถามนักศึกษาว่าการ own "intelligence layer" ระดับ OS นั้นมีนัยด้าน power และ accountability อย่างไรต่อผู้ใช้
**ผู้เชี่ยวชาญด้าน AI:** Google มีข้อได้เปรียบเชิงแข่งขันที่ Apple ไม่มี: Gemini เป็น first-party model ทำให้ integrate ได้ลึกกว่าและลด latency ได้มากกว่า Apple ที่ต้องพึ่ง Google Cloud สำหรับ frontier tasks — irony ที่ Apple จ่ายเงินให้ Google เพื่อให้ iOS 27 แข่งกับ Android ได้
**โปรแกรมเมอร์มืออาชีพ:** Android 17 Gemini APIs เปิดโอกาสที่แท้จริงสำหรับ category ใหม่ของ apps ที่เข้าถึง OS-level context เช่น activity history, cross-app relationships — first movers ใน category นี้จะมีข้อได้เปรียบมากก่อน platform กลายเป็น commoditized

## 4. Microsoft — Investor Lawsuit + GitHub Capacity Crisis

**อาจารย์ (มหาวิทยาลัย):** lawsuit นี้เป็นกรณีตัวอย่างแรกๆ ของ "AI overclaiming liability" — ซึ่งจะกลายเป็นประเด็น governance ที่สำคัญมากขึ้นเมื่อบริษัทมากขึ้นใช้ AI เป็น selling point หลักต่อนักลงทุน นักศึกษาควรเรียนรู้ว่าอะไรคือเส้นแบ่งระหว่าง "roadmap" กับ "misrepresentation"
**ผู้เชี่ยวชาญด้าน AI:** ปัญหา GitHub capacity บ่งชี้ถึง tension จริง: Azure ถูกออกแบบมาสำหรับ steady-state enterprise workload แต่ AI inference/coding assistant demand มี spiky pattern ที่แตกต่างกันอย่างมาก — architecture ที่เหมาะสมอาจต้องการ hybrid cloud ตั้งแต่ต้น
**โปรแกรมเมอร์มืออาชีพ:** GitHub Copilot Enterprise users ควร monitor SLA metrics ด้วยตัวเองเพราะ vendor-reported uptime อาจไม่ตรงกับ latency ที่ developer รู้สึกจริง; ถ้า capacity issues กระทบ productivity ถึงเวลาประเมิน Cursor, Windsurf หรือ alternative tools เป็น fallback

## 5. Apple — New Siri Hands-On: AI ที่เพิ่ม Friction

**อาจารย์ (มหาวิทยาลัย):** กรณี Apple Siri เป็น case study สำคัญเรื่อง "technology regression" — การเพิ่ม AI layer ที่ดูเหมือน upgrade กลับทำให้ประสบการณ์แย่ลงสำหรับ use-case บางอย่าง สอนนักศึกษาว่า "ใหม่กว่า" ไม่ได้แปลว่า "ดีกว่า" เสมอไปโดยเฉพาะกับ UX
**ผู้เชี่ยวชาญด้าน AI):** ปัญหาของ Siri ใหม่สะท้อน challenge ที่แท้จริงของ "AI-native OS integration" — ต้องรักษา backward compatibility กับ hundreds of feature paths เดิม ขณะที่เพิ่ม AI layer ที่มี latency สูงกว่า rule-based system เดิมเสมอ; Apple จะต้องทำ feature-level A/B testing อย่างหนักใน releases ถัดไป
**โปรแกรมเมอร์มืออาชีพ:** บทเรียนสำหรับ developer ที่ integrate Apple Intelligence: ต้องวาง feature flag สำหรับ AI-enhanced features ทุกอย่าง และ collect explicit user feedback แยกระหว่าง "prefer AI version" กับ "prefer classic" เพราะ user preference จะ diverge อย่างมีนัยสำคัญโดยเฉพาะใน power users

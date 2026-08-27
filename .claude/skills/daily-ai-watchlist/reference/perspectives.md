# Perspectives — 2026-08-27 (watchlist)

## 1. Nvidia — Q2 FY2027 earnings crush estimates; Huang forecasts 70% FY28 growth
**อาจารย์ (มหาวิทยาลัย):** รายได้โต 106% ต่อปีเป็นกรณีศึกษาชั้นดีเรื่อง exponential growth และเป็นดัชนีสุขภาพของทั้งอุตสาหกรรม AI ไม่ใช่แค่ตัวบริษัทเดียว
**ผู้เชี่ยวชาญด้าน AI:** คำพูด "AI ถึงจุดเปลี่ยน" ของ Huang สะท้อนดีมานด์ GPU cluster ที่ขยายเกินกลุ่ม hyperscaler เดิม แต่หุ้นที่สวิงเกิน 5.6% ก่อนประกาศชี้ว่าตลาดยังกังวลความยั่งยืนของ capex
**โปรแกรมเมอร์มืออาชีพ:** ดีมานด์ที่ไม่ชะลอหมายถึง GPU จะยังหายากและแพงต่อไป ทีมควรวางแผนงบ infrastructure และ lead time ล่วงหน้า

## 2. Amazon — AWS and Nvidia to deliver 2 million additional GPUs
**อาจารย์ (มหาวิทยาลัย):** ตัวอย่างที่ดีของการวางแผน supply chain ระยะยาวในธุรกิจ capital-intensive ที่ผูกมัดกันข้ามปีงบประมาณ
**ผู้เชี่ยวชาญด้าน AI:** การผูก Vera CPU และ NVLink Fusion เข้ากับ Trainium4 ของ AWS เองสะท้อนกลยุทธ์ hybrid — ใช้ชิปคัสตอมควบคู่กับ Nvidia แทนที่จะเลือกทางใดทางหนึ่งสุดขั้ว ต่างจาก SpaceX ที่เคยประกาศผูก exclusive กับ Nvidia
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ใช้ AWS ควรจับตาว่า capacity ใหม่นี้จะกระทบคิวรอ GPU instance หรือราคาบน EC2/Bedrock เมื่อไร เพราะเป็น supply commitment ระยะยาวถึงปี 2028

## 3. Alphabet — Waymo unveils custom AI chip for its robotaxi fleet
**อาจารย์ (มหาวิทยาลัย):** ตัวอย่างที่ดีของ hardware-software co-design เฉพาะทาง (edge inference) ต่างจาก GPU อเนกประสงค์สำหรับ train โมเดลใหญ่
**ผู้เชี่ยวชาญด้าน AI:** การที่ Waymo เลือกทำ ASIC เฉพาะงาน sensor-fusion/denoising แทนชิปควบคุมการขับขี่ทั้งหมด สะท้อนแนวทางระมัดระวังกว่า Tesla ที่ทำ all-in
**โปรแกรมเมอร์มืออาชีพ:** เป็นแนวทางอ้างอิงสำหรับงาน edge AI/robotics — แบ่งงาน preprocessing เรียลไทม์ให้ ASIC เฉพาะทาง ส่วนโมเดลตัดสินใจหลักยังรันบนฮาร์ดแวร์ทั่วไปที่อัปเกรดง่ายกว่า

## 4. Tesla — Tesla, Uber and Waymo win approval for thousands of robotaxis in Nevada
**อาจารย์ (มหาวิทยาลัย):** กรณีศึกษาที่ดีเรื่องการแข่งขันของผู้เล่นหลายรายในตลาดเดียวกันภายใต้กรอบกำกับดูแลเดียวกัน ต่างจากเมืองที่มักให้สิทธิ์ผู้เล่นรายเดียว
**ผู้เชี่ยวชาญด้าน AI:** โควตา 5,000 คันของ Tesla เทียบกับ 1,000 คันของ Waymo สะท้อนความมั่นใจของหน่วยงานกำกับต่อ FSD stack ของ Tesla ในระดับที่มากกว่า แม้ Waymo จะสะสมไมล์ทดสอบมากกว่ามานาน
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ทำงานด้าน autonomous fleet operations ควรติดตามกระบวนการ inspection/insurance ก่อนเปิดบริการจริงใน 30 วัน เพราะเป็นแม่แบบ regulatory pathway ที่รัฐอื่นอาจทำตาม

## 5. Apple — Apple cuts hundreds of jobs from Siri and Vision Pro teams
**อาจารย์ (มหาวิทยาลัย):** เหมาะสอนเรื่อง organizational reallocation หลังเปิดตัวผลิตภัณฑ์ — การตัดคนจากทีมที่เพิ่งส่งมอบงาน (Siri AI) มักเกิดขึ้นเมื่อ focus เปลี่ยนไปที่โปรเจกต์ถัดไป
**ผู้เชี่ยวชาญด้าน AI:** การตัดคนจากทั้ง Siri และ Vision Pro พร้อมกันชี้ว่า Apple กำลังจัดลำดับความสำคัญใหม่ระหว่างสองสายผลิตภัณฑ์ AI ที่ต่างก็มาช้ากว่าคู่แข่ง
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ผูก integration กับ Siri AI API หรือ Vision Pro SDK ควรจับตาความต่อเนื่องของ roadmap อย่างใกล้ชิดหลังการปรับโครงสร้างนี้

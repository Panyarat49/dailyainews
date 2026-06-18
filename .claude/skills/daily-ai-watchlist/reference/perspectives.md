# Perspectives — 2026-06-18 (watchlist)

## 1. Apple — AI ขึ้นราคา RAM จนกระทบต้นทุน iPhone + Tim Cook ยอมรับปัญหา

**อาจารย์ (มหาวิทยาลัย):** กรณี Apple เป็นตัวอย่างที่ดีสอนนักเรียนว่า AI feature ไม่ได้ "ฟรี" — ต้นทุน hardware (RAM) ที่เพิ่มขึ้นตามความต้องการของโมเดลใน device ส่งผลเป็นลูกโซ่ถึงราคาผู้บริโภค ซึ่งเปิดคำถามว่า on-device AI คุ้มค่าเมื่อเทียบกับ cloud-based approach หรือไม่

**ผู้เชี่ยวชาญด้าน AI:** ปรากฏการณ์นี้สะท้อน tension ระหว่าง privacy (on-device inference) กับ cost efficiency (cloud inference) — Apple เลือกทิศทาง on-device AI เพื่อ privacy differentiator แต่กำลังพบว่าต้นทุน memory bandwidth เป็นข้อจำกัดสำคัญ และ RAM escalation จะเป็น constraint ที่กระทบทุก vendor ที่ทำ edge AI

**โปรแกรมเมอร์มืออาชีพ:** ถ้าออกแบบ app ที่ต้องใช้ on-device model บน iOS — ควรประเมิน memory footprint ตั้งแต่วันแรก เพราะ RAM budget ต่อ app มีจำกัด และถ้า Apple ขึ้นราคาอุปกรณ์จาก AI RAM cost ผู้ใช้ราคาย่อมเยาจะช้าอัพเกรด ทำให้ fragmentation ของ device capability เป็นปัญหาระยะยาว

## 2. Amazon — AWS เปิด Neptune Analytics context graph ที่เรียนรู้จาก agents

**อาจารย์ (มหาวิทยาลัย):** AWS Neptune Analytics แสดงให้เห็นว่า "context layer" กำลังกลายเป็นชั้นโครงสร้างพื้นฐานใหม่ในสถาปัตยกรรม agentic AI — คล้ายกับที่ database layer กลายเป็นส่วนสำคัญในยุค web ใช้สอน architectural evolution ของระบบ AI ได้ดีมาก

**ผู้เชี่ยวชาญด้าน AI:** knowledge graph ที่เรียนรู้จาก agent interactions โดยอัตโนมัติ (ไม่ต้อง manual curation) เป็น approach ที่แก้ปัญหา cold-start ของ RAG/memory systems ได้ — แต่ต้องประเมินว่า graph quality จาก agent-generated data จะดีพอสำหรับ production use cases หรือยัง เทียบกับ curated knowledge bases

**โปรแกรมเมอร์มืออาชีพ:** ถ้าสร้าง agentic workflow บน AWS — Neptune Analytics context graph น่าทดสอบในงานที่ agent ต้องจำ entity relationships ข้ามหลาย sessions เช่น customer service หรือ research agents เพราะ auto-learning graph ลด engineering overhead ของการสร้าง memory layer เองได้มาก

## 3. Alphabet — SandboxAQ $500M CHIPS Act + Google Gemini smart home speaker

**อาจารย์ (มหาวิทยาลัย):** สองข่าวของ Alphabet วันนี้แสดงสองหน้าของ AI strategy — SandboxAQ ใช้ AI+quantum เพื่องาน scientific discovery ในระดับชาติ ขณะที่ Google Gemini เข้าถึงผู้บริโภคผ่าน smart home สอนได้ว่า AI application spectrum กว้างมากตั้งแต่ materials science ถึงเครื่องใช้ในบ้าน

**ผู้เชี่ยวชาญด้าน AI:** SandboxAQ เป็นตัวอย่าง AI-for-science ที่รัฐบาลลงทุนเพราะ ROI ระยะยาวสูง (semiconductor supply chain) ส่วน Gemini smart home เป็นการ repositioning ของ Google Assistant ที่เสียพื้นที่ให้ competitors — ทั้งสองสะท้อนว่า Alphabet กำลัง deploy AI ในทุก vertical พร้อมกัน

**โปรแกรมเมอร์มืออาชีพ:** ถ้าสนใจ home automation หรือ voice AI — Google Gemini integration ใน smart speaker รุ่นใหม่จะเปิด API/SDK ที่มีความสามารถมากกว่า Google Assistant เดิม ควรจับตาเอกสาร developer ที่จะตามมา; สำหรับ SandboxAQ ควรจับตา API สำหรับ molecular simulation ที่จะเปิดให้นักวิจัยภายนอก

## 4. Nvidia — Celestial AI เพิ่มกำลังผลิต wafer ออปติกส์ 4 เท่า รองรับ AI interconnect

**อาจารย์ (มหาวิทยาลัย):** ข่าวนี้สอนว่า AI infrastructure ไม่ได้อยู่แค่ที่ GPU — optical interconnect เป็นส่วนสำคัญที่ทำให้ชิปในดาต้าเซ็นเตอร์สื่อสารกันได้ด้วยความเร็วสูง ใช้อธิบาย "ห่วงโซ่" ของ AI hardware ที่ครอบคลุมตั้งแต่ silicon ถึง photonics

**ผู้เชี่ยวชาญด้าน AI:** Celestial AI ขยาย wafer output 4x สะท้อนว่า bottleneck ของ AI compute ไม่ได้อยู่แค่ที่ GPU supply แต่ลามไปถึง interconnect bandwidth — ยิ่ง GPU cluster ใหญ่ขึ้น ยิ่งต้องการ optical I/O สูงขึ้น และ Nvidia สนับสนุน Celestial AI เพื่อป้องกัน supply chain risk ของตัวเอง

**โปรแกรมเมอร์มืออาชีพ:** สำหรับทีมที่วางแผน multi-node distributed training หรือ inference cluster — interconnect bandwidth คือตัวแปรที่กำหนด scaling efficiency ไม่น้อยกว่า GPU count; ข่าวนี้เป็นสัญญาณว่า optical interconnect กำลังจะ mainstream มากขึ้น และ cloud providers จะนำ tech นี้ไปในรุ่นถัดไปของ accelerator instances

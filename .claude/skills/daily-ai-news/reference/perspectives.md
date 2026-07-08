# Perspectives — 2026-07-08 (ainews)

## 1. GitHub AI agent leaks private repos when asked nicely ("GitLost")
**อาจารย์ (มหาวิทยาลัย):** ช่องโหว่ GitLost เป็นตัวอย่างสอนเรื่อง prompt injection ที่ดีที่สุดเคสหนึ่ง เพราะมันไม่ใช่บั๊กใน AI model โดยตรง แต่เป็นช่องว่างในการออกแบบ workflow ที่ให้ agent มีสิทธิ์เข้าถึงข้อมูล private และโพสต์ผลลัพธ์แบบ public พร้อมกัน — ควรใช้สอนหลักการ "least privilege" ใน agentic system design
**ผู้เชี่ยวชาญด้าน AI:** สิ่งที่น่ากังวลคือช่องโหว่นี้ไม่ได้จำเพาะโมเดล ใช้ได้ทั้งกับ agent ที่ขับเคลื่อนด้วย Claude หรือ Copilot เพราะรากปัญหาอยู่ที่สถาปัตยกรรม GitHub Agentic Workflows เอง และ GitHub ยังไม่มีทั้ง fix และเอกสารเตือนผู้ใช้อย่างเป็นทางการ ทำให้องค์กรที่เปิดใช้ฟีเจอร์นี้อยู่ในความเสี่ยงต่อเนื่อง
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่เปิดใช้ GitHub Agentic Workflows ควรตรวจสอบทันทีว่า agent มีสิทธิ์เข้าถึง private repo ใดบ้าง และปิดความสามารถโพสต์คอมเมนต์สาธารณะจาก workflow ที่แตะข้อมูล sensitive จนกว่า GitHub จะออก patch อย่างเป็นทางการ

## 2. Anthropic launches Claude Cowork on mobile and web
**อาจารย์ (มหาวิทยาลัย):** การขยาย Cowork จาก desktop-only ไปสู่ mobile/web สะท้อนทิศทางที่ agentic AI กำลังเปลี่ยนจาก "เครื่องมือที่ต้องนั่งหน้าคอม" เป็น "ผู้ช่วยที่ทำงานต่อเนื่องในคลาวด์" — ประเด็นที่ควรถกในชั้นเรียนคือความรับผิดชอบเมื่อ agent ทำงานอัตโนมัติต่อแม้ผู้ใช้ปิดเครื่องไปแล้ว
**ผู้เชี่ยวชาญด้าน AI:** การย้าย workload ไปรันบนคลาวด์แทนเครื่อง local เปลี่ยน threat model และ latency profile ของ Cowork อย่างมีนัยสำคัญ ต้องติดตามว่า Anthropic จัดการ state/context ระหว่าง session มือถือกับเว็บอย่างไรให้ต่อเนื่องและปลอดภัย
**โปรแกรมเมอร์มืออาชีพ:** สำหรับทีมที่ใช้ Cowork ในงาน non-coding อยู่แล้ว (ตามข้อมูลผู้ใช้ 90% ไม่ได้ใช้เพื่อ coding) การมาถึงของ mobile/web เปิดโอกาสให้ non-technical staff เข้าถึง agent ได้ง่ายขึ้น — ควรทบทวน permission model และ access control ก่อนปล่อยให้ทีมที่ไม่ใช่ engineer ใช้งานแบบ self-serve

## 3. China's DeepSeek reportedly developing its own AI chip
**อาจารย์ (มหาวิทยาลัย):** ถ้าเป็นจริง นี่คือหลักฐานว่ามาตรการควบคุมการส่งออกชิปกำลังผลักดันให้ AI lab ของจีนขยับจาก "ผู้ใช้ชิปต่างชาติ" ไปสู่ "ผู้ออกแบบชิปเอง" เร็วกว่าที่นักวิเคราะห์หลายคนเคยคาด ควรใช้สอนเรื่อง unintended consequences ของนโยบาย export control
**ผู้เชี่ยวชาญด้าน AI:** DeepSeek พิสูจน์ตัวเองแล้วว่าเก่งด้าน algorithm efficiency (efficient training/inference) แต่การออกแบบชิปเป็นทักษะคนละมิติที่ต้องใช้เวลาและทุนมหาศาลกว่าจะแข่งกับ Nvidia/AMD ได้จริง ควรระวังการตีความข่าวนี้เกินจริงจนกว่าจะมีรายละเอียด architecture ที่ชัดเจนกว่า "sources say"
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่พึ่งพา DeepSeek model ผ่าน API ควรจับตาว่าชิปของตัวเอง (ถ้าเกิดขึ้นจริง) จะทำให้ inference cost ถูกลงและ availability เพิ่มขึ้นแค่ไหน เพราะอาจกระทบทางเลือก provider ในสาย cost-sensitive workload

## 4. Meta's new Muse Image model lets prompts pull in other Instagram users
**อาจารย์ (มหาวิทยาลัย):** ฟีเจอร์ "@mention" คนอื่นในภาพที่ AI สร้างเป็นกรณีศึกษาชั้นดีเรื่อง consent และ likeness rights — คำถามคือใครต้องยินยอมก่อนภาพหน้าตาคนอื่นถูกใช้ generate เนื้อหาใหม่ และแพลตฟอร์มควรมี guardrail อย่างไรก่อนเปิดฟีเจอร์แบบนี้สู่สาธารณะวงกว้าง
**ผู้เชี่ยวชาญด้าน AI:** การให้ Superintelligence Labs ปล่อยโมเดลภาพตัวแรกพร้อมความสามารถอ้างอิงบัญชี Instagram อื่นโดยตรง ต้องอาศัยระบบตรวจสอบ identity/consent ที่แม่นยำมาก มิเช่นนั้นความเสี่ยงเรื่อง deepfake-adjacent misuse จะสูงกว่าเครื่องมือ image-gen ทั่วไปที่ไม่ผูกกับบัญชีจริง
**โปรแกรมเมอร์มืออาชีพ:** นักพัฒนาที่สร้างแอปบน Meta AI API ควรตรวจสอบ policy การใช้ฟีเจอร์ @mention นี้อย่างละเอียด โดยเฉพาะเรื่อง opt-out ของผู้ใช้ที่ไม่ต้องการให้บัญชีถูกดึงไปใช้ใน prompt ของคนอื่น ก่อนนำไปสร้างผลิตภัณฑ์ต่อยอด

## 5. Cloud AI worm "CAI" steals rival malware's stolen credentials, mines crypto
**อาจารย์ (มหาวิทยาลัย):** ปรากฏการณ์ "โจรขโมยของจากโจร" ของเวิร์ม CAI เป็นตัวอย่างที่ดีของวิวัฒนาการ malware ที่แข่งขันกันเองในระบบนิเวศอาชญากรรมไซเบอร์ ควรใช้สอนแนวคิด competitive dynamics ในภัยคุกคามไซเบอร์ ไม่ใช่แค่มองว่าเป็นภัยจากฝ่ายเดียว
**ผู้เชี่ยวชาญด้าน AI:** การที่ CAI เจาะจงเป้าหมายเครื่องมือ cloud-native อย่าง Docker, Kubernetes, Redis, etcd, Kubelet และ Ray สะท้อนว่าผู้โจมตีเข้าใจ AI/ML infrastructure stack สมัยใหม่เป็นอย่างดี โดยเฉพาะ Ray ที่ใช้กันแพร่หลายใน distributed AI training/serving ทำให้ workload AI เป็นเป้าที่มีมูลค่าสูงขึ้นเรื่อย ๆ
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่รัน Kubernetes/Ray cluster สำหรับ AI workload ควรตรวจสอบทันทีว่า dashboard และ API endpoint ของเครื่องมือเหล่านี้ไม่ได้เปิดสู่อินเทอร์เน็ตแบบไม่มี authentication เพราะเป็นช่องทางหลักที่เวิร์มประเภทนี้ใช้เจาะเข้าระบบ

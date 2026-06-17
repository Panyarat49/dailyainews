# Perspectives — 2026-06-17 (ainews)

## 1. Z.ai GLM-5.2 — open-weights model ชนะ GPT-5.5 ด้วยต้นทุน 1/6
**อาจารย์ (มหาวิทยาลัย):** GLM-5.2 เป็นตัวอย่างดีของ "cost-performance frontier" — ราคา 1/6 ที่ประสิทธิภาพเทียบเท่าหมายความว่านักเรียนควรศึกษา trade-off ระหว่าง openness, cost, และ capability อย่างลึกซึ้ง ไม่ใช่แค่ไล่ตาม benchmark อันดับ 1
**ผู้เชี่ยวชาญด้าน AI:** 753B parameters แบบ open-weights สำหรับ long-horizon coding เป็นก้าวสำคัญ — "long-horizon" ต้องรักษา context และ plan หลายขั้นตอนโดยไม่ hallucinate ซึ่งยากกว่า single-shot benchmark มาก ควรตรวจสอบ test-time compute ที่ใช้ก่อนเปรียบเทียบกับ GPT-5.5
**โปรแกรมเมอร์มืออาชีพ:** ต้นทุน 1/6 ในงาน agentic coding loop ที่รันหลายร้อย turn ต่อวันมี savings ชัดเจน ควร benchmark GLM-5.2 กับ domain จริงก่อนย้าย production เพราะ SWE-Bench อาจไม่ reflect codebase ของทีม

## 2. Qualcomm / Tenstorrent — ดีล $10B ใน RISC-V AI chip
**อาจารย์ (มหาวิทยาลัย):** ดีลนี้แสดงให้เห็นว่าการแข่งขันชิป AI ไม่ได้จำกัดอยู่แค่ Nvidia vs AMD แต่ยังมี RISC-V ซึ่งเป็น open ISA ที่ท้าทาย proprietary architecture — บทเรียนสำคัญเรื่อง ecosystem lock-in และการเมืองของ open standards
**ผู้เชี่ยวชาญด้าน AI:** Tenstorrent ภายใต้ Jim Keller มีแนวทาง compiler-first และ open architecture — ถ้า Qualcomm นำ Tenstorrent ไป scale ใน datacenter ได้จะเป็น serious alternative แต่ ecosystem (software stack, CUDA-equivalent) ยังเป็น hurdle ที่ต้องผ่าน
**โปรแกรมเมอร์มืออาชีพ:** ถ้าดีลสำเร็จ Qualcomm+Tenstorrent จะเป็นทางเลือก inference hardware ที่ไม่ต้องพึ่ง CUDA — น่าจับตาสำหรับทีมที่ต้องการ diversify ออกจาก Nvidia lock-in

## 3. AMD / Mext — predictive memory M&A
**อาจารย์ (มหาวิทยาลัย):** การที่ AI สร้างวิกฤต RAM shortage แล้วต้องใช้ AI แก้ปัญหาเดิมนั้นเป็นตัวอย่าง feedback loop ในเทคโนโลยีที่ควรสอน — ความต้องการ KV cache และ MoE expert weights ดัน memory demand เกินที่ HBM จะรองรับได้อย่างมีประสิทธิภาพ
**ผู้เชี่ยวชาญด้าน AI:** Mext ใช้ LSTM + transformers เพื่อ predict ว่า data block ใดจะถูกเรียกใช้เร็วๆ นี้แล้ว migrate อัตโนมัติจาก HBM ไป flash — ตรงกับปัญหา MoE models ที่ expert weights ส่วนใหญ่ inactive ณ เวลาใดเวลาหนึ่ง
**โปรแกรมเมอร์มืออาชีพ:** สำหรับ deployment engineer predictive memory tiering อาจลดต้นทุน HBM ต่อ GPU node โดยไม่ลด throughput — ควรจับตา ROCm integration และว่า Mext จะ embedded ใน AMD drivers หรือเปิดเป็น standalone API

## 4. Google Android 17 — "Intelligence System"
**อาจารย์ (มหาวิทยาลัย):** Google กำหนดนิยาม Android ใหม่ว่าเป็น "Intelligence System" ไม่ใช่แค่ OS — เป็นจุดเปลี่ยนแนวคิดที่ควรถกเรื่อง privacy, model on-device vs. cloud, และการที่ AI อยู่ในมือผู้ใช้กว่า 3 พันล้านคน
**ผู้เชี่ยวชาญด้าน AI:** การนำ Gemini Omni, Lyria 3 และ AudioLM มารวมใน Pixel Drop แสดงว่า Google กำลัง dogfood frontier models บน hardware ตัวเอง — ข้อที่น่าจับตาคือ latency และ energy consumption ของ Gemini Omni บน on-device hardware
**โปรแกรมเมอร์มืออาชีพ:** Android 17 เปิด interaction pattern ใหม่ด้วย bubble-bar UI และ Gemini API ที่ build-in — ควรอ่าน developer changelog ตั้งแต่วันนี้เพราะ Gemini in Chrome (ปลายเดือนนี้) จะสร้าง category ของแอปใหม่

## 5. Weibo VibeThinker-3B — benchmark controversy
**อาจารย์ (มหาวิทยาลัย):** VibeThinker-3B เป็นบทเรียนคลาสสิกเรื่อง "teaching to the test" ในยุค AI — เมื่อ benchmark กลายเป็นเป้าหมาย มันหยุดเป็นการวัดที่ดีแล้ว (Goodhart's Law) ควรใช้ถกในชั้นเรียน
**ผู้เชี่ยวชาญด้าน AI:** LeetCode contest post-cutoff (ผ่าน 123/128 first-attempt) เป็นวิธีทดสอบที่แข็งแกร่งที่สุดที่ contamination-proof ได้ แต่ความสามารถ real-world เช่นไม่รู้จัก uv package manager ยังเป็นข้อกังขาสำคัญ
**โปรแกรมเมอร์มืออาชีพ:** โมเดล 3B ที่ทำ reasoning ได้ดีบน benchmark เป็นโอกาส edge deployment ที่น่าสำรวจ แต่ต้องทดสอบกับ codebase จริงของทีมก่อน เพราะ benchmark tasks อาจต่างจาก real-world code complexity อย่างมาก

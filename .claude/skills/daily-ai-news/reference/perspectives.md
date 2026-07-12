# Perspectives — 2026-07-12 (ainews)

## 1. AI companies want to water down Australia's copyright laws. Artists are outraged, Labor is split
**อาจารย์ (มหาวิทยาลัย):** กรณีนี้เป็นตัวอย่างคลาสสิกของความขัดแย้งระหว่าง industrial policy กับสิทธิ์ทางทรัพย์สินทางปัญญา — เหมาะเป็นกรณีศึกษาให้นักเรียนเห็นว่ารัฐบาลต้องชั่งน้ำหนักระหว่างการดึงดูดการลงทุน data center กับการปกป้องรายได้ของครีเอเตอร์ ซึ่งไม่มีคำตอบที่ถูกต้องตายตัว
**ผู้เชี่ยวชาญด้าน AI:** ประเด็นสำคัญคือการเจรจาแลกเปลี่ยน (carve-out) ระหว่างสิทธิ์ใช้ข้อมูลฝึกโมเดลกับการลงทุนโครงสร้างพื้นฐาน AI ซึ่งกำลังเกิดซ้ำในหลายประเทศ ไม่ใช่แค่ออสเตรเลีย — ทิศทางของกฎหมายนี้อาจกลายเป็นบรรทัดฐานให้ตลาดอื่นอ้างอิงต่อ
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ฝึกหรือ fine-tune โมเดลด้วยข้อมูลจากออสเตรเลียควรจับตาการเปลี่ยนแปลงกฎหมายนี้อย่างใกล้ชิด เพราะอาจกระทบสิทธิ์การใช้ข้อมูล licensing และ data-sourcing pipeline ในอนาคตอันใกล้

## 2. Forget typosquatting; slopsquatting is the software supply chain threat created by AI coding tools
**อาจารย์ (มหาวิทยาลัย):** นี่คือตัวอย่างที่ดีในการสอนเรื่อง emergent risk จาก AI hallucination — ความเสี่ยงไม่ได้จบแค่ "คำตอบผิด" แต่ลามไปเป็นช่องโหว่ความปลอดภัยจริงในระบบซอฟต์แวร์ ควรบรรจุไว้ในหลักสูตร secure coding ยุค AI
**ผู้เชี่ยวชาญด้าน AI:** ปรากฏการณ์นี้สะท้อนขีดจำกัดพื้นฐานของ LLM ที่ยัง hallucinate ชื่อ package ที่ไม่มีอยู่จริงได้บ่อย — การแก้ที่ต้นเหตุต้องอาศัยทั้ง grounding กับ package registry จริงระหว่าง inference และการปรับปรุง training data ไม่ใช่แค่ patch ที่ปลายทาง
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ใช้ AI coding assistant ควรเพิ่มขั้นตอน verify ชื่อ package กับ registry ทางการก่อน install ทุกครั้ง และตั้ง policy ห้าม auto-install จาก suggestion โดยไม่ผ่านการรีวิวมนุษย์ โดยเฉพาะใน CI/CD pipeline

## 3. OpenAI bets on families as ChatGPT goes deeper into households
**อาจารย์ (มหาวิทยาลัย):** การขยายฐานผู้ใช้จาก individual productivity ไปสู่ household เป็นทิศทางที่ platform เทคโนโลยีใหญ่เคยเดินตามมาก่อน (Google, Apple, Meta) — น่าสนใจให้นักเรียนวิเคราะห์ว่า trust-sensitive design สำหรับผู้สูงอายุและเด็กต้องต่างจาก design สำหรับผู้ใช้ทั่วไปอย่างไร
**ผู้เชี่ยวชาญด้าน AI:** ข้อมูล Sensor Tower ที่ระบุว่าฐานผู้ใช้อายุ 35+ โตขึ้นชัดเจนสะท้อนว่า ChatGPT กำลังเปลี่ยนจาก early-adopter tool เป็น mainstream utility — การออกแบบสำหรับ caregiver และผู้สูงวัยต้องคำนึงถึง safety guardrail ที่ต่างจาก power-user segment
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่สร้างผลิตภัณฑ์บน ChatGPT API ควรเตรียมรับมือกับ user base ที่หลากหลายขึ้น (ผู้สูงอายุ ผู้ปกครอง) ซึ่งต้องการ UX ที่เรียบง่ายกว่าและ error handling ที่ชัดเจนกว่าฐานผู้ใช้เดิม

## 4. Colibrì proof-of-concept gains frontier-level 1.5-TB AI model — runs on only 25GB of RAM
**อาจารย์ (มหาวิทยาลัย):** โปรเจกต์นี้เป็นตัวอย่างดีของงานวิศวกรรมแบบ resource-constrained ที่ท้าทายสมมติฐานว่าโมเดลระดับ frontier ต้องใช้ hyperscale hardware เท่านั้น — เหมาะสอนแนวคิด memory-mapped inference และ trade-off ระหว่าง speed กับ accessibility
**ผู้เชี่ยวชาญด้าน AI:** ความเร็วเพียง 0.05–0.1 token/วินาทีทำให้ยังใช้งานจริงไม่ได้ แต่พิสูจน์แนวคิดสำคัญคือโมเดลขนาด 1.5TB สามารถรันบน RAM เพียง 25GB ได้ด้วยเทคนิค offloading ไปยัง NVMe ซึ่งเปิดทางให้ home-lab AI enthusiast เข้าถึงโมเดลระดับ frontier ได้ในอนาคตหากเทคนิคนี้พัฒนาต่อ
**โปรแกรมเมอร์มืออาชีพ:** วิศวกรที่สนใจ local AI deployment ควรติดตามเทคนิค memory-offloading แบบนี้ เพราะแม้วันนี้ช้าเกินใช้งานจริง แต่แนวทาง CPU + NVMe อาจกลายเป็นทางเลือกต้นทุนต่ำสำหรับ inference offline ในอนาคต

## 5. Notion ออกแอปแยก Notion Agents บน iOS ไว้เรียกใช้ผู้ช่วย AI โดยเฉพาะ
**อาจารย์ (มหาวิทยาลัย):** การแยกแอป AI assistant ออกจากแอปหลักสะท้อนเทรนด์ที่ผู้ผลิตซอฟต์แวร์เริ่มมอง agentic AI เป็นผลิตภัณฑ์อิสระ ไม่ใช่แค่ feature เสริม — น่าสนใจให้ผู้เรียนเปรียบเทียบกับ pattern เดียวกันในผลิตภัณฑ์อื่น
**ผู้เชี่ยวชาญด้าน AI:** การให้ผู้ใช้เลือกโมเดลเบื้องหลังได้เอง (GPT, Claude, Gemini) เป็นแนวทาง model-agnostic ที่ช่วยลด vendor lock-in และให้ผู้ใช้เลือกโมเดลที่เหมาะกับงานแต่ละประเภทได้ตรงจุดขึ้น
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ build บน Notion API ควรตรวจสอบว่า Notion Agents เปิด endpoint ใหม่ให้ integrate หรือไม่ เพราะ agentic layer แบบนี้มักตามมาด้วย API ใหม่สำหรับนักพัฒนาภายในไม่กี่เดือน

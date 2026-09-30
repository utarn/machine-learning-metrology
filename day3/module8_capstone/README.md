# Capstone (M8) — โจทย์ 3 แทร็ก + starter + เกณฑ์ให้คะแนน

ครึ่งวันสุดท้ายของหลักสูตร: **11:30–12:00 kickoff** (แบ่งทีม เลือกแทร็ก)
→ **13:00–15:00 สร้าง** → **15:00–16:30 นำเสนอ** — ทีม 2–3 คน เลือก **หนึ่ง
แทร็ก** ผลงาน = โน้ตบุ๊ก + นำเสนอ 10 นาที ซึ่ง **เป็นการวัดผลของหลักสูตรไปในตัว**
(ไม่มี quiz แยก) — เกณฑ์ให้คะแนน: [rubric.md](rubric.md)

## 3 แทร็ก

| แทร็ก | โจทย์ | ทักษะที่ reuse | Starter dataset | Starter notebook |
|---|---|---|---|---|
| **A — ตรวจ defect จากภาพ** 🏭 | จำแนกภาพชิ้นงาน ปกติ/ชำรุด ด้วย 2 วิธี (PatchCore ไม่ต้องมี label ชำรุด vs transfer learning ต้องมี) + confusion matrix | M1 (transfer learning), M6 (PatchCore), M7 (วิเคราะห์ error) | ภาพแผ่นโลหะสังเคราะห์ (สร้างในโน้ตบุ๊ก) หรือรูปถ่ายจริงของทีม | [starter_trackA_defect.ipynb](starter_trackA_defect.ipynb) |
| **B — ฟังเสียงเครื่องจักร** 🔊 | จำแนกเสียง 6 กลุ่มเครื่องจักรจาก MFCC + Random Forest + feature engineering ของทีม (+ มุม anomaly แบบ kNN) | M4 (MFCC/RF), M4-CNN (ทางเลือก spectrogram CNN บน Kaggle), M6 (แนวคิด anomaly) | ESC-50 subset (6 คลาส × 40 คลิป) หรือเสียงจริงที่ทีมอัดเอง | [starter_trackB_machine_listening.ipynb](starter_trackB_machine_listening.ipynb) |
| **C — อ่านค่าจากเอกสารการวัด** 📄 | pipeline สแกนรายงานการวัด → OCR → สกัดตัวเลข → ตาราง/พล็อต → ตรวจความถูกต้อง | M2 (OCR + ตำแหน่ง bbox), คอร์ส DS (ตาราง/สถิติ/กราฟ) | สแกนใบรับรองการสอบเทียบจำลอง 6 หน้า (`datasets/measurement_reports/`) หรือสแกนของทีม | [starter_trackC_report_ocr.ipynb](starter_trackC_report_ocr.ipynb) |

ทั้งสาม starter **รันจบทั้งไฟล์ได้บนเครื่อง CPU ปกติ (offline)** — เปิด Restart &
Run All ผ่านก่อน แล้วค่อยต่อยอดตามหัวข้อท้ายโน้ตบุ๊กของแต่ละแทร็ก
(แทร็กที่อยากไป CNN/โมเดลหนัก มีคำแนะนำสลับไป Kaggle ในโน้ตบุ๊กนั้น)

## ใช้ข้อมูลจริงของทีม (bring-your-own) — ยินดี และเป็นทางเลือกเต็มรูปแบบ

ทุกแทร็กรองรับข้อมูลของทีมเอง โดยไม่ต้องแก้โครงของ starter เกินจำเป็น
เก็บไฟล์ไว้ที่ `data/capstone_<track>/` (gitignored) — คู่มือเตรียมข้อมูล
(ถ่ายรูป / อัดเสียง / สแกนเอกสาร) อยู่หัวข้อ "ทางทีมต่อยอด" ท้าย starter
ของแต่ละแทร็ก ข้อควรระวังที่ถูกวัดใน rubric: **แบ่ง train/test ข้าม
ล็อตถ่าย/เซสชัน/หน้าเอกสาร** (ไม่สุ่มปนกัน) และอ้างอิง license ของข้อมูลที่นำมา

## การตัดสินใจ: Track C ไม่ใช้ Streamlit (decision record)

- **สถานะ: ไม่ใช้** — ตัดสินใจเมื่อ 2026-09-30 ระหว่างเขียนสื่อ M8 (issue #33)
  สอดคล้องกับ #21 ที่ตัด streamlit ออกจาก stack หลัก
- **เหตุผล:** (1) ผลงาน capstone คือโน้ตบุ๊ก + การพูด 10 นาที — ไม่มีช่องให้
  demo UI แข่งกับเวลาสร้างโมเดลครึ่งวัน (2) ลดพื้นผิวติดตั้งของเครื่อง offline
  (3) Track C สาธิตคุณค่าได้ครบด้วย ตาราง pandas + กราฟ matplotlib ในโน้ตบุ๊ก
- **เงื่อนไขนำกลับมาใหม่:** ถ้า cohort อนาคตมีโจทย์ "ส่งมอบโมเดลถึงมือผู้ใช้"
  (เช่น ให้ช่างใช้ตรวจเองหลังจบคอร์ส) ให้เปิดประเด็นตอนออกแบบหลักสูตรรอบถัดไป —
  ตัวอย่าง Streamlit app เก่าของ capstone v1 ดูได้ที่ branch
  [`archive/v1-course`](https://github.com/utarn/machine-learning-metrology/tree/archive/v1-course)
  (`day3/module10_capstone/app.py`)

## ไฟล์ในโฟลเดอร์

| ไฟล์ | คืออะไร |
|---|---|
| `starter_trackA_defect.ipynb` | starter แทร็ก A — PatchCore + transfer learning บนภาพสังเคราะห์ |
| `starter_trackB_machine_listening.ipynb` | starter แทร็ก B — MFCC + RF บน ESC-50 subset + kNN anomaly จิ๋ว |
| `starter_trackC_report_ocr.ipynb` | starter แทร็ก C — OCR รายงานการวัด → ตัวเลข → ตาราง/พล็อต |
| `rubric.md` | เกณฑ์ให้คะแนน + โครงเวลาการนำเสนอ + แผ่นให้คะแนน (พิมพ์ใช้ได้) |
| `explanation.md` | สคริปต์ภาพประกอบสำหรับผู้สอน (สไลด์ kickoff) |
| `function.md` | ฟังก์ชันที่พบครั้งแรกในโมดูลนี้ |

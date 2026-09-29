# Capstone — Module 10 (Day 3)

โปรเจกต์ปลายทางของหลักสูตร: เลือกทำ **หนึ่งแทร็ก** จากสามแทร็กด้านล่าง ใช้สกิลทั้งหมดจาก Day 1–3 (workflow, feature engineering, การวัดผลซื่อสัตย์, pipeline, การอธิบายโมเดล) บนโจทย์เมโทรโลยีตัวจริง น้ำหนักคะแนนตามนโยบายหลักสูตร: **50% ของหลักสูตร**

| แทร็ก | โน้ตบุ๊ก | โจทย์ | Dataset |
|---|---|---|---|
| A — Predictive maintenance | `capstone_A_predictive_maintenance.ipynb` | ทำนาย **RUL** (อายุที่เหลือ) ของเครื่องยนต์เทอร์โบแฟน — แมปเป็น "เวลาที่เหลือก่อนต้องสอบเทียบซ้ำ" ของเครื่องมือ | NASA C-MAPSS FD001 (`datasets/cmapss_turbofan.zip`) |
| B — Pass/fail classifier | `capstone_B_pass_fail_classifier.ipynb` | จำแนกชิ้นงาน PASS/FAIL บนสายผลิตจริง พร้อมเลือก threshold เทียบ tolerance | UCI SECOM (`datasets/secom.zip`) |
| C — Drift predictor | `capstone_C_drift_predictor.ipynb` | พยากรณ์ drift ของมาตรฐานอ้างอิงและตั้ง **recalibration interval** จากแถบความไม่แน่นอน | NOAA CO₂ (`datasets/co2_mm_gl.csv`) |

## โครงสร้างไฟล์

- `capstone_A/B/C_*.ipynb` — **starter notebooks**: ข้อมูล + กรอบคำถาม + `# TODO` skeletons — ทำลงในไฟล์นี้
- `capstone_C_drift_predictor_solution.ipynb` — **ตัวอย่างเฉลยเต็ม** ของแทร็ก C (ผู้สอน/ดูหลังส่งงาน)
- `app.py` — Streamlit demo app ของแทร็ก C (พยากรณ์ drift แบบอินเทอร์แอ็กทีฟ) — รูปแบบการส่งมอบ "โมเดลถึงมือผู้ใช้" ของ Module 10

## การรัน Streamlit demo

```bash
uv run streamlit run day3/capstone/app.py
```

## สิ่งที่ต้องส่ง (ทุกแทร็ก)

1. โน้ตบุ๊กที่รันผ่านหมด (Restart & Run All ผ่าน) — ทุกเซลล์ TODO เติมแล้ว
2. การวัดผลด้วย split/CV ที่ **ซื่อสัตย์ต่อเวลา** (TimeSeriesSplit หรือ time-based split — ไม่มีการสุ่ม)
3. เทียบกับ baseline ที่ระบุในโน้ตบุ๊ก — รายงานพร้อม dispersion ข้าม fold
4. ส่วนอธิบายโมเดล (SHAP หรือ coefficients) พร้อมประโยคตอบผู้ตรวจแบบที่ฝึกใน Module 9
5. ย่อหน้าสุดท้าย: ข้อจำกัดของโมเดล + สิ่งที่จะทำต่อถ้ามีเวลาอีกสัปดาห์

## เกณฑ์ให้คะแนน (locked, 2026-09-29)

แบบฝึกหัดมีน้ำหนัก **50% ของหลักสูตร** — เต็ม **100 คะแนน เส้นผ่าน 60** เกณฑ์เดียวใช้กับทุกแทร็ก (A/B/C) · งาน **เดี่ยว** (คุยกันได้) · ส่งผ่าน LMS เป็น zip ของโฟลเดอร์ repo + โน้ตบุ๊กที่รันผ่าน · เวลา: ครึ่งวันสุดท้ายของ Day 3 ในห้อง + ส่งได้ภายใน 1 สัปดาห์

| หมวด | น้ำหนัก | สิ่งที่ประเมิน |
|---|---|---|
| ความถูกวิธีการวัดผล (methodology rigor) | **35** | split/CV ซื่อสัตย์ต่อเวลา · แจ้ง baseline และชนะมันจริง · รายงาน dispersion ข้าม fold · ไม่มี leakage (pipeline ใช้ถูกต้อง) |
| คุณภาพการอธิบาย (explanation quality) | **25** | SHAP/coefficients ตีความถูก · ประโยคตอบผู้ตรวจแบบ Module 9 · ข้อจำกัดของโมเดลระบุตรงไปตรงมา |
| Reproducibility & craft | **15** | Restart & Run All ผ่าน · TODO เติมครบ · citation ของ dataset ครบ |
| ประสิทธิภาพดิบของโมเดล | **15** | จูนเหมาะสมไม่ overfit · เบียด naive baseline ได้ |
| Viva (5 นาทีต่อคน) | **10** | อธิบายตัวเลขและผล SHAP ของตัวเองได้ |

- **Viva เป็น gate ด้วย** — ถ้าอธิบาย SHAP output ของโน้ตบุ๊กตัวเองไม่ได้เลย คะแนนรวมถูกจำกัดที่ **50/100** ไม่ว่าหมวดอื่นจะได้เท่าไร (กันงานคัดลอก)
- **ส่งซ้ำได้ 1 ครั้ง** ภายในสัปดาห์ส่งงาน — ซ่อมได้เฉพาะหมวด craft/explanation; ปัญหาด้าน methodology (leakage, วัดผลไม่ซื่อสัตย์) ไม่มีการซ่อม
- แล็บ Modules 0–9 (อีก 50%) ให้คะแนนแบบ **completion + genuine effort** เช็ค 3 ข้อในห้อง: TODO ทุกเซลล์ถูกพยายาม · โน้ตบุ๊กรันผ่านหมด · โจทย์คิดระดับ D พยายามตอบ 2–3 ประโยค — เฉลยเปิดเผยหลังจบช่วงแล็บนั้น
- แบบฝึกหัดแต่ละโมดูลตั้งเป้าเวลาไว้ในหัวโน้ตบุ๊ก (~30 นาที Day 1 / ~45 นาที Day 2 / ~60 นาที Day 3) — การปรับจริงรอข้อมูลห้องเรียนรุ่นแรก

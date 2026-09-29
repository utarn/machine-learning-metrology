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

## เกณฑ์ให้คะแนน

จะประกาศเป็น rubric แยกตอนเปิดภาคเรียน (โครงคร่าว: ความถูกวิธีการวัดผล > คุณภาพการอธิบาย > ประสิทธิภาพดิบของโมเดล — ตามลำดับ)

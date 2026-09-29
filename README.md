# Machine Learning for Advanced Metrology Research — สื่อการเรียน

หลักสูตรฝึกอบรม 3 วัน สำหรับนักวิจัยด้านเมโทรโลยี — โน้ตบุ๊กทั้งหมดรันได้ offline (ชุดข้อมูลใส่มาในโฟลเดอร์ `datasets/` พร้อม citation แล้ว)

## โครงสร้าง

| โฟลเดอร์ | หัวข้อ |
|---|---|
| `day1/environment/` | Module 0 — ติดตั้งสภาพแวดล้อม + พื้นฐาน Python |
| `day1/ml_workflow_eda/` | Module 1 — workflow ของ ML และ EDA |
| `day1/feature_engineering/` | Module 2 — feature engineering |
| `day1/regression/` | Module 3 — sensor calibration curve (regression) |
| `day2/classification/` | Module 4 — pass/fail classification |
| `day2/evaluation/` | Module 5 — model evaluation |
| `day2/clustering/` | Module 6 — clustering |
| `day2/anomaly_detection/` | Module 7 — anomaly detection บน telemetry |
| `day3/time_series/` | Module 8 — time-series forecasting (reference drift) |
| `day3/pipelines_interpretability/` | Module 9 — pipelines & SHAP |
| `day3/capstone/` | Module 10 — capstone (3 แทร็ก) + Streamlit demo |

ในแต่ละหัวข้อ: `book.ipynb` = สื่อประกอบการสอน · `exercise.ipynb` = **แบบฝึกหัดที่คุณทำ** (เติมช่อง `# TODO`) · `explanation.md` = สคริปต์ภาพประกอบ ส่วนไฟล์เฉลย (`solution.ipynb`) ผู้สอนจะเปิดเผยในห้อง **หลังจบช่วงแล็บนั้น ๆ**

## ติดตั้ง (ทำครั้งเดียวก่อนวันแรก)

**Windows:** ดับเบิลคลิก `setup.ps1` (หรือคลิกขวา → Run with PowerShell) — ติดตั้งทุกอย่างให้อัตโนมัติ

**macOS / มี `uv` อยู่แล้ว:**

```bash
uv sync
uv run python smoke_test.py   # ต้องขึ้นว่า PASS
```

**ไม่มี `uv` เลย:** `pip install -r requirements.txt` แล้วรัน `python smoke_test.py`

## เปิดโน้ตบุ๊ก

```bash
uv run jupyter lab
```

(หรือ `jupyter lab` จาก environment ที่ติดตั้งแล้ว) — รันเซลล์ตามลำดับจากบนลงล่างด้วย Shift+Enter

## ข้อมูล

ทุกชุดข้อมูลอยู่ใน `datasets/` พร้อมที่มาและ license — ดู `datasets/README.md` และ citation ที่เซลล์แรกของทุกโน้ตบุ๊กที่ใช้งาน รวมถึงรายละเอียดฉบับเต็มใน `docs/research/datasets.md`

## การส่งงาน

- **แล็บ (Modules 0–9):** ทำใน `exercise.ipynb` — ผู้สอนเช็คความคืบหน้าในห้อง ไม่ต้องส่งไฟล์
- **Capstone (Module 10):** ส่ง zip ของโฟลเดอร์ repo + โน้ตบุ๊กที่รันผ่านผ่าน LMS ภายใน 1 สัปดาห์ — เกณฑ์ให้คะแนนอยู่ใน `day3/capstone/README.md`

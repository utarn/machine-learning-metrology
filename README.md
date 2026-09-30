# Machine Learning for Advanced Metrology Research — สื่อการเรียน

หลักสูตรฝึกอบรม 3 วัน สำหรับนักวิจัยด้านเมโทรโลยี — โน้ตบุ๊กทั้งหมดรันได้ offline (ชุดข้อมูลใส่มาในโฟลเดอร์ `datasets/` พร้อม citation แล้ว)

## โครงสร้าง

| โฟลเดอร์ | หัวข้อ |
|---|---|
| `day1/module0_primer/` | Module M0 — Primer: จากข้อมูลสู่โมเดล (v2) |
| `day1/module1_train_3_ways/` | Module M1 — เทรน 3 แบบบนข้อมูลเดียวกัน: HOG+SVM → CNN → transfer learning (v2) |
| `day1/module2_thai_ocr_bakeoff/` | Module M2 — Thai OCR bake-off: CER ด้วย jiwer + Surya layout/table (v2) |
| `day1/module2_feature_engineering/` | Module 2 — feature engineering |
| `day1/module3_regression/` | Module 3 — sensor calibration curve (regression) |
| `day2/module4_classification/` | Module 4 — pass/fail classification |
| `day2/module5_evaluation/` | Module 5 — model evaluation |
| `day2/module6_clustering/` | Module 6 — clustering |
| `day2/module7_anomaly_detection/` | Module 7 — anomaly detection บน telemetry |
| `day3/module8_time_series/` | Module 8 — time-series forecasting (reference drift) |
| `day3/module9_pipelines_interpretability/` | Module 9 — pipelines & SHAP |
| `day3/module10_capstone/` | Module 10 — capstone (3 แทร็ก) + Streamlit demo |

ในแต่ละหัวข้อ: `book.ipynb` = สื่อประกอบการสอน · `exercise.ipynb` = **แบบฝึกหัดที่คุณทำ** (เติมช่อง `# TODO`) · `explanation.md` = สคริปต์ภาพประกอบ ส่วนไฟล์เฉลย (`solution.ipynb`) ผู้สอนจะเปิดเผยในห้อง **หลังจบช่วงแล็บนั้น ๆ**

## ติดตั้ง (ทำครั้งเดียวก่อนวันแรก)

**Windows:** ดับเบิลคลิก `setup.ps1` (หรือคลิกขวา → Run with PowerShell) — ติดตั้งทุกอย่างให้อัตโนมัติ

**macOS / มี `uv` อยู่แล้ว:**

```bash
uv sync
uv run python smoke_test.py   # ต้องขึ้นว่า PASS
```

**ไม่มี `uv` เลย:** `pip install -r requirements-offline.txt` แล้วรัน `python smoke_test.py`

สภาพแวดล้อม pin ไว้สองทาง (ตาม decision #21):

- **`requirements-offline.txt`** — เครื่องผู้เรียน CPU, ใช้ offline · ติดตั้งผ่าน `uv sync` (ไฟล์ `pyproject.toml` ใช้ pin ชุดเดียวกัน) หรือ pip ด้วยไฟล์นี้
- **`requirements-kaggle.txt`** — โมดูลที่ต้องใช้ GPU บน Kaggle Notebooks (torch ใช้ของ Kaggle ที่ติดตั้งมาแล้ว ดูคอมเมนต์ในไฟล์)

หมายเหตุ: สื่อชุด v1 ที่ยังอยู่ใน `day1/`–`day3/` บางโมดูลใช้ `xgboost`/`shap`/`streamlit` ซึ่งถูกตัดออกจาก stack หลักแล้ว — `uv sync` ยังติดตั้งให้ผ่าน dependency group ชั่วคราว `v1-legacy` (จะลบออกเมื่อสื่อชุดใหม่มาแทนที่) และสำเนาฉบับเต็มของสื่อ v1 เก็บไว้ที่ branch [`archive/v1-course`](https://github.com/utarn/machine-learning-metrology/tree/archive/v1-course)

## ตรวจคุณภาพสื่อ (ผู้ดูแล repo)

```bash
scripts/check_materials.sh
```

ตรวจทุกอย่างในคำสั่งเดียว: flake8 ทุก notebook (ผ่าน nbqa) + execute โน้ตบุ๊กของทุกโมดูล offline ใน env สะอาดจาก `uv.lock` — โมดูล Kaggle GPU อยู่นอกสคริปต์นี้ (ตรวจด้วยมือบน Kaggle ตาม checklist ด้านล่าง)

## ก่อนวันอบรม — checklist

- [ ] **Internet ในห้อง** ใช้งานได้จริง — โมดูล Kaggle (M3, M4-CNN, M5) ต้องใช้; ทดสอบ Wi-Fi + จำนวนอุปกรณ์พร้อมกัน
- [ ] **บัญชี Kaggle รายคน** — ผู้เรียนทุกคนสมัครและยืนยันอีเมล/โทรศัพท์ก่อนวันอบรม (ยืนยันเบอร์เพื่อปลดล็อก GPU/Internet ใน notebook)
- [ ] **เครื่องทดสอบ** — ลองตั้งแต่เครื่องจริง 1 เครื่องของห้อง: `setup.ps1` → `smoke_test.py` ต้องขึ้น PASS → เปิด `uv run jupyter lab` ได้
- [ ] **เครื่องผู้สอน** — รัน `scripts/check_materials.sh` ผ่านก่อนวันสอน
- [ ] **Pre-bundle โมเดล/dataset ลงเครื่อง offline** (ดูแผนด้านล่าง)
- [ ] **ระบบเครื่อง:** Tesseract binary ติดตั้งแล้ว (โมดูล M2 OCR — เป็น system package ไม่ได้อยู่ใน pip): Windows ผ่าน installer ของ UB-Mannheim, macOS `brew install tesseract`, Ubuntu `sudo apt install tesseract-ocr` (ไฟล์ภาษา `tha`/`eng` traineddata อยู่ใน repo แล้วที่ `datasets/tessdata/` — notebook ชี้เองผ่าน `--tessdata-dir`)

## แผน pre-bundle โมเดล/dataset ลงเครื่อง offline

เฉพาะไอเทมที่ **license อนุญาตให้แจกต่อ** (รายละเอียด license ใน `docs/course-outline-v2.md` §6) — ขนาดเป็นค่าประมาณ ให้วัดจริงก่อนเลือกวิธีโฮสต์ (USB / ภายในองค์กร):

| รายการ | ใช้ใน | License | ขนาดโดยประมาณ |
|---|---|---|---|
| Fashion-MNIST | M1, capstone A | MIT | ~30–60 MB |
| torchvision weights: MobileNetV3 (M1), backbone ของ anomalib (M6) | M1, M6 | BSD-3 / Apache-2.0 | ~50–150 MB |
| EasyOCR weights (detection + Thai recognition) | M2 | Apache-2.0 | ~90 MB |
| Tesseract `tha`/`eng` traineddata (tessdata_best) | M2 | Apache-2.0 | ~23 MB — **อยู่ใน repo แล้ว** (`datasets/tessdata/`, notebook ชี้ผ่าน `--tessdata-dir` เอง) |
| openthaigpt/thai-trocr | M2 | Apache-2.0 | ~0.4 GB (วัดจริง — model card เคยประมาณ ~1.3 GB แต่ไฟล์จริง ~411 MB) |
| Surya models (layout ~240 MB + table-rec ~210 MB — surya 0.16.7 pin, ไม่ต้องใช้ foundation/detection) | M2 | code Apache-2.0 — weights ของ Datalab แจกผ่าน S3 ของ datalab เอง ตรวจข้อกำหนดก่อนแจกต่อ | ~0.5 GB |
| thai-ocr-evaluation (test split) | M2 | CC BY-SA 4.0 (share-alike) | ~4 MB — **อยู่ใน repo แล้ว** (`datasets/thai_ocr_evaluation/`) |
| **รวมโดยประมาณ** | | | **~1 GB** (ไม่รวมไฟล์ที่อยู่ใน repo แล้ว) |

**ห้าม pre-bundle (license ไม่อนุญาตแจกต่อเชิงพาณิชย์):**

- **ESC-50** (CC BY-NC 3.0, ~600 MB) — ใช้ในห้องเรียนได้ แต่ให้ผู้เรียน/ผู้สอนดาวน์โหลดเองจาก [GitHub ของ ESC-50](https://github.com/karolpiczak/ESC-50) หรือสลับไปใช้ Speech Commands v2 (CC BY 4.0, ~2.4 GB, แจกต่อได้) ถ้าต้องการชุดที่ bundle ได้
- **MVTec AD** (non-commercial) — ไม่ใช้; M6 ใช้รูปถ่ายจริงของผู้เรียนแทน

ชุดข้อมูลตารางของ v1 ทั้งหมดอยู่ใน `datasets/` แล้ว (license แจกต่อได้ — ดู `datasets/README.md`)

**วิธี pre-bundle โมเดล M2 ลงเครื่อง offline** (รันครั้งเดียวบนเครื่องที่มีอินเทอร์เน็ต
จากนั้นคัดลอกโฟลเดอร์ cache ไปยังเครื่องผู้เรียนที่ตำแหน่งเดียวกัน — notebook
ของ M2 โหลดจากตำแหน่งมาตรฐานเหล่านี้เอง ไม่ต้องตั้งค่าอะไรเพิ่ม):

| โมเดล | ตำแหน่ง cache | คำสั่งเตรียม |
|---|---|---|
| EasyOCR (craft_mlt_25k + thai_g2) | `~/.EasyOCR/model/` (Windows `%USERPROFILE%\\.EasyOCR\\model`) | รันครั้งเดียว: `python -c "import easyocr; easyocr.Reader(['th','en'], gpu=False, verbose=False)"` — ถ้าอยากเก็บไว้ที่อื่น ตั้ง `EASYOCR_MODULE_PATH` แล้วคัดลอกโฟลเดอร์นั้น |
| thai-trocr | HF cache: `~/.cache/huggingface` (macOS ก็ path เดียวกัน) | `python -c "from transformers import TrOCRProcessor, VisionEncoderDecoderModel as M; TrOCRProcessor.from_pretrained('openthaigpt/thai-trocr'); M.from_pretrained('openthaigpt/thai-trocr')"` (หรือตั้ง `HF_HOME` ให้เก็บในโฟลเดอร์ที่ควบคุมได้) |
| Surya (layout + table-rec) | `MODEL_CACHE_DIR` — ค่าเริ่มต้น: `~/Library/Caches/datalab/models` (macOS) / `~/.cache/datalab/models` (Linux) / `%LOCALAPPDATA%\datalab\models` (Windows) | `python -c "from surya.layout import LayoutPredictor; from surya.table_rec import TableRecPredictor; LayoutPredictor(); TableRecPredictor()"` — คัดลอกทั้งโฟลเดอร์ `datalab` ไปยังตำแหน่งเดียวกันบนเครื่องเป้าหมาย (หรือตั้ง `MODEL_CACHE_DIR` ให้ตรง) |

หมายเหตุ: tesseract **binary** ยังเป็น system package ที่ติดตั้งตาม checklist
ด้านบน — ส่วน `tha`/`eng` traineddata ไม่ต้องทำอะไรเพิ่มเพราะอยู่ใน repo แล้ว

## เปิดโน้ตบุ๊ก

```bash
uv run jupyter lab
```

(หรือ `jupyter lab` จาก environment ที่ติดตั้งแล้ว) — รันเซลล์ตามลำดับจากบนลงล่างด้วย Shift+Enter

## ข้อมูล

ทุกชุดข้อมูลอยู่ใน `datasets/` พร้อมที่มาและ license — ดู `datasets/README.md` และ citation ที่เซลล์แรกของทุกโน้ตบุ๊กที่ใช้งาน รวมถึงรายละเอียดฉบับเต็มใน `docs/research/datasets.md`

## การส่งงาน

- **แล็บ (Modules 0–9):** ทำใน `exercise.ipynb` — ผู้สอนเช็คความคืบหน้าในห้อง ไม่ต้องส่งไฟล์
- **Capstone (Module 10):** ส่ง zip ของโฟลเดอร์ repo + โน้ตบุ๊กที่รันผ่านผ่าน LMS ภายใน 1 สัปดาห์ — เกณฑ์ให้คะแนนอยู่ใน `day3/module10_capstone/README.md`

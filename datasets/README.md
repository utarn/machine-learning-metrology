# Shared datasets

Public datasets used across the course, downloaded and committed so every notebook runs offline.
Citations must be repeated in the first markdown cell of every notebook that uses a dataset
(see `docs/research/datasets.md` for BibTeX).

| File | Used in | Source | License |
|---|---|---|---|
| `thai_ocr_evaluation/` | `day1/module2_thai_ocr_bakeoff/`, Capstone Track C | openthaigpt/thai-ocr-evaluation (test split, 104 images + metadata.csv) — https://huggingface.co/datasets/openthaigpt/thai-ocr-evaluation | CC BY-SA 4.0. Citation: Sapsathien, S. & Jaroenkantasima, J. *Thai OCR Evaluation Dataset*, openthaigpt. |
| `tessdata/` | `day1/module2_thai_ocr_bakeoff/` | `tha` + `eng` traineddata (tessdata_best) — https://github.com/tesseract-ocr/tessdata_best | Apache-2.0. |
| `measurement_reports/` | `day1/module2_thai_ocr_bakeoff/`, Capstone Track C | **สื่อที่ผลิตเอง** — สแกนหน้ารายงานการวัดสังเคราะห์ (ภาษาไทย) สร้างด้วย `tools/generate_measurement_reports.py` | ไม่มีลิขสิทธิ์ภายนอก (self-generated, license-clean) — ดู `measurement_reports/README.md` |

โมดูลอื่น ๆ ดึงข้อมูล/โมเดลตอนรันเอง (Fashion-MNIST, ESC-50, Speech Commands,
Wisesight, FLEURS, weights ของ OCR/anomaly) — ดูแผน pre-bundle ใน `README.md`

Notes:

- `thai_ocr_evaluation/` is the official test split as-is: `test/metadata.csv`
  (columns `file_name,text,category`) + `test/images/` (104 PNG line-level crops;
  5 categories — handwritten / document / document_enth / real_document / scene_text).
  CC BY-SA 4.0 is share-alike: if you redistribute a derived dataset, keep the same license.
- `tessdata/` holds the two `traineddata` files the OCR module points Tesseract at via
  `--tessdata-dir` (so no system tessdata location is needed during the workshop).
- `measurement_reports/` is synthetic media produced by
  `tools/generate_measurement_reports.py` (deterministic, seeded — regenerate any time).

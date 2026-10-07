# Shared datasets

Public datasets used across the course, downloaded and committed so every notebook runs offline.
Citations must be repeated in the first markdown cell of every notebook that uses a dataset
(see `docs/research/datasets.md` for BibTeX).

| File | Used in | Source | License |
|---|---|---|---|
| `thai_ocr_evaluation/` | `day1/module2_thai_ocr_bakeoff/`, Capstone Track C | openthaigpt/thai-ocr-evaluation (test split, 104 images + metadata.csv) — https://huggingface.co/datasets/openthaigpt/thai-ocr-evaluation | CC BY-SA 4.0. Citation: Sapsathien, S. & Jaroenkantasima, J. *Thai OCR Evaluation Dataset*, openthaigpt. |
| `tessdata/` | `day1/module2_thai_ocr_bakeoff/` | `tha` + `eng` traineddata (tessdata_best) — https://github.com/tesseract-ocr/tessdata_best | Apache-2.0. |
| `measurement_reports/` | `day1/module2_thai_ocr_bakeoff/`, Capstone Track C | **สื่อที่ผลิตเอง** — สแกนหน้ารายงานการวัดสังเคราะห์ (ภาษาไทย) สร้างด้วย `tools/generate_measurement_reports.py` | ไม่มีลิขสิทธิ์ภายนอก (self-generated, license-clean) — ดู `measurement_reports/README.md` |

โมดูลอื่น ๆ ดึงข้อมูล/โมเดลตอนรันเอง (Wisesight, Speech Commands,
FLEURS — Kaggle GPU modules) — ดูแผน pre-bundle ใน `README.md`

## Pre-bundled for offline (local only — not in git)

รัน `uv run python scripts/prebundle_offline.py` บนเครื่องที่มีอินเทอร์เน็ต — สคริปต์เติมโฟลเดอร์เหล่านี้ให้ครบ (skip ถ้ามีอยู่แล้ว; `--force` เพื่อดาวน์โหลดใหม่) โฟลเดอร์เหล่านี้ **ถูก gitignore** — เครื่องผู้เรียนได้จากการคัดลอก `datasets/` ผ่าน USB/LAN หรือรันสคริปต์เองตอนเตรียม:

| Folder | Contents | Used in | License |
|---|---|---|---|
| `esc50/` | ESC-50 (2,000 clips, 50 classes) — https://github.com/karolpiczak/ESC-50 | `day2/module4_sound_to_numbers/` | **CC BY-NC 3.0** — classroom use only. Citation: Piczak, K. J. (2015). *ESC: Dataset for Environmental Sound Classification*, ACM Multimedia. |
| `fashion_mnist/` | Fashion-MNIST via torchvision layout | M1, M7, Capstone Track A | MIT. Citation: Xiao, Rasul & Vollgraf (2017). |
| `models/hf/` | `openthaigpt/thai-trocr` + timm `wide_resnet50_2.racm_in1k` (HF_HOME) | M2, M6 | Apache-2.0 |
| `models/easyocr/` | craft_mlt_25k + thai_g2 (EASYOCR_MODULE_PATH) | M2 | Apache-2.0 |
| `models/surya/` | Surya layout + table-rec (MODEL_CACHE_DIR, surya 0.16.7) | M2 | code Apache-2.0 — weights ของ Datalab ตรวจข้อกำหนดก่อนแจกต่อ |

Notes:

- `thai_ocr_evaluation/` is the official test split as-is: `test/metadata.csv`
  (columns `file_name,text,category`) + `test/images/` (104 PNG line-level crops;
  5 categories — handwritten / document / document_enth / real_document / scene_text).
  CC BY-SA 4.0 is share-alike: if you redistribute a derived dataset, keep the same license.
- `tessdata/` holds the two `traineddata` files the OCR module points Tesseract at via
  `--tessdata-dir` (so no system tessdata location is needed during the workshop).
- `measurement_reports/` is synthetic media produced by
  `tools/generate_measurement_reports.py` (deterministic, seeded — regenerate any time).

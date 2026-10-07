# Machine Learning for Advanced Metrology Research — สื่อการเรียน

หลักสูตรฝึกอบรม 3 วัน สำหรับนักวิจัยด้านเมโทรโลยี — ML บนข้อมูลไม่มีโครงสร้าง
(ภาพ / ภาษา / เสียง) ครบวงจร **"มีข้อมูล → ให้ ML เรียนรู้ → ได้โมเดล → วัดผล"**
ทุกโมดูล โครงหลักสูตรฉบับเต็มอยู่ที่ `docs/course-outline-v2.md`
สื่อชุดเดิม (v1) เก็บถาวรที่ branch
[`archive/v1-course`](https://github.com/utarn/machine-learning-metrology/tree/archive/v1-course)

## ภาพรวมหลักสูตร 3 วัน

| วัน | ธีม | โมดูล |
|---|---|---|
| **Day 1** | ข้อมูลภาพ: จากตัวเลขสู่โมเดล | M0 Primer · M1 เทรน 3 แบบ (HOG+SVM → CNN → transfer learning) · M2 Thai OCR bake-off (CER) |
| **Day 2** | ข้อมูลภาษาและเสียง: เทรนจริงบนข้อมูลจริง | M3 fine-tune mBERT บน Wisesight · M4 เสียง→ตัวเลข→โมเดล (MFCC+RF / spectrogram CNN) · M5 KWS จากศูนย์ + Demucs + ASR วัด WER |
| **Day 3** | ข้อมูลเฉพาะทาง + capstone | M6 PatchCore จากภาพปกติ ~20 ใบ · M7 Grad-CAM + วิเคราะห์ error ทุก modality · M8 Capstone 3 แทร็ก + นำเสนอ 10 นาที |

## โครงสร้างและการแบ่งแพลตฟอร์มต่อโมดูล

| โฟลเดอร์ | โมดูล | Platform |
|---|---|---|
| `day1/module0_primer/` | M0 — Primer: จากข้อมูลสู่โมเดล | Offline (CPU) |
| `day1/module1_train_3_ways/` | M1 — เทรน 3 แบบบนข้อมูลเดียวกัน: HOG+SVM → CNN → transfer learning | Offline (CPU) |
| `day1/module2_thai_ocr_bakeoff/` | M2 — Thai OCR bake-off: CER ด้วย jiwer + Surya layout/table | Offline (CPU) — **ต้อง pre-bundle โมเดล** (ดูด้านล่าง) |
| `day2/module3_thai_sentiment_mbert/` | M3 — Thai sentiment: fine-tune mBERT บน Wisesight | **Kaggle (GPU T4)** |
| `day2/module4_sound_to_numbers/` | M4 — เสียง→ตัวเลข→โมเดล: MFCC features + random forest บน ESC-50 | Offline (CPU) — ต้องมี ESC-50 บนดิสก์ (ดูด้านล่าง) |
| `day2/module4_esc50_cnn/` | M4-CNN — เทรน spectrogram CNN จากศูนย์ บน ESC-50 | **Kaggle (GPU T4)** |
| `day2/module5_kws_demucs_asr/` | M5 — เทรน KWS CNN จากศูนย์บน Speech Commands v2 + Demucs แยก stems + ASR bake-off Whisper vs Typhoon-ASR-0.6B วัด WER บน FLEURS-Thai | **Kaggle (GPU T4)** |
| `day3/module6_patchcore_anomaly/` | M6 — PatchCore anomaly detection: สอนจากภาพปกติ ~20 ใบ → คะแนน + heatmap | Offline (CPU) — backbone จาก HF cache (ดูด้านล่าง) |
| `day3/module7_grad_cam_error_analysis/` | M7 — วิเคราะห์โมเดลที่เราสร้าง: Grad-CAM บน CNN จาก M1 + metric รวมทุก modality | Offline (CPU) |
| `day3/module8_capstone/` | M8 — Capstone 3 แทร็ก (defect จากภาพ / เสียงเครื่องจักร / OCR รายงานการวัด) + starter + rubric | Offline (CPU) สำหรับ starter ทั้งสาม (ต่อยอด GPU ได้ตามโน้ตบุ๊ก) |

ในแต่ละหัวข้อ: `book.ipynb` = สื่อประกอบการสอน · `exercise.ipynb` = **แบบฝึกหัดที่คุณทำ** (เติมช่อง `# TODO`) · `explanation.md` = สคริปต์ภาพประกอบ ส่วนไฟล์เฉลย (`solution.ipynb`) ผู้สอนจะเปิดเผยในห้อง **หลังจบช่วงแล็บนั้น ๆ** — โมดูล capstone (M8) ใช้ starter notebook แทร็กละ 1 ไฟล์แทน book/exercise (ดู `day3/module8_capstone/README.md`)

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

หมายเหตุ: สำเนาฉบับเต็มของสื่อชุดเดิม (v1) เก็บไว้ที่ branch [`archive/v1-course`](https://github.com/utarn/machine-learning-metrology/tree/archive/v1-course) — repo นี้บรรจุเฉพาะสื่อชุด v2 แล้ว

## ตรวจคุณภาพสื่อ (ผู้ดูแล repo)

```bash
scripts/check_materials.sh
```

ตรวจทุกอย่างในคำสั่งเดียว: flake8 ทุก notebook (ผ่าน nbqa) + execute โน้ตบุ๊กของทุกโมดูล offline (M0, M1, M2, M4-RF, M6, M7, M8) ใน env สะอาดจาก `uv.lock` — โมดูล Kaggle GPU (M3, M4-CNN, M5) อยู่นอกสคริปต์นี้ (ตรวจด้วยมือบน Kaggle ตาม checklist ด้านล่าง)

## ก่อนวันอบรม — checklist

สามรายการ Kaggle T4 (M3, M4-CNN, M5) ต้อง **validate ด้วยมือบน Kaggle จริง 1 รอบต่อโมดูล** — สคริปต์ตรวจสื่อ lint ให้แต่ไม่ execute โมดูล GPU เหล่านี้ จึงต้องแต๊กเฉพาะเมื่อรันจริงบน Kaggle แล้วเท่านั้น

- [ ] **Internet ในห้อง** ใช้งานได้จริง — โมดูล Kaggle (M3, M4-CNN, M5) ต้องใช้; ทดสอบ Wi-Fi + จำนวนอุปกรณ์พร้อมกัน
- [ ] **บัญชี Kaggle รายคน** — ผู้เรียนทุกคนสมัครและยืนยันอีเมล/โทรศัพท์ก่อนวันอบรม (ยืนยันเบอร์เพื่อปลดล็อก GPU/Internet ใน notebook)
- [ ] **Kaggle T4 — validate โมดูล M3 ด้วยมือ 1 รอบ** — รัน `day2/module3_thai_sentiment_mbert/book.ipynb` ท็อป-ท้ายจบบน Kaggle (Accelerator: GPU T4, Internet: On) ก่อนวันอบรม — สคริปต์ตรวจสื่อ lint ให้แต่ไม่ execute โมดูล Kaggle
- [ ] **Kaggle T4 — validate โมดูล M4-CNN ด้วยมือ 1 รอบ** — รัน `day2/module4_esc50_cnn/book.ipynb` ท็อป-ท้ายจบบน Kaggle (GPU T4, Internet: On) — ใช้เวลาราว 20–25 นาที (ดาวน์โหลด ESC-50 ~600 MB รวมอยู่ใน notebook แล้ว) — จด accuracy ของสองวิธีจากรอบนั้นไว้เทียบในห้อง
- [ ] **Kaggle T4 — validate โมดูล M5 ด้วยมือ 1 รอบ** — รัน `day2/module5_kws_demucs_asr/book.ipynb` ท็อป-ท้ายจบบน Kaggle (Accelerator: GPU T4, Internet: On) — ตรวจว่า KWS เทรนจบใน ~30 นาที + ได้ accuracy ที่อ่านผลได้, Demucs เปิดฟัง stems ได้, ตาราง WER ออกมาจริง — สคริปต์ตรวจสื่อ lint ให้แต่ไม่ execute โมดูล Kaggle
- [ ] **ESC-50 (M4-RF)** — อยู่ใน `datasets/esc50/` (ไม่ track ใน git) คัดลอกจากเครื่องผู้สอน หรือให้เครื่องผู้เรียนรัน pre-bundle เองก่อนวันอบรม; ย้ำกับห้องว่า license CC BY-NC 3.0 ห้ามใช้เชิงพาณิชย์
- [ ] **เครื่องทดสอบ** — ลองตั้งแต่เครื่องจริง 1 เครื่องของห้อง: `setup.ps1` → `smoke_test.py` ต้องขึ้น PASS → เปิด `uv run jupyter lab` ได้
- [ ] **เครื่องผู้สอน** — รัน `scripts/check_materials.sh` ผ่านก่อนวันสอน
- [ ] **Pre-bundle โมเดล/dataset ลงเครื่อง offline** — รัน `uv run python scripts/prebundle_offline.py` บนเครื่องที่มีอินเทอร์เน็ต (หรือคัดลอก `datasets/` จากเครื่องที่เตรียมแล้ว) ดูแผนด้านล่าง
- [ ] **ระบบเครื่อง:** Tesseract binary ติดตั้งแล้ว (โมดูล M2 OCR — เป็น system package ไม่ได้อยู่ใน pip): Windows ผ่าน installer ของ UB-Mannheim, macOS `brew install tesseract`, Ubuntu `sudo apt install tesseract-ocr` (ไฟล์ภาษา `tha`/`eng` traineddata อยู่ใน repo แล้วที่ `datasets/tessdata/` — notebook ชี้เองผ่าน `--tessdata-dir`)

## แผน pre-bundle โมเดล/dataset ลงเครื่อง offline

ทุกอย่างที่โมดูล offline ต้องใช้อยู่ใน `datasets/` ทั้งหมด — **ไม่ track ใน git** (ขนาด ~2.7 GB เกินเหตุผลสำหรับ repo; เครื่องผู้เรียนได้จากการคัดลอกโฟลเดอร์ `datasets/` ผ่าน USB/LAN จากเครื่องผู้สอน หรือรันสคริปต์เองตอนเตรียม) โน้ตบุ๊กชี้เข้า `datasets/` เองในเซลล์ setup (ถ้าไฟล์ pre-bundle ยังไม่มี จะ fallback ไป default cache / ดาวน์โหลดเองตามเดิม)

**เตรียมบนเครื่องที่มีอินเทอร์เน็ต (ครั้งเดียว):**

```bash
uv sync
uv run python scripts/prebundle_offline.py              # ทุก step
uv run python scripts/prebundle_offline.py --only esc50 # ทีละ step
uv run python scripts/prebundle_offline.py --force      # ดาวน์โหลดใหม่ทั้งหมด
```

ได้โฟลเดอร์ (ขนาดเป็นค่าประมาณ):

| โฟลเดอร์ | สิ่งที่อยู่ข้างใน | ใช้ใน | ~ขนาด |
|---|---|---|---|
| `datasets/esc50/ESC-50-master/` | ESC-50 เต็ม 2,000 คลิป | M4-RF | ~600 MB |
| `datasets/fashion_mnist/` | Fashion-MNIST | M1, M7, capstone A | ~60 MB |
| `datasets/models/hf/` | thai-trocr + timm `wide_resnet50_2.racm_in1k` (HF_HOME) | M2, M6 | ~0.5 GB |
| `datasets/models/easyocr/` | craft_mlt_25k + thai_g2 (EASYOCR_MODULE_PATH) | M2 | ~90 MB |
| `datasets/models/surya/` | Surya layout + table-rec (MODEL_CACHE_DIR) | M2 | ~0.5 GB |
| `datasets/models/torch/` | MobileNetV3-Small ImageNet weights (TORCH_HOME) | M1 | ~10 MB |

**หมายเหตุ license** — การคัดลอกโฟลเดอร์ `datasets/` ไปเครื่องผู้เรียนนับเป็นการใช้ในห้องเรียน ไม่ใช่การแจกต่อสาธารณะ: ESC-50 เป็น CC BY-NC 3.0 (ห้ามเชิงพาณิชย์) และ Surya weights เป็นของ Datalab (ตรวจข้อกำหนดก่อนแจกต่อนอกองค์กร) — ที่เหลือ Apache-2.0/BSD/MIT (รายละเอียด license ใน `docs/course-outline-v2.md` §6)

**ทดสอบว่า offline จริง** (หลัง pre-bundle เสร็จ):

```bash
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 scripts/check_materials.sh
```

โมดูล Kaggle GPU (M3, M4-CNN, M5) **ไม่อยู่ใน pre-bundle** — notebook ดาวน์โหลดข้อมูลเองบน Kaggle (Internet: On)

MVTec AD (non-commercial) — ไม่ใช้; M6 ใช้รูปถ่ายจริงของผู้เรียนแทน

หมายเหตุ: tesseract **binary** ยังเป็น system package ที่ติดตั้งตาม checklist
ด้านบน — ส่วน `tha`/`eng` traineddata อยู่ใน repo แล้วที่ `datasets/tessdata/`

## เปิดโน้ตบุ๊ก

```bash
uv run jupyter lab
```

(หรือ `jupyter lab` จาก environment ที่ติดตั้งแล้ว) — รันเซลล์ตามลำดับจากบนลงล่างด้วย Shift+Enter

## ข้อมูล

ทุกชุดข้อมูลอยู่ใน `datasets/` พร้อมที่มาและ license — ดู `datasets/README.md` และ citation ที่เซลล์แรกของทุกโน้ตบุ๊กที่ใช้งาน รวมถึงรายละเอียดฉบับเต็มใน `docs/research/datasets.md`

## การส่งงาน

- **แล็บ (M0–M7):** ทำใน `exercise.ipynb` — ผู้สอนเช็คความคืบหน้าในห้อง ไม่ต้องส่งไฟล์
- **Capstone (M8):** ส่ง zip ของโฟลเดอร์ repo + โน้ตบุ๊กที่รันผ่านผ่าน LMS ภายใน 1 สัปดาห์ — เกณฑ์ให้คะแนนอยู่ใน `day3/module8_capstone/README.md`

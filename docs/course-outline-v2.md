# Course Outline v2 — Machine Learning กับข้อมูลไม่มีโครงสร้าง สำหรับนักวิจัยด้านเมโทรโลยี

> ฉบับปรับใหม่ของหลักสูตร "Machine Learning for Advanced Metrology Research" (3 วัน)
> สังเคราะห์จาก wayfinder map [#14](https://github.com/utarn/machine-learning-metrology/issues/14) — decisions จาก #19 (datasets/models), #20 (โครงสร้างรายวัน), #21 (toolchain/lab environment), #22 (metrology flavor/capstone)
>
> **สถานะ: ร่างเพื่อรีวิว** — เอกสารนี้คือ input ของงานเขียนสไลด์/notebook จริง (effort ถัดไป)

---

## 1. ภาพรวมหลักสูตร

| หัวข้อ | ค่าที่ lock ไว้ |
|---|---|
| รูปแบบ | 3 วัน, บรรยาย + demo เป็นหลัก, lab เบาๆ ต่อโมดูล |
| ผู้เรียน | นักวิจัยด้านเมโทรโลยี (กลุ่มเดิม) — สมมติผ่านคอร์ส **Data Science 2 วัน** มาแล้ว (หรือมีพื้นฐานเทียบเท่า) |
| ระดับ | กลางแบบภาพรวม — survey หลาย modality, ไม่ลงสูตรคณิตลึก, ไม่เทรนโมเดลจากศูนย์แบบใหญ่ |
| แกนเนื้อหา | **ML บน unstructured data** — image, text/OCR, sound + การวิเคราะห์ผล |
| ปรัชญาของทุกโมดูล | วงจร **"มีข้อมูล → ให้ ML เรียนรู้ → ได้โมเดล → วัดผล"** ครบทุกโมดูล — ผู้เรียน "สร้างโมเดลเอง" ~7 ครั้งตลอด 3 วัน |
| สิ่งที่ไม่มี | ไม่ใช้ LLM/VLM เป็นแกนของโมดูลใด; ไม่สอนหัวข้อ DS ตารางคลาสสิก (EDA, regression, classification, clustering, time-series — อยู่ในคอร์ส DS 2 วัน) |
| เส้นแบ่งกับคอร์ส DS 2 วัน | หลักสูตรนี้สมมติพื้นฐาน DS แล้ว; มี primer สั้นต้นวัน 1 + โน้ตช่วยกลุ่มที่ยังไม่ได้เรียน (รองรับการสลับลำดับการอบรม) |

---

## 2. ตารางเวลาและโมดูล

### Day 1 — ข้อมูลภาพ: จากตัวเลขสู่โมเดล

| เวลา | โมดูล | จุดประสงค์ (เมื่อจบ ผู้เรียน...) | เนื้อหา/lab | Platform | Dataset / โมเดล |
|---|---|---|---|---|---|
| 09:00–10:00 | **M0 Primer: จากข้อมูลสู่โมเดล** | ทบทวนวงจร data→train→evaluate (train/test, overfitting, metric) และเห็นว่า unstructured data ถูกแทนเป็นตัวเลขอย่างไร (pixels / tokens / spectrograms) | บรรยาย + demo สั้น; ตั้งสภาพแวดล้อม (uv sync offline / Kaggle login) | Offline (CPU) | — |
| 10:15–12:00 | **M1 เทรน 3 แบบบนข้อมูลเดียวกัน** | สร้างโมเดลจำแนกภาพด้วย 3 วิธีและอธิบายได้ว่า deep learning ชนะตรงไหน-ทำไม | Lab: HOG+SVM (ตาราง) → **เทรน CNN จากศูนย์** → **transfer learning** (MobileNetV3, freeze backbone + เทรน head) เทียบ accuracy + confusion matrix; แทรก learning-curve สั้น (subset 5%/25%/100%) | Offline (CPU) | Fashion-MNIST (MIT) · sklearn + torchvision |
| 13:00–14:30 | **M2 Thai OCR: ข้อมูลทดสอบ → CER** | วัดผลโมเดลด้วย dataset ทดสอบและอ่านผลเปรียบเทียบได้ (CER) | Lab: **OCR bake-off** 3 โมเดล (EasyOCR / Tesseract `tha` / thai-trocr) บนภาพเอกสารไทย + Surya layout/table extraction; **ภาพตัวอย่างใช้สแกนหน้ารายงานการวัด** (สื่อเมโทรโลยีเฉพาะจุดนี้) + Typhoon-OCR-3B เป็น demo ผู้สอน | Offline (CPU) — ต้อง **pre-bundle โมเดล** | thai-ocr-evaluation (CC BY-SA 4.0) · EasyOCR / pytesseract+`tha` / thai-trocr / Surya (ทั้งหมด Apache-2.0) · jiwer วัด CER |
| 14:45–16:30 | **สรุปวันที่ 1 + ถาม-ตอบ** | เชื่อม "ตัวเลข→โมเดล" ของวันแรกกับ metric ที่วัดได้ | ทบทวน confusion matrix/CER; เกริ่นโจทย์วัน 2 (ข้อมูลภาษาและเสียง) | — | — |

### Day 2 — ข้อมูลภาษาและเสียง: เทรนจริงบนข้อมูลจริง

| เวลา | โมดูล | จุดประสงค์ | เนื้อหา/lab | Platform | Dataset / โมเดล |
|---|---|---|---|---|---|
| 09:00–10:30 | **M3 สอนโมเดลอ่านใจจากข้อความไทย** | fine-tune โมเดลภาษาบนข้อมูลไทยและอ่าน precision/recall ต่อ class ได้ | Lab: demo PyThaiNLP word segmentation (ทำไมไทยตัดคำยาก) → **fine-tune mBERT** บนข้อความ sentiment ไทย — เห็น loss ลดจริง epoch ต่อ epoch; demo สั้น 5 นาที: embedding + kNN | **Kaggle (GPU)** | Wisesight Sentiment (CC0, 26,737 ข้อความ) · mBERT (Apache-2.0) · PyThaiNLP |
| 10:45–12:00 | M3 ต่อ + วิเคราะห์ผล | อ่านผล per-class และชี้ class ที่โมเดลอ่อน | Lab ต่อ: error inspection ต่อ class; สรุป zero-shot vs supervised | Kaggle (GPU) | จาก M3 |
| 13:00–14:30 | **M4 เสียง→ตัวเลข→โมเดล** | แปลงเสียงเป็น features (ตัวเลข!) แล้วเทรนสองวิธีบนข้อมูลเดียวกัน | Lab: MFCC/mel features + **เทรน random forest** (สะพานจากคอร์ส DS) vs **เทรน spectrogram CNN** บน ESC-50 — เทียบ accuracy | Offline (CPU) สำหรับ RF / Kaggle สำหรับ CNN | ESC-50 (CC BY-NC ⚠️ ไม่แจกต่อเชิงพาณิชย์) · librosa + sklearn + torch |
| 14:45–16:30 | **M5 เทรนโมเดลฟังเสียงจากศูนย์** | เทรนโมเดลเสียงด้วยมือของตัวเองจากข้อมูลดิบ | Lab: **เทรน keyword-spotting CNN** จากศูนย์ บน Speech Commands (~30 นาทีบน T4); demo: **Demucs** แยกเสียงร้อง/กลอง/เบสจากเพลงของผู้เรียน + เทียบ ASR ไทย (Whisper vs Typhoon-ASR-0.6B) วัด WER บน FLEURS-Thai | **Kaggle (GPU)** | Speech Commands v2 (CC BY 4.0) · FLEURS-Thai (CC BY 4.0) · demucs (MIT) · Whisper/Typhoon-ASR (Apache-2.0) |

### Day 3 — ข้อมูลเฉพาะทาง: สอนจากข้อมูลน้อย + สังเคราะห์

| เวลา | โมดูล | จุดประสงค์ | เนื้อหา/lab | Platform | Dataset / โมเดล |
|---|---|---|---|---|---|
| 09:00–10:15 | **M6 สอนโมเดลจากภาพ "ปกติ" เพื่อจับความผิดปกติ** 🏭 | สร้างโมเดลตรวจความผิดปกติจากข้อมูลน้อย (~20 ภาพ) — โจทย์จริงของงานเมโทรโลยี | Lab: **anomalib PatchCore** เทรนจากภาพปกติ → ให้คะแนนภาพชำรุด + anomaly heatmap; ใช้รูปเครื่องมือ/ชิ้นงานของผู้เรียนเอง | Offline (CPU) | รูปถ่ายของผู้เรียน + anomalib (Apache-2.0) |
| 10:30–11:30 | **M7 วิเคราะห์โมเดลที่เราสร้าง** | มองเข้าไปในโมเดลและวิเคราะห์ความพลาดอย่างเป็นระบบ | Lab/demo: **Grad-CAM** บน CNN ที่เทรนเองใน M1 + รวม metric ทุก modality (accuracy / CER / WER) — "โมเดลพลาดอะไร ทำไม" | Offline (CPU) | โมเดลจาก M1 |
| 11:30–12:00 | **Capstone kickoff** | เลือก track และข้อมูลของทีม | แบ่งทีม 2–3 คน, เลือก 1 ใน 3 track (ดู §3), รับ starter dataset | ตาม track | ตาม track |
| 13:00–15:00 | **M8 Capstone — สร้าง** | สร้างโมเดล end-to-end ด้วยมือของทีม | ข้อมูล → เทรน → วัดผล → เตรียมนำเสนอ (ผู้สอนเดินให้คำปรึกษา) | ตาม track | starter จากหลักสูตร หรือข้อมูลจริงของทีม |
| 15:00–16:30 | **M8 Capstone — นำเสนอ + ปิดหลักสูตร** | นำเสนอผลงานและรับ feedback | นำเสนอทีมละ ~10 นาที — **ใช้เป็นการวัดผลของหลักสูตรไปในตัว** (ไม่มี quiz แยก); demo ผู้สอนเสริมได้: SAM2 / Depth Anything | — | — |

---

## 3. Capstone — 3 tracks

สมมติผู้เรียนผ่านคอร์ส DS 2 วัน — ทุก track ออกแบบให้**ใช้เทคนิค DS คลาสสิกผสมได้อย่างชัดเจน**

| Track | โจทย์ | ทักษะที่ reuse จากหลักสูตรนี้ | ทักษะ DS คลาสสิกที่ผสม | Starter dataset |
|---|---|---|---|---|
| **A — ตรวจ defect จากภาพ** 🏭 | จำแนกภาพชิ้นงาน/เครื่องมือ ปกติ-ชำรุด + รายงาน confusion matrix | M1 (transfer learning), M6 (PatchCore) | evaluation metrics | Fashion-MNIST หรือรูปถ่ายของทีม |
| **B — ฟังเสียงเครื่องจักร** 🔊 | จำแนกเสียงจาก MFCC/spectrogram features | M4, M5 | RF, feature engineering | ESC-50 / Speech Commands หรือเสียงจริงของทีม |
| **C — อ่านค่าจากเอกสารการวัด** 📄 | pipeline OCR หน้ารายงานการวัด → สกัดค่าตัวเลข → วิเคราะห์/พล็อตแบบตาราง | M2 (OCR + CER) | regression/analysis จากคอร์ส DS | ภาพสแกนรายงานการวัดตัวอย่าง (สื่อที่เตรียม) หรือสแกนของทีม |

**ข้อมูล**: starter dataset จากหลักสูตรทุก track (รับประกันว่าทำจบในครึ่งวัน) — เปิดให้ทีมใช้ข้อมูลจริงของตัวเองถ้ามี
**ผลงาน**: notebook + นำเสนอ ~10 นาที/ทีม (การวัดผลของหลักสูตร)

---

## 4. Toolchain และสภาพแวดล้อม (จาก #21)

### แพลตฟอร์ม — สองทาง ไม่ใช้ Colab
- **เครื่องผู้เรียน (CPU, offline)** — โมดูลเบา: M0, M1, M2, M4 (RF), M6, M7 — ติดตั้งผ่าน `uv sync` (path เดิมของ repo), ไม่ต้องพึ่ง internet ระหว่างสอน
- **Kaggle Notebooks (GPU T4×2/P100)** — โมดูลหนัก: M3 (mBERT), M4 (spectrogram CNN), M5 (KWS/Demucs/ASR), capstone track ที่ต้องการ GPU

### Framework ฐานเดียว
- **PyTorch**: torch + torchvision + torchaudio + transformers + datasets
- **sklearn** (คงจาก stack เดิม) สำหรับโมดูลสะพาน M1/M4 — SVM, RF
- คงเดิม: numpy / pandas / matplotlib / jupyterlab
- **ตัดออกจาก stack หลัก**: xgboost, shap (แทนด้วย Grad-CAM), streamlit (ตัดสินใหม่ตอนเขียน capstone material — Track C อาจใช้)

### ต่อ modality
- **OCR**: easyocr + pytesseract (tesseract-ocr + `tha` traineddata) + thai-trocr (transformers) + surya — ทั้งหมด pip/torch ระบบเดียว
- **Sound**: librosa + torchaudio + transformers (Whisper) + demucs + Typhoon-ASR-0.6B
- **Anomaly**: anomalib (official)
- **Metrics**: jiwer (CER/WER) + sklearn metrics

### Reproducibility
- ทุก notebook มี `%pip install -r` cell ท็อปไฟล์ — เปิดรันได้ทันที
- Pin สองไฟล์: `requirements-offline.txt` (เบา, CPU) และ `requirements-kaggle.txt` (GPU) — เขียนตอนสร้าง material
- คง `uv sync` เป็น offline install path เดิม

---

## 5. โครงสร้างไฟล์ (คง convention เดิมของ repo)

```
day1/moduleN_<slug>/
  book.ipynb        # เนื้อหา+demo ตามที่ผู้สอนเดิน
  exercise.ipynb    # โจทย์ lab ของผู้เรียน
  explanation.md    # อธิบายเชิงลึก (เช่น PatchCore algorithm ใน M6)
  solution.ipynb    # เฉลย
datasets/           # dataset ที่ pre-bundle ได้ (license แจกต่อได้)
```

---

## 6. License summary (ของทุกสิ่งที่ใช้)

| รายการ | License | ข้อควรระวัง |
|---|---|---|
| Fashion-MNIST | MIT | แจกต่อได้, pre-bundle ได้ |
| thai-ocr-evaluation | CC BY-SA 4.0 | แจกต่อได้ (share-alike) |
| Wisesight Sentiment | CC0 | แจกต่อได้เต็มที่ |
| Speech Commands v2 | CC BY 4.0 | แจกต่อได้ (attribute) |
| FLEURS-Thai | CC BY 4.0 | แจกต่อได้ (attribute) |
| **ESC-50** | **CC BY-NC 3.0** ⚠️ | **non-commercial** — ใช้ในห้องเรียนฟรีได้ แต่ **ห้าม bundle ลงสื่อที่แจกต่อเชิงพาณิชย์**; ทางเลือก clean: Speech Commands v2 |
| EasyOCR / Tesseract / thai-trocr / Surya / mBERT / demucs / Whisper / Typhoon-ASR / anomalib / torchvision weights | Apache-2.0 / MIT / BSD-3 | แจกต่อได้ |

---

## 7. งานที่ต้องทำก่อนวันอบรม (hand-off checklist)

- [ ] เขียน notebook/exercise/solution ทั้ง 8 โมดูล ตาม outline นี้ (effort ใหม่)
- [ ] เตรียมภาพสแกนหน้ารายงานการวัดตัวอย่าง สำหรับ M2 + capstone Track C (สื่อเมโทรโลยี)
- [ ] **Pre-bundle โมเดล/dataset ลงเครื่อง offline** — เฉพาะไอเทม license แจกต่อได้ (§6); วัดขนาดรวมและเลือกวิธีโฮสต์
- [ ] สร้าง `requirements-offline.txt` / `requirements-kaggle.txt` แบบ pin รุ่น + ทดสอบบน Kaggle จริง 1 รอบ
- [ ] ยืนยันความพร้อมของห้องอบรม: internet (สำหรับโมดูล Kaggle) + บัญชี Kaggle ของผู้เรียนทุกคน
- [ ] ตัดสินใจจัดการโมดูล v1 เดิมใน repo (แทนที่ในที่เดิม vs เก็บ archive branch) — ทำตอน material ชุดใหม่พร้อมแล้ว
- [ ] ตัดสินใจว่า capstone Track C ใช้ streamlit หรือไม่ (ตัดจาก stack หลักชั่วคราวตาม #21)

---

## 8. สิ่งที่ถูกพิจารณาแล้วและตัดออก (จาก grilling)

- **LLM/VLM เป็นแกนโมดูล** (RAG-lite กับ Typhoon 4B, Qwen2-VL Q&A) — ตัดตามความต้องการ "เน้น machine learning แท้ๆ"
- **Zero-shot เป็นหลักของโมดูล** (SigLIP, OWLv2, CLAP) — ตัดเพราะไม่มีวงจร "ข้อมูล→เทรน"; CLAP/SigLIP อาจกลับมาเป็น demo
- **RT-DETR detector fine-tune** — ต้องเตรียม bounding-box label เอง (friction สูงสุดของหลักสูตร)
- **หัวข้อ DS ตารางคลาสสิก** (regression, classification, clustering, time-series) — ย้ายไปคอร์ส DS 2 วัน
- **Thai image dataset** — ไม่มีตัวเลือกที่ license ใช้ได้จริง (ยืนยันจาก #19); จุดภาษาไทยของหลักสูตรอยู่ที่ OCR/text/sound

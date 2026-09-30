# explanation.md — Module M6: PatchCore — สอนโมเดลจากภาพ "ปกติ" เพื่อจับความผิดปกติ

โมดูลนี้เป็นโมดูลเดียวของหลักสูตรที่ `explanation.md` มีหน้าที่ **อธิบาย algorithm เชิงลึก** (ตาม outline §5) — โน้ตบุ๊กสอน "ใช้ยังไง" ส่วนไฟล์นี้อธิบาย "ทำงานยังไงและทำไม" แยกจากกัน

---

## 1. ทำไมต้อง one-class anomaly detection

ในงานตรวจรับ/สอบเทียบเชิงภาพ การสร้าง classifier สองคลาส (M1) ติดปัญหาจริง 3 ข้อ:

1. **Defect หลากหลายไม่รู้จบ** — ขีดข่วน, รูสึก, คราบ, บิดเบี้ยว, ต่างกันไปตามชิ้นงาน; เก็บตัวอย่างพร้อม label ให้ครบทุกแบบแพงและไม่มีวันครบ
2. **Defect หายาก** — อัตราชำรุดจริงอาจต่ำร้อยล้น ทำให้ชุดเทรนที่สมดุลต้อง "ปลอม" defect ขึ้นมา
3. **Defect ใหม่เกิดขึ้นได้** — โมเดลที่เรียน "เส้นแบ่งระหว่างคลาส" จะไม่รู้จัก defect แบบที่ไม่เคยเห็น

PatchCore ย้อนปัญหา: **เรียนรู้เฉพาะ "ความปกติ"** แล้วนิยามว่า anomaly คือสิ่งที่ "อยู่ไกลจากความปกติที่เคยเห็น" — ใช้ภาพปกติเท่านั้น (one-class / unsupervised) ข้อแลกเปลี่ยนคือเราได้ **คะแนนความแปลก (anomaly score)** ไม่ใช่การวินิจฉัยชนิด defect — เหมือนการตรวจ tolerance: เรารู้ว่า "นอกค่ากลาง = ไม่ผ่าน" โดยไม่ต้องไล่ว่าผิดเพราะอะไร

---

## 2. Pipeline ของ PatchCore ภาพรวม

```
ภาพปกติ N ใบ
   │  (1) backbone ImageNet (frozen) — สกัด feature กลาง
   ▼
patch embeddings ทุกตำแหน่งของทุกภาพ  ──► (2) neighborhood aggregation
   │
   ▼
memory bank  M = {patch feature ทั้งหมด}
   │  (3) coreset subsampling — ย่อเหลือ ~1–10%
   ▼
coreset  C  ⊂ M   (ตัวแทนที่ "คลุม" ทุก patch ปกติ)
   ▲
   │  (4) kNN ต่อ patch ของภาพใหม่ → ระยะต่อ patch
ภาพใหม่ ──► (5) upsample + Gaussian smooth = anomaly map
              (6) max ต่อภาพ = image-level score
```

หัวใจของ algorithm คือ **"ความปกติ = ตารางเทียบ" ไม่ใช่ "ฟังก์ชันที่เทรนด้วย gradient"** — ขั้น (1)–(3) คือทั้งหมดของการ `fit`, ขั้น (4)–(6) คือการ `predict`

---

## 3. (1) Backbone features — ทำไมเป็น layer2/layer3 กลาง ๆ

PatchCore ใช้ WideResNet-50-2 ที่เทรน ImageNet มาแล้ว **แช่แข็งทั้งตัว** และดึง activation จากชั้น**กลาง** (`layer2`, `layer3`) ไม่ใช่ชั้นท้าย:

- **ชั้นท้าย** (หลัง global average pooling) เหลือเวกเตอร์เดียวต่อภาพ — หายตำแหน่งไปหมด จับ "รอยขีดตรงมุมล่าง" ไม่ได้
- **ชั้นกลาง** ยังเป็น **feature map ตามตำแหน่ง** (spatial grid): ภาพ 256×256 ผ่าน layer2 ได้กริด 64×64 และ layer3 ได้ 32×32 — patch หนึ่งชิ้น = เวกเตอร์ 1 ตำแหน่ง (128 และ 256 มิติตามลำดับ) — receptive field ของแต่ละ patch ครอบพื้นที่เล็ก ๆ (~พื้นที่ระดับ texture ถึง ส่วนของวัตถุ) พอดีกับ "ตำหนิเฉพาะจุด"
- **ทำไม weights ของ ImageNet:** feature กลางของ CNN ที่เทรนข้อมูลทั่วไปแล้วจะจับ "texture/ขอบ/ลวดลาย" ที่ transfer ข้ามโดเมนได้ดี (เคยเห็นแล้วใน M1) — PatchCore **ไม่เทรนต่อ** จึงใช้ได้ทันทีกับแผ่นโลหะ/เครื่องมือที่ ImageNet ไม่เคยเห็น

ใน anomalib กำหนดผ่าน `Patchcore(layers=("layer2", "layer3"))` — feature จากสองชั้นถูก concaten เป็นเวกเตอร์ต่อ patch

---

## 4. (2) Neighborhood aggregation — สงบเสียงรบกวนก่อนเก็บ

ก่อนเก็บลง memory bank, PatchCore แทน patch แต่ละชิ้นด้วย **ค่าเฉลี่ยของมันกับ k patch รอบข้างในภาพเดียวกัน** (k=3 ใน anomalib default) — เหตุผล: ตำหนิจริงมัก "เลอะ" กินหลายพิกเซล ส่วน noise ของกล้องเป็นแบบจุดเดียวโดด ๆ การเกลี่ยกับเพื่อนบ้านเชิงพื้นที่เก็บ texture จริงไว้แต่ลบ noise เฉพาะจุดทิ้ง — ทำให้ memory bank สะอาดขึ้นและ false positive จาก sensor noise ลดลง

---

## 5. (3) Coreset subsampling — หัวใจเชิงประสิทธิภาพ

**ปัญหา:** memory bank ดิบใหญ่มาก — ภาพ 256×256 ให้ patch หลายพันชิ้นต่อภาพ, 20 ภาพ = หลายหมื่นเวกเตอร์ × 384 มิติ และตอน predict ต้องหาระยะไป**ทุก** patch — O(N) ต่อ patch ต่อภาพใหม่ ช้าและกิน RAM จนใช้งานจริงไม่ได้

**ทางแก้: coreset** — เลือก subset C ⊂ M ขนาด r·|M| (r = `coreset_sampling_ratio`, default 0.1) ให้ **patch ทุกชิ้นใน M อยู่ใกล้ patch สักชิ้นใน C ให้มากที่สุด** (min-max facility location): C ที่ดี = ตัวแทนครอบคลุมทั้ง distribution ของ "ความปกติ" โดยคะแนน kNN ที่คำนวณกับ C ใกล้เคียงกับที่คำนวณกับ M ทั้งก้อน

**Greedy farthest-point:** หา optimal ตรง ๆ เป็น NP-hard — PatchCore ใช้ greedy:

1. เริ่มด้วย patch ที่ไกลจาก centroid ที่สุด
2. วนซ้ำ: เลือก patch ที่ **ระยะถึงตัวที่เลือกแล้วทั้งหมด (min) มีค่ามากที่สุด (max)** — คือ patch ที่ "ยังไม่ถูกตัวแทนคลุม" มากที่สุด
3. จบเมื่อได้ครบ r·|M| ตัว

ให้การรับประกันแบบ approximation (1 − 1/e) ของปัญหา min-max — เพียงพอเชิงปฏิบัติ

**ทำให้เร็วขึ้นอีกด้วย random projection:** greedy ต้องคำนวณระยะระหว่าง patch หมื่น ๆ ชิ้นทุกรอบ — anomalib (ตามต้นฉบับ) ใช้ **sparse random projection** ย่อเวกเตอร์ก่อนเลือก coreset โดยอาศัย **Johnson–Lindenstrauss lemma**: จุด N จุดในมิติ d ถูกฉายลงมิติ O(log N / ε²) โดยระยะคู่กันเปลี่ยนไม่เกิน (1±ε) — ระยะที่ใช้ "เลือก" จึงเชื่อถือได้แม้มิติเล็กลงมาก แล้วคำนวณ kNN จริงตอน predict ด้วยเวกเตอร์เต็ม

**ผลข้างเคียงที่ผู้เรียนควบคุมได้:** `coreset_sampling_ratio` ต่ำ → memory bank เล็ก (เร็ว, ใช้ RAM น้อย) แต่ความครอบคลุมลด — patch ปกติที่ "หายากในธรรมชาติของตัวเอง" อาจไม่มีตัวแทน แล้วกลายเป็น false positive — นี่คือสิ่งที่ exercise ข้อ 2 ให้ลอง

---

## 6. (4)–(6) Scoring — จากระยะสู่คะแนนและ heatmap

ให้ patch ของภาพใหม่ x และ coreset C:

- **ระยะต่อ patch:** d(p) = ระยะ Euclidean ไป patch ใน C ที่ใกล้สุดอันดับ k (ค่าเฉลี่ยของ k ตัว — re-weight ด้วย softmax ในต้นฉบับเพื่อให้ตัวที่ 2–k มีน้ำหนักเมื่อใกล้กันมาก)
- **anomaly map:** จัด d(p) กลับเป็นกริดตามตำแหน่ง patch → upsample (bilinear) ขึ้นเป็นขนาดภาพ → **Gaussian smoothing** เบา ๆ ลบรอยหยักจากการ upsample — ผลลัพธ์คือ heatmap ที่โน้ตบุ๊กวาด
- **image score:** **ค่า max ของ map** — ตรรกะแบบ QC: ภาพไหนมี patch เดียวที่ชำรุดก็ "ไม่ผ่านทั้งภาพ" (สอดคล้อง tolerance ของงานเมโทรโลยี: ชิ้นงานผิดพลาดจุดเดียวก็ไม่ผ่าน) — ต้นฉบับเพิ่ม re-weighting ของ max ด้วย softmax ระหว่าง patch แต่หลักการเดียวกัน

**จุดสำคัญที่ต่างจาก classifier:** คะแนนนี้เป็น**ระยะจริง** (มีหน่วยเชิง feature-space) ไม่ใช่ความน่าจะเป็น — ค่า 200 ไม่ได้แปลว่า "แปลก 2 เท่าของ 100" ในเชิงสถิติ แต่เทียบ**สัมพัทธ์**กับการกระจายของคะแนนภาพปกติเท่านั้น

---

## 7. Threshold — ขั้นที่โมเดลไม่ทำให้เรา

anomalib default จะ fit **post-processor** ที่หา threshold อัตโนมัติจาก validation set (maximize F1 — adaptive threshold) แล้ว normalize คะแนนให้อยู่ 0–1 รอบ ๆ threshold นั้น

โน้ตบุ๊กของโมดูลนี้**ปิด** ( `post_processor=False` ) เพราะ 2 เหตุผล:

1. การเรียนรู้: ผู้เรียนต้องเห็นว่า threshold คือ**การตัดสินใจเชิงต้นทุน** (FP vs FN) ไม่ใช่ผลลัพธ์อัตโนมัติของโมเดล — maximize F1 ไม่ใช่คำตอบที่ถูกเสมอสำหรับงานตรวจรับ (ดู book หัวข้อ 5 และ exercise ข้อ 3)
2. บนชุดเล็กมาก adaptive threshold ไม่เสถียร (estimation จากไม่กี่ภาพ) — คะแนน normalize แล้วดูเหมือน 0/1 กระโดด จนอ่าน histogram ไม่ได้

ถ้าใช้งานจริงกับ anomalib เต็มรูปแบบ ให้คง post-processor default ไว้แต่**ต้องมี validation set ของภาพปกติ+ชำรุดที่ดีพอ** — เป็น trade-off เดียวกับทุกโมดูลก่อนหน้า

---

## 8. เมื่อไหร่ PatchCore พัง (และวิธีเห็นทัน)

| อาการ | กลไกที่ผิด | สัญญาณ |
|---|---|---|
| วัตถุเลื่อน/หมุนในเฟรม | patch ตำแหน่งใหม่ไม่เคยมีใน bank → FP ทั้งภาพ | heatmap ร้อนกระจายทั้งภาพ ไม่จุดเดียว |
| แสง/กล้องเปลี่ยน | feature ทั้งภาพ shift → FP | histogram ของภาพ "ปกติใหม่" ไปรวมกับกลุ่มชำรุด |
| defect เล็กกว่า 1 patch | ถูกเกลี่ย/ถูก smooth หาย | score สูงขึ้นเล็กน้อยแต่ไม่ผ่าน threshold |
| ภาพปกติที่ให้เทรนมี defect แฝง | bank "กลืน" defect เป็นความปกติ | FN ของ defect แบบนั้นเสมอ |

เคล็ดแบบเมโทรโลยี: ให้เช็ค **score ของภาพปกติที่ถ่ายใหม่ (fresh normal)** ทุกครั้งหลังเทรน — ถ้า fresh normal ได้คะแนนสูงใกล้ threshold แสดงว่า bank ยังไม่ครอบคลุม "ความปกติทั้งหมด" (สภาพถ่ายหลากหลายพอ) — เพิ่มภาพปกติที่หลากหลายขึ้นแล้วเทรนซ้ำ = "ขยาย tolerance band" ของโมเดล

---

## 9. การตัดสินใจเครื่องมือ (decision record)

**เลือก: anomalib 2.6.2 (official) แทนการเขียน PatchCore เองด้วย torch+sklearn**

- วัดจริงใน env ของ harness (CPU, offline): `engine.fit` + scoring ชุด 20 ปกติ/8 ชำรุด ที่ 256×256 จบใน **< 60 วินาที** — ต่ำกว่า timeout 600 s ของ harness มาก จึงไม่จำเป็นต้องเขียนเอง
- ประเด็นที่ต้อง override จาก default (เขียนไว้ในโน้ตบุ๊กแล้ว): `num_workers=0` (worker process ล้มบน macOS ใน notebook), `post_processor=False` (อยากได้คะแนนดิบเพื่อสอน threshold), `visualizer=False` (ไม่ให้เขียนไฟล์เอง), `accelerator="cpu"`, **สร้าง `Engine` ใหม่ทุกครั้งที่ fit ซ้ำ** — Engine เก่าที่เคย fit แล้วจะไม่ populate memory bank ให้โมเดลอินสแตนซ์ใหม่ (พบเองตอนเขียน solution ข้อ 2)
- backbone weights มาจาก timm `wide_resnet50_2.racm_in1k` (Hugging Face) — ดาวน์โหลดครั้งแรก ~130 MB ลง `~/.cache/huggingface/` เครื่อง offline pre-bundle โดยคัดลอก cache นี้ (ดู README แผน pre-bundle)

**อะไรที่เราไม่ใช้:** ชุดข้อมูล MVTec AD — benchmark มาตรฐานของวงการ แต่ license **CC BY-NC-SA 4.0 (non-commercial)** จึงเลี่ยงตามนโยบาย license ของ repo — ใช้ภาพสังเคราะห์ + รูปถ่ายของผู้เรียนแทน (และเหมาะกับเป้าหมาย "ผู้เรียนใช้ของตัวเองได้" มากกว่า)

---

## 10. License + อ้างอิง

| รายการ | License | หมายเหตุ |
|---|---|---|
| anomalib (โค้ด) | Apache-2.0 | <https://github.com/open-edge-platform/anomalib> |
| timm `wide_resnet50_2.racm_in1k` weights | Apache-2.0 | <https://huggingface.co/timm/wide_resnet50_2.racm_in1k> |
| timm (โค้ด) | Apache-2.0 | ใช้เป็น feature extractor wrapper ใน anomalib |
| PyTorch / torchvision | BSD-3-Clause | backbone runtime |
| MVTec AD | CC BY-NC-SA 4.0 | **ไม่ใช้** — non-commercial |

**อ้างอิงหลัก:**

- Roth, K., Penate Sanchez, L., Meier, J., & Ommer, B. (2022). *Towards Total Recall in Industrial Anomaly Detection* (PatchCore). CVPR 2022 · <https://arxiv.org/abs/2106.08265>
- Zagoruyko, S., & Komodakis, N. (2016). *Wide Residual Networks*. BMVC 2016 · <https://arxiv.org/abs/1605.07146>
- Johnson, W. B., & Lindenstrauss, J. (1984). *Extensions of Lipschitz mappings into a Hilbert space*. (รากฐานของ random projection ที่ใช้ใน coreset selection)
- anomalib documentation — PatchCore guide: <https://anomalib.readthedocs.io/en/stable/markdown/guides/reference/models/image/patchcore.html>

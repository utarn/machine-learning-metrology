# explanation.md — Module M1: เทรน 3 แบบบนข้อมูลเดียวกัน

สคริปต์ภาพประกอบสำหรับผู้สอน — แต่ละหัวข้อ = หนึ่งภาพ: แนวคิด (ไทย) → จุดประสงค์ → องค์ประกอบ → image-gen prompt (English)

---

## Figure 1 — Three ways to train on the same data

**แนวคิด:** ข้อมูลชุดเดียวกัน สามปรัชญาต่างกัน: คนออกแบบ feature / โมเดลเรียนรู้เอง / ยืม feature ผู้อื่น

**จุดประสงค์ของภาพ:** ให้ผู้เรียนเห็นภาพรวมทั้ง lab ก่อนลงโค้ด — และจำได้ว่า input เดียวกัน เส้นทางต่างกัน

**องค์ประกอบภาพ:** ภาพเสื้อเชิ้ตขาวดำ 28×28 อยู่ซ้ายสุด แตกสามลูกศรไปสามแถว: (1) "HOG" กริดลูกศรทิศทาง → "SVM" → ผลจำแนก, (2) "CNN" ชั้น conv ซ้อน → ผลจำแนก, (3) "MobileNetV3 (ImageNet)" ปราสาท/หอคอยแข็งแรง (frozen, หิมะปิด = freeze) + กล่อง head เล็กใหม่ → ผลจำแนก

**Image-gen prompt:**
> Educational diagram: one grayscale 28x28 t-shirt image on the left branches into three horizontal pipelines; top pipeline "HOG + SVM" showing a grid of gradient orientation arrows feeding a classifier; middle pipeline "CNN from scratch" showing stacked convolution layers; bottom pipeline "transfer learning" showing a large frozen building (icy, snow-capped, labeled ImageNet) with a small warm-colored trainable head box attached; all three end in a classification result; flat vector infographic style, white background, teal-coral-slate palette.

---

## Figure 2 — HOG: counting edge directions

**แนวคิด:** HOG แปลงภาพเป็น "histogram ทิศทางขอบ" ต่อ cell — feature ที่คนออกแบบ

**จุดประสงค์ของภาพ:** ให้ผู้เรียนเห็นกลไก 3 ขั้น: gradient → นับมุมต่อ cell → normalize เป็นเวกเตอร์

**องค์ประกอบภาพ:** ภาพเสื้อ 28×28 → ลูกศร → ภาพเดียวกันซ้อนลูกศรสั้น ๆ ทุกพิกเซล (ชี้ตาม gradient) → ลูกศร → กริด 7×7 ช่อง แต่ละช่องมี rose diagram (วงกลม 9 ก้าน) → ลูกศร → แถบเวกเตอร์ยาว 441 ช่อง

**Image-gen prompt:**
> Step-by-step HOG feature pipeline in three stages connected by arrows: stage 1 a small grayscale clothing image; stage 2 the same image overlaid with short gradient direction arrows at each pixel; stage 3 a 7x7 grid where each cell contains a small circular histogram with 9 spokes; final arrow to a long feature vector strip labeled "441 dimensions"; flat vector style, white background, technical but friendly, teal-coral palette.

---

## Figure 3 — CNN from scratch: learning what to look at

**แนวคิด:** ชั้น conv เรียนรู้ตัวกรองจากข้อมูล — ขอบหยาบในชั้นต้น ทรงซับซ้อนในชั้นหลัง

**จุดประสงค์ของภาพ:** ให้ผู้เรียนเห็นว่า "โมเดลออกแบบ feature เอง" หมายความว่าอะไร ต่างจาก HOG

**องค์ประกอบภาพ:** แผนผังซ้าย→ขวา: ภาพ 28×28 → Conv 16 ตัวกรอง (แสดงตัวกรองขอบ/มุม) → Pool ย่อขนาด → Conv 32 ตัวกรองทรง → Pool → Flatten → Linear 10 ทางออกพร้อมชื่อคลาสเสื้อผ้า มีป้าย "น้ำหนักทั้งหมดเริ่มสุ่ม — เรียนจากข้อมูล"

**Image-gen prompt:**
> CNN architecture diagram left to right: 28x28 grayscale image input, a layer of 16 small filter tiles (edge and corner detectors), a downsampling pool step, a layer of 32 richer shape filter tiles, another pool step, a flatten strip, and a final linear layer with 10 output slots labeled with clothing class names; a badge reading "all weights learned from data — no human-designed features"; flat vector style, white background, teal-coral-slate palette.

---

## Figure 4 — Transfer learning: freeze the backbone, train the head

**แนวคิด:** ยืมความรู้จาก ImageNet (1.2 ล้านภาพ) โดยไม่แตะน้ำหนักเดิม — เทรนเฉพาะหัวใหม่ให้ตรงโจทย์

**จุดประสงค์ของภาพ:** ทำให้ "freeze + head" เป็นภาพจำ — เหมาะกับข้อมูลน้อย

**องค์ประกอบภาพ:** อาคารหลายชั้นใหญ่ (backbone) มีโซ่/น้ำแข็ง = frozen มีป้าย "MobileNetV3 — เทรนบน ImageNet แล้ว" บนดาดฟ้ามีกล่องเล็กกำลังก่อสร้าง (ไอคอนช่าง/ครกปูน) ป้าย "head ใหม่ — เทรนด้วยข้อมูลของเรา (10k ภาพ)" ลูกศรจากภาพเสื้อเข้าอาคาร และออกจากกล่อง head เป็น 10 คลาส

**Image-gen prompt:**
> Transfer learning metaphor diagram: a tall multi-story building labeled "MobileNetV3 backbone - trained on ImageNet" wrapped in chains and ice (frozen, snowflake icons); on its roof a small construction-site box with a crane labeled "new head - trained on our 10k images"; an arrow carries a small clothing image into the building entrance and exits the rooftop box as 10 class labels; flat vector infographic style, white background, teal-coral-slate palette, friendly technical illustration.

---

## Figure 5 — Learning curve: what little data buys

**แนวคิด:** ข้อมูลน้อย → ทุกวิธีแย่ลง แต่ไม่เท่ากัน — feature ที่ออกแบบดีช่วยได้ตอนข้อมูลน้อย, โมเดลที่เรียนรู้เองชนะเมื่อข้อมูลพอ

**จุดประสงค์ของภาพ:** หัวใจเมโทรโลยีของโมดูล — ผู้เรียนต้องจำ "เส้นโค้งนี้" ไปใช้กับข้อมูลของตัวเอง

**องค์ประกอบภาพ:** กราฟเส้น 3 เส้น แกน x = จำนวนภาพเทรน (500 / 2,500 / 10,000) แกน y = test accuracy ทุกเส้นเดินขึ้น: จุดซ้าย (500) วงกลม "HOG+SVM" สูงสุด, จุดขวา (10,000) เส้น "CNN" แซงขึ้นสูงสุด, เส้น "Transfer" อยู่กลาง — มีแถบข้อความ "ข้อมูลน้อย → เลือกอาวุธให้ถูก"

**Image-gen prompt:**
> Line chart with three rising curves over training-set size on the x-axis (three tick marks: 500, 2500, 10000 images) and test accuracy on the y-axis; curves labeled "HOG + SVM" (highest at the left end), "Transfer learning" (middle), and "CNN from scratch" (lowest at left, highest at right), all monotonically increasing; a small caliper icon and caption "less data, worse model — choose your weapon"; clean scientific plot style, flat vector, white background, teal-coral-slate colors.

---

## Figure 6 — Where models fail: reading 10x10 confusion matrices

**แนวคิด:** โมเดลไม่พลาดแบบสุ่ม — พลาดเป็นคู่ ๆ ที่หน้าตาคล้ายกัน (Shirt/T-shirt/Pullover/Coat)

**จุดประสงค์ของภาพ:** ฝึกอ่าน confusion matrix 10×10 ให้เห็น "โครงสร้างความผิดพลาด" ไม่ใช่แค่ accuracy

**องค์ประกอบภาพ:** heatmap 10×10 แนวทแยงเข้ม (ถูก) ช่องนอกแนวทแยงส่วนใหญ่จาง แต่มีคลัสเตอร์แดง 3–4 ช่องรอบ ๆ แถว/คอลัมน์ Shirt, T-shirt, Pullover, Coat มีป้ายชี้คลัสเตอร์ "ตระกูลเสื้อ — แยกยาก"

**Image-gen prompt:**
> Annotated 10x10 confusion matrix heatmap, strong dark diagonal cells, mostly faint off-diagonal cells, but a visible cluster of red cells grouped around the rows and columns for shirt-like classes (Shirt, T-shirt, Pullover, Coat) with an arrow annotation labeled "shirt family — easily confused"; axis labels as small clothing icons and text; clean scientific figure style, white background, red-to-blue diverging scale.

# explanation.md — Module M7: วิเคราะห์โมเดลที่เราสร้าง (Grad-CAM + metric รวม)

สคริปต์ภาพประกอบสำหรับผู้สอน — แต่ละหัวข้อ = หนึ่งภาพ: แนวคิด (ไทย) → จุดประสงค์ → องค์ประกอบ → image-gen prompt (English)

---

## Figure 1 — Grad-CAM: ถามโมเดลด้วย gradient ว่ามองตรงไหน

**แนวคิด:** Grad-CAM ไม่เปิด "สมอง" โมเดลทั้งก้อน แต่ถามคำถามเดียวให้จบ: ถ้าคะแนนของ class นี้ต้องเพิ่มขึ้น บริเวณไหนของ feature map ชั้น conv สุดท้ายต้องรับผิดชอบ — gradient คือคำตอบ เฉลี่ยต่อช่อง (GAP) คือน้ำหนัก แล้วรวมช่องทั้ง 32 ด้วยน้ำหนักนั้น

**จุดประสงค์ของภาพ:** ให้ผู้เรียนเห็น dataflow ครบ 3 ขั้นในภาพเดียว (forward จับ activation → backward จับ gradient → ถ่วงน้ำหนัก + ReLU) ก่อนอ่านโค้ด hook

**องค์ประกอบภาพ:** ซ้าย — ภาพเสื้อขาวดำ 28×28 ไหลเข้าโมเดล 3 ก้อน (Conv→Pool→Conv→Pool→Flatten→Linear 10 ทาง) เส้นทึบ = forward, เส้นประสีแดง = backward ของ "คะแนน class 'Shirt'" ย้อนกลับมาหยุดที่ feature map ชั้น conv สุดท้าย (สแตกการ์ด 32 ใบ ขนาด 7×7); ขวา — แสดงการคำนวณ: การ์ดแต่ละใบถูกให้น้ำหนัก α (ตัวเลขจาก gradient) แล้วผลรวมเข้าฟังก์ชัน ReLU ได้ heatmap 7×7 ที่บางช่องร้อนบางช่องเย็น จบด้วยลูกศร "ขยาย 7×7 → 28×28"

**Image-gen prompt:**
> Educational diagram of Grad-CAM data flow: left side a small grayscale shirt image flows through a compact CNN drawn as stacked blocks (Conv, Pool, Conv, Pool, Flatten, Linear with 10 outputs); solid teal arrows show the forward pass while a dashed red arrow carries the gradient of one class score backward, stopping at the final convolution feature maps drawn as a stack of 32 small 7x7 cards; right side shows each card weighted by a small alpha badge, summed into a single 7x7 heatmap after a ReLU gate, then an arrow labeled "upsample" stretching the heatmap onto the original shirt image; flat vector infographic style, white background, teal-coral-slate palette.

---

## Figure 2 — อ่าน overlay: ความร้อนของ CAM vs ความละเอียดที่เสียไป

**แนวคิด:** CAM ซ้อนบนภาพเดิม (สี magma, โปร่งแสง ~50%) — สีสว่าง = บริเวณที่ดันคะแนน class นั้น แต่เพราะ feature map ชั้นสุดท้ายแค่ 7×7 ของภาพ 28×28 การขยายกลับมาเลยเบลอเป็นบล็อก — "ที่ไหน" คร่าว ๆ เชื่อได้ "ขอบเขตเป๊ะ ๆ" ไม่ได้

**จุดประสงค์ของภาพ:** ตั้งความคาดหวังให้ถูกก่อนผู้เรียนตีความ heatmap เกินจริง

**องค์ประกอบภาพ:** ภาพเดียวกันสามชั้นซ้อนแบบ exploded view: (1) ภาพเสื้อขาวดำ 28×28, (2) heatmap 7×7 ต้นฉบับแสดงเป็นตาราง 49 ช่องสี magma, (3) heatmap ที่ขยายแล้วซ้อนโปร่งแสงบนภาพ — มีป้ายกำกับ "7x7 = coarse but meaningful" และลูกศรชี้ความกว้างของบล็อกหนึ่งว่า "= 4x4 pixels ของต้นฉบับ"

**Image-gen prompt:**
> Exploded-view educational diagram with three stacked layers of the same grayscale shirt image: bottom layer the crisp 28x28 image, middle layer the raw 7x7 Grad-CAM heatmap shown as a grid of 49 colored cells (magma colormap, some hot some cold), top layer the heatmap bilinearly upsampled and overlaid with transparency on the image showing blocky blur; annotation labels "7x7 = coarse but meaningful" and an arrow noting one heatmap cell covers a 4x4 pixel block of the original; flat vector style, white background, teal-coral palette.

---

## Figure 3 — ตาราง metric รวม: สาม modality, หน่วยความผิดสามแบบ

**แนวคิด:** accuracy / CER / WER ทำงานบน "หน่วยยิบ" ต่างกัน (ทั้งภาพ / อักขระ / คำ) แต่ล้วนห่อเป็น "อัตราความผิดพลาด" 0–1 ได้ — เทียบระดับความยากของโจทย์ได้ เทียบ "ราคาของความผิด" ตรง ๆ ไม่ได้

**จุดประสงค์ของภาพ:** ยึดกฎการอ่าน: เทียบได้หลังแปลงสเกล + ต้องถามเสมอว่า "ความผิด 1 หน่วยของ metric นี้แพงแค่ไหนในงานจริง"

**องค์ประกอบภาพ:** กราฟแท่งแนวนอน 3 กลุ่ม: ภาพ (1−accuracy ~0.13, สีน้ำเงิน "รันสด"), OCR สามแท่ง (CER 0.17/0.39/0.89, สีส้ม "ค่าตัวอย่าง"), เสียง (WER 0.25, สีส้ม "รอค่าจริงจาก M5") — แกนเดียว 0–1 ป้าย "lower is better"; ใต้กราฟมีแถบรูปไอคอนสามตัว: ภาพเต็มใบ / ตัวอักษรเดี่ยว / คำเดียว พร้อมข้อความ "same scale, different unit"

**Image-gen prompt:**
> Horizontal bar chart of error rates on a single 0-1 axis labeled "lower is better": one blue bar "image: CNN, 1-accuracy 0.13" tagged "live run", three orange bars "OCR: CER 0.17 / 0.39 / 0.89" tagged "example values", one orange bar "audio: WER 0.25" tagged "placeholder"; below the chart a legend strip with three icons — a full image frame, a single character, a single word — captioned "same scale, different unit"; clean scientific chart style, white background, blue and orange palette.

---

## Figure 4 — วงจร error inspection 4 ขั้น

**แนวคิด:** การวิเคราะห์ความผิดที่ต่อยอดได้จริงต้องเป็นระบบ: รวบรวม error ครบ → จัดกลุ่ม (คู่สับสน/ประเภทข้อมูล) → มองตัวอย่างจริง (ตา + CAM) → ตั้งสมมติฐานแล้วแก้ตรงจุด

**จุดประสงค์ของภาพ:** ให้ผู้เรียนจำเป็นกระบวนการ ไม่ใช่กิจกรรมครั้งเดียว — และเห็นว่า CAM อยู่ตรงขั้น 3 เท่านั้น

**องค์ประกอบภาพ:** วงกลมลูกศร 4 ขั้น: (1) "collect — list error ทั้งหมด" ไอคอนตะกร้า, (2) "cluster — คู่สับสน + ประเภทข้อมูล" ไอคอนแท็ก, (3) "inspect — ตา + CAM" ไอคอนแว่นขยายบนภาพ heatmap, (4) "act — สมมติฐาน → ข้อมูล/โมเดล/กระบวนการ" ไอคอนประแจ; ขั้น 3 มีเครื่องหมายเน้นว่า Grad-CAM อยู่ตรงนี้เท่านั้น และลูกศรย้อนกลับจากขั้น 4 ไปขั้น 1 เขียน "หลังแก้ — วัดรอบใหม่"

**Image-gen prompt:**
> Circular four-step process diagram with arrows: step 1 "collect" with a basket icon gathering error cards, step 2 "cluster" with tag icons grouping cards by confusion pair, step 3 "inspect" highlighted with a magnifying glass over a heatmap image and a badge reading "Grad-CAM lives here", step 4 "act" with a wrench icon pointing to data/model/process fix labels; a return arrow from step 4 back to step 1 labeled "re-measure after the fix"; flat vector infographic style, white background, teal-coral-slate palette, numbered steps.

---

## Figure 5 — CAM ของ pred vs CAM ของ true: วินิจฉัยชนิดของความผิด

**แนวคิด:** ภาพที่โมเดลผิดมีสอง "ชนิด" — ถ้า CAM ของ pred และ true ทับกันมาก = มองถูกที่แต่หลักฐานไม่พอแยก (ข้อจำกัดของข้อมูล) ถ้าชี้คนละที่ = มองผิดจุดตั้งแต่ต้น (สัญญาณ shortcut learning ต้องตรวจข้อมูล)

**จุดประสงค์ของภาพ:** ให้ผู้เรียนมี "กฎการอ่าน" ที่ชัดสำหรับ error inspection ของตัวเอง

**องค์ประกอบภาพ:** สองแถวเทียบกัน: แถวบน — ภาพเสื้อผ้าคู่หนึ่ง (true ซ้าย, pred ขวา) มี heatmap สองอันซ้อนเกือบทับกัน ป้าย "overlap = data problem"; แถวล่าง — ภาพที่ heatmap ของ pred ไปติดมุมภาพ (พื้นหลัง) ขณะ CAM ของ true อยู่บนวัตถุ ป้าย "no overlap = shortcut suspect"; มีไอคอนตะกร้อ/สัญญาณเตือนที่แถวล่าง

**Image-gen prompt:**
> Two-row educational comparison of misclassified images: top row shows a clothing image with two heatmaps (predicted class and true class) overlapping almost entirely on the garment body, labeled "overlap = data problem, evidence too weak"; bottom row shows an image where the predicted-class heatmap sits in an empty corner while the true-class heatmap covers the object, labeled "no overlap = shortcut suspect" with a small warning icon; flat vector style, white background, magma-colored heatmaps, teal-coral palette.

---

## Figure 6 — Grad-CAM ไม่ใช่คำอธิบายเชิงสาเหตุ

**แนวคิด:** CAM บอกว่าโมเดล "ใช้หลักฐานจากตรงไหน" — ไม่ได้พิสูจน์ว่าเพราะบริเวณนั้นโมเดลจึงตัดสินอย่างนั้น และ heatmap ที่ "ดูสมเหตุสมผล" ไม่การันตีว่าโมเดลถูก (มีงานวิจัยแสดง CAM สวยได้ทั้งที่โมเดลโกง) — จึงต้องใช้คู่กับการตรวจข้อมูลและตัวเลขบน test set

**จุดประสงค์ของภาพ:** วางขอบเขต epistemic ของเครื่องมือ — เหมาะกับหัวข้อ "traceability" ของงานเมโทรโลยี

**องค์ประกอบภาพ:** แผนภาพสองฝั่ง: ซ้าย "Grad-CAM ตอบ" — ภาพ heatmap พร้อมตราประทับ "where the model looked"; ขวา "Grad-CAM ไม่ตอบ" — สามรายการเขียนกากบาท: "why (causal)", "is it correct", "is it fair" มีเครื่องหมายคำถาม; ระหว่างสองฝั่งมีแถบ "+ ต้องเสริมด้วย: test metrics, error inspection, data audit"

**Image-gen prompt:**
> Two-panel educational diagram contrasting what Grad-CAM provides: left panel a heatmap-overlaid image stamped "answers: where the model looked"; right panel a list with three crossed-out items "why (causal explanation)", "is the model correct", "is the model fair" each marked with a question mark; between the panels a connecting strip reading "must be paired with: test metrics, error inspection, data audit"; flat vector infographic style, white background, teal and coral accents, honest scientific tone.

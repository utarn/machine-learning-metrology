# explanation.md — Module M0: Primer — จากข้อมูลสู่โมเดล

สคริปต์ภาพประกอบสำหรับผู้สอน — แต่ละหัวข้อ = หนึ่งภาพ: แนวคิด (ไทย) → จุดประสงค์ → องค์ประกอบ → image-gen prompt (English)

---

## Figure 1 — The data → train → evaluate loop

**แนวคิด:** ทุกโมดูลในหลักสูตรเดินวงจรเดียวกัน — คำถามนำข้อมูล ข้อมูลนำโมเดล และการวัดผลปิดวงจรเสมอ

**จุดประสงค์ของภาพ:** ให้ผู้เรียนจำ "วงจรเดียว, สามช่อง" ก่อนเห็นเทคนิคใด ๆ ทั้งสิ้น

**องค์ประกอบภาพ:** วงจรลูกศร 4 ขั้น: Data → Split (train/test แยกสี) → Train (กล่องโมเดล) → Evaluate (หน้าปัดเครื่องมือวัด/metric) พร้อมลูกศรวนกลับจาก Evaluate ไป Train ติดป้าย "ปรับโมเดล" และไอคอนเครื่องมือวัดกำกับขั้น Data

**Image-gen prompt:**
> Clean circular flow diagram with four labeled stages: "Data" (stack of measurement records with a caliper icon), "Split train/test" (a bar divided into two colored blocks labeled train and test), "Train" (a machine-learning model box with gears), "Evaluate" (a gauge/metric dial with accuracy score); an arrow loops back from Evaluate to Train labeled "tune"; flat vector style, white background, teal-coral-slate palette, numbered circles, no photorealism.

---

## Figure 2 — Underfit / good fit / overfit

**แนวคิด:** ความยากของโมเดลต้องพอดีกับรูปแบบในข้อมูล — ตัดสินจาก test เท่านั้น

**จุดประสงค์ของภาพ:** ประทับใจสามสภาพ โดยเฉพาะ overfit (โมเดลจำ noise) ที่ MSE train สวยแต่ test พัง

**องค์ประกอบภาพ:** สามแผงเทียบกัน แต่ละแผงมี scatter จุดข้อมูล sine + เส้นโมเดล: แผงซ้าย เส้นตรงผ่านกลาง (underfit), แผงกลาง เส้นโค้งตาม sine (good fit), แผงขวา เส้นบิดเบี้ยววิ่งไล่จุดทุกจุด (overfit) — ใต้แผงขวามีป้าย "MSE train ต่ำ / MSE test สูง"

**Image-gen prompt:**
> Three side-by-side scientific scatter plots comparing model fits to noisy sine-wave data: left panel a straight line through the middle labeled "underfit", middle panel a smooth curve following the sine shape labeled "good fit", right panel a wildly wiggly curve passing through every point labeled "overfit" with a caption bar reading "low train error, high test error"; small data points in blue, model curve in coral, flat vector style, white background, minimal axes.

---

## Figure 3 — Reading a confusion matrix

**แนวคิด:** accuracy ตัวเดียวไม่พอ — confusion matrix บอกว่าโมเดลพลาด "ทางไหน" และงานเมโทรโลยีราคาของความพลาดสองทางไม่เท่ากัน

**จุดประสงค์ของภาพ:** ให้ผู้เรียนอ่านแนวทแยง/ช่องนอกแนวทแยงได้ และเข้าใจ FP vs FN ในบริบท pass/fail

**องค์ประกอบภาพ:** ตาราง 2×2 ใหญ่ แกน "จริง" แนวตั้ง / "ทำนาย" แนวนอน ช่องแนวทแยงสีเขียว (ถูก) ช่องนอกสีส้ม/แดง พร้อมป้าย FP ("ดีแต่ตัดสินเสีย — เสียค่าทำซ้ำ") และ FN ("เสียแต่ปล่อยผ่าน — ความเสี่ยงคุณภาพ")

**Image-gen prompt:**
> Educational 2x2 confusion matrix diagram with axes labeled "actual" (vertical) and "predicted" (horizontal); diagonal cells in green labeled "correct", off-diagonal cells in orange and red labeled "false alarm (FP)" and "miss (FN)"; small factory-part icons in the corner cells; Thai-metrology flavor: a caliper icon beside the matrix; flat vector infographic style, white background, clear sans-serif labels.

---

## Figure 4 — Unstructured data becomes numbers (three modalities)

**แนวคิด:** โมเดล ML กินได้แค่ตัวเลข — ภาพ/ข้อความ/เสียงต้องแปลงเป็นอาร์เรย์ก่อนเสมอ

**จุดประสงค์ของภาพ:** จุดพลิกสำคัญของโมดูล — "เห็นข้อมูลไม่มีโครงสร้าง 3 แบบ = ตัวเลข 3 รูปแบบ" ในภาพเดียว

**องค์ประกอบภาพ:** สามแถวแนวนอน: (1) ภาพเสื้อ T ขาวดำ → ลูกศร → กริดตัวเลข 0–255, (2) ประโยคภาษาไทยถูกเส้นแบ่งคำ → ลูกศร → แถวกล่อง ID, (3) คลื่นเสียง → ลูกศร → กราฟ spectrum มี peak สองยอด — ทุกแถวจบที่กล่องเดียวกัน "โมเดล ML"

**Image-gen prompt:**
> Three-row infographic showing data representation: row 1 a grayscale t-shirt photo with arrow to a grid of numbers (pixel values 0-255); row 2 a Thai sentence with word-segmentation marks and arrow to a sequence of numbered token boxes; row 3 an audio waveform with arrow to a frequency spectrum chart with two peaks; all three rows converge on the right into one box labeled "ML model"; flat vector style, white background, teal-coral-slate palette, no photorealism.

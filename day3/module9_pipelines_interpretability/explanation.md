# explanation.md — Module 9: Pipelines & Interpretability (SHAP)

สคริปต์ภาพประกอบสำหรับผู้สอน — แต่ละหัวข้อ = หนึ่งภาพ: แนวคิด (ไทย) → จุดประสงค์ → องค์ประกอบ → image-gen prompt (English)

---

## Figure 1 — Pipeline: one object, every step isolated per fold

**แนวคิด:** `Pipeline` ร้อย impute → select → scale → model เป็นวัตถุเดียว — ตอน cross-validate มัน fit transformer ทุกตัวจาก train ของ fold นั้นเท่านั้น ปิด leakage ทุกช่องทางโดยโครงสร้าง ไม่ต้องพึ่งความระวังของคนเขียนโค้ด

**จุดประสงค์ของภาพ:** ให้เห็นว่า leakage เกิดตรง "ขั้นที่แตะ y แล้ว fit ก่อนแบ่ง" และ pipeline ตัดปัญหานั้นด้วยการย้ายทุกขั้นเข้าไปในกรอบ CV

**องค์ประกอบภาพ:** ซ้าย — แผนภาพ "แบบผิด": กล่อง [คัด feature ด้วย y ทั้งหมด] ก่อนกล่อง [CV folds] มีลูกศรแดงย้อนกลับแสดงข้อมูลอนาคตซึมเข้า; ขวา — "แบบถูก": กล่อง pipeline [impute → select → scale → model] ถูกวนซ้ำในแต่ละ fold โดยเห็นเฉพาะแถบ train; ไอคอนกุญแจ/กำแพงระหว่าง train กับ test; พื้นขาวสไตล์แผนภาพเทคนิค

**Image-gen prompt:**
> Two-part educational diagram comparing leaky and honest machine-learning workflows: left side labeled "leaky" shows a feature-selection box fed by the entire dataset (including future rows) before cross-validation, with a red arrow indicating future information flowing backward into training; right side labeled "honest" shows one pipeline box (impute → select → scale → model) repeated inside each cross-validation fold, touching only the training segment; a thin wall icon separates train from test regions; white background, clean technical diagram style, red and teal accents.

---

## Figure 2 — The leakage penalty on the scorecard

**แนวคิด:** การคัด feature ก่อน CV ทำให้ตัวเลขรายงานฟูมเท็จ — บน SECOM ค่า average precision พุ่งจาก ~0.11 เป็น ~0.19 โดยโมเดลไม่ได้เก่งขึ้นเลย ตัวเลขที่สวยขึ้นคือตัวเลขที่โกง

**จุดประสงค์ของภาพ:** ตรึงตัวเลขเท็จเทียบกับตัวเลขจริงให้เห็นพร้อมกัน — จุดพีคของโมดูลด้าน "วัดผลซื่อสัตย์"

**องค์ประกอบภาพ:** กราฟแท่ง 3 แท่ง: "all 590 features" (~0.075, เทา), "select inside pipeline" (~0.108, teal), "select before CV" (~0.192, แดงพร้อมเครื่องหมายเตือน); เส้นประเฉล้งระหว่างแท่ง teal กับแดงพร้อมป้าย "+78% จากการโกง"; ป้ายใต้แท่งแดง "report this = lie"; พื้นขาว

**Image-gen prompt:**
> Three-bar educational chart of average-precision scores: gray bar "all 590 features" at 0.075, teal bar "selection inside pipeline" at 0.108, and red bar with warning icon "selection before CV" at 0.192; a dashed annotation line between teal and red bars labeled "inflation from leakage"; small caption under the red bar reading "reporting this number is a lie"; white background, scientific chart style.

---

## Figure 3 — SHAP breaks one prediction into contributions

**แนวคิด:** ค่า SHAP ถอด prediction หนึ่งชิ้นออกเป็นส่วน ๆ — base value คือค่าเฉลี่ยของโมเดล แล้วแต่ละ feature ดันผลไปทาง FAIL (แดง) หรือ PASS (น้ำเงิน) จนถึงผลสุดท้าย — เป็น audit trail ที่ผู้ตรวจต้องการ

**จุดประสงค์ของภาพ:** ให้สัญชาตญาณ "แท่งบวกดันหา FAIL, แท่งลบดันหา PASS, รวมกันได้คำตอบ" ก่อนอ่าน waterfall จริง

**องค์ประกอบภาพ:** แผนภาพน้ำตกแบบการ์ตูน: แท่งเริ่มที่ "base value (ค่าเฉลี่ย)" กลางภาพ, แท่งแดง 3–4 แท่งดันขวาไปทางป้าย "FAIL" ขนาดต่างกัน (ใหญ่สุดติดป้าย "ช่องวัด 60"), แท่งน้ำเงิน 2 แท่งดันซ้ายไปทาง "PASS", จบด้วยแท่งสุดท้าย "f(x) = คำตัดสินชิ้นนี้"; ลูกศรบอกทิศการอ่านล่าง→บน

**Image-gen prompt:**
> Educational waterfall diagram explaining a single prediction: starting bar labeled "base value (model average)" in the center, three red bars of varying widths pushing right toward a "FAIL" label (widest bar tagged "sensor channel 60"), two blue bars pushing left toward "PASS", ending bar labeled "f(x) = final verdict for this unit"; reading-direction arrow from bottom to top; white background, clean infographic style, red/blue palette.

---

## Figure 4 — Beeswarm: the global picture of which channels drive FAIL

**แนวคิด:** beeswarm รวม SHAP ของทุกชิ้นไว้ภาพเดียว — แนวตั้งคือ feature, แนวนอนคือแรงดันไปหา FAIL/PASS, สีจุดคือค่าของ feature เอง (แดงสูง น้ำเงินต่ำ) — อ่านได้ทั้ง "ตัวการอันดับหนึ่ง" และ "ทิศทางที่มันทำงาน"

**จุดประสงค์ของภาพ:** สอนอ่านภาพประเภทที่จะติดในรายงาน audit — ให้ผู้เรียนจับคู่ "รูปทรงจุด" กับการตีความได้ทันที

**องค์ประกอบภาพ:** แผนภาพแนวนอนราย feature (5–6 แถว เรียงจากตัวการใหญ่สุดด้านบน), จุดจำนวนมากกระจายรอบเส้นกลางแนวตั้ง (ค่า SHAP = 0), จุดสีแดง/น้ำเงินไล่เฉด, แถบสีคำอธิบาย "feature value: low → high" ด้านขวา, แถวบนสุดมีจุดกระจายไกลไปขวา (แรงดันไป FAIL) มากที่สุด

**Image-gen prompt:**
> Educational beeswarm summary plot: five horizontal feature rows sorted by importance, many small dots scattered around a central zero line of SHAP value, dots colored on a blue-to-red gradient by feature value with a color bar on the right labeled "low → high"; the top row has dots spreading farthest to the right (positive, toward failure); axis label "SHAP value (impact on model output)"; white background, scientific chart style.

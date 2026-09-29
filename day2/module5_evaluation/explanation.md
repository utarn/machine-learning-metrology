# explanation.md — Module 5: Model Evaluation

สคริปต์ภาพประกอบสำหรับผู้สอน — แต่ละหัวข้อ = หนึ่งภาพ: แนวคิด (ไทย) → จุดประสงค์ → องค์ประกอบ → image-gen prompt (English)

---

## Figure 1 — Confusion matrix เป็นตารางตัดสินใจของ gauge

**แนวคิด:** โมเดลคลาสิฟิเคชันในงาน QC คือ gauge ที่ตัดสินใจ "ผ่าน/ตก" — ความผิดพลาดสองช่องไม่เท่าความเสียหายกัน: false accept (ปล่อยของเสียผ่าน) แพงกว่า false reject (ตัดของดีทิ้ง)

**จุดประสงค์ของภาพ:** ประทับให้ผู้เรียนเห็นว่า 2×2 นี้คือ "ใบตรวจรับ" ของ gauge — ก่อนพูดถึง metric ใด ๆ ต้องอ่านช่องผิดพลาดสองช่องให้ได้ก่อน

**องค์ประกอบภาพ:** ตาราง 2×2 ใหญ่ แกน y = actual (PASS/FAIL), แกน x = predicted (PASS/FAIL), ช่องถูก (TN, TP) เติมสีเขียวอมฟ้า มีเครื่องหมายถูก, ช่องผิดสองช่องเติมสีส้มแดงและไฮไลต์เส้นขอบหนา พร้อมป้าย "false accept — ของเสียหลุดถึงลูกค้า" กับ "false reject — ตัดของดีทิ้ง", มีตัวเลขนับจำนวนชิ้นงานในแต่ละช่อง

**Image-gen prompt:**
> Clean educational 2x2 decision matrix diagram for a quality-control gauge: rows labeled "actual PASS" and "actual FAIL", columns labeled "predicted PASS" and "predicted FAIL"; correct cells (TN, TP) filled soft teal with check marks, the two error cells highlighted in orange-red with thick outlines, annotated "false accept — defective part ships" and "false reject — good part scrapped"; sample counts inside each cell, white background, flat scientific diagram style.

---

## Figure 2 — ROC curve และเส้นโอกาส

**แนวคิด:** ROC curve คือคะแนนรวมของโมเดล "ทุกจุดตัดสินใจพร้อมกัน" — โค้งชิดมุมซ้ายบนคือดี, AUC 0.5 (เส้นทแยง) คือการเดาสุ่ม

**จุดประสงค์ของภาพ:** ให้ผู้เรียนจำภาพมาตรฐาน "โค้งดี vs เส้น chance" ก่อนอ่านตัวเลข AUC จริงบน SECOM (0.757)

**องค์ประกอบภาพ:** กราฟสี่เหลี่ยม TPR vs FPR, เส้นโค้ง ROC สีเขียวอมฟ้าโค้งขึ้นชิดมุมซ้ายบน, เส้นทแยงมุมเส้นประสีเข้มติดป้าย "chance (AUC = 0.5)", พื้นที่ใต้โค้งแรเงาบาง ๆ ติดป้าย "AUC", จุด marker กำกับ "default threshold 0.5"

**Image-gen prompt:**
> Scientific ROC curve chart: true positive rate versus false positive rate, a teal curve bowing toward the top-left corner with a lightly shaded area under it labeled "AUC", a dashed dark diagonal line labeled "chance (AUC = 0.5)", a dot marker on the curve labeled "threshold 0.5", axis labels "FPR" and "TPR", white background, minimal educational chart style.

---

## Figure 3 — PR curve บนข้อมูลไม่สมดุล: ไม้บรรทัดที่ซื่อสัตย์กว่า

**แนวคิด:** เมื่อของเสียมีแค่ 6.6% เส้นฐานของ PR curve คืออัตราของเสีย (5.4%) ไม่ใช่ 50% — PR-AUC จึงตัดสินโมเดลเข้มกว่า ROC-AUC ที่ถูก TN มหาศาล "เสริมฟอร์ม"

**จุดประสงค์ของภาพ:** เทียบสองไม้บรรทัดบนข้อมูลชุดเดียวกัน เพื่อให้เห็นว่า "โค้งสวย" ของ ROC อาจหลอก ส่วน PR เปิดโปง precision ที่แท้จริง

**องค์ประกอบภาพ:** สองแผงเทียบกัน: ซ้าย — ROC โค้งสวยและ AUC สูง มีลูกศรกำกับ "TN เยอะช่วยเสริม"; ขวา — PR curve สีส้มแดงลอยต่ำเหนือเส้นฐานเส้นประที่ระดับ 5.4% ติดป้าย "baseline = fail rate", มีป้ายเทียบ "ROC-AUC 0.76 vs PR-AUC 0.16 — same model"

**Image-gen prompt:**
> Two-panel comparison chart: left panel shows an optimistic-looking ROC curve high above its dashed diagonal labeled "TN-heavy data flatters ROC"; right panel shows the precision-recall curve of the same model floating only modestly above a dashed baseline line labeled "baseline = 5.4% fail rate"; annotation comparing "ROC-AUC 0.76" versus "PR-AUC 0.16"; teal and orange-red line colors, white background, scientific chart style.

---

## Figure 4 — k-fold cross-validation และ spread ของ metric

**แนวคิด:** การวัด metric จาก test set เดียวคือการวัดครั้งเดียว — k-fold CV วัดซ้ำ k ครั้ง และ spread ระหว่าง fold คือ repeatability ของการประเมิน

**จุดประสงค์ของภาพ:** เชื่อมสัญชาตญาณการวัดซ้ำหลายครั้งของนักเมโทรโลยี เข้ากับ cross-validation ก่อนสอนการอ่าน mean ± std และการไม่สรุปความต่างของโมเดลที่เล็กกว่า spread

**องค์ประกอบภาพ:** ครึ่งบน — แถบข้อมูลแถวยาวแบ่งเป็น 5 ช่วง สลับเน้นช่อง "test fold" เลื่อนจากซ้ายไปขวา 5 รอบ แต่ละรอบมีป้าย "fit" บนส่วนที่เหลือ; ครึ่งล่าง — dot plot ของค่า metric 5 จุดจาก 5 folds พร้อมเส้น mean ± std ติดป้าย "spread = repeatability of the estimate"

**Image-gen prompt:**
> Educational diagram in two stacked panels: top panel shows a long horizontal data bar divided into five blocks, repeated five times with a different highlighted block each row labeled "test fold" while the rest is labeled "fit"; bottom panel shows a dot plot of five metric values from the five folds with a horizontal mean line and error band labeled "mean ± std = repeatability"; dark slate and teal colors, white background, clean instructional diagram style.

# explanation.md — Module 4: Classification

สคริปต์ภาพประกอบสำหรับผู้สอน — แต่ละหัวข้อ = หนึ่งภาพ: แนวคิด (ไทย) → จุดประสงค์ → องค์ประกอบ → image-gen prompt (English)

---

## Figure 1 — Classification as a decision boundary in measurement space

**แนวคิด:** classification คือการวาดเส้นแบ่งในปริภูมิการวัด — ฝั่งหนึ่งคือ pass อีกฝั่งคือ fail (ต่างจาก regression ที่ตอบเป็นค่าตัวเลขต่อเนื่อง)

**จุดประสงค์ของภาพ:** เชื่อมจาก "เส้นพอดี" ของ Module 3 ไปสู่ "เส้นตัดสิน" ของ Module 4 — จุดข้อมูลคือชิ้นงาน แกนคือค่าที่วัดได้สองช่อง

**องค์ประกอบภาพ:** scatter จุดสองกลุ่มบนแผนภาพสองแกน (แกน x/y = sensor reading 1/2), กลุ่ม teal = PASS กลุ่มส้มแดง = FAIL, เส้นโค้งแบ่งสองกลุ่ม, จุด 2–3 จุดฝั่งผิดข้างถูกไฮไลต์ด้วยวงกลมประพร้อมป้าย "misclassified"

**Image-gen prompt:**
> Clean educational scatter plot in two-dimensional sensor measurement space: teal dots forming one cluster labeled "PASS", orange-red dots forming another labeled "FAIL", a smooth curved decision boundary line separating the two clusters, three individual dots on the wrong side circled with dashed outlines and labeled "misclassified", white background, scientific chart style, axis labels "sensor reading 1" and "sensor reading 2".

---

## Figure 2 — Class imbalance: 104 fails among 1,567 units

**แนวคิด:** ของ fail มีแค่ ~6.6% — โมเดลที่ตอบ "PASS ทุกชิ้น" ก็ได้ accuracy 93.4% โดยไม่จับของเสียเลย

**จุดประสงค์ของภาพ:** ทำให้ความไม่สมดุลของคลาสรู้สึกได้ด้วยตา ก่อนสอนว่า accuracy หลอก

**องค์ประกอบภาพ:** ตารางจุด 1,567 ชิ้นเรียงเป็นกริด (หรือแท่งสองแท่งเทียบสัดส่วน), จุด FAIL 104 จุดสีส้มแดงสังเกตได้ยากท่ามกลางจุด PASS 1,463 จุดสีเทียล, ป้าย "accuracy ของการตอบ PASS ทุกชิ้น = 93.4%", ป้าย "FAIL = 6.6%"

**Image-gen prompt:**
> Educational infographic showing a grid of 1,567 small unit squares almost entirely teal (labeled "PASS 1,463 units") with only 104 scattered squares in orange-red (labeled "FAIL 104 units, 6.6%"), a callout bubble stating "always answering PASS scores 93.4% accuracy and catches zero fails", white background, flat minimal data-visualization style.

---

## Figure 3 — Logistic function: measurement to probability

**แนวคิด:** โมเดล classification ไม่ตอบ pass/fail ตรง ๆ — มันแปลง score จากการวัดเป็น probability ผ่าน logistic function แล้วเราตัดสินทีหลัง

**จุดประสงค์ของภาพ:** ให้เห็นว่า `predict_proba` มาจากไหน และทำไมผลลัพธ์จึงอยู่ในช่วง 0–1 ต่อเนื่อง

**องค์ประกอบภาพ:** กราฟเส้นโค้ง sigmoid รูปตัว S จาก 0 ถึง 1, แกน x = "model score (จากค่าที่วัด)" แกน y = "P(fail)", เส้นประแนวนอนที่ 0.5, จุดตัวอย่างสามจุดบนเส้นโค้งพร้อมป้าย "P(fail) = 0.05 / 0.50 / 0.95"

**Image-gen prompt:**
> Clean scientific line chart of an S-shaped logistic curve mapping a horizontal axis labeled "model score" to a vertical axis labeled "P(fail)" ranging from 0 to 1, dashed horizontal line at 0.5, three marked points on the curve annotated "P = 0.05", "P = 0.50", "P = 0.95", dark slate curve on white background, educational chart style.

---

## Figure 4 — Threshold as a tolerance limit: sliding the cut line

**แนวคิด:** threshold ของการตัดสินคือ tolerance limit — เลื่อนเส้นตัดลงเพื่อจับของเสียมากขึ้น แลกกับการตัดของดีทิ้งมากขึ้น (false accept แลก false reject)

**จุดประสงค์ของภาพ:** ประทับให้เห็นว่าสองความผิดพลาดของ gauge แลกกันโดยตรงผ่านตำแหน่งเส้นตัด — ไม่มีตำแหน่งที่ชนะทั้งสองฝั่ง

**องค์ประกอบภาพ:** แกน x = probability ที่โมเดลประเมิน, การกระจายสองก้อนซ้อนกัน (teal = PASS ก้อนใหญ่, ส้มแดง = FAIL ก้อนเล็ก), เส้นแนวตั้งตัดสินพร้อมป้าย "threshold", พื้นที่แรเงาสองส่วน: "false accept (รับของเสียผ่าน)" ด้านซ้ายเส้นใต้ก้อน FAIL, "false reject (ตัดของดีทิ้ง)" ด้านขวาเส้นใต้ก้อน PASS, ลูกศรแสดง "เลื่อนเส้น ← " พร้อมข้อความ "จับ fail มากขึ้น แต่ตัดของดีทิ้งมากขึ้น"

**Image-gen prompt:**
> Educational probability-density diagram with two overlapping distributions on a horizontal axis labeled "model-estimated P(fail)": a large teal distribution labeled "PASS units" and a small orange-red distribution labeled "FAIL units"; a vertical decision threshold line labeled "threshold"; the area under the FAIL distribution left of the line shaded and labeled "false accept — defective shipped", the area under the PASS distribution right of the line shaded and labeled "false reject — good units scrapped"; an arrow showing the threshold sliding left with the caption "lower threshold: catch more fails, scrap more good units"; white background, scientific chart style.

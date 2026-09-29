# explanation.md — Module 7: Anomaly Detection

สคริปต์ภาพประกอบสำหรับผู้สอน — แต่ละหัวข้อ = หนึ่งภาพ: แนวคิด (ไทย) → จุดประสงค์ → องค์ประกอบ → image-gen prompt (English)

---

## Figure 1 — Rolling robust baseline as a control chart

**แนวคิด:** baseline เคลื่อนที่ด้วย rolling median + MAD ให้ robust z-score — ญาติของ Shewhart chart ที่ limit ปรับตามเวลา จุดที่ |z| ทะลุเพดานคือสัญญาณเตือน

**จุดประสงค์ของภาพ:** เชื่อมสัญชาตญาณ control chart ของนักเมโทรโลยีเข้ากับ detector ตัวแรกก่อนพา ML เข้ามา

**องค์ประกอบภาพ:** แผงบน — ซีรีส์อุณหภูมิยาวพร้อมเส้น rolling median ไหลตามและ limit ±5 robust-z คู่ขนาน (แถบ limit เป็นทางวิ่ง), จุดหนึ่งพุ่งทะลุ limit บนถูกวงกลม; แผงล่าง — ค่า robust z ต่อเวลาพร้อมเส้นประ +5/−5, สไปก์เดียวกันทะลุเส้น, โทน dark slate/teal/orange-red

**Image-gen prompt:**
> Two-panel educational time-series chart styled as a control chart: upper panel shows a long temperature telemetry line with a smooth rolling-median baseline and two parallel dashed control limits forming a moving band, one sharp spike crossing the upper limit circled in orange-red; lower panel shows the corresponding z-score trace with dashed horizontal threshold lines at +5 and -5 and the same spike exceeding them; dark slate data line, teal baseline, orange-red accents, white background, scientific chart style.

---

## Figure 2 — Isolation Forest: fewer cuts means anomalous

**แนวคิด:** Isolation Forest สุ่มตัดอวกาศ feature ซ้ำ ๆ — จุดผิดปกติถูกแยกออกด้วยจำนวนตัดน้อย เพราะอยู่ห่างฝูง จุดปกติต้องถูกตัดหลายครั้งกว่าจะโดดเดี่ยว

**จุดประสงค์ของภาพ:** ให้สัญชาตญาณ "ตัดน้อย = แปลก" ก่อนอ่านโค้ด IsolationForest

**องค์ประกอบภาพ:** กระจายจุด feature สองมิติเป็นฝูงหนาแน่นกลางภาพ จุดเด่นหนึ่งอยู่ห่างออกมุม; เส้นตัดแบบสุ่ม (เส้นแนวตั้ง/นอนสลับกัน) ล้อมฝูงหลายชั้น ขณะที่จุดห่างถูกแยกได้ด้วยเส้นตัดเพียง 2 เส้น; ติดตัวเลข "cuts: 2" ที่จุดห่าง และ "cuts: 9" ที่จุดในฝูง

**Image-gen prompt:**
> Educational scatter plot of a dense elliptical cluster of data points with one isolated outlier far from the cluster; random axis-aligned split lines (alternating vertical and horizontal) partition the plane, requiring many cuts around the dense cluster but only two cuts to isolate the outlier; annotation "2 cuts" near the outlier and "9 cuts" near a central point; dark slate points, teal split lines, orange-red outlier, white background, clean diagram style.

---

## Figure 3 — One-Class SVM learns the boundary of "normal"

**แนวคิด:** One-Class SVM เรียนรู้พรมแดนปิดรอบช่วงข้อมูลที่ "ปกติแน่นอน" (เหมือนการตั้ง gauge reference) แล้วตัดสินจุดใหม่ด้วยตำแหน่งเทียบพรมแดน — จุดที่เคยเป็นสถานะผิดปกติไม่ได้รับอนุญาตในการเรียน

**จุดประสงค์ของภาพ:** อธิบายว่าทำไมต้อง fit เฉพาะ "ช่วงปกติที่ไว้ใจได้" และพรมแดน RBF รัดข้อมูลอย่างไร

**องค์ประกอบภาพ:** ฝูงจุด train (ปกติ) สองสามหย่อมในสเกลเดียว, เส้นขอบ RBF โค้งลู่รัดฝูงอย่างแน่นพอดี, จุดนอกขอบ 3–4 จุดถูกทำเครื่องหมายเป็น outlier นอกเขต, ระบายพื้นที่ในขอบด้วยสีอ่อน "normal region", ป้าย "trained on normal operation only"

**Image-gen prompt:**
> Educational diagram of one-class classification: several loose clusters of dark slate training points with a smooth teal RBF decision boundary curving tightly around them, enclosed region shaded very light teal labeled "normal region"; four orange-red points lying outside the boundary labeled as outliers; caption "trained on normal operation only"; white background, clean scientific illustration style.

---

## Figure 4 — Scorecard on the real timeline

**แนวคิด:** วัด detector ด้วยสองตัวเลขพร้อมกัน — labeled windows ที่จับได้ (caught) และ false alarms นอกหน้าต่าง — บนไทม์ไลน์เดียวกันของซีรีส์จริงเพื่อเปรียบเทียบ detector ต่อ detector

**จุดประสงค์ของภาพ:** สรุปผลทั้งโมดูลเป็นภาพเดียว — สีบอกสถานะ ตำแหน่งบนไทม์ไลน์บอกเหตุการณ์ ทำให้เห็นว่า detector แต่ละตัวพลาดต่างกันตรงไหน

**องค์ประกอบภาพ:** ไทม์ไลน์แนวนอนยาวสามแถว (หนึ่งแถวต่อ detector: rolling z, Isolation Forest, One-Class SVM), ช่วง labeled windows ระบายแถบแดงอ่อนครอบทุกแถว, สัญลักษณ์บนไทม์ไลน์: จุดเขียวในแถบ = caught, กากบาทแดงในแถบ = missed window, จุดส้มนอกแถบ = false alarm, คำอธิบายสีมุมภาพ; หน้าต่างที่ 3 ของแถว rolling z และ IF มีกากบาทแดง (พลาด) ขณะแถว OCSVM มีจุดเขียว

**Image-gen prompt:**
> Three-row horizontal timeline comparison chart: each row labeled "rolling z-score", "Isolation Forest", "One-Class SVM"; four shaded light-red event windows span all rows at the same positions; within windows, green dots mark caught anomalies and red crosses mark missed ones (two crosses in row one and row two at the third window, green dots in row three); orange dots scattered outside windows marking false alarms, sparsest in the middle row; color legend top right; white background, clean infographic style.

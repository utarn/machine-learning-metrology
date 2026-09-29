# explanation.md — Module 1: ML Workflow & EDA

สคริปต์ภาพประกอบสำหรับผู้สอน — แต่ละหัวข้อ = หนึ่งภาพ: แนวคิด (ไทย) → จุดประสงค์ → องค์ประกอบ → image-gen prompt (English)

---

## Figure 1 — The ML workflow loop

**แนวคิด:** งาน ML ไม่ใช่เส้นตรงไปหาโมเดล แต่เป็นวงจรที่เริ่มจากคำถามและวนกลับมาที่ข้อมูลเสมอ

**จุดประสงค์ของภาพ:** ปลูกลำดับความคิดที่ถูก — คำถาม/ข้อมูลมาก่อนโมเดลเสมอ

**องค์ประกอบภาพ:** วงกลมลูกศร 7 ขั้น: Ask a question → Get data → EDA → Features → Train → Evaluate → (ลูกกลับไปที่ EDA/Features/Train), พร้อมไอคอนเครื่องมือวัดแทรกในขั้น Get data, จุดเริ่มต้นไฮไลต์

**Image-gen prompt:**
> Clean circular flow diagram of a machine learning project workflow with seven labeled stages: "1. Ask a question", "2. Get data", "3. EDA", "4. Feature engineering", "5. Train model", "6. Evaluate", with an arrow looping back from evaluate to EDA/features/train; a magnifier and measurement-sensor icon on the "Get data" stage; flat vector style, white background, teal-blue-orange palette, numbered circles.

---

## Figure 2 — Missing values map

**แนวคิด:** ข้อมูลจริงมีรู — ต้องเห็นรูทั้งหมดก่อนเลือกวิธีจัดการ

**จุดประสงค์ของภาพ:** ให้ผู้เรียนจำภาพ "แผนที่ค่าหาย" ของ Air Quality: NMHC หายหนัก 90%, GT columns ~18%, เซนเซอร์ PT08 แทบไม่หาย

**องค์ประกอบภาพ:** ตารางคล้าย heat-strip: แถว = คอลัมน์ข้อมูล (Date, CO(GT), PT08.S1, ..., T, RH, AH), ความยาวแถบแดง = % missing, หมายเลข 90% / 18% / <1% กำกับ

**Image-gen prompt:**
> Minimal data-quality bar chart: horizontal bars for each column of a sensor dataset (Date, CO reference, five sensor channels, temperature T, humidity RH, absolute humidity AH), bar length = percent of missing values, one very long red bar (~90%) labeled "NMHC(GT)", three medium bars (~18%), all others tiny; dark slate background or white, flat vector style, annotation of percentages.

---

## Figure 3 — Correlation heatmap

**แนวคิด:** ความสัมพันธ์ระหว่างช่องสัญญาณเซนเซอร์ ค่าอ้างอิง และสิ่งแวดล้อม — รวมทั้ง cross-sensitivity ต่อ T/RH

**จุดประสงค์ของภาพ:** ให้เห็นว่า heatmap เดียวมองเห็น "ใครเกี่ยวกับใคร" ทั้งกระดาน พร้อมจุดที่ PT08.S3 ติดลบ

**องค์ประกอบภาพ:** heatmap 8×8: แถว/คอลัมน์ = PT08.S1–S5, CO(GT), T, RH; สีแดง = บวก น้ำเงิน = ลบ; ช่อง (S1,CO), (S2,CO), (S5,CO) เข้มแดง, ช่อง (S3,CO) น้ำเงิน, แถว T/RH กับเซนเซอร์สีจางกลาง, มี scale bar −1…+1

**Image-gen prompt:**
> Annotated 8x8 correlation heatmap, rows and columns labeled with sensor channel names (PT08.S1 through PT08.S5, CO ref, T, RH), diverging red-to-blue color scale from -1 to +1, strong red diagonal, a few dark red off-diagonal cells, one clearly blue cell between a sensor channel and CO reference, small white numbers inside cells, clean scientific figure style, white background.

---

## Figure 4 — Random split vs time-based split

**แนวคิด:** ข้อมูลเซนเซอร์เรียงตามเวลา การสุ่มแบ่ง train/test ทำให้โมเดลเห็นอนาคตรั่วมา

**จุดประสงค์ของภาพ:** ประทับใจ "แบ่งตามเวลาเมื่อข้อมูลมีเวลา"

**องค์ประกอบภาพ:** เทียบสองแถบเส้นเวลา: บน — แถบข้อมูลยาว มีจุดสีเหลือง (train) และแดง (test) กระจายปนกัน → ลูกศรข้ามเวลาจาก test กลับมา train (ติดป้าย leakage!), ล่าง — แถบตัดตรง 80% เรียงเวลา สีเหลืองก่อนแดง ติดป้าย "honest"

**Image-gen prompt:**
> Two horizontal timelines compared: top bar shows training points (yellow) and test points (red) randomly interleaved along a time axis with a warning arrow crossing time, labeled "random split — leakage risk"; bottom bar shows yellow block covering the first 80% of the timeline and red block for the last 20%, labeled "time-based split — honest"; flat vector style, white background, clear labels.

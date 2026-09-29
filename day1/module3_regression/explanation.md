# explanation.md — Module 3: Regression

สคริปต์ภาพประกอบสำหรับผู้สอน — แต่ละหัวข้อ = หนึ่งภาพ: แนวคิด (ไทย) → จุดประสงค์ → องค์ประกอบ → image-gen prompt (English)

---

## Figure 1 — Least squares as a calibration

**แนวคิด:** การพอดีเส้นตรงด้วย least squares คือหัวใจของการสอบเทียบ — หาเส้นที่ residual รวมเล็กสุด

**จุดประสงค์ของภาพ:** เชื่อมสัญชาตญาณเดิมของนักเมโทรโลยี (เส้นสอบเทียบ) กับสิ่งที่ LinearRegression ทำ

**องค์ประกอบภาพ:** scatter จุดสอบเทียบ 10 จุดรอบเส้นตรง, เส้นเฉลี่ยแนวดิ่งจากจุดสูงสุด 2–3 จุดถึงเส้น (แสดง residual), ป้าย "minimize Σ residual²", แกน x = applied load, y = reading

**Image-gen prompt:**
> Clean educational scatter plot of ten calibration data points around a straight fitted line, three vertical dashed segments from points down to the line showing residuals, equation label "minimize Σ residual²", axes labeled "applied load" and "instrument reading", white background, dark slate points, teal fitted line, scientific chart style.

---

## Figure 2 — Residuals reveal the missing term

**แนวคิด:** residual plot บอกสิ่งที่โมเดลจับไม่ได้ — รูปทรง U แปลว่าขาดเทอม x²

**จุดประสงค์ของภาพ:** สอนว่า "อย่าเชื่อ R² เดียว ให้ดู residual"

**องค์ประกอบภาพ:** สองแผง: ซ้าย — residual ของ linear fit เรียงตาม x เป็นรูปตัว U ชัด; ขวา — residual ของ quadratic fit กระจายแบนราบรอบศูนย์, เส้นศูนย์สีแดงทั้งสองแผง

**Image-gen prompt:**
> Two-panel residual plot comparison: left panel titled "linear fit" shows residuals forming a clear U-shaped parabola pattern across the x-axis; right panel titled "quadratic fit" shows residuals scattered flat and structureless around zero; red horizontal zero line in both panels, dark scatter dots, white background, scientific chart style.

---

## Figure 3 — Extrapolation warning

**แนวคิด:** โมเดล/สมการสอบเทียบใช้ได้เฉพาะช่วงที่สอบเทียบ — นอกช่วงคือการเดา

**จุดประสงค์ของภาพ:** ประทับความรู้สึก "เส้นที่มั่นใจยังไงก็โกหกนอกช่วง" — เชื่อมกับ calibration range ที่ผู้เรียนคุ้นอยู่แล้ว

**องค์ประกอบภาพ:** scatter ข้อมูลเต็มช่วง, เส้นพอดีจากช่วงล่างเท่านั้นยืดต่อไปทางขวาแล้วไหลหลุดจากข้อมูล, แถบเทาแนวตั้งติดป้าย "beyond calibration range — do not trust", ไอคอนเครื่องหมายตกใจที่ปลายเส้น

**Image-gen prompt:**
> Scientific scatter plot of calibration data across a wide x-range; a fitted curve computed only from the left half of the data continues rightward and visibly diverges from the data cloud; vertical shaded region on the right labeled "beyond calibration range — do not trust"; dashed vertical boundary line; white background, teal fitted curve, dark data points, warning-style annotation.

---

## Figure 4 — Ridge/Lasso shrinkage

**แนวคิด:** regularization หดสัมประสิทธิ์กันผันผวนเมื่อ feature สัมพันธ์กัน; ridge หดทุกตัว, lasso กดบางตัวเป็นศูนย์

**จุดประสงค์ของภาพ:** ให้เห็นความต่าง L1/L2 ในหนึ่งภาพก่อนดูตัวเลขจริง

**องค์ประกอบภาพ:** กราฟเส้นสัมประสิทธิ์ต่อ feature สามชุด: OLS (แท่งสูงแกว่ง), ridge (แท่งเตี้ยลงแต่ไม่เป็นศูนย์), lasso (บางแท่งเป็นศูนย์จริง), แกน x = ชื่อ feature, ตำนานสามสี

**Image-gen prompt:**
> Grouped horizontal bar chart comparing regression coefficients of four sensor features under three models: OLS (large uneven bars, dark slate), Ridge (all bars shrunk but nonzero, teal), Lasso (some bars reduced exactly to zero, orange); legend with the three model names; clean white background, minimal axis labels, educational chart style.

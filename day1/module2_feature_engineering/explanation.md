# explanation.md — Module 2: Feature Engineering

สคริปต์ภาพประกอบสำหรับผู้สอน — แต่ละหัวข้อ = หนึ่งภาพ: แนวคิด (ไทย) → จุดประสงค์ → องค์ประกอบ → image-gen prompt (English)

---

## Figure 1 — The preparation pipeline as plumbing

**แนวคิด:** ข้อมูลดิบไหลผ่านท่อประมวลผลเป็นขั้น ๆ — fit จาก train เท่านั้น, transform ทั้ง train/test

**จุดประสงค์ของภาพ:** ให้ผู้เรียนจำโครง Pipeline/ColumnTransformer เป็นภาพท่อประปา และเห็นจุด leakage (fit จากทั้งชุด)

**องค์ประกอบภาพ:** ท่อประปา 3 ข้อ: Impute → Scale → (Poly) → Model, ลูกศรข้อมูล train (เขียว) และ test (ส้ม) ไหลเข้าท่อเดียวกัน แต่มีป้าย "fit once — on train only" ที่ท่อแต่ละข้อ, มีกากบาทแดงบนเส้นทางสำรองที่ดึงสถิติจาก test

**Image-gen prompt:**
> Flat vector diagram of a data preprocessing pipeline drawn as connected pipes: stages labeled "impute", "scale", "polynomial features", "model"; green flow labeled "train data" and orange flow labeled "test data" both passing through the pipes; each pipe has a tag "fit once — on train only"; a red X marks a bypass pipe labeled "fitting on all data = leakage"; white background, teal and orange palette, minimal text.

---

## Figure 2 — Why scaling matters

**แนวคิด:** feature ที่สเกลใหญ่บังคอลัมน์สเกลเล็กในโมเดลที่วัดระยะ/regularize

**จุดประสงค์ของภาพ:** เห็นก่อน/หลัง standardization ของ AT/V/AP/RH

**องค์ประกอบภาพ:** boxplot คู่ ซ้าย: AT (2–37), V (25–82), AP (~1000), RH (25–100) บนสเกลเดียวทำให้ AT ดูแบนราบ; ขวา: ทุก box อยู่ราว 0 กึ่งกลางเท่ากันหลัง scale, มีป้าย "mean 0, std 1"

**Image-gen prompt:**
> Side-by-side boxplots of four features: left panel titled "before scaling" shows boxes at very different vertical positions (one near 1000, others below 100) on a shared axis; right panel titled "after standardization" shows all four boxes centered at zero with equal spread; clean scientific chart style, white background, teal boxes, axis labels minimal.

---

## Figure 3 — Polynomial features bending the fit

**แนวคิด:** เพิ่มเทอม x² ทำให้เส้นตรงโค้งตามข้อมูลได้

**จุดประสงค์ของภาพ:** ภาพจำของ "โมเดลเดิม + feature ใหม่ = ความสามารถใหม่" ก่อนไปถึง regression module

**องค์ประกอบภาพ:** scatter ข้อมูลโค้งรูปพาราโบลาจาง ๆ, เส้นเทา = linear fit พลาดทั้งสองหาง, เส้นน้ำเงิน = quadratic fit เข้ากับข้อมูล, ป้ายกำกับ "y = b0 + b1x + b2x²"

**Image-gen prompt:**
> Simple scientific scatter plot with parabola-shaped point cloud (light dots), two fitted curves overlaid: a straight gray line missing both ends of the cloud, and a smooth blue quadratic curve following the data; small equation label "y = b0 + b1x + b2x²"; white background, minimal axes, clean educational chart.

---

## Figure 4 — Categorical encoding: one-hot

**แนวคิด:** ข้อมูลหมวดหมู่ต้องกลายเป็นคอลัมน์ 0/1 ก่อนเข้าโมเดล

**จุดประสงค์ของภาพ:** จำรูปแบบ one-hot และเหตุผลที่ไม่ encode เป็น 1,2,3 (ปลอมลำดับ)

**องค์ประกอบภาพ:** ตารางซ้าย: คอลัมน์ sensor_id (S1,S2,S3,...) → ลูกศร → ตารางขวา: คอลัมน์ sensor_S1, sensor_S2, sensor_S3 เป็น 0/1, พร้อมส่วนที่ถูกขีดฆ่า: "S1=1, S2=2, S3=3 ✗ (ปลอมลำดับ)"

**Image-gen prompt:**
> Educational table-transformation diagram: left table with a single column "sensor_id" containing values S1, S2, S3, S1, S2; arrow pointing right to a wide table with three columns "sensor_S1", "sensor_S2", "sensor_S3" filled with 0s and 1s in one-hot pattern; a crossed-out note below shows "S1=1, S2=2, S3=3" marked wrong; flat vector style, white background, green header row.

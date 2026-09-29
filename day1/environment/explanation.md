# explanation.md — Module 0: Environment & Course Setup

ไฟล์นี้เป็นสคริปต์สำหรับสร้างภาพประกอบ (ผู้สอนใช้; นักเรียนไม่ต้องอ่าน)
แต่ละหัวข้อ = หนึ่งภาพ: แนวคิด (ไทย) → จุดประสงค์ของภาพ → องค์ประกอบภาพ → prompt สำหรับ image generation (English, ready-to-use)

---

## Figure 1 — Course roadmap

**แนวคิด:** หลักสูตร 3 วัน 10 โมดูล ไหลจากพื้นฐาน → โมเดล → การประเมิน → การนำไปใช้จริงในงานเมโทรโลยี

**จุดประสงค์ของภาพ:** ให้ผู้เรียนเห็นทั้งเส้นทางก่อนลงลึก และรู้ว่าวันนี้ (Day 1) อยู่ตรงไหน

**องค์ประกอบภาพ:** เส้นทาง 3 ขั้น (Day 1/2/3) เรียงซ้ายไปขวา, แต่ละวันมีกล่องย่อย 4 โมดูล, Day 1: Environment → Workflow & EDA → Feature Engineering → Regression, Day 2: Classification → Evaluation → Clustering → Anomaly Detection, Day 3: Time Series → Pipelines & Interpretability → Capstone, ไอคอนเครื่องมือวัด/ห้องแล็บประกอบทุกกล่อง

**Image-gen prompt:**
> Clean educational infographic, horizontal roadmap of a 3-day machine learning course, three colored segments labeled "Day 1", "Day 2", "Day 3", each containing four labeled module boxes (Day 1: Environment, Workflow & EDA, Feature Engineering, Regression; Day 2: Classification, Evaluation, Clustering, Anomaly Detection; Day 3: Time Series, Pipelines & Interpretability, Capstone), metrology/laboratory icons (calibration weights, sensors, gauges) decorating the path, flat vector style, white background, blue-teal palette, no photorealism.

---

## Figure 2 — Why a pinned environment

**แนวคิด:** ผลลัพธ์งานวัดต้องทำซ้ำได้; environment ซอฟต์แวร์ก็ต้อง reproducible เหมือนกัน

**จุดประสงค์ของภาพ:** ชี้ว่า "โค้ดเดียวกัน + เวอร์ชันต่างกัน = ผลลัพธ์ต่างกัน" และ uv.lock คือกลไกล็อก

**องค์ประกอบภาพ:** เทียบสองฝั่ง — ซ้าย: เครื่องสามเครื่องที่แต่ละเครื่องมีป้ายเวอร์ชันไลบรารีต่างกัน ผลลัพธ์ (กราฟ) ต่างกันเล็กน้อย, ขวา: เครื่องสามเครื่องดึงจากไฟล์ล็อกกลาง (ไอคอนล็อก) ทุกเครื่องได้เวอร์ชันเดียวกัน ผลลัพธ์เหมือนกันเป๊ะ

**Image-gen prompt:**
> Educational diagram comparing unreproducible vs reproducible software environments: left side shows three laptops with different library version tags producing slightly different charts; right side shows the same three laptops all pulling from one central locked version file with a padlock icon, producing identical charts; flat vector illustration, white background, red accent for the chaotic left side, green accent for the reproducible right side, minimal text.

---

## Figure 3 — The five setup steps

**แนวคิด:** setup.ps1 ทำ 5 ขั้นอัตโนมัติ ผู้เรียนควรรู้ว่ากำลังเกิดอะไร

**จุดประสงค์ของภาพ:** ลดความกลัว "กล่องดำ" — เห็นว่าสคริปต์แค่เรียงเครื่องมือมาตรฐาน

**องค์ประกอบภาพ:** ผังลูกศร 5 ขั้น: (1) install uv → (2) install CPython 3.14 → (3) uv sync --frozen (แพ็กเกจจาก uv.lock) → (4) register Jupyter kernel "ml-metrology" → (5) smoke test PASS badge, มีทางแยกย่อยที่ขั้น 3 ว่า offline cache

**Image-gen prompt:**
> Horizontal five-step flowchart of an automated environment setup: 1. Install uv package manager, 2. Install CPython 3.14, 3. Sync pinned packages from lock file (with a small offline-cache branch), 4. Register Jupyter kernel named "ml-metrology", 5. Run smoke test ending with a green PASS badge; numbered circles, arrows left to right, flat vector style, white background, teal-blue palette.

---

## Figure 4 — Notebook anatomy

**แนวคิด:** notebook มีสองชนิดเซลล์ และมีไฟล์สามบทบาทในแต่ละ topic

**จุดประสงค์ของภาพ:** ให้ผู้เรียนแยกบทบาท book / exercise / solution และรู้ว่าเซลล์ไหนโค้ด เซลล์ไหนเรียงความ

**องค์ประกอบภาพ:** ซ้าย: notebook หนึ่งไฟล์ มีเซลล์สลับ markdown (ไอคอนเอกสาร) กับ code (ไอคอน >_), ขวา: สามไฟล์ book.ipynb / exercise.ipynb / solution.ipynb พร้อมป้ายบทบาท "อ่านกับผู้สอน / ทำเอง / เช็กเฉลย"

**Image-gen prompt:**
> Simple educational diagram of a Jupyter notebook: one notebook window showing alternating markdown cells (document icon) and code cells (play icon) with run outputs; beside it three labeled file cards "book.ipynb — guided lesson", "exercise.ipynb — you fill in TODO", "solution.ipynb — check your answers"; flat vector style, friendly colors, white background, minimal text.

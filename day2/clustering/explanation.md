# explanation.md — Module 6: Clustering

สคริปต์ภาพประกอบสำหรับผู้สอน — แต่ละหัวข้อ = หนึ่งภาพ: แนวคิด (ไทย) → จุดประสงค์ → องค์ประกอบ → image-gen prompt (English)

---

## Figure 1 — K-Means carves measurement-space into regimes

**แนวคิด:** K-Means แบ่งพื้นที่การวัด (measurement space) ออกเป็นดินแดน (territory) ของแต่ละ regime โดยมี centroid เป็น "เมืองหลวง" ของดินแดน — จุดข้อมูลแต่ละจุด (หนึ่งชั่วโมงของการวัด) ถูกกำหนดสังกัด centroid ที่ใกล้ที่สุด

**จุดประสงค์ของภาพ:** ทำให้เห็นว่า "cluster" ในสายตาของ K-Means คือการแบ่งเขตอวกาศ 7 มิติด้วยระยะทาง — และ centroid คือค่าเฉลี่ยที่ตีความได้ (แปลงกลับหน่วยจริงเพื่อตั้งชื่อ regime)

**องค์ประกอบภาพ:** พื้นที่ 2 มิติ (แทนพื้นที่ feature) แบ่งด้วยเส้นเขตแดนเป็น 4 โซนสีต่างกัน, จุดข้อมูลกระจายในแต่ละโซน, ดาว/สัญลักษณ์ใหญ่กลางแต่ละโซนติดป้าย "centroid", ป้ายกำกับโซนตามชื่อ regime (เช่น "hot & dry midday", "cool night"), แกน x = sensor response mode, แกน y = T / RH axis

**Image-gen prompt:**
> Educational diagram of a 2D measurement space partitioned into four colored regions (Voronoi-style boundaries) by K-Means clustering; scattered data dots inside each region, a large star marker at each region center labeled "centroid", region labels "hot & dry midday", "cool night", "rush hour, cool", axes labeled "sensor response mode (PC1)" and "temperature-humidity axis (PC2)", white background, dark slate / teal / sand / orange-red color scheme, clean scientific chart style.

---

## Figure 2 — Elbow and silhouette choose k together

**แนวคิด:** เลือกจำนวน cluster ด้วยสองเกณฑ์ประกอบกัน — inertia (ความแน่นในก้อน) ลดลงเสมอเมื่อ k เพิ่ม จึงต้องอ่าน "จุดศอก" ส่วน silhouette (ความแยกเชิงคุณภาพ) มีค่าสูงสุดจริง ๆ ให้อ่าน สองเส้นนี้บางทีก็เห็นพระพักตร์ไม่ตรงกัน และคำตอบสุดท้ายต้องผ่านการตีความว่าแต่ละ k ตั้งชื่อ regime ได้หรือไม่

**จุดประสงค์ของภาพ:** กันการเรียน "มองกราฟเดียวแล้วสรุป" — ให้เห็นตั้งแต่แรกว่า elbow กับ silhouette ให้คำแนะนำไม่เหมือนกัน และการเลือก k เป็นการตัดสินใจที่มี trade-off

**องค์ประกอบภาพ:** แผงคู่ ซ้าย-ขวา ซ้าย: เส้น inertia ต่อ k = 2..8 โค้งชันแล้วแบน มีวงกลมไฮไลต์ที่จุดศอก k ≈ 4 พร้อมป้าย "elbow"; ขวา: เส้น mean silhouette ต่อ k มียอดสูงสุดที่ k=2 พร้อมป้าย "highest ≠ best for the task"; แกน x ตรงกันคือ k

**Image-gen prompt:**
> Two-panel line chart side by side sharing the x-axis "number of clusters k (2 to 8)": left panel "inertia" shows a steeply descending curve that flattens after k=4 with a highlighted circle and label "elbow"; right panel "mean silhouette" shows a curve peaking at k=2 with a highlighted circle and label "highest ≠ best for the task"; dark slate and teal lines, red accent highlight, white background, minimal scientific chart style.

---

## Figure 3 — DBSCAN: core, border, and noise

**แนวคิด:** DBSCAN ไม่แบ่งดินแดน แต่เดินตามความหนาแน่น — จุดที่มีเพื่อนบ้านครบ min_samples ภายในรัศมี eps คือ core จุดขอบที่ติดกับ core คือ border และจุดที่ไม่มีกลุ่มพอรับคือ noise — ในงานเมโทรโลยี noise คือรายชื่อ "ชั่วโมงที่สภาพแวดล้อมไม่อยู่ใน regime ไหนเลย"

**จุดประสงค์ของภาพ:** แยกความคิดคนละขั้วกับ Figure 1: K-Means บังคับทุกจุดให้มีเผ่า, DBSCAN อนุญาตให้บางจุดไม่มีเผ่า — และกลุ่มทรงใดก็ได้ (ไม่ต้องเป็นทรงกลม)

**องค์ประกอบภาพ:** scatter ข้อมูลเป็นก้อนหนาแน่นรูปทรงโค้งยาวหนึ่งก้อน + ก้อนเล็กแยกอีกก้อน, จุดบางส่วนมีวงกลม eps ล้อม (core, สีเข้ม), จุดขอบสีอ่อน, จุดโดดเดี่ยว 3–4 จุดนอกก้อนติดป้าย "noise / out of every regime", เส้นวงกลมรัศมี eps ตัวอย่างหนึ่งวงพร้อมป้าย "eps", ป้าย "min_samples" กำกับจำนวนเพื่อนที่ต้องมี

**Image-gen prompt:**
> Scientific scatter diagram illustrating DBSCAN: one elongated dense blob plus one small separate blob of dark slate points; a few sample points circled with a dashed teal circle labeled "eps", core points drawn darker with faint neighborhood circles, lighter border points at blob edges, three isolated orange-red points far from any blob labeled "noise — out of every regime", annotation "core point: ≥ min_samples neighbors within eps", white background, clean educational chart style.

---

## Figure 4 — PCA projection with clusters and T/RH arrows

**แนวคิด:** PCA ยุบข้อมูล 7 มิติ (5 ช่องเซนเซอร์ + T + RH) ลงบนระนาบ 2 มิติที่อธิบายความแปรปรวนมากที่สุด — จุดข้อมูลถูกระบายสีตาม cluster ของ K-Means และลูกศร loading บอกว่า feature ตัวจริงชี้ไปทางไหนในภาพนี้ (โหมดเซนเซอร์ร่วมบนแกน PC1, แกน T–RH บน PC2)

**จุดประสงค์ของภาพ:** เชื่อมสามชิ้นของโมดูลเข้าด้วยกันในภาพเดียว — scaling, K-Means, PCA — และให้เห็นว่า direction ของ T กับ RH (สวนกัน) และทิศของ S3 (สวนกับเซนเซอร์ช่องอื่น) คือเหตุผลที่ regime แยกตาม T/RH ได้

**องค์ประกอบภาพ:** scatter จุดจาง ๆ 4 สีตาม cluster บนระนาบ PC1–PC2, ลูกศรเรืองจากจุดกำเนิด 7 เส้นแทน feature: กลุ่ม PT08.S1/S2/S4/S5 ชี้ทางเดียวกัน, S3 ชี้ตรงข้าม, T ชี้ขึ้น–RH ชี้ลง (เกือบตรงข้ามกัน) พร้อมป้ายชื่อท้ายลูกศร, คำกำกับ "PC1 59% + PC2 25% ≈ 83% of variance"

**Image-gen prompt:**
> PCA biplot-style educational chart: faintly colored data clouds in four cluster colors on a PC1-PC2 plane; seven loading arrows radiating from the origin — four sensor arrows (PT08.S1, S2, S4, S5) pointing together to the right labeled "shared sensor response mode", one arrow (PT08.S3) pointing opposite left, and two arrows "T" pointing up and "RH" pointing down nearly opposed; axis labels "PC1 (59%)" and "PC2 (25%)", white background, dark slate/teal/orange-red arrows, clean scientific chart style.

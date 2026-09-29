# explanation.md — Module 8: Time-Series Forecasting of Reference Drift

สคริปต์ภาพประกอบสำหรับผู้สอน — แต่ละหัวข้อ = หนึ่งภาพ: แนวคิด (ไทย) → จุดประสงค์ → องค์ประกอบ → image-gen prompt (English)

---

## Figure 1 — Anatomy of a drifting series: trend, seasonality, noise

**แนวคิด:** อนุกรมเวลาที่ตาเห็นคือการซ้อนกันของสามองค์ประกอบ — drift ช้า ๆ (สิ่งที่ห้องสอบเทียบสนใจ), ฤดูกาลวนซ้ำคาบคงที่ (ผลแวดล้อม) และ noise (สิ่งที่อธิบายไม่ได้) — การถอดแยกส่วนทำให้เห็นว่าแต่ละชั้นมีขนาดเท่าไร

**จุดประสงค์ของภาพ:** ให้ผู้เรียนเห็นว่า "เส้นเดียวที่แกว่ง ๆ" จริง ๆ คือสามชั้นซ้อนกัน ก่อนไปเขียนโค้ดถอดองค์ประกอบ

**องค์ประกอบภาพ:** แผงบน — เส้นซีรีส์ดิบไต่ช้าพร้อมคลื่นเล็กซ้อนบน; แผงสอง — เส้น trend เรียบไต่เป็นเกียร์; แผงสาม — คลื่นฤดูกาลสม่ำเสมอวนรอบศูนย์; แผงล่าง — residual เตี้ย ๆ ไม่มีรูปทรง; มีวงเล็บ/ลูกศรชี้ว่า "รวมกัน = แผงบน"; โทน dark slate / teal / amber / orange-red บนพื้นขาว

**Image-gen prompt:**
> Four-panel educational time-series diagram: top panel shows a raw noisy rising line combining slow drift with a small repeating wave; second panel shows the smooth rising trend component alone; third panel shows a regular sinusoidal seasonal wave around zero with fixed period; bottom panel shows tiny shapeless residual noise around zero; a bracket on the right indicates the three lower panels sum to the top one; dark slate, teal, amber and orange-red palette, white background, clean scientific chart style.

---

## Figure 2 — Forward-chaining cross-validation (TimeSeriesSplit)

**แนวคิด:** กับข้อมูลอนุกรมเวลา ห้ามสลับแถวก่อนแบ่ง fold — โมเดลที่เรียนจากอนาคตไปอดีตจะได้คะแนนสวม ทางถูกคือ train อยู่ข้างหน้าเสมอและ test ต่อท้าย แล้วเลื่อนหน้าต่างไปเรื่อย ๆ

**จุดประสงค์ของภาพ:** ฝังภาพจำ "แถบ teal คืออดีต แถบ orange คืออนาคต" ให้ติดตาก่อนผู้เรียนเจอ `TimeSeriesSplit` ในโค้ด

**องค์ประกอบภาพ:** แถบแนวนอน 5 แถว (fold 1–5) บนไทม์ไลน์เดียวกัน แต่ละแถวมีแถบ teal ยาวเริ่มจากซ้าย (โตขึ้นทุก fold) ต่อด้วยช่องว่างเล็กแล้วแถบ orange สั้นต่อท้ายชิดขอบขวา; แกนล่างลูกศรเวลา; หมายเหตุ "train ต้องมาก่อน test เสมอ"

**Image-gen prompt:**
> Educational diagram of forward-chaining cross-validation: five horizontal rows labeled fold 1 to fold 5 on a shared time axis; each row has a teal training segment starting from the left (growing longer each fold) followed by a small gap and a short orange test segment attached to the right edge; arrow labeled "time" along the bottom axis; caption "train always precedes test"; white background, flat infographic style, teal and orange palette.

---

## Figure 3 — Trees interpolate, they do not extrapolate

**แนวคิด:** โมเดลต้นไม้ (XGBoost) ทำนายโดยเลือกจากค่าที่เคยเห็นใน training — กับซีรีส์ที่ไต่ขึ้นตลอด fold test อยู่สูงกว่าทุกค่าที่ train เคยรู้จัก ต้นไม้จึงตอบด้วยค่าสูงสุดเดิมซ้ำ ๆ ส่วน linear model ต่อเส้นออกนอกขอบได้

**จุดประสงค์ของภาพ:** บทเรียนที่สำคัญที่สุดของโมดูล — ทำไม XGBoost แพ้ยับบนสัญญาณ drift ทั้งที่เก่งทุกโมดูลก่อน และทำไมต้องทำนาย "difference" แทน "level"

**องค์ประกอบภาพ:** กราฟจุดซีรีส์ไต่ขึ้นเป็นแถบเฉียง เส้นแบ่ง train (ซ้าย) กับ test (ขวา); บนช่วง test เส้น teal (linear) วิ่งต่อแนวเดิมขึ้นไป ขณะที่เส้น orange (tree) แบนราบค้างที่ระดับสูงสุดของ train; ป้ายกำกับ "linear: ต่อแนวได้" / "tree: ค้างที่ขอบ"; พื้นขาวสไตล์กราฟวิทยาศาสตร์

**Image-gen prompt:**
> Educational chart showing extrapolation failure: a rising scatter series of data points, a vertical divider separating training region (left) from future test region (right); a teal line continues the rising trend through the test region, while an orange line goes flat horizontally at the maximum training level, unable to rise beyond what it saw; small labels "linear extrapolates" on the teal line and "tree plateaus" on the orange line; white background, scientific chart style.

---

## Figure 4 — Recursive forecast with a widening uncertainty band

**แนวคิด:** พยากรณ์หลายก้าวทำด้วยการวน recursive — ทำนายเดือนถัดไปแล้วป้อนกลับเป็น feature — และทุกก้าวที่ไกลออกไป ความไม่แน่นอนสะสมทำให้แถบ ~95% ขยายตัว การตั้ง recalibration interval คือการเดินเข้าไปในแถบนั้นจนกว่าขอบบนจะแตะ tolerance limit

**จุดประสงค์ของภาพ:** สรุปผลลัพธ์ปลายทางของโมดูล — ภาพเดียวที่ผูก forecasting กลับเข้าเคสเมโทรโลยีเรื่องรอบการสอบเทียบซ้ำ

**องค์ประกอบภาพ:** ซีรีส์จริงส่วนท้าย (เส้น dark slate) แล้วต่อด้วยเส้นพยากรณ์ teal ไต่ต่อไปอนาคต รอบเส้นพยากรณ์มีแถบ teal อ่อนรูปกรวยบานออก; เส้นประแนวนอนสีแดงทำเครื่องหมาย tolerance limit; จุดที่ขอบบนของกรวยแตะเส้น tolerance มีเครื่องหมายกากบาทพร้อมป้าย "recalibrate before here"; เส้นประแนวตั้งแบ่งอดีต/อนาคต

**Image-gen prompt:**
> Educational forecast chart: recent history of a rising series in dark slate, continuing into the future as a teal forecast line with a light-teal funnel-shaped uncertainty band widening to the right; a horizontal dashed red line marking a tolerance limit above; a small cross and caption "recalibrate before here" where the upper edge of the funnel touches the tolerance line; vertical dotted divider between observed and forecast regions; white background, scientific chart style.

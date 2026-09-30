# explanation.md — Module M2: Thai OCR: ข้อมูลทดสอบ → CER

สคริปต์ภาพประกอบสำหรับผู้สอน — แต่ละหัวข้อ = หนึ่งภาพ: แนวคิด (ไทย) → จุดประสงค์ → องค์ประกอบ → image-gen prompt (English)

---

## Figure 1 — OCR pipeline และการวัดผลด้วย CER

**แนวคิด:** OCR = แปลง "ภาพที่มีตัวหนังสือ" เป็น "ข้อความ" และการวัดคุณภาพต้องมีข้อความจริง (ground truth) เทียบ

**จุดประสงค์ของภาพ:** ให้ผู้เรียนเห็นทั้ง pipeline และ "ไม้บรรทัด" ที่ใช้เทียบโมเดลก่อนลงมือ

**องค์ประกอบภาพ:** ซ้าย: ภาพสแกนหน้าเอกสารไทย → ลูกศรผ่าน 2 กล่อง "text detection (หากล่องบรรทัด)" และ "text recognition (อ่านตัวอักษร)" → ขวา: ข้อความไทยที่ได้ ขวาล่าง: กล่องเทียบข้อความจริง vs ข้อความที่อ่านได้ มีตัวอักษรผิดไฮไลต์สีแดง และป้ายสูตร "CER = จำนวนตัวอักษรที่ต้องแก้ / ความยาวข้อความจริง"

**Image-gen prompt:**
> Educational diagram for an OCR lesson: on the left a scanned Thai document page; an arrow flows through two labeled boxes "text detection" (bounding boxes around lines) and "text recognition" (letter boxes magnified); on the right the extracted Thai text block; below it a comparison panel showing reference Thai text versus OCR output with two mismatched characters highlighted in red and a formula badge "CER = edits / length of reference"; flat vector infographic style, white background, teal-coral-slate palette.

---

## Figure 2 — Bake-off: แข่งบนชุดทดสอบเดียวกัน

**แนวคิด:** เทียบโมเดลต้องใช้ชุดทดสอบชุดเดียวกัน วิธีวัดเดียวกัน — เหมือนการสอบเทียบที่วัดชิ้นงานมาตรฐานเดียวกัน

**จุดประสงค์ของภาพ:** ทำให้หลัก "fair comparison" เป็นภาพจำ และเชื่อมกับวินัยการสอบเทียบของผู้เรียน

**องค์ประกอบภาพ:** สนามวิ่ง 3 ช่องทาง; จุดสตาร์ทคือภาพเอกสารไทย 20 ใบ (กองเดียวกัน) ป้อนเข้า 3 ช่องทางชื่อ "Tesseract tha", "EasyOCR", "thai-trocr"; เส้นชัยคือกองข้อความที่ได้ ส่งต่อเข้าเครื่องชั่งที่มีเข็มแสดง "CER" ต่างกัน 3 ค่า (สูง/กลาง/ต่ำ) มีป้าย "ชุดทดสอบเดียวกัน · seed เดียวกัน · วิธีวัดเดียวกัน"

**Image-gen prompt:**
> Educational diagram of a fair model comparison: a single stack of 20 small Thai document cards feeds three parallel race lanes labeled "Tesseract tha", "EasyOCR", and "thai-trocr"; each lane ends at a weighing-scale device with a needle labeled "CER" showing three different levels (high, medium, low); a banner above reads "same test set, same metric, same seed"; flat vector infographic style, white background, teal-coral-slate palette, metrology-lab mood with a calibration-weight icon.

---

## Figure 3 — Surya: มองโครงสร้างหน้ากระดาษ

**แนวคิด:** OCR ตัวอักษรบอก "อ่านว่าอะไร" — layout analysis บอกว่า "อะไรอยู่ตรงไหน" (หัวเรื่อง/ย่อหน้า/ตาราง) และ table extraction บอก "ตารางมีกี่แถวกี่คอลัมน์"

**จุดประสงค์ของภาพ:** ให้เห็นว่าเอกสารเมโทรโลยี (ตารางค่าการวัด) ต้องการทั้งสองชั้น

**องค์ประกอบภาพ:** หน้ารายงานการสอบเทียบไทยหน้าเดียวสลายเป็น 3 เลเยอร์ซ้อน: เลเยอร์ 1 กล่องสีต่าง ๆ รอบหัวเรื่อง/ย่อหน้า/ตาราง/รูปพร้อมป้ายชื่อ label; เลเยอร์ 2 ในกล่องตารางมีเส้นแถว (สีน้ำเงิน) และเส้นคอลัมน์ (สีส้ม) ตัดกันเป็นตาราง; เลเยอร์ 3 ช่องตารางถูกเน้นเป็นช่อง ๆ พร้อมลูกศร "crop → OCR ต่อช่อง"

**Image-gen prompt:**
> Three-layer exploded view of one Thai calibration-report page: layer one shows colored bounding boxes around title, paragraphs, a table and a chart with category labels; layer two highlights the table region with blue row lines and orange column lines crossing it; layer three shows individual table cells outlined, with an arrow labeled "crop each cell, then OCR" pointing to a magnified single cell containing a measurement value like "24.6"; flat vector infographic style, white background, teal-coral-slate palette.

---

## Figure 4 — เลือกโมเดลอย่างไรตามงาน

**แนวคิด:** ไม่มีโมเดลใดชนะทุกงาน — เลือกตามชนิดเอกสารและต้นทุน

**จุดประสงค์ของภาพ:** สรุปเป็น decision guide ที่ผู้เรียนจำไปใช้ใน capstone ได้

**องค์ประกอบภาพ:** ต้นไม้ตัดสินใจ 3 ทางจากกล่องกลาง "เอกสารที่ต้อง OCR": ทางซ้าย "บรรทัดเดียว/ลายมือ → thai-trocr (เร็ว, แม่น, ต้องตัดบรรทัดก่อน)"; ทางกลาง "หน้าเต็มหลายบรรทัด → EasyOCR / Surya pipeline"; ทางขวา "ต้องการโครงสร้างตาราง → Surya layout + table"; มุมล่างมีป้ายหมุด "GPU จำเป็น? → Typhoon-OCR-3B (demo ผู้สอน)"

**Image-gen prompt:**
> Decision-tree infographic: a central box "Thai document to OCR" branching into three paths; left branch labeled "single line / handwriting" leading to a card "thai-trocr — fast, accurate, needs line crops first"; middle branch "full page, many lines" leading to "EasyOCR or Surya pipeline"; right branch "need table structure" leading to "Surya layout + table extraction"; bottom corner a pinned badge "needs GPU? Typhoon-OCR-3B (instructor demo)"; flat vector style, white background, teal-coral-slate palette.

# explanation.md — Module M3: สอนโมเดลอ่านใจจากข้อความไทย (fine-tune mBERT)

สคริปต์ภาพประกอบสำหรับผู้สอน — แต่ละหัวข้อ = หนึ่งภาพ: แนวคิด (ไทย) → จุดประสงค์ → องค์ประกอบ → image-gen prompt (English)
ทำรูปที่เหมาะสมสำหรับกระดาษ A4 แนวนอน (landscape) และใช้ palette สีเหมือน logo ของ Mirsofot windows
---

## Figure 1 — ทำไมภาษาไทยตัดคำยาก

**แนวคิด:** ภาษาไทยไม่เว้นวรรคระหว่างคำ — เครื่องอ่านต้องเดาขอบเขตคำ และการเดาผิดเปลี่ยนความหมาย

**จุดประสงค์ของภาพ:** ให้ผู้เรียนเห็นว่า "ตัดคำ" เป็นโจทย์จริงของ NLP ไทย ก่อนเข้าโมเดลใหญ่

**องค์ประกอบภาพ:** ประโยคไทยยาวหนึ่งบรรทัดเขียนติดกันไม่มีช่องว่าง ด้านล่างมีสองแถวของการตัดด้วยเส้นแบ่งสีต่างกัน (สีฟ้า = การตัดถูก, สีส้ม = การตัดผิดตำแหน่ง) และข้อความไทยแปลวลา "same characters, different words"

**Image-gen prompt:**
> Educational diagram about Thai word segmentation: one long continuous line of Thai text with no spaces at the top; below it two alternative ways of slicing the same text into word chunks, one row of correctly-cut segments outlined in teal, one row of wrongly-cut segments outlined in orange with a puzzled-face icon; small caption "same characters, different words"; flat vector infographic style, white background, teal-coral-slate palette.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
---

## Figure 2 — wordpiece: ไม่ตัดเป็น "คำ" ก็ได้

**แนวคิด:** mBERT หั่นข้อความเป็นชิ้นย่อย (subword) จากคลังคงที่ ~119k ชิ้น — ไม่ต้องแก้ปัญหาตัดคำ

**จุดประสงค์ของภาพ:** เชื่อมจาก Figure 1 → แนวทางของ transformer

**องค์ประกอบภาพ:** ประโยคไทยเดียวกันถูกหั่นด้วยกรรไกรเป็นชิ้นเล็ก ๆ ขนาดไม่เท่ากัน แต่ละชิ้นมีเลขกำกับ (token id) ลูกศรจากชิ้นทั้งหมดเข้ากล่อง "mBERT (104 ภาษา)"

**Image-gen prompt:**
> Diagram of subword tokenization: a line of Thai text cut by scissors into small uneven pieces (some one character, some several), each piece in a rounded rectangle with a small number tag under it, arrows from all pieces into a large box labeled "mBERT - 104 languages"; flat vector style, white background, teal-coral palette.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)

---

## Figure 3 — fine-tune mBERT: ยืมสมอง ใส่หัวใหม่

**แนวคิด:** mBERT เทรนมาแล้วบน 104 ภาษา — เราเทรนต่อด้วยข้อมูลไทย 8k ข้อความให้ทำโจทย์ sentiment 4 class

**จุดประสงค์ของภาพ:** อธิบายว่า fine-tune ต่างจากเทรนจากศูนย์ และต่างจาก freeze+head ของ M1 อย่างไร

**องค์ประกอบภาพ:** ตึกหลายชั้นใหญ่ "mBERT pre-trained" ไม่มีหิมะ/โซ่ (ปลดล็อก — เทรนทั้งตัว) บนดาดฟ้าติดกล่องใหม่ "head: 4 ทางออก (pos/neu/neg/q)" ลูกศรข้อความไทยเข้าตึก → ออกจากหัว มีป้าย "ข้อมูลของเรา 8,000 ข้อความ"

**Image-gen prompt:**
> Transfer learning diagram: a tall multi-story building labeled "mBERT pre-trained on 104 languages" WITHOUT chains or ice (fully trainable, warm arrows flowing through all floors); on its roof a small new box labeled "head: 4 outputs"; a stream of short Thai text snippets flows into the entrance and 4 colored label chips (positive, neutral, negative, question) exit the rooftop box; badge reading "fine-tuned on our 8,000 labeled texts"; flat vector infographic style, white background, teal-coral-slate palette.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)

---

## Figure 4 — loss ลดราย epoch

**แนวคิด:** การเทรน = ลด loss ทีละ epoch; val loss ที่ลดตาม = เรียนรู้จริง, ที่เบนขึ้น = overfit

**จุดประสงค์ของภาพ:** ให้ผู้เรียนอ่านกราฟ loss เป็น

**องค์ประกอบภาพ:** กราฟเส้นสองเส้น (train ลดชัน, validation ลดตามช้ากว่า) แกน x = epoch 1..3, แกน y = loss มีลูกศรหมายเหตุ "ลดลง = เรียนรู้" และจุดไข่ปลาว่า "val ขึ้น = overfit"

**Image-gen prompt:**
> Line chart teaching loss curves: x-axis "epoch 1,2,3", y-axis "loss"; a steep decreasing teal line labeled "train loss" and a slower decreasing coral dashed line labeled "validation loss"; a small annotation arrow "going down = learning"; a faint ghost extension beyond epoch 3 where the validation line curls upward with a warning tag "overfit"; clean flat vector style, white background.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)

---

## Figure 5 — อ่าน precision/recall ต่อ class

**แนวคิด:** accuracy เดียวหลอกได้เมื่อ class ไม่สมดุล — ต้องดูราย class

**จุดประสงค์ของภาพ:** ทบทวนนิยาม precision/recall แบบภาพ (ใช้ภาษาเดียวกับโน้ตช่วยใน book)

**องค์ประกอบภาพ:** สองแถวไอคอน: แถวบน (precision) กลุ่มข้อความที่โมเดลตอบ "neg" → นับเฉพาะที่ถูกจริง; แถวล่าง (recall) กลุ่มข้อความที่เป็น "neg" จริง → นับส่วนที่โมเดลจับได้ มีสูตรสั้น ๆ ใต้ภาพ

**Image-gen prompt:**
> Two-row diagram explaining precision vs recall for a class "negative": top row shows chat bubbles the model labeled negative with only some highlighted as truly negative, caption "precision: of what the model flagged, how many were right"; bottom row shows all truly negative bubbles with a net catching most but missing some, caption "recall: of what was truly there, how many did we catch"; flat vector infographic style, white background, teal-coral palette.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)

---

## Figure 6 — Error inspection loop

**แนวคิด:** ตัวเลขบอก "พลาดเท่าไร" การแกะดูตัวอย่างที่ผิดจริงบอก "พลาดเพราะอะไร"

**จุดประสงค์ของภาพ:** ฝังนิสัย "เชื่อตัวเลขหลังดู error"

**องค์ประกอบภาพ:** วงจรสี่ขั้น: metric ต่อ class → ดึงตัวอย่างที่ผิด → อ่านข้อความจริง → เดา pattern/แก้ (เพิ่มข้อมูล/ปรับตั้งค่า) ลูกศรวนกลับ

**Image-gen prompt:**
> Circular four-step process diagram: step 1 a small bar chart labeled "per-class metrics", step 2 a magnifying glass over chat bubbles labeled "pull misclassified examples", step 3 a person reading text labeled "inspect real messages", step 4 a lightbulb labeled "find patterns, adjust", arrows looping back to step 1; flat vector style, white background, teal-coral-slate palette.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
---

## Figure 7 — embedding + kNN

**แนวคิด:** โมเดลภาษาแปลงข้อความเป็นจุดในปริภูมิ — ข้อความอารมณ์/ความหมายใกล้กันอยู่ใกล้กัน kNN หา "ข้อความเดิมที่เหมือนสุด"

**จุดประสงค์ของภาพ:** อธิบาย demo 5 นาทีท้ายโมดูล

**องค์ประกอบภาพ:** scatter 3 กลุ่มสี (pos/neu/neg) จุด query สีดำมีเส้นวงกลมวงล้อม จุดใกล้สุด 5 จุดถูกไฮไลต์

**Image-gen prompt:**
> 2D scatter plot showing three soft clusters of dots in teal (positive), slate (neutral), coral (negative); one black star point as the query with a dashed circle around it highlighting the five nearest dots, thin lines connecting the star to those five neighbors; axis labels "embedding dimension 1 / 2"; flat vector style, white background.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
---

## Figure 8 — zero-shot vs supervised

**แนวคิด:** โมเดล multilingual ใช้ข้ามภาษาแบบ zero-shot ได้ (ฟรีแต่หยาบ) — มี label แล้ว supervised แม่นกว่าชัด

**จุดประสงค์ของภาพ:** สรุปท้ายโมดูล

**องค์ประกอบภาพ:** เทียบสองเส้นทาง: ทางซ้าย โมเดลสำเร็จรูป (ไม่มีข้อมูลไทย) ตอบข้อความไทยด้วยเครื่องหมาย "?" ความแม่นต่ำ; ทางขวา โมเดล + กองข้อความ label ของเรา → ความแม่นสูง

**Image-gen prompt:**
> Side-by-side comparison: left path a ready-made model box with a globe icon but NO Thai data, answering Thai chat bubbles with question marks and a low accuracy gauge; right path the same model box plus a stack of labeled Thai text cards feeding into it, answering confidently with a high accuracy gauge; flat vector infographic style, white background, teal-coral-slate palette.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
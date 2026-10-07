# explanation.md — Module M4-CNN: เทรน spectrogram CNN จากศูนย์ บน ESC-50

สคริปต์ภาพประกอบสำหรับผู้สอน — แต่ละหัวข้อ = หนึ่งภาพ: แนวคิด (ไทย) → จุดประสงค์ → องค์ประกอบ → image-gen prompt (English)
ทำรูปที่เหมาะสมสำหรับกระดาษ A4 แนวนอน (landscape) และใช้ palette สีเหมือน logo ของ Mirsofot windows
---

## Figure 1 — spectrogram คือ "ภาพ" ที่ CNN อ่านได้

**แนวคิด:** เสียง 1 มิติ (เวลา) ถูกจัดเรียงใหม่เป็นภาพ 2 มิติ (เวลา × ความถี่) — พอเป็นภาพ เครื่องมือจาก M1 ก็ใช้ได้ทันที

**จุดประสงค์ของภาพ:** ให้ผู้เรียนเห็นว่า CNN ไม่ได้ "เข้าใจเสียง" โดยตรง — มันอ่านภาพ spectrogram แล้วเราเลือกให้มันเห็นเสียงในรูปที่ถูกต้อง

**องค์ประกอบภาพ:** ซ้าย: คลื่นเสียงยาว 1 แถว → ลูกศร "STFT + mel filter" → ขวา: heatmap 128×216 ที่มี texture ชัด (แถบนอน = โทนยาว, เส้นตั้ง = เสียงกระแทก, เส้นโค้ง = เสียงร้อง) — ล่างขวา: ไอคอน CNN จิ๋วชี้มาที่ heatmap

**Image-gen prompt:**
> Educational diagram: a one-dimensional sound wave on the left transforms (arrow labeled "STFT + mel filters") into a 2D heatmap "image" on the right, 128x216 pixels, with visible textures: horizontal bright bands, vertical impact lines, curved singing shapes; a tiny CNN icon looks at the heatmap with a magnifying glass; flat vector infographic style, white background, teal-coral-slate palette, clean sans-serif labels.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
---

## Figure 2 — ทำไม CNN ชนะ RF: ข้อมูลที่โมเดล "เห็น" ต่างกัน

**แนวคิด:** RF กินสรุป 40 ตัวเลข (mean/std ของ MFCC) — ลวดลายตามเวลาถูกทิ้งไป; CNN อ่าน spectrogram เต็มและเรียนรู้ pattern เอง

**จุดประสงค์ของภาพ:** อธิบายช่องว่าง accuracy ระหว่างสองวิธีด้วย "ข้อมูลที่หายไป" ไม่ใช่ "โมเดลเก่งกว่า"

**องค์ประกอบภาพ:** ซ้าย: heatmap 128×216 มีลูกศรหนา ๆ ยุบลงเป็นแถบ 40 ช่อง (บาง texture ตกพื้นมีเครื่องหมายกากบาท) → RF → accuracy ~45%; ขวา: heatmap เดียวกันเข้า CNN โดยตรง → accuracy ~65%+ — มีป้าย "ข้อมูลเดียวกัน, fold เดียวกัน"

**Image-gen prompt:**
> Split comparison diagram, banner on top reading "same data, same test fold": left side shows a spectrogram heatmap squeezed into a 40-number strip (a few texture details falling out marked with red X icons) feeding a decision-tree forest icon with an accuracy bar labeled ~45%; right side shows the full heatmap feeding a small layered CNN icon with a taller accuracy bar labeled ~65%+; flat vector infographic style, white background, teal-coral palette.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
---

## Figure 3 — CNN จากศูนย์: สถาปัตยกรรมจิ๋ว 3 ชั้น conv

**แนวคิด:** โครงข่ายเดียวกับที่ผู้เรียนเทรนเองใน M1 ขยายจาก 2 ชั้นเป็น 3 ชั้น conv เพราะ "ภาพ" 128×216 ใหญ่กว่า 28×28 มาก

**จุดประสงค์ของภาพ:** ให้ผู้เรียนเชื่อมว่านี่คือทักษะเดิม (Conv/Pool/Flatten/Linear) ใช้กับข้อมูลใหม่ ไม่มีแนวคิดเครือข่ายใหม่ที่ต้องเรียนเพิ่ม

**องค์ประกอบภาพ:** ซ้าย: ภาพ spectrogram 1 ช่อง (ช่องสีเดียว — grayscale) → Conv(32) → MaxPool → Conv(64) → MaxPool → Conv(64) → MaxPool → Flatten → Linear(50) → ป้าย 50 class — ขนาดภาพลดจาก 128×216 → 64×108 → 32×54 → 16×27 แสดงเป็นกล่องเล็กลงตามลำดับ

**Image-gen prompt:**
> Architecture pipeline diagram: a spectrogram "image" (one grayscale channel, 128x216) passes left to right through Conv(32) -> MaxPool -> Conv(64) -> MaxPool -> Conv(64) -> MaxPool -> Flatten -> Linear(50); intermediate feature-map boxes get visually smaller at each pool step with size labels 64x108, 32x54, 16x27; final output row of 50 labeled slots; flat vector infographic, white background, teal-coral-slate palette.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
---

## Figure 4 — ทำงานบน Kaggle: GPU, internet, และข้อมูล ~600 MB

**แนวคิด:** โมดูลนี้หนักเกิน CPU เครื่องเรียน — เทรนจริงบน T4 ฟรีของ Kaggle โดยดาวน์โหลดข้อมูลใน notebook เอง (ห้าม bundle ลงสื่อ — CC BY-NC)

**จุดประสงค์ของภาพ:** อธิบาย workflow ของห้องเรียนก่อนเริ่ม: สมัคร/ยืนยันบัญชี, เปิด GPU + Internet, กด Run All, รอ ~20 นาที

**องค์ประกอบภาพ:** ซ้าย: ไอคอนเบราว์เซอร์ kaggle.com มีปุ่มตั้งค่าสองปุ่ม "Accelerator: GPU T4" และ "Internet: On" → กลาง: notebook ที่กำลังดาวน์โหลดก้อนเมฆ zip "ESC-50 ~600 MB" → ขวา: การ์ด GPU T4 ที่เร่งรอบเทรน CNN พร้อมเส้นเวลา "~20–25 นาที"

**Image-gen prompt:**
> Workshop workflow diagram: left a browser window labeled kaggle.com with two toggle switches "Accelerator: GPU T4" and "Internet: On"; center a notebook screen downloading a cloud labeled "ESC-50 ~600 MB"; right a GPU card labeled "T4" powering a small CNN training with a progress timeline labeled "~20-25 minutes"; flat vector infographic style, white background, teal-coral-slate palette.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
---

## Figure 5 — bake-off บน fold เดียวกัน: อ่านผลแบบนักวิจัย

**แนวคิด:** การเทียบยุติธรรมต้องใช้ข้อมูลทดสอบชุดเดียวกัน — ตารางสรุปทั้งค่าที่เราวัดเองและค่าอ้างอิงจาก paper

**จุดประสงค์ของภาพ:** สอนวิธี "อ่าน" ผลเปรียบเทียบ: ค่าที่วัดเอง vs baseline ที่เผยแพร่ vs คนจริง — และถามต่อว่าคุ้มต้นทุนไหม

**องค์ประกอบภาพ:** แผนภูมิบาร์ 4 แท่งแนวนอน: "RF + MFCC (เราวัด) ~45%", "CNN จิ๋ว (เราวัด) ~65%+", "CNN baseline ของ paper 64.5%", "คนจริง 81.3%" — แท่งของเรามีขอบเส้นประ (บอกว่าค่าจริงขึ้นกับรอบ) ด้านขวามีกล่องคำถาม "คุ้มต้นทุน GPU ไหม?"

**Image-gen prompt:**
> Horizontal bar chart graphic titled "measured vs published": four bars — "our RF + MFCC ~45%" (dashed outline, mint), "our small CNN ~65%+" (dashed outline, coral), "published CNN baseline 64.5%" (solid slate), "human accuracy 81.3%" (solid dark gray); a question box on the right labeled "is the gain worth the GPU cost?"; flat vector infographic style, white background, teal-coral-slate palette, clean sans-serif labels.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)

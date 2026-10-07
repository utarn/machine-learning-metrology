# explanation.md — Module M5: เทรนโมเดลฟังเสียงจากศูนย์ + Demucs + ASR bake-off

สคริปต์ภาพประกอบสำหรับผู้สอน — แต่ละหัวข้อ = หนึ่งภาพ: แนวคิด (ไทย) → จุดประสงค์ → องค์ประกอบ → image-gen prompt (English)
ทำรูปที่เหมาะสมสำหรับกระดาษ A4 แนวนอน (landscape) และใช้ palette สีเหมือน logo ของ Mirsofot windows

---

## Figure 1 — เสียงคือตัวเลขอยู่แล้ว: จาก waveform สู่ log-mel spectrogram

**แนวคิด:** ไฟล์เสียงคือตัวเลขความดันอากาศต่อเวลา — แต่ CNN อ่าน "ภาพ" ได้ดีกว่า จึงแปลงเป็น log-mel spectrogram (เวลา × ความถี่)

**จุดประสงค์ของภาพ:** ให้ผู้เรียนเห็นการแปลงสามขั้น waveform → spectrogram → log-mel ว่าคือการจัดรูปข้อมูล ไม่ใช่การเปลี่ยนข้อมูล

**องค์ประกอบภาพ:** สามแถวซ้อนกันของคลิปเสียง 1 วินาทีเดียวกัน แถวบน: เส้นคลื่นบดบัง (waveform) แถวกลาง: แถบสีความถี่-เวลา (spectrogram) แถวล่าง: ภาพ log-mel 64 แถบที่สีสม่ำเสมอกว่า มีลูกศรเชื่อมระหว่างแถวพร้อมป้าย "16000 ตัวเลข/วินาที" "หั่นหน้าต่าง + FFT" "สเกล mel + log"

**Image-gen prompt:**
> Educational diagram of audio feature extraction, three stacked panels of the same one-second sound: top a jagged line waveform labeled "16,000 numbers per second", middle a colorful spectrogram with an arrow labeled "window + FFT", bottom a smoother log-mel heatmap labeled "mel scale + log"; flat vector infographic style, white background, teal-coral-slate palette.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)

---

## Figure 2 — 12 class: 10 คำสั่ง + unknown + silence

**แนวคิด:** ระบบฟังคำสั่งจริงต้องตอบได้ทั้ง "คำที่รู้จัก" และ "ไม่ใช่คำสั่ง" — เราจึงเพิ่ม 2 class พิเศษ

**จุดประสงค์ของภาพ:** อธิบายว่าทำไม KWS ไม่ใช่การจำแนก 10 คำเท่านั้น และ `_silence_` สร้างจากเสียงห้องจริงได้

**องค์ประกอบภาพ:** วงกลมกลางแบ่ง 12 ส่วน สิบส่วนมีป้ายคำสั่ง (down/go/left/no/off/on/right/stop/up/yes) หนึ่งส่วนป้าย "unknown — คำอื่น 25 คำ" อีกส่วนป้าย "silence — เสียงห้อง" รอบ ๆ มีไอคอนไมโครโฟนและไอคอนหู

**Image-gen prompt:**
> Diagram of a 12-segment pie wheel for a keyword-spotting classifier: ten teal segments labeled down, go, left, no, off, on, right, stop, up, yes; one coral segment labeled "unknown (25 other words)"; one gray segment labeled "silence (room noise)"; small microphone and ear icons around the wheel; flat vector infographic style, white background.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)

---

## Figure 3 — เทรน CNN จากศูนย์: น้ำหนักเริ่มแบบสุ่ม

**แนวคิด:** "จากศูนย์" = ค่าน้ำหนักทุกตัวเริ่ม random แล้ว gradient descent ปรับตาม loss จากข้อมูลเรา — ต่างจาก transfer learning (M1/M3) ที่ยืมสมองสำเร็จรูป

**จุดประสงค์ของภาพ:** เชื่อมโมเดลเสียงกับโมเดลภาพ M1 — เทคนิคเดียวกัน แค่ "ภาพ" เป็น spectrogram

**องค์ประกอบภาพ:** ภาพ log-mel เข้าซ้าย ผ่านชั้น conv+pool สามชั้น (กล่องซ้อนเล็กลงเรื่อย ๆ ป้าย 16 → 32 → 64 channel) ออกขวาเป็น 12 ช่องคะแนน ใต้ภาพมีเส้นประกอบ "weights เริ่มแบบสุ่ม — ไม่มี pre-trained" และลูกศรวนย้อนกลับ labeled "gradient descent 6 epochs"

**Image-gen prompt:**
> Diagram of a small CNN for audio classification: a log-mel spectrogram image on the left flows through three conv+pool blocks drawn as shrinking stacked boxes labeled 16, 32, 64 channels, then two dense layers ending in 12 output slots; below, a curved backpropagation arrow labeled "gradient descent, weights start random — no pre-training"; flat vector infographic style, white background, teal-coral-slate palette.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)

---

## Figure 4 — อ่าน loss/accuracy ราย epoch

**แนวคิด:** รอบเทรนพิมพ์ loss (ควรลด) และ accuracy ทั้ง train/val (ควรขึ้น) — ตัวเลขคู่นี้บอกว่าโมเดล "เรียนรู้" หรือ "ท่องจำ"

**จุดประสงค์ของภาพ:** ฝึกอ่านกราฟการเทรนเป็น — ทักษะเดียวกันกับทุก modality ในคอร์ส

**องค์ประกอบภาพ:** กราฟคู่ซ้าย-ขวา ซ้าย: เส้น loss ลดชันพร้อมป้าย "ลด = เรียนรู้" ขวา: เส้น accuracy ขึ้นสองเส้น (train สูงกว่า val เล็กน้อย) มีช่องว่างระหว่างเส้น labeled "gap = เริ่มท่องจำ"

**Image-gen prompt:**
> Two side-by-side line charts: left chart a decreasing teal loss curve labeled "going down = learning"; right chart two rising accuracy curves, train slightly above validation, with the shaded gap between them labeled "gap = memorizing"; clean flat vector style, white background, teal-coral palette.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)

---

## Figure 5 — confusion matrix ของเสียง: อ่านว่าโมเดลสับสนอะไร

**แนวคิด:** accuracy เดียวไม่พอ — confusion matrix บอกว่าโมเดลสับสนคู่ไหน และ `_unknown_` มักเป็น class ที่อ่อนที่สุด

**จุดประสงค์ของภาพ:** ให้ผู้เรียนอ่านตาราง 12×12 อย่างเป็นระบบ (ทแยง = ถูก, นอกทแยง = ผิด)

**องค์ประกอบภาพ:** ตารางสีน้ำเงิน 12×12 มีแถบเข้มตามแนวทแยง มีวงกลมสีส้มล้อมช่องนอกทแยงที่สีเข้มสุดสองช่องพร้อมลูกศร "คู่สับสนสูงสุด" แกนมีป้ายชื่อคำย่อ 10 คำ + unk + sil

**Image-gen prompt:**
> Educational confusion matrix diagram: a 12 by 12 blue heatmap grid with a strong dark diagonal labeled "correct"; two off-diagonal cells circled in orange with an arrow labeled "top confusions"; axis tick labels read down, go, left, no, off, on, right, stop, up, yes, unk, sil; flat vector infographic style, white background.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)

---

## Figure 6 — Demucs: เพลงหนึ่งชิ้น → สี่แทร็ก

**แนวคิด:** source separation = โมเดลเรียน "เสียงของแต่ละชนิดเครื่องดนตรีหน้าตาเป็นอย่างไร" จากข้อมูลมหาศาล แล้วแยกออกจากกัน — ผลลัพธ์คือเสียงจริงที่ฟังกลับได้

**จุดประสงค์ของภาพ:** ให้ผู้เรียนเห็นว่า Demucs ต่างจาก KWS — ไม่ใช่จำแนก "คลิปนี้คืออะไร" แต่สร้างเสียง 4 ชุดพร้อมกัน

**องค์ประกอบภาพ:** ท่อเสียงใหญ่ (เพลง mix) ไหลเข้ากล่อง "Demucs htdemucs" แล้วแตกออกเป็นสี่ท่อ: กลอง/เบส/เครื่องดนตรีอื่น/เสียงร้อง แต่ละท่อมีรูป waveform ของตัวเอง มีป้ายเล็ก "แยกได้จริงแต่ไม่สมบูรณ์ — เสียงซึมข้ามแทร็กได้"

**Image-gen prompt:**
> Diagram of music source separation: one thick audio stream labeled "mix" enters a box labeled "Demucs htdemucs" and splits into four separate pipes labeled drums, bass, other, vocals, each pipe ending in its own small waveform drawing; a small footnote tag reads "imperfect — some sound leaks between stems"; flat vector infographic style, white background, teal-coral-slate palette.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)

---

## Figure 7 — ASR bake-off: เสียงเดียวกัน สองโมเดล วัดด้วย WER

**แนวคิด:** เปรียบเทียบโมเดลอย่างเป็นธรรม = ชุดทดสอบเดียวกัน + ตัวชี้วัดเดียวกัน — เหมือนการสอบเทียบเครื่องมือสองเครื่องด้วยตัวชิ้นงานอ้างอิงชุดเดียว

**จุดประสงค์ของภาพ:** สรุป pipeline ของการวัด ASR ก่อนดูผลจริง

**องค์ประกอบภาพ:** คลิปเสียงไทยอยู่กลาง แตกเป็นสองเส้นทาง: เส้นซ้ายเข้ากล่อง "Whisper-small (หลายภาษา)" เส้นขวาเข้ากล่อง "Typhoon-ASR-0.6B (เทรนเสียงไทย ~10,800 ชม.)" ทั้งสองเส้นรวมกันที่กล่อง "jiwer — เทียบกับบทอ้างอิง" ออกเป็นป้ายคะแนน WER/CER สองแถบ

**Image-gen prompt:**
> Diagram of an ASR comparison pipeline: a Thai speech clip in the center splits into two paths, left into a box labeled "Whisper-small (multilingual)", right into a box labeled "Typhoon-ASR-0.6B (trained on Thai)"; both paths merge into a box labeled "jiwer — compare with reference transcript" ending in two score badges WER and CER; flat vector infographic style, white background, teal-coral palette.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)

---

## Figure 8 — WER นับยังไง: S + I + D

**แนวคิด:** WER = (แทน S + ใส่เกิน I + ตกหล่น D) / จำนวนคำอ้างอิง — สองผลถอดที่ได้ WER เท่ากันอาจผิดคนละแบบ

**จุดประสงค์ของภาพ:** ให้ผู้เรียนนับ WER ด้วยมือได้ และเข้าใจว่าทำไมต้องดูตัวอย่างจริงประกอบ

**องค์ประกอบภาพ:** แถบคำอ้างอิงสามคำวางเรียง ใต้มันเป็นสองแถวผลถอด แถวหนึ่งมีคำหนึ่งขีดฆ่าแล้วแทนคำใหม่ (S) อีกแถวมีคำหายไปหนึ่งช่องว่างว่างเปล่า (D) มุมขวามีสูตร "WER = (S+I+D) / N" และป้ายเตือน "WER เท่ากัน ≠ ผิดแบบเดียวกัน"

**Image-gen prompt:**
> Educational diagram of word error rate: a reference row of three word boxes on top; below it two hypothesis rows, the first with one word crossed out and replaced (labeled S, substitution), the second with one empty gap where a word is missing (labeled D, deletion); a formula card on the right reads "WER = (S+I+D) / N"; a small warning tag reads "equal WER, different mistakes"; flat vector infographic style, white background.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)

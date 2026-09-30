# explanation.md — Module M8: Capstone (3 tracks + rubric)

สคริปต์ภาพประกอบสำหรับผู้สอน (สไลด์ kickoff 11:30–12:00) — แต่ละหัวข้อ = หนึ่งภาพ:
แนวคิด (ไทย) → จุดประสงค์ → องค์ประกอบ → image-gen prompt (English)

---

## Figure 1 — ครึ่งวันสุดท้าย: kickoff → สร้าง → นำเสนอ

**แนวคิด:** capstone คือวงจร "มีข้อมูล → ให้ ML เรียนรู้ → ได้โมเดล → วัดผล"
ที่ทีมเดินเองครบรอบ โดยมีเวลาจำกัดจริง — เวลาที่เหลือให้ "วัดผล + เตรียมพูด"
เสมอ ไม่ใช่จูนโมเดลจนวินาทีสุดท้าย

**จุดประสงค์ของภาพ:** ตั้งความคาดหวังเรื่องเวลาตั้งแต่ kickoff — ทีมส่วนใหญ่
จะใช้เวลาไม่พอถ้าไม่วางแผนตามภาพนี้

**องค์ประกอบภาพ:** แถบเวลาแนวนอนครึ่งวัน: กล่อง "kickoff 30 นาที — แบ่งทีม,
เลือก track, รับ starter" → กล่องใหญ่ "สร้าง 2 ชั่วโมง" ที่ข้างในแบ่งเป็น
ขั้น data → เทรน → วัดผล → เตรียมพูด (เขียนว่า "เผื่อ 20 นาทีสุดท้ายไว้
เตรียมพูดเสมอ") → กล่อง "นำเสนอ 90 นาที — ทีมละ 10 นาที"; ผู้สอนเดินดูแล
ในช่วงกลาง (ไอคอนคนยืนบนแถบเวลา)

**Image-gen prompt:**
> Horizontal timeline of a half-day capstone session: a small kickoff box
> (30 minutes: form teams, pick track, receive starter), a large two-hour
> build box containing four inner stages labeled data, train, measure,
> prepare-talk with a note "reserve the last 20 minutes for the talk",
> and a final 90-minute presentation box subdivided into 10-minute team
> slots; a small instructor icon walking along the build phase; flat
> vector infographic style, white background, teal-coral-slate palette.

---

## Figure 2 — 3 tracks: เลือกจาก "ข้อมูลที่ทีมมี" ไม่ใช่ความชอบ

**แนวคิด:** แต่ละแทร็กคือ modality คนละตระกูล (image / sound / document)
แต่วงจรเดียวกัน — ตัวตัดสินที่ดีที่สุดคือ **ทีมมีข้อมูลแบบไหนอยู่แล้ว**
(หรืออยากถ่าย/อัด/สแกนอะไรให้เสร็จใน 2 ชั่วโมง)

**จุดประสงค์ของภาพ:** ใช้ในสไลด์ kickoff — ทีมตัดสินใจเลือก track ภายใน
5 นาทีด้วยเกณฑ์เดียวกัน

**องค์ประกอบภาพ:** สามการ์ดวางแนวนอน: (A) ภาพชิ้นงานโลหะครึ่งปกติครึ่งชำรุด
พร้อม heatmap — ข้อความ "มี/ถ่ายรูปได้ · ชำรุดหายากก็ทำได้ (PatchCore)";
(B) เสียงคลื่น+spectrogram — "อัดเสียงเครื่องจักรได้ ≥ 20 คลิปต่อสภาพ";
(C) เอกสารสแกนที่มีตารางตัวเลขกำลังถูก OCR — "มีรายงานการวัด/ตารางตัวเลข
ที่ยังเป็นกระดาษ"; ใต้การ์ดทุกใบ: "notebook + พูด 10 นาที — เกณฑ์เดียวกัน"

**Image-gen prompt:**
> Three parallel track cards side by side: card A a metal workpiece photo
> half normal half defect with an anomaly heatmap overlay and caption
> "have or can take photos; rare defects OK (PatchCore)"; card B a sound
> waveform and spectrogram with a microphone icon and caption "can record
> 20+ clips per condition"; card C a scanned document with a numeric table
> being converted by OCR into a pandas table and a chart, caption "have
> paper measurement reports"; under all three a shared banner reading
> "notebook + 10-minute talk, same rubric"; flat vector infographic style,
> white background, teal-coral-slate palette.

---

## Figure 3 — โครงการนำเสนอ 10 นาที

**แนวคิด:** นำเสนอที่ดีของงาน ML ไม่ใช่เรื่องเล่าทุกขั้นตอน แต่คือ
"โจทย์ 2 นาที → วิธี 3 นาที → ผล 3 นาที → ข้อจำกัด+ต่อยอด 2 นาที" —
และทุกส่วนตอบคำถามเดียว: **เรารู้อะไรขึ้นมาที่ไม่รู้ก่อน**

**จุดประสงค์ของภาพ:** เป็น template ที่ทีมลากไปทำสไลด์ได้ตรง ๆ
(สอดคล้อง rubric หมวด 4)

**องค์ประกอบภาพ:** แถบเวลา 10 ช่อง (1 นาที/ช่อง) แบ่งสี 4 ช่วง: 0–2
"โจทย์ + ข้อมูล" (แสดงตัวอย่างข้อมูลจริง), 2–5 "วิธี — เลือกเพราะอะไร",
5–8 "ผลลัพธ์ — metric + กราฟที่อ่านออกใน 10 วิ", 8–10 "ข้อจำกัด +
ถ้ามีเวลาอีกสัปดาห์"; เหนือช่วงสุดท้ายมีป้าย "ส่วนที่ทีมมักพลาด —
ห้ามตัดทิ้ง"

**Image-gen prompt:**
> A 10-segment horizontal time bar (one segment per minute) divided into
> four colored phases: minutes 0-2 "problem + data, show real samples",
> minutes 2-5 "method — and why this one", minutes 5-8 "results — metric
> plus one chart readable in 10 seconds", minutes 8-10 "limitations +
> next steps if one more week"; a small warning badge over the final
> phase reading "the part teams skip — don't"; flat vector infographic
> style, white background, teal-coral-slate palette.

---

## Figure 4 — Rubric: 5 หมวด 100 คะแนน

**แนวคิด:** คะแนนกระจายไปที่ "คิดเป็น" มากกว่า "ตัวเลขสวย" — วัดผลซื่อสัตย์
25 + วิเคราะห์ 20 + นำเสนอ 25 + craft 20 ส่วนความแม่นของโมเดลเด่นที่สุด
ไม่ใช่หมวดแยก แต่โผล่ในหมวด 3

**จุดประสงค์ของภาพ:** ตอบคำถามที่ทุกทีมถามใน kickoff: "ทำยาก ๆ ได้คะแนนเยอะไหม"
— คำตอบ: ทำ**ถูก**ได้คะแนนเยอะ

**องค์ประกอบภาพ:** วงกลม (donut chart) 5 ส่วน: โจทย์+ข้อมูล 10, วงจร ML+
วัดผลซื่อสัตย์ 25, ผลลัพธ์+วิเคราะห์ 20, นำเสนอ 25, reproducibility 20 —
มีเส้นผ่านที่ 60 และป้ายข้างวง "Restart & Run All ไม่ผ่าน = จำกัดที่ 60"

**Image-gen prompt:**
> Donut chart of five rubric categories: "problem and data 10", "ML loop
> and honest evaluation 25", "results and error analysis 20",
> "10-minute presentation 25", "reproducibility and craft 20"; a pass
> line marker at 60 points drawn across the donut with a side note
> "notebook must restart-and-run-all or capped at 60"; flat vector
> infographic style, white background, teal-coral-slate palette.

---

## Figure 5 — Bring-your-own: จัดการข้อมูลจริงอย่างซื่อสัตย์

**แนวคิด:** ทีมใช้ข้อมูลจริงได้เต็มที่ — ประเด็นเดียวที่ถูกวัดคือ
split ต้องตัดตาม "โลกที่เปลี่ยน" (ล็อตถ่าย / เซสชันอัด / หน้าเอกสาร)
ไม่ใช่สุ่มภาพปนกัน

**จุดประสงค์ของภาพ:** กันกับดัก leakage ที่เจอแน่นอนใน capstone —
ภาพ/คลิปจากการถ่าย-อัดเซสชันเดียวใกล้เคียงกันจน metric สวยหลอก

**องค์ประกอบภาพ:** สามแถว (รูป/เสียง/เอกสาร) แต่ละแถวแสดงกล่อง "เซสชัน 1,
เซสชัน 2, เซสชัน 3" ไหลเข้ากากบาท: เซสชัน 1–2 → train (สี teal), เซสชัน 3 →
test (สี coral) — พร้อม X ใหญ่บนเส้น "สุ่มปนทุกชิ้น" และเช็ค "จดเงื่อนไข:
แสง/ไมค์/ระยะ คงที่หรือไม่ — จดไว้พูด"

**Image-gen prompt:**
> Three rows labeled photos, recordings, scans, each showing three
> session boxes; in every row sessions 1-2 flow into a teal "train"
> tray and session 3 flows into a coral "test" tray; a large red X
> over an alternative path where all items are shuffled together
> randomly, captioned "leakage: same session on both sides"; a small
> checklist note "record conditions: light, mic, distance — mention
> them in the talk"; flat vector infographic style, white background,
> teal-coral-slate palette.

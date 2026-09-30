# explanation.md — Module M4: เสียง → ตัวเลข → โมเดล (ESC-50: MFCC + random forest)

สคริปต์ภาพประกอบสำหรับผู้สอน — แต่ละหัวข้อ = หนึ่งภาพ: แนวคิด (ไทย) → จุดประสงค์ → องค์ประกอบ → image-gen prompt (English)

---

## Figure 1 — เสียง → ตัวเลข → โมเดล (pipeline ของทั้งโมดูล)

**แนวคิด:** เสียงดิบไม่ใช่ตาราง — แต่พอแปลงเป็น MFCC feature ก็กลายเป็นตารางที่ random forest กินได้ทันที

**จุดประสงค์ของภาพ:** ให้ผู้เรียนเห็นภาพรวมของโมดูลก่อนลงโค้ด — ว่าเรากำลังต่อ "โลกเสียง" เข้ากับ "โลกตาราง" ที่คุ้นเคยจากคอร์ส DS

**องค์ประกอบภาพ:** ซ้ายสุดเป็นไอคอนลำโพงพร้อมคลื่นเสียง ลูกศรไปเครื่องบดป้าย "MFCC" ที่ปล่อยเวกเตอร์ 40 ช่อง → ลูกศร → ตาราง 2,000 แถว × 40 คอลัมน์ → ลูกศร → ป่าต้นไม้เล็ก ๆ ป้าย "Random Forest" → ออกทางขวาเป็นป้าย class "dog / siren / ..." — มีเส้นประแยกขวาบนไปกล่องหมอกป้าย "CNN บน Kaggle (ครึ่งหลังของโมดูล)"

**Image-gen prompt:**
> Educational pipeline diagram: a speaker icon with a sound wave on the left feeds a machine labeled "MFCC" that outputs a 40-cell feature vector strip; the strip fills one row of a large spreadsheet (2000 rows x 40 columns); the spreadsheet feeds a small forest of decision trees labeled "Random Forest" which outputs a classification label; a dashed arrow branches to a foggy box labeled "CNN on Kaggle - second half"; flat vector infographic style, white background, teal-coral-slate palette, clean sans-serif labels.

---

## Figure 2 — waveform vs spectrogram: เสียงเดียวกัน สองมุมมอง

**แนวคิด:** waveform บอก "ดังเมื่อไร" แต่ spectrogram บอก "ความถี่ไหนดังเมื่อไร" — ความถี่คือหัวใจของการจำแนกเสียง

**จุดประสงค์ของภาพ:** ให้ผู้เรียนเห็นว่าทำไมต้องแปลงเสียงก่อนให้โมเดลอ่าน

**องค์ประกอบภาพ:** ซ้าย: กราฟคลื่นไซน์ซับซ้อน (waveform) แกน x = เวลา, ขวา: ภาพ heatmap เดียวกันในมุมมอง spectrogram แกน x = เวลา แกน y = ความถี่ สีส้มร้อน = จุดดัง มีแถบแนวนอนสีสว่างแสดง "โทนยาว" และเส้นตั้งแสดง "เสียงกระแทก" — ลูกศรจากซ้ายไปขวาป้าย "หั่นเฟรม + FFT"

**Image-gen prompt:**
> Two-panel educational diagram of the same audio clip: left panel a raw waveform (oscillating line, x-axis time); right panel the same clip as a mel-spectrogram heatmap (x-axis time, y-axis frequency, warm bright colors = loud, horizontal bright bands labeled "sustained tone", vertical lines labeled "impact click"); an arrow between panels labeled "cut into frames + FFT"; flat vector style, white background, teal-coral palette, Thai-friendly minimal design.

---

## Figure 3 — MFCC: บีบ spectrogram เป็นลายนิ้วมือของเสียง

**แนวคิด:** MFCC = mel filterbank (ตามหูมนุษย์) + log + DCT — เหลือ ~20 ตัวเลขต่อเฟรมที่ "ฟัง" อยู่

**จุดประสงค์ของภาพ:** แยกขั้นตอน 4 ขั้นให้เห็นว่าข้อมูลถูกบีบทีละชั้นอย่างไร

**องค์ประกอบภาพ:** ซ้าย: spectrogram → เฟรมเดียวถูกดึงออกมา → ตัวกรองรูปโค้ง 26 อันเรียงซ้อนกว้างขึ้นตามความถี่ (ป้าย "mel filterbank") → log → แถบ 26 ค่า → กรรไกรป้าย "DCT" → แถบ 20 ค่า ป้าย "MFCC" — ขวาสุด: heatmap 20×216 ป้าย "คลิป 5 วินาที"

**Image-gen prompt:**
> Step-by-step MFCC diagram: a spectrogram on the left; one time frame pulled out; it passes through 26 curved triangular filter shapes stacked along the frequency axis (labeled "mel filterbank"), then a logarithm step, then a scissors labeled "DCT" compressing 26 values into the first 20 values of a strip labeled "MFCC"; at the far right a small heatmap 20x216 labeled "one 5-second clip"; flat vector infographic, white background, teal-coral-slate palette.

---

## Figure 4 — จากคลิปสู่ตาราง: mean + std = 40 ตัวเลข (สะพานจากคอร์ส DS)

**แนวคิด:** random forest กินแค่แถวตารางยาวเท่ากัน — สรุป MFCC ต่อ coefficient ด้วย mean และ std ตลอดเวลา

**จุดประสงค์ของภาพ:** ให้ผู้เรียนเชื่อมกลับไปที่ "ตาราง → โมเดล" ที่ทำคล่องแล้ว และเข้าใจว่าขั้นบีบนี้คือที่มาของเพดาน accuracy

**องค์ประกอบภาพ:** heatmap 20×216 → ลูกศรสองเส้นจากแต่ละแถวไปสองกล่อง "mean" และ "std" → แถบเวกเตอร์ 40 ช่อง → ตารางใหญ่ที่แถวแรกไฮไลต์ พร้อมป้าย label "dog" — มุมขวาล่างมีรูปสายฟ้าป้าย "ข้อมูล texture ละเอียดถูกทิ้งตรงนี้"

**Image-gen prompt:**
> Educational diagram: a 20x216 MFCC heatmap on the left; from each of its 20 rows two arrows go to boxes labeled "mean" and "std"; the results merge into a 40-cell feature vector strip; the strip becomes one highlighted row of a spreadsheet labeled "2000 clips x 40 features" with a class label tag "dog"; a small lightning icon in the corner labeled "fine texture discarded here"; flat vector style, white background, teal-coral palette.

---

## Figure 5 — 5-fold protocol และ data leakage จากไฟล์ต้นทาง

**แนวคิด:** คลิปหลายคลิปตัดมาจากไฟล์อัดเดียวกัน — fold ที่ชุดข้อมูลจัดมาให้กันคลิปญาติพี่น้องข้ามฝั่ง train/test

**จุดประสงค์ของภาพ:** สอนแนวคิด leakage ด้วยตัวอย่างเสียง แล้วเชื่อมกับงานเมโทรโลยี (เครื่อง/วันวัดเดียวกัน)

**องค์ประกอบภาพ:** ตาราง 5 แถว = fold 1–5 แต่ละ fold มีไอคอนไมโครโฟนกลุ่มเดียวกัน (คลิปจากไฟล์เดียวกัน) แถวหนึ่งถูกไฮไลต์สีส้ม = "test" ที่เหลือสีเขียว = "train" มีเครื่องหมายสกัดกั้นระหว่างกันป้าย "คลิปจากไฟล์เดียวกันห้ามข้ามฝั่ง" — ด้านล่างมีแถบวนลูกศร 5 รอบป้าย "วนครบ 5 folds แล้วเฉลี่ย"

**Image-gen prompt:**
> Cross-validation diagram: five horizontal rows labeled fold 1-5, each row contains small microphone icons of matching colors (clips from the same source file share a color); one row highlighted orange as "test", the rest green as "train", a barrier symbol between them labeled "same-source clips must not cross"; below, a circular arrow loop with five ticks labeled "rotate 5 folds, average"; flat vector infographic, white background, teal-coral-slate palette.

---

## Figure 6 — bake-off: RF (40 ตัวเลข) vs CNN (spectrogram เต็ม)

**แนวคิด:** วิธีเดิม (feature ที่คนออกแบบ + RF) เร็วและอธิบายได้ — CNN อ่านข้อมูลเต็มและแม่นกว่า แต่แลกด้วย GPU และความอธิบายได้

**จุดประสงค์ของภาพ:** ปิดโมดูลด้วยการตัดสินใจแบบวิศวกร ไม่ใช่ "deep learning คือคำตอบเสมอ"

**องค์ประกอบภาพ:** แผนภูมิข้อหมาบาร์ (bar chart) 3 แท่ง: "RF + MFCC ~45%" (สีเขียวมิ้นต์), "CNN baseline ~64%" (สีส้มคอรัล), "คนจริง 81%" (สีเทา) — ใต้แต่ละแท่งมีไอคอนต้นทุน: CPU / GPU / หูคน — ส่วนบนมีป้าย "ข้อมูลเดียวกัน, fold เดียวกัน, เทียบตรง ๆ"

**Image-gen prompt:**
> Horizontal bar chart educational graphic titled "same data, fair comparison": three bars labeled "RF + MFCC ~45%" (mint green, small CPU icon), "CNN on spectrogram ~64%" (coral orange, small GPU icon), "human accuracy 81%" (slate gray, ear icon); a banner at top reading "same dataset, same test fold"; flat vector infographic style, white background, clean sans-serif labels, teal-coral-slate palette.

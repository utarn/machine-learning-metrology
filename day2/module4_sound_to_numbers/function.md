# Function Reference — Module M4: เสียง → ตัวเลข → โมเดล (ESC-50: MFCC + random forest)

Only functions introduced for the first time in this module are listed here, in the order you will meet them. Functions from earlier v2 modules (`train_test_split`, `ConfusionMatrixDisplay.from_predictions` — M0's `function.md`; `TensorDataset`/`DataLoader`, `nn.Conv2d` — M1's `function.md`) are not repeated. `RandomForestClassifier` is listed here because the v2 course has not met it before — it is the bridge back to your 2-day DS course.

## 1. `librosa.load(path, sr=22050, mono=True)` — librosa

What it does: Loads an audio file and returns `(y, sr)` — `y` is the waveform as a 1-D numpy array of numbers (amplitude per sample), `sr` is the sampling rate. `sr=22050` resamples on the fly (ESC-50 originals are 44,100 Hz — half the resolution is plenty for classification and 2x faster), `mono=True` mixes channels to one.
Example: `y, sr = librosa.load("1-100032-A-0.wav", sr=22050, mono=True)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "librosa — load(path, sr=22050, mono=True)"
Center: a wav-file icon feeding a machine labeled "resample 44.1kHz -> 22.05kHz + mix to mono"; the machine outputs a long horizontal number strip labeled "y: ~110,250 numbers" with a small tag "sr: 22050"; a speedometer icon on the machine labeled "2x faster".
Caption strip at the bottom: "a sound file becomes one long row of numbers."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 2. `librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)` — librosa

What it does: Computes Mel-Frequency Cepstral Coefficients — for every short frame (~23 ms) it folds the spectrum onto the mel scale (matching human hearing), takes the log, and compresses with a DCT into `n_mfcc` coefficients. Returns a `(n_mfcc, n_frames)` matrix: a 5-second clip at sr=22050 gives 20 x ~216.
Example: `m = librosa.feature.mfcc(y=y, sr=22050, n_mfcc=20)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "librosa — feature.mfcc(y, sr, n_mfcc=20)"
Center: a wide spectrogram panel cut into thin vertical slices (frames); each slice passes through curved triangular filter shapes labeled "mel", then a log step, then a compressor labeled "DCT"; out comes a small heatmap 20 rows by many columns labeled "(20, 216)".
Caption strip at the bottom: "110,250 raw numbers -> a 20 x 216 fingerprint table."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 3. `librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)` + `librosa.power_to_db(S, ref=np.max)` — librosa

What it does: Builds a mel spectrogram — the full "image" of the sound before the MFCC compression step: `(n_mels, n_frames)` = 128 x 216 for a 5-second clip. `power_to_db` converts power to decibels (log scale, relative to the loudest value), which is what both your eyes in the plot and the CNN in module4_esc50_cnn actually consume.
Example: `S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)` then `img = librosa.power_to_db(S, ref=np.max)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "librosa — melspectrogram + power_to_db"
Center: a waveform entering a machine labeled "STFT + 128 mel filters" that outputs a heatmap "image" of the sound (time x frequency, warm bright colors = loud); a small dial on the output labeled "decibels (log scale)".
Caption strip at the bottom: "the full picture of a sound — this is what the CNN will read."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 4. `librosa.feature.delta(m, axis=1)` — librosa (ใช้ใน exercise)

What it does: Computes the local time-derivative of each MFCC coefficient — how fast each value is rising or falling between neighbouring frames. `axis=1` is the time axis. Adding mean+std of the delta doubles the feature table and captures "movement" (a rising chirp vs a steady tone) that plain mean/std miss.
Example: `d = librosa.feature.delta(m, axis=1)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "librosa — feature.delta(m, axis=1)"
Center: one MFCC row shown as a wavy line over time; below it a second line labeled "delta" showing positive bumps where the first line rises and negative bumps where it falls; an arrow between them labeled "slope between frames".
Caption strip at the bottom: "mean+std says 'where the sound sits' — delta says 'where it is moving'."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 5. `Parallel(n_jobs=-1)(delayed(fn)(x) for x in xs)` — joblib

What it does: Runs `fn` over every item using all CPU cores in parallel (n_jobs=-1 = all cores). We use it to extract features from 2,000 clips — each clip is independent, so this is an embarrassingly parallel loop that turns minutes into seconds.
Example: `X = np.asarray(Parallel(n_jobs=-1)(delayed(mfcc_row)(p) for p in paths))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "joblib — Parallel(n_jobs=-1) + delayed(fn)"
Center: a long queue of 2000 small wav-file icons on the left splitting into 8 parallel conveyor lanes, each lane running the same small machine labeled "mfcc_row", all lanes merging on the right into one stack of 2000 feature-vector strips labeled "X (2000, 40)".
Caption strip at the bottom: "every clip is independent — feed all cores at once."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 6. `RandomForestClassifier(n_estimators=200, n_jobs=-1, random_state=SEED)` — sklearn.ensemble

What it does: Trains a random forest — hundreds of decision trees, each fit on a random subset of rows and features, voting together at prediction time. `n_estimators` is the tree count (more trees = more stable but slower, diminishing returns around a few hundred), `n_jobs=-1` parallelizes across cores, `random_state` fixes the seed so your run is reproducible.
Example: `rf = RandomForestClassifier(n_estimators=200, n_jobs=-1, random_state=42).fit(X_train, y_train)` then `pred = rf.predict(X_test)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — RandomForestClassifier(n_estimators=200)"
Center: one feature-table row entering a grove of many small decision trees, each tree slightly different (some fed with highlighted columns, some with highlighted rows — random subsets); every tree holds a small vote card; a ballot box labeled "majority vote" outputs the predicted class.
Caption strip at the bottom: "many imperfect trees voting together beat one perfect-looking tree."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 7. `Counter(pairs).most_common(k)` — collections (standard library)

What it does: Counts how often each item occurs in a list, then `.most_common(k)` returns the k most frequent items as `(item, count)` pairs. We use it on `(true_class, predicted_class)` pairs of the wrong predictions to rank confusion pairs — a quicker read than the full 50x50 confusion matrix.
Example: `Counter((t, p) for t, p in zip(y_true, y_pred) if t != p).most_common(8)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "collections — Counter(...).most_common(8)"
Center: a pile of mismatched label tags (each tag shows two class names, e.g. "breathing -> keyboard_typing") dropping into a counting machine; the machine outputs a ranked list board with the top 8 tag pairs and tally marks next to each.
Caption strip at the bottom: "tally the mistakes, read the most common pairs first."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

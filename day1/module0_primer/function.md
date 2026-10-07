# Function Reference — Module M0: Primer — จากข้อมูลสู่โมเดล

Only functions introduced for the first time in this module are listed here, in the order you will meet them. Functions already covered in the Data Science course are not repeated.

## 1. `train_test_split(*arrays, test_size, random_state)` — sklearn.model_selection

What it does: Randomly splits arrays into train and test parts (same row order preserved across all arrays passed).
Example: `x_tr, x_te, y_tr, y_te = train_test_split(x, y, test_size=0.33, random_state=42)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — train_test_split(x, y, test_size, random_state)"
Center: one large diagram illustrating a long strip of data points on the left being shuffled and dealt into two smaller strips on the right — a wider teal strip labeled "train" and a narrower coral strip labeled "test", with a padlock icon labeled "random_state=42" to show the split is repeatable.
Caption strip at the bottom: "train_test_split() deals rows into a training pile and an untouched test pile."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 2. `make_pipeline(*steps)` — sklearn.pipeline

What it does: Chains preprocessing steps and an estimator into one object that fits/predicts as a unit.
Example: `make_pipeline(PolynomialFeatures(degree=3), LinearRegression()).fit(x_tr[:, None], y_tr)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — make_pipeline(...)"
Center: one large diagram illustrating raw data cubes entering a horizontal factory pipe with two stations bolted together — the first station labeled "PolynomialFeatures" expanding each cube into a stack of derived cubes, the second station labeled "LinearRegression" stamping a prediction tag — data flows left to right through both stations in one continuous pipe.
Caption strip at the bottom: "make_pipeline() chains preprocessing + model so they act as one object."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 3. `mean_squared_error(y_true, y_pred)` — sklearn.metrics

What it does: Average of squared differences between true and predicted values (lower = better).
Example: `mean_squared_error(y_te, model.predict(x_te[:, None]))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — mean_squared_error(y_true, y_pred)"
Center: one large diagram illustrating a scatter of blue dots (true values) each with a short vertical coral dashed line down to the model curve, each gap drawn as a small square with a "squared" badge, arrows from all squares into a gauge labeled "MSE — lower is better".
Caption strip at the bottom: "mean_squared_error() averages the squared gaps between truth and prediction."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 4. `ConfusionMatrixDisplay.from_predictions(y_true, y_pred)` — sklearn.metrics

What it does: Draws the confusion matrix: rows = true class, columns = predicted class, diagonal = correct.
Example: `ConfusionMatrixDisplay.from_predictions(yb_te, pred, colorbar=False)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — ConfusionMatrixDisplay.from_predictions()"
Center: one large diagram illustrating a 2x2 grid table with axes labeled "actual" (rows) and "predicted" (columns); diagonal cells filled green with checkmarks, off-diagonal cells filled orange with warning icons; a magnifier hovers over one orange cell labeled "where does the model fail?"
Caption strip at the bottom: "from_predictions() shows not just how much the model got wrong, but in which direction."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 5. `word_tokenize(text, engine)` — pythainlp.tokenize

What it does: Cuts a Thai string into word tokens (Thai has no spaces between words).
Example: `word_tokenize("การสอบเทียบเครื่องมือวัด", engine="newmm")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "pythainlp — word_tokenize(text, engine='newmm')"
Center: one large diagram illustrating a single continuous ribbon of Thai text flowing left, then scissors (a small tokenization blade) cutting it into separated rounded token boxes that line up with gaps on the right, each box getting a small number tag — no spaces existed before, the blade decides the word boundaries.
Caption strip at the bottom: "word_tokenize() cuts Thai text (which has no spaces) into word units."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 6. `np.fft.rfft(signal)` / `np.fft.rfftfreq(n, d)` — numpy

What it does: Real fast Fourier transform — turns a time series into energy per frequency; `rfftfreq` gives the matching frequency axis.
Example: `spec = np.abs(np.fft.rfft(sig)); freqs = np.fft.rfftfreq(len(t), 1.0 / fs)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.fft.rfft(signal)"
Center: one large diagram illustrating a wiggly time-series line on the left (x-axis "time") passing through a prism-like triangle labeled "FFT", and emerging on the right as a spectrum chart (x-axis "frequency") with two sharp peaks standing up at 50 and 120 Hz.
Caption strip at the bottom: "rfft() re-expresses a signal from energy-over-time to energy-per-frequency."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

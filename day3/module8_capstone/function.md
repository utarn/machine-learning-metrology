# Function Reference — Module M8: Capstone (3 tracks + rubric)

Only functions introduced for the first time in this module are listed here, in the order you will meet them. Functions reused from earlier modules (`easyocr.Reader.readtext(detail=0)`, `librosa.feature.mfcc`, `RandomForestClassifier`, `anomalib` Folder/Patchcore/Engine, `ConfusionMatrixDisplay`, `roc_auc_score`) are not repeated — see each module's `function.md`.

## 1. `.readtext(image, detail=1, paragraph=False)` — easyocr.Reader

What it does: Same OCR as M2 but returns one `(bbox_4points, text, confidence)` tuple per detected box — the positions let us rebuild table structure (which column / which row each token belongs to), which `detail=0` throws away.
Example: `for bb, txt, _conf in reader.readtext(np.array(img), detail=1, paragraph=False):`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "easyocr — readtext(image, detail=1)"
Center: one large diagram illustrating a scanned page on the left with a few table cells highlighted by dashed rectangles, and on the right the same cells shown as small result cards each carrying three badges — a tiny 4-corner frame icon labeled "bbox", the text content, and a small confidence number.
Caption strip at the bottom: "detail=1 keeps where each token sits, not just what it says."
```

## 2. `re.sub(pattern, repl, string)` — re (standard library)

What it does: Replaces every substring matching a regex; the starter uses it to strip everything except digits, dot, and signs from OCR tokens before parsing (`[^0-9.+\-]` → `""`), which is how stray Thai glyphs and spaces fall away.
Example: `s = re.sub(r"[^0-9.+\-]", "", txt)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "re — re.sub(pattern, repl, string)"
Center: one large diagram illustrating a conveyor belt of OCR token cards (mixed: "+ o.05", "4o.00", "ห้องปฏิบัติการ") passing a filter gate labeled "[^0-9.+\\-] -> ''"; numeric-looking cards come out cleaned on the right while letters and Thai glyphs fall through into a discard bin.
Caption strip at the bottom: "sub() washes a token down to the characters a number needs."
```

## 3. `pd.to_numeric(x, errors="coerce")` — pandas

What it does: Converts a column (or a whole DataFrame via `.apply`) to numbers; anything unparseable becomes NaN instead of raising — exactly what we want for the cells OCR failed to read.
Example: `df3 = pd.DataFrame(table, columns=cols).apply(pd.to_numeric, errors="coerce")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "pandas — pd.to_numeric(x, errors='coerce')"
Center: one large diagram illustrating a column of mixed cells — most cells show numbers in teal as they pass a conversion funnel, one cell shows unreadable text turning into a soft gray "NaN" cell at the bottom instead of breaking the funnel.
Caption strip at the bottom: "coerce turns unreadable cells into NaN, so the table still builds."
```

## 4. `DataFrame.mean(axis=1)` / `Series.std(ddof=1)` — pandas

What it does: Row-wise statistics across selected columns (here: the three repeated readings per calibration point); `ddof=1` is the sample standard deviation (divide by n-1) — the same definition the report's own summary column uses, which is what makes the internal-consistency check meaningful.
Example: `df6["เฉลี่ย (คำนวณ)"] = reads.mean(axis=1)` then `reads.std(axis=1, ddof=1)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "pandas — mean(axis=1) and std(ddof=1)"
Center: one large diagram illustrating one table row with three reading cells flowing sideways (an arrow labeled "axis=1") into two badges — a rounded "mean" badge averaging the three, and a spread "std" badge drawn as a small error bar; a tiny footnote chip reads "ddof=1: divide by n-1".
Caption strip at the bottom: "row-wise stats turn repeated readings into one summary per point."
```

## 5. `LogisticRegression(max_iter=1000).fit(X, y)` — sklearn.linear_model

What it does: Trains a linear classifier on the extracted 576-dim MobileNetV3 features for the labeled two-class task (Track A, method 2) — the "head" of transfer learning, here using the classic tabular tool from the DS course instead of a torch head.
Example: `clf = LogisticRegression(max_iter=1000).fit(X_all[tr], y_all[tr])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — LogisticRegression(max_iter=1000)"
Center: one large diagram illustrating a scatter of two point clouds (normal teal, defect coral) in a high-dimensional space simplified to 2D, with a single straight decision boundary line separating them; arrows from the points to the line during training; a small chip labeled "head on frozen features".
Caption strip at the bottom: "a linear boundary on good features is often all the head needs."
```

## 6. `librosa.feature.zero_crossing_rate(y)` / `.rms(y=y)` / `.spectral_centroid(y=y, sr=sr)` — librosa

What it does: Three hand-designed audio features beyond MFCC — how often the signal flips sign (noisiness), its energy envelope (loudness), and its brightness (dominant-frequency center); Track B appends their mean/std as 6 extra columns before re-training the RF.
Example: `zcr = librosa.feature.zero_crossing_rate(y)` then `[zcr.mean(), zcr.std()]`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "librosa — zero_crossing_rate / rms / spectral_centroid"
Center: one large diagram illustrating the same short waveform shown three times side by side; first copy marked with small dots at every zero crossing labeled "noisiness"; second copy with a filled area under its curve labeled "energy"; third copy overlaid on a frequency spectrum with a pivot point at the balance center labeled "brightness"; each ending in a small (mean, std) output chip.
Caption strip at the bottom: "three physically meaningful numbers you can explain in the talk."
```

## 7. `NearestNeighbors(n_neighbors=k).fit(F).kneighbors(F2)` — sklearn.neighbors

What it does: Finds the k closest training vectors for each query vector and their distances; Track B's mini anomaly detector fits it on "normal" MFCC vectors only and uses the mean neighbor distance as an anomaly score — the PatchCore idea (M6) in pure tabular form.
Example: `nn = NearestNeighbors(n_neighbors=3).fit(X[y_cat == "engine"])` then `d, _ = nn.kneighbors(F)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — NearestNeighbors(n_neighbors=3).kneighbors()"
Center: one large diagram illustrating a teal cluster of normal-feature dots with a faint blue circle around each of its 3-neighbor links; two query points outside — one teal point close to the cluster with a short distance arrow and a low score badge, one coral point far away with a long arrow and a high score badge labeled "anomaly".
Caption strip at the bottom: "distance to the k nearest normal points is the anomaly score."
```

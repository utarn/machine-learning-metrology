# Function Reference — Module M3: สอนโมเดลอ่านใจจากข้อความไทย (fine-tune mBERT)

Only functions introduced for the first time in this module are listed here, in the order you will meet them. Functions from earlier modules (`word_tokenize` and `train_test_split` — M0's `function.md`) are not repeated.
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)

## 1. `AutoTokenizer.from_pretrained(checkpoint)` + `tokenizer(texts, truncation, max_length, padding, return_tensors)` — transformers

What it does: Loads the tokenizer that matches a checkpoint (for mBERT: wordpiece, ~119k pieces over 104 languages). Calling it converts text to `input_ids`/`attention_mask` tensors; `truncation=True, max_length=64` cuts long texts, `padding=True` equalizes lengths in a batch.
Example: `enc = tokenizer(texts, truncation=True, max_length=64, return_tensors="pt")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "transformers — AutoTokenizer.from_pretrained(checkpoint)"
Center: one large diagram showing Thai chat bubbles entering a funnel-shaped machine labeled "wordpiece tokenizer"; the machine outputs rows of small numbered tiles (input ids) of different lengths, then a padding step aligns all rows to the same length with pale gray filler tiles, cut off after tile 64 with a small scissors icon labeled "truncation".
Caption strip at the bottom: "same tokenizer as the checkpoint — text becomes equal-length rows of token ids."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 2. `load_dataset(repo_id)` + `.features`, `.select`, `.rename_column`, `.map` — datasets

What it does: Downloads a dataset from the Hugging Face hub into a DatasetDict of splits. `.features["col"].names` gives class-label names; `.select(indices)` picks rows (our stratified subset); `.rename_column` renames a column; `.map(fn, batched=True)` applies a function to every batch (we use it to tokenize).
Example: `ds = load_dataset("pythainlp/wisesight_sentiment")` then `tok = d.rename_column("category", "labels").map(tokenize, batched=True)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "datasets — load_dataset(repo_id), select, rename_column, map"
Center: one large diagram showing a cloud with a small parquet-file icon downloading into three labeled trays "train / validation / test"; from the train tray, a highlighted subset of cards is lifted out (label "select — stratified subset"), a name tag on the cards is swapped (label "rename_column: category -> labels"), and the cards pass through a small machine stamping token tiles on each (label "map(tokenize)").
Caption strip at the bottom: "load once from the hub, then reshape with select / rename_column / map."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 3. `AutoModelForSequenceClassification.from_pretrained(checkpoint, num_labels, id2label, label2id)` — transformers

What it does: Downloads a pretrained model and attaches a fresh classification head with `num_labels` outputs. The head starts random — that is why loss starts high. `id2label`/`label2id` name the outputs so saved predictions are readable.
Example: `model = AutoModelForSequenceClassification.from_pretrained(CHECKPOINT, num_labels=4, id2label=id2label, label2id=label2id)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "transformers — AutoModelForSequenceClassification.from_pretrained"
Center: one large diagram showing a cloud downloading a large multi-layer block labeled "mBERT (pre-trained)" and a construction crane attaching a small unfinished box on top labeled "new head: 4 outputs (random init)" with four output slots colored teal, slate, coral, gray; a tiny dice icon near the head labeled "starts random".
Caption strip at the bottom: "pretrained brain + fresh random head — training will tune both."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 4. `TrainingArguments(...)`, `Trainer(...)`, `.train()`, `.state.log_history`, `.predict()` — transformers

What it does: `TrainingArguments` holds the training recipe (learning rate, batch size, epochs, `eval_strategy="epoch"` for per-epoch evaluation, `fp16` for GPU speed, `report_to="none"` to disable external logging). `Trainer` bundles model + args + datasets + `compute_metrics` and runs the loop with `.train()`; `.state.log_history` records the loss/metrics per epoch; `.predict(dataset)` runs the trained model over a whole split.
Example: `trainer = Trainer(model, args, train_dataset=..., eval_dataset={...}, data_collator=..., processing_class=tokenizer, compute_metrics=compute_metrics)` then `trainer.train()` and `pred_out = trainer.predict(tok["test"])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "transformers — TrainingArguments + Trainer"
Center: one large diagram of a conveyor-belt training loop: batches of token-tile rows enter a machine labeled "Trainer.train()", above the belt a dashboard card lists settings "lr 2e-5 / batch 32 / epochs 3 / fp16"; at the end of each belt lap a gauge labeled "eval at epoch" records a small notebook icon labeled "log_history"; an exit chute labeled ".predict(test)" releases a tray of predictions.
Caption strip at the bottom: "one object holds the recipe, one object runs the loop, log_history keeps the numbers."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 5. `compute_metrics(eval_pred)` — your own function

What it does: Receives an `EvalPrediction` (logits + labels), converts logits to class ids with `argmax`, and returns a dict of metrics — Trainer calls it after every evaluation and prefixes the keys with the dataset name (e.g. `eval_val_accuracy`).
Example: `return {"accuracy": float((preds == labels).mean())}`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "compute_metrics(eval_pred) — your own scoring function"
Center: one large diagram showing two trays entering a small stamping machine — left tray holds rows of raw score bars (logits) with the tallest bar highlighted per row (label "argmax"), right tray holds the correct answer tags (labels); the machine stamps out a single card labeled "accuracy: 0.xx".
Caption strip at the bottom: "logits -> argmax -> compare with labels — return one dictionary."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 6. `precision_recall_fscore_support(y_true, y_pred, labels)` — sklearn.metrics

What it does: Computes precision, recall, F1 and support for every class in one call — returns four arrays, one entry per class. We use the precision and recall arrays for the per-class bar chart. (precision/recall as concepts first met in M0; this per-class variant is new here.)
Example: `prec, rec, _, _ = precision_recall_fscore_support(y_true, y_pred, labels=range(len(LABELS)))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — precision_recall_fscore_support(y_true, y_pred)"
Center: one large diagram showing a table with four class rows (pos, neu, neg, q); two columns fan out of the table as separate strips — a teal strip labeled "precision per class" and a coral strip labeled "recall per class", each strip divided into four segments with numbers; small tags under the strips labeled "one array per metric".
Caption strip at the bottom: "one call returns four arrays — one number per class, ready for plotting."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 7. `NearestNeighbors(n_neighbors=k).fit(E)` + `.kneighbors(q)` — sklearn.neighbors

What it does: Indexes a matrix of embedding vectors (one row per text); `kneighbors` returns the distance and index of the k closest rows to a query vector. Combined with model embeddings, this is search-by-meaning without any extra training.
Example: `nn = NearestNeighbors(n_neighbors=6).fit(E)` then `dist, nbr_idx = nn.kneighbors(E[[q_pos]])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — NearestNeighbors(n_neighbors=k).fit(E)"
Center: one large diagram showing a scatter of small dots organized in soft color clusters; a black star query point with a dashed circle around it; thin lines from the star to the five nearest dots, each line tagged with a distance number; a small index card beside the plot labeled "dist, nbr_idx".
Caption strip at the bottom: "fit an index over embeddings, then kneighbors finds the most similar texts."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 8. `set_seed(SEED)` — transformers

What it does: Seeds Python, NumPy and torch RNGs in one call so dropout, shuffling and head initialization repeat across runs.
Example: `transformers.set_seed(42)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "transformers — set_seed(SEED)"
Center: one large diagram showing a single key labeled "seed = 42" inserted into three small locks in a row labeled "python", "numpy", "torch"; all three locks open in unison and a path of identical dice faces extends from them.
Caption strip at the bottom: "one seed key rewinds every random source the same way."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

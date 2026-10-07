# Function Reference — Module M6: PatchCore anomaly detection

Only functions introduced for the first time in this module are listed here, in the order you will meet them. Functions from earlier modules (e.g. M0's `repo_root()` pattern, M1's `accuracy_score`, `plt` conventions) are not repeated.

## 1. `Folder(name, root, normal_dir, abnormal_dir, val_split_mode, val_split_ratio, num_workers, seed)` — anomalib.data

What it does: Builds a data module that reads images from plain folders: `normal_dir` images are used for training (PatchCore trains on normal images only), `abnormal_dir` images go to the test split only. `val_split_mode="from_test"` carves a validation slice out of the test set (anomalib needs one for its internal threshold metrics); `num_workers=0` avoids spawn-worker crashes in notebooks on macOS/Windows.
Example: `dm = Folder(name="m6_sample", root=str(SAMPLE_DIR), normal_dir="good", abnormal_dir="defect", val_split_mode="from_test", val_split_ratio=0.3, num_workers=0, seed=42)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "anomalib.data — Folder"
Center: one large diagram showing two photo folders labeled "good" and "defect"; arrows from the "good" folder split into a large tray labeled "train (normal only)" and a small tray labeled "validation"; arrows from the "defect" folder go only into a tray labeled "test"; a small padlock icon sits on the arrow into train from the defect side with a cross over it, labeled "defect images never used for training".
Caption strip at the bottom: "point Folder at plain image folders — normal trains, abnormal only tests."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 2. `Patchcore(layers, num_neighbors, coreset_sampling_ratio, post_processor, visualizer)` — anomalib.models

What it does: Creates a PatchCore model: a frozen ImageNet WideResNet-50-2 backbone (`layers=("layer2","layer3")` = mid-level spatial features), a memory bank built from normal-image patch features reduced by coreset subsampling (`coreset_sampling_ratio`, default 0.1), and kNN scoring per patch (`num_neighbors`). `post_processor=False` gives RAW scores (kNN distances) instead of threshold-normalized 0/1 values; `visualizer=False` stops anomalib from writing its own heatmap files.
Example: `model = Patchcore(layers=("layer2","layer3"), num_neighbors=3, post_processor=False, visualizer=False)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "anomalib.models — Patchcore"
Center: one large diagram of three stages connected by arrows: (1) a metal plate photo entering a frozen ice-covered CNN tower labeled "WideResNet-50 (frozen)", with small colored tiles streaming out of two mid floors labeled "layer2 / layer3"; (2) a large drawer labeled "memory bank" with a funnel labeled "coreset x0.1" compressing thousands of tiles into a few representative ones; (3) a new plate photo whose tiles are compared with ruler arrows to the nearest bank tile, the farthest tile highlighted in coral.
Caption strip at the bottom: "features from frozen ImageNet layers, compressed normal-patch memory, kNN distance = anomaly score."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 3. `Engine(accelerator, max_epochs, logger, default_root_dir, enable_progress_bar).fit(model, datamodule)` — anomalib.engine

What it does: Drives training/prediction (wraps PyTorch Lightning). For PatchCore, `fit` is NOT gradient training: it runs the frozen backbone over the normal images, collects patch features into the memory bank, then runs coreset selection — one epoch is enough and it finishes in seconds on CPU. `accelerator="cpu"` matches the offline student machines; `logger=False` and `enable_progress_bar=False` keep notebook output clean; `default_root_dir` points checkpoint output at the gitignored `data/` folder. Important: create a NEW Engine for each refit — a used Engine will not populate a new model instance's memory bank.
Example: `engine = Engine(accelerator="cpu", max_epochs=1, logger=False, default_root_dir=str(RUN_DIR), enable_progress_bar=False)` then `engine.fit(model=model, datamodule=dm)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "anomalib.engine — Engine.fit"
Center: one large diagram contrasting two panels: left panel labeled "what fit does NOT do" showing a staircase labeled "gradient descent" with a big red cross and a flat loss curve; right panel labeled "what fit DOES" showing a pipeline: photos on a conveyor belt pass a scanning camera (labeled "extract features"), tiles drop into a large cabinet (labeled "memory bank"), then a small robot sorts and keeps only a few tiles (labeled "coreset selection"); a stopwatch icon labeled "seconds on CPU".
Caption strip at the bottom: "PatchCore fit builds a memory bank — no gradients, one pass."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 4. `model.pre_processor` + `model(batch)` — anomalib (direct inference)

What it does: Every anomalib model carries a `pre_processor` module (resize to 256×256 + ImageNet normalization). Calling the model directly on a stacked batch of pre-processed tensors (after `model.eval()` and inside `torch.no_grad()`) returns an `InferenceBatch` with `pred_score` (one number per image = max patch distance) and `anomaly_map` (256×256 distance map per image) — works on ANY image path, no datamodule needed, which is how the notebook scores the learner's own photos.
Example: `out = model(torch.stack([prep(p) for p in paths]))` then `out.pred_score`, `out.anomaly_map`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "anomalib — model(batch) direct inference"
Center: one large diagram showing arbitrary photos (a phone camera snapshot, a scanned report, a synthetic plate) each passing through a small funnel labeled "pre_processor resize+normalize", stacking into a single transparent 3D slab labeled "batch", then flowing into a dark machine labeled "PatchCore eval" that outputs two things: a gauge labeled "pred_score" per photo and a translucent heat overlay on each photo labeled "anomaly_map".
Caption strip at the bottom: "score any image path — no dataloader required."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 5. `to_image(img)` + `to_dtype(tensor, dtype, scale=True)` — torchvision.transforms.v2.functional

What it does: Converts a PIL image to a torchvision image tensor (uint8, CHW), then rescales it to float32 in [0, 1] — the input format `model.pre_processor` expects before it resizes and normalizes.
Example: `x = model.pre_processor(to_dtype(to_image(Image.open(p).convert("RGB")), torch.float32, scale=True))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "torchvision transforms.v2.functional — to_image, to_dtype"
Center: one large diagram showing a photo file icon becoming a pixel grid (labeled "to_image — uint8, CHW"), then a dial labeled "÷255" turning the grid into translucent floating-point tiles (labeled "to_dtype — float32 in [0,1]"), then an arrow into a small funnel labeled "pre_processor".
Caption strip at the bottom: "PIL image -> uint8 tensor -> float [0,1] -> ready for the model's pre-processor."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 6. `roc_auc_score(y_true, y_score)` — sklearn.metrics

What it does: Computes ROC AUC from ground-truth labels (0/1) and raw anomaly scores — the standard "how well do scores separate normal from defective" number for one-class detectors, independent of any threshold choice.
Example: `auc = roc_auc_score([0]*20 + [1]*8, np.concatenate([s_good, s_def]))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.metrics — roc_auc_score"
Center: one large diagram showing two overlapping score histograms (low teal heap labeled "normal", high coral heap labeled "defective") above a slider labeled "threshold"; to the right an ROC curve square with a teal curve hugging the top-left corner and a big stamp labeled "AUC = area under this curve — threshold-free".
Caption strip at the bottom: "one number for how well raw scores separate the two groups, before any threshold."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 7. `np.percentile(a, q)` — numpy

What it does: Returns the q-th percentile of an array — used to set the anomaly threshold from the distribution of normal-image scores (e.g. p95 keeps 95% of normal images below the alarm line by design).
Example: `THRESHOLD = float(np.percentile(s_good, 95))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — percentile(a, q)"
Center: one large diagram of a single teal histogram of normal-image scores with vertical dashed lines at 50%, 80%, 95% and 99% positions, each line tagged "q"; a coral zone above the 95% line labeled "alarm zone (5% of normals by design)"; a small gauge icon labeled "choose q from the cost of false alarms vs missed defects".
Caption strip at the bottom: "the alarm line is a business decision — percentile turns it into a knob."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 8. `ImageDraw.Draw(img).line(...)` / `.ellipse(...)` — PIL (Pillow)

What it does: Draws shapes onto a PIL image — used here to synthesize the defect samples (scratch = `line` with a dark color and width; pit/burn/rust = `ellipse` fills) so the notebook runs offline without any dataset download.
Example: `d = ImageDraw.Draw(img)` then `d.line([(x0, 45), (x0 + 18, 210)], fill=(10, 8, 6), width=9)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "PIL — ImageDraw.line, ellipse"
Center: one large diagram showing a brushed-metal plate thumbnail; a virtual pen tool draws a dark diagonal scratch (labeled "line fill, width"), then a stamp tool adds a bright circular pit with a dark core (labeled "ellipse fill"), a burn blotch and a speckled rust patch; small tags "synthetic defect: scratch / pit / burn / rust".
Caption strip at the bottom: "draw your own ground-truth defects — offline, reproducible, no dataset needed."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

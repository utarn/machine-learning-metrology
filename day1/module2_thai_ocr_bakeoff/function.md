# Function Reference — Module M2: Thai OCR: ข้อมูลทดสอบ → CER

Only functions introduced for the first time in this module are listed here, in the order you will meet them. Functions from earlier modules are not repeated — see M0/M1's `function.md`.

## 1. `jiwer.cer(reference, hypothesis)` — jiwer

What it does: Character Error Rate — minimum character edits (substitute/delete/insert) divided by the length of the reference. Accepts one string each, or lists of strings (errors pooled across all pairs).
Example: `jiwer.cer("อุณหภูมิ 24.6", "อุณหภูมิ 24.5")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "jiwer — cer(reference, hypothesis)"
Center: two horizontal strips of Thai characters stacked one above the other; a red dashed line connects three mismatched character pairs with a small scissors icon (substitute), a deleted gap marker, and an inserted gap marker; below, a fraction badge reads "edits over reference length" with the value "CER = 0.10".
Caption strip at the bottom: "cer() counts the fewest character edits needed to fix the guess."
```

## 2. `pytesseract.image_to_string(image, lang, config)` — pytesseract

What it does: Runs the system Tesseract binary on an image and returns plain text. `lang` picks traineddata (e.g. `tha`, `tha+eng`); `config` passes engine options — here `--tessdata-dir` pointing at the traineddata shipped in the repo. Pass a file path (not a PIL image): recent tesseract/leptonica builds can fail reading images piped through stdin.
Example: `pytesseract.image_to_string(str(path), lang="tha", config=f"--tessdata-dir {TESSDATA}")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "pytesseract — image_to_string(image, lang, config)"
Center: a small Thai document image on the left feeds a gearbox-like machine labeled "Tesseract engine"; a pipe labeled "lang='tha'" carries a language plug shaped like a Thai character into the machine; a settings dial labeled "--tessdata-dir" points to a small folder icon; the machine outputs a text strip with Thai characters.
Caption strip at the bottom: "a system engine you steer with language files and options."
```

## 3. `easyocr.Reader(lang_list, gpu=False)` and `.readtext(image, detail=0)` — easyocr

What it does: `Reader` loads detection + recognition models for the chosen languages (downloaded once into `~/.EasyOCR` on first use). `readtext` returns the recognized text strings (with `detail=0`) for every detected text region.
Example: `reader = easyocr.Reader(["th", "en"], gpu=False)`; `reader.readtext(np.array(img), detail=0)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "easyocr — Reader(['th','en']) then readtext(image)"
Center: a scene photo and a document thumbnail both feed a two-stage machine: stage one stamps small rectangles around text regions (detection), stage two reads each rectangle (recognition) and hands out small text tags; a plug board labeled "th" and "en" supplies two language modules into the machine's side.
Caption strip at the bottom: "Reader finds the words and reads them in one call."
```

## 4. `TrOCRProcessor.from_pretrained(...)` / `VisionEncoderDecoderModel.from_pretrained(...)` / `.generate(pixel_values)` — transformers

What it does: Loads the thai-trocr line-OCR model: the processor resizes the image to model input; `generate` decodes the text token by token. Line-level model — feed it one text line at a time. `local_files_only=True` first keeps pre-bundled machines offline.
Example: `pv = processor(images=img, return_tensors="pt").pixel_values`; `ids = trocr.generate(pv, max_new_tokens=64)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "transformers — thai-trocr: processor then generate"
Center: one Thai text-line image enters a funnel labeled "processor (resize + normalize)" becoming a compact grid of numbers, which enters a tall transformer tower with an eye icon (vision encoder) on top and a pen icon (decoder) writing Thai characters out token by token; a small padlock badge reads "local_files_only=True keeps it offline".
Caption strip at the bottom: "one line in, Thai text out, token by token."
```

## 5. `LayoutPredictor()([image])` and `TableRecPredictor()([image])` — surya

What it does: Layout analysis finds page structure (title/paragraph/table/figure boxes); table recognition splits a page's table into rows, columns and cells with indices (`row_id`, `col_id`) you can use to crop cells and OCR them separately. Both are plain torch models that run on CPU.
Example: `layouts = layout_pred([page])[0]`; `tres = table_pred([img_t])[0]`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "surya — LayoutPredictor and TableRecPredictor"
Center: a Thai report page on the left; first arrow to a copy of the page covered in colored bounding boxes labeled title, paragraph, table, figure; second arrow zooms the table region with blue horizontal row lines and orange vertical column lines; one intersection cell glows with the label "cell (row_id, col_id)" and a small crop arrow leaves the page.
Caption strip at the bottom: "layout tells you where, table-rec tells you rows and columns."
```

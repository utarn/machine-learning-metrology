# Datasets & pretrained models for unstructured-data ML — OCR, text, image, sound (research ticket)

**Date:** 2026-09-30 · **Branch:** `research/datasets-models-survey` · **Issue:** #19
**Question:** What datasets + pretrained models suit light labs of the revised 3-day intermediate course on unstructured data (OCR / text / image / sound), runnable on free Colab, with course-safe licenses, small downloads, and Thai-language options where practical?

**Verification:** licenses below were read from the Hugging Face dataset/model API (`huggingface.co/api/...`), GitHub repo APIs, and the Common Voice release metadata (`common-voice/cv-dataset`, `cv-corpus-27.0-2026-09-11.json`) on 2026-09-30. Common Voice Thai figures come from the official release JSON, not the website UI.

**Teaching stance (locked, matches the course revision):** pretrained inference demos + small fine-tunes only; nothing that needs more than ~30 min training on a free T4; every notebook must show the source URL + citation (same status policy as `datasets.md`).

---

## Summary table

| Modality | Recommendation | Dataset (+ license) | Pretrained model (+ license) | Thai? | Free-Colab fit |
|---|---|---|---|---|---|
| OCR | **Thai OCR bake-off lab** | `openthaigpt/thai-ocr-evaluation` — CC BY-SA 4.0, <1K images | EasyOCR (Apache-2.0), Tesseract `tha` (Apache-2.0), `openthaigpt/thai-trocr` (Apache-2.0, 103M params) | Yes | CPU-only OK; T4 faster |
| Text | **Fine-tune an encoder on Thai sentiment** | Wisesight Sentiment Corpus (PyThaiNLP) — CC0; UCI mirror CC BY 4.0; 26,737 messages | `google-bert/bert-base-multilingual-cased` (Apache-2.0); WangchanBERTa as demo (license not machine-readable — caveat) | Yes | mBERT fine-tune: ~2–5 min/epoch on T4 |
| Image | **Transfer learning on Fashion-MNIST** | Fashion-MNIST (MIT, 70K 28×28, ~30 MB) | torchvision `mobilenet_v3_small` / `resnet18` weights (BSD-3) | No practical Thai dataset found | CPU-feasible; T4 minutes |
| Sound | **ESC-50 classification + Whisper Thai ASR demo** | ESC-50 (CC BY-NC 3.0, 2,000 clips, ~600 MB); Google Speech Commands v2 (CC BY 4.0, 2.3 GB) as CC alternative | Whisper (Apache-2.0); `biodatlab/whisper-th-small` Thai-finetuned (Apache-2.0) | Yes (ASR only) | ESC-50 lab CPU/T4; Whisper inference on T4 (fp16) |

---

## Module — OCR (Thai printed text)

### Primary: EasyOCR + Tesseract + ThaiTrOCR comparison ("OCR bake-off")

- **What it is:** three pretrained OCR systems with different architectures — CRAFT-detection CNN (EasyOCR), legacy LSTM engine (Tesseract), and a ViT+Transformer encoder-decoder (TrOCR) — evaluated on the same Thai printed-document images with Character Error Rate.
- **Model licenses (all verified):**
  - EasyOCR — Apache-2.0 (GitHub `JaidedAI/EasyOCR`); supports Thai (`th`) among 80+ languages; detection (~15 MB) + recognition (~65 MB) models download on first use. Colab: `pip install easyocr`, CPU inference fine.
  - Tesseract 5 + `tha` traineddata — Apache-2.0; `pytesseract` wrapper; zero-GPU.
  - `openthaigpt/thai-trocr` — Apache-2.0, 103M params (HF API safetensors), trained for Thai+English line OCR; loads on CPU/T4 with `transformers` pipeline `image-to-text`.
- **Dataset:** `openthaigpt/thai-ocr-evaluation` (HF) — CC BY-SA 4.0, size category `n<1K` evaluation images over Thai document domains. Small enough to fetch in a notebook.
- **Lab shape:** run all three on 10–20 Thai printed lines (course-provided images or the dataset's), compute CER with `jiwer`, discuss when deep OCR beats the classic engine (fonts, layout, noise). Pure inference — nothing to train.
- **Lecture demo (not a lab):** `typhoon-ai/typhoon-ocr-3b` (Apache-2.0, 3.75B params — HF API) shows modern VLM-based document extraction for Thai; needs 4-bit quantization to fit a T4, so instructor demos it live, students don't run it.

### Alternatives considered
- `microsoft/trocr-base-printed` — great pedagogy for English printed text but English-only; keep as the "explain TrOCR" slide reference.
- Thai handwritten OCR models (e.g. `kkatiz/thai-trocr-thaigov-v2`, community fine-tunes of DeepSeek-OCR) — mostly small-audience models without clear license metadata; not vetted for course use.
- ICDAR/SROIE receipt datasets — benchmark-grade but license terms require registration; more friction than value for a 45-min lab.

**Recommendation:** the 3-model Thai OCR bake-off above. All Apache-2.0, all inference-only, genuinely Thai, runs on free Colab CPU.

---

## Module — Text (Thai NLP)

### Primary: Wisesight Sentiment Corpus + mBERT fine-tune

- **Dataset:** Wisesight Sentiment Corpus — 26,737 Thai social-media messages, labels `pos/neu/neg/q`. **CC0 1.0** (PyThaiNLP GitHub/HF `pythainlp/wisesight_sentiment`; UCI ML Repository mirror is CC BY 4.0). Kudos: identical license story to the tabular datasets already in `datasets/` — attribution + source URL in the notebook, no restrictions.
- **Model:** `google-bert/bert-base-multilingual-cased` — **Apache-2.0** (HF API cardData), 178M params. Fine-tunes on Wisesight in ~2–5 min/epoch on a T4; even CPU runs one epoch if you subsample. This is the "light fine-tune" lab of the course.
- **Thai-specific teaching hook:** no word boundaries. Demo **PyThaiNLP** (Apache-2.0) word segmentation first — students see why whitespace tokenization fails in Thai before meeting the tokenizer.

### Alternatives considered
- **WangchanBERTa** (`airesearch/wangchanberta-base-att-spm-uncased`, 105M, 138K downloads) — best-known Thai encoder; *but the HF model card carries no machine-readable license tag* (code repo `vistec-AI/thai2transformers` is Apache-2.0; weights' terms must be checked on the release page before course distribution). Use as a **masked-LM demo** with a license-check caveat; mBERT is the model students fine-tune.
- IMDB reviews / 20 newsgroups — classic English teaching sets, but IMDB has no formal license; not needed given Wisesight exists.

**Recommendation:** Wisesight (CC0) + mBERT fine-tune, with PyThaiNLP segmentation demo up front and WangchanBERTa as instructor demo.

---

## Module — Image (computer vision)

### Primary: Fashion-MNIST + torchvision transfer learning

- **Dataset:** Fashion-MNIST — 70K 28×28 grayscale images, 10 classes. **MIT** (GitHub `zalandoresearch/fashion-mnist`, verified API). ~30 MB, loads via `torchvision.datasets.FashionMNIST` in seconds. Same 10-class format students already know from MNIST-era tabular labs.
- **Model:** torchvision pretrained `mobilenet_v3_small` (2.5M params) or `resnet18` — weights distributed under the repo's BSD-3-Clause. Freeze backbone → train the head: minutes on T4, feasible on CPU with subsampling.
- **Lab shape:** replace-head transfer learning, confusion matrix, error inspection. Reinforces the evaluation-metrics module from the tabular course.

### Alternatives considered
- **CIFAR-10** (60K 32×32 RGB) — the canonical step up from MNIST, but ships with **no formal license**; customary for teaching, still worth a slide-note.
- **NEU Surface Defect Database** — 1,800 grayscale images, 6 metal surface-defect classes; extremely metrology-relevant (QC inspection). Caveats: original release has **no explicit license** (Kaggle mirror states "License Unknown"); a Roboflow re-upload is CC BY 4.0 but redistribution provenance is murky. Use only as an instructor demo after license vetting, or substitute students' own phone photos of instruments/gauges.
- Food-101 / plant-disease sets — fun but off-theme and license-light.

**Thai options:** none practical found — no widely-licensed Thai image-classification dataset with clear terms surfaced in the search. State this explicitly in the course: the image module runs in English-domain data; the Thai angle is covered by the OCR and sound modules instead.

**Recommendation:** Fashion-MNIST (MIT) + MobileNetV3-Small transfer learning. Metrology tie-in via NEU defect images only as a vetted demo.

---

## Module — Sound (audio)

### Primary: ESC-50 classification lab + Whisper Thai ASR demo

- **ESC-50** — 2,000 × 5-sec environmental-sound clips, 50 classes, 5 pre-arranged folds. License: **CC BY-NC** (repo badge + LICENSE file, verified) — fine for a free non-commercial course; cannot be folded into anything commercial. ~600 MB zip; works on CPU for feature-based methods, T4 for spectrogram + small CNN or pretrained `MIT/ast-finetuned-audioset` (Apache-2.0) inference.
- **Thai ASR (demo, not lab):**
  - **Mozilla Common Voice, Thai** — license **CC0**; official release metadata (CV 27.0, 2026-09-11): 427 total hours, **173 validated hours**, 33K train clips, ~9 GB download for the full Thai package. Practicalities: download is gated (free account on HF/Mozilla), and the full package is too big for a classroom — pull the train split or use `datasets` streaming to sample a few hundred clips.
  - **FLEURS, Thai (`th_th`)** — Google/CMU/UTokyo multi-speaker ASR set, **CC BY 4.0**, ~a few hours per language, trivially loadable per-language from HF `google/fleurs`. The practical Thai *lab* dataset if students should run anything themselves.
  - **Models:** `openai/whisper-small` — **Apache-2.0** (HF API), 244M params, transcribes Thai on a T4 in fp16 within free-tier limits; `biodatlab/whisper-th-small` (Mahidol BIODAT lab) — **Apache-2.0**, Thai-finetuned Whisper for a fine-tuned-vs-base comparison. Whisper (large-v3) as lecture demo only — near the T4's 16 GB ceiling.
- **Alternative (clean-license lab dataset):** **Google Speech Commands v2** — CC BY 4.0 (HF API), 2.3 GB, 105K one-second clips of 35 keywords — keyword-spotting lab if you'd rather avoid the CC BY-NC on ESC-50.

**Recommendation:** ESC-50 (or Speech Commands if NC is unacceptable) for the hands-on classification lab; Whisper + FLEURS-Thai / Common Voice-Thai samples for the Thai ASR demo. The Thai speech story is strong — this is the course's best Thai modality after OCR.

---

## Implications for course structure

1. **Day shape:** the four modalities split naturally into two 1.5-day halves — *images (OCR + CV)* and *signals (text + sound)* — each ending in an inference/evaluation lab rather than a training marathon.
2. **Every module is "pretrained first":** the only weight training students do is (a) image-module head fine-tune and (b) text-module mBERT fine-tune. OCR and sound are pure inference + metric computation (CER / WER / accuracy). This fits free-Colab runtime limits and the intermediate audience.
3. **License story is uniform:** recommended stack is Apache-2.0/MIT/CC0/CC BY 4.0 almost everywhere; the only non-commercial item is ESC-50 (CC BY-NC) — swap to Speech Commands v2 (CC BY 4.0) if the course material itself must be redistributable without restriction.
4. **Thai coverage:** OCR (three Thai-capable models + Thai dataset), text (CC0 Thai corpus + Thai segmentation), sound (Thai ASR with CC0/CC BY data). Image is the one modality with no practical Thai dataset — either accept English-domain image data or have students photograph their own instruments.
5. **Tooling additions to the stack:** `transformers`, `datasets`, `torch`(+`torchvision`/`torchaudio`), `easyocr`, `pytesseract`, `pythainlp`, `jiwer` — all pip-installable on Colab; no `apt` beyond tesseract-ocr + `tha` language pack.
6. **Common Voice practicality caveat:** gated download + 9 GB Thai package → pre-download a 200–500-clip sample and host it with the course materials (CC0 permits this), or stream.

## Appendix — license verification log (2026-09-30)

| Item | Source checked | License found |
|---|---|---|
| `openthaigpt/thai-trocr` | HF API cardData | apache-2.0 |
| `openthaigpt/thai-ocr-evaluation` | HF API cardData | cc-by-sa-4.0 |
| EasyOCR | GitHub API repo | Apache-2.0 |
| Tesseract / `tha` traineddata | repo licensing | Apache-2.0 |
| `typhoon-ai/typhoon-ocr-3b`, `-7b` | HF API cardData | apache-2.0 |
| Wisesight Sentiment Corpus | PyThaiNLP GitHub / HF | CC0 1.0 (UCI mirror: CC BY 4.0) |
| `google-bert/bert-base-multilingual-cased` | HF API cardData | apache-2.0 |
| WangchanBERTa (`airesearch/...`) | HF API + README | **no license metadata on card** (code repo Apache-2.0) — verify weights terms before distribution |
| Fashion-MNIST | GitHub API repo | MIT |
| torchvision pretrained weights | repo licensing | BSD-3-Clause |
| CIFAR-10 | — | none formal |
| NEU Surface Defect | Kaggle mirror page | original unknown; Roboflow mirror CC BY 4.0 |
| ESC-50 | repo LICENSE + badge | CC BY-NC |
| Google Speech Commands v2 | HF API cardData | cc-by-4.0 |
| Whisper (`openai/whisper-small`) | HF API cardData | apache-2.0 |
| `biodatlab/whisper-th-small` | HF API cardData | apache-2.0 |
| Common Voice Thai | `common-voice/cv-dataset` release JSON (CV 27.0) | CC0; 427 h total / 173 h validated |
| `google/fleurs` | HF API cardData | cc-by-4.0 |

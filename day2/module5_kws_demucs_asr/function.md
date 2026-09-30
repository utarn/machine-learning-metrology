# Function Reference — Module M5: เทรนโมเดลฟังเสียงจากศูนย์ + Demucs + ASR bake-off

Only functions introduced for the first time in this module are listed here, in the order you will meet them. Functions from earlier modules (e.g. `confusion_matrix` from M1, `set_seed` from M3) are not repeated.

## 1. `sf.read(path, dtype)` + `sf.write(path, data, samplerate)` — soundfile

What it does: Reads an audio file into a NumPy array (shape = samples, or samples × channels) plus its sample rate; `write` saves an array back to disk. No torch involved — plain, fast wav reading (16 kHz mono for both datasets in this module).
Example: `wave, sr = sf.read("clip.wav", dtype="float32")` then `sf.write("out.wav", data.T, 44100)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "soundfile — sf.read(path, dtype) / sf.write"
Center: one large diagram of a wav file icon flowing left-to-right into a small machine labeled "read" that outputs a row of thousands of tiny number tiles next to a tag "sr = 16000"; below, the reverse arrow flows from a stack of number tiles through a machine labeled "write" back into a wav file icon.
Caption strip at the bottom: "audio files are just arrays of numbers — soundfile reads and writes them."
```

## 2. `torchaudio.transforms.MelSpectrogram(...)` + `AmplitudeToDB()` — torchaudio

What it does: Builds a reusable transform that converts a waveform tensor `[batch, samples]` into a mel spectrogram `[batch, n_mels, time]`; `AmplitudeToDB` compresses the dynamic range (log scale). Pure tensor math — no file I/O.
Example: `mel_fn = MelSpectrogram(sample_rate=16000, n_fft=1024, hop_length=256, n_mels=64)` then `feats = to_db(mel_fn(x))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "torchaudio — MelSpectrogram(...) + AmplitudeToDB()"
Center: one large diagram of a jagged waveform strip entering a machine with two dials labeled "n_fft 1024 / hop 256" and a slider labeled "64 mel bands"; the machine outputs a heatmap image with 64 horizontal stripes; a second small stamp labeled "log scale" presses onto the heatmap making its colors even.
Caption strip at the bottom: "waveform -> time x frequency heatmap, squeezed by log."
```

## 3. `TensorDataset(X, y)` + `DataLoader(..., batch_size, shuffle)` — torch.utils.data

What it does: Bundles feature/label tensors into a dataset and yields shuffled mini-batches — the minimal training loop plumbing when features already fit in memory.
Example: `loader = DataLoader(TensorDataset(X_train, y_train), batch_size=128, shuffle=True)` then `for xb, yb in loader: ...`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "torch.utils.data — TensorDataset + DataLoader"
Center: one large diagram of two long trays (a feature tray of spectrogram cards and a label tray of word tags) feeding a shuffling machine labeled "shuffle"; the machine releases small bundles of 128 card+tag pairs strapped together on a conveyor belt labeled "batch".
Caption strip at the bottom: "pair each feature with its label, shuffle, serve in fixed-size bundles."
```

## 4. `nn.Conv2d / BatchNorm2d / ReLU / MaxPool2d / Linear / Dropout` + `CrossEntropyLoss` + `Adam` — torch.nn / torch.optim

What it does: The building blocks of a CNN (first met in M1 as ready-made parts) plus the two objects every from-scratch training loop needs: a loss function and an optimizer. `CrossEntropyLoss` takes raw logits + integer labels; `Adam` updates every parameter using its gradients.
Example: `loss = loss_fn(model(xb), yb); loss.backward(); optimizer.step()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "torch.nn + torch.optim — loss, backward, step"
Center: one large diagram of a three-station loop: station 1 "model(xb)" stamps a prediction card; station 2 "CrossEntropyLoss" compares it with the correct tag and shows a loss number; station 3 "backward + optimizer.step" sends small adjustment arrows back into every layer of the model with a wrench icon; the loop repeats around a circular arrow.
Caption strip at the bottom: "predict, measure, adjust — repeat until the loss stops dropping."
```

## 5. `librosa.load(path, sr=None, mono=False)` + `torchaudio.functional.resample(wav, sr, target)` — librosa / torchaudio

What it does: `librosa.load` decodes any audio format (mp3 included, via ffmpeg fallback) and returns a channels × samples array; `resample` converts the sample rate to what a model expects (Demucs: 44,100 Hz).
Example: `audio, sr = librosa.load(song_path, sr=None, mono=False)` then `wav = TF.resample(wav, sr, 44100)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "librosa.load + torchaudio.functional.resample"
Center: one large diagram showing mp3/wav/m4a file icons dropping into a decoder funnel labeled "librosa.load (any format)"; the funnel outputs two parallel waveform strips labeled "2 channels"; the strips then pass through a speed-matching machine labeled "resample -> 44100 Hz" with a small metronome icon.
Caption strip at the bottom: "decode anything, then match the sample rate the model was trained on."
```

## 6. `get_model("htdemucs")` + `apply_model(model, mix, device, split, overlap)` — demucs

What it does: `get_model` fetches pretrained Demucs weights (4 sources: drums/bass/other/vocal at 44.1 kHz stereo); `apply_model` runs it over a `[1, 2, samples]` tensor, cutting long songs into 8-second chunks with overlap automatically, and returns `[1, 4, 2, samples]` — one stem per source. `model.sources` and `model.samplerate` describe the output.
Example: `stems = apply_model(model, wav[None].to(device), device=device, split=True, overlap=0.25)[0]`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "demucs — get_model + apply_model"
Center: one large diagram of a stereo song tensor (two stacked waveform strips in a slot labeled [1, 2, samples]) entering a slicing machine that cuts it into overlapping 8-second pieces labeled "split, overlap 0.25"; the pieces pass through a big box labeled "htdemucs" and re-merge into four output slots labeled drums, bass, other, vocal.
Caption strip at the bottom: "slice the song, separate each piece, stitch the stems back together."
```

## 7. `Audio(data, rate)` + `display(...)` — IPython.display

What it does: Renders a playable audio player directly in the notebook from a NumPy array (or `[channels, samples]` for stereo) — how you listen to test clips, synthesized silence, or Demucs stems without leaving the page.
Example: `display(Audio(wave, rate=16000))` or `display(Audio(stem, rate=44100))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "IPython.display — Audio(data, rate)"
Center: one large diagram of a row of number tiles labeled "samples" flowing into a small speaker icon with a play button; below the speaker four smaller players in a row labeled mix, drums, bass, vocal each with their own tiny waveform; a clock icon labeled "rate = samples per second" sits beside them.
Caption strip at the bottom: "numbers + a rate = a play button inside your notebook."
```

## 8. `pipeline("automatic-speech-recognition", model, device)` — transformers

What it does: One-call ASR: builds tokenizer/feature extractor + model behind the scenes; pass a 16 kHz waveform (NumPy array) and `generate_kwargs={"language": "th", "task": "transcribe"}` to force Thai transcription.
Example: `pipe = pipeline("automatic-speech-recognition", model="openai/whisper-small", device=0)` then `pipe(wave, generate_kwargs={"language": "th", "task": "transcribe"})["text"]`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "transformers — pipeline('automatic-speech-recognition')"
Center: one large diagram of a waveform entering a single combined box labeled "pipeline: feature extractor + model + decoder"; a settings dial on the box reads "language: th"; Thai text cards exit the right side; a small comparison badge labeled "Whisper-small 244M" hangs on the box.
Caption strip at the bottom: "one call wires up everything — audio in, text out."
```

## 9. `AutoProcessor.from_pretrained` + `apply_chat_template(..., audio)` + `AutoModelForMultimodalLM` — transformers 5.x

What it does: Loads the processor and multimodal model for Typhoon-ASR (Qwen3-ASR based). The chat template takes a system text (`"Thai"` for plain transcription) plus an audio block in the user message, tokenizes everything into model inputs, and `generate` produces the transcript tokens.
Example: `inputs = processor.apply_chat_template([msgs], tokenize=True, return_dict=True, return_tensors="pt")` then `out = model.generate(**inputs, max_new_tokens=440)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "transformers 5.x — AutoProcessor + AutoModelForMultimodalLM"
Center: one large diagram of a chat bubble conversation: a small system bubble labeled "Thai", a user bubble holding a waveform snippet; both bubbles feed into a template machine labeled "apply_chat_template" that outputs aligned token tiles; the tiles enter a large model box labeled "Typhoon-ASR 0.6B" and Thai text exits the top.
Caption strip at the bottom: "audio joins the conversation as just another message content block."
```

## 10. `jiwer.wer(refs, hyps)` + `jiwer.cer(refs, hyps)` — jiwer

What it does: Computes word/character error rate between lists of reference and hypothesis strings (first met as `cer` in M2 — same call pattern, different granularity). Lower is better; 1.0 means everything wrong.
Example: `jiwer.wer(refs, hyps)` returns one aggregate number for the whole list.

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "jiwer — wer(refs, hyps) / cer(refs, hyps)"
Center: one large diagram of two parallel conveyor belts, the top one carrying reference transcript cards in Thai and the bottom one carrying hypothesis cards; a comparator machine between them stamps red marks on mismatched words (substitution, insertion, deletion icons); a scoreboard on the right shows "WER = errors / words" and a smaller dial labeled "CER".
Caption strip at the bottom: "align reference and hypothesis, count the mistakes, divide by the truth."
```

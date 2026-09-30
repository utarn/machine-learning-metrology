# Function Reference — Module M4-CNN: เทรน spectrogram CNN จากศูนย์ บน ESC-50

ฟังก์ชันส่วนใหญ่ของโมดูลนี้คุณเจอมาแล้ว: `librosa.load` / `melspectrogram` / `power_to_db` (ดู `module4_sound_to_numbers/function.md`) และ `TensorDataset` / `DataLoader` / `nn.Conv2d` / `nn.MaxPool2d` / ลูป `loss.backward()` + `opt.step()` (ดู M1's `function.md`) — ที่นี่จึงลิสต์เฉพาะของใหม่ที่เกิดจากการย้ายไปเทรนบน **GPU** เป็นหลัก

## 1. `torch.cuda.is_available()` + `torch.cuda.get_device_name(0)` — torch

What it does: Checks whether a CUDA GPU is visible to PyTorch and prints its name. Every Kaggle-bound notebook should call this first and warn loudly if it falls back to CPU — training the same CNN on CPU takes ~10x longer.
Example: `DEVICE = "cuda" if torch.cuda.is_available() else "cpu"`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "torch — cuda.is_available() / cuda.get_device_name(0)"
Center: a small checkbox panel labeled "GPU available?" with two outcomes: a green check leading to a GPU card icon labeled "Tesla T4", and a gray warning triangle leading to a slow snail icon labeled "CPU fallback - 10x slower".
Caption strip at the bottom: "check before you train - loud warnings save afternoons."
```

## 2. `tensor.to(device)` / `model.to(device)` / `tensor.cpu()` — torch

What it does: Moves tensors and model weights between devices — the GPU has its own memory, so both the model and every batch must be moved onto it with `.to(DEVICE)`, and results moved back with `.cpu()` (numpy/accuracy_score only work on CPU tensors). This is the only new code the GPU costs you in the training loop you already know from M1.
Example: `model = SmallCNN().to(DEVICE)` ... `for xb, yb in dl: xb, yb = xb.to(DEVICE), yb.to(DEVICE)` ... `pred = out.argmax(1).cpu().numpy()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "torch — .to(device) / .cpu()"
Center: two rooms side by side labeled "CPU" and "GPU"; a crane moves a model block and small batch boxes labeled "xb, yb" from the CPU room across a bridge labeled ".to(DEVICE)" into the GPU room; a return conveyor labeled ".cpu()" carries a results card labeled "predictions (numpy)" back out.
Caption strip at the bottom: "the GPU has its own memory - model and every batch ride the bridge."
```

## 3. `nn.Flatten()` — torch.nn (แบบ "มองภาพรวมใหม่")

What it does: Collapses every feature map `(batch, channels, height, width)` into one long vector per sample before the final `Linear` layer — after 3 MaxPools our 128 x 216 spectrogram has become 64 maps of 16 x 27, so the flattened vector is 64 x 16 x 27 = 27,648 wide. You used it in M1's SmallCNN; here note the arithmetic, because the flatten dimension is what you must recompute when the input shape changes (e.g. `n_mels=64` in the exercise).
Example: `nn.Flatten(), nn.Linear(64 * (in_mels // 8) * (in_frames // 8), 50)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "torch — nn.Flatten() before Linear"
Center: a stack of 64 small grids (16x27 each) being unrolled ribbon-style into one long strip labeled "27,648 cells" feeding a final Linear layer labeled "-> 50 classes"; a calculator icon labeled "64 x 16 x 27".
Caption strip at the bottom: "change the input size and this number changes with it."
```

## 4. `Counter(pairs).most_common(k)` — collections (standard library)

What it does: Tallies how often each `(true_class, predicted_class)` pair occurs among the wrong predictions and ranks them — a compact error report next to the full 50x50 confusion matrix.
Example: `Counter((t, p) for t, p in zip(y_true, y_pred) if t != p).most_common(8)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "collections — Counter(...).most_common(8)"
Center: a pile of mismatched label tags (each tag shows two class names) dropping into a tally machine that outputs a ranked board of the top 8 pairs with tally marks.
Caption strip at the bottom: "rank the mistakes before you read all 2,500 cells of the matrix."
```

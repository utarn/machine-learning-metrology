# Function Reference — Module M7: วิเคราะห์โมเดลที่เราสร้าง (Grad-CAM + metric รวม)

Only functions introduced for the first time in this module are listed here, in the order you will meet them. Functions from earlier modules (FashionMNIST, DataLoader, confusion matrix, `jiwer.cer`) are not repeated — see M0/M1/M2's `function.md`. โมดูลนี้ implement Grad-CAM เองด้วย torch hooks — ไม่ต้องติดตั้งไลบรารีเพิ่ม

## 1. `Module.register_forward_hook(fn)` — torch.nn.Module

What it does: Installs a function that fires right after the target layer's forward pass; the hook receives the layer's output, letting us capture the conv feature maps (`A^k`) that Grad-CAM weights — and attach a tensor hook to them for gradients.
Example: `self.h_fw = target_layer.register_forward_hook(self._save_act)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "torch — Module.register_forward_hook(fn)"
Center: one large diagram illustrating a CNN layer block with data flowing through it left to right; a small ear-like badge attached to the block's right edge copies the flowing output (a stack of small feature-map cards) onto a clipboard labeled "acts" while the original data continues onward untouched.
Caption strip at the bottom: "a forward hook taps the layer's output and keeps a copy."
```

## 2. `Tensor.register_hook(fn)` — torch.Tensor

What it does: Installs a function that fires when the backward pass computes the gradient of this exact tensor — Grad-CAM attaches it to the last-conv activation inside the forward hook, capturing `∂y^c/∂A^k`, the ingredient averaged per channel (GAP).
Example: `out.register_hook(self._save_grad)` (then `self.grads = grad.detach()`)

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "torch — Tensor.register_hook(fn)"
Center: one large diagram illustrating a stack of small feature-map cards (the conv layer's activation) with a dashed red gradient stream flowing right-to-left through them; a small ear-like badge attached directly to the card stack copies the flowing red stream (arrows of varying thickness) onto a clipboard labeled "grads" while the stream continues toward earlier layers.
Caption strip at the bottom: "a tensor hook taps the gradient of exactly this tensor during backward."
```

## 3. `torch.nn.functional.interpolate(x, size, mode, align_corners)` — torch

What it does: Resizes a tensor; Grad-CAM uses bilinear mode to stretch the coarse 7×7 heatmap back to the original 28×28 image size for overlay.
Example: `F.interpolate(cam[None, None], size=(28, 28), mode="bilinear", align_corners=False)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "torch — F.interpolate(x, size, mode='bilinear')"
Center: one large diagram illustrating a tiny 7x7 grid of magma-colored cells on the left stretching upward and rightward along guide lines into a smooth larger 28x28 grid on the right, with faint diagonal guide lines showing each original cell corner being pulled to its new position; a small magnifier icon labeled "bilinear: blend 4 neighbors" sits between them.
Caption strip at the bottom: "interpolate() stretches a coarse heatmap back to image size."
```

## 4. `torch.save(obj, path)` / `torch.load(path, map_location, weights_only)` — torch

What it does: Saves tensors (here: `model.state_dict()`, the learned weights) to disk and loads them back — the load-or-train cell uses this so a second run skips retraining; `weights_only=True` loads tensors only (safer than pickling whole objects).
Example: `torch.save(cnn.state_dict(), CKPT)` then `cnn.load_state_dict(torch.load(CKPT, map_location="cpu", weights_only=True))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "torch — save(obj, path) and load(path, map_location, weights_only)"
Center: one large diagram illustrating a model brain icon on the left pouring numbered weight chips into a small file box labeled "m1_small_cnn.pt" (arrow down = save), and on the right the same chips flowing out of the box back into an identical empty brain (arrow up = load) with a checkpoint stamp reading "weights_only: tensors only, safe".
Caption strip at the bottom: "save the weights once, load them every run after."
```

## 5. `ax.imshow(X, cmap, alpha)` — matplotlib (overlay idiom)

What it does: Draws an image on an Axes; calling it twice on the same Axes — grayscale base, then the heatmap with `cmap="magma"` and partial transparency (`alpha=0.55`) — produces the classic Grad-CAM overlay.
Example: `ax.imshow(img, cmap="gray"); ax.imshow(heat, cmap="magma", alpha=0.55)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib — ax.imshow(X, cmap, alpha), twice = overlay"
Center: one large diagram illustrating two transparent glass sheets being stacked: the bottom sheet holds a grayscale 28x28 clothing image, the top sheet holds a magma-colored heatmap printed on semi-transparent film (labeled "alpha=0.55"), and beneath the pair the combined result shows the shirt visible through glowing hot spots.
Caption strip at the bottom: "draw the base image, then draw the heatmap on top with transparency."
```

## 6. `confusion_matrix(y_true, y_pred)` — sklearn.metrics

What it does: Builds the C×C count table of true-vs-predicted classes; M7 uses it numerically — per-class error `1 − diagonal/row_sum` and the top off-diagonal confusion pair (zero the diagonal, then `argmax`).
Example: `cm = confusion_matrix(y_test, preds); np.fill_diagonal(cm_off, 0)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — confusion_matrix(y_true, y_pred)"
Center: one large diagram illustrating a 10x10 grid where the diagonal cells are dark teal (correct counts) with the diagonal crossed out by a translucent bar on a small inset grid labeled "zero the diagonal, then argmax"; one off-diagonal cell glows coral and pops out with a callout reading "top confusion pair: T-shirt -> Shirt".
Caption strip at the bottom: "the count table tells you which classes the model mixes up."
```

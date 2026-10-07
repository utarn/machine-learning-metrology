# Function Reference — Module M1: เทรน 3 แบบบนข้อมูลเดียวกัน

Only functions introduced for the first time in this module are listed here, in the order you will meet them. Functions from earlier modules (train_test_split, mean_squared_error, ConfusionMatrixDisplay) are not repeated — see M0's `function.md`.

## 1. `FashionMNIST(root, train, download=True)` — torchvision.datasets

What it does: Loads the Fashion-MNIST dataset (60k train / 10k test 28×28 grayscale clothing images). First call downloads into `root`; later calls load from disk (offline-friendly).
Example: `train_full = FashionMNIST(root=DATA, train=True, download=True)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "torchvision — FashionMNIST(root, train, download)"
Center: one large diagram illustrating a zip archive icon descending from a cloud into a folder labeled "data/", then opening into two neat stacks of small grayscale clothing thumbnails — a tall stack labeled "train 60,000" and a shorter stack labeled "test 10,000", each thumbnail a 28x28 shirt, shoe, or bag.
Caption strip at the bottom: "FashionMNIST() downloads once, then always loads from disk."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 2. `.data` / `.targets` — FashionMNIST tensors

What it does: The images as a `(N, 28, 28)` uint8 tensor and the labels as a `(N,)` tensor; `.numpy()` converts to numpy arrays.
Example: `X_train = train_full.data.numpy()[idx_tr]`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "torchvision — dataset.data and dataset.targets"
Center: one large diagram illustrating a deck of grayscale image cards fanning out to two trays: the left tray holds the picture cards stacked as a 3D block labeled ".data -> (N, 28, 28)", the right tray holds small numbered tags labeled ".targets -> (N,)" with a rubber-band binding them in the same order.
Caption strip at the bottom: "data holds the pictures, targets holds the labels — same order, one index apart."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 3. `LinearSVC(C, max_iter, dual="auto")` — sklearn.svm

What it does: Linear support vector classifier — finds the separating hyperplane with the widest margin; `C` controls the penalty for misclassification.
Example: `LinearSVC(C=1.0, max_iter=5000, dual="auto").fit(Ftr_hog, y_train)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — LinearSVC(C, max_iter, dual='auto')"
Center: one large diagram illustrating a 2D scatter with two point clouds (teal shirts, coral shoes); a solid straight line separates them with two dashed parallel lines at equal distance on either side; the empty band between the dashed lines is highlighted and labeled "widest margin"; a dial labeled "C" sits in the corner.
Caption strip at the bottom: "LinearSVC() draws the separating line with the widest safety margin."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 4. `nn.Conv2d(in_ch, out_ch, kernel_size, padding)` / `nn.MaxPool2d(2)` — torch.nn

What it does: Convolution layer slides learnable filters over the image to produce feature maps; max pooling halves the map size keeping the strongest response.
Example: `nn.Conv2d(1, 16, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "torch — nn.Conv2d(...) and nn.MaxPool2d(2)"
Center: one large diagram illustrating a grayscale image on the left with a small 3x3 filter square sliding across it (motion arrows), producing a stack of feature-map cards in the middle labeled "16 filters", then those cards shrinking to half-size blocks labeled "max pool: keep the strongest response".
Caption strip at the bottom: "Conv2d learns small pattern filters; MaxPool2d shrinks the map, keeping the strongest signals."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 5. `TensorDataset` + `DataLoader(batch_size, shuffle)` — torch.utils.data

What it does: Wraps tensors as a dataset and serves them in shuffled mini-batches for training.
Example: `DataLoader(TensorDataset(X, y), batch_size=128, shuffle=True, generator=g)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "torch — TensorDataset + DataLoader"
Center: one large diagram illustrating a big pile of image-plus-label pairs on the left being dealt by a conveyor into small trays of 128 pairs each, the trays leaving in shuffled order (dice icon labeled "shuffle") toward a training loop arrow.
Caption strip at the bottom: "DataLoader() deals the dataset in shuffled mini-batches of 128."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 6. `loss.backward()` / `opt.step()` — training loop

What it does: The core deep-learning loop — forward pass computes predictions and loss, `backward()` computes gradients, `opt.zero_grad()` clears them, `step()` nudges every weight downhill.
Example:
```
opt.zero_grad()
loss = loss_fn(model(xb), yb)
loss.backward()
opt.step()
```

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "torch — the training loop in four moves"
Center: one large circular diagram with four stations connected by arrows: "forward: predict" (model box with data flowing through), "loss" (a gauge), "backward: gradients" (arrows flowing backwards through the model box), "step: update weights" (a wrench turning bolts on the model box), with a "zero_grad" reset stamp before the loop restarts.
Caption strip at the bottom: "predict, measure the loss, send gradients back, nudge the weights — repeat."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 7. `mobilenet_v3_small(weights=...)` — torchvision.models

What it does: Loads MobileNetV3-Small with pretrained ImageNet weights; we use it as a frozen feature extractor (576-dim vector per image).
Example: `tvm.mobilenet_v3_small(weights=tvm.MobileNet_V3_Small_Weights.IMAGENET1K_V1)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "torchvision — mobilenet_v3_small(weights=IMAGENET1K_V1)"
Center: one large diagram illustrating a download arrow bringing a compact pretrained brain icon (labeled "ImageNet: 1.2M images already seen") into a tall narrow building of stacked layers; a padlock icon labeled "freeze" locks the building while a small attachable head box glows warm beside the roof.
Caption strip at the bottom: "mobilenet_v3_small() brings pretrained vision knowledge we can freeze and borrow."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

## 8. `p.requires_grad_(False)` — freezing parameters

What it does: Marks parameters so the optimizer never updates them — the backbone becomes a fixed feature extractor.
Example: `for p in backbone.parameters(): p.requires_grad_(False)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "torch — p.requires_grad_(False)  (freeze)"
Center: one large diagram illustrating a stack of weight-layer slabs with small padlocks snapped onto each slab and snowflake badges (labeled "frozen"); to the right, one separate small slab remains unlocked with a green wrench icon and label "head — still trainable".
Caption strip at the bottom: "requires_grad_(False) padlocks the pretrained layers so training only touches the new head."
เขียนคำอธิบายสั้นๆ ที่เข้าใจง่ายสำหรับแต่ละฟังก์ชัน พร้อมตัวอย่างการเรียกใช้ และอธิบายพารามิเตอร์ที่ใช้ในฟังก์ชันนั้น ๆ ให้ชัดเจน พร้อมคำอธิบายภาพประกอบ (image prompt) สำหรับสร้างภาพประกอบการสอนแบบ infographic style (flat vector, plain white background, muted colors, clean sans-serif labels, no photorealism, no 3D, no gradients)
```

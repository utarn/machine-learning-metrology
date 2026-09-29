# Function Reference — Module 5: Evaluation

Only functions introduced for the first time in this module are listed here, in the order you will meet them. Functions already covered in earlier modules are not repeated — look them up in the earlier modules' `function.md`.

## 1. `Utf8` — polars

What it does: The polars text (string) data type — declared for the timestamp column so it is read as raw text, not auto-parsed numbers.
Example: `schema_overrides={"label": pl.Int64, "timestamp": pl.Utf8}`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — pl.Utf8"
Center: one large diagram illustrating a small table with two columns; the label column shows a badge "Int64" over numeric cells, while the timestamp column shows a coral badge "Utf8" over cells holding quoted text like "21/04/2008 11:06:00" — with a note that Utf8 means "text characters, kept as-is".
Below the diagram: a small code snippet box rendering exactly this code: schema_overrides={"label": pl.Int64, "timestamp": pl.Utf8}
Caption strip at the bottom: Polars' text data type — declare a column as raw string text.
```

## 2. `to_numpy` — numpy

What it does: Converts a Polars column or DataFrame into a plain NumPy array — the format scikit-learn expects.
Example: `y = (lab["label"] == 1).to_numpy().astype(int)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — Series.to_numpy()"
Center: one large diagram illustrating a tidy polars table column on the left labeled with column metadata melting into a plain rectangular grid of bare numbers on the right labeled "NumPy array"; a badge on the grid reads "what scikit-learn eats", with an arrow showing the one-way conversion.
Below the diagram: a small code snippet box rendering exactly this code: y = (lab["label"] == 1).to_numpy().astype(int)
Caption strip at the bottom: Hand a Polars column over to NumPy as a bare array for scikit-learn.
```

## 3. `confusion_matrix` — sklearn.metrics

What it does: Builds the 2x2 table of every prediction outcome: true/false positives and negatives — the first thing to look at.
Example: `cm = confusion_matrix(y_test, y_pred)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.metrics — confusion_matrix(y_true, y_pred)"
Center: one large diagram illustrating a 2x2 grid whose rows are labeled "actual PASS / actual FAIL" and columns "predicted PASS / predicted FAIL"; each cell holds a counter of parts sorted into it, labeled TN, FP (false reject), FN (false accept), TP, with arrows showing real parts flowing from a production line into the matching cell.
Below the diagram: a small code snippet box rendering exactly this code: cm = confusion_matrix(y_test, y_pred)
Caption strip at the bottom: Sort every prediction into a 2x2 table of what was right and wrong.
```

## 4. `ravel` — sklearn.metrics

What it does: Flattens the 2x2 confusion matrix into four plain numbers: tn, fp, fn, tp.
Example: `tn, fp, fn, tp = cm.ravel()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.metrics — cm.ravel()"
Center: one large diagram illustrating the 2x2 confusion-matrix square being unrolled like a sleeping bag into a single horizontal strip of four labeled cells reading "tn, fp, fn, tp", each cell feeding into one of four variable boxes below.
Below the diagram: a small code snippet box rendering exactly this code: tn, fp, fn, tp = cm.ravel()
Caption strip at the bottom: Flatten the 2x2 confusion matrix into four numbers: TN, FP, FN, TP.
```

## 5. `imshow` — matplotlib.pyplot

What it does: Displays a 2-D array as an image-like grid of colored cells — here it forms the background of the confusion-matrix graphic.
Example: `ax.imshow(np.ones_like(cm), cmap="Greys", vmin=0, vmax=3)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib.pyplot — ax.imshow(matrix, cmap=...)"
Center: one large diagram illustrating a 2x2 grid of colored squares rendered as if each array value picked a shade from a small color ramp strip labeled "cmap"; row and column labels "actual" and "predicted" wrap the grid, showing numbers in an array becoming colored picture cells.
Below the diagram: a small code snippet box rendering exactly this code: ax.imshow(np.ones_like(cm), cmap="Greys", vmin=0, vmax=3)
Caption strip at the bottom: Show a 2-D array as a grid of colored cells — an image drawn from numbers.
```

## 6. `accuracy_score` — sklearn.metrics

What it does: The fraction of predictions that were correct — simple, but misleading when one class dominates.
Example: `acc = accuracy_score(y_test, y_pred)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.metrics — accuracy_score(y_true, y_pred)"
Center: one large diagram illustrating a field of 314 part chips, most stamped with a teal check (correct) and a few with a coral cross (wrong); a fraction bar reads "292 / 314 = 0.93" with a caution tag "looks great — but 93% were PASS anyway".
Below the diagram: a small code snippet box rendering exactly this code: acc = accuracy_score(y_test, y_pred)
Caption strip at the bottom: Fraction of all predictions that were correct — can flatter imbalanced data.
```

## 7. `precision_score` — sklearn.metrics

What it does: Of everything the model flagged as FAIL, the fraction that really was FAIL — "when I raise the alarm, how often am I right?"
Example: `prec = precision_score(y_test, y_pred, zero_division=0)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.metrics — precision_score(y_true, y_pred)"
Center: one large diagram illustrating a bin labeled "flagged FAIL" holding 10 chips — 6 coral truly-failed chips and 4 teal good chips mistakenly flagged; a fraction above reads "6 of 10 flagged were truly bad = precision 0.6".
Below the diagram: a small code snippet box rendering exactly this code: prec = precision_score(y_test, y_pred, zero_division=0)
Caption strip at the bottom: Of all parts flagged FAIL, how many really were FAIL.
```

## 8. `recall_score` — sklearn.metrics

What it does: Of all the real FAILs, the fraction the model caught — "how many defects slipped through?"
Example: `rec = recall_score(y_test, y_pred)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.metrics — recall_score(y_true, y_pred)"
Center: one large diagram illustrating a fishing net catching coral defect chips swimming in a stream: 11 caught inside the net, 6 escaping past it to the right; a fraction reads "11 of 17 real FAILs caught = recall 0.65".
Below the diagram: a small code snippet box rendering exactly this code: rec = recall_score(y_test, y_pred)
Caption strip at the bottom: Of all the real FAILs, how many the model actually caught.
```

## 9. `f1_score` — sklearn.metrics

What it does: The harmonic mean of precision and recall — one number that is only high when both are high.
Example: `f1 = f1_score(y_test, y_pred)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.metrics — f1_score(y_true, y_pred)"
Center: one large diagram illustrating a balance scale whose two pans hold a "precision" weight and a "recall" weight; the needle below shows a single F1 gauge that only reads high when both pans are equally heavy — a lopsided pairing pulls the F1 gauge down.
Below the diagram: a small code snippet box rendering exactly this code: f1 = f1_score(y_test, y_pred)
Caption strip at the bottom: One balanced score combining precision and recall — high only if both are high.
```

## 10. `zeros_like` — numpy

What it does: Creates an array of zeros with the same shape as another array — here the "lazy model" that predicts PASS (0) for every part.
Example: `lazy = np.zeros_like(y_test)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.zeros_like(y_test)"
Center: one large diagram illustrating the y_test array shown as a row of mixed 0/1 cells casting a ghost outline beside it; the ghost outline is filled entirely with zeros, cell by cell, labeled "same shape, all zeros — the lazy all-PASS prediction".
Below the diagram: a small code snippet box rendering exactly this code: lazy = np.zeros_like(y_test)
Caption strip at the bottom: Make an all-zeros array shaped exactly like another array.
```

## 11. `set_ylabel` — matplotlib.pyplot

What it does: Sets the label text of a plot's y-axis — here, "metric value" on the threshold-sweep chart.
Example: `ax.set_ylabel("metric value")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib.pyplot — ax.set_ylabel(text)"
Center: one large diagram illustrating a mini line chart whose vertical axis has a blank label placeholder being stamped with the rotated text "metric value" by a small label gun; the x-axis keeps its own separate label to show the two are set independently.
Below the diagram: a small code snippet box rendering exactly this code: ax.set_ylabel("metric value")
Caption strip at the bottom: Write the text label along a plot's vertical axis.
```

## 12. `roc_curve` — sklearn.metrics

What it does: Returns the false-positive and true-positive rates at every possible threshold — the points that draw the ROC curve.
Example: `fpr, tpr, _ = roc_curve(y_test, y_proba)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.metrics — roc_curve(y_true, y_proba)"
Center: one large diagram illustrating a square plot with a dashed diagonal "chance" line from corner to corner and a teal curve bowing up above it toward the top-left; along the curve, three small threshold dials (0.9, 0.5, 0.1) show how sliding the threshold walks you along the curve, trading true-positive rate against false-positive rate.
Below the diagram: a small code snippet box rendering exactly this code: fpr, tpr, _ = roc_curve(y_test, y_proba)
Caption strip at the bottom: Trace true-positive vs false-positive rate at every threshold — the ROC curve.
```

## 13. `roc_auc_score` — sklearn.metrics

What it does: Summarizes the ROC curve as one number from 0 to 1 — the area under it; how well scores rank FAIL above PASS.
Example: `roc_auc = roc_auc_score(y_test, y_proba)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.metrics — roc_auc_score(y_true, y_proba)"
Center: one large diagram illustrating the ROC square with the area between the diagonal chance line and the bowed teal curve shaded in, filled with a hatching pattern labeled "AUC = 0.757"; a random deck on the side reads "0.5 = coin flip ranking, 1.0 = perfect ranking".
Below the diagram: a small code snippet box rendering exactly this code: roc_auc = roc_auc_score(y_test, y_proba)
Caption strip at the bottom: One number for the ROC curve: the area under it, 0.5 = random, 1.0 = perfect.
```

## 14. `precision_recall_curve` — sklearn.metrics

What it does: Precision vs recall at every threshold — the more honest curve when positive cases are rare.
Example: `prec_c, rec_c, _ = precision_recall_curve(y_test, y_proba)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.metrics — precision_recall_curve(y_true, y_proba)"
Center: one large diagram illustrating a square plot whose x-axis is recall and y-axis precision, with a coral curve stepping down from the top-left (high precision, low recall) toward the bottom-right; a dashed horizontal baseline near the floor is labeled "fail rate 5.4% — the number to beat", and a slider under the plot shows the threshold moving the operating point along the curve.
Below the diagram: a small code snippet box rendering exactly this code: prec_c, rec_c, _ = precision_recall_curve(y_test, y_proba)
Caption strip at the bottom: Plot precision against recall at every threshold — honest when positives are rare.
```

## 15. `average_precision_score` — sklearn.metrics

What it does: Summarizes the precision-recall curve into one number (PR-AUC) — weighted mean precision across recalls.
Example: `pr_auc = average_precision_score(y_test, y_proba)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.metrics — average_precision_score(y_true, y_proba)"
Center: one large diagram illustrating the precision-recall plot with the area under the coral curve shaded, labeled "PR-AUC = 0.157", next to a comparison strip: "ROC-AUC said 0.757, but PR-AUC 0.157 tells the rare-defect truth"; a tiny baseline band at the fail-rate level emphasizes how far above baseline the curve reaches.
Below the diagram: a small code snippet box rendering exactly this code: pr_auc = average_precision_score(y_test, y_proba)
Caption strip at the bottom: One number for the precision-recall curve — the area under it (PR-AUC).
```

## 16. `StratifiedKFold` — sklearn.model_selection

What it does: Splits data into k folds while keeping the class ratio the same in every fold — fair cross-validation for imbalanced data.
Example: `cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.model_selection — StratifiedKFold(n_splits=5)"
Center: one large diagram illustrating a long data bar (mostly teal PASS chips with a thin band of coral FAIL chips) sliced into 5 vertical folds; every fold contains the same thin coral stripe, shown side by side, with one fold highlighted as the validation slice and the other four stacked as the training slice.
Below the diagram: a small code snippet box rendering exactly this code: cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
Caption strip at the bottom: Split into 5 folds, each keeping the same PASS/FAIL class ratio.
```

## 17. `cross_validate` — sklearn.model_selection

What it does: Runs the model once per fold and returns a score per fold — mean ± std tells you the repeatability of the metric.
Example: `cv_res = cross_validate(clf, X, y, cv=cv, scoring=scoring)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.model_selection — cross_validate(model, X, y, cv, scoring)"
Center: one large diagram illustrating the 5-fold carousel: one model box cloned five times, each fed a different train/validation slice and emitting a small score card; the five score cards line up as a row of dots whose average and spread are drawn as "mean ± std", styled like a repeatability gauge from a calibration lab.
Below the diagram: a small code snippet box rendering exactly this code: cv_res = cross_validate(clf, X, y, cv=cv, scoring=scoring)
Caption strip at the bottom: Score the model on every fold — report mean ± std as the metric's repeatability.
```

## 18. `repeat` — numpy

What it does: Repeats each value a given number of times in a row — used here to spread one CV-score dot across the positions of its fold group.
Example: `np.repeat(xpos, 5)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.repeat(xpos, 5)"
Center: one large diagram illustrating a short row of position tags [0, 1, 2] being fed through a small duplicator machine that stamps each tag five times in a row — 0 0 0 0 0 1 1 1 1 1 2 2 2 2 2 — so five scattered fold-dots can share one x position on a chart.
Below the diagram: a small code snippet box rendering exactly this code: np.repeat(xpos, 5)
Caption strip at the bottom: Repeat every value n times in a row — one x position per group of 5 dots.
```

## 19. `mean_absolute_error` — sklearn.metrics

What it does: The average absolute size of prediction errors for regression — easy to read and robust to outliers.
Example: `mae = mean_absolute_error(yc_te, pred_pe)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.metrics — mean_absolute_error(y_true, y_pred)"
Center: one large diagram illustrating a scatter of predicted-vs-actual points around a diagonal target line, with straight vertical gap segments drawn between each point and the line, each labeled |error|; the segments' lengths are averaged by a small calculator icon into one result "MAE = 3.5 MW".
Below the diagram: a small code snippet box rendering exactly this code: mae = mean_absolute_error(yc_te, pred_pe)
Caption strip at the bottom: Average the straight-line size of errors — no squaring, outliers don't dominate.
```

## 20. `calibration_curve` — sklearn.metrics

What it does: Groups predictions into bins and compares predicted probability against the observed fail rate — the reliability diagram for your gauge.
Example: `frac_pos, mean_pred = calibration_curve(y_test, y_proba, n_bins=5, strategy="quantile")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.calibration — calibration_curve(y_true, y_proba, n_bins=5)"
Center: one large diagram illustrating a square plot with a dashed diagonal labeled "perfectly calibrated" (predicted = observed); five binned buckets of parts feed the plot, each bin becoming a dot whose x is the predicted P(FAIL) and y the real fail rate — the dots drift below the diagonal, tagged "model overconfident".
Below the diagram: a small code snippet box rendering exactly this code: frac_pos, mean_pred = calibration_curve(y_test, y_proba, n_bins=5, strategy="quantile")
Caption strip at the bottom: Bin the predictions and check predicted probability against the real fail rate.
```

## 21. `RandomForestRegressor` — sklearn.ensemble

What it does: Many decision trees voting on a number instead of a class — the regression sibling of RandomForestClassifier.
Example: `RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.ensemble — RandomForestRegressor(n_estimators=200)"
Center: one large diagram illustrating a small forest of decision trees where, instead of vote tickets, each tree holds up a small number card (like 435.2 MW); all cards feed into an averaging funnel producing one final numeric prediction — a dial showing a continuous value rather than a PASS/FAIL stamp.
Below the diagram: a small code snippet box rendering exactly this code: RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1)
Caption strip at the bottom: Many decision trees each predict a number; the average is the prediction.
```

---
**21 new functions introduced in this module.**

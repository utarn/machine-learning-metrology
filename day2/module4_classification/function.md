# Function Reference — Module 4: Classification

Only functions introduced for the first time in this module are listed here, in the order you will meet them. Functions already covered in earlier modules are not repeated — look them up in the earlier modules' `function.md`.

## 1. `zipfile.ZipFile` — python

What it does: Opens a ZIP archive so you can read the files packed inside it (the SECOM dataset ships as a `.zip`).
Example: `with zipfile.ZipFile(DATA / "secom.zip") as z:`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — zipfile.ZipFile(path)"
Center: one large diagram illustrating a closed zipper box labeled "secom.zip" being opened at the top, with two flat document sheets sliding out of it, labeled "secom.data" and "secom_labels.data", an arrow pointing from the opened box to the two sheets showing what goes in (a path to the zip) and what comes out (the files inside as raw bytes).
Below the diagram: a small code snippet box rendering exactly this code: with zipfile.ZipFile(DATA / "secom.zip") as z:
Caption strip at the bottom: Open a ZIP archive so the files packed inside it can be read.
```

## 2. `io.BytesIO` — python

What it does: Wraps raw bytes so they behave like a file on disk — letting `read_csv` read data that came straight out of a ZIP member.
Example: `pl.read_csv(io.BytesIO(z.read("secom.data")), separator=" ", ...)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — io.BytesIO(bytes)"
Center: one large diagram illustrating a stream of raw bytes (a row of small squares labeled 0/1) flowing into a converter box labeled "BytesIO" and coming out shaped like a familiar file-folder icon, so a function that expects a file can swallow it; an arrow labeled "read_csv" then pulls the data into a small table.
Below the diagram: a small code snippet box rendering exactly this code: pl.read_csv(io.BytesIO(z.read("secom.data")), separator=" ", ...)
Caption strip at the bottom: Wrap raw bytes so they behave like a file — read straight from memory instead of disk.
```

## 3. `rename` — polars

What it does: Renames columns of a DataFrame using a mapping of old name → new name.
Example: `.rename({"column_0": "n_missing"})`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — rename({'column_0': 'n_missing'})"
Center: one large diagram illustrating a small table whose column header reads "column_0" with a sticky-note being pasted over it renaming it to "n_missing"; a small dictionary icon (two curly braces) with an arrow shows the old name going in and the new name coming out.
Below the diagram: a small code snippet box rendering exactly this code: .rename({"column_0": "n_missing"})
Caption strip at the bottom: Give DataFrame columns new names using an old-name-to-new-name mapping.
```

## 4. `bar` — matplotlib.pyplot

What it does: Draws a vertical bar chart — here, the number of PASS vs FAIL units in the SECOM dataset.
Example: `ax.bar(["PASS (-1)", "FAIL (+1)"], [n_pass, n_fail], color=["#2a9d8f", "#e76f51"])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib.pyplot — ax.bar(labels, heights)"
Center: one large diagram illustrating two vertical bars rising from a baseline — one tall teal bar labeled "PASS" and one short coral bar labeled "FAIL" — with category names written under the bars and value labels on top, showing that category names go in and bar heights are the counts.
Below the diagram: a small code snippet box rendering exactly this code: ax.bar(["PASS (-1)", "FAIL (+1)"], [n_pass, n_fail])
Caption strip at the bottom: Draw a vertical bar chart: one bar per category, height = value.
```

## 5. `text` — matplotlib.pyplot

What it does: Places free text at an (x, y) position inside a plot — used here to write the count above each bar.
Example: `ax.text(i, v + 25, f"{v:,}", ha="center", color="#264653", fontsize=11)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib.pyplot — ax.text(x, y, s)"
Center: one large diagram illustrating a mini bar chart where a text label "1,463" floats just above the top of one bar, placed by a small crosshair marker at coordinates (x, y); dotted leader lines from the axes show how x and y pin down where the text lands.
Below the diagram: a small code snippet box rendering exactly this code: ax.text(i, v + 25, f"{v:,}", ha="center")
Caption strip at the bottom: Put a piece of text at an exact (x, y) spot inside the plot.
```

## 6. `DummyClassifier` — sklearn.dummy

What it does: A deliberately "stupid" baseline model that ignores all features — here it always answers the most frequent class (PASS), which already scores 93.4% accuracy.
Example: `dummy = DummyClassifier(strategy="most_frequent")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.dummy — DummyClassifier(strategy='most_frequent')"
Center: one large diagram illustrating a simple wind-up toy robot holding a single sign that always says "PASS", ignoring a whole conveyor of feature cards streaming past it; a speech bubble reads "accuracy 93.4% — caught 0 of 104 FAILs".
Below the diagram: a small code snippet box rendering exactly this code: dummy = DummyClassifier(strategy="most_frequent")
Caption strip at the bottom: A baseline model that always guesses the most common class — the score to beat.
```

## 7. `drop` — polars

What it does: Removes named columns and keeps everything else — used to peel off the label column to build the feature matrix X.
Example: `X = secom.drop("label")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.drop('label')"
Center: one large diagram illustrating a wide table where one coral column labeled "label" is being lifted out and dropped into a small trash bin below, while the remaining teal columns slide together and stay intact as the output table labeled "X".
Below the diagram: a small code snippet box rendering exactly this code: X = secom.drop("label")
Caption strip at the bottom: Remove named columns and keep everything else.
```

## 8. `round` — numpy

What it does: Rounds array values to a given number of decimal places — used here to display the learned imputer medians tidily.
Example: `np.round(prep.named_steps['impute'].statistics_[:5], 3)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.round(arr, digits)"
Center: one large diagram illustrating a row of long decimal numbers like 2.718281 flowing into a funnel/rounding machine labeled "3 decimals" and coming out as tidy short numbers like 2.718; the number of decimals is shown as a small dial set to 3.
Below the diagram: a small code snippet box rendering exactly this code: np.round(prep.named_steps['impute'].statistics_[:5], 3)
Caption strip at the bottom: Round every number in an array to a fixed number of decimal places.
```

## 9. `LogisticRegression` — sklearn.linear_model

What it does: A linear classifier that outputs a probability for each class; `class_weight="balanced"` compensates for the far-more-common PASS class.
Example: `LogisticRegression(class_weight="balanced", max_iter=2000, random_state=42)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.linear_model — LogisticRegression(class_weight='balanced')"
Center: one large diagram illustrating a classic S-shaped sigmoid curve over an input axis of sensor readings, with a horizontal dashed threshold line at probability 0.5; points left of the S sit in a teal "PASS" zone, points right in a coral "FAIL" zone, and two small balance weights labeled "balanced" sit under each class to show rare FAILs get extra weight.
Below the diagram: a small code snippet box rendering exactly this code: LogisticRegression(class_weight="balanced", max_iter=2000)
Caption strip at the bottom: A linear classifier that turns features into a class probability via an S-curve.
```

## 10. `SVC` — sklearn.svm

What it does: Support Vector classifier that separates the classes with a smooth non-linear (RBF kernel) boundary.
Example: `SVC(kernel="rbf", class_weight="balanced", random_state=42)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.svm — SVC(kernel='rbf')"
Center: one large diagram illustrating a 2-D scatter of teal dots and coral dots separated by a smooth curved boundary line drawn between them, with the boundary hugging a few emphasized dots on its edges (the support vectors, drawn with small rings); a small "rbf" badge suggests the curve can bend.
Below the diagram: a small code snippet box rendering exactly this code: SVC(kernel="rbf", class_weight="balanced", random_state=42)
Caption strip at the bottom: Separate the classes with a flexible curved boundary built from edge-case points.
```

## 11. `CalibratedClassifierCV` — sklearn.calibration

What it does: Wraps a classifier (like SVC) and recalibrates its raw scores so they become honest, comparable probabilities.
Example: `CalibratedClassifierCV(SVC(kernel="rbf", ...), ensemble=False)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.calibration — CalibratedClassifierCV(estimator)"
Center: one large diagram illustrating a model box labeled "SVC" feeding raw scores into a gauge dial being adjusted by a small calibration wrench; before the wrench the needle overshoots a red zone, after it the needle aligns with honest marks labeled 0.0 to 1.0 "true probability".
Below the diagram: a small code snippet box rendering exactly this code: CalibratedClassifierCV(SVC(kernel="rbf", ...), ensemble=False)
Caption strip at the bottom: Wrap a classifier so its raw scores become honest, comparable probabilities.
```

## 12. `RandomForestClassifier` — sklearn.ensemble

What it does: An ensemble of many decision trees that each vote on the class; robust and non-linear, and it can report which features it used most.
Example: `RandomForestClassifier(n_estimators=300, class_weight="balanced_subsample", random_state=42, n_jobs=-1)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.ensemble — RandomForestClassifier(n_estimators=300)"
Center: one large diagram illustrating a small forest of simple decision trees (drawn as branching flowcharts), each tree casting a vote ticket labeled PASS or FAIL into a ballot box at the front; a majority counter reads the winning vote as the prediction, and one tree shows a tiny yes/no split at a node.
Below the diagram: a small code snippet box rendering exactly this code: RandomForestClassifier(n_estimators=300, class_weight="balanced_subsample")
Caption strip at the bottom: Hundreds of decision trees vote together — the majority wins.
```

## 13. `XGBClassifier` — xgboost

What it does: Gradient-boosted trees — trees are built one after another, each correcting the previous ones' mistakes; `scale_pos_weight` handles the PASS/FAIL imbalance.
Example: `XGBClassifier(n_estimators=300, learning_rate=0.1, max_depth=5, scale_pos_weight=spw, eval_metric="logloss")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "xgboost — XGBClassifier(n_estimators=300, learning_rate=0.1)"
Center: one large diagram illustrating a row of small decision trees being stacked left to right like building blocks, each new tree labeled "fixes leftover errors" with an arrow to the residual mistakes of the stack before it; a small speedometer labeled "learning_rate 0.1" shows each correction is applied gently.
Below the diagram: a small code snippet box rendering exactly this code: XGBClassifier(n_estimators=300, learning_rate=0.1, max_depth=5)
Caption strip at the bottom: Gradient-boosted trees — each new tree fixes the mistakes left by the ones before.
```

## 14. `Int64` — polars

What it does: The polars 64-bit integer data type — used here to relabel -1/+1 classes as 0/1, which XGBoost requires.
Example: `y01_train = (train["label"] == 1).cast(pl.Int64)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — pl.Int64"
Center: one large diagram illustrating a column of values labeled -1 and +1 passing through a converter stamp labeled "cast(pl.Int64)" and emerging as whole-number 0 and 1 values; a small tag on the output column reads "Int64 = whole numbers only".
Below the diagram: a small code snippet box rendering exactly this code: y01_train = (train["label"] == 1).cast(pl.Int64)
Caption strip at the bottom: Polars' integer data type — relabel classes as whole numbers 0/1.
```

## 15. `predict_proba` — sklearn.pipeline

What it does: Predicts a probability for each class instead of a hard label — the P(FAIL) score that threshold decisions are built on.
Example: `p_fail_test = logit.predict_proba(X_test)[:, 1]`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.pipeline — predict_proba(X)[:, 1]"
Center: one large diagram illustrating a fitted model box taking in a row of feature cells and emitting, for each part, a two-segment horizontal probability bar — a teal PASS segment and a coral FAIL segment summing to 100% — with one bar highlighted reading "P(FAIL) = 0.72"; the [:, 1] step is drawn as a hand picking the coral (FAIL) column only.
Below the diagram: a small code snippet box rendering exactly this code: p_fail_test = logit.predict_proba(X_test)[:, 1]
Caption strip at the bottom: Output class probabilities per part, not just a hard PASS/FAIL label.
```

## 16. `feature_importances_` — sklearn.ensemble

What it does: After fitting, a score per feature telling how much the forest relied on it when splitting PASS from FAIL.
Example: `imp = rf.named_steps["model"].feature_importances_`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.ensemble — .feature_importances_"
Center: one large diagram illustrating the fitted forest of trees opened up, with all 590 feature cards feeding into a sorting tray that outputs a horizontal bar ranking: a few bars slightly longer (feature_51, feature_130...) but none dominant, labeled "top score only ~0.026 of 1.0"; each bar's length equals how often that feature was used for splits.
Below the diagram: a small code snippet box rendering exactly this code: imp = rf.named_steps["model"].feature_importances_
Caption strip at the bottom: After fitting: one importance score per feature — how much the model used it.
```

## 17. `argsort` — numpy

What it does: Returns the indices that would sort an array — used here to rank features from most to least important.
Example: `top = np.argsort(imp)[::-1][:15]`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.argsort(imp)[::-1][:15]"
Center: one large diagram illustrating a row of importance bars in scrambled original order, each carrying a small index tag; arrows lift the tags and re-rank them from longest bar (highest importance) down to shortest, with the first 15 positions of the re-ranked list boxed and labeled "top 15 indices".
Below the diagram: a small code snippet box rendering exactly this code: top = np.argsort(imp)[::-1][:15]
Caption strip at the bottom: Get the positions that would sort an array — here, the indexes of the most important features.
```

## 18. `barh` — matplotlib.pyplot

What it does: Draws a horizontal bar chart — used to display the top-15 feature importances.
Example: `ax.barh([f"feature_{i + 1}" for i in top][::-1], imp[top][::-1], color="#2a9d8f")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib.pyplot — ax.barh(labels, widths)"
Center: one large diagram illustrating horizontal bars growing rightward from a left axis, each labeled with a feature name (feature_51, feature_130, ...) on the left and its length equal to its importance value; the longest bar sits at the top, showing a ranked top-15 importance chart.
Below the diagram: a small code snippet box rendering exactly this code: ax.barh(feature_names, imp[top], color="#2a9d8f")
Caption strip at the bottom: Draw a horizontal bar chart — one bar per item, width = value.
```

## 19. `where` — numpy

What it does: Picks values element-by-element from one of two arrays depending on a boolean condition — used to simulate sensor readings that differ between pass and fail units.
Example: `reading = np.where(is_fail, rng.normal(10.45, .15, n), rng.normal(10.00, .15, n))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.where(cond, a, b)"
Center: one large diagram illustrating a vertical column of toggle switches labeled with True/False; each switch routes its row to one of two value trays — tray A (coral, used when the condition is True) or tray B (teal, when False) — and the chosen value slides into the output row, one pick per row.
Below the diagram: a small code snippet box rendering exactly this code: reading = np.where(is_fail, rng.normal(10.45, .15, n), rng.normal(10.00, .15, n))
Caption strip at the bottom: For each element, choose from array A if the condition is True, else from array B.
```

## 20. `arange` — numpy

What it does: Makes an array of evenly spaced integers (or floats) between a start and a stop — here, the list of candidate defect counts k.
Example: `ks = np.arange(0, 6)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.arange(start, stop)"
Center: one large diagram illustrating a number line from 0 to 6 with evenly spaced dots stamped at each integer 0, 1, 2, 3, 4, 5; brackets above show "start = 0" and "stop = 6 (not included)" with the step gap between dots labeled "1".
Below the diagram: a small code snippet box rendering exactly this code: ks = np.arange(0, 6)
Caption strip at the bottom: Generate evenly spaced integers from start up to (not including) stop.
```

## 21. `math.comb` — math

What it does: Counts the number of ways to choose k items out of n ("n choose k") — the combinatorial factor in the binomial formula for pass/fail lots.
Example: `math.comb(n_lot, int(k)) * p**k * (1 - p) ** (n_lot - k)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — math.comb(n, k)"
Center: one large diagram illustrating a tray of n = 10 round parts with k = 2 of them circled in coral; beside it, several small groupings of 2 circled parts drawn out, with a counter badge reading "C(10,2) = 45 ways to choose", showing that the function counts combinations without listing them all.
Below the diagram: a small code snippet box rendering exactly this code: math.comb(n_lot, int(k)) * p**k * (1 - p) ** (n_lot - k)
Caption strip at the bottom: Count how many ways k items can be chosen from n — the "n choose k" factor.
```

## 22. `exp` — numpy

What it does: The exponential function e^x applied element-wise — the ingredient of the logistic (sigmoid) curve 1/(1+e^-z).
Example: `sig = 1 / (1 + np.exp(-z))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.exp(x)"
Center: one large diagram illustrating the exponential curve e^x as a gently rising swoosh over an x-axis, with a side panel showing the same curve flipped and folded into the classic S-shaped logistic curve labeled "1 / (1 + e^-z)" — showing exp as the engine inside the sigmoid used for classification.
Below the diagram: a small code snippet box rendering exactly this code: sig = 1 / (1 + np.exp(-z))
Caption strip at the bottom: Raise e to the power of x, element-wise — the sigmoid curve's building block.
```

## 23. `argmin` — numpy

What it does: Returns the index of the smallest value in an array — used to find the decision cutoff where the failure probability is closest to 0.5.
Example: `x_star = xs[np.argmin(np.abs(post_fail - 0.5))]`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.argmin(arr)"
Center: one large diagram illustrating a row of values drawn as bars of different heights, with a magnifying glass hovering over the single shortest bar; the bar carries its index tag "position 217" highlighted in coral, and a label reads "argmin returns the index, not the value".
Below the diagram: a small code snippet box rendering exactly this code: x_star = xs[np.argmin(np.abs(post_fail - 0.5))]
Caption strip at the bottom: Find the position (index) of the smallest value in an array.
```

## 24. `set_ylim` — matplotlib.pyplot

What it does: Fixes the vertical range shown on a plot's y-axis — used to pin the probability axis at 0 to 1.
Example: `axes[1].set_ylim(-0.05, 1.05)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib.pyplot — ax.set_ylim(lo, hi)"
Center: one large diagram illustrating a mini chart with a vertical axis; two hands (or clamp icons) grip the top and bottom of the y-axis and stretch it so the ticks read exactly -0.05 at the bottom and 1.05 at the top, with a note "probabilities always shown on a fixed 0-to-1 scale".
Below the diagram: a small code snippet box rendering exactly this code: axes[1].set_ylim(-0.05, 1.05)
Caption strip at the bottom: Pin the y-axis to an exact range, from lo to hi.
```

---
**25 new functions introduced in this module.**

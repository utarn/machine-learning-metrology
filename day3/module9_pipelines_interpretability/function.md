# Function Reference — Module 9: Pipelines & Interpretability

Only functions introduced for the first time in this module are listed here, in the order you will meet them. Functions already covered in earlier modules are not repeated — look them up in the earlier modules' `function.md`.

## 1. `z.read(name)` — python (zipfile)

What it does: Reads one file out of an opened zip archive and returns its raw bytes — here it pulls `secom.data` out of `secom.zip` so the CSV reader can work on it without ever unpacking to disk.
Example: `pl.read_csv(io.BytesIO(z.read("secom.data")), separator=" ")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python zipfile — z.read(name)"
Center: one large diagram illustrating an open flat zip-archive folder icon containing three stacked file cards labeled "secom.data", "secom_labels.data", "readme"; a coral hand arrow pulls exactly one card (the one named "secom.data") out of the archive; the card dissolves into a stream of small bytes (0s and 1s) flowing into a rounded box labeled "raw bytes"; a small tag notes "the other files stay inside the zip".
Below the diagram: a small code snippet box rendering exactly this code: pl.read_csv(io.BytesIO(z.read("secom.data")), separator=" ")
Caption strip at the bottom: Extracts one member file from a zip archive as raw bytes, without unpacking anything to disk.
```

## 2. `Pipeline.steps / pipeline.named_steps["name"]` — sklearn.pipeline

What it does: Inspects the inside of a fitted pipeline: `.steps` lists every stage as `(name, step)` pairs, and `named_steps["name"]` hands you one stage back by its name — here used to pull out the trained model and imputer so SHAP can explain them.
Example: `model = pipe_xgb.named_steps["model"]`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.pipeline — Pipeline.steps / pipeline.named_steps[\"name\"]"
Center: one large diagram illustrating a horizontal conveyor belt of three connected boxes with name tags: "impute", "scale", "model"; above it a list panel labeled ".steps" shows the same three boxes written as name-and-step pairs; a coral magnifying lens hovers over the last box and lifts its lid open, with a label "named_steps[\"model\"]" pointing inside to reveal the trained model gear; arrows show both routes reach the same internals.
Below the diagram: a small code snippet box rendering exactly this code: model = pipe_xgb.named_steps["model"]
Caption strip at the bottom: Opens up a pipeline to inspect its stages — list them all with .steps, or grab one by name with named_steps.
```

## 3. `SelectKBest(f_classif, k=20)` — sklearn.feature_selection

What it does: Keeps only the k most informative features and drops the rest; placed inside the pipeline, it re-ranks and re-selects fresh on every cross-validation fold, so feature selection never leaks the test fold's information.
Example: `("select", SelectKBest(f_classif, k=20)),`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.feature_selection — SelectKBest(f_classif, k=20)"
Center: one large diagram illustrating a wide column of 590 small feature bars at the top narrowing through a funnel shape; the bars are ranked and only the top 20 tallest teal bars pass through the funnel's narrow slot into a small tray labeled "k = 20 kept", while greyed-out bars pile into a discard bin labeled "dropped"; a circular refresh icon with the note "re-selects inside every CV fold" sits beside the funnel.
Below the diagram: a small code snippet box rendering exactly this code: ("select", SelectKBest(f_classif, k=20)),
Caption strip at the bottom: A filter that keeps only the top-k most informative features — and re-chooses them fresh in every fold.
```

## 4. `f_classif` — sklearn.feature_selection

What it does: The scoring function SelectKBest consults: for each feature it runs an ANOVA F-test measuring how strongly the feature values separate the two classes (PASS vs FAIL), producing the F-score used to rank features.
Example: `SelectKBest(f_classif, k=20)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.feature_selection — f_classif"
Center: one large diagram illustrating a leaderboard of four small feature rows; each row shows two dot clouds side by side — teal dots labeled "PASS" and coral dots labeled "FAIL" — plotted over the feature's value axis; the top row's two clouds sit far apart with a big gap (a high F-score badge "F = high"), the bottom row's clouds overlap heavily (a low F-score badge); an arrow from the leaderboard to a ranked score column on the right labeled "F-score per feature".
Below the diagram: a small code snippet box rendering exactly this code: SelectKBest(f_classif, k=20)
Caption strip at the bottom: Scores each feature by how well it separates the classes — the ranking rule behind SelectKBest.
```

## 5. `shap.TreeExplainer(model)` — shap

What it does: Builds an explainer tuned for tree models (like XGBoost): it can compute, for every prediction, how much each feature pushed the output up or down.
Example: `explainer = shap.TreeExplainer(model)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "shap — shap.TreeExplainer(model)"
Center: one large diagram illustrating a small flat decision tree (nodes and branches) with a prediction bulb at its base; a coral wrench-and-magnifier icon labeled "explainer" is attached to the tree's side; from each leaf path, thin dark slate blue arrows fan out to a row of small feature tags, each tagged with a plus or minus contribution marker; a tag reads "knows how to read tree models".
Below the diagram: a small code snippet box rendering exactly this code: explainer = shap.TreeExplainer(model)
Caption strip at the bottom: Wraps a tree model in an explainer that can attribute every prediction to individual features.
```

## 6. `explainer(Zte)` — shap

What it does: Calling the explainer on a batch of rows computes their SHAP values and returns one `Explanation` object holding every feature's contribution to every row's prediction.
Example: `sv = explainer(Zte.iloc[:200])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "shap — explainer(Zte)"
Center: one large diagram illustrating a batch of data rows (a small table of 200 rows drawn as stacked horizontal strips) entering a coral machine labeled "explainer" from the left; out of the right side comes a neat 2-D grid of small plus and minus cells labeled "Explanation object: SHAP values per row x per feature"; teal cells tilt up (push prediction up), coral cells tilt down (push it down); a tag notes "200 rows in, an explanation for each out".
Below the diagram: a small code snippet box rendering exactly this code: sv = explainer(Zte.iloc[:200])
Caption strip at the bottom: Computes SHAP contributions for a batch of rows, returned as one Explanation object.
```

## 7. `sv.shape` — shap

What it does: The size of the SHAP results — `(n_rows, n_features)` — a quick sanity check that you got one contribution value per row per feature (here 200 rows x 590 features).
Example: `print(sv.shape)  # (200, 590)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "shap — sv.shape"
Center: one large diagram illustrating a 2-D grid of small cells (rows drawn in dark slate blue, columns in teal) with a horizontal double-headed arrow under it labeled "590 features" and a vertical double-headed arrow beside it labeled "200 rows"; a corner tag shows the pair "(200, 590)" as the single answer; a small ruler icon emphasizes "measuring the shape, not the values".
Below the diagram: a small code snippet box rendering exactly this code: print(sv.shape)  # (200, 590)
Caption strip at the bottom: Reports the SHAP result's dimensions — one row per sample, one column per feature.
```

## 8. `explainer.expected_value` — shap

What it does: The model's baseline output — the average prediction before any feature pushes are applied; every waterfall explanation starts from this base value.
Example: `round(float(explainer.expected_value), 3)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "shap — explainer.expected_value"
Center: one large diagram illustrating a single horizontal number-line gauge with a bold dark slate blue marker at its center labeled "base value (E[f(X)])"; on either side, faint ghost arrows labeled "feature pushes" point away from the marker but are drawn translucent, emphasizing that no push has been applied yet; a small flat-avatar crowd icon above the marker with the note "the average model output over the data".
Below the diagram: a small code snippet box rendering exactly this code: round(float(explainer.expected_value), 3)
Caption strip at the bottom: The model's baseline output — the starting point every SHAP explanation pushes off from.
```

## 9. `plt.figure()` — matplotlib.pyplot

What it does: Opens a brand-new, empty figure canvas — used here so each SHAP chart gets its own fresh plot instead of drawing into the previous one.
Example: `plt.figure()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib.pyplot — plt.figure()"
Center: one large diagram illustrating an easel holding a blank white canvas with a thin dark slate blue border; to its left, a faded finished chart on a second easel; a coral paint-roller or "new sheet" arrow moves from the old chart to the fresh blank canvas; a small tag on the blank canvas reads "empty canvas ready to draw on".
Below the diagram: a small code snippet box rendering exactly this code: plt.figure()
Caption strip at the bottom: Starts a fresh empty figure so the next chart gets its own canvas.
```

## 10. `shap.plots.beeswarm(sv, max_display=8)` — shap

What it does: Draws a dot-cloud summary across all rows: one row per feature, each dot is one sample, horizontal position is that feature's SHAP push, and dot color shows whether the feature's value was high or low — the global "which features matter" view.
Example: `shap.plots.beeswarm(sv, max_display=8, show=False)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "shap — shap.plots.beeswarm(sv, max_display=8)"
Center: one large diagram illustrating a horizontal beeswarm chart: eight feature-name labels on the left axis, most important at the top; along each row a swarm of small round dots spreads horizontally from a central zero line — dots pushed right in teal and left in coral; each dot's shade varies from light to dark with a small two-color colorbar legend labeled "feature value: low to high"; the top row's swarm is widest with a tag "biggest average impact".
Below the diagram: a small code snippet box rendering exactly this code: shap.plots.beeswarm(sv, max_display=8, show=False)
Caption strip at the bottom: One dot per sample per feature — a swarm map of which features push predictions up or down the most.
```

## 11. `plt.gcf().set_size_inches(9, 4.5)` — matplotlib.pyplot

What it does: Gets the Current Figure (`gcf`) — whichever figure matplotlib is drawing into right now — and resizes it; used here to reshape the figure after SHAP has already drawn its chart into it.
Example: `plt.gcf().set_size_inches(9, 4.5)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib.pyplot — plt.gcf().set_size_inches(9, 4.5)"
Center: one large diagram illustrating a chart canvas with corner drag handles like a design tool; a coral cursor hand drags the bottom-right corner so a dashed "before" outline (small) expands to a solid "after" outline (wide rectangle, 9 x 4.5 proportion marked); a dark slate blue spotlight highlights the canvas labeled "the current figure"; a small tag reads "gcf = get current figure".
Below the diagram: a small code snippet box rendering exactly this code: plt.gcf().set_size_inches(9, 4.5)
Caption strip at the bottom: Grabs whichever figure is currently active and stretches it to the size you want.
```

## 12. `plt.title("...")` — matplotlib.pyplot

What it does: Puts a title text on top of the current figure — here naming what the SHAP beeswarm shows.
Example: `plt.title("SHAP beeswarm - top drivers of FAIL")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib.pyplot — plt.title(\"...\")"
Center: one large diagram illustrating a small chart panel (a simple line and dot plot) with a coral banner rectangle being lowered onto its top edge by two small hands; the banner carries bold dark slate blue text reading "SHAP beeswarm - top drivers of FAIL"; dashed alignment guides show the banner snapping centered above the chart.
Below the diagram: a small code snippet box rendering exactly this code: plt.title("SHAP beeswarm - top drivers of FAIL")
Caption strip at the bottom: Pins a title banner onto the top of the current chart.
```

## 13. `shap.plots.waterfall(sv[i_fail], max_display=8)` — shap

What it does: Explains ONE row's prediction: a horizontal bar starts at the base value, then each feature's push (red raising it, blue lowering it) stacks up left to right until the bar reaches that row's final prediction.
Example: `shap.plots.waterfall(sv[i_fail], max_display=8, show=False)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "shap — shap.plots.waterfall(sv[i_fail], max_display=8)"
Center: one large diagram illustrating a single-row explanation: one horizontal stacked bar starting at a block labeled "base value"; feature segments join it one after another like stepping stones — coral segments pushing the bar's endpoint up and teal segments pulling it down, each with a small feature-name tag; the bar ends at a block labeled "f(x) = this row's prediction"; a magnifier badge above reads "one sample, one story".
Below the diagram: a small code snippet box rendering exactly this code: shap.plots.waterfall(sv[i_fail], max_display=8, show=False)
Caption strip at the bottom: Walks one prediction back to the baseline, showing each feature's push along the way.
```

## 14. `sv.values` — shap

What it does: The raw SHAP numbers behind the Explanation object as a plain 2-D array — one signed value per row per feature — so you can do your own math, like averaging |SHAP| per feature to rank importance.
Example: `np.abs(sv.values).mean(axis=0)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "shap — sv.values"
Center: one large diagram illustrating a 2-D grid of small cells, each cell tinted coral (positive) or teal (negative) by its sign, with a few cells showing tiny numbers like +0.4 and -0.2; a coral funnel arrow collapses the grid column-wise into a single short row of bars below labeled "mean |SHAP| per feature", with the tallest bar highlighted and a crown tag "top feature"; a side note reads "the plain numbers behind the Explanation".
Below the diagram: a small code snippet box rendering exactly this code: np.abs(sv.values).mean(axis=0)
Caption strip at the bottom: The raw signed SHAP numbers as an array — ready for your own math like ranking feature importance.
```

## 15. `shap.plots.scatter(sv[:, f], color=sv)` — shap

What it does: Plots one feature's value (x-axis) against its SHAP contribution (y-axis) for every row, with points colored by another feature — revealing HOW a sensor drives the prediction (e.g. monotone, thresholded, or interaction effects).
Example: `shap.plots.scatter(sv[:, top_feature], color=sv, show=False)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "shap — shap.plots.scatter(sv[:, f], color=sv)"
Center: one large diagram illustrating a scatter chart: the x-axis labeled "feature value" and the y-axis labeled "SHAP value for this feature"; a cloud of round dots trends upward from lower-left to upper-right with a thin trend line through them; dots are colored along a teal-to-coral colorbar on the right labeled "another feature's value", showing an interaction pattern; one dot is circled with the tag "one row = one dot".
Below the diagram: a small code snippet box rendering exactly this code: shap.plots.scatter(sv[:, top_feature], color=sv, show=False)
Caption strip at the bottom: Feature value vs its SHAP effect for every row — shows how one sensor actually drives predictions.
```

---
New functions introduced in this module: **15**.

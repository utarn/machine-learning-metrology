# Function Reference — Module 2: Feature Engineering

Only functions introduced for the first time in this module are listed here, in the order you will meet them. Functions already covered in earlier modules are not repeated — look them up in the earlier modules' `function.md`.

## 1. `.columns` — polars

What it does: Lists the column names of the table.
Example: `print(ccpp.shape, "| columns:", ccpp.columns)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.columns"
Center: one large diagram illustrating a data table whose column headers lift off as a horizontal strip of name tags (AT, V, AP, RH, PE) held together like a key ring — columns gives you just the names, without the data.
Below the diagram: a small code snippet box rendering exactly this code: print(ccpp.shape, "| columns:", ccpp.columns)
Caption strip at the bottom: ".columns lists the column names of the table."
```

## 2. `rng.random(n)` — numpy

What it does: Draws n random numbers between 0 and 1 (here: to decide which cells become missing).
Example: `pl.Series(rng.random(len(aq))) < 0.10`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — rng.random(n)"
Center: one large diagram illustrating a dice-thrower hopper dropping a stream of small chips onto a 0-to-1 number line, the chips scattering densely near neither end but uniformly across the whole line; a coral threshold line at 0.10 catches the few chips below it — uniform random draws between 0 and 1.
Below the diagram: a small code snippet box rendering exactly this code: pl.Series(rng.random(len(aq))) < 0.10
Caption strip at the bottom: "rng.random(n) draws n uniform random numbers between 0 and 1."
```

## 3. `pl.when(...).then(...).otherwise(...)` — polars

What it does: An if/else expression applied to every row: if the test holds give one value, otherwise another.
Example: `pl.when(pl.Series(rng.random(len(aq))) < 0.10).then(None).otherwise(pl.col("T"))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — pl.when(...).then(...).otherwise(...)"
Center: one large diagram illustrating a Y-shaped fork in a conveyor belt: a condition sign (dice < 0.10) decides at the junction; chips meeting the test take the upper branch into a tray labelled then(None) becoming empty dashed cells, all others take the lower branch labelled otherwise keeping their original value — a row-by-row if/else.
Below the diagram: a small code snippet box rendering exactly this code: pl.when(pl.Series(rng.random(len(aq))) < 0.10).then(None).otherwise(pl.col("T"))
Caption strip at the bottom: "when/then/otherwise is an if/else applied to every row."
```

## 4. `pl.Series("name", values)` — polars

What it does: Creates a named one-dimensional column of values from a numpy array or list.
Example: `pl.Series("AT_x_RH", X_train["AT"].to_numpy() * X_train["RH"].to_numpy())`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — pl.Series(\"name\", values)"
Center: one large diagram illustrating a naked row of computed numbers on the left entering a labeling machine; it exits on the right as a tidy single column strip wearing a name tag reading AT_x_RH on top — raw values become a named column object ready to insert into a table.
Below the diagram: a small code snippet box rendering exactly this code: pl.Series("AT_x_RH", X_train["AT"].to_numpy() * X_train["RH"].to_numpy())
Caption strip at the bottom: "pl.Series() creates a named column from an array of values."
```

## 5. `SimpleImputer(strategy="median")` — sklearn.impute

What it does: Creates a filler that replaces missing values with a learned summary value (here the median).
Example: `imp = SimpleImputer(strategy="median").fit(pdf[["T"]])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — SimpleImputer(strategy=\"median\")"
Center: one large diagram illustrating a column of cells with grey hole-shaped gaps; an imputer machine with a plaster/patch dispenser stands beside it, holding a marker line labelled median ready to plug every hole — the machine learns the fill value from the data itself.
Below the diagram: a small code snippet box rendering exactly this code: imp = SimpleImputer(strategy="median").fit(pdf[["T"]])
Caption strip at the bottom: "SimpleImputer fills missing values with a learned statistic."
```

## 6. `fit()` (learn from data) — sklearn

What it does: The universal sklearn method that learns from data — the transformer (or model) studies the training data and stores what it learned.
Example: `imp = SimpleImputer(strategy="median").fit(pdf[["T"]])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — .fit(X, y)"
Center: one large diagram illustrating a student machine with an open notebook brain; training data flows in through an input arrow, the machine studies it, and small learned facts (a median marker, a mean marker) file themselves into slots inside its head — fit means "learn from this data, remember it".
Below the diagram: a small code snippet box rendering exactly this code: imp = SimpleImputer(strategy="median").fit(pdf[["T"]])
Caption strip at the bottom: "fit() learns from the data and remembers what it learned."
```

## 7. `transform()` (apply what was learned) — sklearn

What it does: The universal sklearn method that applies what fit() learned to data — filling, scaling, or encoding without re-learning.
Example: `filled = imp.transform(pdf[["T"]])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — .transform(X)"
Center: one large diagram illustrating a processing machine whose settings panel is already set (dials locked in place, tagged "learned by fit"); new data flows in one side and comes out the other converted — gaps filled with the learned median — while the settings stay untouched; apply, don't re-learn.
Below the diagram: a small code snippet box rendering exactly this code: filled = imp.transform(pdf[["T"]])
Caption strip at the bottom: "transform() applies what fit() learned to the data."
```

## 8. `.statistics_` — sklearn.impute

What it does: The values the imputer learned — the fill statistic it will use for each column.
Example: `imp.statistics_[0]`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — imputer.statistics_"
Center: one large diagram illustrating the imputer machine opened to show its memory compartment: one small plaque per input column displaying the learned fill value (e.g. the median 24.4 for column T), with the underscore-suffixed name statistics_ on a label reading "learned attribute" — what fit() left behind.
Below the diagram: a small code snippet box rendering exactly this code: imp.statistics_[0]
Caption strip at the bottom: "statistics_ holds the fill values the imputer learned."
```

## 9. `np.isnan(...)` — numpy

What it does: Checks element by element which values are NaN (missing).
Example: `np.isnan(filled).sum()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.isnan(array)"
Center: one large diagram illustrating an array of cells passing under a detector scanner; cells containing real numbers stay grey while cells containing the NaN symbol light up coral and project as True chips in a matching output array — a value-by-value missingness test.
Below the diagram: a small code snippet box rendering exactly this code: np.isnan(filled).sum()
Caption strip at the bottom: "np.isnan() flags which elements are NaN (missing)."
```

## 10. `.sum()` (array method) — numpy

What it does: Adds up array values — here it counts how many True flags there are.
Example: `np.isnan(filled).sum()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — arr.sum()"
Center: one large diagram illustrating a row of True/False chips where each True chip weighs 1 and each False weighs 0; all chips slide onto a scale pan and the readout shows the total count — adding up booleans counts how many.
Below the diagram: a small code snippet box rendering exactly this code: np.isnan(filled).sum()
Caption strip at the bottom: "sum() adds up array values — True flags count as 1."
```

## 11. `StandardScaler()` — sklearn.preprocessing

What it does: Rescales each column to mean 0 and standard deviation 1 so features become comparable.
Example: `scaler = StandardScaler().fit(X_train)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — StandardScaler()"
Center: one large diagram illustrating four columns of dots at wildly different scales (ranges 0-40, 0-100000, 990-1030, 25-100) entering a calibration press; they exit all centered on a shared zero line with the same width, each labelled mean 0, std 1 — different units squeezed onto one common scale.
Below the diagram: a small code snippet box rendering exactly this code: scaler = StandardScaler().fit(X_train)
Caption strip at the bottom: "StandardScaler rescales each column to mean 0, std 1."
```

## 12. `.to_numpy()` — polars

What it does: Converts a Polars column to a numpy array so plain math and sklearn can use it.
Example: `X_train["AT"].to_numpy() * X_train["RH"].to_numpy()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — series.to_numpy()"
Center: one large diagram illustrating a named table column strip entering a gateway labelled to_numpy and coming out as an unlabeled, plain row of raw numeric cells with a small numpy gear badge — the column sheds its table identity to become raw math material.
Below the diagram: a small code snippet box rendering exactly this code: X_train["AT"].to_numpy() * X_train["RH"].to_numpy()
Caption strip at the bottom: "to_numpy() converts a Polars column into a raw numpy array."
```

## 13. `range(n)` — python

What it does: Counts 0, 1, 2, ... up to n-1 — the loop counter for "do this n times".
Example: `[X_train_s[:, i] for i in range(4)]`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — range(n)"
Center: one large diagram illustrating a row of stepping stones numbered 0, 1, 2, 3 appearing one after another with a hopping arrow visiting each in order and stopping before a fence labelled n — the sequence runs from 0 up to but not including n.
Below the diagram: a small code snippet box rendering exactly this code: [X_train_s[:, i] for i in range(4)]
Caption strip at the bottom: "range(n) counts 0, 1, ... n-1 — the loop counter."
```

## 14. `ax.grid(...)` — matplotlib.pyplot

What it does: Adds background gridlines to a plot so values are easier to read.
Example: `ax.grid(axis="y", alpha=0.3)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib — ax.grid(...)"
Center: one large diagram illustrating a plain chart panel on the left receiving faint horizontal ruled lines laid over it like graph paper (light, semi-transparent, labelled alpha 0.3) — the same panel on the right shown before, bare and harder to read against.
Below the diagram: a small code snippet box rendering exactly this code: ax.grid(axis="y", alpha=0.3)
Caption strip at the bottom: "grid() adds faint background gridlines for easier reading."
```

## 15. `OneHotEncoder()` — sklearn.preprocessing

What it does: Turns one category column into one 0/1 column per category.
Example: `enc = OneHotEncoder(sparse_output=False).fit(toy[["sensor_id"]].to_pandas())`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — OneHotEncoder()"
Center: one large diagram illustrating a single category column with values S1, S2, S3 fanning out like a dealer's cards into three parallel 0/1 columns headed sensor_id_S1, sensor_id_S2, sensor_id_S3, where each row lights up exactly one 1 among zeros — one category hot at a time.
Below the diagram: a small code snippet box rendering exactly this code: enc = OneHotEncoder(sparse_output=False).fit(toy[["sensor_id"]].to_pandas())
Caption strip at the bottom: "OneHotEncoder turns one category column into one 0/1 column per category."
```

## 16. `pl.DataFrame({...})` — polars

What it does: Builds a Polars table by hand from a dict of column names and values.
Example: `toy = pl.DataFrame({"sensor_id": ["S1", "S2", "S3"], "mv": [12.1, 11.8, 13.0]})`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — pl.DataFrame({...})"
Center: one large diagram illustrating loose named value lists (a list of sensor_id strings and a list of mv numbers) being stood upright side by side and joined into a small table with proper column headers — a table assembled by hand from raw lists.
Below the diagram: a small code snippet box rendering exactly this code: toy = pl.DataFrame({"sensor_id": ["S1", "S2", "S3"], "mv": [12.1, 11.8, 13.0]})
Caption strip at the bottom: "pl.DataFrame() builds a table by hand from named columns."
```

## 17. `pd.DataFrame(...)` — pandas

What it does: Builds a pandas table — used here to wrap encoder output and attach column names.
Example: `pd.DataFrame(enc.transform(...), columns=enc.get_feature_names_out())`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "pandas — pd.DataFrame(...)"
Center: one large diagram illustrating a bare grid of 0/1 numbers on the left receiving a header strip of column-name tags from above (sensor_id_S1, sensor_id_S2, sensor_id_S3) and becoming a proper labeled pandas table with a small panda badge in the corner — raw numbers dressed as a named table.
Below the diagram: a small code snippet box rendering exactly this code: pd.DataFrame(enc.transform(...), columns=enc.get_feature_names_out())
Caption strip at the bottom: "pd.DataFrame() builds a pandas table, optionally with named columns."
```

## 18. `.get_feature_names_out()` — sklearn.preprocessing

What it does: Returns the names of the columns a transformer generated.
Example: `poly.get_feature_names_out(["AT", "V", "AP", "RH"])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — transformer.get_feature_names_out()"
Center: one large diagram illustrating a transformer machine that widened a 4-column table into a 15-column matrix; a dispenser on the machine's output slot prints one name tag per new column (AT, V, AP, RH, AT V, AT AP, ...) laid out in a row — ask the machine what it called its outputs.
Below the diagram: a small code snippet box rendering exactly this code: poly.get_feature_names_out(["AT", "V", "AP", "RH"])
Caption strip at the bottom: "get_feature_names_out() returns the generated columns' names."
```

## 19. `pl.concat(..., how="horizontal")` — polars

What it does: Glues tables together side by side, column-wise.
Example: `pl.concat([toy, encoded], how="horizontal")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — pl.concat([a, b], how=\"horizontal\")"
Center: one large diagram illustrating two tables of equal height sliding toward each other horizontally and clicking together like puzzle halves into one wider table — the original columns on the left, the new encoded columns attached on the right, row-for-row.
Below the diagram: a small code snippet box rendering exactly this code: pl.concat([toy, encoded], how="horizontal")
Caption strip at the bottom: "concat(how=\"horizontal\") glues tables together side by side."
```

## 20. `PolynomialFeatures(degree=2)` — sklearn.preprocessing

What it does: Generates new columns for products of features — x squared, x times y, and so on.
Example: `poly = PolynomialFeatures(degree=2, include_bias=False)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — PolynomialFeatures(degree=2)"
Center: one large diagram illustrating two input columns x and y entering a multiplier chamber that outputs a wider set of columns labelled x, y, x², xy, y² — every pairwise product of the inputs appearing as fresh columns; a degree dial set to 2 on the machine.
Below the diagram: a small code snippet box rendering exactly this code: poly = PolynomialFeatures(degree=2, include_bias=False)
Caption strip at the bottom: "PolynomialFeatures adds product columns like x² and x·y."
```

## 21. `fit_transform()` (learn + apply in one step) — sklearn

What it does: Learns from the data AND applies the learned transformation in a single call.
Example: `X_poly = poly.fit_transform(X_train[:5])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — .fit_transform(X)"
Center: one large diagram illustrating a machine shown as one compact unit combining a study phase and an apply phase: data enters once, an inner brain icon briefly learns (small dial icons set themselves), and the transformed output immediately flows out the far side — two arrows (fit, transform) fused into one bent arrow.
Below the diagram: a small code snippet box rendering exactly this code: X_poly = poly.fit_transform(X_train[:5])
Caption strip at the bottom: "fit_transform() learns from the data and applies it in one step."
```

## 22. `np.log(...)` — numpy

What it does: The natural logarithm, element by element (used in the dew-point physics formula).
Example: `gamma = np.log(rh / 100) + a * at / (b + at)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.log(array)"
Center: one large diagram illustrating a rising exponential curve with values on the left axis; the log operation shown as a ladder laid along the curve compressing big multiplicative steps into even additive steps — points far apart up the curve become evenly spaced after log; a ln symbol above a row of transformed cells.
Below the diagram: a small code snippet box rendering exactly this code: gamma = np.log(rh / 100) + a * at / (b + at)
Caption strip at the bottom: "np.log() takes the natural logarithm of every element."
```

## 23. `Pipeline([...])` — sklearn.pipeline

What it does: Chains processing steps and a model into one object so they always run in order.
Example: `model = Pipeline([("scaler", StandardScaler()), ("poly", PolynomialFeatures(...)), ("ridge", Ridge(alpha=1.0))])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — Pipeline([...])"
Center: one large diagram illustrating three machine boxes linked by arrows on one assembly line, each with a name tag: scaler, then poly, then ridge (the final model box); raw data enters the left end and a prediction-ready model comes out the right — the whole chain behaves as one object.
Below the diagram: a small code snippet box rendering exactly this code: model = Pipeline([("scaler", StandardScaler()), ("poly", PolynomialFeatures(...)), ("ridge", Ridge(alpha=1.0))])
Caption strip at the bottom: "Pipeline chains steps and a model into one ordered object."
```

## 24. `Ridge(alpha=...)` — sklearn.linear_model

What it does: Linear regression with a penalty that shrinks coefficients — tames wild features.
Example: `("ridge", Ridge(alpha=1.0))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — Ridge(alpha=...)"
Center: one large diagram illustrating a bar chart of coefficient bars being pulled gently toward zero by coiled springs attached to a zero wall; a dial labelled alpha controls the spring strength — larger alpha pulls the bars shorter, but none reach exactly zero.
Below the diagram: a small code snippet box rendering exactly this code: ("ridge", Ridge(alpha=1.0))
Caption strip at the bottom: "Ridge adds an L2 penalty that shrinks coefficients toward zero."
```

## 25. `score()` (evaluate a model) — sklearn

What it does: The universal sklearn method that evaluates a fitted model — for regression it returns the R² score.
Example: `model.score(X_test, y_test)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — .score(X, y)"
Center: one large diagram illustrating a fitted model box with predictions streaming out and being compared against the true answer chips on a grading gauge; the gauge needle rests near 1.0 and displays the R² value in a badge — score() grades the model on given data.
Below the diagram: a small code snippet box rendering exactly this code: model.score(X_test, y_test)
Caption strip at the bottom: "score() evaluates the fitted model — R² for regression."
```

## 26. `ColumnTransformer([...])` — sklearn.compose

What it does: Applies different transformers to different columns of the same table.
Example: `prep = ColumnTransformer([("sensor", StandardScaler(), [...]), ("ref_with_missing", Pipeline([...]), [...])])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — ColumnTransformer([...])"
Center: one large diagram illustrating a table whose columns are split into colored groups at a routing switchboard: one group of sensor columns routed to a scaler machine, another group routed through an impute-then-scale mini pipeline, all outputs merging at the far end into one combined matrix — different treatment per column group, one result.
Below the diagram: a small code snippet box rendering exactly this code: prep = ColumnTransformer([("sensor", StandardScaler(), [...]), ("ref_with_missing", Pipeline([...]), [...])])
Caption strip at the bottom: "ColumnTransformer routes different columns through different transformers."
```

## 27. `LinearRegression()` — sklearn.linear_model

What it does: Plain ordinary least-squares regression — the straight-line baseline model.
Example: `baseline = LinearRegression().fit(X_train, y_train)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — LinearRegression()"
Center: one large diagram illustrating a scatter of dots with a straight teal best-fit line threaded through them, small vertical error segments shown as faint coral stubs between dots and line; the line's slope and crossing are the knobs being adjusted to minimize the stubs — the simplest fitting machine.
Below the diagram: a small code snippet box rendering exactly this code: baseline = LinearRegression().fit(X_train, y_train)
Caption strip at the bottom: "LinearRegression fits the best straight line through the data."
```

## 28. `GridSearchCV(...)` — sklearn.model_selection

What it does: Tries every combination of settings with cross-validation and keeps the best one.
Example: `search = GridSearchCV(pipe_poly, param_grid, cv=5)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — GridSearchCV(model, param_grid, cv)"
Center: one large diagram illustrating a grid of candidate setting cells (alpha values across a row), each cell tried out on a small folding fan of 5 cross-validation segments; each cell shows its score bar and the winning cell is highlighted with a coral crown — an automatic tournament over settings.
Below the diagram: a small code snippet box rendering exactly this code: search = GridSearchCV(pipe_poly, param_grid, cv=5)
Caption strip at the bottom: "GridSearchCV tries every setting combination and keeps the best."
```

## 29. `.best_params_` — sklearn.model_selection

What it does: The winning parameter combination found by the search.
Example: `best_alpha = search.best_params_["ridge__alpha"]`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — search.best_params_"
Center: one large diagram illustrating a podium with the tournament's grid of tried settings faded behind it; the winning cell's setting card (ridge__alpha = 1) is lifted onto the top podium spot under a small trophy — the learned attribute holding the best settings.
Below the diagram: a small code snippet box rendering exactly this code: best_alpha = search.best_params_["ridge__alpha"]
Caption strip at the bottom: "best_params_ holds the winning parameter combination."
```

## 30. `.best_estimator_` — sklearn.model_selection

What it does: The fully retrained model with the best settings — ready to use.
Example: `r2_best = search.best_estimator_.score(X_test, y_test)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — search.best_estimator_"
Center: one large diagram illustrating the tournament grid fading behind as the champion machine — a model box wearing the winning-settings badge — steps forward fully assembled and powered on, with a green ready light, ready to predict on new data.
Below the diagram: a small code snippet box rendering exactly this code: r2_best = search.best_estimator_.score(X_test, y_test)
Caption strip at the bottom: "best_estimator_ is the retrained model with the best settings."
```

---

Total: 31 new functions introduced in this module.

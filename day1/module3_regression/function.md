# Function Reference — Module 3: Regression & Model Fitting

Only functions introduced for the first time in this module are listed here, in the order you will meet them. Functions already covered in earlier modules are not repeated — look them up in the earlier modules' `function.md`.

## 1. `np.median(...)` — numpy

What it does: The middle value of the data — barely moves when an outlier is present.
Example: `median = np.median(readings)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.median(array)"
Center: one large diagram illustrating a sorted row of dots on a number line with a coral flag planted exactly at the middle dot (the median); beside it a faded second row shows one extreme dot pushed far right dragging the mean marker with it while the median flag stays put — the middle value resists outliers.
Below the diagram: a small code snippet box rendering exactly this code: median = np.median(readings)
Caption strip at the bottom: "np.median() gives the middle value — robust against outliers."
```

## 2. `.copy()` (array method) — numpy

What it does: Makes an independent copy of an array so the original stays intact.
Example: `bad = readings.copy()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — arr.copy()"
Center: one large diagram illustrating one row of value cells on the left being duplicated through a photocopier into an identical row on the right; a link-cutting scissors icon between the two rows shows the copy is independent — edit the copy and the original is untouched.
Below the diagram: a small code snippet box rendering exactly this code: bad = readings.copy()
Caption strip at the bottom: "copy() duplicates an array so experiments don't touch the original."
```

## 3. `np.corrcoef(...)` — numpy

What it does: The correlation coefficient between two variables — how tightly they move together.
Example: `np.corrcoef(xs, ys)[0, 1]`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.corrcoef(x, y)"
Center: one large diagram illustrating two dot clouds side by side — one tightly clustered along a diagonal line with a big r = 0.99 badge, one round and loose with a small r = 0.03 badge — both reduced by the function into a single number r between -1 and 1 for each pair.
Below the diagram: a small code snippet box rendering exactly this code: np.corrcoef(xs, ys)[0, 1]
Caption strip at the bottom: "np.corrcoef() measures how tightly two variables move together."
```

## 4. `np.percentile(...)` — numpy

What it does: The value at a given percentile — Q1 and Q3 for the IQR outlier rule.
Example: `q1, q3 = np.percentile(t, [25, 75])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.percentile(data, [25, 75])"
Center: one large diagram illustrating a hundred sorted dots spread along a number line; coral flags drop at the 25% cut and the 75% cut, labelled Q1 and Q3, with the span between them bracketed as the IQR — percentile asks "what value sits at this fraction of the sorted data?".
Below the diagram: a small code snippet box rendering exactly this code: q1, q3 = np.percentile(t, [25, 75])
Caption strip at the bottom: "np.percentile() reads off values at given percentiles."
```

## 5. `np.loadtxt(...)` — numpy

What it does: Loads a plain-text data file straight into a numpy array (the NIST Pontius dataset).
Example: `np.loadtxt(DATA / "Pontius.dat", skiprows=60, max_rows=40)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.loadtxt(path)"
Center: one large diagram illustrating a plain-text file page with a header block of comment lines skipped over (shown greyed behind a skiprows stamp) and 40 data rows peeled off into a clean numeric array grid — text file in, array out.
Below the diagram: a small code snippet box rendering exactly this code: np.loadtxt(DATA / "Pontius.dat", skiprows=60, max_rows=40)
Caption strip at the bottom: "loadtxt() loads a plain-text data file into a numpy array."
```

## 6. `ax.set_xlabel(...)` — matplotlib.pyplot

What it does: Labels the x-axis of a plot panel.
Example: `ax.set_xlabel("applied load x (N)")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib — ax.set_xlabel(text)"
Center: one large diagram illustrating a scatter chart with an empty slot under its horizontal axis like a nameplate holder; a label banner reading "applied load x (N)" slides up into the slot and clicks into place beneath the axis — set_xlabel names the x-axis.
Below the diagram: a small code snippet box rendering exactly this code: ax.set_xlabel("applied load x (N)")
Caption strip at the bottom: "set_xlabel() labels the x-axis of a plot."
```

## 7. `r2_score(y_true, y_pred)` — sklearn.metrics

What it does: R² — the fraction of variance the model explains (1.0 is perfect).
Example: `r2_score(yp, pred)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — r2_score(y_true, y_pred)"
Center: one large diagram illustrating two rows of chips — true values and predictions — being compared pair by pair into a gauge meter whose needle points near the right end marked 1.0; the gauge scale runs from 0 (explains nothing) to 1 (explains everything), with the needle position stamped R² = 0.99.
Below the diagram: a small code snippet box rendering exactly this code: r2_score(yp, pred)
Caption strip at the bottom: "r2_score() grades how much of the variance the model explains."
```

## 8. `mean_squared_error(y_true, y_pred)` — sklearn.metrics

What it does: The mean of squared errors — take its square root to get RMSE in original units.
Example: `np.sqrt(mean_squared_error(yp, pred))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — mean_squared_error(y_true, y_pred)"
Center: one large diagram illustrating a scatter with a fitted line; vertical coral error segments from each point to the line are squared into small shaded squares, all the squares pour into an averaging funnel, and one number emerges — with an attached square-root sign showing the route to RMSE.
Below the diagram: a small code snippet box rendering exactly this code: np.sqrt(mean_squared_error(yp, pred))
Caption strip at the bottom: "mean_squared_error() averages the squared prediction errors."
```

## 9. `.predict(X)` — sklearn.linear_model

What it does: Produces the trained model's predicted y values for given X inputs.
Example: `pred = lin.predict(Xp)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — model.predict(X)"
Center: one large diagram illustrating a trained model box (fitted line stored inside as a small chart icon); fresh input chips enter the left funnel and predicted output chips stream out of the right pipe, each computed from the learned line — ask the model, get answers.
Below the diagram: a small code snippet box rendering exactly this code: pred = lin.predict(Xp)
Caption strip at the bottom: "predict() produces the model's answers for new inputs."
```

## 10. `.intercept_` — sklearn.linear_model

What it does: The fitted intercept b0 — where the line crosses the y-axis.
Example: `lin.intercept_`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — model.intercept_"
Center: one large diagram illustrating a fitted straight line crossing a vertical y-axis; the crossing point is circled in coral and labelled b0, with a dotted arrow from the intersection to a value badge — the learned attribute intercept_ holds exactly that crossing value.
Below the diagram: a small code snippet box rendering exactly this code: lin.intercept_
Caption strip at the bottom: "intercept_ is the fitted value where the line crosses the axis."
```

## 11. `.coef_` — sklearn.linear_model

What it does: The fitted slope/coefficients — one per feature.
Example: `lin.coef_[0]`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — model.coef_"
Center: one large diagram illustrating a fitted line with a slope triangle (rise over run) shaded on it, labelled b1; beside it a small rack of coefficient bars — one bar per input feature, taller bar meaning stronger effect — with the attribute name coef_ on the rack.
Below the diagram: a small code snippet box rendering exactly this code: lin.coef_[0]
Caption strip at the bottom: "coef_ holds the fitted slope of each feature."
```

## 12. `np.asarray(...)` — numpy

What it does: Converts a column (or list) into a numpy array for element-wise math.
Example: `resid = np.asarray(yp) - pred`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.asarray(column)"
Center: one large diagram illustrating a table column strip passing through a gateway labelled asarray and emerging as a plain row of numeric cells ready for element-wise subtraction with another array — whatever you hand it comes out as numpy math material.
Below the diagram: a small code snippet box rendering exactly this code: resid = np.asarray(yp) - pred
Caption strip at the bottom: "np.asarray() converts a column into a numpy array for math."
```

## 13. `ax.axhline(y)` — matplotlib.pyplot

What it does: Draws a horizontal reference line across the whole plot (here: the zero-residual line).
Example: `axes[0].axhline(0, color="#e76f51", lw=1)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib — ax.axhline(y)"
Center: one large diagram illustrating a residual scatter plot; a thin coral horizontal line is drawn edge-to-edge across the panel at height zero like a taut wire, with dots scattered above and below it — a full-width reference line at a chosen y value.
Below the diagram: a small code snippet box rendering exactly this code: axes[0].axhline(0, color="#e76f51", lw=1)
Caption strip at the bottom: "axhline() draws a horizontal reference line across the plot."
```

## 14. `np.polyfit(x, y, deg)` — numpy

What it does: Fits a polynomial of a chosen degree to (x, y) data and returns its coefficients.
Example: `b2, b1, b0 = np.polyfit(pont["x"].to_numpy(), np.asarray(yp), 2)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.polyfit(x, y, deg)"
Center: one large diagram illustrating scattered data points with a gently curved teal line threading through them; the curve is described by three coefficient chips labelled b2, b1, b0 sliding out of the fitting machine — degree 2 means a quadratic, the coefficients are the curve's recipe.
Below the diagram: a small code snippet box rendering exactly this code: b2, b1, b0 = np.polyfit(pont["x"].to_numpy(), np.asarray(yp), 2)
Caption strip at the bottom: "np.polyfit() fits a polynomial curve and returns its coefficients."
```

## 15. `np.polyval(coeffs, x)` — numpy

What it does: Evaluates a fitted polynomial at given x values — turns coefficients back into predictions.
Example: `pred = np.polyval([b2, b1, b0], pont["x"].to_numpy())`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.polyval(coeffs, x)"
Center: one large diagram illustrating three coefficient chips (b2, b1, b0) loaded into a small evaluation machine; a row of new x values enters, each is plugged into the polynomial b2·x² + b1·x + b0, and a row of computed y values exits — the recipe run at every point.
Below the diagram: a small code snippet box rendering exactly this code: pred = np.polyval([b2, b1, b0], pont["x"].to_numpy())
Caption strip at the bottom: "np.polyval() evaluates the fitted polynomial at new x values."
```

## 16. `np.linspace(start, stop, num)` — numpy

What it does: Creates evenly spaced points across a range — used to draw smooth fitted lines.
Example: `xs = np.linspace(-3, 3, 100)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.linspace(start, stop, num)"
Center: one large diagram illustrating a ruler segment between -3 and 3 with 100 tick marks placed at perfectly even spacing, the first and last tick highlighted with start/stop tags — a row of equally spaced sample points generated on demand.
Below the diagram: a small code snippet box rendering exactly this code: xs = np.linspace(-3, 3, 100)
Caption strip at the bottom: "linspace() creates evenly spaced points across a range."
```

## 17. `.reshape(-1, 1)` (array method) — numpy

What it does: Turns a 1-D array into a single column — the 2-D shape sklearn expects for X.
Example: `grid = np.linspace(...).reshape(-1, 1)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — arr.reshape(-1, 1)"
Center: one large diagram illustrating a horizontal row of cells rotating up on a hinge into a single vertical column, with the -1 tag meaning "figure this length out for me" and the 1 tag meaning "one column" — same values, new shape, nothing lost.
Below the diagram: a small code snippet box rendering exactly this code: grid = np.linspace(...).reshape(-1, 1)
Caption strip at the bottom: "reshape(-1, 1) turns a row of values into one column."
```

## 18. `Lasso(alpha=...)` — sklearn.linear_model

What it does: Linear regression with an L1 penalty that can push coefficients all the way to zero — automatic feature selection.
Example: `lasso = Lasso(alpha=0.1).fit(X_train, y_train)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — Lasso(alpha=...)"
Center: one large diagram illustrating a bar chart of coefficient bars being squeezed toward zero; unlike gentle ridge springs, here a pair of scissors snips the weakest bars completely down to zero (they lie flat), while the important bars survive — an alpha dial controls how aggressive the cutting is.
Below the diagram: a small code snippet box rendering exactly this code: lasso = Lasso(alpha=0.1).fit(X_train, y_train)
Caption strip at the bottom: "Lasso's L1 penalty can zero out coefficients — built-in feature selection."
```

## 19. `make_pipeline(...)` — sklearn.pipeline

What it does: Chains a scaler, transformers, and a model into one pipeline object with automatic step names.
Example: `pipe = make_pipeline(StandardScaler(), Ridge(alpha=a))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — make_pipeline(step1, step2, ...)"
Center: one large diagram illustrating machine boxes snapping onto one assembly line left to right — a StandardScaler box then a Ridge model box — each box auto-printed with a lowercase name tag (standardscaler, ridge); data enters at the left end and the finished model powers up at the right end, no names needed from you.
Below the diagram: a small code snippet box rendering exactly this code: pipe = make_pipeline(StandardScaler(), Ridge(alpha=a))
Caption strip at the bottom: "make_pipeline() chains steps into one object, naming them for you."
```

## 20. `.named_steps["name"]` — sklearn.pipeline

What it does: Reaches into a fitted pipeline and grabs one of its steps by name.
Example: `lasso_model.named_steps["lasso"].coef_`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — pipe.named_steps[\"name\"]"
Center: one large diagram illustrating a pipeline shown as a row of linked machine boxes, each wearing its name tag; a hand opens a hatch on the box tagged lasso and pulls out its coefficient bars — named_steps is the door into any individual step of the chain.
Below the diagram: a small code snippet box rendering exactly this code: lasso_model.named_steps["lasso"].coef_
Caption strip at the bottom: "named_steps[\"name\"] accesses one step of the pipeline by name."
```

## 21. `cross_val_score(model, X, y, cv)` — sklearn.model_selection

What it does: Evaluates a model with k-fold cross-validation, returning one score per fold.
Example: `scores = cross_val_score(pipe, X_train, y_train, cv=5, scoring="r2")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — cross_val_score(model, X, y, cv=5)"
Center: one large diagram illustrating a data strip folded like an accordion into 5 segments; in each of five small repeat diagrams a different segment is shaded coral as the held-out test part while the teal rest trains a mini model, and each run reports one score chip — five fair test scores, one per fold.
Below the diagram: a small code snippet box rendering exactly this code: scores = cross_val_score(pipe, X_train, y_train, cv=5, scoring="r2")
Caption strip at the bottom: "cross_val_score() tests the model on every fold and returns the scores."
```

## 22. `ax.errorbar(x, y, yerr)` — matplotlib.pyplot

What it does: Draws points with error bars — here the CV mean plus/minus one std per alpha.
Example: `ax.errorbar(alphas, cv_means, yerr=cv_stds, marker="o", capsize=4)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib — ax.errorbar(x, y, yerr)"
Center: one large diagram illustrating a row of dots along a curve, each dot topped and tailed by a short vertical whisker capped with small horizontal ends, the whisker length showing the uncertainty spread around each mean value — points plus their error ranges.
Below the diagram: a small code snippet box rendering exactly this code: ax.errorbar(alphas, cv_means, yerr=cv_stds, marker="o", capsize=4)
Caption strip at the bottom: "errorbar() plots points with error bars showing their spread."
```

## 23. `ax.set_xscale("log")` — matplotlib.pyplot

What it does: Switches the x-axis to a logarithmic scale, so widely ranging values fit on one plot.
Example: `ax.set_xscale("log")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib — ax.set_xscale(\"log\")"
Center: one large diagram illustrating an axis relabelled by a swapping hand: on the left a crowded linear axis where values 0.001 to 100 squash the small ones into one corner; on the right the same axis with tick marks 0.001, 0.01, 0.1, 1, 10, 100 spread evenly — equal steps become equal distances.
Below the diagram: a small code snippet box rendering exactly this code: ax.set_xscale("log")
Caption strip at the bottom: "set_xscale(\"log\") makes each factor-of-10 take the same space."
```

## 24. `np.argmax(...)` — numpy

What it does: The position (index) of the largest value — picks the winner from the CV scores.
Example: `best = alphas[int(np.argmax(cv_means))]`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.argmax(values)"
Center: one large diagram illustrating a row of score bars of different heights with position labels 0, 1, 2, 3, 4 beneath; a coral crown drops onto the tallest bar and an arrow points to its position number, not its height — argmax returns WHERE the maximum lives, not the maximum itself.
Below the diagram: a small code snippet box rendering exactly this code: best = alphas[int(np.argmax(cv_means))]
Caption strip at the bottom: "np.argmax() returns the index of the largest value."
```

## 25. `.mean()` (Series method) — polars

What it does: The average of a column's values — here used by hand to center a feature for scaling.
Example: `x_mean, x_std = train_p["x"].mean(), train_p["x"].std()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — series.mean()"
Center: one large diagram illustrating a vertical column strip of values with a balance-point triangle marker computed at its average height; the single mean value chip slides out beside it — one call, the column's average.
Below the diagram: a small code snippet box rendering exactly this code: x_mean, x_std = train_p["x"].mean(), train_p["x"].std()
Caption strip at the bottom: ".mean() gives the average of a column's values."
```

## 26. `.best_score_` — sklearn.model_selection

What it does: The best cross-validated score achieved during the search.
Example: `search.best_score_`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — search.best_score_"
Center: one large diagram illustrating a tournament grid of tried settings fading behind a podium; on the winner's podium sits a score badge showing the cross-validated R² of the best setting — the learned attribute best_score_ records how good the champion actually was.
Below the diagram: a small code snippet box rendering exactly this code: search.best_score_
Caption strip at the bottom: "best_score_ is the best cross-validated score found by the search."
```

---

Total: 28 new functions introduced in this module.

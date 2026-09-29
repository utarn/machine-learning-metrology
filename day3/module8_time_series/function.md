# Function Reference — Module 8: Time Series

Only functions introduced for the first time in this module are listed here, in the order you will meet them. Functions already covered in earlier modules are not repeated — look them up in the earlier modules' `function.md`.

## 1. `Series.rolling_mean(window_size=12, center=True, min_samples=6)` — polars

What it does: Smooths a series by sliding a window of a fixed size along it and averaging the values inside each window — here a 12-month moving average becomes the trend estimate (center=True puts the window's midpoint on each date; min_samples=6 tolerates edge windows with a few missing points).
Example: `trend = s.rolling_mean(window_size=12, center=True, min_samples=6)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — Series.rolling_mean(window_size=12, center=True, min_samples=6)"
Center: one large diagram illustrating a jagged monthly time-series line (dark slate blue) with a highlighted sliding window box of 12 points; a smaller inset shows the window centered on one point with 6 points on each side; a smooth bold teal curve emerges from the windows, riding through the middle of the jagged line; a small coral arrow label says "trend estimate"; a tiny corner tag reads "window slides one point at a time".
Below the diagram: a small code snippet box rendering exactly this code: trend = s.rolling_mean(window_size=12, center=True, min_samples=6)
Caption strip at the bottom: Slides an averaging window along the series — a 12-month moving average reveals the trend.
```

## 2. `np.nanmean(arr)` — numpy

What it does: Like `np.mean`, but it ignores missing values (NaN) instead of turning the whole answer into NaN — essential here because de-trended monthly data still has holes at the series edges.
Example: `seas_profile = np.array([np.nanmean(detrended[month == m]) for m in range(1, 13)])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.nanmean(arr)"
Center: one large diagram illustrating a row of twelve vertical bars (teal) representing monthly averages, where two bars are drawn as dashed outlines with a small "NaN" gap label; a coral magnifying glass hovers over the gaps; a bold dark slate blue arrow sweeps only over the solid bars and points to a single result box labeled "mean of the non-missing values"; a small crossed-out NaN symbol emphasizes that gaps are skipped, not counted.
Below the diagram: a small code snippet box rendering exactly this code: np.nanmean(detrended[month == m])
Caption strip at the bottom: Computes the mean while skipping missing (NaN) values instead of poisoning the result.
```

## 3. `arr.max()` — numpy

What it does: Returns the largest value in the array — here used on the seasonal profile to measure its amplitude (`max - min`), the size of the yearly swing.
Example: `amplitude = seas_profile.max() - seas_profile.min()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — arr.max()"
Center: one large diagram illustrating a small line chart of twelve monthly seasonal values rising and falling in a wave; the tallest peak is circled in teal with a flag labeled "max", the deepest trough is circled in coral with a flag labeled "min"; a vertical double-headed dark slate blue arrow spans between them labeled "amplitude = max - min".
Below the diagram: a small code snippet box rendering exactly this code: amplitude = seas_profile.max() - seas_profile.min()
Caption strip at the bottom: Picks out the largest value in the array — here it sizes the yearly seasonal swing.
```

## 4. `np.column_stack([a, b])` — numpy

What it does: Sticks several 1-D arrays side by side as columns of one 2-D matrix — here two lagged copies of the CO2 series (`y_{t-1}` and `y_{t-12}`) become the two feature columns of the forecasting model's input matrix X.
Example: `X = np.column_stack([v[12 : N - 1], v[0 : N - 13]])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.column_stack([a, b])"
Center: one large diagram illustrating two horizontal 1-D strips of numbers side by side — the top strip teal and labeled "y(t-1)", the bottom strip coral and labeled "y(t-12)" — both sliding with arrows into a 2-D grid table on the right that has exactly two columns matching the two colors, with a column header row reading "X"; a small tag says "each lag becomes a feature column".
Below the diagram: a small code snippet box rendering exactly this code: X = np.column_stack([v[12 : N - 1], v[0 : N - 13]])
Caption strip at the bottom: Glues 1-D lagged series side by side into a 2-D feature matrix for the model.
```

## 5. `TimeSeriesSplit(n_splits=5)` — sklearn.model_selection

What it does: Creates a cross-validation splitter built for time data: unlike random shuffling, every fold trains only on the past and tests on the next chunk of the future.
Example: `tscv = TimeSeriesSplit(n_splits=5)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.model_selection — TimeSeriesSplit(n_splits=5)"
Center: one large diagram illustrating a stack of five horizontal fold bars, one per row, labeled "fold 0" to "fold 4"; in each row a teal block on the left grows longer row by row (the training past) and a coral block immediately follows it (the test future); an arrow down the left side labeled "time flows forward" and a small crossed-out shuffle icon in a corner with the note "no shuffling — order matters".
Below the diagram: a small code snippet box rendering exactly this code: tscv = TimeSeriesSplit(n_splits=5)
Caption strip at the bottom: Builds a splitter whose folds always train on the past and test on the next slice of the future.
```

## 6. `TimeSeriesSplit(...).split(X)` — sklearn.model_selection

What it does: The splitter's workhorse method: handed the data, it yields one `(train_indices, test_indices)` pair per fold, so a `for tr, te in ...:` loop can fit on the past and evaluate on the next future chunk.
Example: `for tr, te in tscv.split(X):`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.model_selection — TimeSeriesSplit(...).split(X)"
Center: one large diagram illustrating a timeline strip of many small squares with a walking-forward mechanism: a teal bracket covers the past portion (labeled "train indices") and a coral bracket covers the next portion (labeled "test indices"); a dark slate blue arrow labeled "walks forward one fold at a time" shows the pair of brackets sliding right; at the right edge an output tag shows the pair "(train, test)" being handed out per fold, like tickets from a dispenser.
Below the diagram: a small code snippet box rendering exactly this code: for tr, te in tscv.split(X):
Caption strip at the bottom: Yields one (train_indices, test_indices) pair per fold, walking forward through time.
```

## 7. `XGBRegressor(n_estimators=300, max_depth=3, learning_rate=0.05, random_state=42)` — xgboost

What it does: Creates a gradient-boosted tree regressor — 300 small decision trees built one after another, each correcting what the previous ones got wrong; a flexible nonlinear learner to challenge the linear model.
Example: `xgb = XGBRegressor(n_estimators=300, max_depth=3, learning_rate=0.05, random_state=42)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "xgboost — XGBRegressor(n_estimators=300, max_depth=3, learning_rate=0.05, random_state=42)"
Center: one large diagram illustrating a chain of four small flat decision trees (tiny node-and-branch icons) connected left to right by arrows; under each arrow a small coral plus/minus tag labeled "corrects the previous error"; the chain ends in a single prediction gauge; a settings tag lists "300 trees, depth 3, small learning rate".
Below the diagram: a small code snippet box rendering exactly this code: xgb = XGBRegressor(n_estimators=300, max_depth=3, learning_rate=0.05, random_state=42)
Caption strip at the bottom: Builds a team of small decision trees in sequence, each one fixing the remaining errors of the team so far.
```

## 8. `ax.fill_between(x, lower, upper, alpha=...)` — matplotlib.pyplot

What it does: Shades the area between two curves — here it paints the forecast's ~95% uncertainty band, a cone that widens as the prediction horizon grows.
Example: `ax.fill_between(future_years, fc - band, fc + band, alpha=0.18)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib.pyplot — ax.fill_between(x, lower, upper, alpha=...)"
Center: one large diagram illustrating a forecast chart: a solid teal line continues past a dotted vertical "today" marker into the future; two fainter dashed curves fan out above and below it, and the wedge between them is shaded in translucent teal (a widening uncertainty cone); small labels "lower" and "upper" point at the two dashed curves and "alpha = transparency" points at the shaded wedge.
Below the diagram: a small code snippet box rendering exactly this code: ax.fill_between(future_years, fc - band, fc + band, alpha=0.18)
Caption strip at the bottom: Shades the band between two curves — the forecast's uncertainty cone, widening with horizon.
```

## 9. `ax.axvline(x)` — matplotlib.pyplot

What it does: Draws a vertical line across the whole chart at one x position — here marking "today", the last observed data point where forecasting begins.
Example: `ax.axvline(dec[-1], color="#999", lw=0.8, ls=":")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib.pyplot — ax.axvline(x)"
Center: one large diagram illustrating a time-series chart where a thin vertical dotted grey line cuts the whole panel from top to bottom at one x position; left of the line a dark slate blue solid line labeled "observed past", right of it a teal dashed line labeled "forecast future"; a small flag on the vertical line reads "today"; a tiny inset shows the one chosen x value on the axis with an arrow up to the line.
Below the diagram: a small code snippet box rendering exactly this code: ax.axvline(dec[-1], color="#999", lw=0.8, ls=":")
Caption strip at the bottom: Drops a full-height vertical marker line at one x value — the "today" line where forecasting starts.
```

---
New functions introduced in this module: **9**.

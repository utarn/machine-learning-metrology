# Function Reference — Module 7: Anomaly Detection

Only functions introduced for the first time in this module are listed here, in the order you will meet them. Functions already covered in earlier modules are not repeated — look them up in the earlier modules' `function.md`.

## 1. `Path.read_text` — python

What it does: Reads a whole text file into one string — used to load the JSON file of labeled anomaly windows.
Example: `(DATA / "nab_machine_temperature_labels.json").read_text()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — Path.read_text()"
Center: one large diagram illustrating a document icon labeled "nab_machine_temperature_labels.json" being unspooled like a tape reel into a single long strip of text characters held in a Python variable box; the whole file goes in, one whole string comes out.
Below the diagram: a small code snippet box rendering exactly this code: (DATA / "nab_machine_temperature_labels.json").read_text()
Caption strip at the bottom: Read an entire text file into one string.
```

## 2. `json.loads` — python

What it does: Parses a JSON text string into Python objects (lists and dicts) — here, the list of labeled anomaly windows.
Example: `lab_windows = json.loads((DATA / "labels.json").read_text())[...]`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — json.loads(text)"
Center: one large diagram illustrating a flat strip of JSON text with braces and quotes ('[{"start": ...}]') being melted and re-assembled by a parser machine into a neat rack of Python list-and-dict shapes — a stack of labeled start/end window cards that code can loop over.
Below the diagram: a small code snippet box rendering exactly this code: lab_windows = json.loads(text)
Caption strip at the bottom: Parse JSON text into Python lists and dicts you can work with.
```

## 3. `zeros` — numpy

What it does: Creates an array filled with zeros — here an all-False boolean mask that labeled windows get switched into one by one.
Example: `lab_mask = np.zeros(df.height, dtype=bool)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.zeros(n, dtype=bool)"
Center: one large diagram illustrating a long strip of cells all stamped gray "False" being produced by a small factory machine whose settings dial reads "dtype = bool"; on the right, a few cells are being individually flipped to coral "True" by labeled windows sliding over them.
Below the diagram: a small code snippet box rendering exactly this code: lab_mask = np.zeros(df.height, dtype=bool)
Caption strip at the bottom: Make an all-zeros (all-False) array of a given length to build on.
```

## 4. `datetime64` — numpy

What it does: Converts a timestamp string into NumPy's datetime type so it can be compared with the series' timestamps.
Example: `(ts >= np.datetime64(a)) & (ts <= np.datetime64(b))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.datetime64(string)"
Center: one large diagram illustrating a text label "2013-12-10 05:20:00" on a card passing through a converter stamp and coming out as a clock-calendar token that clicks into the same timeline ruler as the series' own timestamps; two converted endpoints a and b frame a shaded comparison window on the ruler with >= and <= gates.
Below the diagram: a small code snippet box rendering exactly this code: (ts >= np.datetime64(a)) & (ts <= np.datetime64(b))
Caption strip at the bottom: Turn a timestamp string into NumPy's datetime type so dates can be compared.
```

## 5. `axvspan` — matplotlib.pyplot

What it does: Shades a vertical band across the whole plot between two x-values — used to mark the labeled anomaly windows on the time series.
Example: `ax.axvspan(np.datetime64(a), np.datetime64(b), color="#e76f51", alpha=0.15)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib.pyplot — ax.axvspan(start, end)"
Center: one large diagram illustrating a time-series line chart where a translucent coral vertical band spans from floor to ceiling between two x positions (start and end arrows on the x-axis), highlighting everything that happens inside that time window.
Below the diagram: a small code snippet box rendering exactly this code: ax.axvspan(np.datetime64(a), np.datetime64(b), color="#e76f51", alpha=0.15)
Caption strip at the bottom: Shade a translucent vertical band between two x-values across the whole plot.
```

## 6. `rolling_median` — polars

What it does: A sliding-window median — a robust moving baseline of what the signal "usually is" at each moment.
Example: `roll_med = s.rolling_median(window_size=W, min_samples=W // 2)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — Series.rolling_median(window_size=W)"
Center: one large diagram illustrating a jagged time-series line with a rectangular window frame sliding along it from left to right; inside the current frame, the middle value is picked out with a small caret marker, and the trail of window medians is drawn as a smooth teal baseline line flowing through the noisy series.
Below the diagram: a small code snippet box rendering exactly this code: roll_med = s.rolling_median(window_size=W, min_samples=W // 2)
Caption strip at the bottom: Slide a window along the series, taking the median inside it — a robust moving baseline.
```

## 7. `abs` — polars

What it does: Absolute value, element-wise — applied to the deviation from the baseline so both spikes above and dips below count.
Example: `roll_mad = (s - roll_med).abs().rolling_median(...)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — Series.abs()"
Center: one large diagram illustrating a number line symmetric around zero with a spike dipping below it (-4.2) and a spike above it (+3.7) both being flipped up by a small fold arrow at zero, landing as positive bars 4.2 and 3.7 — deviations above and below the baseline made comparable.
Below the diagram: a small code snippet box rendering exactly this code: roll_mad = (s - roll_med).abs().rolling_median(...)
Caption strip at the bottom: Drop the minus signs — distance from the baseline, above or below.
```

## 8. `empty` — numpy

What it does: Creates an empty array of a given shape, ready to be filled in — here a table for the 5 window features per window.
Example: `feats = np.empty((n_win, 5))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.empty((n_win, 5))"
Center: one large diagram illustrating an empty rectangular grid (rows = windows, columns = 5 feature slots labeled mean, std, slope, min, max) being manufactured by a machine; dotted placeholder cells await values, with one row mid-fill showing actual numbers being written in.
Below the diagram: a small code snippet box rendering exactly this code: feats = np.empty((n_win, 5))
Caption strip at the bottom: Reserve an empty array of a given shape to fill in later.
```

## 9. `IsolationForest` — sklearn.ensemble

What it does: An ensemble of random split trees that isolates points which are easy to separate — those quick-to-isolate points are the anomalies; `contamination` says what fraction you expect.
Example: `iso = IsolationForest(contamination=CONTAM, random_state=42).fit(feats)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.ensemble — IsolationForest(contamination=0.01)"
Center: one large diagram illustrating a dot cloud being cut by random slicing lines from a decision tree: a lone coral dot near the edge is separated after just one cut (labeled "isolated in 1 cut = anomaly"), while a dense teal crowd needs many cuts to separate (labeled "many cuts = normal"); a tiny gauge shows contamination = 1% of 100 dots flagged.
Below the diagram: a small code snippet box rendering exactly this code: iso = IsolationForest(contamination=CONTAM, random_state=42).fit(feats)
Caption strip at the bottom: Random cuts that isolate odd points fast — the fast-to-isolate ones are the anomalies.
```

## 10. `OneClassSVM` — sklearn.svm

What it does: Learns a closed boundary around the normal data only (trained on a trusted clean stretch); points outside the boundary are anomalies.
Example: `ocsvm = make_pipeline(StandardScaler(), OneClassSVM(nu=NU, gamma=GAMMA))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.svm — OneClassSVM(nu=0.01, gamma=0.05)"
Center: one large diagram illustrating a closed, slightly wobbly teal boundary curve hugging a cloud of normal dots like a fence around a village; two coral dots stand outside the fence tagged "-1 anomaly", and small dials read "nu = expected outlier fraction, gamma = how wiggly the fence is".
Below the diagram: a small code snippet box rendering exactly this code: OneClassSVM(nu=NU, gamma=GAMMA)
Caption strip at the bottom: Learn the shape of "normal" only — anything outside the boundary is an anomaly.
```

## 11. `concatenate` — numpy

What it does: Joins arrays end-to-end — here, appending a synthetic slow-drift segment onto the end of the real temperature series.
Example: `v_drift = np.concatenate([v, drift_seg])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.concatenate([a, b])"
Center: one large diagram illustrating two array strips — a long teal wiggly series strip "v" and a shorter coral gently-rising strip "drift_seg" — being welded end-to-end at a junction point into one longer strip labeled "v_drift".
Below the diagram: a small code snippet box rendering exactly this code: v_drift = np.concatenate([v, drift_seg])
Caption strip at the bottom: Join arrays end-to-end into one longer array.
```

## 12. `nanmedian` — numpy

What it does: The median while ignoring NaN values — the typical noise scale (sigma) for the CUSUM detector, computed even where values are missing.
Example: `sigma = float(np.nanmedian(mad_d.to_numpy()))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.nanmedian(arr)"
Center: one large diagram illustrating a row of values with a few hollow "NaN" gaps; the sorter ignores the gap cells (shown swept aside on a small reject tray) and picks the middle of the remaining real values, crowned as sigma, the typical noise scale.
Below the diagram: a small code snippet box rendering exactly this code: sigma = float(np.nanmedian(mad_d.to_numpy()))
Caption strip at the bottom: Take the median while skipping missing (NaN) values.
```

## 13. `isfinite` — numpy

What it does: True where a value is a real number (not NaN or infinity) — guards the CUSUM loop against missing residuals.
Example: `r = resid_d[i] if np.isfinite(resid_d[i]) else 0.0`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.isfinite(x)"
Center: one large diagram illustrating a quality-control gate on a conveyor of value tokens: normal number tokens pass through stamped "True" (teal), while broken tokens labeled "NaN" and "inf" are diverted to a reject chute stamped "False" (coral).
Below the diagram: a small code snippet box rendering exactly this code: r = resid_d[i] if np.isfinite(resid_d[i]) else 0.0
Caption strip at the bottom: True where a value is a usable real number, False for NaN or infinity.
```

## 14. `flatnonzero` — numpy

What it does: Returns the indices where a boolean mask is True — here, the positions of the CUSUM alarms.
Example: `alarm_idx = len(v) + np.flatnonzero(cusum_flag[d_slice])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.flatnonzero(mask)"
Center: one large diagram illustrating a long boolean strip of gray False cells with a few coral True cells; index tags (12, 57, 203) are lifted off just the True cells and collected into an output list labeled "positions of every alarm", while the False cells are ignored.
Below the diagram: a small code snippet box rendering exactly this code: alarm_idx = len(v) + np.flatnonzero(cusum_flag[d_slice])
Caption strip at the bottom: Report the index of every True in a boolean mask.
```

## 15. `fit_predict` — sklearn.ensemble

What it does: IsolationForest's combined method — fits the trees and outputs the +1/-1 labels in a single call.
Example: `IsolationForest(contamination=CONTAM, random_state=42).fit_predict(feats)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.ensemble — IsolationForest(...).fit_predict(X)"
Center: one large diagram illustrating a two-stage machine merged into one box: raw window features enter the left half (labeled "fit", gears building the trees) and immediately exit the right half as a row of stamped +1 (teal, normal) and -1 (coral, anomaly) tokens — one combined pass instead of two separate boxes.
Below the diagram: a small code snippet box rendering exactly this code: IsolationForest(contamination=CONTAM, random_state=42).fit_predict(feats)
Caption strip at the bottom: Fit and predict in one call — labels come straight out of the freshly built forest.
```

---
**15 new functions introduced in this module.**

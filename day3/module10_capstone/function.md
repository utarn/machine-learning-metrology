# Function Reference — Module 10: Capstone

Only functions introduced for the first time in this module are listed here, in the order you will meet them. Functions already covered in earlier modules are not repeated — look them up in the earlier modules' `function.md`.

## 1. `df.join(other, on="key")` — polars

What it does: Merges two tables by matching rows on a shared key column — here each engine's end-of-life cycle (computed per unit with group_by) is brought back onto every one of that engine's rows, so RUL can be computed row by row.
Example: `df = tr.join(maxc, on="unit")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.join(other, on=\"unit\")"
Center: one large diagram illustrating two flat tables side by side: the left table (teal header) has many rows with a "unit" key column plus sensor columns; the right table (coral header) is a short lookup with the same "unit" key column and one "max_cycle" column; matching key values are linked by dark slate blue arcs connecting row 1 to row 1, row 2 to row 2; the merged result appears below or to the right as one wide table whose rows carry the extra "max_cycle" column; a small tag reads "one match per key value".
Below the diagram: a small code snippet box rendering exactly this code: df = tr.join(maxc, on="unit")
Caption strip at the bottom: Merges two tables by matching their shared key column, attaching the lookup info onto every row.
```

## 2. `model.get_params()` — xgboost

What it does: Returns the model's current settings as a dict — used here with `**` unpacking to stamp out fresh, identically-configured copies of the model for each experiment, without one run's fitted state leaking into another.
Example: `XGBRegressor(**xgb.get_params())`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "xgboost — model.get_params()"
Center: one large diagram illustrating a model box (drawn as a small stack of flat decision trees) with its front panel opened on a hinge like a cabinet door; inside, a clipboard checklist shows setting lines such as "n_estimators: 300", "max_depth: 3", "learning_rate: 0.05"; a coral photocopier-style arrow carries the checklist to two identical fresh model boxes on the right labeled "fresh copy"; a small tag reads "** unpacks the dict into arguments".
Below the diagram: a small code snippet box rendering exactly this code: XGBRegressor(**xgb.get_params())
Caption strip at the bottom: Reads out the model's settings as a dict — handy for cloning a fresh, identical model.
```

---
New functions introduced in this module: **2**.

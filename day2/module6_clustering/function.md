# Function Reference — Module 6: Clustering

Only functions introduced for the first time in this module are listed here, in the order you will meet them. Functions already covered in earlier modules are not repeated — look them up in the earlier modules' `function.md`.

## 1. `str.to_datetime` — polars

What it does: Parses text (like "Date" + "Time" strings) into real datetime values using a format string.
Example: `(pl.col("Date") + " " + pl.col("Time")).str.to_datetime("%d/%m/%Y %H.%M.%S")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — str.to_datetime(format)"
Center: one large diagram illustrating a column of quoted text cells reading "15/01/2004 11.00.00" passing through a parser machine stamped with a format mask "%d/%m/%Y %H.%M.%S" and coming out as calendar-and-clock icons (a real datetime), one per row.
Below the diagram: a small code snippet box rendering exactly this code: (pl.col("Date") + " " + pl.col("Time")).str.to_datetime("%d/%m/%Y %H.%M.%S")
Caption strip at the bottom: Turn text like "15/01/2004 11.00.00" into real datetime values using a format mask.
```

## 2. `with_row_index` — polars

What it does: Adds a new column of sequential row numbers (0, 1, 2, ...) so every row can be referred to by id.
Example: `clean = aq.drop_nulls(FEATURES).with_row_index("row_id")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.with_row_index('row_id')"
Center: one large diagram illustrating a table without row numbers gaining a slim new leftmost column where a small numberer stamps 0, 1, 2, 3, ... down each row, the new column header tagged "row_id" in teal.
Below the diagram: a small code snippet box rendering exactly this code: clean = aq.drop_nulls(FEATURES).with_row_index("row_id")
Caption strip at the bottom: Add a column of sequential row numbers 0, 1, 2, ... to the table.
```

## 3. `std` — polars

What it does: Computes the standard deviation of each selected column — here, to reveal that raw sensor scales differ ~45x.
Example: `stds = clean.select(FEATURES).std().row(0)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.std()"
Center: one large diagram illustrating seven columns of a sensor table each getting a spread-measuring caliper icon; the outputs line up as one summary row of std values (217, 398, ..., 8.8) with the tiny 8.8 highlighted in coral next to the huge ones, showing wildly different spreads.
Below the diagram: a small code snippet box rendering exactly this code: stds = clean.select(FEATURES).std().row(0)
Caption strip at the bottom: One row of standard deviations — how spread out each column is.
```

## 4. `row` — polars

What it does: Gets one row of the DataFrame as a tuple of values — used here to pull the std values out of the 1-row result.
Example: `stds = clean.select(FEATURES).std().row(0)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.row(0)"
Center: one large diagram illustrating a small table with its top row highlighted; a hand reaches in and lifts that single row out, laying it flat as a horizontal tuple of values (217, 398, 126, ...) with the index "0" pointing at which row was grabbed.
Below the diagram: a small code snippet box rendering exactly this code: stds = clean.select(FEATURES).std().row(0)
Caption strip at the bottom: Pull out one row of the table as a plain tuple of values.
```

## 5. `KMeans` — sklearn.cluster

What it does: Partitions points into k groups by repeatedly assigning each point to its nearest center and moving the centers — the workhorse clustering algorithm.
Example: `km = KMeans(n_clusters=4, n_init=10, random_state=42).fit(Xs)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.cluster — KMeans(n_clusters=4)"
Center: one large diagram illustrating a scatter of dots being pulled toward four star-shaped centroids, each dot colored by its nearest star; dashed arrows show the stars sliding toward the middle of their dot crowds, with a circular loop badge "assign -> move -> repeat" and faint Voronoi-style region boundaries.
Below the diagram: a small code snippet box rendering exactly this code: km = KMeans(n_clusters=4, n_init=10, random_state=42).fit(Xs)
Caption strip at the bottom: Split points into k groups — each point joins its nearest center, centers move, repeat.
```

## 6. `n_clusters` — sklearn.cluster

What it does: The number of clusters you ask KMeans for — the k you must choose (here via elbow and silhouette plots).
Example: `km = KMeans(n_clusters=4, n_init=10, random_state=42).fit(Xs)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.cluster — KMeans(n_clusters=k)"
Center: one large diagram illustrating the same scattered dot cloud drawn three times small (k=2, k=4, k=7), each with that many star centroids; a hand dial labeled "k" points at 4, and a question badge asks "how many regimes does the machine really have?"
Below the diagram: a small code snippet box rendering exactly this code: KMeans(n_clusters=4, n_init=10, random_state=42)
Caption strip at the bottom: The dial you must set: how many clusters to divide the points into.
```

## 7. `inertia_` — sklearn.cluster

What it does: After fitting: the total squared distance of points from their cluster centers — lower is tighter; the elbow plot uses it.
Example: `inertias.append(km.inertia_)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.cluster — km.inertia_"
Center: one large diagram illustrating a cluster of dots with dashed distance lines running from each dot to its star-shaped centroid, all the line lengths summed by a big sigma symbol into one number badge "inertia"; beside it a small elbow curve falls steeply then flattens with the elbow marked.
Below the diagram: a small code snippet box rendering exactly this code: inertias.append(km.inertia_)
Caption strip at the bottom: Total squared distance of points to their centers — lower means tighter clusters.
```

## 8. `labels_` — sklearn.cluster

What it does: After fitting: the cluster number (0..k-1) assigned to every point.
Example: `clean.with_columns(pl.Series("cluster", km_final.labels_))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.cluster — km.labels_"
Center: one large diagram illustrating a dot cloud where every dot has been stamped with a small numbered tag (0, 1, 2, 3) matching the color of its cluster region; on the side, a table row per dot receives the same tag, showing the labels flowing out as a column ready to attach to the data.
Below the diagram: a small code snippet box rendering exactly this code: clean.with_columns(pl.Series("cluster", km_final.labels_))
Caption strip at the bottom: After fitting: the cluster number stamped on every point.
```

## 9. `silhouette_score` — sklearn.metrics

What it does: Scores how well points sit inside their cluster versus the nearest other cluster, from -1 to 1 — used to pick k.
Example: `silhouette_score(Xs, km.labels_)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.metrics — silhouette_score(X, labels)"
Center: one large diagram illustrating two dot clusters: one tight and well separated (a dot with short dashed arrow to its own center, long dashed arrow to the other cluster, labeled "b much bigger than a = score near 1"), and one smeared pair of overlapping clusters labeled "score near 0"; a small scale from -1 to +1 sums it up.
Below the diagram: a small code snippet box rendering exactly this code: silhouette_score(Xs, km.labels_)
Caption strip at the bottom: Grade clustering quality from -1 to 1 — are points snug inside their own cluster?
```

## 10. `bincount` — numpy

What it does: Counts how many points fall into each numbered bucket — here, how many hours belong to each cluster.
Example: `np.bincount(km_final.labels_).tolist()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.bincount(labels)"
Center: one large diagram illustrating a row of labeled slots 0, 1, 2, 3 (buckets) receiving tossed tokens one by one; each slot ends with a tally counter reading its total (e.g. 3965, 2023, 1267, 1736), the token stream above showing raw label numbers dropping into the right slot by number.
Below the diagram: a small code snippet box rendering exactly this code: np.bincount(km_final.labels_).tolist()
Caption strip at the bottom: Tally how many items carry each integer label 0, 1, 2, ...
```

## 11. `cluster_centers_` — sklearn.cluster

What it does: After fitting: the coordinates of each cluster's center point (in scaled units).
Example: `scaler.inverse_transform(km_final.cluster_centers_)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.cluster — km.cluster_centers_"
Center: one large diagram illustrating four star-shaped centroid markers sitting at the heart of four dot crowds, each star radiating a subtle glow ring; a small coordinate card next to each star lists its center position across the 7 sensor axes.
Below the diagram: a small code snippet box rendering exactly this code: scaler.inverse_transform(km_final.cluster_centers_)
Caption strip at the bottom: After fitting: the exact coordinates of each cluster's center.
```

## 12. `inverse_transform` — sklearn.preprocessing

What it does: Converts scaled values back to their original units — so centroids can be read as real sensor readings (°C, %).
Example: `scaler.inverse_transform(km_final.cluster_centers_)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.preprocessing — scaler.inverse_transform(X)"
Center: one large diagram illustrating a small table of abstract scaled numbers (like -1.2, 0.4) flowing left-to-right through an "undo scaler" machine (arrows pointing backwards, mean=0 badge crossed out) and coming out as values with real units attached: 28.1 °C, 32.4 % — the reverse trip of the original StandardScaler.
Below the diagram: a small code snippet box rendering exactly this code: scaler.inverse_transform(km_final.cluster_centers_)
Caption strip at the bottom: Un-scale values back to their original units — read centroids as real sensor numbers.
```

## 13. `Config` — polars

What it does: Temporarily changes how polars prints tables — here, making the printed table wider so 7-column centroids aren't truncated.
Example: `with pl.Config(tbl_width_chars=250): print(centroids)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — pl.Config(tbl_width_chars=250)"
Center: one large diagram illustrating a console window showing a table cut off mid-column with a "..." truncation marker; beside it the same window widened (arrows stretching the frame) so all seven columns fit, with a small settings dial labeled "tbl_width_chars" turned up.
Below the diagram: a small code snippet box rendering exactly this code: with pl.Config(tbl_width_chars=250): print(centroids)
Caption strip at the bottom: Adjust how polars prints tables — widen the output so wide frames aren't cut off.
```

## 14. `PCA` — sklearn.decomposition

What it does: Finds the few directions that capture the most variance, so 7-D data can be compressed and drawn in 2-D.
Example: `pca = PCA(n_components=2).fit(Xs)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.decomposition — PCA(n_components=2)"
Center: one large diagram illustrating a 3-D-ish dot cloud being rotated and projected onto two thick arrows labeled PC1 and PC2 that run through the cloud's longest and second-longest spread directions; the shadow of the cloud landing on a flat 2-D plane shows the compression to a drawable map.
Below the diagram: a small code snippet box rendering exactly this code: pca = PCA(n_components=2).fit(Xs)
Caption strip at the bottom: Squeeze many features onto the few directions that carry the most variance.
```

## 15. `explained_variance_ratio_` — sklearn.decomposition

What it does: The fraction of total variance each principal component explains — PC1 + PC2 tells you whether the 2-D plot is honest.
Example: `evr = pca.explained_variance_ratio_`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.decomposition — pca.explained_variance_ratio_"
Center: one large diagram illustrating a horizontal stacked bar or two pie slices labeled "PC1 = 58.9%" (teal) and "PC2 = 22.5%" (coral) filling most of a bar labeled "total variance", with the remaining gray sliver labeled "the 18.6% your 2-D plot doesn't show".
Below the diagram: a small code snippet box rendering exactly this code: evr = pca.explained_variance_ratio_
Caption strip at the bottom: How much of the data's variance each component explains — is the 2-D map honest?
```

## 16. `components_` — sklearn.decomposition

What it does: The loadings: how much each original feature contributes to each principal component.
Example: `np.round(pca.components_, 3)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.decomposition — pca.components_"
Center: one large diagram illustrating a recipe card for each principal component: a row of feature names (S1, S2, S3, T, RH...) each with a weight bar above or below zero — most teal bars pointing positive, one coral bar (S3) pointing negative, annotated "S3 runs against the others"; the bars are the loadings that mix the original features.
Below the diagram: a small code snippet box rendering exactly this code: np.round(pca.components_, 3)
Caption strip at the bottom: The mixing weights — how much each original feature contributes to each component.
```

## 17. `NearestNeighbors` — sklearn.neighbors

What it does: Indexes the data so each point's nearest neighbours can be found quickly — the first step of the k-distance plot for choosing DBSCAN's eps.
Example: `nn = NearestNeighbors(n_neighbors=MIN_SAMPLES).fit(Xs)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.neighbors — NearestNeighbors(n_neighbors=10)"
Center: one large diagram illustrating a dot cloud with one highlighted point in the middle drawing straight dashed lines to its 10 nearest neighbouring dots (each labeled with a small distance number), the whole scene framed as an address-book index being built from all points.
Below the diagram: a small code snippet box rendering exactly this code: nn = NearestNeighbors(n_neighbors=MIN_SAMPLES).fit(Xs)
Caption strip at the bottom: Build an index so each point's nearest neighbours can be looked up fast.
```

## 18. `kneighbors` — sklearn.neighbors

What it does: Returns the distance from each point to its k nearest neighbours — the raw material of the k-distance curve.
Example: `dists, _ = nn.kneighbors(Xs)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.neighbors — nn.kneighbors(X)"
Center: one large diagram illustrating every dot in a cloud sending out a measuring tape to its 10th nearest neighbour; on the right, a rising sorted curve (the k-distance plot) is being assembled from those measured lengths, with the elbow region circled in coral.
Below the diagram: a small code snippet box rendering exactly this code: dists, _ = nn.kneighbors(Xs)
Caption strip at the bottom: Measure each point's distance to its k nearest neighbours.
```

## 19. `sort` — numpy

What it does: Sorts an array's values in ascending order — here, ordering the k-th-neighbour distances to draw the k-distance curve.
Example: `kdist = np.sort(dists[:, -1])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.sort(arr)"
Center: one large diagram illustrating a row of bars of jumbled heights being swept by a sorting arm into a smooth ascending staircase from shortest to longest, with before/after rows labeled "scrambled" and "sorted".
Below the diagram: a small code snippet box rendering exactly this code: kdist = np.sort(dists[:, -1])
Caption strip at the bottom: Rearrange an array's values from smallest to largest.
```

## 20. `annotate` — matplotlib.pyplot

What it does: Places a text note with an arrow pointing at a specific spot on the chart — used to mark the elbow of the k-distance curve.
Example: `ax.annotate("elbow -> choose eps ~= 1.0", xy=(4000, 1.02), ...)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib.pyplot — ax.annotate(text, xy=...)"
Center: one large diagram illustrating a curve on a mini chart with a coral callout bubble floating to the side reading "elbow -> choose eps ~= 1.0", connected by a thin arrow that bends down and touches the exact elbow point of the curve, which is ringed with a coral marker.
Below the diagram: a small code snippet box rendering exactly this code: ax.annotate("elbow -> choose eps ~= 1.0", xy=(4000, 1.02))
Caption strip at the bottom: Attach an arrowed note pointing at an exact spot on the chart.
```

## 21. `DBSCAN` — sklearn.cluster

What it does: Density-based clustering: groups dense regions into clusters and marks sparse points as noise (-1) — no need to pick k in advance.
Example: `db = DBSCAN(eps=1.0, min_samples=MIN_SAMPLES).fit(Xs)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn.cluster — DBSCAN(eps=1.0, min_samples=10)"
Center: one large diagram illustrating a dot map where dense blobs are colored as clusters, thin circles of radius eps are drawn around a few core points, and three lone gray dots outside every circle carry tags reading "-1 = noise"; a note "no k needed — density decides" sits in the corner.
Below the diagram: a small code snippet box rendering exactly this code: db = DBSCAN(eps=1.0, min_samples=MIN_SAMPLES).fit(Xs)
Caption strip at the bottom: Cluster by density — dense blobs join, lonely points get flagged as noise.
```

## 22. `set` — python

What it does: Python's set type holds unique values only — used here to count distinct cluster labels.
Example: `n_cl = len(set(lab)) - (1 if -1 in lab else 0)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — set(labels)"
Center: one large diagram illustrating a stream of repeated label chips (0, 0, 1, -1, 0, 1, 2, ...) pouring into a funnel-shaped box labeled "set" and coming out as just one chip per distinct value (0, 1, 2, -1), duplicates bouncing off; a counter below reads "len(set) = 4".
Below the diagram: a small code snippet box rendering exactly this code: n_cl = len(set(lab)) - (1 if -1 in lab else 0)
Caption strip at the bottom: Collapse a list to its unique values only — count distinct cluster labels.
```

## 23. `group_by` — polars

What it does: Bundles rows that share the same key values into groups — here, hours grouped by regime so each regime's profile can be summarized.
Example: `clean.group_by("hour", "cluster").len()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.group_by('hour', 'cluster')"
Center: one large diagram illustrating a flat table of rows being gathered into small colored bundles tied with string, one bundle per unique (hour, cluster) pair — rows with the same key combination sliding together into the same bundle, with a group id tag on each.
Below the diagram: a small code snippet box rendering exactly this code: clean.group_by("hour", "cluster").len()
Caption strip at the bottom: Gather rows sharing the same key values into groups, ready to summarize.
```

## 24. `agg` — polars

What it does: Collapses each group down to summary values — counts, means, min/max — one output row per group.
Example: `.agg(pl.len().alias("n_hours"), pl.col("T").mean().round(1), ...)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — .agg(pl.len(), pl.col('T').mean(), ...)"
Center: one large diagram illustrating each group bundle from a group_by being fed through a press that squeezes many rows into a single summary row — the press stamped with three small gauges labeled "count", "mean(T)", "min/max date"; below, one tidy output row per group lines up in a results table.
Below the diagram: a small code snippet box rendering exactly this code: .agg(pl.len().alias("n_hours"), pl.col("T").mean().round(1))
Caption strip at the bottom: Squeeze each group into one summary row: counts, means, min/max.
```

## 25. `dt.hour` — polars

What it does: Datetime accessor that extracts just the hour-of-day (0–23) from a datetime column — also `.dt.month()`, `.dt.date()`.
Example: `clean.with_columns(pl.col("ts").dt.hour().alias("hour"))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — dt.hour()"
Center: one large diagram illustrating a column of full datetime cells (calendar + clock icons showing 11:00, 14:00, 03:00) passing under a magnifying glass focused only on the clock face; the output column holds just the hour numbers 11, 14, 3, with the calendar part grayed out and dropped.
Below the diagram: a small code snippet box rendering exactly this code: clean.with_columns(pl.col("ts").dt.hour().alias("hour"))
Caption strip at the bottom: Extract the hour of day (0-23) from a datetime column.
```

## 26. `pivot` — polars

What it does: Turns long grouped data into a wide table — one column per cluster, one row per hour.
Example: `.pivot(on="cluster", index="hour", values="len")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — .pivot(on='cluster', index='hour', values='len')"
Center: one large diagram illustrating a narrow long table (rows of hour/cluster/count triplets) being rotated like a turnstile into a wide grid: hours run down the left edge as row labels, cluster numbers become the column headers across the top, and counts fill the cells at each crossing.
Below the diagram: a small code snippet box rendering exactly this code: .pivot(on="cluster", index="hour", values="len")
Caption strip at the bottom: Rotate long data into a wide table — one column per group, one row per key.
```

## 27. `fill_null` — polars

What it does: Replaces missing values with a chosen value — here, filling cluster-hour combinations that have zero members with 0.
Example: `.fill_null(0)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.fill_null(0)"
Center: one large diagram illustrating a table with several empty cells marked with question marks; a glue gun labeled "0" fills each empty cell with a teal zero, the question marks disappearing row by row.
Below the diagram: a small code snippet box rendering exactly this code: .fill_null(0)
Caption strip at the bottom: Replace every missing value with a chosen fill value, here 0.
```

## 28. `sum_horizontal` — polars

What it does: Sums several columns row-by-row (across, not down) — here, the total member count per hour used to turn counts into percentages.
Example: `pl.col(c) / pl.sum_horizontal([pl.col(c2) for c2 in cl_cols]) * 100`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — pl.sum_horizontal([...])"
Center: one large diagram illustrating one row of a table with four columns of counts; horizontal arrows sweep across the row adding the values left-to-right into a single total at the row's end (like a scoreboard summing across), with a note "across the row, not down the column".
Below the diagram: a small code snippet box rendering exactly this code: pl.col(c) / pl.sum_horizontal([pl.col(c2) for c2 in cl_cols]) * 100
Caption strip at the bottom: Add up several columns row-by-row — a per-row total across the table.
```

## 29. `set_xticks` — matplotlib.pyplot

What it does: Controls exactly where tick marks sit on the x-axis and what text labels they carry.
Example: `axes[0].set_xticks(range(0, 24, 3))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib.pyplot — ax.set_xticks(ticks, labels)"
Center: one large diagram illustrating a horizontal axis where small tick pins are being hammered in at exact positions 0, 3, 6, 9, ... 21 (evenly every 3), replacing a crowded default axis; each pin gets a neat number label beneath it.
Below the diagram: a small code snippet box rendering exactly this code: axes[0].set_xticks(range(0, 24, 3))
Caption strip at the bottom: Choose exactly where the x-axis ticks go and what they say.
```

## 30. `unique` — numpy

What it does: Returns the distinct values of an array (optionally with a count of each) — used to find DBSCAN clusters smaller than 100 hours.
Example: `zip(*np.unique(lab[lab >= 0], return_counts=True))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.unique(arr, return_counts=True)"
Center: one large diagram illustrating a jumbled stream of label chips (2, 0, 0, 1, 2, 0, ...) entering a sorter with two exit trays: the left tray holds one chip per distinct value (0, 1, 2) and the right tray holds a matching tally card for each (3, 1, 2), connected by thin lines.
Below the diagram: a small code snippet box rendering exactly this code: zip(*np.unique(lab[lab >= 0], return_counts=True))
Caption strip at the bottom: List the distinct values in an array, with a count for each.
```

## 31. `isin` — numpy

What it does: Marks, for every element, whether it is one of a given list of values — used to flag points belonging to small clusters.
Example: `np.isin(lab, small_ids)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.isin(lab, small_ids)"
Center: one large diagram illustrating a guest-list check at a door: a short allowlist card labeled "small_ids = [1, 4]" stands beside a queue of label chips; each chip passing the gate gets stamped True (coral) if its number is on the list and False (gray) if not, producing an output row of True/False flags.
Below the diagram: a small code snippet box rendering exactly this code: n_small = int(np.isin(lab, small_ids).sum())
Caption strip at the bottom: For every element, is it in this list? — a True/False mask.
```

---
**32 new functions introduced in this module.**

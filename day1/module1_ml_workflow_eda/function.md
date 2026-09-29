# Function Reference — Module 1: The ML Workflow & Exploratory Data Analysis

Only functions introduced for the first time in this module are listed here, in the order you will meet them. Functions already covered in earlier modules are not repeated — look them up in the earlier modules' `function.md`.

## 1. `pl.read_csv(path, ...)` — polars

What it does: Reads a CSV file into a Polars DataFrame (a table of rows and columns).
Example: `pl.read_csv(DATA / "air_quality_uci.csv", separator=";", null_values="-200")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — pl.read_csv(path)"
Center: one large diagram illustrating a CSV document on the left drawn as a page of comma-separated text lines; the rows peel off the page and flow along a conveyor arrow into a neat rectangular data table with column headers on the right — raw text becomes a structured table.
Below the diagram: a small code snippet box rendering exactly this code: pl.read_csv(DATA / "air_quality_uci.csv", separator=";", null_values="-200")
Caption strip at the bottom: "read_csv() reads a CSV file into a Polars DataFrame (a table)."
```

## 2. `.shape` — polars

What it does: The size of the table as (number of rows, number of columns).
Example: `print(aq.shape)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.shape"
Center: one large diagram illustrating a data table wrapped in a measuring frame; a horizontal double-headed arrow along the bottom edge is labelled "rows" with a count, and a vertical double-headed arrow along the side is labelled "columns"; the pair is stamped in the corner as (9358, 15) — height times width.
Below the diagram: a small code snippet box rendering exactly this code: print(aq.shape)
Caption strip at the bottom: ".shape gives the table size as (rows, columns)."
```

## 3. `.head(n)` — polars

What it does: Shows the first few rows of the table so you can peek at the data.
Example: `aq.head(3)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.head(n)"
Center: one large diagram illustrating a tall data table with many rows; the top three rows are highlighted in teal and lifted out by an arrow into a small separate card in front, while the remaining rows fade to grey below — a peek at just the first rows.
Below the diagram: a small code snippet box rendering exactly this code: aq.head(3)
Caption strip at the bottom: "head() shows the first few rows of the table."
```

## 4. `df["col"]` (get one column) — polars

What it does: Pulls a single column out of the table as a Series (a one-dimensional list of values).
Example: `x = aq[col].drop_nulls()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df[\"col\"]"
Center: one large diagram illustrating a multi-column data table; one vertical column is highlighted in teal and slid out sideways by an arrow into a standalone single strip of values labelled Series, with square brackets around the column name on the extraction arrow — one column leaves the table as its own object.
Below the diagram: a small code snippet box rendering exactly this code: x = aq[col].drop_nulls()
Caption strip at the bottom: "df[\"col\"] pulls out one column as a Series."
```

## 5. `.schema` — polars

What it does: The column names and their data types — the table's structure.
Example: `aq.schema`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.schema"
Center: one large diagram illustrating a data table on the left and its blueprint on the right: a two-column list where each row shows a column name with a small type tag attached (String, Float64, Datetime) — like an architectural plan of the table's columns and types.
Below the diagram: a small code snippet box rendering exactly this code: aq.schema
Caption strip at the bottom: ".schema lists each column name and its data type."
```

## 6. `.schema.items()` — polars

What it does: Loops over the schema as (column name, data type) pairs.
Example: `for c, dtype in aq.schema.items():`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.schema.items()"
Center: one large diagram illustrating the schema blueprint opened like a drawer; column-name chips each walk out holding hands with their dtype tag (name with String, name with Float64), one pair at a time, into a for-loop arrow — iterate over the pairs.
Below the diagram: a small code snippet box rendering exactly this code: for c, dtype in aq.schema.items():
Caption strip at the bottom: "schema.items() loops over (column name, data type) pairs."
```

## 7. `pl.String` — polars

What it does: The Polars data type for text columns.
Example: `if dtype == pl.String and c not in ("Date", "Time"):`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — pl.String"
Center: one large diagram illustrating a table column filled with quoted text values ("S1", "LC-01", "2004-01-01"); a type badge reading String is clipped to the top of the column, and a sorting tray beside it shows text values grouped apart from number chips — the label that marks a column as text.
Below the diagram: a small code snippet box rendering exactly this code: if dtype == pl.String and c not in ("Date", "Time"):
Caption strip at the bottom: "pl.String is the data type for text columns."
```

## 8. `.with_columns([...])` — polars

What it does: Adds new columns or replaces existing ones, returning a new table.
Example: `aq.with_columns([pl.col(c).str.replace(",", ".").cast(pl.Float64) for c in decimal_cols])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.with_columns([...])"
Center: one large diagram illustrating a data table on the left passing through a transformation station where fresh glowing columns slide down from above and click into the table, which exits on the right with one more column than before — old columns can also be swapped for new versions in place.
Below the diagram: a small code snippet box rendering exactly this code: aq.with_columns([pl.col(c).str.replace(",", ".").cast(pl.Float64) for c in decimal_cols])
Caption strip at the bottom: "with_columns() adds or replaces columns, returning a new table."
```

## 9. `pl.col("name")` — polars

What it does: Refers to a column by name inside an expression — the handle you transform.
Example: `pl.col("Date")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — pl.col(\"name\")"
Center: one large diagram illustrating a data table with many columns; a hand-shaped cursor grabs one vertical column by a name tag reading Date, lifting it slightly out of the table with a highlight glow — pl.col() is the handle that points at a column so expressions can act on it.
Below the diagram: a small code snippet box rendering exactly this code: pl.col("Date")
Caption strip at the bottom: "pl.col() refers to a column by name inside an expression."
```

## 10. `.str.replace(old, new)` — polars

What it does: Finds and replaces text inside a string column (here: commas become decimal points).
Example: `pl.col(c).str.replace(",", ".", literal=True)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — col.str.replace(old, new)"
Center: one large diagram illustrating a column of text values like "3,5" and "2,4" passing through a find-and-replace machine; inside the machine a comma glyph morphs into a dot glyph, and the values exit as "3.5" and "2.4" — every occurrence swapped at once.
Below the diagram: a small code snippet box rendering exactly this code: pl.col(c).str.replace(",", ".", literal=True)
Caption strip at the bottom: "str.replace() finds and replaces text inside a string column."
```

## 11. `.replace(old, new)` — polars

What it does: Swaps one specific value for another in a column (here: the error code -200 becomes null).
Example: `.replace(-200.0, None)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — col.replace(old, new)"
Center: one large diagram illustrating a column of numeric cells; each cell containing -200 flips over like a tile and turns into an empty dashed cell labelled null, while all other cells stay untouched — a targeted value-for-value swap.
Below the diagram: a small code snippet box rendering exactly this code: .replace(-200.0, None)
Caption strip at the bottom: "replace() swaps one specific value for another (-200 becomes null)."
```

## 12. `.cast(dtype)` — polars

What it does: Changes a column's data type (here: text like "3,5" into real decimal numbers).
Example: `.cast(pl.Float64)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — col.cast(new_type)"
Center: one large diagram illustrating a column of text chips ("12.3", "13.1") entering a casting furnace labelled cast(pl.Float64); inside, the quotation marks burn away and the chips come out as clean numeric cells 12.3 and 13.1 with a Float64 badge — same values, new type.
Below the diagram: a small code snippet box rendering exactly this code: .cast(pl.Float64)
Caption strip at the bottom: "cast() changes a column's data type, e.g. text to decimal number."
```

## 13. `pl.Float64` — polars

What it does: The Polars data type for decimal numbers (floating-point values).
Example: `.cast(pl.Float64)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — pl.Float64"
Center: one large diagram illustrating a table column of decimal values (24.1, -0.05, 1000.5); a type badge reading Float64 is clipped to the column top, with a small ruler-and-decimal-point icon on the badge showing it is the numeric decimal type, distinct from a faded text badge beside it.
Below the diagram: a small code snippet box rendering exactly this code: .cast(pl.Float64)
Caption strip at the bottom: "pl.Float64 is the data type for decimal numbers."
```

## 14. `pl.format("{} {}", ...)` — polars

What it does: Builds a text column by gluing other columns' values into a template.
Example: `pl.format("{} {}", pl.col("Date"), pl.col("Time"))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — pl.format(\"{} {}\", ...)"
Center: one large diagram illustrating a template strip reading "{} {}" with two empty slots; two value streams — chips from a Date column (01/03/2004) and a Time column (18.00.00) — flow into the slots and fuse into one combined text chip "01/03/2004 18.00.00" — a template filled row by row.
Below the diagram: a small code snippet box rendering exactly this code: pl.format("{} {}", pl.col("Date"), pl.col("Time"))
Caption strip at the bottom: "format() builds a text column from other columns' values."
```

## 15. `.str.strptime(dtype, format)` — polars

What it does: Parses text into proper date/time values using a format pattern.
Example: `.str.strptime(pl.Datetime, format="%d/%m/%Y %H.%M.%S", strict=False)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — col.str.strptime(dtype, format)"
Center: one large diagram illustrating a text chip "01/03/2004 18.00.00" entering a parser machine guided by a stencil ruler labelled %d/%m/%Y %H.%M.%S; the chip exits as a proper calendar-and-clock icon with a Datetime badge — loose text becomes a real timestamp the computer can compute with.
Below the diagram: a small code snippet box rendering exactly this code: .str.strptime(pl.Datetime, format="%d/%m/%Y %H.%M.%S", strict=False)
Caption strip at the bottom: "str.strptime() parses text into real date/time values."
```

## 16. `pl.Datetime` — polars

What it does: The Polars data type for timestamps — dates with times.
Example: `.str.strptime(pl.Datetime, format="...")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — pl.Datetime"
Center: one large diagram illustrating a column of timestamp values each shown as a tiny calendar page fused with a clock face; a type badge reading Datetime is clipped to the column top, and a faded text-badge column beside it shows what the same values look like before parsing.
Below the diagram: a small code snippet box rendering exactly this code: .str.strptime(pl.Datetime, format="%d/%m/%Y %H.%M.%S")
Caption strip at the bottom: "pl.Datetime is the data type for real timestamps."
```

## 17. `.alias("new_name")` — polars

What it does: Renames the result of an expression — gives a computed column its name.
Example: `.alias("ts")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — expr.alias(\"name\")"
Center: one large diagram illustrating a freshly computed column sliding out of a transformation machine with no name tag; a hand clips a luggage-style name tag reading ts onto the column header — alias names the result so it can be referenced later.
Below the diagram: a small code snippet box rendering exactly this code: .alias("ts")
Caption strip at the bottom: "alias() gives the result of an expression its column name."
```

## 18. `.select(...)` — polars

What it does: Picks (and transforms) specific columns, returning a smaller table.
Example: `aq.select("ts", "CO(GT)", "T", "RH")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.select(...)"
Center: one large diagram illustrating a wide data table with 13 columns; four columns are highlighted in teal and lifted vertically out of the table into a new narrow table on the right, while the unselected columns fade grey — choose exactly the columns you want to keep.
Below the diagram: a small code snippet box rendering exactly this code: aq.select("ts", "CO(GT)", "T", "RH")
Caption strip at the bottom: "select() picks specific columns into a new table."
```

## 19. `pl.exclude(...)` — polars

What it does: Selects every column EXCEPT the ones you name.
Example: `aq.select(pl.exclude("Date", "Time"))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — pl.exclude(...)"
Center: one large diagram illustrating a data table where two named columns (Date, Time) are marked with coral exclusion tags and slide out of the selection area, while all remaining columns glow teal and move together into the result table — everyone except the named ones.
Below the diagram: a small code snippet box rendering exactly this code: aq.select(pl.exclude("Date", "Time"))
Caption strip at the bottom: "exclude() selects every column except the ones you name."
```

## 20. `.describe()` — polars

What it does: Quick summary statistics of every numeric column in one table.
Example: `aq.describe()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.describe()"
Center: one large diagram illustrating a data table feeding into a summary report card; the report shows one compact row of key figures per column — count, mean, std, min, percentiles, max — with tiny icons for each statistic, like a medical check-up chart for the data.
Below the diagram: a small code snippet box rendering exactly this code: aq.describe()
Caption strip at the bottom: "describe() gives quick summary statistics of every numeric column."
```

## 21. `.null_count()` — polars

What it does: Counts the missing values in each column.
Example: `nulls = aq.null_count().transpose(include_header=True, header_name="column", column_names=["n_null"])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.null_count()"
Center: one large diagram illustrating a data table where missing values are drawn as grey holes in the cells; a counting scanner passes over each column and reports a number above it (how many holes per column), producing a small one-row result table of counts.
Below the diagram: a small code snippet box rendering exactly this code: nulls = aq.null_count()
Caption strip at the bottom: "null_count() counts the missing values in each column."
```

## 22. `.transpose(...)` — polars

What it does: Flips rows and columns (used here to make the null report readable).
Example: `nulls.transpose(include_header=True, header_name="column", column_names=["n_null"])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.transpose(...)"
Center: one large diagram illustrating a wide, squat one-row table being rotated 90 degrees (a curved rotation arrow around it) into a tall, narrow table where each former column becomes a labelled row — rows and columns swap places.
Below the diagram: a small code snippet box rendering exactly this code: nulls.transpose(include_header=True, header_name="column")
Caption strip at the bottom: "transpose() flips rows and columns to make reports readable."
```

## 23. `.height` — polars

What it does: The number of rows in the DataFrame.
Example: `(pl.col("n_null") / aq.height * 100).round(2)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.height"
Center: one large diagram illustrating a tall data table with a vertical ruler along its left edge counting the rows from top to bottom; the ruler ends in a single number badge — height is just "how many rows", in contrast to a faded horizontal width arrow beside it.
Below the diagram: a small code snippet box rendering exactly this code: (pl.col("n_null") / aq.height * 100).round(2)
Caption strip at the bottom: ".height is the number of rows in the table."
```

## 24. `.round(n)` — polars

What it does: Rounds every value in a column to n decimal places.
Example: `(pl.col("n_null") / aq.height * 100).round(2)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — col.round(n)"
Center: one large diagram illustrating a column of long decimal values (4.37185, 12.93740) passing under a cutting gate labelled round(2); the extra digits are sliced off and the column exits with tidy two-decimal values (4.37, 12.94) — a whole column trimmed at once.
Below the diagram: a small code snippet box rendering exactly this code: (pl.col("n_null") / aq.height * 100).round(2)
Caption strip at the bottom: "round() rounds every value in a column to n decimals."
```

## 25. `.sort(col, descending)` — polars

What it does: Orders the rows by the values of a column.
Example: `nulls.sort("pct", descending=True)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.sort(\"col\")"
Center: one large diagram illustrating table rows shown as horizontal bars of different lengths (unsorted, jumbled) on the left; they slide through a sorting gate and emerge on the right stacked neatly from longest to shortest with a downward arrow — rows reordered by one column's values.
Below the diagram: a small code snippet box rendering exactly this code: nulls.sort("pct", descending=True)
Caption strip at the bottom: "sort() orders the rows by a column's values."
```

## 26. `plt.rcParams` — matplotlib.pyplot

What it does: Global plot settings — here, the list of fonts so Thai text renders correctly.
Example: `plt.rcParams["font.family"] = ["DejaVu Sans", "Noto Sans Thai", ...]`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib — plt.rcParams"
Center: one large diagram illustrating a control panel with sliders and switches labelled font.family, font size, and figure size; the panel wires out to several small chart frames that all change together when a slider moves — rcParams sets defaults for every plot at once.
Below the diagram: a small code snippet box rendering exactly this code: plt.rcParams["font.family"] = ["DejaVu Sans", "Noto Sans Thai", ...]
Caption strip at the bottom: "rcParams sets global defaults for all your plots."
```

## 27. `plt.subplots(...)` — matplotlib.pyplot

What it does: Creates a figure with one or more plotting panels (axes).
Example: `fig, axes = plt.subplots(1, 3, figsize=(13, 3.2))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib — plt.subplots(rows, cols)"
Center: one large diagram illustrating an empty picture frame being divided by dashed guide lines into a 1-by-3 grid of three empty panels; each panel hands back a small label tag — one reading fig (the whole frame) and three reading ax (the panels) — showing what subplots returns.
Below the diagram: a small code snippet box rendering exactly this code: fig, axes = plt.subplots(1, 3, figsize=(13, 3.2))
Caption strip at the bottom: "subplots() creates a figure with one or more plotting panels."
```

## 28. `.drop_nulls()` — polars

What it does: Removes rows (or values) that contain missing data.
Example: `x = aq[col].drop_nulls()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.drop_nulls()"
Center: one large diagram illustrating a data table with several grey hole cells marked as missing passing over a sieve; the hole-containing rows fall through into a discard tray below while the complete rows slide across cleanly — missing data swept away.
Below the diagram: a small code snippet box rendering exactly this code: x = aq[col].drop_nulls()
Caption strip at the bottom: "drop_nulls() removes rows with missing values."
```

## 29. `ax.hist(x, bins)` — matplotlib.pyplot

What it does: Draws a histogram — how the values of one column are distributed.
Example: `ax.hist(x, bins=40, color="#2a9d8f", edgecolor="white")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib — ax.hist(x, bins)"
Center: one large diagram illustrating a stream of dots falling from a hopper into a row of adjacent vertical bins along a number line; the bins fill to different heights forming a histogram silhouette — the shape of the data's distribution.
Below the diagram: a small code snippet box rendering exactly this code: ax.hist(x, bins=40, color="#2a9d8f", edgecolor="white")
Caption strip at the bottom: "hist() draws a histogram of a column's distribution."
```

## 30. `ax.set_title(...)` — matplotlib.pyplot

What it does: Puts a title on one plot panel.
Example: `ax.set_title(f"{col}  (n={len(x)})")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib — ax.set_title(text)"
Center: one large diagram illustrating a chart panel with an empty slot above it like a nameplate holder; a title banner slides down into the slot and clicks into place above the chart — set_title labels the panel.
Below the diagram: a small code snippet box rendering exactly this code: ax.set_title(f"{col}  (n={len(x)})")
Caption strip at the bottom: "set_title() adds a title to one plot panel."
```

## 31. `len(df)` (number of rows) — polars

What it does: Counts the rows of a DataFrame (or items of a Series) — used all over the notebooks.
Example: `n_train = int(len(aq) * 0.8)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — len(df)"
Center: one large diagram illustrating a data table with a counting hand ticking off each row beside it, finishing at a large number badge showing the row total; a small Series strip beside it shows len works on one column too.
Below the diagram: a small code snippet box rendering exactly this code: n_train = int(len(aq) * 0.8)
Caption strip at the bottom: "len() counts the rows of a DataFrame."
```

## 32. `fig.suptitle(...)` — matplotlib.pyplot

What it does: One big title spanning all panels of a figure.
Example: `fig.suptitle("การกระจายค่าของคอลัมน์ตัวอย่าง", y=1.03)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib — fig.suptitle(text)"
Center: one large diagram illustrating a figure frame containing three small chart panels, each with its own tiny local title; above the whole frame a single wide banner stretches across all three panels — the suptitle sits over everything, with a small y= position tag showing it can float slightly above.
Below the diagram: a small code snippet box rendering exactly this code: fig.suptitle("การกระจายค่าของคอลัมน์ตัวอย่าง", y=1.03)
Caption strip at the bottom: "suptitle() adds one big title across the whole figure."
```

## 33. `fig.tight_layout()` — matplotlib.pyplot

What it does: Automatically tidies spacing so titles and labels don't overlap.
Example: `fig.tight_layout()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib — fig.tight_layout()"
Center: one large diagram illustrating a two-panel figure drawn twice: on the left the panels overlap and labels stick out of the frame messily (marked with a coral warning glow); on the right the same panels snap apart into evenly spaced alignment after a tidying arrow labelled tight_layout passes over.
Below the diagram: a small code snippet box rendering exactly this code: fig.tight_layout()
Caption strip at the bottom: "tight_layout() tidies spacing so labels don't overlap."
```

## 34. `plt.show()` — matplotlib.pyplot

What it does: Renders the figure on screen.
Example: `plt.show()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib — plt.show()"
Center: one large diagram illustrating a chart being held backstage behind a theatre curtain; the curtain pulls open and the finished chart appears lit on a monitor screen facing the viewer — show() presents the completed figure.
Below the diagram: a small code snippet box rendering exactly this code: plt.show()
Caption strip at the bottom: "show() renders the plot on screen."
```

## 35. `ax.boxplot(...)` — matplotlib.pyplot

What it does: Draws box-and-whisker plots comparing the spread of several columns.
Example: `ax.boxplot([aq[c].drop_nulls() for c in sensors], tick_labels=[...])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib — ax.boxplot(data)"
Center: one large diagram illustrating five box-and-whisker glyphs side by side, one per sensor column; each box shows a thick median line, a box spanning the middle half of the data, and whiskers reaching to the extremes, with a couple of outlier dots beyond — spreads compared at a glance.
Below the diagram: a small code snippet box rendering exactly this code: ax.boxplot([aq[c].drop_nulls() for c in sensors])
Caption strip at the bottom: "boxplot() draws box-and-whisker plots to compare spreads."
```

## 36. `ax.scatter(x, y)` — matplotlib.pyplot

What it does: Draws a scatter plot of points — two columns plotted against each other.
Example: `ax.scatter(pair["co_gt"], pair[col], s=3, alpha=0.2)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib — ax.scatter(x, y)"
Center: one large diagram illustrating two data columns as parallel streams feeding into a plotting frame; each matched pair of values lands as one dot on the frame, building up a cloud of points that reveals an upward trend — every row becomes one point.
Below the diagram: a small code snippet box rendering exactly this code: ax.scatter(pair["co_gt"], pair[col], s=3, alpha=0.2)
Caption strip at the bottom: "scatter() plots each row as a point — two columns against each other."
```

## 37. `.corr()` — polars

What it does: Computes the correlation matrix of all numeric columns — how strongly each pair moves together.
Example: `corr = aq.select(cols).drop_nulls().corr()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.corr()"
Center: one large diagram illustrating several column arrows entering a comparison machine and emerging as a square grid matrix; each grid cell holds a correlation value from -1 to 1, cells shading teal for strong positive and coral for negative pairs — every column paired with every other.
Below the diagram: a small code snippet box rendering exactly this code: corr = aq.select(cols).drop_nulls().corr()
Caption strip at the bottom: "corr() computes how strongly each pair of columns moves together."
```

## 38. `.to_pandas()` — polars

What it does: Converts a Polars table into a pandas DataFrame (needed by seaborn and some pandas tools).
Example: `corr_pd = corr.to_pandas()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.to_pandas()"
Center: one large diagram illustrating a table passing through a conversion gate between two labeled zones: a teal zone with a polar-bear-like polars chip and a coral zone with a panda icon; the table keeps its exact rows and columns but changes its badge from polars to pandas as it crosses.
Below the diagram: a small code snippet box rendering exactly this code: corr_pd = corr.to_pandas()
Caption strip at the bottom: "to_pandas() converts a Polars table into a pandas DataFrame."
```

## 39. `sns.heatmap(...)` — seaborn

What it does: Draws a colored grid — here the correlation matrix with a number in each cell.
Example: `sns.heatmap(corr_pd, annot=True, fmt=".2f", cmap="RdBu_r", vmin=-1, vmax=1, ax=ax)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "seaborn — sns.heatmap(matrix)"
Center: one large diagram illustrating a square grid of cells colored from teal (positive, near 1) through white (zero) to coral (negative, near -1) along a small color legend bar; each cell carries its printed number, and row/column name tags line the edges — a correlation matrix as a heat picture.
Below the diagram: a small code snippet box rendering exactly this code: sns.heatmap(corr_pd, annot=True, fmt=".2f", cmap="RdBu_r")
Caption strip at the bottom: "heatmap() draws a colored grid of matrix values with numbers in the cells."
```

## 40. `.set_index("col")` — pandas

What it does: Makes a column the row labels of a pandas DataFrame (needed for time-series tools).
Example: `ts = ...to_pandas().set_index("ts")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "pandas — df.set_index(\"col\")"
Center: one large diagram illustrating a pandas table with a plain numbered left edge (1, 2, 3...); a timestamp column slides out of the table and rotates to become the new left-edge row labels, each timestamp now addressing its row — set_index promotes a column to the index.
Below the diagram: a small code snippet box rendering exactly this code: ts = ...to_pandas().set_index("ts")
Caption strip at the bottom: "set_index() makes a column the row labels of the table."
```

## 41. `.resample("1D")` — pandas

What it does: Groups a time series into time buckets (here: daily) so you can aggregate per period.
Example: `daily = ts.resample("1D").mean()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "pandas — ts.resample(\"1D\")"
Center: one large diagram illustrating a dense jagged stream of hourly dots flowing left to right and falling into a row of daily boxes labelled with calendar-page icons; each box collects its day's points, ready to be summarized into one value per day — a fine series regrouped into periods.
Below the diagram: a small code snippet box rendering exactly this code: daily = ts.resample("1D").mean()
Caption strip at the bottom: "resample() groups a time series into time buckets, e.g. one per day."
```

## 42. `.mean()` — pandas

What it does: The average — after resampling, one mean value per daily bucket.
Example: `daily = ts.resample("1D").mean()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "pandas — group.mean()"
Center: one large diagram illustrating three daily buckets each holding a small cluster of dots; a balance-point marker is computed within each bucket and one single averaged dot per bucket remains in a tidy output row — many points per day collapse to one mean per day.
Below the diagram: a small code snippet box rendering exactly this code: daily = ts.resample("1D").mean()
Caption strip at the bottom: "mean() averages the values in each group or bucket."
```

## 43. `ax.plot(x, y)` — matplotlib.pyplot

What it does: Draws a line connecting values — here the daily time series over dates.
Example: `ax1.plot(daily.index, daily["CO(GT)"], color="#e76f51")`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib — ax.plot(x, y)"
Center: one large diagram illustrating a series of dated points along a time axis being connected left-to-right by one continuous coral line, drawn as if a pen travels from point to point — a line chart of a value over time.
Below the diagram: a small code snippet box rendering exactly this code: ax1.plot(daily.index, daily["CO(GT)"], color="#e76f51")
Caption strip at the bottom: "plot() connects values with a line — the classic time-series chart."
```

## 44. `ax.twinx()` — matplotlib

What it does: Adds a second y-axis on the right so two different-scaled series can share one plot.
Example: `ax2 = ax1.twinx()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib — ax.twinx()"
Center: one large diagram illustrating one chart frame with a twin axis: a coral y-axis scale on the left edge and a teal y-axis scale with different numbers on the right edge, sharing the same plot area in which two lines (one per scale) are drawn — twin axes welded onto one panel.
Below the diagram: a small code snippet box rendering exactly this code: ax2 = ax1.twinx()
Caption strip at the bottom: "twinx() adds a second y-axis so two scales share one plot."
```

## 45. `fig.legend(...)` — matplotlib

What it does: Shows a legend explaining which color is which series.
Example: `fig.legend(loc="upper left", bbox_to_anchor=(0.12, 0.95))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "matplotlib — fig.legend(...)"
Center: one large diagram illustrating a chart with two differently colored lines; a small floating key card in the corner shows a short coral line sample next to the label "CO(GT) reference" and a teal sample next to "PT08.S1 sensor" — the legend translates colors into names.
Below the diagram: a small code snippet box rendering exactly this code: fig.legend(loc="upper left", bbox_to_anchor=(0.12, 0.95))
Caption strip at the bottom: "legend() shows which color is which series."
```

## 46. `train_test_split(X, y, test_size)` — sklearn.model_selection

What it does: Randomly splits the data into a training set and a held-back test set.
Example: `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sklearn — train_test_split(X, y, test_size)"
Center: one large diagram illustrating one data rectangle shuffled lightly and then cut into two blocks: a large teal block labelled train (80%) and a smaller coral block labelled test (20%) set apart with a small padlock icon meaning "do not touch until the end"; four output arrows labelled X_train, X_test, y_train, y_test leave the cut.
Below the diagram: a small code snippet box rendering exactly this code: X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
Caption strip at the bottom: "train_test_split() holds back a test set you must not peek at."
```

## 47. `.dtypes` — pandas

What it does: Lists each column's data type in a pandas DataFrame.
Example: `print(type(pdf), pdf.dtypes.tolist())`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "pandas — df.dtypes"
Center: one large diagram illustrating a pandas table with each column header wearing a small type tag (float64, int64, datetime64, object) like clipped luggage labels, and a checklist beside it reading out the tags column by column — a type inventory of the table.
Below the diagram: a small code snippet box rendering exactly this code: print(type(pdf), pdf.dtypes.tolist())
Caption strip at the bottom: "dtypes lists each column's data type."
```

## 48. `pl.from_pandas(pdf)` — polars

What it does: Converts a pandas DataFrame back into a Polars table.
Example: `back = pl.from_pandas(pdf)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — pl.from_pandas(pdf)"
Center: one large diagram illustrating the reverse conversion gate of to_pandas: a table with a panda badge crosses from the coral pandas zone back through the gate into the teal polars zone, emerging with a polars badge — same table, other engine, with a two-way arrow icon between the two zones.
Below the diagram: a small code snippet box rendering exactly this code: back = pl.from_pandas(pdf)
Caption strip at the bottom: "from_pandas() converts a pandas DataFrame back to Polars."
```

## 49. `.quantile(q)` — polars

What it does: Returns the value at a given percentile of a column (Q1 is 0.25, Q3 is 0.75).
Example: `q1 = aq["T"].quantile(0.25)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — series.quantile(q)"
Center: one large diagram illustrating a sorted row of dots along a number line with a coral flag at the 25% position labelled Q1 and a teal flag at the 75% position labelled Q3; the flags cut the sorted data into quarters — quantile reads off the value at any cut point.
Below the diagram: a small code snippet box rendering exactly this code: q1 = aq["T"].quantile(0.25)
Caption strip at the bottom: "quantile() returns the value at a given percentile of the data."
```

## 50. `.filter(condition)` — polars

What it does: Keeps only the rows that match a condition.
Example: `outliers = aq.filter((pl.col("T") < lo) | (pl.col("T") > hi))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.filter(condition)"
Center: one large diagram illustrating table rows flowing through a funnel gate guarded by a condition sign reading "T < lo OR T > hi"; only rows passing the test continue into the output tray while rejected rows bounce off into a faded side pile — a row sieve.
Below the diagram: a small code snippet box rendering exactly this code: outliers = aq.filter((pl.col("T") < lo) | (pl.col("T") > hi))
Caption strip at the bottom: "filter() keeps only the rows matching a condition."
```

## 51. `.min()` — polars

What it does: The smallest value in a column.
Example: `outliers["T"].min()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — series.min()"
Center: one large diagram illustrating a row of dots of varying heights along a number line; a coral arrow points down to the lowest dot, which is circled and carries a badge labelled min — the floor of the column.
Below the diagram: a small code snippet box rendering exactly this code: outliers["T"].min()
Caption strip at the bottom: "min() gives the smallest value in a column."
```

## 52. `.max()` — polars

What it does: The largest value in a column.
Example: `outliers["T"].max()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — series.max()"
Center: one large diagram illustrating a row of dots of varying heights along a number line; a teal arrow points up to the highest dot, which is circled and carries a badge labelled max — the ceiling of the column, the mirror image of min.
Below the diagram: a small code snippet box rendering exactly this code: outliers["T"].max()
Caption strip at the bottom: "max() gives the largest value in a column."
```

## 53. `.tail(n)` — polars

What it does: Takes the last n rows of the table.
Example: `test = aq.tail(len(aq) - n_train)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — df.tail(n)"
Center: one large diagram illustrating a tall data table whose bottom three rows are highlighted in coral and lifted out by a downward arrow into a small card, while the rows above fade grey — head's mirror image, peeking at the end of the table.
Below the diagram: a small code snippet box rendering exactly this code: test = aq.tail(len(aq) - n_train)
Caption strip at the bottom: "tail() takes the last n rows of the table."
```

## 54. `.date()` — polars

What it does: Extracts just the date part from a datetime value (dropping the time).
Example: `test["ts"].min().date().isoformat()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "polars — dt.date()"
Center: one large diagram illustrating a datetime chip shown as a calendar page fused with a clock face; the clock part detaches and drops away, leaving only the calendar page labelled with the plain date — peel the time off a timestamp.
Below the diagram: a small code snippet box rendering exactly this code: test["ts"].min().date().isoformat()
Caption strip at the bottom: "date() extracts just the date part of a datetime."
```

---

Total: 54 new functions introduced in this module (including `df["col"]`, column selection by name).

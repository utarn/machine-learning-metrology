# Function Reference — Module 0: Environment & Python Basics

Only functions introduced for the first time in this module are listed here, in the order you will meet them. Functions already covered in earlier modules are not repeated — look them up in the earlier modules' `function.md`.

## 1. `print(...)` — python

What it does: Displays values on the screen so you can see what your code produced.
Example: `print(load_g, n_readings, sensor_id, is_calibrated)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — print(...)"
Center: one large diagram illustrating a computer terminal window at the right, with the word "print" on a small button at the left; the values 100.0, 40 and "LC-01" fly along curved arrows out of the code editor and land as a single text line inside the terminal screen, showing exactly what goes in (values) and what comes out (visible output text).
Below the diagram: a small code snippet box rendering exactly this code: print(load_g, n_readings, sensor_id, is_calibrated)
Caption strip at the bottom: "print() displays values on the screen so you can see what your code produced."
```

## 2. `type(...)` — python

What it does: Tells you what kind of value something is (int, float, str, bool).
Example: `print(type(load_g), type(n_readings))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — type(x)"
Center: one large diagram illustrating a magnifying glass held over four small value chips (100.0, 40, "LC-01", True); each chip gets a stamped label tag underneath reading "float", "int", "str", "bool" — the function looks at a value and reports its type tag.
Below the diagram: a small code snippet box rendering exactly this code: print(type(load_g), type(n_readings))
Caption strip at the bottom: "type() tells you what kind of value something is."
```

## 3. `abs(...)` — python

What it does: Absolute value — drops the minus sign from a number.
Example: `abs(v) >= 0.02`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — abs(x)"
Center: one large diagram illustrating a horizontal number line with zero in the middle; a dot at -0.05 on the left is connected by a folding arrow across the zero point to a dot at +0.05 on the right, with the minus sign visually clipped off and floating away — distance from zero stays the same.
Below the diagram: a small code snippet box rendering exactly this code: abs(v) >= 0.02
Caption strip at the bottom: "abs() gives the absolute value — it drops the minus sign."
```

## 4. `sum(...)` — python

What it does: Adds up all the numbers in a list and returns one total.
Example: `mean = sum(values) / len(values)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — sum(list)"
Center: one large diagram illustrating a column of numbered chips (10.0, 20.0, 30.0) sliding down a funnel into one large plus symbol, and a single output chip labelled with the total emerging at the bottom — many numbers in, one sum out.
Below the diagram: a small code snippet box rendering exactly this code: mean = sum(values) / len(values)
Caption strip at the bottom: "sum() adds up all the numbers in a list and gives you one total."
```

## 5. `len(...)` — python

What it does: Counts how many items are in a list, dict, or string.
Example: `v_std = (sum((v - v_mean) ** 2 for v in vals) / len(vals)) ** 0.5`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — len(x)"
Center: one large diagram illustrating a horizontal row of five small boxes; a measuring ruler runs along the top of the row with tick marks touching each box, and a big circular count badge at the end displays the number 5 — the function walks the row and counts the items.
Below the diagram: a small code snippet box rendering exactly this code: n = len(vals)
Caption strip at the bottom: "len() counts how many items are in a list, dict, or string."
```

## 6. `round(...)` — python

What it does: Rounds a number to a given number of decimal places.
Example: `{k: round(v, 2) for k, v in z_scores.items()}`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — round(x, n)"
Center: one large diagram illustrating the long number 24.73186 on the left, with a pair of scissors cutting after the second decimal; the trailing digits "186" fall away as small cut-off scraps, and the tidy result 24.73 sits on the right in a highlighted chip.
Below the diagram: a small code snippet box rendering exactly this code: round(v, 2)
Caption strip at the bottom: "round() shortens a number to the decimal places you ask for."
```

## 7. `zip(...)` — python

What it does: Pairs up items from two lists side by side, like a zipper.
Example: `sum(w * v for w, v in zip(weights, values))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — zip(a, b)"
Center: one large diagram illustrating two horizontal rows of chips — the top row labelled weights (0.5, 0.3, 0.2) and the bottom row labelled values (10.0, 20.0, 30.0) — being zipped together by an actual zipper pull in the middle, producing vertical pairs (0.5 with 10.0, 0.3 with 20.0, 0.2 with 30.0) joined by small connector links.
Below the diagram: a small code snippet box rendering exactly this code: sum(w * v for w, v in zip(weights, values))
Caption strip at the bottom: "zip() pairs up items from two lists side by side, like a zipper."
```

## 8. `int(...)` — python

What it does: Converts a value to a whole number (chopping off the decimal part).
Example: `n_outliers = int((np.abs(readings - mean) > 2 * std).sum())`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — int(x)"
Center: one large diagram illustrating the number 3.7 on the left; its decimal tail ".7" detaches and drops into a small discard bin below, while the clean whole number 3 sits in a highlighted chip on the right — the value becomes a counting-style whole number.
Below the diagram: a small code snippet box rendering exactly this code: n_outliers = int(...)
Caption strip at the bottom: "int() converts a value to a whole number."
```

## 9. `float` — python

What it does: The decimal-number data type — measurements are almost always floats.
Example: `load_g = 100.0  # float`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — float"
Center: one large diagram illustrating a measurement chip showing 100.0 with its decimal point glowing and circled; above it hangs a tag labelled "float", and beside it a small whole number 100 with a crossed-out tag showing that without the decimal point it would be an int instead.
Below the diagram: a small code snippet box rendering exactly this code: load_g = 100.0  # float
Caption strip at the bottom: "float is the decimal-number type — measured values are floats."
```

## 10. `str` — python

What it does: The text data type — names, labels, and dates-as-text are strings.
Example: `sensor_id = "LC-01"  # str`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — str"
Center: one large diagram illustrating the characters L C - 0 1 sitting inside a pair of large quotation marks that act like a container box around them; a hanging tag labelled "str" is attached to the container, showing that quoted text is a string value.
Below the diagram: a small code snippet box rendering exactly this code: sensor_id = "LC-01"  # str
Caption strip at the bottom: "str is the text type — anything in quotes is a string."
```

## 11. `bool` — python

What it does: The True/False data type — the answer to every yes/no question in code.
Example: `is_calibrated = True  # bool`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — bool"
Center: one large diagram illustrating a large two-position toggle switch with only two settings: a teal position labelled True (with a check mark) and a grey position labelled False (with a cross); the lever points to True, and a tag labelled "bool" hangs from the switch.
Below the diagram: a small code snippet box rendering exactly this code: is_calibrated = True  # bool
Caption strip at the bottom: "bool is the True/False type — a switch with only two states."
```

## 12. `list` — python

What it does: An ordered collection of values kept in one variable.
Example: `channels = ["ch1", "ch2", "ch3"]`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — list"
Center: one large diagram illustrating three labelled boxes ("ch1", "ch2", "ch3") lined up left to right inside a pair of square brackets that hold them together like a tray; small position numbers 0, 1, 2 sit under the boxes to show order, and a tag labelled "list" hangs above.
Below the diagram: a small code snippet box rendering exactly this code: channels = ["ch1", "ch2", "ch3"]
Caption strip at the bottom: "list is an ordered collection of values in one variable."
```

## 13. `dict` — python

What it does: A collection of key:value pairs — look up a value by its name.
Example: `offsets = {"ch1": 0.02, "ch2": -0.05, "ch3": 0.01}`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — dict"
Center: one large diagram illustrating a small two-column lookup table inside curly braces; the left column holds keys "ch1", "ch2", "ch3" and the right column holds values 0.02, -0.05, 0.01, with arrows from each key to its value; a tag labelled "dict" hangs above.
Below the diagram: a small code snippet box rendering exactly this code: offsets = {"ch1": 0.02, "ch2": -0.05, "ch3": 0.01}
Caption strip at the bottom: "dict stores key:value pairs — look up a value by its key."
```

## 14. `def` — python

What it does: Defines your own reusable function — a named machine with inputs.
Example: `def to_celsius(temp_f: float) -> float:`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — def"
Center: one large diagram illustrating a machine being assembled from a blueprint: the blueprint sheet shows the machine's name plate "to_celsius", an input funnel on the left labelled temp_f, and an output pipe on the right; the keyword def is written on the blueprint header — def declares the machine before it runs.
Below the diagram: a small code snippet box rendering exactly this code: def to_celsius(temp_f: float) -> float:
Caption strip at the bottom: "def defines your own reusable function — a named machine with inputs."
```

## 15. `return` — python

What it does: Sends the function's result back to whoever called it.
Example: `return (temp_f - 32) * 5 / 9`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — return"
Center: one large diagram illustrating a function machine box with an input funnel on the left receiving the value 68.0, gears working inside, and the finished result 20.0 sliding out of an output chute on the right along an arrow labelled "return" toward a waiting hand — the keyword return is printed on the output chute.
Below the diagram: a small code snippet box rendering exactly this code: return (temp_f - 32) * 5 / 9
Caption strip at the bottom: "return sends the function's result back out to the caller."
```

## 16. `assert` — python

What it does: Checks a condition; stops with an error if it is False (used to verify exercise answers).
Example: `assert abs(celsius_to_kelvin(25.0) - 298.15) < 1e-9`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — assert"
Center: one large diagram illustrating a checkpoint gate across a conveyor belt: a value chip passes through a scanner; if the condition holds, a big green check mark lights up and the chip continues; a second faded lane shows a red stop barrier where a failing chip is halted. The word assert is written on the scanner housing.
Below the diagram: a small code snippet box rendering exactly this code: assert abs(celsius_to_kelvin(25.0) - 298.15) < 1e-9
Caption strip at the bottom: "assert checks a condition and stops with an error if it is False."
```

## 17. `items()` (dict method) — python

What it does: Loops over a dict as key–value pairs, giving you both parts at once.
Example: `for name, version in pinned.items():`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — dict.items()"
Center: one large diagram illustrating a dict box opened like a drawer; inside, three key:value pairs (python: 3.14.x, numpy: 2.5.3, polars: 1.44.2) walk out in single file, each key holding hands with its value, ready to be looped over one pair at a time; the method name .items() is printed on the drawer handle.
Below the diagram: a small code snippet box rendering exactly this code: for name, version in pinned.items():
Caption strip at the bottom: "items() loops over a dict as key–value pairs."
```

## 18. `**` (power operator) — python

What it does: Raises a number to a power (here used for squared deviations and square roots via ** 0.5).
Example: `std = (sum((v - mean) ** 2 for v in values) / len(values)) ** 0.5`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — ** (power operator)"
Center: one large diagram illustrating a base block labelled 2 with a smaller raised block labelled 3 stacked up-and-to-the-right like a step, connected by the two-star symbol ** ; an arrow leads to the result 8. A second smaller example shows 9 ** 0.5 = 3 with a square-root sign above it.
Below the diagram: a small code snippet box rendering exactly this code: (v - mean) ** 2
Caption strip at the bottom: "** raises a number to a power — squaring, or ** 0.5 for square roots."
```

## 19. `math.sqrt(...)` — math

What it does: Square root of a single number.
Example: `math.sqrt(2)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "math — math.sqrt(x)"
Center: one large diagram illustrating a large radical (square-root) sign with the number 2 tucked under it and the result 1.414... emerging to the right; a small right triangle with legs 1 and 1 and hypotenuse labelled sits beside it to show where the root comes from; the prefix math. is on a small import badge.
Below the diagram: a small code snippet box rendering exactly this code: math.sqrt(2)
Caption strip at the bottom: "math.sqrt() gives the square root of one number at a time."
```

## 20. `math.isfinite(...)` — math

What it does: Checks that a value is a real number (not infinity or NaN).
Example: `all(math.isfinite(v) for v in vals)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "math — math.isfinite(x)"
Center: one large diagram illustrating a quality-control gate: three chips approach it — an ordinary number 24.2 passes through with a green check, a chip showing the infinity symbol and a chip showing NaN are both turned away with small red crosses; the gate is labelled isfinite.
Below the diagram: a small code snippet box rendering exactly this code: all(math.isfinite(v) for v in vals)
Caption strip at the bottom: "isfinite() checks a value is a real number, not infinity or NaN."
```

## 21. `np.array(...)` — numpy

What it does: Turns a Python list into a numpy array so math works on the whole thing at once.
Example: `readings = np.array([24.1, 24.3, 24.0, 24.2, 24.1])`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.array(list)"
Center: one large diagram illustrating five loose numbered chips scattered on the left, flowing through a funnel labelled np.array, and snapping into one neat connected row of linked cells on the right with a subtle glow — a scattered list becomes one mathematical object that can be operated on all at once.
Below the diagram: a small code snippet box rendering exactly this code: readings = np.array([24.1, 24.3, 24.0, 24.2, 24.1])
Caption strip at the bottom: "np.array() turns a Python list into a numpy array for whole-array math."
```

## 22. `.mean()` (array method) — numpy

What it does: The average of all values in the array.
Example: `readings.mean()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — arr.mean()"
Center: one large diagram illustrating a row of dots at different heights on a small chart; a coral triangular fulcrum sits under the exact balance point of the dots, labelled mean — like a seesaw balanced at the average; an arrow from the array of dots points to the single computed value.
Below the diagram: a small code snippet box rendering exactly this code: readings.mean()
Caption strip at the bottom: ".mean() gives the average — the balance point of all the values."
```

## 23. `.std()` (array method) — numpy

What it does: Standard deviation — how spread out the values are around the mean.
Example: `readings.std()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — arr.std()"
Center: one large diagram illustrating a bell-shaped cluster of dots around a central mean line; a horizontal double-headed arrow spans from the mean out to a typical dot, bracketed and labelled std — a wider spread gives a longer arrow, shown as a faded wider second bell behind.
Below the diagram: a small code snippet box rendering exactly this code: readings.std()
Caption strip at the bottom: ".std() measures the spread — the typical distance from the mean."
```

## 24. `.shape` (array attribute) — numpy

What it does: The size/dimensions of the array, as a tuple (used to check the answer).
Example: `assert readings.shape == (1000,)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — arr.shape"
Center: one large diagram illustrating a 1-D row of cells on the left with a stamped label (1000,) next to it, and a faded 2-D grid on the right with the label (rows, columns); a measuring frame wraps around each array reporting its dimensions — shape answers "how big is this array?".
Below the diagram: a small code snippet box rendering exactly this code: assert readings.shape == (1000,)
Caption strip at the bottom: ".shape reports the size and dimensions of the array."
```

## 25. `np.sqrt(...)` — numpy

What it does: Square root applied to every element of an array at once.
Example: `np.sqrt(np.array([2.0, 4.0, 8.0]))`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.sqrt(array)"
Center: one large diagram illustrating a row of three cells holding 2.0, 4.0, 8.0 passing under one wide radical (square-root) sign drawn as a gate over the whole row, and emerging on the right as 1.41, 2.0, 2.83 — one operation applied to every element simultaneously, arrows element-by-element.
Below the diagram: a small code snippet box rendering exactly this code: np.sqrt(np.array([2.0, 4.0, 8.0]))
Caption strip at the bottom: "np.sqrt() takes the square root of every element of an array at once."
```

## 26. `np.abs(...)` — numpy

What it does: Absolute value of every element of an array.
Example: `np.abs(readings - mean) > 2 * std`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.abs(array)"
Center: one large diagram illustrating a wave line that dips below a horizontal zero axis on the left; the below-zero parts fold upward across the axis like a mirror, becoming a fully positive wave on the right — every negative element flips to positive while positives pass through unchanged.
Below the diagram: a small code snippet box rendering exactly this code: np.abs(readings - mean) > 2 * std
Caption strip at the bottom: "np.abs() makes every element positive — distances from the mean."
```

## 27. `np.random.default_rng(seed)` — numpy

What it does: Creates a random-number generator with a fixed seed, so "random" results are the same every run.
Example: `rng = np.random.default_rng(42)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — np.random.default_rng(seed)"
Center: one large diagram illustrating a dice with a padlock and key inserted into its side, the key tagged seed = 42; two identical output tapes unroll from two copies of the dice showing exactly the same sequence of numbers — locking the seed makes the randomness reproducible.
Below the diagram: a small code snippet box rendering exactly this code: rng = np.random.default_rng(42)
Caption strip at the bottom: "default_rng(seed) creates a reproducible random-number generator."
```

## 28. `rng.normal(loc, scale, size)` — numpy

What it does: Draws random values from a bell-shaped (normal) distribution — simulated measurement noise.
Example: `noise = rng.normal(loc=0.0, scale=0.5, size=5)`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "numpy — rng.normal(loc, scale, size)"
Center: one large diagram illustrating a bell curve with its peak marked loc (the center) and a shaded band marked scale (the width); dots are being dropped from a small hopper and land clustered under the bell, dense near the peak and sparse at the tails — samples drawn from the distribution.
Below the diagram: a small code snippet box rendering exactly this code: noise = rng.normal(loc=0.0, scale=0.5, size=5)
Caption strip at the bottom: "rng.normal() draws random values from a bell-shaped distribution."
```

## 29. `Path.cwd()` — pathlib

What it does: Gives the folder the notebook is currently running from.
Example: `cwd = Path.cwd()`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "pathlib — Path.cwd()"
Center: one large diagram illustrating a file-system tree of folders drawn as connected folder icons; a large coral map pin drops onto the folder labelled "you are here", marking the current working directory that Path.cwd() returns.
Below the diagram: a small code snippet box rendering exactly this code: cwd = Path.cwd()
Caption strip at the bottom: "Path.cwd() tells you which folder the notebook is running from."
```

## 30. `Path / "name"` (join path) — pathlib

What it does: Joins a folder path and a name together with the / operator, safely.
Example: `data = cwd / "datasets"`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "pathlib — Path / \"name\""
Center: one large diagram illustrating two folder blocks — one labelled cwd and one labelled "datasets" — sliding together and joining through a large slash / connector in the middle, producing a single combined path block on the right; a small crossed-out string-glue icon shows why you should not paste text paths by hand.
Below the diagram: a small code snippet box rendering exactly this code: data = cwd / "datasets"
Caption strip at the bottom: "The / operator joins folder and name into one safe path."
```

## 31. `.exists()` — pathlib

What it does: Checks whether a file or folder actually exists on disk.
Example: `if (cwd / "datasets").exists():`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "pathlib — path.exists()"
Center: one large diagram illustrating a magnifying glass inspecting two folders side by side: the first folder is solid and gets a green check mark labelled True, the second is drawn as a faint dashed outline and gets a red cross labelled False — exists() answers "is this really there?".
Below the diagram: a small code snippet box rendering exactly this code: if (cwd / "datasets").exists():
Caption strip at the bottom: ".exists() checks whether a file or folder actually exists."
```

## 32. `sys.version` — sys

What it does: A text string describing the running Python version.
Example: `sys.version.split()[0]`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "sys — sys.version"
Center: one large diagram illustrating a small ID-card for the Python interpreter: a rounded card with a simple snake logo and a long version string printed on it ("3.14.2 | packaged by ..."), with the version number at the start highlighted by a coral outline — sys.version is the interpreter's self-description.
Below the diagram: a small code snippet box rendering exactly this code: sys.version.split()[0]
Caption strip at the bottom: "sys.version is a text string describing the running Python version."
```

## 33. `.split()` (str method) — python

What it does: Splits text into pieces at the spaces (here, to grab just the version number).
Example: `sys.version.split()[0]`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "python — text.split()"
Center: one large diagram illustrating one long strip of text being cut at its spaces by small scissors into separate word chips laid out in a row; the first chip is highlighted with a coral outline and an arrow labelled [0] picks it up — indexing into the split pieces.
Below the diagram: a small code snippet box rendering exactly this code: sys.version.split()[0]
Caption strip at the bottom: "split() cuts text into pieces — take the piece you need."
```

## 34. `numpy.__version__` (version-check idiom) — environment

What it does: Reports the installed version of a library — the same `.__version__` idiom works for pandas, polars, sklearn, xgboost, and matplotlib, letting you confirm your environment matches the course pins.
Example: `"numpy": numpy.__version__`

**Image prompt:**
```
Create a single educational illustration card for a data-science course, flat vector infographic style, plain white background, soft muted colors (teal, coral, dark slate blue), clean sans-serif labels, no photorealism, no 3D, no gradients.

Title at the top: "environment — library.__version__"
Center: one large diagram illustrating a shelf of six small library boxes labelled numpy, pandas, polars, sklearn, xgboost, matplotlib; each box has an ID badge clipped to it showing its version number (2.5.3, 3.0.6, 1.44.2, 1.9.1, 3.4.1, 3.11.2); a magnifying glass hovers over the numpy badge with the attribute path numpy.__version__ written beside it — the same badge idiom works on every box.
Below the diagram: a small code snippet box rendering exactly this code: "numpy": numpy.__version__
Caption strip at the bottom: "Check each library's installed version against the course pins."
```

---

Total: 34 new functions introduced in this module.

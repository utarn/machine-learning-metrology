# Smoke test for the ML for Metrology course environment.
# Run:  uv run python smoke_test.py   (or: python smoke_test.py in an activated venv)
# Prints library versions, then exercises the core workflow:
# polars read -> sklearn fit/predict -> matplotlib render. Ends with a clear pass/fail line.

import sys
import tempfile
from pathlib import Path

failures = []

def check(label, fn):
    try:
        fn()
        print(f"  OK   {label}")
    except Exception as exc:  # noqa: BLE001 - report any failure and continue
        failures.append((label, exc))
        print(f"  FAIL {label}: {exc}")

def check_versions():
    import matplotlib, numpy, pandas, polars, pyarrow, seaborn
    import sklearn, xgboost, shap, streamlit, joblib, jupyterlab, ipykernel

    versions = {
        "python": sys.version.split()[0],
        "numpy": numpy.__version__,
        "pandas": pandas.__version__,
        "pyarrow": pyarrow.__version__,
        "polars": polars.__version__,
        "matplotlib": matplotlib.__version__,
        "seaborn": seaborn.__version__,
        "scikit-learn": sklearn.__version__,
        "xgboost": xgboost.__version__,
        "shap": shap.__version__,
        "streamlit": streamlit.__version__,
        "joblib": joblib.__version__,
    }
    for name, ver in versions.items():
        print(f"  {name}=={ver}")

def check_polars():
    import polars as pl
    import tempfile
    df = pl.DataFrame({"x": [1.0, 2.0, 3.0], "y": ["a", "b", "c"]})
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "smoke.csv"
        df.write_csv(p)
        back = pl.read_csv(p)
    assert back.shape == (3, 2) and back["x"].sum() == 6.0

def check_sklearn():
    from sklearn.linear_model import LinearRegression
    import numpy as np
    rng = np.random.default_rng(42)
    X = rng.normal(size=(50, 2))
    y = X @ np.array([2.0, -1.0]) + 0.1 * rng.normal(size=50)
    model = LinearRegression().fit(X, y)
    pred = model.predict(X[:5])
    assert pred.shape == (5,)

def check_matplotlib():
    import matplotlib
    matplotlib.use("Agg")  # no display needed in a smoke test
    import matplotlib.pyplot as plt
    import tempfile
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2], [0, 1, 4])
    with tempfile.TemporaryDirectory() as tmp:
        fig.savefig(Path(tmp) / "smoke.png")
    plt.close(fig)

print("ML for Metrology course environment smoke test")
print("Versions:")
check("versions import + print", check_versions)
print("Core workflow:")
check("polars write/read CSV", check_polars)
check("scikit-learn fit + predict", check_sklearn)
check("matplotlib render to file", check_matplotlib)

print()
if failures:
    print("ไม่ผ่าน (FAIL) — environment is NOT ready:")
    for label, exc in failures:
        print(f"  - {label}: {exc}")
    sys.exit(1)
print("ผ่าน (PASS) — environment is ready. สภาพแวดล้อมพร้อมใช้งาน")

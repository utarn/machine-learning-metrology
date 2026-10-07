# Smoke test for the ML for Metrology course environment.
# Run: uv run python smoke_test.py (or: python smoke_test.py in a venv)
# Prints library versions, then exercises the core workflow:
# polars read -> sklearn fit/predict -> torch tensor math -> matplotlib render.
# Ends with a clear pass/fail line.
#
# Covers the full offline v2 stack (requirements-offline.txt). The packages
# removed from the main stack in #21 (xgboost / shap / streamlit) belonged to
# the v1 material, which is archived on branch archive/v1-course and no
# longer ships with the course (retired in #34).

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
    import matplotlib
    import numpy
    import pandas
    import polars
    import pyarrow
    import seaborn
    import sklearn
    import joblib
    import torch
    import torchvision
    import torchaudio
    import transformers
    import datasets

    versions = {
        "python": sys.version.split()[0],
        "numpy": numpy.__version__,
        "pandas": pandas.__version__,
        "pyarrow": pyarrow.__version__,
        "polars": polars.__version__,
        "matplotlib": matplotlib.__version__,
        "seaborn": seaborn.__version__,
        "scikit-learn": sklearn.__version__,
        "joblib": joblib.__version__,
        "torch": torch.__version__,
        "torchvision": torchvision.__version__,
        "torchaudio": torchaudio.__version__,
        "transformers": transformers.__version__,
        "datasets": datasets.__version__,
    }
    for name, ver in versions.items():
        print(f"  {name}=={ver}")


def check_polars():
    import polars as pl
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


def check_torch():
    import torch
    x = torch.arange(6, dtype=torch.float32).reshape(2, 3)
    assert x.sum().item() == 15.0  # CPU is the expected path on lab machines


def check_librosa():
    import librosa
    import numpy as np
    y = np.sin(2 * np.pi * 440 * np.linspace(0, 0.2, 4410))
    mfcc = librosa.feature.mfcc(y=y, sr=22050, n_mfcc=5)
    assert mfcc.shape[0] == 5


def check_matplotlib():
    import matplotlib
    matplotlib.use("Agg")  # no display needed in a smoke test
    import matplotlib.pyplot as plt
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
check("torch tensor math (CPU)", check_torch)
check("librosa MFCC", check_librosa)
check("matplotlib render to file", check_matplotlib)

print()
if failures:
    print("ไม่ผ่าน (FAIL) — environment is NOT ready:")
    for label, exc in failures:
        print(f"  - {label}: {exc}")
    sys.exit(1)
print("ผ่าน (PASS) — environment is ready. สภาพแวดล้อมพร้อมใช้งาน")

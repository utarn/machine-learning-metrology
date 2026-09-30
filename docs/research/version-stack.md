# Pinned Version Stack — ML for Advanced Metrology Research

Researched: 2026-09-29. Sources: PyPI JSON API, endoflife.date, official release notes
(pandas blog, scikit-learn whatsnew/highlights, xgboost changelog, shap GitHub releases,
polars GitHub releases, uv installation docs).

> **Update 2026-09-30 (v2 stack, #21/#25):** the pins above describe the v1 stack.
> The v2 course (unstructured data) splits into two pinned files —
> `requirements-offline.txt` (CPU: adds PyTorch base torch 2.14.0 /
> torchvision 0.29.0 / torchaudio 2.11.0, transformers 5.17.0, datasets 5.0.1,
> easyocr 1.7.2, pytesseract 0.3.13, surya-ocr 0.22.1, anomalib 2.6.2,
> librosa 1.0.0, pythainlp 5.3.8, jiwer 4.0.0) and `requirements-kaggle.txt`
> (GPU: transformers/datasets/librosa/demucs 4.1.0/jiwer/pythainlp — torch comes
> preinstalled on Kaggle). xgboost / shap / streamlit left the main stack; they
> survive only in the transitional `v1-legacy` dependency group. Resolution note:
> uv locks only the target platforms (`tool.uv.environments`) because shap's
> darwin-x86_64 `numba<0.63` pin conflicts with librosa 1.0.0 / numpy 2.5.

> **Update 2026-09-30 (#27, M2 Thai OCR):** surya-ocr 0.22.1 was replaced by
> **surya-ocr 0.16.7** and transformers 5.17.0 by **4.57.6** (both files). Reason:
> surya >= 0.20 rewrote layout/table-rec/recognition as a VLM inference stack that
> requires a llama-server binary (system package) plus a multi-GB GGUF download —
> incompatible with the offline-CPU constraint and the Windows learner path. 0.17.x
> still ships plain torch models, but its layout task is the foundation-model
> token-decoder and it degenerates on real pages (measured on our synthetic
> calibration-report pages: a dense table+figure page came back as ONE
> `PageHeader` box), so **0.16.7 — the last release with the dedicated layout
> model — is the pin** (verified: layout returns 11 sensible boxes on the same
> page; table-rec 23 rows / 5 cols / 115 cells; both CPU, offline after cache
> populate). Both 0.16.7 and 0.17.x vendor code against transformers 4.x
> internals, hence the 4.57.6 pin — thai-trocr / Whisper / mBERT all work on
> 4.57. With 0.16.7 the M2 notebooks need only the **layout (~240 MB)** and
> **table-rec (~210 MB)** models (not the 1.4 GB foundation model). Model caches
> for pre-bundle: EasyOCR `~/.EasyOCR`, thai-trocr HF cache (`HF_HOME`), Surya
> `MODEL_CACHE_DIR` (default per-OS datalab cache dir; manifest-based local-only
> check → no network once the dir is populated).

> **Update 2026-09-30 (#34, v1 retired):** the v1 modules in `day1/`–`day3/`
> were removed (material lives only on `archive/v1-course`), so the
> transitional `v1-legacy` dependency group (xgboost / shap / streamlit) and
> the `darwin-x86_64` exclusion it forced were dropped from
> `pyproject.toml`/`uv.lock`. The pins below describe the v1 stack and are
> kept as the research record only — the live pins are
> `requirements-offline.txt` / `requirements-kaggle.txt` above.

## Pinned versions (ready for requirements.txt)

```text
# requirements.txt — verified 2026-09-29
numpy==2.5.3
pandas==3.0.6
pyarrow==25.0.1          # strongly recommended alongside pandas 3.0 (backing for the str dtype)
polars==1.44.2
matplotlib==3.11.2
seaborn==0.13.2
scikit-learn==1.9.1
xgboost==3.4.1
shap==0.52.0
streamlit==1.64.0
joblib==1.6.0
jupyterlab==4.6.4
ipykernel==7.3.0
```

Tooling (installed per machine, not in requirements.txt):

```text
uv==0.12.20
CPython: 3.14.7 (latest stable) — primary
         3.13.15 (previous stable) — fallback for Windows-lab machines
```

Suggested `pyproject.toml` guard: `requires-python = ">=3.13,<3.15"`.

## Python version

- Latest stable CPython: **3.14.7** (EOL 2030-10).
- Previous stable: **3.13.15** (EOL 2029-10) — keep as the Windows-lab fallback.
- Every package in the stack ships wheels for both 3.13 and 3.14:
  - numpy 2.5.3, scikit-learn 1.9.1, matplotlib 3.11.2: explicit `cp314` wheels.
  - polars 1.44.2: now a pure-Python wrapper; binary comes from `polars-runtime-*`
    (abi3) — installs on any CPython >= 3.10.
  - xgboost 3.4.1: `py3-none-{win_amd64, macosx, manylinux}` wheels — version-agnostic.
  - shap 0.52.0: `cp312-abi3` wheels (cover 3.12/3.13/3.14) plus `cp314t` free-threaded wheels.
  - numba 0.67.0 (pulled in by shap): `cp314` wheels exist; caps `numpy<2.6` — compatible with numpy 2.5.x.

Recommendation: teach on **3.14.7**; if any lab machine has a problem (e.g. GPU/driver or
corporate image quirks), 3.13.15 is fully supported by the same pin set.

## Pairwise compatibility notes

| Pair | Status |
|---|---|
| shap 0.52.0 × numpy 2.5.3 | OK. shap requires `numpy>=2` (SPEC 0 minimums raised in 0.52, May 2026); no upper bound. Numba constraint `numpy<2.6` is satisfied by 2.5.3. |
| shap × CPython 3.14 | OK. 0.50 (Nov 2025) dropped Python 3.9/3.10 and began testing against 3.14; 0.52 ships abi3 + cp314t wheels; 0.53.0rc0 already tests 3.15rc. shap no longer lags — minimum Python is 3.12. |
| shap × scikit-learn 1.9 | OK (shap lists scikit-learn as an unconditional dependency, no version cap). |
| shap × xgboost 3.4 | OK — xgboost is in shap's test matrix; TreeExplainer supports XGBoost 3.x. |
| macOS Intel quirk | On `darwin ×86_64` only, shap pins `numba<0.63` / `llvmlite<0.46`. Windows lab machines are unaffected. |
| xgboost 3.4.1 × scikit-learn 1.9.1 | OK. The sklearn interface (`XGBClassifier`, `XGBRegressor`, `fit/predict/score`) is unchanged; xgboost 3.4 even "corrected scikit-learn input tags". Notable 3.4 deprecations: the random-forest wrapper classes are deprecated (use `num_parallel_tree`), and `trees_to_dataframe()` now uses pandas `NA` instead of mixing `np.nan`/`None`. Default binaries are built against CUDA 13.3 (use `xgboost-cu12` if a lab needs CUDA 12.9). |
| streamlit 1.64.0 × pandas 3.0.6 | OK — streamlit declares `pandas<4,>=1.4.0`, so 3.0.x is the supported major. Also pins `pyarrow !=25.0.0,<26` → pyarrow 25.0.1 satisfies it. Pins `numpy<3,>=1.23` → 2.5.3 OK. |
| seaborn 0.13.2 × pandas 3.0 / numpy 2.5 / matplotlib 3.11 | OK in practice. seaborn declares loose floors only (`numpy>=1.20`, `pandas>=1.2`, `matplotlib>=3.4`) with no caps; it is pure Python so there are no wheel issues. Caveat: last release was Sept 2023 — expect a few FutureWarnings, and a 0.14 aligned with the pandas `str` dtype is likely eventually. |
| scikit-learn 1.9.1 × pandas 3.0.6 | OK. sklearn depends on `narwhals` for dataframe-agnostic input handling; 1.8/1.9 track pandas 3.0 (1.9.1, Sept 2026, includes pandas-array-API fixes). |
| joblib 1.6.0 × sklearn 1.9.1 | OK — sklearn requires `joblib>=1.4.0`, no cap. |
| polars 1.44.2 × numpy 2.5 | OK (`numpy>=1.16` optional extra; interop via `to_numpy()`/`from_numpy`). |

## Breaking API changes in the last year that affect beginner teaching code

1. **pandas 3.0.0 (21 Jan 2026) — the big one.** If any course material was written for
   pandas 2.x, review it:
   - **Copy-on-Write is now the only mode.** Chained assignment such as
     `df["col"][df["other"] > 5] = x` silently stops working — must use
     `df.loc[mask, "col"] = x`. The `SettingWithCopyWarning` is gone. Defensive `.copy()`
     calls are no longer needed.
   - **New default `str` dtype** for string columns (instead of `object`). Code that
     checks `df.dtypes == object` to find text columns breaks; use `pandas.api.types.is_string_dtype`
     or `dtype == "str"`. Strings are pyarrow-backed when pyarrow is installed — hence
     pyarrow is pinned in requirements.
   - **Default datetime resolution changed** from nanoseconds to microseconds (or the
     input's resolution) — old overflow behavior for pre-1678/post-2262 dates differs.
   - New `pd.col()` callable syntax for `assign`; all pre-3.0 deprecations removed
     (migrate any 2.x code through 2.3 warning-free first).
2. **scikit-learn 1.9 (Sept 2026)** is additive: experimental callbacks API, HTML
   representation of estimators now shows fitted attributes, `metric_at_thresholds`,
   opt-in `sparse_interface="sparray"`. No teaching-code breakage. The removals that
   bit old tutorials happened in the 1.6 (mid-2025) "API repair" release — any material
   older than mid-2025 should be re-run once against 1.9.
3. **polars**: 1.x API has been stable since 1.0 (July 2024) — teaching idioms
   (`pl.scan_csv`/`pl.read_csv`, `group_by` (not pandas' `groupby`), expressions,
   `LazyFrame.collect()`, `df.write_csv`) are unchanged. Minor recent deprecations
   (1.44, Aug 2026): `rechunk` parameter on read/scan functions and `Expr.rechunk()`
   deprecated. Note packaging change: polars is now a thin pure-Python wrapper around
   `polars-runtime-32/64` packages (since 1.43) — irrelevant to users, but a reason to
   pin the full `polars==1.44.2` (uv resolves the matching runtime automatically).
   **A polars 2.0.0rc2 exists (Sept 2026)** — uv/pip will not select RCs by default, but
   do not loosen the pin to `polars>=1`; keep `==1.44.x` (or `>=1.44,<2`) until 2.0
   final ships.
4. **Teaching pandas vs polars idioms**: with pandas 3.0's CoW + `str` dtype + `pd.col()`,
   pandas and polars have converged noticeably (immutable-ish semantics, expression-like
   APIs). Chained-assignment examples are now wrong in *both* libraries — update any
   side-by-side comparison notebooks accordingly.

## uv on Windows for the classroom

uv 0.12.20 supports Windows 10+ well: single standalone binary, no Python needed up front
(uv can install/manage CPython itself via `uv python install`), first-class
`pyproject.toml`/`uv.lock` workflow.

One-click PowerShell setup (the currently recommended command from the uv docs):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then, in the course repo:

```powershell
uv sync          # creates .venv from uv.lock and installs all pinned deps
uv run jupyter lab   # or: .venv\Scripts\Activate.ps1
```

Notes for the lab setup:
- Pin the installer version for reproducibility:
  `irm https://astral.sh/uv/0.12.20/install.ps1 | iex`.
- `uv python install 3.14` (or 3.13) inside the lab avoids needing a system Python
  installer at all.
- Commit `uv.lock` so every classroom machine gets byte-identical packages.
- If `Set-ExecutionPolicy` is blocked on lab images, uv is also on PyPI
  (`pip install uv`) and as a plain .exe from GitHub releases.

## Summary of risks

- Low risk overall: all pins are mutually compatible and have Windows/macOS wheels.
- Biggest teaching-content risk is **pandas 3.0** semantics (CoW + str dtype), not
  installation.
- Watch items: polars 2.0 (RC out — do not unpin), seaborn 0.14 (overdue release),
  shap 0.53 final (drops numba/llvmlite entirely — only an improvement).

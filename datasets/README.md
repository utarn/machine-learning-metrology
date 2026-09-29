# Shared datasets

Public datasets used across the course, downloaded and committed so every notebook runs offline.
Citations must be repeated in the first markdown cell of every notebook that uses a dataset
(see `docs/research/datasets.md` for BibTeX).

| File | Used in | Source | License |
|---|---|---|---|
| `Pontius.dat` | `day1/regression/` | NIST StRD "Pontius" load-cell calibration — https://www.itl.nist.gov/div898/strd/lls/data/Pontius.shtml | Public domain (US Gov). Citation: Pontius, P., NIST. *Load Cell Calibration*. NIST StRD. |
| `ccpp_power_plant.csv` | `day1/ml_workflow_eda/`, `day1/feature_engineering/`, `day1/regression/`, Module 5 (regression metrics) | UCI Combined Cycle Power Plant — https://doi.org/10.24432/C5002N | CC BY 4.0. Citation: Tüfekci, P. & Kaya, H. (2014). *Combined Cycle Power Plant* [Data set]. UCI ML Repository. |
| `air_quality_uci.csv` | `day1/ml_workflow_eda/`, Module 6 | UCI Air Quality — https://doi.org/10.24432/C59K5F | CC BY 4.0. Citation: De Vito, S., et al. (2008). *Air Quality* [Data set]. UCI ML Repository. |
| `secom.zip` (not yet committed — Day 2) | Module 4/5, Capstone B | UCI SECOM — https://doi.org/10.24432/C54305 | CC BY 4.0 |

Notes:

- `ccpp_power_plant.csv` was converted once from the official `Folds5x2_pp.xlsx`
  (values unchanged; verified 9,568 × 5, columns `AT, V, AP, RH, PE`).
- `air_quality_uci.csv` is the official file as-is: semicolon-separated, decimal **comma**,
  missing values tagged `-200` — parsing it is part of the Day-1 EDA lesson.
- `Pontius.dat` is the official NIST StRD ASCII file (40 observations + certified values header).

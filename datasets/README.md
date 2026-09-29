# Shared datasets

Public datasets used across the course, downloaded and committed so every notebook runs offline.
Citations must be repeated in the first markdown cell of every notebook that uses a dataset
(see `docs/research/datasets.md` for BibTeX).

| File | Used in | Source | License |
|---|---|---|---|
| `Pontius.dat` | `day1/module3_regression/` | NIST StRD "Pontius" load-cell calibration — https://www.itl.nist.gov/div898/strd/lls/data/Pontius.shtml | Public domain (US Gov). Citation: Pontius, P., NIST. *Load Cell Calibration*. NIST StRD. |
| `ccpp_power_plant.csv` | `day1/module1_ml_workflow_eda/`, `day1/module2_feature_engineering/`, `day1/module3_regression/`, Module 5 (regression metrics) | UCI Combined Cycle Power Plant — https://doi.org/10.24432/C5002N | CC BY 4.0. Citation: Tüfekci, P. & Kaya, H. (2014). *Combined Cycle Power Plant* [Data set]. UCI ML Repository. |
| `air_quality_uci.csv` | `day1/module1_ml_workflow_eda/`, Module 6 | UCI Air Quality — https://doi.org/10.24432/C59K5F | CC BY 4.0. Citation: De Vito, S., et al. (2008). *Air Quality* [Data set]. UCI ML Repository. |
| `secom.zip` | `day2/module4_classification/`, `day2/module5_evaluation/`, Capstone B | UCI SECOM — https://doi.org/10.24432/C54305 | CC BY 4.0. Citation: McCann, M. & Johnston, A. (2008). *SECOM* [Data set]. UCI ML Repository. |
| `machine_temperature_system_failure.csv` | `day2/module7_anomaly_detection/` | Numenta Anomaly Benchmark (NAB), `realKnownCause/machine_temperature_system_failure` — https://github.com/numenta/NAB | MIT. Citation: Ahmad, S., et al. (2017). "Unsupervised real-time anomaly detection for streaming data", *Neurocomputing* 262. |
| `nab_machine_temperature_labels.json` | `day2/module7_anomaly_detection/` | NAB companion anomaly-window labels — https://github.com/numenta/NAB/blob/master/labels/combined_windows.json | MIT (same repo). |
| `co2_mm_gl.csv` | `day3/module8_time_series/`, Capstone C | NOAA GML globally-averaged CO₂ monthly means — https://gml.noaa.gov/ccgg/trends/ | Public domain (US Gov); fair credit required per file header. Citation: Lan, X., Thoning, K.W., Dlugokencky, E.J. *Trends in globally-averaged CO₂*, NOAA GML, Version 2026-09. |
| `cmapss_turbofan.zip` | Capstone A | NASA C-MAPSS Turbofan Engine Degradation Simulation Data Set — https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/ | Free, attribution required (no OSS license). Citation: Saxena, A., Goebel, K., Simon, D., Eklund, N. (2008). "Damage propagation modeling for aircraft engine run-to-failure simulation", *Proc. PHM 2008*. |

Notes:

- `ccpp_power_plant.csv` was converted once from the official `Folds5x2_pp.xlsx`
  (values unchanged; verified 9,568 × 5, columns `AT, V, AP, RH, PE`).
- `air_quality_uci.csv` is the official file as-is: semicolon-separated, decimal **comma**,
  missing values tagged `-200` — parsing it is part of the Day-1 EDA lesson.
- `Pontius.dat` is the official NIST StRD ASCII file (40 observations + certified values header).
- `secom.zip` is the official UCI zip, unmodified (contains `secom.data` — 1,567 × 590
  space-separated features, many NaNs — plus `secom_labels.data` with label `-1` = PASS /
  `1` = FAIL and a quoted timestamp; opening it with `zipfile` is part of the lesson).
- `machine_temperature_system_failure.csv` is the official NAB file as-is (22,696 rows of
  `timestamp,value`, 5-minute sampling); `nab_machine_temperature_labels.json` holds the
  4 hand-labeled anomaly windows for the same series.
- `co2_mm_gl.csv` is the official NOAA GML file as-is: `#` comment header (the credit
  policy lives in it), then `year,month,decimal,average,average_unc,trend,trend_unc` —
  missing months carry the sentinel `-99.99` (handling it is part of the Module 8 lesson).
- `cmapss_turbofan.zip` is the official inner `CMAPSSData.zip` from NASA PCoE, unmodified
  (contains `train/test_FD001..FD004.txt`, `RUL_FD00xx.txt`, the readme and the Saxena
  2008 paper; opening it with `zipfile` is part of Capstone A).

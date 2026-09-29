# Dataset selection per module (research ticket)

**Date:** 2026-09-29 · **Branch:** `research/datasets`
**Status policy (locked):** popular public datasets are PREFERRED; any dataset requiring citation is fine — citation + source URL must be shown in every notebook that uses it. Deterministic seeded synthetic data is the fallback ONLY where no public counterpart fits the metrology story.

**Verification:** every URL below was fetched (HTTP 200) and the data files actually downloaded/inspected on 2026-09-29. See [Verification log](#appendix-verification-log).

---

## Summary table

| Module | Case study | Primary dataset | License / credit | Shape | Fallback |
|---|---|---|---|---|---|
| 3 | Sensor calibration curve | **NIST StRD "Pontius"** (load-cell calibration) + **UCI Combined Cycle Power Plant** for multivariate ridge/lasso | Public domain (US Gov) / CC BY 4.0 | 40 obs (1×1) / 9,568 × 5 | Optional seeded `calib_multisensor` |
| 4 | Pass/Fail QC classification | **UCI SECOM** (semiconductor manufacturing) | CC BY 4.0 (DOI 10.24432/C54305) | 1,567 × 591 (590 features + Pass/Fail) | Hydraulic condition monitoring (UCI 601) |
| 5 | Evaluation metrics demo | **Reuse SECOM** (+ CCPP for regression metrics / TimeSeriesSplit-style CV) | — | as above | none needed |
| 6 | Clustering devices by T/RH response | **UCI Air Quality** (gas multisensor device) | CC BY 4.0 (DOI 10.24432/C59K5F) | 9,358 hourly rows × 13 features | Hydraulic condition monitoring |
| 7 | Anomaly detection on telemetry | **NAB `machine_temperature_system_failure`** | MIT (repo) + Aharon/Ahmad et al. paper | 22,696 rows (timestamp, value) | Seeded drift/shift generator (sketched) |
| 8 | Forecasting reference drift | **NOAA GML globally-averaged CO2** (`co2_mm_gl.csv`) | US Gov, freely available; credit requested in file header | 572 monthly rows (1979–2026) | Seeded reference-drift generator (sketched) |
| Capstone A | Predictive maintenance | **NASA C-MAPSS** Turbofan Engine Degradation (PCoE) | NASA PCoE — free, attribution required (no OSS license) | 4 runs FD001–FD004, 21 sensors + 3 op settings, RUL target | FEMTO/PRONOSTIA bearing (1.16 GB — too big for classroom download) |
| Capstone B | Pass/fail classifier | **Reuse SECOM** | — | as above | — |
| Capstone C | Drift predictor | **Reuse NOAA `co2_mm_gl`** (or NAB) | — | as above | — |

---

## Module 3 — Sensor Calibration Curve (linear / ridge / lasso / polynomial, extrapolation warning)

### Primary: NIST Statistical Reference Datasets (StRD) — "Pontius" load-cell calibration
- **What it is:** real NIST load-cell calibration data — 40 observations, 1 response variable `y`, 1 predictor `x` (load), certified least-squares quadratic model. It is literally a metrology calibration dataset, published by NIST for benchmarking regression fitting.
- **URL:** https://www.itl.nist.gov/div898/strd/lls/data/Pontius.shtml (data file: https://www.itl.nist.gov/div898/strd/lls/data/LINKS/DATA/Pontius.dat) — verified HTTP 200.
- **License:** U.S. Government work → public domain (17 USC §105). Attribution courtesy is still shown in the course notebooks.
- **Citation (plain):** Pontius, P., NIST. *Load Cell Calibration*. NIST Statistical Reference Datasets (StRD), https://www.itl.nist.gov/div898/strd/lls/data/Pontius.shtml
- **Size/shape:** 40 observations, 1 predictor + 1 response; ASCII file.
- **Column mapping for the metrology case:** `x` → applied load (kg) to a mass comparator; `y` → instrument reading. Use for: OLS line vs. quadratic fit, residual analysis, and the **extrapolation warning** (fit on the lower-load range, predict beyond the calibration span — this is the natural place to teach "calibration curves are only valid inside their accredited range").
- **Limits:** single predictor → not suitable for ridge/lasso. That is what the companion dataset below is for.

### Companion (for ridge / lasso / multiple predictors): UCI Combined Cycle Power Plant (CCPP)
- **What it is:** 9,568 data points over 6 years (2006–2011) from a combined-cycle power plant at full load: 4 environmental/process features → net electrical output.
- **URL:** https://archive.ics.uci.edu/dataset/294/combined+cycle+power+plant — direct zip: https://archive.ics.uci.edu/static/public/294/combined+cycle+power+plant.zip — verified HTTP 200.
- **License:** CC BY 4.0.
- **DOI / citation:** Tüfekci, P. & Kaya, H. (2014). *Combined Cycle Power Plant* [Data set]. UCI Machine Learning Repository. https://doi.org/10.24432/C5002N
- **Size/shape:** 9,568 × 5 (`AT`, `V`, `AP`, `RH`, `PE`).
- **Column mapping:** `AT` ambient temperature (°C, 1.81–37.11) → "environmental temperature at the measuring rig"; `V` exhaust vacuum → "sensor channel 2"; `AP` ambient pressure (hPa) → "barometric pressure measurement"; `RH` relative humidity (%) → "humidity sensor"; `PE` → "measured response (mV)". Ridge/lasso on correlated T/RH/pressure channels demonstrates shrinkage on noisy co-located sensors; polynomial features on `AT` + extrapolation beyond the observed temperature range gives the extrapolation warning in a multivariate setting.

### Optional synthetic fallback: `calib_multisensor` (only if instructor wants planted effects)
Deterministic generator (seed 42):
- Columns: `temp_c` (rig temperature), `load_g` (applied load), `ch1_mv`, `ch2_mv`, `ch3_mv` (3 sensor-channel readings), `ref_mv` (reference reading).
- Noise model: heteroscedastic Gaussian — σ(x) = 0.05 + 0.002·x (noisier at high load), plus mild AR(1) correlation across repeated readings of the same load point.
- Planted effects: ch1 linear gain + small temperature cross-sensitivity; ch2 quadratic-in-load term (so plain OLS undershoots at the extremes); ch3 sticky zero-drift over the session (bias ramps with reading order); 60 training points clustered in [10, 90] °C plus 6 held-out extrapolation points in [95, 120] °C to trigger the extrapolation warning.

**Recommendation:** use Pontius as the headline "this is real calibration data from NIST" example and CCPP for regularized multivariate regression; the synthetic generator is optional, not needed by policy.

---

## Module 4 — Pass/Fail QC classification (logistic regression, SVM, random forest, XGBoost; tolerance limits)

### Primary: UCI SECOM
- **What it is:** data from a semiconductor manufacturing process — the classic industrial pass/fail QC dataset, widely used in ML-for-manufacturing courses.
- **URL:** https://archive.ics.uci.edu/dataset/179/secom — direct zip: https://archive.ics.uci.edu/static/public/179/secom.zip — verified HTTP 200 and downloaded (1.9 MB zip).
- **License:** CC BY 4.0.
- **DOI:** https://doi.org/10.24432/C54305
- **Citation (plain):** McCann, M. & Johnston, A. (2008). *SECOM* [Data set]. UCI Machine Learning Repository. https://doi.org/10.24432/C54305
- **Size/shape (verified):** 1,567 rows × 591 columns — `secom.data`: 590 process/sensor features (values space-separated, many NaNs); `secom.labels.data`: label `-1` = PASS, `1` = FAIL plus timestamp. Only **104 fails (~6.6%)** — strong class imbalance, which is exactly the point: threshold choice ≈ tolerance-limit choice.
- **Column mapping for the metrology case:** features → "process sensor/probe measurements on the line"; label → "unit passes final gauge check (-1) / fails (1)"; timestamp → to demonstrate that samples arrive in production order (split by time, not randomly). Use the NaN density to teach imputation strategy before comparing logistic regression / SVM / RF / XGBoost. The "tolerance limits" tie-in: adjust the decision threshold against the cost of letting a bad unit pass.
- **Synthetic fallback:** not needed.

### Alternative (if a richer tolerance-limit story is wanted): UCI "Condition monitoring of hydraulic systems"
- **URL:** https://archive.ics.uci.edu/dataset/601/condition+monitoring+of+hydraulic+systems — verified HTTP 200.
- **License:** CC BY 4.0; **DOI:** https://doi.org/10.24432/C5HS5C
- **Citation (plain):** Helwig, N., Pignanelli, E., Schütze, A. (2015). *Condition monitoring of a complex hydraulic system using multivariate statistics*; *Condition Monitoring of Hydraulic Systems* [Data set]. UCI Machine Learning Repository. https://doi.org/10.24432/C5HS5C
- **Shape:** 2,205 cycles × 17 sensor aggregates (e.g., temperature sensors `TS1–TS4`, pressure `PS1–PS6`, flow) + target columns incl. internal pump leakage and valve condition (`y_valve`: 73 / 80 / 90 / 100 %) — valve condition maps directly onto "tolerance limits" teaching (binarize at 90% and discuss where the limit should sit).
- **Recommendation:** keep as alternative; SECOM remains primary because it is the canonical, most-referenced pass/fail dataset.

---

## Module 5 — Model evaluation metrics demo

**Reuse SECOM** (confusion matrix, ROC-AUC, PR-AUC, cross-validation on an imbalanced industrial QC problem — ideal because accuracy alone is meaningless at 6.6% positives). For regression metrics (R², RMSE, residual plots) reuse **CCPP** from Module 3. No new dataset, no extra citation burden beyond Modules 3–4.

---

## Module 6 — Clustering devices by temperature/humidity response behavior (K-Means, DBSCAN, PCA)

### Primary: UCI Air Quality (gas multisensor device)
- **What it is:** hourly responses of a metal-oxide gas multisensor device deployed on the field in an Italian city (Sept 2004 – Feb 2005), recorded alongside reference concentrations from a certified analyzer plus temperature and humidity. The 5 PT08 sensor channels under varying T/RH are the clustering story.
- **URL:** https://archive.ics.uci.edu/dataset/360/air+quality — direct zip: https://archive.ics.uci.edu/static/public/360/air+quality.zip — verified HTTP 200 and downloaded.
- **License:** CC BY 4.0.
- **DOI:** https://doi.org/10.24432/C59K5F
- **Citation (plain):** De Vito, S., Massera, E., Piga, M., Martinotto, L., Di Francia, G. (2008). "On field calibration of an electronic nose for benzene estimation in an urban pollution monitoring scenario", *Sensors and Actuators B: Chemical*, 129(2), 750–757; *Air Quality* [Data set]. UCI Machine Learning Repository. https://doi.org/10.24432/C59K5F
- **Size/shape (verified):** 9,358 hourly instances × 13 features. Columns (semicolon-separated CSV, decimal comma — needs explicit parsing note in the notebook): `Date`, `Time`, `CO(GT)`, `PT08.S1(CO)`, `NMHC(GT)`, `C6H6(GT)`, `PT08.S2(NMHC)`, `NOx(GT)`, `PT08.S3(NOx)`, `NO2(GT)`, `PT08.S4(NO2)`, `PT08.S5(O3)`, `T` (°C), `RH` (%), `AH` (absolute humidity). Missing values tagged **-200**.
- **Column mapping for the metrology case:** the 5 `PT08.S*` columns → "response of sensor device k"; `T`, `RH` → the temperature/humidity axis of the case study. Two workable framings:
  1. **Cluster operating regimes** — rows (hours) clustered on `[PT08.S1..S5, T, RH]`; K-Means finds environmental/regime clusters, DBSCAN flags anomalous regimes, PCA (on sensor responses) shows how the 5 channels collapse into a few response modes that correlate with T/RH.
  2. **Cluster devices** — build a per-channel response profile (each PT08 channel's sensitivity/offset fitted as a function of T and RH, then normalize) and cluster the 5 channels — small but pedagogically closest to "cluster devices by their T/RH response behavior".
  Framing 1 is the robust one for class exercises; framing 2 works as the worked demo.
- **Synthetic fallback:** not needed.
- **Alternative:** UCI hydraulic condition monitoring (DOI 10.24432/C5HS5C, above) — cluster sensor channels / cycles by temperature-driven behavior.

---

## Module 7 — Anomaly detection on daily telemetry (drift, sudden shift; Isolation Forest, One-Class SVM)

### Primary: Numenta Anomaly Benchmark (NAB) — `machine_temperature_system_failure`
- **What it is:** real industrial telemetry — internal temperature of a large industrial machine, sampled near-continuously for ~3 months, with hand-labeled anomalies (failures and shutdowns): sudden shifts, prolonged dropouts, and drift-like behavior. The most widely used public telemetry anomaly series.
- **URL:** https://github.com/numenta/NAB (raw file: https://raw.githubusercontent.com/numenta/NAB/master/data/realKnownCause/machine_temperature_system_failure.csv) — verified HTTP 200, downloaded, **22,696 rows**.
- **License:** **MIT** (repo LICENSE, confirmed via GitHub API) — attribution in the notebook suffices.
- **Citation (plain):** Ahmad, S., Lavin, A., Purdy, S., Agha, Z. (2017). "Unsupervised real-time anomaly detection for streaming data", *Neurocomputing*, 262, 134–147. Data: Numenta Anomaly Benchmark (NAB), https://github.com/numenta/NAB (MIT License). Companion labels file: https://raw.githubusercontent.com/numenta/NAB/master/labels/combined_windows.json
- **Size/shape:** 1 CSV ≈ 732 KB; 2 columns: `timestamp`, `value`.
- **Column mapping for the metrology case:** `timestamp` → "probe/sensor telemetry clock"; `value` → "probe internal temperature (°C)" or any monitored channel. Teaching flow: rolling baseline + Isolation Forest on window features (mean/std/slope) → sudden-shift detection (machine shutdowns); One-Class SVM on stationary segment → flagging the degradation periods; discuss why long slow drift is the hard case for both.
- **Limit & synthetic fallback (justified):** NAB labels the *sudden* anomalies; it does not ship a labeled slow-drift ground truth. If the lesson needs a controlled drift detector exercise, add a deterministic seeded variant of the same series format (same 2 columns):
  - Baseline: slow diurnal sinusoid (24 h period, amplitude ~2 units) around 90 units.
  - Planted effects: (a) linear drift +0.01/step for 3 weeks mid-series; (b) abrupt level shift of −8 units (sustained); (c) 15 point-anomalies (σ spikes); (d) variance inflation segment (degradation). Noise: Gaussian σ=0.8, seed 42, so every student regenerates identical data.

### Alternative (degradation-progression story): NASA FEMTO/PRONOSTIA bearing dataset
- **URL:** https://phm-datasets.s3.amazonaws.com/NASA/10.+FEMTO+Bearing.zip (listed on the NASA PCoE data set repository, https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/) — verified HTTP 200, **1.16 GB**.
- **Citation:** Nectoux, P., et al. (2012). "PRONOSTIA: An experimental platform for bearings accelerated degradation tests." IEEE PHM 2012.
- **Note:** real run-to-failure degradation traces (vibration), ideal for "gradual degradation vs. sudden shift", but too heavy for classroom download — use pre-extracted features or keep as instructor demo only.

---

## Module 8 — Time-series forecasting of standard-reference drift (trend/seasonality, lag features, TimeSeriesSplit)

### Primary: NOAA GML globally-averaged CO2 monthly means (`co2_mm_gl.csv`)
- **What it is:** globally-averaged atmospheric CO2, monthly, 1979–present: a clean monotone long-term trend (→ "reference drift") plus a regular seasonal cycle (→ "seasonal environmental response"). This is the classic trend+seasonality teaching series and is exactly the shape of a standard drifting over time.
- **URL:** https://gml.noaa.gov/ccgg/trends/data.html — direct file: https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_gl.csv — verified HTTP 200, downloaded (24.7 KB).
- **License:** freely available; U.S. Government work. The data-use policy in the file header **requires fair credit** ("please include relevant citation text").
- **Citation (plain):** Lan, X., Thoning, K.W., Dlugokencky, E.J.: *Trends in globally-averaged CO2 determined from NOAA Global Monitoring Laboratory measurements*, Version 2026-09, https://gml.noaa.gov/ccgg/trends/ (contact per file header: Xin Lan, NOAA GML).
- **Size/shape (verified):** 572 monthly rows; columns `year, month, decimal, average, average_unc, trend, trend_unc` (units: ppm; missing months present as NaN).
- **Column mapping for the metrology case:** `decimal` (decimal year) → time since last reference calibration; `average` → "measured offset of the working standard vs. reference (ppm)" — taught as drift magnitude; `trend` → the smooth drift component to recover by lag-feature regression; the seasonal residual → "environmental seasonality". Exercises: STL decomposition, lag features (t−1, t−12), forward-only `TimeSeriesSplit` CV, and the honest point that a drifting standard extrapolated beyond its recalibration interval is exactly the Module 3 extrapolation warning, revisited.
- **Synthetic fallback sketch (if the instructor insists on a true reference-standard story):** deterministic generator (seed 42), columns: `days_since_calibration`, `offset_uv`, `temp_lab_c`; drift model `offset = a·t + b·√t + c·sin(2πt/365.25) + ε`, ε ~ N(0, σ) with σ inflating after a mid-series "contamination event" and 2 planted recalibration resets (offset jumps to 0).

---

## Capstone tracks

| Track | Dataset | Reuse of |
|---|---|---|
| A. Predictive maintenance | **NASA C-MAPSS — Turbofan Engine Degradation Simulation Data Set** | new dataset |
| B. Pass/fail classifier | **SECOM** | Module 4/5 |
| C. Drift predictor | **NOAA `co2_mm_gl`** (or NAB for anomaly-adjacent framing) | Module 8 (or 7) |

### C-MAPSS details
- **URL:** NASA PCoE Data Set Repository: https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/ (verified 200). Direct zip (Turbofan Engine Degradation Simulation Data Set, "Data Set 1"): https://phm-datasets.s3.amazonaws.com/NASA/6.+Turbofan+Engine+Degradation+Simulation+Data+Set.zip — verified HTTP 200, 12.4 MB. Data Set 2: `17.+Turbofan+Engine+Degradation+Simulation+Data+Set+2.zip`.
- **License:** freely distributed by NASA PCoE; no OSS license attached — **attribution required** (cite the paper below and NASA PCoE). Acceptable under the locked policy.
- **Citation (plain):** Saxena, A., Goebel, K., Simon, D., Eklund, N. (2008). "Damage propagation modeling for aircraft engine run-to-failure simulation", *Proc. PHM 2008*; data via NASA Prognostics Center of Excellence (PCoE) Data Set Repository.
- **Shape:** 4 subsets FD001–FD004 (train + test + RUL ground truth); per-unit time series with 3 operating settings + 21 sensor channels; target = Remaining Useful Life (RUL).
- **Mapping for the metrology story:** engines ≡ "instruments in service"; sensor channels ≡ "gauge channels"; RUL ≡ "time-to-next-recalibration". This keeps the capstone consistent with the course's metrology framing while using the canonical PHM dataset.

---

## Citation-block requirement (applies to every notebook)

Per the locked policy, every notebook using any of the above must display, in its first markdown cell, the dataset name, the source URL, the license, and the citation string given above. BibTeX for the key ones:

```bibtex
@misc{secom2008,
  author = {McCann, Michael and Johnston, Allyson},
  title  = {SECOM},
  year   = {2008},
  howpublished = {UCI Machine Learning Repository},
  doi    = {10.24432/C54305}
}

@misc{airquality2008,
  author = {De Vito, Saverio and Massera, Ettore and Piga, Marco and Martinotto, Luca and Di Francia, Girolamo},
  title  = {Air Quality},
  year   = {2008},
  howpublished = {UCI Machine Learning Repository},
  doi    = {10.24432/C59K5F}
}

@article{devito2008,
  author  = {De Vito, Saverio and Massera, Ettore and Piga, Marco and Martinotto, Luca and Di Francia, Girolamo},
  title   = {On field calibration of an electronic nose for benzene estimation in an urban pollution monitoring scenario},
  journal = {Sensors and Actuators B: Chemical},
  volume  = {129}, number = {2}, pages = {750--757}, year = {2008}
}

@misc{ccpp2014,
  author = {T{\"u}fekci, P{\i}nar and Kaya, Heysem},
  title  = {Combined Cycle Power Plant},
  year   = {2014},
  howpublished = {UCI Machine Learning Repository},
  doi    = {10.24432/C5002N}
}

@article{ahmad2017nab,
  author  = {Ahmad, Subutai and Lavin, Alexander and Purdy, Scott and Agha, Zahra},
  title   = {Unsupervised real-time anomaly detection for streaming data},
  journal = {Neurocomputing}, volume = {262}, pages = {134--147}, year = {2017}
}

@inproceedings{saxena2008cmapss,
  author    = {Saxena, Abhinav and Goebel, Kai and Simon, Don and Eklund, Neil},
  title     = {Damage propagation modeling for aircraft engine run-to-failure simulation},
  booktitle = {Proc. 1st Int. Conf. on Prognostics and Health Management (PHM 2008)},
  year      = {2008}
}

@inproceedings{nectoux2012pronostia,
  author    = {Nectoux, Patrick and Gouriveau, Rafael and Medjaher, Kamal and Ramasso, Emmanuel and Morello, Brigitte Chebel and Zerhouni, Noureddine and Darouti, Christophe},
  title     = {PRONOSTIA: An experimental platform for bearings accelerated degradation tests},
  booktitle = {IEEE Int. Conf. on Prognostics and Health Management (PHM'12)},
  year      = {2012}
}
```

NIST StRD (Pontius) is a U.S. Government work (public domain) — cite by URL and attribution: "Pontius, P., NIST. Load Cell Calibration. NIST StRD, https://www.itl.nist.gov/div898/strd/lls/data/Pontius.shtml". NOAA GML data likewise public-domain with required credit (see file header).

---

## Appendix: verification log (2026-09-29)

| Resource | Check | Result |
|---|---|---|
| UCI SECOM zip (`/static/public/179/secom.zip`) | HTTP GET + unzip | 200; 1.9 MB; `secom.data` 1,567 lines × 590 features; labels -1/1 with timestamps |
| UCI SECOM page | license + DOI | CC BY 4.0; DOI 10.24432/C54305 |
| UCI Air Quality zip (`/static/public/360/air+quality.zip`) | HTTP GET + unzip | 200; 9,472-line CSV (9,358 data rows), 13 features + Date/Time, sep `;`, decimal `,` |
| UCI Air Quality page | license + DOI | CC BY 4.0; DOI 10.24432/C59K5F |
| UCI CCPP zip (`/static/public/294/...`) | HTTP HEAD | 200 |
| UCI CCPP page | license + DOI | CC BY 4.0; DOI 10.24432/C5002N |
| UCI hydraulic condition monitoring page | license + DOI | 200; CC BY 4.0; DOI 10.24432/C5HS5C |
| NIST StRD Pontius `.dat` + info page | HTTP GET | 200; 40 obs, 1×1, certified quadratic; US Gov public domain |
| NAB `machine_temperature_system_failure.csv` | HTTP GET + line count | 200; 732 KB; 22,696 rows |
| NAB repo license | GitHub API `license` field | MIT |
| NOAA `co2_mm_gl.csv` | HTTP GET | 200; 24.7 KB; 572 monthly rows; credit policy in file header |
| NASA PCoE repository page + C-MAPSS zip | HTTP HEAD | 200; 12.4 MB |
| NASA FEMTO bearing zip | HTTP HEAD | 200; 1.16 GB (too large for classroom) |

No dataset on the primary list requires synthetic fallback; the two sketched generators (Module 7 planted-drift variant, Module 8 reference-drift variant, Module 3 `calib_multisensor`) are optional extensions for planted-effect teaching, not policy-driven fallbacks.

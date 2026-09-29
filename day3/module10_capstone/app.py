"""Streamlit demo — Drift Predictor & Recalibration Interval (Capstone C, Module 10)

รัน:  uv run streamlit run day3/module10_capstone/app.py

Demo ของแทร็ก C: โหลดซีรีส์ drift จริง (NOAA CO₂ แมปเป็น "ค่าเบี่ยงเบนของ
working standard"), เทรนโมเดล linear บน lag features, พยากรณ์แบบ recursive
พร้อมแถบความไม่แน่นอน แล้วให้ผู้ใช้เลื่อน tolerance เพื่อดู recalibration
interval ที่แนะนำเปลี่ยนตาม — ตัวอย่าง "โมเดลถึงมือผู้ใช้" ของ Module 10.
"""

from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

import matplotlib.pyplot as plt
import numpy as np
import polars as pl
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import TimeSeriesSplit

# ฟอนต์ไทยสำหรับป้ายกราฟ — fallback list รองรับทุกแพลตฟอร์ม (macOS/Windows)
plt.rcParams["font.family"] = ["DejaVu Sans", "Noto Sans Thai", "Leelawadee UI", "Tahoma", "Thonburi"]


def data_dir() -> Path:
    for p in (Path.cwd(), *Path.cwd().parents):
        if (p / "datasets").exists():
            return p / "datasets"
    raise FileNotFoundError("ไม่พบ datasets/ — รัน streamlit จากใน repo")


@st.cache_data
def load_series() -> tuple[np.ndarray, np.ndarray]:
    """โหลด + เก็บกวาด sentinel -99.99 → (ค่า, ปีแบบทศนิยม)."""
    raw = pl.read_csv(data_dir() / "co2_mm_gl.csv", comment_prefix="#")
    df = raw.with_columns(
        pl.when(pl.col("average") < 0).then(None).otherwise(pl.col("average")).alias("average")
    ).drop_nulls("average")
    return df["average"].to_numpy(), df["decimal"].to_numpy()


@st.cache_data
def fit_and_forecast(horizon: int) -> dict:
    """เทรน linear บน differences + recursive forecast พร้อมแถบ ±2σ√h."""
    v, dec = load_series()
    N = len(v)
    dy = v[12:] - v[: N - 12]
    i0, i1 = 12, len(dy)
    Xd = np.column_stack([dy[i0 - 1 : i1 - 1], dy[i0 - 12 : i1 - 12]])
    yd = dy[i0:]

    tscv = TimeSeriesSplit(n_splits=5)
    maes = []
    for tr, te in tscv.split(Xd):
        m = LinearRegression().fit(Xd[tr], yd[tr])
        pred = v[12 + te] + m.predict(Xd[te])
        maes.append(mean_absolute_error(v[12 + te] + yd[te], pred))

    model = LinearRegression().fit(Xd, yd)
    sigma = float((yd - model.predict(Xd)).std())

    hist = list(v)
    fc = []
    for _ in range(horizon):
        d1, d12 = hist[-1] - hist[-13], hist[-12] - hist[-24]
        nxt = hist[-12] + float(model.predict(np.array([[d1, d12]]))[0])
        hist.append(nxt)
        fc.append(nxt)
    fc = np.array(fc)
    band = 2 * sigma * np.sqrt(np.arange(1, horizon + 1))
    return {
        "v": v, "dec": dec, "fc": fc, "band": band, "sigma": sigma,
        "cv_mae": float(np.mean(maes)), "cv_mae_folds": maes,
        "future_years": dec[-1] + np.arange(1, horizon + 1) / 12,
    }


st.set_page_config(page_title="Drift Predictor — ML for Metrology", page_icon="📉", layout="wide")

st.title("Drift Predictor — ตั้งรอบสอบเทียบซ้ำจากข้อมูล")
st.caption(
    "Demo ของ Capstone C (ML for Advanced Metrology Research) · ข้อมูล: NOAA GML globally-averaged CO₂ "
    "monthly means — Lan, X., Thoning, K.W., Dlugokencky, E.J., *Trends in globally-averaged CO₂*, "
    "Version 2026-09, https://gml.noaa.gov/ccgg/trends/ (U.S. Government work, fair credit required) · "
    "แมป: ค่า ppm ≡ ค่าเบี่ยงเบนของ working standard เทียบ reference"
)

with st.sidebar:
    st.header("ตั้งค่า")
    tolerance = st.slider(
        "Tolerance limit (+ ppm จากค่าล่าสุด)", 2.0, 12.0, 6.0, 0.5,
        help="ถ้าค่าเบี่ยงเบนทะลุระดับนี้ถือว่ามาตรฐานใช้ไม่ได้",
    )
    horizon = st.slider("พยากรณ์ล่วงหน้า (เดือน)", 12, 60, 24, 6)
    margin = st.slider(
        "Safety margin (เดือน ที่ตัดก่อนแตะ tolerance)", 0, 6, 2,
        help="จุดตัดลบ margin = recalibration interval ที่แนะนำ",
    )
    st.divider()
    st.markdown(
        "**โมเดล:** linear regression บน year-over-year differences "
        "(lags Δt−1, Δt−12) · วัดด้วย TimeSeriesSplit — ดูเหตุผลเต็มใน "
        "`day3/module10_capstone/capstone_C_drift_predictor_solution.ipynb`"
    )

out = fit_and_forecast(horizon)
v, dec, fc, band = out["v"], out["dec"], out["fc"], out["band"]
fy = out["future_years"]
tol_level = v[-1] + tolerance

h = np.arange(1, horizon + 1)
above = h[fc + band >= tol_level]
cross = int(above[0]) if len(above) else None
interval = max(cross - margin, 1) if cross else None

c1, c2, c3 = st.columns(3)
c1.metric("ค่าล่าสุด", f"{v[-1]:.2f} ppm")
c2.metric("CV MAE (median of folds)", f"{out['cv_mae']:.3f} ppm",
          help=f"folds: {np.round(out['cv_mae_folds'], 3)}")
c3.metric(
    "Recalibration interval ที่แนะนำ",
    f"{interval} เดือน" if interval else f"> {horizon} เดือน",
    help="จุดที่ขอบบนของแถบ ~95% แตะ tolerance − safety margin",
)

fig, ax = plt.subplots(figsize=(11, 4.4))
ax.plot(dec[-240:], v[-240:], color="#264653", lw=1.1, label="ข้อมูลจริง (พฤติกรรมมาตรฐาน)")
ax.plot(fy, fc, color="#2a9d8f", lw=1.7, label="พยากรณ์ (recursive)")
ax.fill_between(fy, fc - band, fc + band, color="#2a9d8f", alpha=0.18, label="ช่วง ~95% (±2σ√h)")
ax.axhline(tol_level, color="#e76f51", ls="--", lw=1.3, label=f"tolerance limit (+{tolerance:g} ppm)")
if cross:
    ax.axvline(fy[cross - 1], color="#e76f51", lw=0.9, ls=":")
    ax.annotate(f"ขอบบนแตะ tolerance\nที่ +{cross} เดือน", (fy[cross - 1], tol_level),
                xytext=(-110, -12), textcoords="offset points",
                color="#e76f51", fontsize=9)
ax.set_xlabel("ปี")
ax.set_ylabel("CO₂ (ppm)")
ax.legend(loc="upper left", fontsize=9)
st.pyplot(fig)

st.markdown(
    f"""
**อ่านผล:** แถบความไม่แน่นอนบานตาม √h — จุดที่ขอบบนแตะ tolerance คือ horizon ที่ยาวที่สุด
ที่ยังมั่นใจได้ ~95% ว่ามาตรฐานยังอยู่ใน spec ตัด margin เหลือ **{interval} เดือน** เป็นรอบที่แนะนำ
เลื่อน tolerance ลง (spec คับขึ้น) หรือ margin ขึ้น (ระวังตัวมากขึ้น) แล้วสังเกตรอบสั้นลงอย่างไร

**ข้อจำกัด (ต้องแจ้งผู้ใช้เสมอ):** โมเดลสมมุติว่า drift เดินต่อแบบเดิม — เหตุการณ์ใหม่
(ซ่อมบำรุง, เปลี่ยนชิ้นส่วน) ทำให้พยากรณ์ใช้ไม่ได้ทันที · แถบ ±2σ√h เป็น approximation แบบ
random-walk ยังไม่รวมความไม่แน่นอนของพารามิเตอร์โมเดล
"""
)

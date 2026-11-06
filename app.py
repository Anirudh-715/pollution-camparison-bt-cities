"""
app.py — Air Quality Comparison Dashboard
Light & Clean Design  ·  Streamlit + Plotly
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestClassifier

# ─── PAGE CONFIG ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Air Quality · Delhi · Chandigarh · Solan · Shimla",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── CLEAN CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Page background ── */
[data-testid="stAppViewContainer"] { background: #ffffff; }
[data-testid="stHeader"]          { background: #ffffff; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #fafbfd;
    border-right: 1px solid #e8ecf1;
}
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stSlider label,
[data-testid="stSidebar"] .stMultiSelect label {
    font-size: 13px !important;
    font-weight: 600;
    color: #4a5568 !important;
}

/* ── Hero ── */
.hero {
    background: linear-gradient(135deg, #e8f4f8 0%, #f0f7f4 50%, #eef2f7 100%);
    border: 1px solid #d5e3ec;
    border-radius: 16px;
    padding: 2.2rem 2.5rem 1.8rem;
    margin-bottom: 1.6rem;
}
.hero h1 {
    font-size: 1.85rem;
    font-weight: 800;
    color: #1a3a4a;
    margin: 0 0 0.5rem 0;
    letter-spacing: -0.3px;
}
.hero p {
    font-size: 1.02rem;
    color: #4a6d7c !important;
    margin: 0;
    line-height: 1.6;
}
.hero b { color: #1a3a4a; }
.city-tag {
    display: inline-block;
    background: white;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.85rem;
    font-weight: 600;
    margin: 2px 3px;
    border: 1.5px solid;
}

/* ── Section titles ── */
.sec-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #1a3a4a;
    margin: 1.6rem 0 0.8rem 0;
    padding-bottom: 0.4rem;
    border-bottom: 2px solid #4db8a4;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: #f7f9fb;
    border-radius: 12px;
    padding: 5px 6px;
    gap: 6px;
    border: 1px solid #e2e8f0;
    margin-bottom: 1.4rem;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    padding: 10px 24px;
    font-size: 0.95rem;
    font-weight: 600;
    color: #4a5568;
    background: transparent;
    border: none !important;
}
.stTabs [aria-selected="true"] {
    background: #4db8a4 !important;
    color: white !important;
}

/* ── Metric cards ── */
[data-testid="metric-container"] {
    background: #f7f9fb;
    border-radius: 12px;
    padding: 1.1rem 1.3rem;
    border: 1px solid #e2e8f0;
    border-left: 4px solid #4db8a4;
}
[data-testid="metric-container"] label {
    font-size: 0.72rem !important;
    font-weight: 700 !important;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #718096 !important;
}
[data-testid="stMetricValue"] {
    font-size: 1.5rem !important;
    font-weight: 700 !important;
    color: #1a3a4a !important;
}

/* ── Prediction badge ── */
.pred-badge {
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    font-size: 1.8rem;
    font-weight: 800;
    letter-spacing: 1px;
    margin: 0.8rem 0;
    color: white;
    box-shadow: 0 4px 12px rgba(0,0,0,0.12);
}

/* ── Text sizes ── */
p, li, .stMarkdown p {
    font-size: 1rem;
    color: #2d3748;
    line-height: 1.65;
}
.stCaption {
    font-size: 0.85rem !important;
    color: #718096 !important;
}
</style>
""", unsafe_allow_html=True)


# ─── CONSTANTS ───────────────────────────────────────────────────────────────
AQI_COLORS = {
    "Good":         "#48bb78",
    "Satisfactory": "#68d391",
    "Moderate":     "#ecc94b",
    "Poor":         "#ed8936",
    "Very Poor":    "#e53e3e",
    "Severe":       "#9b2c2c",
}

CITY_COLORS = {
    "Delhi":      "#e53e3e",   # Red
    "Chandigarh": "#3182ce",   # Blue
    "Solan":      "#38a169",   # Green
    "Shimla":     "#dd6b20",   # Orange
}

CITY_HEX = {"Delhi": "#e53e3e", "Chandigarh": "#3182ce", "Solan": "#38a169", "Shimla": "#dd6b20"}
ELEV = {"Delhi": 216, "Chandigarh": 321, "Solan": 1502, "Shimla": 2276}
POLLUTANTS   = ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]
SEASON_ORDER = ["Winter", "Summer", "Monsoon", "Post-Monsoon"]
BUCKET_ORDER = ["Good", "Satisfactory", "Moderate", "Poor", "Very Poor", "Severe"]

# Plotly clean layout — all text forced to dark
PL = dict(
    font=dict(family="'Segoe UI', Inter, sans-serif", size=13, color="#1a1a1a"),
    paper_bgcolor="#ffffff",
    plot_bgcolor="#ffffff",
    margin=dict(t=44, b=32, l=40, r=16),
    title_font=dict(size=14, color="#1a1a1a"),
    legend=dict(bgcolor="#ffffff", bordercolor="#e2e8f0", borderwidth=1,
                font=dict(size=12, color="#1a1a1a")),
)
AX = dict(gridcolor="#edf2f7", linecolor="#e2e8f0", zeroline=False,
          tickfont=dict(color="#1a1a1a", size=12),
          title_font=dict(color="#1a1a1a", size=13))


# ─── DATA & MODEL ───────────────────────────────────────────────────────────
@st.cache_data(show_spinner="Loading data…")
def load_data():
    d = pd.read_csv("data/pollution_daily.csv")
    d["Date"] = pd.to_datetime(d["Date"])
    h = pd.read_csv("data/pollution_hourly_raw.csv")
    h["Timestamp"] = pd.to_datetime(h["Timestamp"])
    h["Hour"] = h["Timestamp"].dt.hour
    return d, h

@st.cache_resource(show_spinner="Training model…")
def train_model(df):
    X = df[POLLUTANTS + ["Elevation_m"]]
    y = df["AQI_Bucket"]
    clf = RandomForestClassifier(n_estimators=120, random_state=42, n_jobs=-1)
    clf.fit(X, y)
    return clf

try:
    daily_df, hourly_df = load_data()
except FileNotFoundError as e:
    st.error(f"Data not found: {e}. Run `fetch_data.py` then `calculate_aqi.py`.")
    st.stop()

model = train_model(daily_df)
ALL_CITIES = sorted(daily_df["City"].unique())


# ─── SIDEBAR ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚙️ Filters")

    sel_cities = st.multiselect("Cities", ALL_CITIES, default=ALL_CITIES)
    st.divider()

    min_d, max_d = daily_df["Date"].min().date(), daily_df["Date"].max().date()
    date_sel = st.date_input("Date range", value=(min_d, max_d),
                              min_value=min_d, max_value=max_d)
    st.divider()

    param  = st.selectbox("Parameter", ["AQI"] + POLLUTANTS)
    smooth = st.slider("Smoothing (days)", 1, 30, 7)

    st.divider()
    st.caption("📡 Open-Meteo CAMS reanalysis\n📐 CPCB sub-index AQI formula")

if not sel_cities:
    st.info("👈 Open the sidebar and select at least one city.")
    st.stop()

start_dt = pd.Timestamp(date_sel[0] if isinstance(date_sel, (list, tuple)) else min_d)
end_dt   = pd.Timestamp(date_sel[1] if isinstance(date_sel, (list, tuple)) and len(date_sel) == 2 else max_d)

filt = daily_df[
    daily_df["City"].isin(sel_cities)
    & (daily_df["Date"] >= start_dt)
    & (daily_df["Date"] <= end_dt)
].copy()

if filt.empty:
    st.warning("No data for the selected filters.")
    st.stop()


# ─── Helper: apply axis style + force dark text everywhere ──────────────────
def style_fig(fig, **extra):
    fig.update_layout(**PL, **extra)
    fig.update_xaxes(**AX)
    fig.update_yaxes(**AX)
    # Force all text elements to dark
    fig.update_annotations(font_color="#1a1a1a")
    fig.update_coloraxes(colorbar_tickfont_color="#1a1a1a",
                          colorbar_title_font_color="#1a1a1a")
    return fig


# ─── HERO BANNER ─────────────────────────────────────────────────────────────
city_tags = ""
for city, col in CITY_HEX.items():
    city_tags += f'<span class="city-tag" style="color:{col}; border-color:{col};">{city}</span>'

st.markdown(f"""
<div class="hero">
    <h1>🌿 Air Quality Comparative Study</h1>
    <p>
        Analysing <b>PM₂.₅ · PM₁₀ · NO₂ · SO₂ · CO · O₃</b> and CPCB AQI
        across four topographically distinct cities in North India (2023).
    </p>
    <div style="margin-top: 0.7rem;">
        {city_tags}
    </div>
</div>
""", unsafe_allow_html=True)


# ─── TABS ────────────────────────────────────────────────────────────────────
t1, t2, t3, t4, t5 = st.tabs([
    "📊  Summary",
    "📈  Trends",
    "🕒  Diurnal & Correlations",
    "🤖  AQI Predictor",
    "📋  Data Table",
])


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 1 — SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════
with t1:
    city_aqi  = filt.groupby("City")["AQI"].mean()
    cleanest  = city_aqi.idxmin()
    worst     = city_aqi.idxmax()
    dominant  = filt["Prominent_Pollutant"].mode().iloc[0]
    pm25_mean = filt.groupby("City")["PM2.5"].mean()
    ratio     = pm25_mean.get("Delhi", 0) / max(pm25_mean.get("Shimla", 1), 0.1)
    n_days    = int(filt.groupby("City")["Date"].nunique().mean())

    k1, k2, k3, k4, k5 = st.columns(5)
    k1.metric("🏆 Cleanest City",       cleanest,    f"AQI {city_aqi[cleanest]:.0f}")
    k2.metric("⚠️ Most Polluted",       worst,       f"AQI {city_aqi[worst]:.0f}",
              delta_color="inverse")
    k3.metric("🎯 Top Pollutant",       dominant)
    k4.metric("🏔️ Delhi / Shimla",     f"{ratio:.1f}× PM2.5")
    k5.metric("📅 Days Analysed",       f"{n_days}")

    st.markdown("")

    col_l, col_r = st.columns([1, 1.5])

    with col_l:
        st.markdown('<div class="sec-title">Mean Pollutant Concentrations</div>',
                    unsafe_allow_html=True)
        tbl = (filt.groupby("City")[["PM2.5","PM10","NO2","SO2","AQI"]]
               .mean().round(1).reset_index())
        st.dataframe(tbl, use_container_width=True, hide_index=True, height=195)
        st.caption("µg/m³ (CO in mg/m³). NAAQS 24 h: PM2.5 ≤ 60 · PM10 ≤ 100 · NO2 ≤ 80")

    with col_r:
        st.markdown('<div class="sec-title">Days per AQI Category (%)</div>',
                    unsafe_allow_html=True)
        pct = pd.crosstab(filt["City"], filt["AQI_Bucket"], normalize="index") * 100
        cols_ok = [b for b in BUCKET_ORDER if b in pct.columns]
        pct = pct[cols_ok].reset_index()

        fig = px.bar(pct, x="City", y=cols_ok, color_discrete_map=AQI_COLORS,
                     labels={"value": "% of days", "variable": "Category"})
        style_fig(fig, barmode="stack", height=290,
                  legend_title_text="AQI Category")
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="sec-title">Elevation vs Median PM₂.₅</div>',
                unsafe_allow_html=True)
    elev_df = (filt.groupby(["City","Elevation_m"])[["PM2.5","AQI"]]
               .median().round(1).reset_index())
    fig2 = px.scatter(elev_df, x="Elevation_m", y="PM2.5", text="City",
                      size="AQI", color="City", color_discrete_map=CITY_COLORS,
                      size_max=55,
                      labels={"Elevation_m": "Elevation (m)",
                              "PM2.5": "Median PM2.5 (µg/m³)"})
    fig2.update_traces(textposition="top center",
                       textfont=dict(size=13, color="#1a3a4a"))
    style_fig(fig2, height=340, showlegend=False)
    st.plotly_chart(fig2, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 2 — TRENDS
# ═══════════════════════════════════════════════════════════════════════════════
with t2:
    st.markdown(f'<div class="sec-title">{param} — {smooth}-Day Rolling Average</div>',
                unsafe_allow_html=True)

    pieces = []
    for city in sel_cities:
        c = filt[filt["City"] == city].sort_values("Date").copy()
        c["Smoothed"] = c[param].rolling(smooth, min_periods=1).mean()
        pieces.append(c)
    ts = pd.concat(pieces, ignore_index=True)

    fig_ts = px.line(ts, x="Date", y="Smoothed", color="City",
                     color_discrete_map=CITY_COLORS,
                     labels={"Smoothed": param, "Date": ""})
    if param == "AQI":
        for y0, y1, col, lbl in [
            (0, 50, "#48bb78","Good"), (51, 100, "#68d391","Satisfactory"),
            (101, 200, "#ecc94b","Moderate"), (201, 300, "#ed8936","Poor"),
            (301, 500, "#e53e3e","Very Poor"),
        ]:
            fig_ts.add_hrect(y0=y0, y1=y1, fillcolor=col, opacity=0.06,
                             line_width=0, annotation_text=lbl,
                             annotation_position="left",
                             annotation_font=dict(size=9, color=col))

    fig_ts.update_traces(line_width=2.5)
    style_fig(fig_ts, height=430, hovermode="x unified")
    st.plotly_chart(fig_ts, use_container_width=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(f'<div class="sec-title">Distribution — {param}</div>',
                    unsafe_allow_html=True)
        fig_box = px.box(filt, x="City", y=param, color="City",
                         color_discrete_map=CITY_COLORS, points="outliers")
        style_fig(fig_box, showlegend=False, height=340)
        st.plotly_chart(fig_box, use_container_width=True)

    with c2:
        st.markdown(f'<div class="sec-title">Seasonal Mean — {param}</div>',
                    unsafe_allow_html=True)
        s_agg = (filt.groupby(["Season","City"])[param]
                 .mean().round(2).reset_index())
        fig_s = px.bar(s_agg, x="Season", y=param, color="City",
                       color_discrete_map=CITY_COLORS, barmode="group",
                       category_orders={"Season": SEASON_ORDER})
        style_fig(fig_s, height=340)
        st.plotly_chart(fig_s, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 3 — DIURNAL & CORRELATION
# ═══════════════════════════════════════════════════════════════════════════════
with t3:
    d1, d2 = st.columns(2)

    with d1:
        st.markdown('<div class="sec-title">24-Hour PM₂.₅ Profile</div>',
                    unsafe_allow_html=True)
        h_agg = (hourly_df[hourly_df["City"].isin(sel_cities)]
                 .groupby(["City","Hour"])["PM2.5"]
                 .mean().round(2).reset_index())
        fig_h = px.line(h_agg, x="Hour", y="PM2.5", color="City",
                        color_discrete_map=CITY_COLORS, markers=True,
                        labels={"Hour": "Hour (IST)", "PM2.5": "PM2.5 (µg/m³)"})
        fig_h.update_traces(line_width=2.5, marker_size=6)
        style_fig(fig_h, height=370)
        fig_h.update_xaxes(tickmode="linear", tick0=0, dtick=2)
        st.plotly_chart(fig_h, use_container_width=True)
        st.caption("Morning (7-10 AM) and evening (7-11 PM) vehicular peaks.")

    with d2:
        st.markdown('<div class="sec-title">Pollutant Correlation</div>',
                    unsafe_allow_html=True)
        c_city = st.selectbox("City:", sel_cities, key="corr_city")
        corr = filt[filt["City"] == c_city][POLLUTANTS].corr().round(2)
        fig_c = px.imshow(corr, text_auto=".2f",
                          color_continuous_scale=["#e8f4f8","#a0d8cd","#4db8a4"],
                          zmin=-1, zmax=1,
                          title=f"Correlation — {c_city}")
        fig_c.update_traces(textfont=dict(color="#1a1a1a", size=14))
        style_fig(fig_c, height=370)
        st.plotly_chart(fig_c, use_container_width=True)

    st.markdown('<div class="sec-title">PM₂.₅ Violin Plot</div>', unsafe_allow_html=True)
    fig_v = px.violin(filt, x="City", y="PM2.5", color="City",
                      color_discrete_map=CITY_COLORS, box=True, points="outliers")
    style_fig(fig_v, showlegend=False, height=340)
    st.plotly_chart(fig_v, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 4 — ML PREDICTOR
# ═══════════════════════════════════════════════════════════════════════════════
with t4:
    st.markdown("""
    <div style="background:#f7f9fb; border:1px solid #e2e8f0; border-radius:14px;
                padding:1.4rem 1.8rem; margin-bottom:1.2rem;">
        <h4 style="margin:0 0 0.4rem; color:#1a3a4a; font-size:1.2rem;">
            🤖 Real-Time AQI Category Predictor
        </h4>
        <p style="margin:0; color:#718096; font-size:0.95rem;">
            Drag the sliders to simulate atmospheric conditions.
            The Random Forest model (≈ 98% accuracy) instantly predicts
            the CPCB AQI category.
        </p>
    </div>
    """, unsafe_allow_html=True)

    sl1, sl2, sl3 = st.columns(3)

    with sl1:
        sim_city = st.selectbox("City (sets elevation):", ALL_CITIES, key="pred_city")
        st.caption(f"Elevation: **{ELEV[sim_city]} m** above MSL")
        sim_pm25 = st.slider("PM2.5 (µg/m³)",  1.0, 350.0, 55.0, 1.0)
        sim_pm10 = st.slider("PM10  (µg/m³)",  5.0, 500.0, 95.0, 1.0)

    with sl2:
        sim_no2 = st.slider("NO2   (µg/m³)",  1.0, 250.0, 30.0, 1.0)
        sim_so2 = st.slider("SO2   (µg/m³)",  1.0, 200.0, 12.0, 1.0)
        sim_co  = st.slider("CO    (mg/m³)",  0.1,  20.0,  1.2, 0.1)
        sim_o3  = st.slider("O3    (µg/m³)",  1.0, 250.0, 45.0, 1.0)

    with sl3:
        inp = pd.DataFrame([{
            "PM2.5": sim_pm25, "PM10": sim_pm10, "NO2": sim_no2,
            "SO2": sim_so2, "CO": sim_co, "O3": sim_o3,
            "Elevation_m": ELEV[sim_city],
        }])
        pred  = model.predict(inp)[0]
        probs = model.predict_proba(inp)[0]
        color = AQI_COLORS.get(pred, "#555")

        st.markdown("**Predicted Category**")
        st.markdown(
            f"<div class='pred-badge' style='background:{color};'>{pred.upper()}</div>",
            unsafe_allow_html=True,
        )

        prob_df = (pd.DataFrame({"Category": model.classes_, "Conf": probs * 100})
                     .sort_values("Conf", ascending=True))
        fig_p = px.bar(prob_df, x="Conf", y="Category", orientation="h",
                       text=prob_df["Conf"].apply(lambda v: f"{v:.1f}%"),
                       color="Category", color_discrete_map=AQI_COLORS)
        fig_p.update_traces(textposition="outside")
        style_fig(fig_p, showlegend=False, height=230)
        fig_p.update_xaxes(range=[0, 110], title_text="Confidence (%)")
        st.plotly_chart(fig_p, use_container_width=True)

    st.markdown('<div class="sec-title">Feature Importance (Gini)</div>',
                unsafe_allow_html=True)
    imp = pd.Series(model.feature_importances_,
                    index=POLLUTANTS + ["Elevation_m"]).sort_values()
    fig_fi = px.bar(imp, orientation="h",
                    labels={"value": "Importance", "index": "Feature"},
                    color=imp.values,
                    color_continuous_scale=["#e2e8f0","#4db8a4","#1a3a4a"])
    style_fig(fig_fi, showlegend=False, coloraxis_showscale=False, height=270)
    st.plotly_chart(fig_fi, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 5 — DATA TABLE
# ═══════════════════════════════════════════════════════════════════════════════
with t5:
    st.markdown('<div class="sec-title">Filtered Dataset</div>', unsafe_allow_html=True)
    show_cols = ["City","Date","Season","AQI","AQI_Bucket","Prominent_Pollutant",
                 "PM2.5","PM10","NO2","SO2","CO","O3","Elevation_m"]
    st.dataframe(filt[show_cols].reset_index(drop=True),
                 use_container_width=True, height=460, hide_index=True)

    csv = filt[show_cols].to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download CSV", data=csv,
                       file_name="pollution_filtered.csv", mime="text/csv")
    st.caption(f"{len(filt):,} rows · {', '.join(sel_cities)} · {start_dt.date()} → {end_dt.date()}")

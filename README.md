# Comparative Air Quality Analysis: Delhi, Chandigarh, Solan, and Shimla
### Data Science Laboratory Project

This project conducts an empirical comparative analysis of ambient air quality dynamics across four topographically distinct regions in Northern India:
1. **Delhi**: Indo-Gangetic Plains Megacity (Elevation: 216m) — Heavy traffic, industrial emissions, winter temperature inversions.
2. **Chandigarh**: Shivalik Foothills Planned City (Elevation: 321m) — High green cover, organized transit, moderate urban density.
3. **Solan**: Mid-Hills Industrial Corridor (Elevation: 1,502m) — Industrial belt (Baddi/Nalagarh proximity), mountain highway emissions.
4. **Shimla**: High-Altitude Mountain Resort (Elevation: 2,276m) — Elevated Himalayan topography, tourism-driven traffic, cleaner baseline atmosphere.

---

## 👥 Collaborative Team Roles & Equal Contribution

To model a real-world distributed data engineering pipeline, **each member independently sourced the 2023 atmospheric monitoring data for their assigned city**, and the team integrated all streams into a unified master dataset:

| Member | Assigned City | Technical Responsibility |
| :--- | :--- | :--- |
| **Member 1 (Lead Speaker)** | 🔵 **Chandigarh** (321m) | **Machine Learning Modeling** (Logistic Regression, Random Forest 98% accuracy, Gini Feature Importance) |
| **Member 2** | 🔴 **Delhi** (216m) | **Data Integration Pipeline & CPCB AQI Engine** (Hourly-to-daily aggregation, unit harmonization, breakpoint interpolation) |
| **Member 3** | 🟢 **Solan** (1,502m) | **Exploratory Data Analysis (EDA)** (Particulate boxplots, 14-day rolling trends, seasonal bars, diurnal curves) |
| **Member 4** | 🟠 **Shimla** (2,276m) | **Statistical Hypothesis Testing** (D'Agostino normality test, Kruskal-Wallis H-test, Mann-Whitney U with Bonferroni correction) |

Detailed word-for-word presentation scripts and viva prep: see [`PRESENTATION_SCRIPTS.md`](PRESENTATION_SCRIPTS.md).

---

## 📁 Project Structure

```
pollution-comparison/
│
├── data/
│   ├── pollution_hourly_raw.csv           # 35,040 hourly observations (2023 full year)
│   └── pollution_daily.csv                # 1,460 daily observations with CPCB sub-indices & AQI
│
├── fetch_data.py                          # Automated API fetcher (Open-Meteo CAMS reanalysis)
├── calculate_aqi.py                       # Official Indian CPCB AQI breakpoint calculation engine
├── generate_notebook.py                   # Generates the Jupyter / Google Colab notebook
├── generate_presentation_docs.py          # Script to compile PDF and PowerPoint slides
│
├── pollution_analysis.ipynb               # Complete Lab Notebook (EDA, ANOVA, Hypothesis Testing, ML)
├── app.py                                 # Interactive Streamlit Web Dashboard
├── Presentation_Guide_and_Scripts.pdf     # Printable Word-for-Word Presentation & Viva Guide
├── Air_Quality_Project_Presentation.pptx # 16:9 PowerPoint Slide Deck for Presentation
├── PRESENTATION_SCRIPTS.md                # Markdown script for all 4 team members
├── TEAM_WORK_DIVISION.md                  # Project allocation and study guide
├── requirements.txt                       # Python environment dependencies
└── README.md                              # Complete documentation & lab report
```

---

## ❓ Academic Rationale: Why the 2023 Calendar Year?

A common question in environmental data science is: *Why use 2023 rather than rolling real-time data?*

1. **Complete 365-Day Cycle (All 4 Meteorological Seasons):**  
   Air quality in India is heavily seasonal. Comparing cities over an incomplete year or recent months creates severe statistical bias. A full calendar year ensures fair, balanced representation across:
   - **Winter (Jan–Feb):** Cold air stagnation and severe temperature inversions.
   - **Summer / Pre-Monsoon (Mar–May):** High temperature, dust storms, and convective dispersion.
   - **Monsoon (Jun–Sep):** Precipitation wash-out scrub effect lowering particulate matter.
   - **Post-Monsoon (Oct–Dec):** Regional agricultural stubble burning and boundary-layer contraction.
2. **Quality-Assured Reanalysis Calibration:**  
   Real-time station sensors frequently experience outages, missing data, and uncalibrated sensor drift. The Copernicus Atmosphere Monitoring Service (CAMS) reanalysis undergoes posterior quality-control and ground-truth validation, ensuring a complete, gap-free record across all 35,040 hours.
3. **Benchmark Reproducibility:**  
   In an academic evaluation, statistical test statistics ($H = 905.64, p < 10^{-190}$) and Machine Learning weights ($97.95\%$ accuracy) must remain identical every time the professor or examiner runs the notebook.

---

## 🌐 Data Sourcing & Direct Download Links

The underlying data is powered by the **[Open-Meteo Air Quality API](https://open-meteo.com/en/docs/air-quality-api)**, backed by the **Copernicus Atmosphere Monitoring Service (CAMS)** / ECMWF.

Direct 1-click links to download individual city datasets:

| City | Coordinates | Direct CSV Download | Direct Excel (.xlsx) Download |
| :--- | :---: | :---: | :---: |
| **Chandigarh** | 30.7333°N, 76.7794°E | [📥 Download CSV](https://air-quality-api.open-meteo.com/v1/air-quality?latitude=30.7333&longitude=76.7794&hourly=pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone&start_date=2023-01-01&end_date=2023-12-31&timezone=Asia/Kolkata&format=csv) | [📊 Download Excel](https://air-quality-api.open-meteo.com/v1/air-quality?latitude=30.7333&longitude=76.7794&hourly=pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone&start_date=2023-01-01&end_date=2023-12-31&timezone=Asia/Kolkata&format=xlsx) |
| **Delhi** | 28.6139°N, 77.2090°E | [📥 Download CSV](https://air-quality-api.open-meteo.com/v1/air-quality?latitude=28.6139&longitude=77.2090&hourly=pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone&start_date=2023-01-01&end_date=2023-12-31&timezone=Asia/Kolkata&format=csv) | [📊 Download Excel](https://air-quality-api.open-meteo.com/v1/air-quality?latitude=28.6139&longitude=77.2090&hourly=pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone&start_date=2023-01-01&end_date=2023-12-31&timezone=Asia/Kolkata&format=xlsx) |
| **Solan** | 30.9045°N, 77.0967°E | [📥 Download CSV](https://air-quality-api.open-meteo.com/v1/air-quality?latitude=30.9045&longitude=77.0967&hourly=pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone&start_date=2023-01-01&end_date=2023-12-31&timezone=Asia/Kolkata&format=csv) | [📊 Download Excel](https://air-quality-api.open-meteo.com/v1/air-quality?latitude=30.9045&longitude=77.0967&hourly=pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone&start_date=2023-01-01&end_date=2023-12-31&timezone=Asia/Kolkata&format=xlsx) |
| **Shimla** | 31.1048°N, 77.1734°E | [📥 Download CSV](https://air-quality-api.open-meteo.com/v1/air-quality?latitude=31.1048&longitude=77.1734&hourly=pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone&start_date=2023-01-01&end_date=2023-12-31&timezone=Asia/Kolkata&format=csv) | [📊 Download Excel](https://air-quality-api.open-meteo.com/v1/air-quality?latitude=31.1048&longitude=77.1734&hourly=pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone&start_date=2023-01-01&end_date=2023-12-31&timezone=Asia/Kolkata&format=xlsx) |

---

## 🚀 Quickstart Guide

### 1. Local Setup
```bash
pip install -r requirements.txt
```

### 2. Launch the Interactive Web Dashboard
```bash
streamlit run app.py
```
Dashboard features:
- **Executive KPIs**: Cleanest vs. most polluted city metrics, Delhi/Shimla particulate ratio.
- **Comparative Trends**: Interactive Plotly time-series with custom date ranges and rolling averages.
- **Diurnal Cycles**: 24-hour rush-hour profiles comparing mountain vs. plains vehicular spikes.
- **Live ML Predictor**: Real-time slider simulation to predict CPCB AQI buckets.

### 3. Open in Google Colab
1. Upload `pollution_analysis.ipynb` to [Google Colab](https://colab.research.google.com).
2. Upload the `data/` directory.
3. Run all cells (`Runtime -> Run all`).

---

## 🔬 Core Methodologies & Results

### 1. CPCB Sub-Index Formula
Sub-indices $I_p$ are computed using linear interpolation across official Central Pollution Control Board (CPCB) concentration breakpoints:
$$I_p = I_{low} + \frac{I_{high} - I_{low}}{B_{high} - B_{low}} \times (C_p - B_{low})$$
$$\text{Overall AQI} = \max(I_{PM2.5}, I_{PM10}, I_{NO2}, I_{SO2}, I_{CO}, I_{O3})$$

### 2. Statistical Hypothesis Testing
- **Normality Test**: D'Agostino-Pearson tests confirmed that particulate pollutants ($PM_{2.5}, PM_{10}$) violate normality ($p < 10^{-10}$), necessitating non-parametric methods.
- **Kruskal-Wallis H-Test**:
  - $H = 905.64, \quad p = 5.29 \times 10^{-196}$
  - **Conclusion**: Statistically significant differences exist across the four urban-topographical zones ($p < 0.001$).
- **Post-Hoc Mann-Whitney U Tests (Bonferroni corrected, $\alpha_{adj} = 0.0083$)**:
  - Every pairwise combination yielded $p < 0.001$.
  - Crucially, **Solan has significantly higher particulate pollution than Shimla ($p = 1.29 \times 10^{-10}$)**, confirming that industrial/transit corridors override altitude benefits.

### 3. Machine Learning Classification
- **Model**: Random Forest Classifier (100 estimators, max depth 12).
- **Target**: AQI Category (`Good`, `Satisfactory`, `Moderate`, `Poor`, `Very Poor`).
- **Performance**:
  - **Accuracy**: **97.95%** (vs. 88.36% for baseline Multinomial Logistic Regression).
  - **Macro F1-Score**: **0.98** (weighted).
  - **Top Features**: $PM_{2.5}$ and $PM_{10}$ constitute over 85% of total Gini split importance.

---

## 📊 Summary of Annual City Air Quality (2023)

| City | Elevation (m) | Mean $PM_{2.5}$ ($\mu g/m^3$) | Mean $PM_{10}$ ($\mu g/m^3$) | Mean AQI | Dominant AQI Category |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Delhi** | 216 | 66.2 ± 33.4 | 112.3 ± 52.5 | 145.0 ± 74.7 | Moderate / Poor |
| **Chandigarh** | 321 | 38.6 ± 16.5 | 58.8 ± 25.2 | 93.6 ± 33.4 | Satisfactory |
| **Solan** | 1,502 | 22.2 ± 8.5 | 33.7 ± 13.3 | 93.0 ± 21.7 | Satisfactory |
| **Shimla** | 2,276 | 18.6 ± 8.1 | 28.1 ± 12.1 | 80.7 ± 17.1 | Satisfactory / Good |

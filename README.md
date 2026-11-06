# Comparative Air Quality Analysis: Delhi, Chandigarh, Solan, and Shimla
### Data Science Laboratory Project

This project conducts an empirical comparative analysis of ambient air quality dynamics across four topographically distinct regions in Northern India:
1. **Delhi**: Indo-Gangetic Plains Megacity (Elevation: 216m) — Heavy traffic, industrial emissions, winter temperature inversions.
2. **Chandigarh**: Shivalik Foothills Planned City (Elevation: 321m) — High green cover, organized transit, moderate urban density.
3. **Solan**: Mid-Hills Industrial Corridor (Elevation: 1,502m) — Industrial belt (Baddi/Nalagarh proximity), mountain highway emissions.
4. **Shimla**: High-Altitude Mountain Resort (Elevation: 2,276m) — Elevated Himalayan topography, tourism-driven traffic, cleaner baseline atmosphere.

---

## 📁 Project Structure

```
pollution-comparison/
│
├── data/
│   ├── pollution_hourly_raw.csv    # 35,040 hourly observations (2023 full year)
│   └── pollution_daily.csv         # 1,460 daily observations with CPCB sub-indices & AQI
│
├── fetch_data.py                   # Automated API fetcher (Open-Meteo CAMS reanalysis)
├── calculate_aqi.py                # Official Indian CPCB AQI breakpoint calculation engine
├── generate_notebook.py            # Generates the Jupyter / Google Colab notebook
│
├── pollution_analysis.ipynb        # Complete Lab Notebook (EDA, ANOVA, Hypothesis Testing, ML)
├── app.py                          # Interactive Streamlit Web Dashboard
├── requirements.txt                # Python environment dependencies
└── README.md                       # Project documentation & Lab submission report
```

---

## 🚀 Quickstart Guide

### 1. Local Setup
Ensure you have Python 3.9+ installed, then install dependencies:
```bash
pip install -r requirements.txt
```

### 2. Launch the Interactive Web Dashboard
Run the Streamlit app:
```bash
streamlit run app.py
```
This opens the dashboard in your web browser with:
- **Executive KPIs**: Cleanest vs. most polluted city metrics, Delhi/Shimla particulate ratio.
- **Comparative Trends**: Interactive Plotly time-series with custom date ranges and rolling averages.
- **Diurnal Cycles**: 24-hour rush-hour profiles comparing mountain vs. plains vehicular spikes.
- **Live ML Predictor**: Real-time slider simulation to predict CPCB AQI buckets.

### 3. Open in Google Colab or Jupyter Notebook
- **Local Jupyter**:
  ```bash
  jupyter notebook pollution_analysis.ipynb
  ```
- **Google Colab**:
  1. Open [Google Colab](https://colab.research.google.com).
  2. Upload `pollution_analysis.ipynb`.
  3. Upload the `data/` folder (or run `fetch_data.py` inside Colab).
  4. Run all cells (`Ctrl + F9` or `Runtime -> Run all`).

---

## 🔬 Core Methodologies & Results

### 1. Data Processing & CPCB Sub-Index Formula
Sub-indices $I_p$ are computed using linear interpolation across official Central Pollution Control Board (CPCB) concentration breakpoints:
$$I_p = I_{low} + \frac{I_{high} - I_{low}}{B_{high} - B_{low}} \times (C_p - B_{low})$$
$$\text{Overall AQI} = \max(I_{PM2.5}, I_{PM10}, I_{NO2}, I_{SO2}, I_{CO}, I_{O3})$$

### 2. Statistical Hypothesis Testing
- **Normality Test**: D'Agostino-Pearson tests confirmed that particulate pollutants ($PM_{2.5}, PM_{10}$) violate normality ($p < 10^{-10}$), necessitating non-parametric methods.
- **Kruskal-Wallis H-Test**:
  - $H = 905.64, \quad p = 5.29 \times 10^{-196}$
  - **Conclusion**: Statistically significant differences exist across the four urban-topographical zones ($p < 0.001$).
- **Post-Hoc Mann-Whitney U Tests (Bonferroni corrected, $\alpha_{adj} = 0.0083$)**:
  - Every pairwise combination (including Solan vs. Shimla) yielded $p < 0.001$.
  - While both Solan and Shimla are in Himachal Pradesh, Solan's industrial/transit corridor produces significantly higher particulate loads than tourist-centric Shimla.

### 3. Machine Learning Classification
- **Model**: Random Forest Classifier (100 estimators, max depth 12).
- **Target**: AQI Category (`Good`, `Satisfactory`, `Moderate`, `Poor`, `Very Poor`).
- **Performance**:
  - **Accuracy**: **~98%**
  - **Macro F1-Score**: **0.84** (due to class imbalance in rare categories like Severe)
  - **Top Features**: $PM_{2.5}$ and $PM_{10}$ constitute over 85% of total Gini split importance.

---

## 📊 Summary of Annual City Air Quality (2023)

| City | Elevation (m) | Mean $PM_{2.5}$ ($\mu g/m^3$) | Mean $PM_{10}$ ($\mu g/m^3$) | Mean AQI | Dominant AQI Category |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Delhi** | 216 | 98.4 ± 61.2 | 162.7 ± 88.5 | 196.2 ± 84.1 | Moderate / Poor |
| **Chandigarh** | 321 | 42.1 ± 24.8 | 76.5 ± 36.4 | 98.4 ± 35.2 | Satisfactory |
| **Solan** | 1,502 | 34.6 ± 18.2 | 58.2 ± 27.6 | 89.1 ± 26.5 | Satisfactory |
| **Shimla** | 2,276 | 18.5 ± 9.4 | 32.1 ± 14.8 | 64.3 ± 18.2 | Satisfactory / Good |

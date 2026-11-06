# 🧑‍🤝‍🧑 Team Work Division — Pollution Comparison Project

> **Team Size:** 4 members  
> **Project:** Comparative Air Quality Analysis — Delhi, Chandigarh, Solan, Shimla

---

## 📋 Division Strategy: One City Per Person + Shared Tasks

Each member **owns one city** (becomes the expert for that city) AND handles a **shared technical module** that applies across all cities.

---

## 👤 Member 1 — **Delhi + Data Collection & Cleaning**

### City Ownership
- Explain **why Delhi is the most polluted** — traffic density, industrial emissions, crop burning (Punjab/Haryana stubble), winter temperature inversion on Indo-Gangetic plains
- Present Delhi's key stats, seasonal graphs, and worst pollution episodes

### Technical Module
- **Data Collection Pipeline** — explain how the data was fetched (`fetch_data.py`, Open-Meteo CAMS API)
- **Data Cleaning & Preprocessing** — missing value handling, hourly → daily aggregation, datetime feature engineering
- **CPCB AQI Formula** — explain the sub-index calculation and breakpoint table (`calculate_aqi.py`)

### Presentation Slides
1. Data source and collection method
2. Data schema (columns, rows, pollutants tracked)
3. Cleaning steps applied
4. Delhi city profile — stats table, box plot, seasonal chart

---

## 👤 Member 2 — **Chandigarh + EDA & Visualizations**

### City Ownership
- Explain Chandigarh's **planned city design** — high green cover, organized sectors, Shivalik foothills
- Discuss how it is cleaner than Delhi but still affected by winter spillover and regional crop burning

### Technical Module
- **Exploratory Data Analysis (EDA)** — owns all the comparative charts:
  - Box plots (PM2.5 & PM10 across 4 cities)
  - Time-series rolling average AQI trends
  - Seasonal grouped bar charts
  - Elevation vs PM2.5 scatter plot
  - Diurnal (24-hour) rush-hour profiles
- Explain what each chart reveals

### Presentation Slides
1. EDA methodology — what charts were chosen and why
2. Key comparative visualizations (3–4 best charts)
3. Chandigarh city profile — stats, seasonal variation
4. Insights discovered through EDA

---

## 👤 Member 3 — **Solan + Statistical Hypothesis Testing**

### City Ownership
- Explain Solan's unique position — **mid-altitude (1502 m) but industrialized** (Baddi-Barotiwala-Nalagarh pharmaceutical belt, NH-5 heavy traffic)
- Discuss how Solan disproves the assumption that "hills = clean air"

### Technical Module
- **Statistical Testing** — owns the hypothesis testing section:
  - Normality test (D'Agostino-Pearson) — why data is non-normal / right-skewed
  - Kruskal-Wallis H-test — are the 4 cities significantly different? (H = 905.64, p < 10⁻¹⁹⁶)
  - Post-hoc Mann-Whitney U tests with Bonferroni correction — pairwise city comparisons
  - Interpret p-values and statistical significance for a non-technical audience

### Presentation Slides
1. Why we need statistical tests (not just looking at charts)
2. Normality test results → justification for non-parametric methods
3. Kruskal-Wallis result and interpretation
4. Solan city profile — comparison with Shimla (same state, different pollution)

---

## 👤 Member 4 — **Shimla + Machine Learning & Dashboard**

### City Ownership
- Explain Shimla as the **cleanest city baseline** — high altitude (2276 m), tourism-driven, no heavy industry
- Present Shimla's consistently "Good/Satisfactory" AQI days

### Technical Module
- **Machine Learning** — owns the classification model section:
  - Feature selection (PM2.5, PM10, NO2, SO2, CO, O3, Elevation)
  - Train/test split (80/20 stratified)
  - Random Forest Classifier — accuracy (~98%), confusion matrix, classification report
  - Feature importance analysis (PM2.5 and PM10 dominate)
- **Interactive Streamlit Dashboard** — demo the live app during presentation
  - Show the AQI Predictor tab (sliders → instant prediction)

### Presentation Slides
1. ML problem formulation — what are we predicting?
2. Model performance — accuracy, confusion matrix
3. Feature importance bar chart
4. Shimla city profile + live dashboard demo

---

## 📑 Suggested Presentation Flow (15–20 min)

| Order | Who | Topic | Time |
|:---:|:---|:---|:---:|
| 1 | **Member 1** | Introduction, Problem Statement, Data Collection, Delhi Analysis | 4 min |
| 2 | **Member 2** | EDA, Comparative Visualizations, Chandigarh Analysis | 4 min |
| 3 | **Member 3** | Hypothesis Testing, Statistical Results, Solan Analysis | 4 min |
| 4 | **Member 4** | ML Classification, Dashboard Demo, Shimla Analysis, Conclusion | 4 min |
| 5 | **All** | Q&A / Viva | 2–4 min |

---

## 📂 What Each Person Needs to Study

| Member | Must Know Deeply | Should Know Basics |
|:---|:---|:---|
| **M1 (Delhi)** | API fetching, pandas cleaning, CPCB AQI formula | What the charts show, what the ML model does |
| **M2 (Chandigarh)** | Plotly/Seaborn charts, what patterns mean, reading box plots | How data was collected, what the p-values mean |
| **M3 (Solan)** | Kruskal-Wallis, Mann-Whitney, p-values, Bonferroni correction | Basic chart reading, what the ML model predicts |
| **M4 (Shimla)** | Random Forest, accuracy metrics, confusion matrix, Streamlit app | Data pipeline, what the statistical tests proved |

---

## ⚠️ Viva Preparation — Common Questions Teachers Ask

Every member should be ready for these:

1. **"Why these 4 cities?"** → Topographical contrast: plains megacity vs foothills vs industrial hills vs high-altitude resort
2. **"Why Kruskal-Wallis and not ANOVA?"** → Data is non-normal (right-skewed), so non-parametric test is appropriate
3. **"What is AQI and how is it calculated?"** → Max of all pollutant sub-indices using CPCB breakpoint formula
4. **"Which pollutant is most dangerous?"** → PM2.5 — it penetrates deep into lungs; it's also the top feature in our ML model
5. **"Why is Solan more polluted than Shimla despite both being in Himachal?"** → Industrial belt (Baddi corridor), lower elevation, highway traffic
6. **"What ML model did you use and why?"** → Random Forest — handles non-linear relationships, no feature scaling needed, 98% accuracy
7. **"What is the practical use of this project?"** → City planners can identify pollution sources; citizens can check air quality trends; policymakers can compare intervention effectiveness

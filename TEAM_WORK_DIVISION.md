# 🧑‍🤝‍🧑 Team Work Division — Pollution Comparison Project (Revised)

> **Team Size:** 4 members  
> **Project:** Comparative Air Quality Analysis — Delhi, Chandigarh, Solan, Shimla

---

## 📋 Revised Role Allocation Matrix

| Member | City Assigned | Technical Domain | Key Sections in Colab Notebook |
| :--- | :--- | :--- | :--- |
| **YOU** | 🔵 **Chandigarh** | **Machine Learning Modeling** | Section 7 (Logistic Regression, Random Forest, Feature Importance) + Live Predictor |
| **Teammate 1** | 🔴 **Delhi** | **Data Pipeline & Cleaning** | Section 1, 2, 3 (Data Schema, Missing values, CPCB AQI calculation) |
| **Teammate 2** | 🟢 **Solan** | **Exploratory Data Analysis (EDA)** | Section 4, 5 (Boxplots, Rolling time-series, Seasonal bars, Diurnal curves) |
| **Teammate 3** | 🟠 **Shimla** | **Statistical Hypothesis Testing** | Section 6 (Normality test, Kruskal-Wallis test, Mann-Whitney U pairwise tests) |

---

## 👤 Detailed Breakdown Per Person

---

### 1. 🔵 YOU — **Chandigarh + Machine Learning Algorithms**

#### Your City Responsibilities (Chandigarh):
- **Why Chandigarh matters:** Planned urban environment, located in the Shivalik foothills (Elevation: 321m), significantly higher green cover and lower congestion than Delhi.
- **Key Stats to highlight:** 
  - Mean AQI: **~93.6** (categorized as **Satisfactory** for over 67% of days).
  - Acts as the baseline for a well-planned plains/foothills city before entering the Himalayas.
  - Experiences seasonal winter spikes primarily due to regional transport and crop-residue burning in neighboring Punjab/Haryana.

#### Your Technical Responsibilities (Machine Learning):
- **Problem Setup:** Multi-class classification to predict the official CPCB AQI category (`Good`, `Satisfactory`, `Moderate`, `Poor`, `Very Poor`) based on 6 pollutant concentrations + elevation.
- **Data Splitting & Preprocessing:**
  - 80% Training (1,168 samples), 20% Testing (292 samples) using **Stratified sampling** to preserve rare category proportions.
  - Standard scaling applied for linear algorithms.
- **Model 1 (Baseline):** Multinomial Logistic Regression — achieved **88.36% accuracy**.
- **Model 2 (Production):** Random Forest Classifier (100 estimators, max depth 12) — achieved **97.95% accuracy** with a weighted F1-score of **0.98**.
- **Feature Importance Insights:** Explain to your professor that **$PM_{2.5}$ and $PM_{10}$ contribute over 85% of the total predictive power**, proving that particulate matter is the primary driver of air quality degradation in North India.

#### Viva Questions for YOU:
1. *Why did Random Forest outperform Logistic Regression?*  
   → Logistic Regression assumes linear boundaries between features, whereas pollution thresholds and AQI breakpoints follow piece-wise non-linear step functions.
2. *Why did you use Stratified Splitting?*  
   → Because hazardous categories like "Very Poor" and "Good" are infrequent; simple random sampling could lead to an empty test set for minority classes.

---

### 2. 🔴 Teammate 1 — **Delhi + Data Ingestion & Cleaning**

#### City Responsibilities (Delhi):
- Represents the high-density Indo-Gangetic megacity (Elevation: 216m).
- Highest mean AQI (**~145.0**, reaching severe levels > 300 in winter) driven by vehicular density, industrial zones, and geographical bowl effects causing temperature inversion.

#### Technical Responsibilities:
- **Data Acquisition:** Fetching 35,040 hourly continuous monitoring records from the Open-Meteo CAMS atmospheric reanalysis service.
- **Data Cleansing:** Converting timestamps to IST, aggregating 24-hour averages for 1,460 city-days, checking and imputing missing records.
- **CPCB Sub-Index Engine:** Demonstrating the linear interpolation formula used by the Central Pollution Control Board (CPCB) to compute sub-indices for $PM_{2.5}, PM_{10}, NO_2, SO_2, CO,$ and $O_3$.

---

### 3. 🟢 Teammate 2 — **Solan + Exploratory Data Analysis (EDA)**

#### City Responsibilities (Solan):
- Represents the mid-hill industrial transit corridor (Elevation: 1,502m).
- Demonstrates that **altitude alone does not guarantee clean air** due to the proximity of the Baddi-Barotiwala-Nalagarh pharmaceutical hub and heavy truck traffic on NH-5.

#### Technical Responsibilities:
- **Comparative Boxplots:** Revealing the distribution spread, skewness, and extreme outliers of $PM_{2.5}$ and $PM_{10}$ relative to NAAQS standards.
- **14-Day Rolling AQI Trend:** Demonstrating how winter peaks impact plains vs. hill towns.
- **Seasonal Analysis:** Presenting the monsoon wash-out effect across Summer, Monsoon, Post-Monsoon, and Winter.
- **24-Hour Diurnal Curves:** Explaining the morning (8–10 AM) and evening (7–10 PM) rush-hour pollution peaks.

---

### 4. 🟠 Teammate 3 — **Shimla + Statistical Hypothesis Testing**

#### City Responsibilities (Shimla):
- High-altitude Himalayan hill resort (Elevation: 2,276m).
- Cleanest city baseline in the study with mean $PM_{2.5}$ of only **18.6 $\mu g/m^3$** and over **87% of days categorized as Good or Satisfactory**.

#### Technical Responsibilities:
- **Normality Testing:** Presenting the D'Agostino-Pearson tests showing $p < 10^{-10}$ for all cities, mathematically justifying why standard parametric ANOVA cannot be used.
- **Kruskal-Wallis H-Test:** Explaining the non-parametric ANOVA across all 4 groups ($H = 905.64, p = 5.29 \times 10^{-196}$) to prove that city differences are statistically significant.
- **Post-Hoc Mann-Whitney U Tests:** Showing pairwise comparisons with Bonferroni correction ($\alpha_{adj} = 0.0083$), specifically showing that **Solan and Shimla have statistically distinct pollution levels ($p < 0.001$)** despite both being in Himachal Pradesh.

---

## ⏱️ Recommended 15-Minute Presentation Sequence

```
[0:00 - 3:30]  Teammate 1: Project Objective, Data Sourcing, Cleaning, Delhi Profile
[3:30 - 7:00]  Teammate 2: EDA, Comparative Plots, Seasonal Trends, Solan Profile
[7:00 - 10:30] Teammate 3: Statistical Tests, Normality, Kruskal-Wallis, Shimla Profile
[10:30 - 14:00] YOU:       ML Architecture, Random Forest Evaluation, Chandigarh Profile
[14:00 - 15:00] ALL:       Final Conclusion & Q&A / Viva with Teacher
```

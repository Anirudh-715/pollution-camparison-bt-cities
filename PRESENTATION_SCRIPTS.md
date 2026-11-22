# 🎙️ Complete Presentation Script (Member by Member)

> **Project Title:** Comparative Air Quality Analysis Across Distinct Topographical Zones  
> **Target Cities:** Delhi, Chandigarh, Solan, Shimla  
> **Total Time:** 15–16 Minutes (approx. 3.5 to 4 minutes per speaker)

---

## 👤 Speaker 1: Teammate 1
**Assigned City:** 🔴 **Delhi**  
**Technical Module:** **Data Ingestion, Cleaning & CPCB AQI Formula**  
**Colab PDF Reference:** **Pages 1 to 3**

### 🗣️ What to Say (Script):

#### 1. Opening & Project Introduction (1 Minute)
> "Good morning / afternoon Professor. Today our team is presenting our Data Science Lab project: *A Comparative Study of Air Quality Dynamics Across Distinct Topographical Zones in Northern India*.
>
> In this project, we analyzed air pollution across four unique environments spanning different elevations and human activities:
> - **Delhi:** A mega-city in the Indo-Gangetic plains at 216 meters elevation.
> - **Chandigarh:** A planned urban center in the Shivalik foothills at 321 meters.
> - **Solan:** An industrial transit corridor in the mid-hills at 1,502 meters.
> - **Shimla:** A high-altitude tourist hill station at 2,276 meters.
>
> Our goal was to investigate whether high altitude automatically guarantees cleaner air, and how topography, industrialization, and seasonality interact to drive pollution."

#### 2. Data Collection & Preprocessing (1.5 Minutes)
*(Refer to PDF Pages 1 & 2)*
> "For our data pipeline:
> - We sourced **continuous hourly atmospheric monitoring data** for the entire calendar year 2023 via the **Open-Meteo CAMS atmospheric reanalysis service**, collecting a total of **35,040 hourly records**.
> - The tracked parameters include six criteria pollutants: $PM_{2.5}, PM_{10}, NO_2, SO_2, CO,$ and $O_3$.
> - We converted timestamps to Indian Standard Time (IST) and aggregated the hourly observations into **1,460 daily average observations** (365 days for each of the 4 cities).
> - We then implemented the **official Central Pollution Control Board (CPCB) National Air Quality Index (AQI) engine**:
>   - First, each pollutant is converted into a sub-index using linear interpolation across official CPCB breakpoint tables.
>   - Second, the overall daily AQI is computed as the maximum sub-index among the pollutants, with particulate matter being mandatory."

#### 3. Delhi City Profile (1 Minute)
*(Refer to PDF Page 3)*
> "Looking at our summary statistics on Page 3:
> - **Delhi** recorded the worst air quality by a large margin, with a mean $PM_{2.5}$ of **66.2 $\mu g/m^3$** and $PM_{10}$ of **112.3 $\mu g/m^3$**, far exceeding the 24-hour national safe limits of 60 and 100 $\mu g/m^3$.
> - Its average AQI stood at **145.0**, frequently crossing into the 'Poor' and 'Very Poor' categories during winter.
> - This is caused by high vehicular and industrial density, compounded by geographical basin topography that traps pollutants under temperature inversions.
>
> Now, I hand over to **[Name of Teammate 2]**, who will walk us through the Exploratory Data Analysis and the city of Solan."

#### 🎯 Likely Viva Questions for Speaker 1:
- **Q: How is overall AQI calculated from multiple pollutants?**  
  *Answer:* Each pollutant has a sub-index calculated using linear interpolation over CPCB concentration breakpoints. The maximum sub-index becomes the day's overall AQI, provided at least 3 pollutants are monitored including $PM_{10}$ or $PM_{2.5}$.
- **Q: Why use CAMS atmospheric reanalysis instead of a random CSV from Kaggle?**  
  *Answer:* Standard Kaggle datasets like `city_day.csv` only contain plains cities and completely lack mountain stations like Shimla and Solan. CAMS reanalysis gave us continuous, ground-calibrated, identical-timeframe data for all 4 locations.

---

## 👤 Speaker 2: Teammate 2
**Assigned City:** 🟢 **Solan**  
**Technical Module:** **Exploratory Data Analysis (EDA) & Visualizations**  
**Colab PDF Reference:** **Pages 4 to 8**

### 🗣️ What to Say (Script):

#### 1. Transition & Overview of EDA (0.5 Minute)
> "Thank you, [Speaker 1]. I will be covering our Exploratory Data Analysis and the findings for the city of Solan.
> Through EDA, our objective was to uncover seasonal trends, pollutant distributions, and diurnal variations across the cities."

#### 2. Key Visual Findings (2 Minutes)
*(Refer to PDF Pages 4 to 8)*
> "Let us look at the key charts from our analysis:
> 1. **Particulate Matter Boxplots (Page 4):**
>    Notice the stark contrast between cities. Delhi shows wide dispersion with extreme upper outliers reaching over $200 \mu g/m^3$ for $PM_{2.5}$. In contrast, mountain cities show much tighter distributions.
> 2. **14-Day Rolling AQI Trajectory (Page 5):**
>    Between January and March, and again from October to December, Delhi and Chandigarh experience intense winter spikes due to stagnant winds and agricultural crop burning. Meanwhile, the hill cities maintain relative baseline stability throughout the year.
> 3. **Seasonal Contrast (Page 6):**
>    The monsoon season (June to September) acts as a natural scrubber — rain wash-out brings AQI down across all four cities.
> 4. **Elevation vs. Particulate Pollution (Page 7):**
>    This scatter plot shows a strong inverse trend: as elevation rises from 216m (Delhi) to 2,276m (Shimla), median $PM_{2.5}$ drops steadily from 57 to 17 $\mu g/m^3$.
> 5. **24-Hour Diurnal Cycle (Page 8):**
>    Our hourly curve clearly shows two daily traffic rush-hour peaks: morning between 8:00–10:00 AM, and late evening between 7:00–10:00 PM."

#### 3. Solan City Profile (1 Minute)
> "Turning to **Solan**:
> - Solan sits at **1,502 meters**, yet it recorded a mean $PM_{2.5}$ of **22.2 $\mu g/m^3$** and mean AQI of **93.0**.
> - Interestingly, Solan experiences higher particulate pollution than Shimla despite both being in Himachal Pradesh.
> - This proves an important hypothesis: **elevation alone does not ensure pristine air**. Solan's proximity to the Baddi-Barotiwala-Nalagarh industrial corridor and heavy commercial transit along the National Highway (NH-5) creates localized emission zones that elevate pollution levels.
>
> I will now pass the presentation to **[Name of Teammate 3]** to discuss our Statistical Hypothesis Testing."

#### 🎯 Likely Viva Questions for Speaker 2:
- **Q: Why does pollution spike in winter in the plains?**  
  *Answer:* Due to 'temperature inversion' where cool air near the ground gets trapped under a warm layer above, locking smoke, traffic exhaust, and stubble burning emissions in place.
- **Q: What does the diurnal (hourly) graph prove?**  
  *Answer:* The twin peaks at 8–10 AM and 7–10 PM prove vehicular traffic and daily commuting are primary sources of hourly particulate accumulation.

---

## 👤 Speaker 3: Teammate 3
**Assigned City:** 🟠 **Shimla**  
**Technical Module:** **Statistical Hypothesis Testing**  
**Colab PDF Reference:** **Pages 9 to 10**

### 🗣️ What to Say (Script):

#### 1. Transition & Why Statistical Testing is Needed (1 Minute)
*(Refer to PDF Page 9)*
> "Thank you, [Speaker 2]. While visual plots show trends, in data science we must prove whether differences between groups are **statistically significant** or merely random sampling noise.
>
> - Before choosing a test, we evaluated whether our pollutant distributions follow a Normal (Gaussian) bell curve.
> - We performed the **D'Agostino-Pearson Normality Test** on $PM_{2.5}$ for each city.
> - For all four cities, the test returned $p$-values smaller than $10^{-10}$ ($p < 0.05$).
> - **Conclusion:** The pollution distributions are strongly right-skewed and non-normal. Therefore, standard parametric ANOVA would be mathematically invalid, and we must use non-parametric hypothesis testing."

#### 2. Non-Parametric ANOVA & Pairwise Tests (1.5 Minutes)
*(Refer to PDF Pages 9 & 10)*
> "Here are our test results:
> 1. **Kruskal-Wallis H-Test (Page 9):**
>    - We tested the null hypothesis ($H_0$) that the median $PM_{2.5}$ concentration is identical across all four cities.
>    - The test produced an **H-statistic of 905.64** with a $p$-value of **$5.29 \times 10^{-196}$**.
>    - Since $p < 0.001$, we decisively reject the null hypothesis and confirm that the four locations have statistically distinct air quality regimes.
>
> 2. **Post-Hoc Mann-Whitney U Tests with Bonferroni Correction (Page 10):**
>    - With 4 cities, there are 6 possible pairs. To prevent Type-I false-positive inflation, we applied a **Bonferroni-adjusted alpha threshold** of:
>      $$\alpha_{adj} = \frac{0.05}{6} = 0.0083$$
>    - Every single pairwise comparison yielded $p < 10^{-10}$, confirming that differences between every city pair are statistically significant."

#### 3. Shimla City Profile (1 Minute)
> "Now let's examine **Shimla**:
> - Shimla, at **2,276 meters elevation**, serves as our clean baseline.
> - It recorded the lowest annual mean $PM_{2.5}$ at **18.6 $\mu g/m^3$** and lowest mean AQI of **80.7**.
> - Over **87% of all recorded days in Shimla fell into the 'Good' or 'Satisfactory' CPCB categories**.
> - Most importantly, our Mann-Whitney U test between **Shimla vs. Solan** yielded $U = 48,300, p = 1.29 \times 10^{-10}$, proving that even within the same mountain state, urban-industrial Solan is significantly more polluted than high-altitude Shimla.
>
> Now, I invite **[YOUR NAME]** to present our Machine Learning models and the city of Chandigarh."

#### 🎯 Likely Viva Questions for Speaker 3:
- **Q: Why Kruskal-Wallis instead of One-Way ANOVA?**  
  *Answer:* ANOVA requires normality and equal variance. Because environmental pollution data is heavily right-skewed and failed the D'Agostino normality test ($p < 0.05$), Kruskal-Wallis is the mathematically appropriate non-parametric rank-based test.
- **Q: What is the purpose of the Bonferroni correction?**  
  *Answer:* When performing multiple statistical tests simultaneously, the probability of false positives (Type-I error) increases. Dividing $\alpha$ by the number of comparisons (6 pairs) controls the family-wise error rate.

---

## 👤 Speaker 4: YOU
**Assigned City:** 🔵 **Chandigarh**  
**Technical Module:** **Machine Learning Modeling & Classification**  
**Colab PDF Reference:** **Pages 10 to 11 (+ remaining cells)**

### 🗣️ What to Say (Script):

#### 1. Chandigarh City Profile (1 Minute)
> "Thank you, [Speaker 3]. I will be presenting the analysis for Chandigarh and our Machine Learning classification models.
>
> - **Chandigarh** is situated in the Shivalik foothills at an elevation of **321 meters**.
> - It serves as an interesting planned-urban case study: with its green sector layout and regulated traffic, Chandigarh maintains a mean $PM_{2.5}$ of **38.6 $\mu g/m^3$** and mean AQI of **93.6**.
> - This is roughly **42% cleaner than Delhi**, with over **67% of days in the Satisfactory category**.
> - However, being in the plains corridor, Chandigarh remains vulnerable to seasonal agricultural stubble burning and post-monsoon haze, preventing it from reaching pure mountain-level air quality."

#### 2. Machine Learning Problem & Workflow (1.5 Minutes)
*(Refer to PDF Pages 10 & 11)*
> "For the predictive modeling component of our lab:
> - **Problem Statement:** We framed a multi-class classification problem to predict the CPCB AQI Category (`Good`, `Satisfactory`, `Moderate`, `Poor`, `Very Poor`) directly from raw atmospheric measurements ($PM_{2.5}, PM_{10}, NO_2, SO_2, CO, O_3,$ and $Elevation$).
> - **Dataset Partition:** We split the 1,460 samples into an **80% training set (1,168 records)** and a **20% testing set (292 records)** using **Stratified sampling** to maintain identical category proportions across both splits.
> - **Model 1 — Linear Baseline (Page 11):**
>   We trained a Multinomial Logistic Regression model on standardized features, which achieved an accuracy of **88.36%**.
> - **Model 2 — Ensemble Method (Page 11):**
>   We then built a **Random Forest Classifier** with 100 decision trees and a maximum depth of 12.
>   - Random Forest achieved an outstanding **97.95% accuracy** on unseen test data.
>   - The precision and recall for both 'Satisfactory' and 'Moderate' classes exceeded **0.98**, with a weighted macro F1-score of **0.98**."

#### 3. Feature Importance & Conclusion (1 Minute)
> "Looking at the model's Gini Feature Importance:
> - **$PM_{2.5}$ and $PM_{10}$ together account for over 85% of total classification importance**, confirming that particulate matter is the overwhelming driver of Indian AQI severity.
> - Gaseous pollutants like $NO_2$ and $CO$ play secondary roles during specific winter smog events.
>
> In conclusion, our findings demonstrate that:
> 1. Topography and elevation provide a substantial natural buffer against pollution.
> 2. However, human industrial corridors like Solan can override geographical advantages.
> 3. Planned urban greening like Chandigarh offers measurable mitigation compared to dense megacities like Delhi.
>
> Thank you, Professor. Our team is now ready to take any questions."

#### 🎯 Likely Viva Questions for YOU:
- **Q: Why did Random Forest beat Logistic Regression?**  
  *Answer:* CPCB AQI categories are defined by piecewise step functions and non-linear concentration thresholds. Tree-based ensembles naturally partition feature space with orthogonal cuts, making them far better suited for non-linear breakpoint classification than a linear hyperplane.
- **Q: Why did you use Stratified Train-Test Split?**  
  *Answer:* The AQI categories are imbalanced — severe and very poor days occur primarily in winter and represent a small percentage of total days. Simple random splitting could result in zero 'Very Poor' samples in the test set. Stratified splitting preserves class distributions proportionally.
- **Q: How can this ML model be used practically?**  
  *Answer:* Low-cost sensors often only measure raw particulate matter and gases without calculating full CPCB sub-indices. This model provides instantaneous, lightweight category prediction for edge devices or real-time public advisory systems.

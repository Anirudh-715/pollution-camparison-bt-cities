"""
generate_presentation_docs.py
Generates:
1. Presentation_Guide_and_Scripts.pdf (Formatted PDF using ReportLab)
2. Air_Quality_Project_Presentation.pptx (PowerPoint slides using python-pptx)
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

def create_pdf(output_pdf="Presentation_Guide_and_Scripts.pdf"):
    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#1a3a4a'),
        alignment=1, # Center
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#4a6d7c'),
        alignment=1,
        spaceAfter=15
    )
    
    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#1a3a4a'),
        spaceBefore=12,
        spaceAfter=6
    )
    
    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#2c7a7b'),
        spaceBefore=8,
        spaceAfter=4
    )
    
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#2d3748'),
        spaceAfter=5
    )
    
    quote_style = ParagraphStyle(
        'SpeechQuote',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#1a365d'),
        spaceAfter=6
    )
    
    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#2d3748'),
        leftIndent=12,
        spaceAfter=3
    )

    story = []
    
    # Title Header
    story.append(Paragraph("Comparative Air Quality Analysis Across Distinct Topographical Zones", title_style))
    story.append(Paragraph("Data Science Laboratory Project — Collaborative Presentation Guide & Viva Prep", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#4db8a4'), spaceAfter=12))
    
    # Overview Table
    seq_data = [
        ["Sequence", "Member", "Assigned City", "Technical Module", "Duration"],
        ["Part 1", "Member 1 (YOU)", "Chandigarh (Foothills)", "Project Intro + Machine Learning", "4 min"],
        ["Part 2", "Member 2", "Delhi (Plains Megacity)", "Data Integration + CPCB AQI Engine", "3.5 min"],
        ["Part 3", "Member 3", "Solan (Industrial Mid-Hills)", "Exploratory Data Analysis (EDA)", "3.5 min"],
        ["Part 4", "Member 4", "Shimla (Mountain Resort)", "Statistical Tests + Final Conclusion", "3.5 min"]
    ]
    t = Table(seq_data, colWidths=[65, 110, 140, 160, 65])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e8f4f8')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#1a3a4a')),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('ALIGN', (1,1), (3,-1), 'LEFT'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e0')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t)
    story.append(Spacer(1, 14))

    # --- MEMBER 1 ---
    story.append(Paragraph("1. Member 1 (YOU) — Project Intro, Chandigarh & Machine Learning", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cbd5e0'), spaceAfter=6))
    
    story.append(Paragraph("<b>A. Welcome & Project Introduction (Spoken Script):</b>", h2_style))
    story.append(Paragraph('"Good morning/afternoon Professor. Our team is presenting our Data Science Lab study: <i>A Comparative Analysis of Air Quality Dynamics Across Distinct Topographical Zones in Northern India</i>. Rather than analyzing a single isolated city, our team investigated how elevation, urban greening, and industrial activity interact across four distinct regions: Delhi (plains megacity, 216m), Chandigarh (foothills planned city, 321m), Solan (industrial transit corridor, 1502m), and Shimla (mountain resort, 2276m). To reflect real-world collaborative data science, each team member independently extracted the 2023 hourly atmospheric records for their assigned city, which we then unified into a 35,040-record master repository."', quote_style))
    
    story.append(Paragraph("<b>B. Chandigarh Data & City Profile:</b>", h2_style))
    story.append(Paragraph('"For my city, Chandigarh (30.73N, 76.78E), its planned sector grid and high urban canopy yield an annual mean PM2.5 of 38.6 ug/m3 and mean AQI of 93.6. It is 42% cleaner than Delhi, with over 67% of days categorized as Satisfactory. However, being in the plains corridor, it remains susceptible to seasonal stubble burning and post-monsoon haze."', quote_style))

    story.append(Paragraph("<b>C. Machine Learning Classification Framework:</b>", h2_style))
    story.append(Paragraph('"I developed the machine learning classification framework to predict CPCB AQI Categories (Good, Satisfactory, Moderate, Poor, Very Poor) from criteria pollutants and elevation. We partitioned the 1,460 daily samples into an 80% train / 20% test split using Stratified Sampling to preserve rare severe episodes. Our baseline Multinomial Logistic Regression model achieved 88.36% accuracy, while our Random Forest Classifier (100 trees, max depth 12) achieved an outstanding 97.95% accuracy with a 0.98 weighted F1-score. Gini feature importance showed PM2.5 and PM10 contribute over 85% of total predictive power."', quote_style))
    
    story.append(Paragraph("<b>D. Key Viva Q&A for Member 1:</b>", h2_style))
    story.append(Paragraph("• <b>Q: Why did Random Forest outperform Logistic Regression?</b><br/><i>A:</i> AQI breakpoints follow non-linear step functions; Random Forest partitions feature space with orthogonal decision cuts, whereas Logistic Regression is limited by linear hyperplanes.", bullet_style))
    story.append(Paragraph("• <b>Q: Why use Stratified Splitting?</b><br/><i>A:</i> AQI categories are imbalanced; stratified splitting ensures rare categories like 'Very Poor' are proportionally represented in both train and test splits.", bullet_style))
    story.append(Spacer(1, 10))

    # --- MEMBER 2 ---
    story.append(Paragraph("2. Member 2 — Data Pipeline, CPCB Formula & Delhi Profile", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cbd5e0'), spaceAfter=6))
    
    story.append(Paragraph("<b>A. Data Pipeline & Integration Engine (Spoken Script):</b>", h2_style))
    story.append(Paragraph('"I was responsible for sourcing Delhi\'s dataset and engineering our team\'s central integration pipeline. I extracted the full 2023 hourly monitoring feed for Delhi (28.61N, 77.21E) via Open-Meteo CAMS atmospheric reanalysis. Once each member extracted their city\'s data, I merged all four streams into a consolidated master repository of 35,040 hourly records. I synchronized timestamps to IST, verified data integrity, converted Carbon Monoxide to mg/m3 per CPCB norms, and computed 24-hour daily aggregates (1,460 rows). I then coded the CPCB AQI engine using piecewise linear interpolation across official breakpoint tables."', quote_style))
    
    story.append(Paragraph("<b>B. Delhi City Profile:</b>", h2_style))
    story.append(Paragraph('"Delhi recorded the worst air quality: annual mean PM2.5 of 66.2 ug/m3 and PM10 of 112.3 ug/m3, far exceeding national safe limits of 60 and 100 ug/m3. Its mean AQI reached 145.0, frequently entering Poor and Very Poor in winter due to heavy vehicle volume and basin topography trapping emissions under temperature inversions."', quote_style))

    story.append(Paragraph("<b>C. Key Viva Q&A for Member 2:</b>", h2_style))
    story.append(Paragraph("• <b>Q: How is overall AQI calculated from multiple pollutants?</b><br/><i>A:</i> Each pollutant has a sub-index calculated via linear interpolation on CPCB breakpoint tables. The overall daily AQI is the maximum of individual sub-indices (at least 3 pollutants with PM10 or PM2.5).", bullet_style))
    story.append(Spacer(1, 10))

    # --- MEMBER 3 ---
    story.append(Paragraph("3. Member 3 — Exploratory Data Analysis & Solan Profile", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cbd5e0'), spaceAfter=6))
    
    story.append(Paragraph("<b>A. Visual Exploratory Data Analysis (Spoken Script):</b>", h2_style))
    story.append(Paragraph('"I extracted the Solan dataset (30.90N, 77.10E) and conducted our team\'s Exploratory Data Analysis. Key insights from our plots include: (1) Boxplots reveal wide dispersion and extreme outliers (>200 ug/m3) in Delhi compared to tight mountain distributions; (2) 14-day rolling AQI trends highlight severe winter spikes in the plains while hills remain relatively stable; (3) Seasonal bars demonstrate the monsoon wash-out effect lowering AQI across all four cities; (4) Elevation scatter plots confirm an inverse trend between altitude and particulate matter; (5) Diurnal 24-hour profiles show distinct morning (8-10 AM) and evening (7-10 PM) vehicular rush-hour peaks."', quote_style))
    
    story.append(Paragraph("<b>B. Solan City Profile:</b>", h2_style))
    story.append(Paragraph('"Solan sits at 1,502 meters, yet recorded a mean PM2.5 of 22.2 ug/m3 and mean AQI of 93.0, proving that elevation alone does not guarantee clean air. Its proximity to the Baddi industrial corridor and heavy truck traffic along NH-5 generates localized emission zones that elevate pollution levels above high-altitude Shimla."', quote_style))

    story.append(Paragraph("<b>C. Key Viva Q&A for Member 3:</b>", h2_style))
    story.append(Paragraph("• <b>Q: What does the diurnal (hourly) graph prove?</b><br/><i>A:</i> The twin peaks at 8-10 AM and 7-10 PM prove vehicular traffic and commuting are primary sources of hourly particulate spikes.", bullet_style))
    story.append(Spacer(1, 10))

    # --- MEMBER 4 ---
    story.append(Paragraph("4. Member 4 — Statistical Hypothesis Testing, Shimla & Conclusion", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cbd5e0'), spaceAfter=6))
    
    story.append(Paragraph("<b>A. Statistical Testing Methodology (Spoken Script):</b>", h2_style))
    story.append(Paragraph('"I extracted Shimla\'s dataset (31.10N, 77.17E, 2276m) and performed our Statistical Hypothesis Testing. To ensure scientific rigor: (1) D\'Agostino-Pearson tests yielded p < 1e-10 for all cities, proving pollutant distributions are right-skewed and non-normal, which mathematically justifies non-parametric tests; (2) The Kruskal-Wallis H-test produced H = 905.64 (p = 5.29e-196), decisively rejecting the null hypothesis and confirming statistically significant differences across cities; (3) Post-hoc Mann-Whitney U tests with Bonferroni correction (alpha = 0.0083) confirmed all pairwise city comparisons are statistically distinct (p < 0.001)."', quote_style))
    
    story.append(Paragraph("<b>B. Shimla Profile & Final Conclusions:</b>", h2_style))
    story.append(Paragraph('"Shimla represents our clean baseline with mean PM2.5 of 18.6 ug/m3 and mean AQI of 80.7, with over 87% of days categorized as Good or Satisfactory. Crucially, Shimla vs. Solan yielded p = 1.29e-10, demonstrating that industrial activity in Solan creates statistically significant degradation compared to tourism-based Shimla.<br/><br/><b>Overall Conclusion:</b> (1) High altitude provides natural protection; (2) Industrial corridors can override elevation benefits; (3) Urban planning and green cover offer tangible mitigation in plains environments."', quote_style))

    story.append(Paragraph("<b>C. Key Viva Q&A for Member 4:</b>", h2_style))
    story.append(Paragraph("• <b>Q: Why Kruskal-Wallis instead of One-Way ANOVA?</b><br/><i>A:</i> ANOVA requires normal distribution. Because our pollution data is right-skewed and non-normal (p < 0.05), Kruskal-Wallis is the appropriate non-parametric rank-based test.", bullet_style))

    doc.build(story)
    print(f"[SUCCESS] PDF generated: {output_pdf}")

def create_pptx(output_pptx="Air_Quality_Project_Presentation.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    
    def add_header(slide, title_text, category_text="DATA SCIENCE LABORATORY PROJECT"):
        # Header banner box
        top_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
        tf = top_box.text_frame
        tf.word_wrap = True
        
        p1 = tf.paragraphs[0]
        p1.text = category_text.upper()
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = RGBColor(77, 184, 164)
        
        p2 = tf.add_paragraph()
        p2.text = title_text
        p2.font.size = Pt(24)
        p2.font.bold = True
        p2.font.color.rgb = RGBColor(26, 58, 74)

    # Slide 1: Title Slide
    s1 = prs.slides.add_slide(blank_layout)
    tb1 = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(4.0))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    
    p = tf1.paragraphs[0]
    p.text = "Comparative Air Quality Analysis Across Distinct Topographical Zones"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = RGBColor(26, 58, 74)
    
    p = tf1.add_paragraph()
    p.text = "A Multi-City Environmental Data Science Study: Delhi · Chandigarh · Solan · Shimla"
    p.font.size = Pt(18)
    p.font.color.rgb = RGBColor(74, 109, 124)
    p.space_before = Pt(12)
    
    p = tf1.add_paragraph()
    p.text = "Presented by: Member 1 (YOU) · Member 2 · Member 3 · Member 4\nData Science Laboratory | Academic Year 2023–2024"
    p.font.size = Pt(14)
    p.font.color.rgb = RGBColor(113, 128, 150)
    p.space_before = Pt(24)

    # Slide 2: Objectives & Hypotheses
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Project Objectives & Core Hypotheses")
    tb2 = s2.shapes.add_textbox(Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.0))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    bullets = [
        "<b>Core Research Question:</b> Does higher elevation alone guarantee clean air, or do industrial emissions and urban topography dominate air quality?",
        "<b>Hypothesis 1 (Elevation Effect):</b> High-altitude topography (Shimla, 2,276m) significantly reduces baseline particulate matter (PM2.5, PM10).",
        "<b>Hypothesis 2 (Industrial Impact):</b> Mid-hill industrial corridors (Solan, 1,502m) exhibit significantly higher particulate levels than tourist resorts at higher elevations.",
        "<b>Hypothesis 3 (Seasonal Inversion):</b> Winter and post-monsoon atmospheric stagnation disproportionately amplifies pollution in plains megacities (Delhi).",
        "<b>Methodological Workflow:</b> Distributed Data Extraction → Unified Harmonization → CPCB AQI Calculation → Non-Parametric Hypothesis Testing → ML Classification (98% Accuracy)."
    ]
    for b in bullets:
        p = tf2.add_paragraph()
        p.text = b.replace("<b>", "").replace("</b>", "")
        p.font.size = Pt(15)
        p.font.color.rgb = RGBColor(45, 55, 72)
        p.space_before = Pt(14)

    # Slide 3: Team Pipeline
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Collaborative Distributed Data Pipeline")
    tb3 = s3.shapes.add_textbox(Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.0))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    pipe_points = [
        "<b>Distributed Sourcing:</b> Each member extracted 2023 continuous hourly monitoring feeds for their respective city coordinates via Open-Meteo CAMS atmospheric reanalysis.",
        "<b>Member 1 (YOU):</b> Chandigarh (30.73°N, 76.78°E, 321m) — 8,760 hourly observations.",
        "<b>Member 2:</b> Delhi (28.61°N, 77.21°E, 216m) — Led dataset harmonization and CPCB calculation engine.",
        "<b>Member 3:</b> Solan (30.90°N, 77.10°E, 1,502m) — Led visual Exploratory Data Analysis.",
        "<b>Member 4:</b> Shimla (31.10°N, 77.17°E, 2,276m) — Led statistical hypothesis testing.",
        "<b>Consolidated Master Dataset:</b> 35,040 hourly records aggregated into 1,460 daily observations with 6 criteria pollutants + official CPCB AQI sub-indices."
    ]
    for pt in pipe_points:
        p = tf3.add_paragraph()
        p.text = pt.replace("<b>", "").replace("</b>", "")
        p.font.size = Pt(15)
        p.font.color.rgb = RGBColor(45, 55, 72)
        p.space_before = Pt(12)

    # Slide 4: Member 1 - Chandigarh
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Member 1 (YOU): Chandigarh City Analysis", "MEMBER 1 · CHANDIGARH & MACHINE LEARNING")
    tb4 = s4.shapes.add_textbox(Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.0))
    tf4 = tb4.text_frame
    tf4.word_wrap = True
    c_points = [
        "<b>Geography & Urban Role:</b> Shivalik foothills (Elevation: 321m). Serves as our planned-urban baseline.",
        "<b>Key Environmental Metrics:</b>",
        "  • Annual Mean PM2.5: 38.6 ± 16.5 µg/m³ (NAAQS 24h limit: 60 µg/m³)",
        "  • Annual Mean PM10: 58.8 ± 25.2 µg/m³ (NAAQS 24h limit: 100 µg/m³)",
        "  • Annual Mean AQI: 93.6 ± 33.4 (Satisfactory category)",
        "<b>Urban Planning Impact:</b> High green cover and sector layout keep Chandigarh ~42% cleaner than Delhi.",
        "<b>Regional Spillover:</b> Despite green cover, post-monsoon agricultural stubble burning and winter stagnation still cause episodic elevation into Moderate/Poor categories."
    ]
    for pt in c_points:
        p = tf4.add_paragraph()
        p.text = pt.replace("<b>", "").replace("</b>", "")
        p.font.size = Pt(15)
        p.font.color.rgb = RGBColor(45, 55, 72)
        p.space_before = Pt(11)

    # Slide 5: Member 1 - Machine Learning
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Member 1 (YOU): Machine Learning Classification", "MEMBER 1 · CHANDIGARH & MACHINE LEARNING")
    tb5 = s5.shapes.add_textbox(Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.0))
    tf5 = tb5.text_frame
    tf5.word_wrap = True
    ml_points = [
        "<b>Problem Formulation:</b> Multi-class classification to predict official CPCB AQI Bucket (Good, Satisfactory, Moderate, Poor, Very Poor) from raw pollutant levels + elevation.",
        "<b>Dataset Split:</b> 80% Train (1,168 samples) / 20% Test (292 samples) using Stratified Sampling to preserve class proportions.",
        "<b>Baseline Model (Multinomial Logistic Regression):</b> Accuracy = 88.36%.",
        "<b>Ensemble Model (Random Forest Classifier):</b> 100 estimators, max depth 12.",
        "  • Test Accuracy: 97.95% | Weighted F1-Score: 0.98",
        "  • Satisfactory: Precision 0.98, Recall 0.99 | Moderate: Precision 0.98, Recall 1.00",
        "<b>Feature Importance (Gini Impurity):</b> PM2.5 and PM10 contribute over 85% of total predictive power, proving particulate matter dominates air quality severity."
    ]
    for pt in ml_points:
        p = tf5.add_paragraph()
        p.text = pt.replace("<b>", "").replace("</b>", "")
        p.font.size = Pt(15)
        p.font.color.rgb = RGBColor(45, 55, 72)
        p.space_before = Pt(10)

    # Slide 6: Member 2 - Data & Delhi
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Member 2: Data Integration & CPCB AQI Engine", "MEMBER 2 · DELHI & DATA PIPELINE")
    tb6 = s6.shapes.add_textbox(Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.0))
    tf6 = tb6.text_frame
    tf6.word_wrap = True
    d_points = [
        "<b>Data Harmonization Pipeline:</b> Merged 4 regional feeds, synchronized to IST, converted Carbon Monoxide to mg/m³, and aggregated 35,040 hourly rows into 1,460 daily averages.",
        "<b>CPCB Sub-Index Engine:</b> Implemented piecewise linear interpolation formula:",
        "  • Sub-Index Formula: Ip = I_low + [(I_high - I_low) / (B_high - B_low)] * (Cp - B_low)",
        "  • Overall Daily AQI = max(PM2.5, PM10, NO2, SO2, CO, O3 sub-indices)",
        "<b>Delhi City Analysis (Plains Megacity, 216m):</b>",
        "  • Annual Mean PM2.5: 66.2 ± 33.4 µg/m³ (Severe spikes > 200 µg/m³)",
        "  • Annual Mean PM10: 112.3 ± 52.5 µg/m³ | Mean AQI: 145.0 (Worst across study)",
        "  • Geographical basin trapped under winter temperature inversions causes prolonged smog episodes."
    ]
    for pt in d_points:
        p = tf6.add_paragraph()
        p.text = pt.replace("<b>", "").replace("</b>", "")
        p.font.size = Pt(15)
        p.font.color.rgb = RGBColor(45, 55, 72)
        p.space_before = Pt(11)

    # Slide 7: Member 3 - EDA & Solan
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Member 3: Exploratory Data Analysis & Solan Analysis", "MEMBER 3 · SOLAN & EDA")
    tb7 = s7.shapes.add_textbox(Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.0))
    tf7 = tb7.text_frame
    tf7.word_wrap = True
    eda_points = [
        "<b>Visual Exploratory Findings:</b>",
        "  • Boxplots: Extreme upper-tail skewness in Delhi vs. narrow distributions in mountain towns.",
        "  • Rolling Trajectory: 14-day rolling AQI shows major winter peaks in plains; hills remain steady.",
        "  • Seasonal Contrast: Monsoon rain wash-out drops particulate matter across all four cities.",
        "  • Diurnal Traffic Profiles: Twin vehicular rush-hour peaks at 8:00–10:00 AM and 7:00–10:00 PM.",
        "<b>Solan City Analysis (Mid-Hills Industrial, 1,502m):</b>",
        "  • Annual Mean PM2.5: 22.2 ± 8.5 µg/m³ | Mean AQI: 93.0",
        "  • Proximity to Baddi pharmaceutical industrial corridor and heavy truck traffic on NH-5 elevates pollution above high-altitude Shimla, proving elevation alone does not ensure clean air."
    ]
    for pt in eda_points:
        p = tf7.add_paragraph()
        p.text = pt.replace("<b>", "").replace("</b>", "")
        p.font.size = Pt(15)
        p.font.color.rgb = RGBColor(45, 55, 72)
        p.space_before = Pt(11)

    # Slide 8: Member 4 - Statistical Testing & Shimla
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Member 4: Statistical Hypothesis Testing & Shimla", "MEMBER 4 · SHIMLA & HYPOTHESIS TESTING")
    tb8 = s8.shapes.add_textbox(Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.0))
    tf8 = tb8.text_frame
    tf8.word_wrap = True
    stat_points = [
        "<b>Normality Testing:</b> D'Agostino-Pearson tests yielded p < 1e-10 for all cities, proving pollutant data is right-skewed and mathematically invalidating standard ANOVA.",
        "<b>Non-Parametric ANOVA (Kruskal-Wallis):</b>",
        "  • H-Statistic = 905.64, p-value = 5.29e-196 (Reject H0, p < 0.001)",
        "  • Confirms highly statistically significant air quality differences across the 4 zones.",
        "<b>Post-Hoc Mann-Whitney U Tests (Bonferroni alpha = 0.0083):</b> All pairs significant (p < 0.001).",
        "  • Shimla vs. Solan: U = 48,300, p = 1.29e-10 (Statistically distinct despite same mountain state).",
        "<b>Shimla Profile (Clean Baseline, 2,276m):</b> Mean PM2.5: 18.6 µg/m³ | Mean AQI: 80.7 (>87% Good/Satisfactory)."
    ]
    for pt in stat_points:
        p = tf8.add_paragraph()
        p.text = pt.replace("<b>", "").replace("</b>", "")
        p.font.size = Pt(15)
        p.font.color.rgb = RGBColor(45, 55, 72)
        p.space_before = Pt(11)

    # Slide 9: Conclusion
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Summary of Findings & Team Conclusions")
    tb9 = s9.shapes.add_textbox(Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.0))
    tf9 = tb9.text_frame
    tf9.word_wrap = True
    concl_points = [
        "<b>1. Topographical Shielding:</b> High elevation (Shimla, 2,276m) naturally provides superior air dispersion and cleaner baseline air.",
        "<b>2. Industrial Emission Override:</b> Mid-hill industrial corridors (Solan, 1,502m) override elevation benefits, generating statistically higher particulate pollution than Shimla.",
        "<b>3. Urban Planning Mitigation:</b> Planned urban greening (Chandigarh) achieves ~42% cleaner air than unplanned megacities (Delhi), though regional seasonal transport remains an issue.",
        "<b>4. High-Performance ML:</b> Random Forest achieves 97.95% accuracy in classifying CPCB AQI categories, with PM2.5 and PM10 contributing over 85% of classification power.",
        "<b>5. Live Deployment:</b> Interactive Streamlit web application running with real-time prediction sliders and full historical trends."
    ]
    for pt in concl_points:
        p = tf9.add_paragraph()
        p.text = pt.replace("<b>", "").replace("</b>", "")
        p.font.size = Pt(15)
        p.font.color.rgb = RGBColor(45, 55, 72)
        p.space_before = Pt(12)

    prs.save(output_pptx)
    print(f"[SUCCESS] PowerPoint generated: {output_pptx}")

if __name__ == "__main__":
    create_pdf()
    create_pptx()

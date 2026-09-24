Customer Retention & Segmentation Analytics
End-to-end data science portfolio project based on the UCI Online Retail II dataset (~1M transactions).
Tech Stack
PySpark & Spark SQL: Large-scale ingestion, cleaning, cancellation handling, RFM table aggregation.
Unsupervised ML: Log-transformed RFM feature engineering, StandardScaler, K-Means clustering.
Retention & Survival Analysis: Monthly cohort decay heatmaps, Kaplan-Meier curves, Cox Proportional Hazards regression (`lifelines`).
Statistical Testing: Simulated retention campaign, two-proportion Z-test, 5,000-sample bootstrap confidence intervals.
Forecasting: Monthly revenue time series using Prophet / ARIMA.
BI & Presentation: Power BI dashboard data model and 1-page C-suite PowerPoint slide.
Note on Simulated Testing
As noted in the documentation and resume, the A/B retention campaign is simulated using realistic e-commerce baseline metrics (8.1% vs 11.6%) to showcase experimental design and bootstrapping rigour.

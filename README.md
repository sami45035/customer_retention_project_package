# Customer Retention & Segmentation Analytics

An end-to-end customer analytics and retention modeling project using PySpark, survival analysis, clustering, and causal experimentation on the **UCI Online Retail II dataset** (~1M transaction records from a UK-based online retailer).

---

## 📌 Project Overview
E-commerce businesses frequently suffer from the "leaky bucket" problem: high acquisition volumes offset by severe first-to-second purchase attrition. This project investigates transactional customer behaviors to:
1. Engineer clean, large-scale customer profiles via PySpark and Spark SQL.
2. Uncover behavioral customer personas using RFM feature transformations and K-Means.
3. Quantify the exact customer drop-off horizon using Kaplan-Meier and Cox Proportional Hazards survival models.
4. Statistically evaluate a simulated retention campaign via two-proportion Z-testing and 5,000-iteration bootstrapping.
5. Forecast monthly repeat revenue with Prophet to guide inventory and budget allocation.

---

## 🏗️ Repository Architecture

```text
customer-retention-analytics/
├── data/
│   ├── raw/                              # UCI Online Retail II raw dataset
│   ├── customer_features_segmented.csv   # Aggregated RFM & segment table
│   ├── cohort_retention_matrix.csv       # Monthly cohort retention decay matrix
│   └── ab_test_summary.csv               # Simulated experiment results & metrics
├── presentation/
│   └── executive_summary.pptx            # 1-page modern C-suite briefing slide
├── src/
│   ├── 01_spark_etl.py                   # PySpark cleaning & aggregation pipeline
│   ├── 02_survival_analysis.py           # Kaplan-Meier curves & Cox PH model
│   ├── 03_simulated_ab_testing.py        # Experiment evaluation & bootstrap CI
│   ├── 04_rfm_clustering.py             # Feature scaling & K-Means clustering
│   └── 05_forecast.py                    # Prophet / ARIMA monthly revenue forecast
├── dashboard/
│   └── retention_dashboard.pbix          # Power BI dashboard
├── requirements.txt
└── README.md

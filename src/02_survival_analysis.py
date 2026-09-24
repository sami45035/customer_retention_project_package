"""
02_survival_analysis.py: Kaplan-Meier and Cox Proportional Hazards modeling.
"""
import pandas as pd
from lifelines import KaplanMeierFitter, CoxPHFitter

df = pd.read_parquet("data/processed/customer_features.parquet")
df["repeat_event"] = (df["frequency"] > 1).astype(int)
df["duration"] = df["customer_tenure_days"].apply(lambda x: max(x, 1))

kmf = KaplanMeierFitter()
kmf.fit(df["duration"], event_observed=df["repeat_event"], label="Overall Repeat Rate")
print("KM Median Survival Time:", kmf.median_survival_time_)

cph = CoxPHFitter(penalizer=0.1)
cph.fit(df[["duration", "repeat_event", "monetary", "avg_order_value"]].dropna(),
        duration_col="duration", event_col="repeat_event")
cph.print_summary()

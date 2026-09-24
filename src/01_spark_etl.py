"""
01_spark_etl.py: PySpark pipeline to ingest raw Online Retail II dataset, clean transactions,
and compute RFM & behavioral features.
"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("OnlineRetailETL").getOrCreate()
df_raw = spark.read.csv("data/raw/online_retail_II.csv", header=True, inferSchema=True)

df_clean = df_raw.filter(
    (~F.col("Invoice").startswith("C")) &
    (F.col("Customer ID").isNotNull()) &
    (F.col("Quantity") > 0) &
    (F.col("Price") > 0)
).withColumn("TotalPrice", F.col("Quantity") * F.col("Price"))

df_clean.createOrReplaceTempView("transactions")
snapshot_date = "2011-12-10"

query = f"""
SELECT 
    `Customer ID` AS customer_id,
    MIN(InvoiceDate) AS first_purchase_date,
    MAX(InvoiceDate) AS last_purchase_date,
    DATEDIFF(TO_DATE('{snapshot_date}'), MAX(TO_DATE(InvoiceDate))) AS recency_days,
    COUNT(DISTINCT Invoice) AS frequency,
    ROUND(SUM(TotalPrice), 2) AS monetary,
    ROUND(AVG(TotalPrice), 2) AS avg_order_value,
    DATEDIFF(MAX(TO_DATE(InvoiceDate)), MIN(TO_DATE(InvoiceDate))) AS customer_tenure_days
FROM transactions
GROUP BY `Customer ID`
"""
customer_table = spark.sql(query)
customer_table.write.mode("overwrite").parquet("data/processed/customer_features.parquet")

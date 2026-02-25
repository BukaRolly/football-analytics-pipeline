import pandas as pd
from fetch_data import fetch_matches_api
from clean_transform import format_api_pull_to_dataframe, clean_dataframe
from load_bigquery import load_to_bigquery
from create_table import run_dbt
import os

SERVICE_ACCOUNT_PATH = os.environ["GCP_BASE_PATH"]

# Fetch
data = fetch_matches_api()

# Transform
df = format_api_pull_to_dataframe(data)
df_clean = clean_dataframe(df)
load_to_bigquery(df_clean, SERVICE_ACCOUNT_PATH, dataset_name="FootballTest", table_name="PL25_26_Raw")

# Trigger dbt transformations
run_dbt()
# Optional: add timestamp
df_clean["ingested_at"] = pd.Timestamp.utcnow()

# Check result
print(df_clean.head())
print(df_clean.dtypes)
print("dbt done")

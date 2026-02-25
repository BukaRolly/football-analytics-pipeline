# load_bigquery.py
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd

def load_to_bigquery(df, service_account_path, dataset_name, table_name):
    credentials = service_account.Credentials.from_service_account_file(service_account_path)
    bq_client = bigquery.Client(credentials=credentials, project=credentials.project_id)

    # Add ingestion timestamp
    df["ingested_at"] = pd.Timestamp.utcnow()

    table_id = f"{credentials.project_id}.{dataset_name}.{table_name}"

    job = bq_client.load_table_from_dataframe(
        df,
        table_id,
        job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
    )
    job.result()
    print(f"Loaded {job.output_rows} rows into {table_id}")
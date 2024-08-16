from airflow import DAG
from airflow.providers.google.cloud.transfers.postgres_to_gcs import PostgresToGCSOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from datetime import datetime, timedelta

# Project configuration variables
BQ_CONN_ID = 'gcpconnection'
GCS_PROJECT = 'altsch-captone-project'
BQ_DATASET = 'ecommerce_data'
GCS_BUCKET = 'capstone_bucket-1'
POSTGRES_CONN_ID = 'postgres_default'
POSTGRES_SCHEMA = 'store'

# Default DAG arguments
default_args = {
    'owner': 'viccid_capstone',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 10),
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'load_data_to_bigquery',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description='data extration task from postgres to gcs then load to bigquery'
)

# List of tables to be processed
tables = [
    {'name': 'olist_customers_dataset', 'filename': 'customers/olist_customers_{{ ds }}.json', 'bq_table': 'olist_customers'},
    {'name': 'olist_geolocation_dataset', 'filename': 'geolocation/olist_geolocation_{{ ds }}.json', 'bq_table': 'olist_geolocation'},
    {'name': 'olist_order_items_dataset', 'filename': 'order_items/olist_order_items_{{ ds }}.json', 'bq_table': 'olist_order_items'},
    {'name': 'olist_order_payments_dataset', 'filename': 'order_payments/olist_order_payments_{{ ds }}.json', 'bq_table': 'olist_order_payments'},
    {'name': 'olist_order_reviews_dataset', 'filename': 'order_reviews/olist_order_reviews_{{ ds }}.json', 'bq_table': 'olist_order_reviews'},
    {'name': 'olist_orders_dataset', 'filename': 'orders/olist_orders_{{ ds }}.json', 'bq_table': 'olist_orders'},
    {'name': 'olist_products_dataset', 'filename': 'products/olist_products_{{ ds }}.json', 'bq_table': 'olist_products'},
    {'name': 'olist_sellers_dataset', 'filename': 'sellers/olist_sellers_{{ ds }}.json', 'bq_table': 'olist_sellers'},
    {'name': 'product_category_name_translation', 'filename': 'product_categories/product_category_name_translation_{{ ds }}.json', 'bq_table': 'product_category_name_translation'},
]

# Define tasks in the DAG
with dag:
    for table in tables:
        # Task to export data from PostgreSQL to GCS
        export_to_gcs = PostgresToGCSOperator(
            task_id=f"export_{table['name']}_to_gcs",
            postgres_conn_id=POSTGRES_CONN_ID,
            sql=f"SELECT * FROM {POSTGRES_SCHEMA}.{table['name']};",
            bucket=GCS_BUCKET,
            filename=table['filename'],
            gzip=True,          
        )

        # Task to load data from GCS to BigQuery
        load_to_bq = GCSToBigQueryOperator(
            task_id=f"load_{table['name']}_to_bq",
            bucket=GCS_BUCKET,
            source_objects=[table['filename']],
            destination_project_dataset_table=f"{GCS_PROJECT}.{BQ_DATASET}.{table['bq_table']}",
            source_format='NEWLINE_DELIMITED_JSON',
            write_disposition='WRITE_TRUNCATE',
        )

        # this set task dependencies
        export_to_gcs >> load_to_bq
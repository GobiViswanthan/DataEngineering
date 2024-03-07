from collections import namedtuple

gcs_config = {
    "app_name": "PYSPARK_WITH_GCP_BUCKET",
    "gcs_jar": "https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop3-latest.jar",
    "service_account_json": "GCS_SERVICE_ACCOUNT_KEY.json",
    "bucket_name": "dataproc_practice_bucket",
    "input_file_name": "employee/employee.csv",
    "output_dir_name": "employee_output"
}
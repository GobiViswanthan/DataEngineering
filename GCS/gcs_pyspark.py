from pyspark.sql import SparkSession
from pyspark.sql.functions import split
from config import gcs_config


spark = SparkSession.builder \
    .appName(gcs_config["app_name"]) \
    .config("spark.jars", gcs_config["gcs_jar"]) \
    .config("spark.sql.repl.eagerEval.enabled", True) \
    .getOrCreate()

# Set GCS credentials if necessary
spark._jsc.hadoopConfiguration().set("google.cloud.auth.service.account.json.keyfile", gcs_config["service_account_json"])

# transformations configurations
split_column, split_by, new_columns = "name", " ", ["first_name", "last_name"]

# Read CSV file from GCS into DataFrame
df = spark.read.csv(f"gs://{gcs_config['bucket_name']}/{gcs_config['input_file_name']}", header=True, inferSchema=True)

# Split the name column into first name and last name
split_columns = [
    split(df[split_column], split_by, len(new_columns)).getItem(i).alias(new_columns[i])
    for i in range(len(new_columns))
]
df = df.select("*", *split_columns)

# Coalesce the DataFrame to a single partition
df = df.coalesce(1)

# Write the DataFrame to a single CSV file in GCS
df.write.csv(f"gs://{gcs_config['bucket_name']}/{gcs_config['output_dir_name']}/", header=True)

# Stop SparkSession
spark.stop()

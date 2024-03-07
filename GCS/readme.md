# PySpark Script for GCS Integration

This script demonstrates how to use PySpark to read data from Google Cloud Storage (GCS), perform transformations, and write the processed data back to GCS. It includes configurations for accessing GCS and splitting a CSV file's column into multiple columns.

## Requirements

- Python 3
- Apache Spark
- PySpark
- GCS service account key JSON file
- Access to a GCS bucket to the service account

## Installation

1. Clone this repository:

    ```bash
    git clone <repository_url>
    ```

2. Install the required dependencies:

    ```bash
    pip install pyspark
    ```

## Usage

1. Ensure you have a GCS service account key JSON file (`GCS_SERVICE_ACCOUNT_KEY.json`) with appropriate permissions to access the GCS bucket (`STORAGE ACCESS ADMIN`) specified in the configuration.

2. Update the `config.py` file with your GCS configurations:

    ```python
    gcs_config = {
        "app_name": "YOUR_PREFERRED_APP_NAME",
        "gcs_jar": "https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop3-latest.jar",
        "service_account_json": "GCS_SERVICE_ACCOUNT_KEY.json",
        "bucket_name": "GCS_BUCKET_NAME",
        "input_file_name": "FILE_PATH_IN_THE_BUCKET",
        "output_dir_name": "OUTPUT_DIR_NAME_IN_THE_BUCKET"
    }
    ```

3. Run the `gcs_pyspark.py` script:

    ```bash
    python gcs_pyspark.py
    ```

## Script Overview

- The script reads a CSV file from the specified GCS bucket and splits the `name` column into `first_name` and `last_name`.
- It then coalesces the DataFrame into a single partition for efficient writing.
- Finally, it writes the processed DataFrame back to GCS in CSV format.

## Configuration Details

- `app_name`: The name of the Spark application.
- `gcs_jar`: The URL to the GCS connector JAR file.
- `service_account_json`: The path to the GCS service account key JSON file.
- `bucket_name`: The name of the GCS bucket where the input and output files are located.
- `input_file_name`: The path to the input CSV file within the GCS bucket.
- `output_dir_name`: The directory within the GCS bucket where the output CSV file will be stored.

## License

This project is licensed under the [MIT License](LICENSE).

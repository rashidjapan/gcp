# GCP Data Pipeline

This directory contains a sample data pipeline structure for deployment to Google Cloud Platform.

## Structure

- `.github/workflows/`: CI/CD configurations
- `scripts/`: Source code for ETL jobs
- `data/`: Sample data files
- `requirements.txt`: Python dependencies

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the ETL job:
   ```bash
   python scripts/etl_job.py
   ```

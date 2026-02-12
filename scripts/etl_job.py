import pandas as pd
import os

def run_etl():
    print("Starting ETL job...")
    
    # Define paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'sample_weather.csv')
    
    if os.path.exists(data_path):
        print(f"Reading data from {data_path}")
        df = pd.read_csv(data_path)
        print("Data sample:")
        print(df.head())
        print("ETL job completed successfully.")
    else:
        print(f"Error: Data file not found at {data_path}")

if __name__ == "__main__":
    run_etl()

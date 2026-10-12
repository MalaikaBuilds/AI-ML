import pandas as pd
import sqlite3
def extract_data():
    print("\n[EXTRACT] Reading data from GitHub...")
    url = "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv"
    df = pd.read_csv(url)
    print(f"Rows extracted: {df.shape[0]}")
    print(f"Columns extracted: {df.shape[1]}")
    return df
def transform_data(df):
    print("\n[TRANSFORM] Creating a copy of the dataset...")
    transformed_df = df.copy()
    return transformed_df
def load_data(df):
    print("\n[LOAD] Loading data into SQLite database...")
    database_name = "energy_data.db"
    table_name = "energy_data"
    with sqlite3.connect(database_name) as connection:
        df.to_sql(
            table_name,
            connection,
            if_exists="replace",
            index=False
        )
    print(f"Rows loaded: {df.shape[0]}")
    print(f"Database created: {database_name}")
    print(f"Table created: {table_name}")
def run_etl():
    try:
        extracted_df = extract_data()
        transformed_df = transform_data(extracted_df)
        load_data(transformed_df)
        print("\nETL completed successfully!")
    except Exception as error:
        print(f"\nETL Pipeline Failed: {error}")
if __name__ == "__main__":
    run_etl()
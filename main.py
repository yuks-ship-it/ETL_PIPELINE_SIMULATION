from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

RAW_DATA_PATH = "data/raw/students_raw.csv"

def run_etl():
    df = extract_data(RAW_DATA_PATH)
    clean_df = transform_data(df)
    load_data(clean_df)

if __name__ == "__main__":
    run_etl()

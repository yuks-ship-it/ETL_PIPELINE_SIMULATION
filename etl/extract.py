import pandas as pd

def extract_data(file_path):
    print("Extracting data from CSV...")
    return pd.read_csv(file_path)

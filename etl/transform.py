import pandas as pd

def transform_data(df):
    print("Transforming data...")

    # Convert age column to numeric safely
    df["age"] = pd.to_numeric(df["age"], errors="coerce")

    # Fill missing ages with mean
    age_mean = int(df["age"].mean())
    df["age"] = df["age"].fillna(age_mean)

    # Fill missing emails
    df["email"] = df["email"].fillna("not_provided@student.com")

    # Standardize department
    df["department"] = df["department"].str.upper()

    return df

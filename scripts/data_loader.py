import pandas as pd

def load_raw_data(file_path='data/raw_data.csv'):

    return pd.read_csv(file_path)

def load_transformed_data(file_path='data/transformed_data.csv'):

    return pd.read_csv(file_path)


raw_data = load_raw_data()
transformed_data = load_transformed_data()

print("Raw Data:")
print(raw_data.head())

print("\nTransformed Data:")
print(transformed_data.head())

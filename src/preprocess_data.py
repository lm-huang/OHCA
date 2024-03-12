import numpy as np
import pandas as pd
import sqlite3
import os

path=['data/nemsis.db','data/processeddataCA']

missing_indicators = [
    'unknown', 'not recorded', '', '7701003', '7701001', '.', '-',
    'na', 'n/a', 'NA', 'null', 'none', 'undefined', 'missing', 'nan'
]
missing_indicators = [mi.lower() for mi in missing_indicators]  

def standardize_value(input_value):
    """
    Standardizes given input by checking against various formats of missing data.
    Returns None for missing data, and a cleaned, trimmed string otherwise.
    """
    if pd.isna(input_value):
        return None
    standardized_value = str(input_value).strip().lower()
    return None if standardized_value in missing_indicators else standardized_value

def preprocess_dataframe(dataframe: pd.DataFrame):
    """
    Applies data cleaning across all object type columns in a DataFrame.
    """
    for col in dataframe.columns:
        if dataframe[col].dtype == object:
            dataframe[col] = dataframe[col].apply(lambda x: standardize_value(x))
    return dataframe

def process_csv_files(directory: str):
    """
    Generator that processes each CSV file in a given directory,
    cleaning and yielding the filename and cleaned DataFrame.
    """
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            dataframe = pd.read_csv(file_path, low_memory=False)
            yield filename, preprocess_dataframe(dataframe)

def run():
    db_path = path[0]
    csv_folder = path[1]

    connection = sqlite3.connect(db_path)
    for filename, df in process_csv_files(csv_folder):
        table_name = os.path.splitext(filename)[0]
        df.to_sql(table_name, connection, if_exists="replace", index=False)
        print(f"Processed {filename} into SQLite table {table_name} at {db_path}")

    connection.close()

if __name__ == "__main__":
    run()

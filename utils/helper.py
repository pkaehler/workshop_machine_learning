import pandas as pd

def load_dataset(file_path, index_col=None, date_columns=None, delimiter=','):
    df = pd.read_csv(file_path, index_col=index_col, parse_dates=date_columns, sep=delimiter)
    return df

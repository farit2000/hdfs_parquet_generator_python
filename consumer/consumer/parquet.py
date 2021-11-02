import pandas as pd


def get_parquet_from_json(list_of_dict):
    df = pd.DataFrame(list_of_dict)
    return df.to_parquet()

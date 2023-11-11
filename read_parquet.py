import pandas as pd

df = pd.read_parquet('data/parquet/ethereum__transactions__13891880_to_13892879.parquet', engine='pyarrow')
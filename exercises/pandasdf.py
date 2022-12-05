import numpy as np
import pandas as pd

df = pd.read_csv(r"DATA_HANDLING.csv")
print(df)
# print('The head data\n')
# print(df.head(3))
# print('\n\n\nThe tail data\n')
# print(df.tail(3))

# numbersOnly = df.select_dtypes(include = ['int64', 'float64'])
# print(numbersOnly)

empty = df.loc[:, df.isna().any(axis = 0)]
print(empty)
print(df.dtypes)
# https://github.com/ranaroussi/yfinance
# https://pypi.org/project/yfinance/

import pandas as pd

# carico dataframe da file
df = pd.read_csv('datiapple_2024.csv')

# stampo a video il df da csv
print(df)

df = pd.read_excel('datiapple_2024.xlsx')

# stampo a video il df da xlsx
print(df)

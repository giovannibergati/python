# https://github.com/ranaroussi/yfinance
# https://pypi.org/project/yfinance/
# https://finance.yahoo.com/

import yfinance as yf

# definisco il ticker
ticker = "AAPL"

# definisco finestra temporale DA => A
startdate = "2024-01-01"
enddate = "2024-03-31"

# download dati azionari
df = yf.download(ticker,start=startdate,end=enddate)

# stampo a video
print(df)

# salvo il file in .csv
df.to_csv('datiapple_2024.csv')

# salvo il file in .xlsx
df.to_excel('datiapple_2024.xlsx')

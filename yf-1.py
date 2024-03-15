# https://github.com/ranaroussi/yfinance
# https://pypi.org/project/yfinance/

import yfinance as yf

aapl = yf.Ticker("AAPL")

hist = aapl.history(period="1d")
dividends = aapl.dividends
splits = aapl.splits

# stampo a video
print (hist)



import yfinance as yf
import pandas as pd

# Scaricare i dati storici per Apple (AAPL) e Google (GOOG)
aapl_df = yf.download('AAPL', start='2024-01-01', end='2024-12-31')
goog_df = yf.download('GOOG', start='2024-01-01', end='2024-12-31')

# Calcolare il rendimento giornaliero percentuale per AAPL e GOOG
aapl_df['daily_return'] = aapl_df['Close'].pct_change()
goog_df['daily_return'] = goog_df['Close'].pct_change()

# Creare un nuovo DataFrame combinando i rendimenti
combined_returns = pd.DataFrame({
    'AAPL': aapl_df['daily_return'],
    'GOOG': goog_df['daily_return']
})

# Calcolare il rendimento medio giornaliero del portafoglio
# Supponiamo che il portafoglio sia equamente ponderato
portfolio_return = combined_returns.mean(axis=1)

# Visualizzare i primi 5 rendimenti di portafoglio
print(portfolio_return.head(5))

import matplotlib.pyplot as plt

# Grafico dei rendimenti giornalieri di AAPL e GOOG
combined_returns.plot(title="Rendimenti Giornalieri di AAPL e GOOG nel 2024")
plt.show()

# Grafico del rendimento cumulativo del portafoglio nel 2020
(1 + portfolio_return).cumprod().plot(title="Rendimento Cumulativo del Portafoglio nel 2024")
plt.show()

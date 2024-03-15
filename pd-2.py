import pandas as pd

# Creazione di un DataFrame di esempio
data = {'date': ['2020-01-01', '2020-01-02', '2020-01-03', None],
        'close_price': [100, 101, None, 102],
        'volume': [200, None, 300, 300]}
df = pd.DataFrame(data)

# Visualizzazione del DataFrame originale
print("DataFrame Originale:")
print(df)

# Gestione dei valori mancanti
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='coerce')  # Conversione della colonna 'date' in formato datetime
df = df.dropna(subset=['date'])  # Rimozione delle righe dove 'date' è mancante
df['close_price'] = df['close_price'].fillna(df['close_price'].mean())  # Sostituzione dei valori mancanti in 'close_price' con la media
df['volume'] = df['volume'].fillna(0)  # Sostituzione dei valori mancanti in 'volume' con 0

# Visualizzazione del DataFrame dopo la pulizia
print("\nDataFrame Dopo la Pulizia:")
print(df)

import pandas as pd

# Creazione di un DataFrame di esempio
data = {
    'date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04'],
    'symbol': ['STOCK1', ' STOCK1', ' STOCK2', 'STOCK2'],
    'close_price': [430, 432, 2100, 2120],
    'volume': [100, 150, 120, 110]
}
df = pd.DataFrame(data)

# Filtraggio: Selezionare solo le righe di ''STOCK1'
filtered_df = df[df['symbol'] == 'STOCK1']

# Ordinamento: Ordinare i dati per 'close_price' in modo crescente
sorted_df = df.sort_values(by='close_price', ascending=True)

# Raggruppamento: Calcolare il volume medio per simbolo
grouped_df = df.groupby('symbol')['volume'].mean()

# Ristrutturazione: Pivot dei dati per avere i simboli come colonne e prezzi come valori
pivot_df = df.pivot(index='date', columns='symbol', values='close_price')

# Stampa dei risultati
print("DataFrame Filtrato (solo 'STOCK1'):")
print(filtered_df)
print("\nDataFrame Ordinato per Prezzo di Chiusura:")
print(sorted_df)
print("\nVolume Medio per Simbolo:")
print(grouped_df)
print("\nDataFrame Ristrutturato (Pivot):")
print(pivot_df)

import pandas as pd
import numpy as np


# 1. Generazione dei Dati con array, senza liste
np.random.seed(42)

dates = pd.date_range(start='2025-03-01', periods=30, freq='D')
cities = np.array(['Milano', 'Roma', 'Torino'])
products = np.array(['Prodotto A', 'Prodotto B', 'Prodotto C'])

n_dates = len(dates)
n_cities = len(cities)
n_products = len(products)
n_rows = n_dates * n_cities * n_products

date_col = np.repeat(dates.values, n_cities * n_products)
city_col = np.tile(np.repeat(cities, n_products), n_dates)
product_col = np.tile(products, n_dates * n_cities)
sales_col = np.random.randint(100, 500, size=n_rows)

df = pd.DataFrame({
    'Data': date_col,
    'Città': city_col,
    'Prodotto': product_col,
    'Vendite': sales_col
})

pivot_table = df.pivot_table(index='Città', columns='Prodotto', values='Vendite', aggfunc='mean')
groupby_total = df.groupby('Prodotto', as_index=False)['Vendite'].sum()

# 4. Menu per la scelta del formato di esportazione
print("In quale formato vuoi salvare il DataFrame?")
print("1 - CSV")
print("2 - JSON")
print("3 - Excel (XLSX)")


scelta = input("Inserisci il numero corrispondente alla tua scelta: ")

match scelta:
    case "1":
        df.to_csv("Analisi_Vendite.csv", index=False)
        print("File salvato come Analisi_Vendite.csv")
    case "2":
        df.to_json("Analisi_Vendite.json", orient='records', indent=2, date_format='iso')
        print("File salvato come Analisi_Vendite.json")
    case "3":
        df.to_excel("Analisi_Vendite.xlsx", index=False)
        print("File salvato come Analisi_Vendite.xlsx")
   
    case _:
        print("Scelta non valida. Nessun file è stato salvato.")

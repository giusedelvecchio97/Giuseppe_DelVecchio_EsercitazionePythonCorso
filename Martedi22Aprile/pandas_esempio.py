import pandas as pd





# Creiamo un semplice DataFrame con due colonne
df = pd.DataFrame({
    "Nome": ["Alice", "Bob", "Charlie"],
    "Vendite": [1200, 950, 1800]
})

# Salviamo il DataFrame in un file CSV
file_path = 'C:/Users/diego/Desktop/PythonCorso/Martedi22Aprile/vendite.csv'

df.to_csv(file_path, index=False)

file_path='vendite.csv'

dp=pd.read_csv(file_path)

print(dp.head())

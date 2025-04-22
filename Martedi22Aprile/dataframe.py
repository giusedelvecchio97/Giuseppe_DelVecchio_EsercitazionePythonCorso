import pandas as pd
import random
import numpy as np

# Liste di nomi e città
nomi = ['Anna', 'Luca', 'Marco', 'Giulia', 'Paolo', 'Sara', 'Elena', 'Michele', 'Giorgia', 'Francesco']
città = ['Roma', 'Milano', 'Torino', 'Napoli', 'Bologna']

# Generazione del dataset casuale
dati = []
for _ in range(30):
    nome = random.choice(nomi)
    età = random.choice([random.randint(10, 80), None])  # Aggiungiamo valori None
    città_ = random.choice(città)
    salario = random.choice([random.randint(1000, 5000), None])  # Anche qui valori None
    dati.append([nome, età, città_, salario])

# Aggiungiamo qualche riga duplicata
dati.append(dati[0])
dati.append(dati[1])

# Creiamo il DataFrame
df = pd.DataFrame(dati, columns=["Nome", "Età", "Città", "Salario"])

print("Prime 5 righe:")
print(df.head())

print("\nUltime 5 righe:")
print(df.tail())

print("\nDuplicati trovati:", df.duplicated().sum())

# Rimozione duplicati
df = df.drop_duplicates()


print("\nStatistiche descrittive:")
print(df.describe())

print("\nMediana Età:", df['Età'].median())
print("Mediana Salario:", df['Salario'].median())

print("\nDeviazione standard:")
print(df[['Età', 'Salario']].std())

mediana_eta = df['Età'].median()
mediana_salario = df['Salario'].median()

df['Età'] = df['Età'].fillna(mediana_eta)
df['Salario'] = df['Salario'].fillna(mediana_salario)







def categoria_eta(eta):
    if eta < 18:
        return "Giovane"
    elif eta <= 65:
        return "Adulto"
    else:
        return "Senior"

df['CategoriaEtà'] = df['Età'].apply(categoria_eta)

df.to_csv("dati_puliti.csv", index=False)
print("\nDataFrame pulito salvato in 'dati_puliti.csv'")
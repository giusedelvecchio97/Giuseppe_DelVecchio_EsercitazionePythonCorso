import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carica i dati dal file CSV
df = pd.read_csv('train.csv')  # Assicurati che 'train.csv' sia nella stessa cartella

# 2. Copia e pulizia del DataFrame
df_cleaned = df.copy()
df_cleaned = df_cleaned.drop('Cabin', axis=1)            # Rimuove la colonna Cabin (tanti valori nulli)
df_cleaned = df_cleaned.drop_duplicates()                # Elimina eventuali righe duplicate

# Riempie i valori NaN della colonna 'Age' con la media
media_eta = df_cleaned['Age'].mean()
df_cleaned['Age'] = df_cleaned['Age'].fillna(media_eta)

# (Facoltativo: stampa informazioni utili sul DataFrame)
print(df_cleaned.head())
print(df_cleaned.describe())
print(df_cleaned.info())

# 3. ANALISI: Sopravvivenza per classe passeggero (Pclass)

# Matplotlib – Grafico a barre classico
survival_by_pclass = df_cleaned.groupby('Pclass')['Survived'].value_counts().unstack()
survival_by_pclass.plot(kind='bar', stacked=False)
plt.title('Sopravvivenza per Classe Passeggero')
plt.xlabel('Classe Passeggero')
plt.ylabel('Numero di Passeggeri')
plt.xticks(rotation=0)
plt.legend(title='Sopravvissuto', labels=['No', 'Sì'])
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()

# Seaborn – Grafico con stile più moderno
sns.countplot(data=df_cleaned, x='Pclass', hue='Survived')
plt.title('Sopravvivenza per Classe Passeggero')
plt.xlabel('Classe Passeggero')
plt.ylabel('Numero di Passeggeri')
plt.xticks(ticks=[0, 1, 2], labels=['1st', '2nd', '3rd'])  # Personalizza le etichette
plt.legend(title='Sopravvissuto', labels=['No', 'Sì'])
plt.tight_layout()
plt.show()

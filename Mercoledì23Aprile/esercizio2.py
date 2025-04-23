import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score

# Creo un dataset di esempio che segue la struttura descritta nell'immagine
# (Poiché non abbiamo un CSV reale, lo simuliamo per l'esercizio)
df = pd.DataFrame({
    'ID_Cliente': range(1, 11),
    'Eta': [25, 40, 35, 23, np.nan, 45, 31, 22, 60, 29],
    'Durata_Abbonamento': [12, 24, 6, 18, 3, 48, 36, 12, 60, 5],
    'Tariffa_Mensile': [30.0, 50.0, 45.0, 35.0, 25.0, np.nan, 55.0, 30.0, 60.0, 40.0],
    'Dati_Consumati': [10, 20, 15, 12, 8, 25, 18, 10, 30, 16],
    'Servizio_Clienti_Contatti': [2, 5, 1, 0, 3, 6, 1, 2, 4, 3],
    'Churn': ['No', 'Si', 'No', 'No', 'Si', 'No', 'Si', 'No', 'No', 'Si']
})


df.to_csv("telecom_churn.csv", index=False)
# --- 1. Caricamento ed Esplorazione Iniziale ---

# Visualizza informazioni generali sul dataset
info_df = df.info()

# Statistiche descrittive
descrizione_df = df.describe()

# Valori unici per la colonna 'Churn'
churn_counts = df['Churn'].value_counts()

# Colonne con valori mancanti
valori_mancanti = df.isnull().sum()


df = pd.read_csv("telecom_churn.csv")  # Assumiamo che il file si chiami così

# Esplorazione iniziale
print(df.info())            # Struttura del dataset, tipi di dati e valori nulli
print(df.describe())        # Statistiche descrittive per colonne numeriche
print(df['Churn'].value_counts())  

print(df.isnull().sum())

# Imputazione dei valori mancanti (esempio semplice: riempiamo con media o moda)
df['Età'] = df['Età'].fillna(df['Età'].mean())
df['Tariffa_Mensile'] = df['Tariffa_Mensile'].fillna(df['Tariffa_Mensile'].mean())
df['Dati_Consumati'] = df['Dati_Consumati'].fillna(df['Dati_Consumati'].mean())

# Correzione valori non realistici
df = df[df['Età'] > 0]  # Esclude età negative
df = df[df['Tariffa_Mensile'] >= 0]

# Creazione colonna utile: costo per GB
df['Costo_per_GB'] = df['Tariffa_Mensile'] / df['Dati_Consumati']

# GroupBy per esplorare relazione con Churn
print(df.groupby('Churn')[['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Costo_per_GB']].mean())

# Correlazioni (solo numeriche)
print(df.corr(numeric_only=True))

# Creazione colonna utile: costo per GB
df['Costo_per_GB'] = df['Tariffa_Mensile'] / df['Dati_Consumati']

# GroupBy per esplorare relazione con Churn
print(df.groupby('Churn')[['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Costo_per_GB']].mean())

# Correlazioni (solo numeriche)
print(df.corr(numeric_only=True))


# Conversione Churn in numerico
df['Churn'] = df['Churn'].map({'No': 0, 'Sì': 1})

# Normalizzazione manuale (Min-Max Scaling)
for col in ['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Dati_Consumati', 'Servizio_Clienti_Contatti', 'Costo_per_GB']:
    df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())



# Selezione feature e target
X = df[['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Dati_Consumati', 'Servizio_Clienti_Contatti', 'Costo_per_GB']]
y = df['Churn']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Regressione logistica
model = LogisticRegression()
model.fit(X_train, y_train)

# Predizioni
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# Valutazione
print("Accuratezza:", accuracy_score(y_test, y_pred))
print("AUC:", roc_auc_score(y_test, y_prob))

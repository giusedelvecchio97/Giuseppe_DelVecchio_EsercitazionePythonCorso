import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np

# 1. Carica il dataset
try:
    df = pd.read_csv("train.csv")
except FileNotFoundError:
    print("Errore: Il file 'train.csv' non è stato trovato.")
    exit()

# Verifica le colonne del DataFrame
print("Colonne del DataFrame iniziale:")
print(df.columns)

# 2. Feature Engineering: Estrazione del titolo dal nome
if 'Name' in df.columns:
    df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
    print("\nTitoli estratti:")
    print(df['Title'].value_counts())
else:
    print("La colonna 'Name' non esiste nel DataFrame.")

# 3. Pulizia e Imputazione dei dati mancanti
df = df.drop(['Cabin', 'Ticket', 'PassengerId', 'Name'], axis=1, errors='ignore')  # Rimuove colonne non utili e 'Name' dopo l'estrazione
df['Age'].fillna(df['Age'].median(), inplace=True)  # Riempie i valori mancanti per 'Age' con la mediana
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)  # Riempie i valori mancanti per 'Embarked' con la moda

print("\nInformazioni sul DataFrame dopo la pulizia e l'imputazione:")
df.info()

# 4. Raggruppamento di titoli rari
rare_titles = df['Title'].value_counts()[df['Title'].value_counts() < 10].index
df['Title'] = df['Title'].replace(rare_titles, 'Rare')
print("\nTitoli dopo il raggruppamento di quelli rari:")
print(df['Title'].value_counts())

# 5. Label Encoding per variabili categoriche
label_encoders = {}
for col in ['Sex', 'Embarked', 'Title']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le
print("\nDataFrame dopo Label Encoding:")
print(df.head())

# 6. Rilevamento e visualizzazione degli outlier per ogni attributo
print("\nRilevamento e visualizzazione degli outlier per ogni attributo:")
plt.figure(figsize=(18, 12))
for i, column in enumerate(df.columns):
    plt.subplot(3, 3, i + 1)
    sns.boxplot(y=df[column])
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)][column]
    print(f"\nOutlier in '{column}': {len(outliers)} ({len(outliers) / len(df):.2%})")
    plt.title(f'Boxplot di {column} (Outlier: {len(outliers)})')
plt.tight_layout()
plt.show()

# 7. Rimozione degli outlier (opzionale - decommenta per eseguire)
# print("\nRimozione degli outlier dal DataFrame:")
# df_no_outliers = df.copy()
# for column in df.columns:
#     Q1 = df_no_outliers[column].quantile(0.25)
#     Q3 = df_no_outliers[column].quantile(0.75)
#     IQR = Q3 - Q1
#     lower_bound = Q1 - 1.5 * IQR
#     upper_bound = Q3 + 1.5 * IQR
#     df_no_outliers = df_no_outliers[(df_no_outliers[column] >= lower_bound) & (df_no_outliers[column] <= upper_bound)]
#
# print(f"Shape del DataFrame originale: {df.shape}")
# print(f"Shape del DataFrame senza outlier (rimozione conservativa): {df_no_outliers.shape}")
# df = df_no_outliers # Aggiorna il DataFrame principale con quello senza outlier

# 8. Preparazione dei dati per il modello
X = df.drop('Survived', axis=1)  # Elimina la colonna 'Survived' per ottenere le features
y = df['Survived']  # La variabile target è 'Survived'
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print("\nShape dei set di training e test:")
print(f"X_train: {X_train.shape}, y_train: {y_train.shape}")
print(f"X_test: {X_test.shape}, y_test: {y_test.shape}")

# 9. Addestramento del modello di regressione logistica (per confronto)
logreg_model = LogisticRegression(max_iter=300, solver='liblinear')
logreg_model.fit(X_train, y_train)
y_pred_logreg = logreg_model.predict(X_test)
accuracy_logreg = accuracy_score(y_test, y_pred_logreg)
print(f"\nAccuratezza con Regressione Logistica: {accuracy_logreg:.2f}")

# 10. Analisi della multicollinearità (come nel codice precedente)
correlation_matrix = X.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matrice di Correlazione tra le Features')
plt.show()

print("\nAnalisi della Multicollinearità (basata sulla matrice di correlazione):")
for i in range(len(correlation_matrix.columns)):
    for j in range(i):
        if abs(correlation_matrix.iloc[i, j]) > 0.7:  # Soglia arbitraria di 0.7
            colname1 = correlation_matrix.columns[i]
            colname2 = correlation_matrix.columns[j]
            print(f"Potenziale multicollinearità tra: {colname1} e {colname2} (Correlazione: {correlation_matrix.iloc[i, j]:.2f})")
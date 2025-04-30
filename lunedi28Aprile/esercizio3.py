# Importazioni necessarie
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# 1. Carica il dataset Wine
data = load_wine()
X = data.data  # Le caratteristiche (features)
y = data.target  # Le etichette (target)

# 2. Esplora il dataset
df = pd.DataFrame(X, columns=data.feature_names)

# Statistiche descrittive
print("Statistiche descrittive delle caratteristiche:\n")
print(df.describe())

# Numero di campioni per ciascuna classe
print(f"\nDistribuzione delle classi:\n{pd.Series(y).value_counts()}")

# 3. Visualizzazione della distribuzione delle classi
plt.figure(figsize=(8, 6))
plt.bar(range(3), pd.Series(y).value_counts(), tick_label=data.target_names)
plt.xlabel('Classe')
plt.ylabel('Numero di campioni')
plt.title('Distribuzione delle classi nel dataset Wine')
plt.show()

# 4. Riduzione della dimensionalità con PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Visualizzazione dei dati trasformati
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', edgecolor='k', s=100)
plt.xlabel('Componente principale 1')
plt.ylabel('Componente principale 2')
plt.title('PCA: Proiezione del dataset Wine')
plt.colorbar(label='Classe')
plt.show()

# 5. Suddividi i dati in training e test set (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Applica un algoritmo di classificazione: RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 7. Valuta la performance del modello
y_pred = model.predict(X_test)

# Calcola le metriche di valutazione
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print(f"\nValutazione del modello:\n")
print(f"Accuratezza: {accuracy}")
print(f"Precisione: {precision}")
print(f"Recall: {recall}")
print(f"F1-score: {f1}")

# 8. Visualizza l'importanza delle feature
feature_importances = model.feature_importances_
plt.figure(figsize=(10, 6))
plt.barh(data.feature_names, feature_importances)
plt.xlabel('Importanza della Feature')
plt.title('Importanza delle Feature nel RandomForestClassifier')
plt.show()

# 9. Visualizza la matrice di confusione
cm = confusion_matrix(y_test, y_pred)

# Visualizza la matrice di confusione come heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=data.target_names, yticklabels=data.target_names)
plt.xlabel('Predizione')
plt.ylabel('Reale')
plt.title('Matrice di Confusione')
plt.show()

# 10. Ottimizzazione del modello con GridSearchCV
param_grid = {
    'n_estimators': [50, 100, 200],  # Numero di alberi nella foresta
    'max_depth': [None, 10, 20],      # Profondità massima degli alberi
}

grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5)

# Esegui il fitting con GridSearchCV
grid_search.fit(X_train, y_train)

# Stampa i migliori parametri trovati da GridSearchCV
print(f"\nMigliori parametri trovati tramite GridSearchCV: {grid_search.best_params_}")

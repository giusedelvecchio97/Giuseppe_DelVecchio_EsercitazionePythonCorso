# 1. Importa le librerie necessarie
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV

# 2. Carica il dataset Wine
data = load_wine()
X = data.data  # Le caratteristiche
y = data.target  # Le etichette (target)

# 3. Suddividi il dataset in training e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Definisci la griglia dei parametri da esplorare
param_grid = {
    'max_depth': [3, 5, 7],          # Tre possibili profondità da provare
    'criterion': ['gini', 'entropy'] # Due criteri diversi di divisione
}

# 5. Crea un oggetto GridSearchCV
grid_search = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=5)

# 6. Esegui il fitting del GridSearch sui dati di training
grid_search.fit(X_train, y_train)

# 7. Stampa i migliori parametri trovati
print(f"Migliori parametri: {grid_search.best_params_}")


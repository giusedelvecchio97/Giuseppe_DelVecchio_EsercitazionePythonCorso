# 1. Importazione librerie necessarie
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV

# 2. Carica il dataset Wine
# Dataset supervisionato: X = feature chimiche, y = classe del vino
wine = load_wine()
X = wine.data
y = wine.target

df = pd.DataFrame(wine.data, columns=wine.feature_names)
df['target'] = wine.target
df.info()
print(df.head())

# 3. Standardizza le caratteristiche
# Portiamo ogni feature ad avere media 0 e deviazione standard 1
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Suddividi i dati in training e test set (70% - 30%)
# Separiamo per evitare overfitting e testare la generalizzazione
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)

# 5. Applica un algoritmo di classificazione (DecisionTreeClassifier)
# Decision tree costruisce regole di decisione basate sui dati
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 6. Predici i dati di test
y_pred = model.predict(X_test)

# 7. Valuta la performance del modello
# Stampiamo Precision, Recall, F1-Score: metriche fondamentali per la classificazione
print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred, target_names=wine.target_names))

# 8. Visualizza la matrice di confusione
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=wine.target_names,
            yticklabels=wine.target_names)
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix - Wine Dataset')
plt.show()

# 9. (Extra) Visualizza l'albero decisionale
# Utile per interpretare come il modello ha costruito la classificazione
plt.figure(figsize=(20,10))
plot_tree(model, filled=True, feature_names=wine.feature_names,
          class_names=wine.target_names, rounded=True)
plt.title('Decision Tree Visualization - Wine Dataset')
plt.show()





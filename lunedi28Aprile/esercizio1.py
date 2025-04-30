# 1. Importare le librerie necessarie
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


# 2. Caricare il dataset Iris
iris = load_iris()
X = iris.data  # Features: lunghezza/larghezza di sepali e petali
y = iris.target  # Target: specie di Iris

# 3. Standardizzare le caratteristiche utilizzando StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Suddividere i dati in training (70%) e test (30%)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# 5. Applicare l'algoritmo DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 6. Predire i dati di test
y_pred = model.predict(X_test)

# 7. Valutare la performance del modello
print("Classification Report:")
print(classification_report(y_test, y_pred))

# 8. Visualizzare la matrice di confusione
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

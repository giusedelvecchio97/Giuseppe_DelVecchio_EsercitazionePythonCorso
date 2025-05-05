import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Generiamo un dataset di esempio con parametri corretti
X, y = make_classification(n_samples=100, n_features=2,
                           n_informative=2, n_redundant=0,
                           n_repeated=0, n_classes=2, random_state=42)

# Dividiamo in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creiamo il modello Decision Tree
dt_gini_synthetic = DecisionTreeClassifier(max_depth=3, criterion="gini", random_state=42)
dt_gini_synthetic.fit(X_train, y_train)

# Facciamo previsioni sul set di test
y_pred_gini_synthetic = dt_gini_synthetic.predict(X_test)

# Valutiamo le prestazioni sul dataset sintetico
print("Decision Tree (Gini) Accuracy (Synthetic Data):", accuracy_score(y_test, y_pred_gini_synthetic))
print("\nDecision Tree (Gini) Classification Report (Synthetic Data):\n", classification_report(y_test, y_pred_gini_synthetic, target_names=["Classe 0", "Classe 1"]))

# Matrice di confusione per il dataset sintetico
cm_gini_synthetic = confusion_matrix(y_test, y_pred_gini_synthetic)
sns.heatmap(cm_gini_synthetic, annot=True, cmap='Blues', xticklabels=["Classe 0", "Classe 1"], yticklabels=["Classe 0", "Classe 1"])
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Decision Tree (Gini) Confusion Matrix (Synthetic Data)')
plt.show()

# Visualizziamo l'albero decisionale per il dataset sintetico
plt.figure(figsize=(12, 6))
plot_tree(dt_gini_synthetic, feature_names=["Feature 1", "Feature 2"], class_names=["Classe 0", "Classe 1"], filled=True)
plt.title("Decision Tree Classifier (Gini Impurity) - Synthetic Data")
plt.show()

# Visualizzazione dei dati sintetici e della superficie di decisione (opzionale, ma utile)
plt.figure(figsize=(10, 8))
h = .02  # step size nel meshgrid
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
Z = dt_gini_synthetic.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.RdBu, alpha=0.8)

# Plot dei punti di training e test
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=plt.cm.RdBu, label='Training data')
plt.scatter(X_test[:, 0], X_test[:, 1], marker='x', c=y_test, cmap=plt.cm.RdBu, label='Test data')

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Decision Surface of Decision Tree (Gini) - Synthetic Data')
plt.legend()
plt.show()





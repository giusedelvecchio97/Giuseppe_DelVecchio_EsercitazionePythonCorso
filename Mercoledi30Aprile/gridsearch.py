import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Generiamo il dataset di esempio
X, y = make_classification(n_samples=100, n_features=2,
                           n_informative=2, n_redundant=0,
                           n_repeated=0, n_classes=2, random_state=42)

# Dividiamo in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Definiamo la griglia di iperparametri da esplorare
param_grid = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [None, 2, 3, 4, 5],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 3, 5]
}

# Creiamo un'istanza di DecisionTreeClassifier
tree = DecisionTreeClassifier(random_state=42)

# Eseguiamo la Grid Search con cross-validation (cv=5)
grid_search = GridSearchCV(tree, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Visualizziamo i migliori iperparametri trovati
print("Migliori iperparametri trovati:", grid_search.best_params_)

# Otteniamo il miglior modello trovato dalla Grid Search
best_tree = grid_search.best_estimator_

# Valutiamo il miglior modello sul set di test
y_pred_best = best_tree.predict(X_test)
print("Accuracy del miglior modello sul set di test:", accuracy_score(y_test, y_pred_best))
print("\nClassification Report del miglior modello sul set di test:\n", classification_report(y_test, y_pred_best, target_names=["Classe 0", "Classe 1"]))

# Matrice di confusione per il miglior modello
cm_best = confusion_matrix(y_test, y_pred_best)
sns.heatmap(cm_best, annot=True, cmap='Greens', xticklabels=["Classe 0", "Classe 1"], yticklabels=["Classe 0", "Classe 1"])
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix del Miglior Modello (Grid Search)')
plt.show()

# Visualizziamo l'albero decisionale del miglior modello
plt.figure(figsize=(12, 6))
plot_tree(best_tree, feature_names=["Feature 1", "Feature 2"], class_names=["Classe 0", "Classe 1"], filled=True)
plt.title("Albero Decisionale del Miglior Modello (Grid Search)")
plt.show()

# Visualizzazione della superficie di decisione del miglior modello (opzionale)
plt.figure(figsize=(10, 8))
h = .02
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
Z = best_tree.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.RdBu, alpha=0.8)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=plt.cm.RdBu, label='Training data')
plt.scatter(X_test[:, 0], X_test[:, 1], marker='x', c=y_test, cmap=plt.cm.RdBu, label='Test data')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Decision Surface del Miglior Modello (Grid Search)')
plt.legend()
plt.show()
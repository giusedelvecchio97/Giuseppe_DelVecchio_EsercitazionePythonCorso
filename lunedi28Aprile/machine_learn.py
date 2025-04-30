from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Caricamento del dataset
data = load_iris()
X = data.data # le caratteristiche
y = data.target # le etichette

# Divisione dei dati in set di addestramento e di test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creazione del modello di classificazione
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Addestramento del modello
model.fit(X_train, y_train)

# Predizione delle etichette per il set di test
predictions = model.predict(X_test)

# Calcolo dell'accuratezza del modello
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy:.2f}')




# Importare le librerie necessarie
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Caricare il dataset Iris
iris = load_iris()
X = iris.data # Caratteristiche (lunghezza e larghezza di sepali e petali)
y = iris.target # Etichette (specie di Iris)

# Suddividere il dataset in set di training e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definire il modello: K-Nearest Neighbors Classifier
model = KNeighborsClassifier(n_neighbors=3)

# Addestrare il modello sui dati di training
model.fit(X_train, y_train)

# Fare predizioni sui dati di test
y_pred = model.predict(X_test)

# Valutare le prestazioni del modello
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza del modello: {accuracy:.2f}")



#stesso uso ma con due for

import random
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Caricare il dataset Iris
iris = load_iris()
X = iris.data
y = iris.target

# For esterno: ripetiamo 5 volte con diverse randomizzazioni
for external_iteration in range(5):
    # Genera un random_state casuale tra 0 e 1000
    random_state_value = random.randint(0, 1000)

    # Dividere i dati usando questo random_state
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=random_state_value
    )

    print(f"\n🌟 Iterazione esterna {external_iteration + 1}")
    print(f"Random_state usato: {random_state_value}")

    # For interno: proviamo diversi valori di n_neighbors
    for n_neighbors in range(1, 6):  # provo K da 1 a 5
        # Definire il modello con n_neighbors variabile
        model = KNeighborsClassifier(n_neighbors=n_neighbors)

        # Addestrare e testare
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        # Stampare i risultati
        print(f"  ➡️ n_neighbors={n_neighbors}, Accuratezza={accuracy:.4f}")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# 1. Carica il dataset
df = pd.read_csv("train.csv")

# 2. Pulizia dati
df = df.drop(['Cabin', 'Ticket', 'Name', 'PassengerId'], axis=1)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# 3. Estrai 'Title' dal nome
df['Title'] = pd.read_csv("train.csv")['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)

# 4. Label encoding per variabili categoriche
label_encoders = {}
for col in ['Sex', 'Embarked', 'Title']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le  # salviamo per eventuali inverse_transform

# Mostriamo le etichette codificate
print("Etichette codificate per 'Sex':", label_encoders['Sex'].classes_)
print("Etichette codificate per 'Embarked':", label_encoders['Embarked'].classes_)
print("Etichette codificate per 'Title':", label_encoders['Title'].classes_)

# 5. Visualizza correlazione tra variabili e 'Survived'
sns.countplot(data=df, x='Sex', hue='Survived')
plt.title('Sopravvivenza per Sesso (dopo codifica LabelEncoder)')
plt.xlabel('Sesso (0=Donna, 1=Uomo)')
plt.ylabel('Numero Passeggeri')
plt.legend(title='Sopravvissuto')
plt.show()

sns.countplot(data=df, x='Embarked', hue='Survived')
plt.title('Sopravvivenza per porto di imbarco')
plt.show()

sns.countplot(data=df, x='Title', hue='Survived')
plt.title('Sopravvivenza per titolo')
plt.show()

# 6. Prepara dati per modello
X = df.drop('Survived', axis=1)
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. Allena modello Random Forest
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 8. Valuta accuratezza
print(f"Accuratezza con LabelEncoder: {accuracy_score(y_test, y_pred):.2f}")

# 9. Importanza delle feature
importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
plt.figure(figsize=(8, 5))
importances.plot(kind='bar')
plt.title('Importanza delle variabili (LabelEncoded)')
plt.tight_layout()
plt.show()

# 10. Confusion Matrix per analizzare la performance del modello
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Non sopravvissuto', 'Sopravvissuto'])
disp.plot(cmap=plt.cm.Blues)
plt.title('Matrice di Confusione')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Caricamento dati

df = pd.read_csv('kc_house_data.csv')

print(df.head())
print(df.info())
print(df.describe())

# Rimozione duplicati
df_cleaned = df.drop_duplicates()

# Feature e target
X = df_cleaned.drop(['price', 'id', 'zipcode', 'date'], axis=1)
y = df_cleaned['price']

# Matrice di correlazione iniziale
plt.figure(figsize=(8, 6))
correlation_matrix = df_cleaned.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Matrice di correlazione delle colonne numeriche')
plt.show()

# Calcolo VIF con standardizzazione per stabilità
def calculate_vif(df):
    numeric_df = df.select_dtypes(include=np.number)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(numeric_df)
    vif_data = pd.DataFrame()
    vif_data["Feature"] = numeric_df.columns
    vif_data["VIF"] = [variance_inflation_factor(X_scaled, i) for i in range(X_scaled.shape[1])]
    return vif_data.sort_values(by='VIF', ascending=False)

# Rimozione multicollinearità
columns_to_drop = ['price', 'id', 'zipcode', 'date']
df_vif = df_cleaned.drop(columns=columns_to_drop)

# Rimozione manuale iniziale (basata su VIF noti alti)
columns_to_remove = ['sqft_above', 'grade', 'bathrooms']
for col_to_remove in columns_to_remove:
    if col_to_remove in df_vif.columns:
        print(f"\nEliminando la colonna: {col_to_remove}")
        df_vif_temp = df_vif.drop(columns=[col_to_remove])
        vif_result = calculate_vif(df_vif_temp)
        print("VIF dopo la rimozione:")
        print(vif_result.head())
        df_vif = df_vif_temp

# Rimozione iterativa di VIF > 10
while True:
    vif_result = calculate_vif(df_vif)
    highest_vif_feature = vif_result.iloc[0]
    if highest_vif_feature['VIF'] < 10:
        break
    column_to_remove = highest_vif_feature['Feature']
    print(f"\nEliminando la colonna con VIF più alto: {column_to_remove} (VIF = {highest_vif_feature['VIF']:.2f})")
    df_vif = df_vif.drop(columns=[column_to_remove])
    print("VIF dopo la rimozione:")
    print(calculate_vif(df_vif).head())

# Visualizzazione finale della correlazione
print("\nDataFrame finale (df_vif) dopo la gestione della multicollinearità:")
print(df_vif.head())

plt.figure(figsize=(8, 6))
sns.heatmap(df_vif.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Matrice di correlazione dopo l'utilizzo di VIF")
plt.show()

# Reintegro sicuro della variabile target
df_vif['price'] = y.values

# Split train/test
X = df_vif.drop('price', axis=1)
y = df_vif['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=69)

# Standardizzazione
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Regressione Lineare
linear_regression = LinearRegression()
linear_regression.fit(X_train_scaled, y_train)
y_pred_linear = linear_regression.predict(X_test_scaled)
r2_linear = r2_score(y_test, y_pred_linear)

# Ridge
ridge = Ridge(alpha=1.0)
ridge.fit(X_train_scaled, y_train)
y_pred_ridge = ridge.predict(X_test_scaled)
r2_ridge = r2_score(y_test, y_pred_ridge)

# Lasso
lasso = Lasso(alpha=0.1)
lasso.fit(X_train_scaled, y_train)
y_pred_lasso = lasso.predict(X_test_scaled)
r2_lasso = r2_score(y_test, y_pred_lasso)

# Risultati
results = {
    "R^2 Regressione Lineare": r2_linear,
    "R^2 Ridge": r2_ridge,
    "R^2 Lasso": r2_lasso,
}
print("\nRisultati dei modelli:")
print(results)

# ================================
# (Opzionale) Confronto con RFE
# ================================
# model_rfe = LinearRegression()
# selector = RFE(model_rfe, n_features_to_select=10)
# selector = selector.fit(X_train_scaled, y_train)
# selected_features = X.columns[selector.support_]
# print("\nTop 10 feature selezionate da RFE:")
# print(selected_features)

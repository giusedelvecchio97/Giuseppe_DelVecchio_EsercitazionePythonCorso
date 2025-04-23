import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Genera 30 temperature casuali tra 10 e 35 gradi
np.random.seed(0)
temperatures = np.random.rand(30)  # genera float tra 0 e 1
df = pd.DataFrame({'Temperatura': temperatures})


# Calcolo delle statistiche
temp_max = df['Temperatura'].max()
temp_min = df['Temperatura'].min()
temp_mean = df['Temperatura'].mean()
temp_median = df['Temperatura'].median()

# ---------------------------
# 1. Grafico della temperatura massima
# ---------------------------
plt.figure(figsize=(10, 4))
plt.plot(df['Temperatura'], marker='o', color='gray', label='Temp. Giornaliera')
plt.axhline(temp_max, color='red', linestyle='--')
plt.title('Temperatura Massima')
plt.xlabel('Giorno del Mese')
plt.ylabel('Temperatura (°C)')
plt.show()

# ---------------------------
# 2. Grafico della temperatura minima
# ---------------------------
plt.figure(figsize=(10, 4))
plt.plot(df['Temperatura'], marker='o', color='gray', label='Temp. Giornaliera')
plt.axhline(temp_min, color='blue', linestyle='--')
plt.title('Temperatura Minima')
plt.xlabel('Giorno del Mese')
plt.ylabel('Temperatura (°C)')
plt.show()

# ---------------------------
# 3. Grafico della temperatura media
# ---------------------------
plt.figure(figsize=(10, 4))
plt.plot(df['Temperatura'], marker='o', color='gray', label='Temp. Giornaliera')
plt.axhline(temp_mean, color='green', linestyle='--')
plt.title('Temperatura Media')
plt.xlabel('Giorno del Mese')
plt.ylabel('Temperatura (°C)')
plt.show()

# ---------------------------
# 4. Grafico della mediana delle temperature
# ---------------------------
plt.figure(figsize=(10, 4))
plt.plot(df['Temperatura'], marker='o', color='gray', label='Temp. Giornaliera')
plt.axhline(temp_median, color='purple', linestyle='--')
plt.title('Mediana della Temperatura')
plt.xlabel('Giorno del Mese')
plt.ylabel('Temperatura (°C)')
plt.show()

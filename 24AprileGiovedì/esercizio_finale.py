import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. GENERAZIONE DEI DATI
# Creiamo un intervallo di date per un anno intero (365 giorni) a partire dal 1 gennaio 2023
date_range = pd.date_range(start="2023-01-01", periods=365, freq="D")

# Impostiamo il seme del generatore di numeri casuali per rendere i risultati ripetibili
np.random.seed(42)

# Generiamo i visitatori con media 2000 e deviazione standard 500
base_visitors = np.random.normal(loc=2000, scale=500, size=365)

# Creiamo un trend lineare crescente da 0 a 500 lungo l'anno (per simulare l'aumento della popolarità)
increment = np.linspace(0, 500, 365)

# Sommiamo il trend ai dati base per ottenere la serie finale
visitatori = base_visitors + increment

# 2. CREAZIONE DEL DATAFRAME
# Creiamo un DataFrame con le date come indice e i visitatori come colonna
df = pd.DataFrame({
    'Visitatori': visitatori
}, index=date_range)

# 3. ANALISI DEI DATI
# Raggruppiamo per mese e calcoliamo media e deviazione standard
monthly_stats = df.resample('M').agg(['mean', 'std'])

# 4. VISUALIZZAZIONE

# Primo grafico: andamento giornaliero e media settimanale a blocchi (ogni 7 giorni)
plt.figure(figsize=(14, 6))  # Imposta la dimensione della figura

# Grafico della serie originale giornaliera (linea leggera)
plt.plot(df.index, df['Visitatori'], label='Visitatori giornalieri', alpha=0.5)

# Calcolo della media settimanale ogni 7 giorni, senza sovrapposizione
media_settimanale = df['Visitatori'].resample('7D').mean()

# Visualizziamo la media settimanale con uno scatter (pallini verdi)
plt.scatter(media_settimanale.index, media_settimanale, 
            label='Media settimanale (ogni 7 giorni)', 
            color='green', s=60, marker='o', edgecolor='black')

# Titoli e decorazioni
plt.title('Numero di Visitatori Giornalieri con Media Settimanale (Scatter)')
plt.xlabel('Data')
plt.ylabel('Numero di Visitatori')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# Secondo grafico: media mensile dei visitatori
plt.figure(figsize=(10, 5))

# Prendiamo solo la media dal DataFrame delle statistiche mensili
monthly_stats['Visitatori', 'mean'].plot(kind='bar', color='skyblue')

plt.title('Media Mensile dei Visitatori')
plt.xlabel('Mese')
plt.ylabel('Numero Medio di Visitatori')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

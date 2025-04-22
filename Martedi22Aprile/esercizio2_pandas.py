import pandas as pd
import numpy as np

# ----------------------------
# CREAZIONE DEL DATAFRAME
# ----------------------------
np.random.seed(0)
prodotti = ['ProdottoA', 'ProdottoB', 'ProdottoC']
città = ['Milano', 'Roma', 'Torino']

df = pd.DataFrame({
    'Prodotto': np.random.choice(prodotti, 20),
    'Quantità': np.random.randint(1, 20, 20),
    'Prezzo Unitario': np.random.uniform(5.0, 20.0, 20).round(2),
    'Città': np.random.choice(città, 20)
})

# 1. Aggiunta colonna "Totale Vendite"
df['Vendite'] = df['Quantità'] * df['Prezzo Unitario']

# 2. Statistiche iniziali
vendite_per_prodotto = df.groupby('Prodotto')['Vendite'].sum().reset_index()
quantità_totali = df.groupby('Prodotto')['Quantità'].sum()
prodotto_top = quantità_totali.idxmax()
quantità_top = quantità_totali.max()

vendite_per_città = df.groupby('Città')['Vendite'].sum()
città_top = vendite_per_città.idxmax()
vendite_top = vendite_per_città.max()

vendite_sopra_1000 = df[df['Vendite'] > 1000]
df_ordinato = df.sort_values(by='Vendite', ascending=False)
vendite_per_città_count = df['Città'].value_counts()

# ----------------------------
# STAMPE INIZIALI
# ----------------------------
print(" PRIME 5 RIGHE DEL DATAFRAME:")
print(df.head())

print("\n ULTIME 5 RIGHE DEL DATAFRAME:")
print(df.tail())

print("\n TOTALE VENDITE PER PRODOTTO:")
print(vendite_per_prodotto)

print("\n PRODOTTO PIÙ VENDUTO (per quantità):")
print("Prodotto:", prodotto_top)
print("Quantità:", quantità_top)

print("\n CITTÀ CON IL MAGGIOR VOLUME DI VENDITE:")
print(città_top)

print("\n VENDITE CON VALORE SUPERIORE A 1000€:")
print(vendite_sopra_1000)

print("\n DATAFRAME ORDINATO PER TOTALE VENDITE (prime 5 righe):")
print(df_ordinato.head())

print("\nNUMERO DI VENDITE PER OGNI CITTÀ:")
print(vendite_per_città_count)

# ----------------------------
# FUNZIONI MENU PIVOT & MODIFICA
# ----------------------------
def mostra_menu():
    print("\n--- MENU MODIFICA DATI ---")
    print("1. Visualizza tabella pivot")
    print("2. Modifica un valore (usando pivot)")
    print("3. Esci")

def crea_pivot(df):
    pivot = df.pivot_table(index='Prodotto', columns='Città', values='Vendite', aggfunc='sum', fill_value=0)
    return pivot

def modifica_valore(df, pivot):
    print("\nTabella Pivot:")
    print(pivot)

    prodotto = input("\nInserisci il nome del prodotto da modificare: ")
    città = input("Inserisci la città da modificare: ")

    if prodotto in pivot.index and città in pivot.columns:
        print(f"\nValore attuale: {pivot.loc[prodotto, città]}")
        nuovo_valore = float(input("Inserisci il nuovo valore delle vendite: "))

        # Modifichiamo TUTTE le righe che corrispondono a quel prodotto e città
        condizione = (df['Prodotto'] == prodotto) & (df['Città'] == città)
        righe_corrette = df.loc[condizione]

        if len(righe_corrette) == 1:
            # Se c'è una sola riga, la modifichiamo direttamente
            df.loc[condizione, 'Vendite'] = nuovo_valore
        elif len(righe_corrette) > 1:
            print("\nCi sono più righe corrispondenti. Modifico la PRIMA occorrenza.")
            indice = righe_corrette.index[0]
            df.at[indice, 'Vendite'] = nuovo_valore
        else:
            print("Nessuna riga trovata con quei valori.")

        print(" Modifica completata nel DataFrame originale.")
    else:
        print(" Prodotto o città non trovati nella tabella pivot.")

    return df

# ----------------------------
# CICLO INTERATTIVO MENU
# ----------------------------
while True:
    mostra_menu()
    scelta = input("\nScegli un'opzione: ")

    if scelta == "1":
        pivot = crea_pivot(df)
        print("\nTabella Pivot:")
        print(pivot)

    elif scelta == "2":
        pivot = crea_pivot(df)
        df = modifica_valore(df, pivot)

    elif scelta == "3":
        print(" Uscita dal programma.")
        break

    else:
        print(" Scelta non valida. Riprova.")



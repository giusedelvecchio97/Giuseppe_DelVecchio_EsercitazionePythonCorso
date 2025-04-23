import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class AnalisiDati:
    @staticmethod
    def genera_dataframe(n=10):
        """
        Genera un DataFrame con colonne 'altezza', 'peso', 'età'.
        """
        np.random.seed(0)
        df = pd.DataFrame({
            'altezza': np.random.randint(150, 200, size=n),
            'peso': np.random.randint(50, 100, size=n),
            'età': np.random.randint(20, 60, size=n)
        })
        print(" DataFrame generato con successo.\n")
        return df

    @staticmethod
    def normalizza_minmax(df):
        """
        Normalizza le colonne 'altezza' e 'peso' con min-max.
        """
        df_norm = df.copy()
        for col in ['altezza', 'peso']:
            min_val = df_norm[col].min()
            max_val = df_norm[col].max()
            df_norm[col] = (df_norm[col] - min_val) / (max_val - min_val)
        print(" Normalizzazione completata.\n")
        return df_norm

    @staticmethod
    def visualizza_confronto(df_orig, df_norm):
        """
        Crea un confronto visivo tra dati originali e normalizzati.
        """
      
        fig,axes = plt.subplots(1, 2, figsize=(14, 6))
        sns.lineplot(data=df_orig[['altezza', 'peso']], markers=True, dashes=False, ax=axes[0])
        axes[0].set_title('Dati Originali')
        axes[0].set_ylabel('Valori')
        axes[0].set_xlabel('Indice')

        sns.lineplot(data=df_norm[['altezza', 'peso']], markers=True, dashes=False, ax=axes[1])
        axes[1].set_title('Dati Normalizzati (Min-Max)')
        axes[1].set_ylabel('Valori Normalizzati')
        axes[1].set_xlabel('Indice')

        plt.tight_layout()
        plt.show()
        print("Visualizzazione completata.\n")

# ==========================
# Menu principale con match
# ==========================

df_originale = None
df_normalizzato = None

while True:
    print("\n MENU ANALISI DATI")
    print("1. Genera dati simulati")
    print("2. Normalizza altezza e peso")
    print("3. Visualizza confronto grafico")
    print("0. Esci")

    scelta = input(" Inserisci la tua scelta: ")

    match scelta:
        case "1":
            df_originale = AnalisiDati.genera_dataframe()
            print(df_originale)
        case "2":
            if df_originale is not None:
                df_normalizzato = AnalisiDati.normalizza_minmax(df_originale)
                print(df_normalizzato)
            else:
                print(" Devi prima generare i dati (opzione 1).")
        case "3":
            if df_originale is not None and df_normalizzato is not None:
                AnalisiDati.visualizza_confronto(df_originale, df_normalizzato)
            else:
                print(" Devi prima generare e normalizzare i dati.")
        case "0":
            print(" Fine programma.")
            break
        case _:
            print(" Scelta non valida. Riprova.")

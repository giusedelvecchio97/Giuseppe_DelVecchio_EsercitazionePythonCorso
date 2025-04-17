import numpy as np
import sqlite3



class GestioneArray:
    def __init__(self):
        self.array1 = None  # array linspace
        self.array2 = None  # array random
        self.array_somma = None  # somma elemento per elemento

    def crea_array_linspace(self,num1,num2,num3):
      
        self.array1 = np.linspace(num1, num2, num3)

    def crea_array_casuale(self, num):
        
        self.array2 = np.random.rand(num)
    def somma_array(self):
        
            self.array_somma = self.array1 + self.array2
            return self.somma_array
        
    def somma_totale(self):
        
        return sum(self.array_somma)
            
        

    def somma_maggiori_di_5(self):
        
            return np.sum(self.array_somma[self.array_somma > 5])
    
    
    def stampa(self):
        print(f"{self.array1},{self.array2},{self.somma_array},{self.somma_totale()},{self.somma_maggiori_di_5()}")
        
        
gestore = GestioneArray()
    
while True:
        print("\n--- MENU ---")
        print("1. Crea array1 con linspace")
        print("2. Crea array2 con numeri casuali")
        print("3. Somma array1 e array2")
        print("4. Somma degli elementi > 5 in array_somma")
        print("5. Esci")

        scelta = input("Scegli un'opzione : ")

        match scelta:
            case '1':
                
                num1=int(input("inserisci valore di partenza"))
                num2=int(input("inserisci valore di fine intervallo"))
                num3=int(input("numero totale di elementi"))
                gestore.crea_array_linspace(num1,num2,num3)
            case '2':
                num=int(input("inserisci quanti numeri tra 0 e 1 devo generare"))
                gestore.crea_array_casuale(num)
            case '3':
                arr_sum=gestore.somma_array()
                print(arr_sum)
            case '4':
                sum5=gestore.somma_maggiori_di_5()
                print(sum5)
                
            case '5':
                somma_totale=gestore.somma_totale()
                print(somma_totale)
            
            case 6:
                gestore.stampa()
            case _:
                print("Scelta non valida. Riprova.")
                break






# Connessione al database SQLite
conn = sqlite3.connect('matrice.db')
cursor = conn.cursor()

# Creazione della tabella
cursor.execute("""
CREATE TABLE IF NOT EXISTS Matrice1 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    riga INTEGER,
    colonna INTEGER,
    valore INTEGER
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Matrice2 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    riga INTEGER,
    colonna INTEGER,
    valore INTEGER
);
""")

# Inserimento dei valori della matrice nel database
for i in range(gestore.array1.shape[0]):  # Itera sulle righe
    for j in range(gestore.array1.shape[1]):  # Itera sulle colonne
        cursor.execute("""
        INSERT INTO Matrice (riga, colonna, valore)
        VALUES (?, ?, ?)
        """, (i + 1, j + 1, gestore.array1[i, j]))  # Inserisce la riga, la colonna e il valore

for i in range(gestore.array2.shape[0]):  # Itera sulle righe
    for j in range(gestore.array2array2.shape[1]):  # Itera sulle colonne
        cursor.execute("""
        INSERT INTO Matrice (riga, colonna, valore)
        VALUES (?, ?, ?)
        """, (i + 1, j + 1, gestore.array2[i, j]))
# Commit e chiusura della connessione
conn.commit()
conn.close()
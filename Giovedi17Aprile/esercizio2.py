import numpy as np
import sqlite3

matrice = np.random.randint(1, 101, size=(6, 6))
centrale = matrice[1:5, 1:5]
righe_invertite = centrale[::-1]
indici = np.arange(6)
diagonale = righe_invertite[indici, indici]


maschera = matrice % 3 == 0
nuova_righe=righe_invertite[maschera] = -1

print(matrice)
print(centrale)
print(righe_invertite)
print(diagonale)
print(nuova_righe)
    
    
    



# Connessione a un database (si crea se non esiste)
conn = sqlite3.connect("matrice.db")
cursor = conn.cursor()

# Crea la tabella
cursor.execute("""
CREATE TABLE IF NOT EXISTS Matrice (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    col1 INTEGER,
    col2 INTEGER,
    col3 INTEGER,
    col4 INTEGER,
    col5 INTEGER,
    col6 INTEGER
)
""")


for i in range(matrice.shape):
    cursor.execute("""
        INSERT INTO Matrice (col1, col2, col3, col4, col5, col6)
        VALUES (?, ?, ?, ?, ?, ?)
    """, matrice[i])

# Salva le modifiche
conn.commit()


cursor.execute("SELECT * FROM Matrice")
matrice_nuova=np.array(cursor.fetchall())




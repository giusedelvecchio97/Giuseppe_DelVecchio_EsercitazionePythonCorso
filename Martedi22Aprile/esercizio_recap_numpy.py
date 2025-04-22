import sqlite3
import numpy as np
from collections import Counter

# Connessione al database
conn = sqlite3.connect("esempio_numpy.db")
cursor = conn.cursor()

# 1. Creazione delle tabelle
cursor.execute("DROP TABLE IF EXISTS tabella1")
cursor.execute("DROP TABLE IF EXISTS tabella2")
cursor.execute("DROP TABLE IF EXISTS tabella3")

cursor.execute("CREATE TABLE tabella1 (id INTEGER PRIMARY KEY, valore INTEGER)")
cursor.execute("CREATE TABLE tabella2 (id INTEGER PRIMARY KEY, valore INTEGER)")
cursor.execute("CREATE TABLE tabella3 (id INTEGER PRIMARY KEY, valore INTEGER)")

# 2. Popolamento con NumPy
valori1 = np.random.randint(10, 100, size=10)           # Valori casuali
valori2 = np.arange(10, 20)                             # Sequenza
valori3 = np.linspace(5, 15, num=10, dtype=int)         # Equidistanti (convertiti in int)

for i in range(10):
    cursor.execute("INSERT INTO tabella1 (id, valore) VALUES (?, ?)", (i + 1, int(valori1[i])))
    cursor.execute("INSERT INTO tabella2 (id, valore) VALUES (?, ?)", (i + 1, int(valori2[i])))
    cursor.execute("INSERT INTO tabella3 (id, valore) VALUES (?, ?)", (i + 1, int(valori3[i])))

conn.commit()

# 3. Recupero dati per operazioni
def get_valori(tabella):
    cursor.execute(f"SELECT valore FROM {tabella}")
    return np.array([row[0] for row in cursor.fetchall()])

# 4. Menu interattivo
while True:
    print("\nMENU OPERAZIONI:")
    print("1. Somma tabella1")
    print("2. Prodotto con scalare in tabella2")
    print("3. Moda dei valori in tabella3")
    print("4. Mediana di tabella1")
    print("5. Media di tabella2")
    print("0. Esci")

    scelta = input("Scegli un'opzione: ")

    match scelta:
        case "1":
            v1 = get_valori("tabella1")
            print(f"Somma tabella1 = {np.sum(v1)}")

        case "2":
            v2 = get_valori("tabella2")
            scalare = int(input("Inserisci lo scalare: "))
            print(f"Prodotto con scalare = {v2 * scalare}")

        case "3":
            v3 = get_valori("tabella3")
            moda = Counter(v3).most_common(1)[0][0]
            print(f"Moda tabella3 = {moda}")

        case "4":
            v1 = get_valori("tabella1")
            print(f"Mediana tabella1 = {np.median(v1)}")

        case "5":
            v2 = get_valori("tabella2")
            print(f"Media tabella2 = {np.mean(v2)}")

        case "0":
            print("Chiusura programma.")
            break

        case _:
            print(" Scelta non valida.")

# Chiusura connessione
conn.close()


import sqlite3
import numpy as np

# Connessione al database in memoria
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Eliminazione tabelle se già esistono
for nome in ["clienti", "tabella1", "tabella2", "tabella3", "stati"]:
    cursor.execute(f"DROP TABLE IF EXISTS {nome}")

# Creazione tabella clienti
cursor.execute('''
    CREATE TABLE clienti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
''')

# Creazione tabella stati
cursor.execute('''
    CREATE TABLE stati (
        nome_stato TEXT PRIMARY KEY,
        id_cliente INTEGER,
        FOREIGN KEY (id_cliente) REFERENCES clienti(id)
    )
''')

# Creazione delle tabelle tabella1, tabella2 e tabella3
for i in range(1, 4):
    cursor.execute(f'''
        CREATE TABLE tabella{i} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            col1 REAL,
            col2 REAL,
            col3 REAL,
            id_cliente INTEGER,
            FOREIGN KEY (id_cliente) REFERENCES clienti(id)
        )
    ''')

# Inserimento dati clienti
clienti = [("Alice",), ("Bob",), ("Charlie",), ("David",)]
cursor.executemany("INSERT INTO clienti (nome) VALUES (?)", clienti)

# Generazione delle matrici
matrice1 = np.random.rand(3, 3)
matrice2 = np.arange(9).reshape(3, 3)
matrice3 = np.linspace(10, 18, 9).reshape(3, 3)  

# Inserimento nelle tabelle tabella1, tabella2, tabella3
for i, matrice in enumerate([matrice1, matrice2, matrice3], 1):
    for j in range(3):
        cursor.execute(f'''
            INSERT INTO tabella{i} (col1, col2, col3, id_cliente) 
            VALUES (?, ?, ?, ?)
        ''', (*matrice[j], j + 1))

# Inserimento stati e associazione ai clienti
stati = [("Italia", 1), ("Francia", 2), ("Germania", 3), ("Spagna", 1)]
cursor.executemany("INSERT INTO stati (nome_stato, id_cliente) VALUES (?, ?)", stati)

conn.commit()

# Funzione per ottenere matrice da tabella
def get_matrice(tabella):
    cursor.execute(f"SELECT col1, col2, col3 FROM {tabella}")
    return np.array(cursor.fetchall())

# Funzione JOIN clienti e tabelle
def join_and_print_tables():
    query = '''
    SELECT c.id, c.nome, t1.col1, t1.col2, t1.col3,
           t2.col1, t2.col2, t2.col3,
           t3.col1, t3.col2, t3.col3
    FROM clienti c
    JOIN tabella1 t1 ON c.id = t1.id_cliente
    JOIN tabella2 t2 ON c.id = t2.id_cliente
    JOIN tabella3 t3 ON c.id = t3.id_cliente
    '''
    cursor.execute(query)
    risultati = cursor.fetchall()

    print("\n--- Risultati del JOIN tra le tabelle ---")
    for riga in risultati:
        print("ID:", riga[0])
        print("Nome:", riga[1])
        print("Tabella1:", riga[2], riga[3], riga[4])
        print("Tabella2:", riga[5], riga[6], riga[7])
        print("Tabella3:", riga[8], riga[9], riga[10])
        print("-" * 40)

# Funzione per calcolare la media per cliente e stato
def media_per_cliente_stato():
    id_cliente = input("Inserisci l'ID del cliente: ")
    stato = input("Inserisci il nome dello stato: ")

    query = '''
    SELECT t1.col1, t1.col2, t1.col3,
           t2.col1, t2.col2, t2.col3,
           t3.col1, t3.col2, t3.col3
    FROM stati s
    JOIN tabella1 t1 ON s.id_cliente = t1.id_cliente
    JOIN tabella2 t2 ON s.id_cliente = t2.id_cliente
    JOIN tabella3 t3 ON s.id_cliente = t3.id_cliente
    WHERE s.id_cliente = ? AND s.nome_stato = ?
    '''
    cursor.execute(query, (id_cliente, stato))
    dati = cursor.fetchall()

    if dati:
        array = np.array(dati).flatten()
        print(f"Media degli acquisti del cliente {id_cliente} nello stato '{stato}': {np.mean(array):.2f}")
    else:
        print("Nessun dato trovato per questo cliente in questo stato.")

# Menu interattivo
def menu():
    while True:
        print("\n MENU:")
        print("1. Operazioni su tabella1")
        print("2. Operazioni su tabella2")
        print("3. Operazioni su tabella3")
        print("4. Mostra JOIN completo")
        print("5. Media per cliente e stato")
        print("0. Esci")

        scelta = input("Scegli un'opzione: ")

        match scelta:
            case "1" | "2" | "3":
                while True:
                    print(f"\n📋 OPERAZIONI SU TABELLA {scelta}:")
                    print("1. Somma")
                    print("2. Media")
                    print("3. Mediana")
                    print("0. Indietro")

                    op = input("Scelta operazione: ")
                    m = get_matrice(f"tabella{scelta}")

                    match op:
                        case "1": print("Somma:", np.sum(m))
                        case "2": print("Media:", np.mean(m))
                        case "3": print("Mediana:", np.median(m))
                        case "0": break
                        case _: print("Operazione non valida.")

            case "4":
                join_and_print_tables()

            case "5":
                media_per_cliente_stato()

            case "0":
                print("Chiusura del programma.")
                break

            case _:
                print("Scelta non valida.")


# Avvio del menu (decommenta se vuoi farlo partire direttamente)
# menu()

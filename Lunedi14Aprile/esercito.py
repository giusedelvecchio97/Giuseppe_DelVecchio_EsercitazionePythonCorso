import sqlite3

# Creazione del database in memoria (usa "esercito.db" per un file)
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Creazione della tabella UnitaMilitare
cursor.execute("""
CREATE TABLE UnitaMilitare (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE NOT NULL,
    numero_soldati INTEGER NOT NULL,
    tipo TEXT NOT NULL
)
""")

# Creazione della tabella ControlloMilitare
cursor.execute("""
CREATE TABLE ControlloMilitare (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT
)
""")

# Creazione della relazione Unita <-> ControlloMilitare
cursor.execute("""
CREATE TABLE UnitaControllo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    unita_id INTEGER NOT NULL,
    controllo_id INTEGER NOT NULL,
    FOREIGN KEY (unita_id) REFERENCES UnitaMilitare(id),
    FOREIGN KEY (controllo_id) REFERENCES ControlloMilitare(id)
)
""")

# Creazione della tabella Esercito
cursor.execute("""
CREATE TABLE Esercito (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT
)
""")

# Creazione della relazione ControlloMilitare <-> Esercito
cursor.execute("""
CREATE TABLE ControlloEsercito (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    controllo_id INTEGER NOT NULL,
    esercito_id INTEGER NOT NULL,
    FOREIGN KEY (controllo_id) REFERENCES ControlloMilitare(id),
    FOREIGN KEY (esercito_id) REFERENCES Esercito(id)
)
""")

# Commit delle operazioni
conn.commit()

# Verifica: elenco delle tabelle create
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
tables
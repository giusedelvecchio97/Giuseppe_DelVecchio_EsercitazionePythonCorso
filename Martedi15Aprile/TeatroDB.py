import sqlite3

conn = sqlite3.connect("teatro.db")
cursor = conn.cursor()

# Tabella principale dei posti (VIP e Standard)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Posto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero INTEGER NOT NULL,
    fila TEXT NOT NULL,
    occupato BOOLEAN NOT NULL,
    tipo TEXT NOT NULL CHECK (tipo IN ('VIP', 'Standard'))
)
''')

# Tabella specifica per PostiVIP (collega all'ID del Posto)
cursor.execute('''
CREATE TABLE IF NOT EXISTS PostoVIP (
    id_posto INTEGER PRIMARY KEY,
    FOREIGN KEY (id_posto) REFERENCES Posto(id) ON DELETE CASCADE
)
''')

# Tabella specifica per PostiStandard
cursor.execute('''
CREATE TABLE IF NOT EXISTS PostoStandard (
    id_posto INTEGER PRIMARY KEY,
    costo REAL NOT NULL,
    FOREIGN KEY (id_posto) REFERENCES Posto(id) ON DELETE CASCADE
)
''')

# Tabella dei Servizi disponibili
cursor.execute('''
CREATE TABLE IF NOT EXISTS Servizio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
)
''')

# Tabella di collegamento tra Servizi e PostiVIP (molti-a-molti)
cursor.execute('''
CREATE TABLE IF NOT EXISTS ServizioPostoVIP (
    id_servizio INTEGER,
    id_posto_vip INTEGER,
    PRIMARY KEY (id_servizio, id_posto_vip),
    FOREIGN KEY (id_servizio) REFERENCES Servizio(id) ON DELETE CASCADE,
    FOREIGN KEY (id_posto_vip) REFERENCES PostoVIP(id_posto) ON DELETE CASCADE
)
''')

conn.commit()
conn.close()

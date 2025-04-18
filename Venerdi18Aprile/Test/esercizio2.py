import mysql.connector

# Funzione per stabilire la connessione al database
def connessione_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tua_password_db",
        database="rubrica"
    )

# Funzione per il login dell'utente
def login():
    nome_utente = input("Inserisci il nome utente: ")
    password = input("Inserisci la tua password: ")

    conn = connessione_db()
    cursor = conn.cursor()

    query = "SELECT * FROM utenti WHERE nome = %s AND password = %s"    #verifica co una query se l'utente esista nel database, select per ritornare i valori relativi a quelle credenziali
    cursor.execute(query, (nome_utente, password))

    if cursor.fetchone():                                      #se esiste allora è loggato
        print("Login effettuato con successo!")
        return True
    else:
        print("Nome utente o password errati.")
        return False

# Funzione per creare un nuovo contatto
def crea_contatto():
    nome = input("Inserisci il nome del contatto: ")
    telefono = input("Inserisci il numero di telefono: ")
    email = input("Inserisci l'email del contatto: ")

    conn = connessione_db()
    cursor = conn.cursor()

    query = "INSERT INTO contatti (nome, telefono, email) VALUES (%s, %s, %s)"
    cursor.execute(query, (nome, telefono, email))
    conn.commit()

    print("Contatto creato con successo!")

# Funzione per visualizzare tutti i contatti
def visualizza_contatti():
    conn = connessione_db()
    cursor = conn.cursor()

    query = "SELECT * FROM contatti"
    cursor.execute(query)

    for contatto in cursor.fetchall():
        print(f"Nome: {contatto[1]}, Telefono: {contatto[2]}, Email: {contatto[3]}")

# Funzione principale con il menu
def menu():
    if not login():
        return

    while True:
        print("\nMenu:")
        print("1. Crea un nuovo contatto")
        print("2. Visualizza tutti i contatti")
        print("3. Esci")

        scelta = input("Scegli un'opzione: ")

        match scelta:
            case "1":
                crea_contatto()
            case "2":
                visualizza_contatti()
            case "3":
                print("Uscita in corso...")
                break
            case _:
                print("Opzione non valida.")

# Avvia il programma
menu()

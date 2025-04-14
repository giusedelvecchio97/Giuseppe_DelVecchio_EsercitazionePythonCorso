import mysql.connector





mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Zanetti44C!",

)

mycursor = mydb.cursor()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Zanetti44C!",
  database="classestudenti"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS classestudenti")

def crea_tabella_studenti():
    query = """ CREATE TABLE IF NOT EXISTS STUDENTI (
        MATRICOLA INT AUTO_INCREMENT PRIMARY KEY,
        NOME VARCHAR(50) NOT NULL,
        COGNOME VARCHAR(50) NOT NULL
        
    )"""
    mycursor.execute(query)
    mycursor.execute("ALTER TABLE STUDENTI AUTO_INCREMENT = 1000")
    print("Tabella STUDENTI pronta.")

def aggiungi_studente(my_cursor, table):
    nome = input('\nInserisci il nome dell\'alunno: ').strip()
    cognome = input('\nInserisci il cognome dell\'alunno: ').strip()
    
    query = f'INSERT INTO {table} (NOME, COGNOME) VALUES(%s,%s)'
    values = (nome.upper(), cognome.upper())
    my_cursor.execute(query, values)
    mydb.commit()
    print(f"{nome.upper()} {cognome.upper()} aggiunto.")
    
def elimina_studente(my_cursor, table):
    while True:
        nome = input('\nInserisci il nome dell\'alunno: ').strip()
        cognome = input('\nInserisci il cognome dell\'alunno: ').strip()
        values = (nome.upper(), cognome.upper())
        query = f'SELECT * FROM {table} WHERE NOME = %s AND COGNOME = %s'
        my_cursor.execute(query, values)
        res = my_cursor.fetchone()
        print(res)
    
        if res:
            conferma = int(input('Vuoi eliminare questo alunno? (1/SÃ¬, 2/No)'))
            if conferma == 1:
                query = f'DELETE FROM {table} WHERE NOME = %s AND COGNOME = %s'
                my_cursor.execute(query, values)
                mydb.commit()
                print(f'{nome}, {cognome} eliminato.')
                break
            elif conferma == 2:
                print('Ripeti operazione')
                continue
            else:
                print('Errore, opzione non valida')
                continue
        else:
            print(f"Studente {nome} {cognome} non trovato.")
            
            
def crea_tabella_voti():
    query = """ CREATE TABLE IF NOT EXISTS VOTI (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        MATRICOLA INT,
        ESAME VARCHAR(50) NOT NULL,
        VOTO INT NOT NULL,
        FOREIGN KEY (MATRICOLA) REFERENCES STUDENTI(MATRICOLA)
    )"""
    mycursor.execute(query)
    print("Tabella VOTI pronta.")    

def aggiungi_voto(my_cursor, table):
    matricola = int(input('\nInserisci la matricola dello studente: '))
    esame = input('\nInserisci il nome dell\'esame: ').strip()
    voto = int(input('\nInserisci il voto (18-30): '))
    
    query = f'SELECT * FROM STUDENTI WHERE MATRICOLA = %s' # Verifica se la matricola esiste nel database dello studente
    my_cursor.execute(query, (matricola,))
    if my_cursor.fetchone():  # Se esiste
        query = f'INSERT INTO {table} (MATRICOLA, ESAME, VOTO) VALUES(%s,%s,%s)'
        values = (matricola, esame.upper(), voto)
        my_cursor.execute(query, values)
        mydb.commit()
        print(f"Voto per {esame} aggiunto.")
    else:
        print("Matricola non trovata. Impossibile aggiungere il voto.")

def visualizza_voti(my_cursor):
    matricola = int(input('\nInserisci la matricola dello studente: '))
    
    # Controllo che la matricola esista
    query = f'SELECT * FROM STUDENTI WHERE MATRICOLA = %s'
    my_cursor.execute(query, (matricola,))
    if my_cursor.fetchone():  # Se esiste
        query = f'SELECT ESAME, VOTO FROM VOTI WHERE MATRICOLA = %s' # Visualizza i voti dello studente
        my_cursor.execute(query, (matricola,))
        risultati = my_cursor.fetchall()
        if risultati:
            print("\nVoti:")
            for esame, voto in risultati:
                print(f"{esame}: {voto}")
        else:
            print("Nessun voto trovato per questo studente.")
    else:
        print("Matricola non trovata.") 
        

def crea_tabella_voti():
    query = """ CREATE TABLE IF NOT EXISTS VOTI (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        MATRICOLA INT,
        ESAME VARCHAR(50) NOT NULL,
        VOTO INT NOT NULL,
        FOREIGN KEY (MATRICOLA) REFERENCES STUDENTI(MATRICOLA)
    )"""
    mycursor.execute(query)
    print("Tabella VOTI pronta.")   
    


def media():
    
# Chiedi all'utente di inserire la matricola che vuole cercare
    matricola_cercata = input("Inserisci la matricola che vuoi cercare: ")

    # Esegui la query con WHERE e GROUP BY
    query = """
        SELECT matricola, AVG(voto) AS media_voti
        FROM VOTI
        WHERE matricola = %s
        GROUP BY matricola
    """
    mycursor.execute(query, (matricola_cercata,))

    # Ottieni i risultati
    risultato = mycursor.fetchone()

    # Verifica se la matricola è stata trovata e mostra il risultato
    if risultato:
        print(f"\nMatricola {matricola_cercata} ha una media voti di: {risultato[1]:.2f}")
    else:
        print(f"\nMatricola {matricola_cercata} non trovata.")
        
            

def menu():
    crea_tabella_studenti()
    while True:
         print("\n=== MENU STUDENTI ===")
         print("1. Aggiungi studente")
         print("2. Elimina studente")
         print("3. Esci")

         scelta = input("Scegli un'opzione (1-3): ")

         match scelta:
            case "1":
                aggiungi_studente(mycursor, "STUDENTI")
            case "2":
                elimina_studente(mycursor, "STUDENTI")
            case "3":
                print("Uscita dal programma.")
                break
            case _:
                print("Scelta non valida. Riprova.")

    mycursor.close()
    mydb.close()

menu()
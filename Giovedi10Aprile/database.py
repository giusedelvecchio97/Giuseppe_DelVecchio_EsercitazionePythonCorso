import mysql.connector

#abbiamo creato la connesione al DB
myDB=mysql.connector.connect(      #oggetto connesione DB

    host="localhost",                   #variabili per connetterti al db
    user="root",
    password="Zanetti44C!",
    database="corsopython"
)

myCursor= myDB.cursor()    #cursone che serve per le query al db
                            #cursore che interagisce col DB
                            # il cursor è un buffer , quindi una volta che scarica dal DB i valori, magari con un for, si svuota




    #il cursore serve solo per modificare la struttura del DB


#query="CREATE TABLE utenti(ID INT PRIMARY KEY,NOME VARCHAR(50),INDIRIZZO VARCHAR(50))"
query="ALTER TABLE  utenti MODIFY ID INT AUTO_INCREMENT "

def insertdati(dati):
    query="INSERT INTO utenti(NOME,INDIRIZZO) VALUES(%s,%s) "   #%s serve per injection e si usa su ogni comando per modificare i dati
    #val=[("Giuseppe","Via Isonzo"),("Marco","Via Napoli"),("Andrea","Via Garrubba")]  # per mettere più valori insieme basta dare una lista di tuple


    myCursor.executemany(query,dati)    
    myDB.commit()  # gestione dati


#print(myCursor.rowcount," righe inserite!")

def select():
    
    query="select *from utenti"
    myCursor.execute(query)
    
    result= myCursor.fetchall()     #serve per mettere i dati in result, cattura i risultati della query
    
    for row in result:
        print(row)
        
    
select()



def selectOne():
    
    query="select *from utenti"
    myCursor.execute(query)
    
    result= myCursor.fetchone() 
    print(result) 
    



# se devo modificare la struttura basta execute, invece per le select fechone o fetchall, per modifiche invece sui dati per forza il commit()

myDB.close()   #chiude il Db 
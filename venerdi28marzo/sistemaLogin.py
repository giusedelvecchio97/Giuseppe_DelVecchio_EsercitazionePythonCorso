account=["admin","1234"]
database=[account]

nome=input("inserisci nome da ricercare")
password=input("inserisci passwrod da ricercare")

account1=[nome,password]


    #verifica se le credenziali esistano, nel caso lo fossero da il benvenuto
if(account1 in database):
    
    print("Ciao Benevenuto ",account1[0])
    
    # chiede all'utente se voglia modificare nome o password
    scelta=input("vuoi modificare un campo del programma? seleziona A per modificare nome o B per la password")
    
    match scelta:

           # nel primo caso fa inserire il nuovo nome, lo salva in accoun1 lista d appoggio, rimuove la lista vecchia dal database e la aggiunge col nuovo campo         
                
        case "A":
            nome1=input("inserisci nuovo nome")
            account1.remove(nome)
            account1.insert(0,nome1)
            database.remove(account)
            database.appende(account1)

                #analogamente fa con la password nuova
        case "B":
            
            pass1=input("inserisci nuova password")
            account1.remove(password)
            account1.insert(1,pass1)
            database.remove(account)
            database.appende(account1) 
        case _ :
            
            print("uscita")
        
        #chiede all'utente se voglia inserire domande come colore o animale preferito 
    scelta1=input("quale domada preferisci? \n 1 quale sia il tuo colore preferito? \n 2quale sia il tuo animale preferito?")
    if(scelta==1):
        
                #inserisce colore, aggiunge un campo alla lista d'appoggio database1 e rimuove dal database quella vecchia e aggiunge quella nuova con il nuovo campo aggiunto domanda
        risposta=input("inserisci colore")
        account1.append(risposta)
        database.remove(account)
        database.appende(account1) 
        
        
        #analogamente lo fa con animale
    else:
        risposta1=input("inserisci animale")
        account1.append(risposta1)
        database.remove(account)
        database.appende(account1) 
        
        
        

        
    
        # nel caso le occorenze non fossero nel database     
    
else:
    
    print("credenziali errate, inserisci credenziali corrette")
    
   
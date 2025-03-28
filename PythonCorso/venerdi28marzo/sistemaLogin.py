account=["admin","1234"]
database=[account]

nome=input("inserisci nome da ricercare")
password=input("inserisci passwrod da ricercare")

account1=[nome,password]

if(account1 in database):
    
    print("Ciao Benevenuto ",account1[0])
    
    
    scelta=input("vuoi modificare un campo del programma? seleziona A per modificare nome o B per la password")
    
    match scelta:
        case "A":
            nome1=input("inserisci nuovo nome")
            account1.remove(nome)
            account1.insert(0,nome1)
            database.remove(account)
            database.appende(account1)
        
        case "B":
            
            pass1=input("inserisci nuova password")
            account1.remove(password)
            account1.insert(1,pass1)
            database.remove(account)
            database.appende(account1) 
        case _ :
            
            print("uscita")
        
        
    scelta1=input("quale domada preferisci? \n 1 quale sia il tuo colore preferito? \n 2quale sia il tuo animale preferito?")
    if(scelta==1):
        
        risposta=input("inserisci colore")
        account1.append(risposta)
        
    else:
        riposta1=input("inserisci animale")
        account1.append(risposta1)  
        
        
        

        
    
            
    
else:
    
    print("credenziali errate, inserisci credenziali corrette")
    
    scelta=input("vuoi un suggerimento? SI or NO")
    
    if(scelta=="SI"):
        
        print("colore giallo")
        print("animale preferito: leone")
    
    else:
    
        print("uscita dal programma")
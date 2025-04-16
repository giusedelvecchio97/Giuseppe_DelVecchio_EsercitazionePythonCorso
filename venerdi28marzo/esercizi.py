num=int(input(print("inserisci un numero")))

if(num>0):
    print("numero positivo")
    if(num>10):
        print("ok")
        
    
else:
    print("valore inserito non corretto")
    
    
    
 # inizializza una lista di parole, fa scegliere all'utente l'opzione
 #in base alla scelta farà svolgere l'azione di aggiunta rimozione o ordinamento
    
parole=["Marco","Guido","Giuseppe"]

scelta=int(input(print("inserisci scelta, in base a cosa tu voglia fare.\n 1 Aggiungere\n 2Eliminare\n 3 Ordinare")))

if(scelta==1):
    
    parole.append(input(print("inserisci il nome da aggiungere")))
    print(parole)
    
elif(scelta==2):
        parole.remove(input(print("Inserisci nome da eliminare")))
        print(parole)
        
else:
    
    parole.sort()
    print(parole)
    
    
    
# inizializzo una lista di account( a sua volta lista di 3 elementi))

accounts=[]
id=1

# l'utente sceglie se inserire un nuovo account o ricercarlo nel caso selezionasse NO
scelta=input(print("cosa vuoi fare? vuoi inserire account nuovo? Scrivi Si or No"))

if(scelta=="SI"):

    #   inizializza una lista con i 3 campi id,nome e password e lo aggiunge alla lista accaunts

 nome=input(print("inserisci un nome"))
 password=input(print("inserisci password"))
 account=[nome,password,id]
 accounts.append(account)


            # altrimenti lo ricerca nella lista accounts nel caso esistesse
else :
    nome=input(print("inserisci il nome da ricercare"))
    password=input(print(" inserisci la password da ricercare"))
    
    account1=[nome,password,id]
    
    if(account1 in accounts):
        print("account presente")
        
    else :
        print("account non presente")
    


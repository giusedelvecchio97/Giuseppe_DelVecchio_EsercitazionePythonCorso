import membroSquadra as ms
import random

squadra1=[]
squadra2=[]

def inserimento_squadre():
    
    lista=[]
    scelta=int(input(" cosa vuoi fare ? \n1. inserire Giocatore\n2. Inserire Allenatore\n3.Inserire Staff"))
    
    
    match(scelta):
        
        
        case 1:
            
            
            for i in range(4):
                
                nome=input("inserisci nome giocatore")
                eta=input("inserisci eta")
                ruolo=input("inserisci ruolo")
                rate=int(input("inserisci valore giocatore"))
                ruolo=input("inserire numero maglia")
                giocatore=ms.Giocatore(nome,eta,ruolo,rate)
                lista.append(giocatore)
            
            return lista
                
                
                
                
                
            
        case 2:
            
            
                
                nome=input("inserisci allenatore")
                eta=input("inserisci eta")
                esperienza=input("inserisci esperienza")
                rate=int(input("iserisci valore allenatore"))
                allenatore=ms.Allenatore(nome,eta,esperienza,rate)
                lista.append(allenatore)
                return lista
                
                
                
            
                
                
                
        case 3:
            
            for i in range(1):
                
                nome=input("inserisci nome assistente ")
                eta=input("inserisci eta")
                esperienza=("inserisci esperienza")
                rate=input("inserisci rate")
                
                scelta1=int(input(" l'assistente è un fisioterapista o un analista? 1 or 2"))
                
                if(scelta1==1):
                    
                    laurea=input("inserisci laurea")
                    fisio=ms.Fisioterapista(nome,eta,esperienza,rate,laurea)
                    lista.append(fisio)
                    
                else:
                    storico=float(input("inserisci percentuale storico"))
                    laurea=input("inserisci laurea")
                    analista=ms.Analista(nome,eta,esperienza,rate,laurea,storico)
                    lista.append(analista)
            
            return lista
                    
        case _:
            print("uscita")
            
                    
                    
                    







def gioca_partita(squadra1,squadra2):
    

    for i in range(len(squadra1)):
        
        sum=sum+squadra1[i].rate
        
    for i in range(len(squadra2)):
        
        sum1=sum1+squadra2[i].rate
        
    
    if(sum>sum1):
        
        print("squadra1 ha vinto")
        
        a=0
        b=0
        
        
        while(a<=b):
            a=random.randint(1,6)
            b=random.randint(1,5)
            
        
        print(f" squdra 1 {a}--- squadra2 {b}")
        
        
    
    elif(sum<sum1):
        
        print("squdra 2 ha vinto")
        
          
        a=0
        b=0
        
        
        while(a>=b):
            a=random.randint(1,6)
            b=random.randint(1,5)
            
        
        print(f" squdra 1 {a}--- squadra2 {b}")
    
    else:
        print("pareggio")
        
          
        a=1
        b=0
        
        
        while(a<b) or (a>b):
            a=random.randint(1,6)
            b=random.randint(1,5)
            
        
        print(f" squdra 1 {a}--- squadra2 {b}")
        
        






opzione=int(input("Ciao, cosa vuoi fare? \n1. comporre squadra\2. giocare partita"))

match opzione:
    
    case 1:  
        squadra1=inserimento_squadre()
        
    case 2: 
        gioca_partita(squadra1,squadra2)
        
    
    
    case _:
        
        print("uscita")
        
        

        
    
    
        
    
    
        




        
        
        
        

                    
                    
                
                
                
                
        
        
import numpy as np


start=0
stop=0
step=0
c=True
while c:
    
    scelta=int(input("Cosa vuoi fare?\n1.inserire lo start\n2.stop\n3step\n0 per uscire e visualizzare l'array "))
    
    match scelta:
        
        case 1: 
            start=int(input("inserire un valore per lo start"))
            
        case 2:
             stop=int(input("inserire un valore per lo stop"))
             
        case 3:
            
            
            while True:
                step=int(input("inserire un valore per lo step"))
                if(step==0):
                    print("valore errato")
                    
                    continue
                
                else: break
            
        
        
        
            
            
            
            
        case _:
            c=False
                


arr=np.arange(start,stop+1,step) 
print(arr)    

righe=(int(input("inserisci riga per il reshape")))
colonna=(int(input("inserisci riga per il reshape")))
arr2=arr.reshape(righe,colonna)
print(arr2)
          
            
import numpy as np







print("-----inizio programma-----")
while True:
 
 scelta=int(input(" inserisci la scelta corretta :\n1 CREA UN ARRAY E CAMBIA LA FORMA\n2.GENERA UN ARRAY CASUALE E CALCOLA\n3.STAMPA LE SOMME\n0.ESCI"))   
 match scelta:
     
    case 1:
        
        
        
        arr=np.linspace(0,10,12)
        matrice=arr.reshape(3,4)
        print(matrice)
    case 2:
       arr1=np.random.choice([0, 1], size=(3, 4))
       print(arr1)
       
    
    
    case 3:
        print("Sum of arr1:", arr1.sum())
        print("Sum of arr:", arr.sum())
         
        
    case _:
        print("esci")
        break
        
        
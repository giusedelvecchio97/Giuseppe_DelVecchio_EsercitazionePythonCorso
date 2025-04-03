#primo esercizio

scelta=int(input("inserisci opzione:\n1.numero\n2.Lettera"))
i=0  #contatore per il numero di caratteri per le stringhe
if scelta==1:
    
    num=int(input("inserisci numero"))
    
    
    if num%2==0:
        print("numero pari")
    else:
        print("numero dispari")  
        
else:
    stringa=input("inserisci la stringa")
    
    
        
    if len(stringa)%2==0:
        print("numero pari")
    else:
        print("numero dispari") 
        
        




flag=True
lista=[]

while(risp=="SI"):
    while(flag):
        num=int(print("inserisci numeri da inserire"))
        lista.append(num)
        
        scelta=int(print("vui inserire ancora numeri?1 per inserire 0 per uscire"))
        if scelta!=1:
            flag=False
        #creo due liste per i primi e i non primi, controllo se siano divisibili per i numeri primi secono la fattorizzazione dei primi, e salvo quei numeri nei vari array in base all'esito delle divisioni
        primi=[]
        nonprimi=[]
        for var in lista:
            
            if lista[i] <= 1:
                   
                    nonprimi.append(lista[i])
                    
                    if lista[i]<= 3:
                            
                            primi.append(lista[i])
                    if lista[i] % 2 == 0 or lista[i]% 3 == 0:
                        nonprimi.append(lista[i])   
                    k = 5
                    while k * k <= lista[i]:
                        if lista[i]% k == 0 or lista[i]% (k + 2) == 0:
                            nonprimi.append(lista[i])
                            k+=6
                    primi.append(lista[i])
        
        print(primi)
        print(nonprimi)
        
        risp=(input("vuoi ripetere il ciclo?"))
    




#esercizio 3       
        

num1=int(input("inserisci primo numero"))
    
num2=int(input("inserisci secondo numero"))
lista1=[]
lista2=[]


              
 # controllo quali siano i divisori primi dei due numeri e li salvo nelle liste1 e 2                          
for i in range(1, int(num1**0.5) + 1):
     if num1 % i == 0:  # Se i è divisore di n
            lista1.add(i)
        
for i in range(1, int(num2**0.5) + 1):
 if num2 % i == 0:  # Se i è divisore di n
            lista2.add(i)
   # controllo se le liste hanno divisori in comune, altrimenti sono coprimi     
if(lista1!=lista2):
    print("i numeri sono coprimi")
    
    
#ordino le due stringhe così da ottenere una succesione di caratteri identica nel caso fossero acronimi
stringa1=input("inserisci prima stringa")
stringa2=input("inserisci seconda stringa")
stringa.sort()
stringa2.sort()

if stringa1==stringa2:
    ("le stringe sono degli acronimi")   

        
    
                  



    
    
    
  
    
    
    
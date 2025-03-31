controller= True
while(controller):
    
    while(controller):
        
        scelta=bool(input(" vuoi continuare?"))
        
        if(scelta==False):
            controller=False
        
        else:
            var=0
            
            while(var<5):
                var= var+1
            
            print("valore diventato maggiore di 5")
            
            


#esempio FOR

lista=[1,2,3,4]


for num in lista:
    print(num)
    
    

string="Mirko"

for c in string:
    
    print(c)
    
    
    

# due cicli, quello più esterno serve all'utente per continuare ad inserire un valore per far continuare il codice
#l'altro ciclo col range serve a stampare i valori da num a 0
controller=True

while(controller):

        num=int(input("inserisci un valore il conteggio"))

        for num in range(num,-1,-1):
            print(num)
            
    

        scelta=int(input("vuoi continuare"))

        if(scelta=="NO"):
            controller=False
            
            
            
  
  

# menu per permettere di scegliere se verificare i primi o verificare se un numero sia pari o meno

scelta=int(input("Quale esercizio vuoi vedere? numeri primi\n numeri pari\n inserici 1 o 2 per le scelte"))   

match scelta:
    
    case 1:
       

        i=0
        lista=[]

        while(i!=5):
            var=int(input("inserisci un numero"))    
            
        
            if(var%2==0):
            
                lista.append(var)
                i=i+1

            
                
        print(lista)
        
    case 2:
                i=0
                lista=[]

                while(i!=5):
                    n=int(input("inserisci un numero"))
                    
                
                    if n <= 1:
                        print("numero non primo")
                    if n <= 3:
                        lista.append(var)
                    if n % 2 == 0 or n % 3 == 0:
                        print("numero non primo")
                    k = 5
                    while k * k <= n:
                        if n % k == 0 or n % (k + 2) == 0:
                        
                         k+=6
                        
                        else:
                            
                            lista.append(var)
                            i+=1
                    
                    
                    print(lista)    

    case _:
        
        print("ciao")
        
                        

    
    


    
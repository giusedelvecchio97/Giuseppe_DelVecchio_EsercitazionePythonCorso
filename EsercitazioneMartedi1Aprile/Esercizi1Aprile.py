controller=True     #ESERCIZIO 1
flag=True

while(controller):
   
    while(flag):
        num=int(input("inserisci un numero"))
        if(num>0):
            flag=False
        else:
            print("inserisci un valore maggiore di zero")
    
     
        
            
    scelta=int(input("Inserisci una scelta..Cosa vuoi fare?\n1.Visualizzare la somma dei pari da 1 a n\n2 visualizzare i dispari\3 visualizzare i primi"))
    
    match scelta:
        case 1:
            var=0 
            for var in range(num):
                
                if(var%2==0):
                    somma=somma+var
            
            print(somma)
        
        case 2:
            
            for var in range(num):
                
                if(num%2!=0):
                    
                    print(var) 
            
        
        case 3:
            
             if num <= 1:
                   
                    print("numero non primo")
                    
                    if num<= 3:
                            
                            print("numero primo")
                    if num % 2 == 0 or num% 3 == 0:
                        print("numero non primo")   
                    k = 5
                    while k * k <= num:
                        if num% k == 0 or num% (k + 2) == 0:
                            print("numero non primo")
                            k+=6
                    print("numero primo")
        
        case _:
            print("premi 0 per uscire")
            controller=False
                    

#ESERCIZIO 2

controller=True
flasg=True

while(controller):
   
    while(flag):
        num=int(input("inserisci un numero"))
        if(num>0):
            flag=False
        else:
            print("inserisci un valore maggiore di zero")
    
     
        
            
    scelta=int(input("Inserisci una scelta..Cosa vuoi fare?\n1.Generare una lista di casuali da 1 a n\n2 Stampare la somma dei numeri pari\3 verificare se un numero è primo o meno\n4. stampare i dispari\n5.stampare i primi6.verificare se la somma sia un primo o meno"))
    
    match scelta:
        
        case 1:
            
            random=None
            lista = random.sample(range(1, 101), 10)
            print(lista)
        
        case 2:
            for var in range(len(lista)-1):
                
                if(var%2==0):
                    somma=somma+var
            
            print(somma)
            
        
        case 3:
            flag=False
            for var in range(len(lista)-1):
            
                if var <= 1:
                    
                        print("numero non primo")
                        print(flag)
                        
                        if var<= 3:
                                
                                print("numero primo")
                                print(flag=True)
                        if var % 2 == 0 or var% 3 == 0:
                            print("numero non primo") 
                            print(flag)  
                        k = 5
                        while k * k <= var:
                            if var% k == 0 or var% (k + 2) == 0:
                                print("numero non primo")
                                print(flag)
                                k+=6
                        print("numero primo")
                        print(flag=True)
                    
        case 4:
            
            for var in range(len(lista)-1):
                
                if(var%2!=0):
                    
                    print(var)
                    
        case 5:
             for var in range(len(lista)-1):
            
                
                    
                        
                    
                        
                        if var<= 3:
                                
                                print("numero primo")
                                print(var)
                       
                        k = 5
                        while k * k <= var:
                            if var% k == 0 or var% (k + 2) == 0:
                                print("numero non primo")
                               
                                k+=6
                        print("numero primo")
                        print(var)
            
        case 6:
             
            for var in range(len(lista)-1):
                  
                  num=num+var   

            if num <= 1:
                    
                        print("numero non primo")
                        print(flag)
                        
                        if num<= 3:
                                
                                print("numero primo")
                                print(flag=True)
                        if num % 2 == 0 or num% 3 == 0:
                            print("numero non primo") 
                            print(flag)  
                        k = 5
                        while k * k <= num:
                            if num% k == 0 or num% (k + 2) == 0:
                                print("numero non primo")
                                print(flag)
                                k+=6
                        print("numero primo")
                        print(flag=True)
            
            
        case _:
            print("premi 0 per uscire")
            controller=False
                    
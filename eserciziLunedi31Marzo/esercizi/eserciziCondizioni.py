
#esercizio 1
eta= int( input("inserisci la tua età"))

if (eta<18):
    
    print("mi dispiace, non puoi vedere questo film")

else:
    print("puoi vedere questo film")
    
    

#ESERCIZIO 2

scelta=int(input("inserisci scelta=\n 1.moltiplicazione1n2.addizione\n 3.divisione\n,4.sottrazione"))
num1=0
num2=0
match scelta:
    
    case 1:
        
        num1=float(input("inserisci 1 numero"))
        num2=float(input("inserisci secondo numero"))
        
        prodotto=num1*num2
        print(prodotto)
        
        scelta1=int(input("vuoi fare un'altra operazione?2.addizione\n 3.divisione\n,4.sottrazione"))
        
        match scelta1:
            
            case 1:
                
                print(num1+num2)
            
            case 2:
                
                if(num2==0):
                    num2=int(input("inserisci un valore maggiore di zero"))
                
                    div=num1/num2
                    print(div)
                
                else :
                    
                    div=num1/num2
                    print(div)
                    
                
                    
                    
                
            
            
            
            case 3:
                
                sottr=num1-num2
                print(sottr)
            
            case _:
                print("ciao")
       
      
            
                        
                
                        
        
    case 2:
        
        num1=float(input("inserisci 1 numero"))
        num2=float(input("inserisci secono numero")) 
        somma=num1+num2   
        scelta1=int(input("vuoi fare un'altra operazione?2.moltiplicazione\n 3.divisione\n,4.sottrazione"))
        
        match scelta1:
            
            case 1:
                
                print(num1*num2)
            
            case 2:
                
                if(num2==0):
                    num2=int(input("inserisci un valore maggiore di zero"))
                
                    div=num1/num2
                    print(div)
                
                else :
                    
                    div=num1/num2
                    print(div)
                    
                
                    
                    
                
            
            
            
            case 3:
                
                sottr=num1-num2
                print(sottr)
            
            case _:
                print("ciao")
        
     
         
        
        
                 
    case 3:
            num1=float(input("inserisci 1 numero"))
             
             
            num2=float(input("inserisci secondo numero"))
             
            if(num2==0):
                 
                print("attenzione stai usando 0 come denominatore ")
                num2=float(input("inserisci di nuovo il valore"))
            else:
                    
                div=num1/num2
                print(div)
            
            scelta1=int(input("vuoi fare un'altra operazione?2.addizione\n 3.addizione\n,4.sottrazione"))
            
            match scelta1:
            
                case 1:
                
                 print(num1+num2)
            
                case 2:
              
              
                    print(num1*num2)
                    
                
            
                case 3:
                
                    sottr=num1-num2
                    print(sottr)
            
                case _:
                    print("ciao")
            
                
    
    case 4:
        
        num1=float(input("inserisci 1 numero"))
             
             
        num2=float(input("inserisci secondo numero"))
        
        sottr=num1-num2
        print(sottr)
    
    
    case _:
                print("ciao")
            
            
            
        
        
                            
    

                            
                
                            
            
            
                                  
                
            
            
        
           
        
        
        
        
        
        
    
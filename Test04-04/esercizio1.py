



var=int(input("inserisci un valore "))
int1=[]
float1=[]


for i in range(var-1):
    
    c=True
    while(c):
        
        var1=int(input("inserisci valore intero"))
        
        int1.append(var1)
        
        var2=float(input("inserisci un valore float"))
        float1.append(var2)
        
        risposta=input("vui continuare a inserire?")
        if(risposta.upper()=="NO"):
            
            c=False    
    
    
    
    
    scelta=int(input("inserisci scelta "))
    
    match scelta:
        
        
        case 1:
            
            print(int1)
            
        case 2:
            print(float1)
            
        case 3:
            print(int1,float1)
        
        case _:
            c=False
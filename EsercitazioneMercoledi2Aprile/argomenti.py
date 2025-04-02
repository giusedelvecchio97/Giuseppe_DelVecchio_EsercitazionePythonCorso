
def operazioni(a,b):
    x=a
    y=b
    
    print("OPERAZIONI FATTE NEL CORSO,STAMPATE GRAZIE AL METODO print()")
    print(x+y)
    print(x-y)
    print(x/y)
    print(x%y)
    print(x**y)
    print(x*y)
  
def lista(): 
      
      lista=["Marco","Stefano","Andrea"] 
      print(lista.sort)
      print(len(lista))
      print(lista.reverse())
      print(lista)
      
      
def blocco_if():
    
    var=int(input("inserisci un valore >10 e <15"))
    
    if(var>10 and var<15):
        
        print("ok ")
    
    elif(var<10):
        ("range sbagliato")
        
    else:
        print("troppo alto")
        

def cicli():
    
    i=0
    for i in range(0,10,2):
        
        print(i)
        
    
    str="MARCO"
    
    for i in str:
        
        print(i)
        
    
    var=print(input("inserisci un valore <10"))
    
    while(var>10):
        print("valore errato")
        

def tuple():
    
    tupla=(2,3,4,5,5)
    print(tupla)
    print("stamperà 1 volta il 5")
    
    
    
def insiemi():
    
    set=(1,2,4,5)
    set2=(1,2,5,8,9)
    print("unione")
    print(set.union(set2))
    print("intersezione ")
    print(set.intersection(set2))
    print("differenza",set.difference(set2))
    print("differenza simmetrica",set.simmetric_difference(set2))
    
    
def modificasomma(somma):
    
    def wrapper(*arg,**wrags):
        
        print("la somma tra a e b è")
        sum=somma()
        print("la modifichiamo")
        
        return sum*9

 

@modificasomma
def somma(a,b):
        
        return a+b
        
     
print(somma(4,5))


c=True

while(c):
    
    var=int(input("inserisci scelta:1. prime operazioni e assegnazione\n blocco if\n3. Cicli\n4 decoratori\5 liste\6tuple\n7insiemi")) 
    
    match var:
        
        case 1:
                operazioni(4,5)   
        
        case 2:
            
             blocco_if()
            
        
        case 3:
            cicli()
            
        
        case 4:
            
            
            print(somma(4,6))
            
        case 5:
            
            lista()
            
            
        case 6:
            tuple()
        
        
        case 7:
            insiemi()
        
        case 8:
            
            print("ciao")
            
            c=False
     
    


    
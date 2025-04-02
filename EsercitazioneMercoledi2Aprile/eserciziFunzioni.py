
#funzione che calcola il quadrato di un numero
def quadrato(num):
    
    num=int("inserisci un numero")
    return num**2

#funzione di una somma dei quadrati degli elemnti della lista
def somma_lista(lista):
    var=0
    somma=0
    for var in lista:
        
        var=var**2          #scorro nella lista e aggiungo a var il valore della lista al quadrato
        somma=somma+var
    
    return somma
    
def quadrato_super(lista1,lista2):    # funzione che mi carica una lista inizialmente,chiedendo all'utente il numero che preferisca, poi carica in superlista le liste caricate dall'utente
    
    while(controller):
            
            while(controller1):
                
                lista2.append(int(input("inserisci elemento")))
                risposta=input("vuoi inserire altri valori?") 
                if(risposta=="NO"):
                  controller1=False
                  
            lista1.append(lista2)
            risposta=input("vuoi inserire altre liste?") 
            if(risposta=="NO"):
                  controller1=False
    sum=0   
    for v in lista1:
            sum= sum+ somma_lista(lista2)   #scorrendo sulla superlista applico la funzione sooma_lista a tutte le liste in superlista e l'aggiungo ad una variabile
            
    print(sum)
                 
        
    



scelta=int(input("ciao cosa vuoi fare?\n1.inserire un numero e farne il quadrato\n2. fare una somma dei quadrati di una lista"))
lista=[]
superlista=[]
controller=True
controller1=False
match scelta:
    
    case 1:
        
        print(quadrato)
    
    case 2:
       
        while(controller):
           
           lista.append(input("inserisci valore"))
           risposta=input("vuoi inserire altri valori?") 
           if(risposta=="NO"):
               controller=False
        print(somma_lista)
        
    case 3:
        
       quadrato_super(superlista,lista)
                
    
    case _:
        print("uscita sistema")
        controller=False
           
        
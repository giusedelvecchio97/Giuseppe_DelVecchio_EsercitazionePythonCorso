

def funzioneSaluto(nome):
    print("ciao",nome)
    print("benvenuto nel nostro programma")
    
    
    
def somma(a,b):
    return a+b
    
    

var=somma(3,5)
print(var)




#esercizio1

def random(n):
    return random.sample(range(1, 101), 1)


def gioco():
    control=True
    while (control):
        
        num=int(input("inserisci il numero "))
        if(num>random(num)):
            print("numero inserito più alto")
        if(num<random(num)):
            print("numero inserito più basso")
        else:
            print("numero corretto")
            control=False

gioco()
            
#esercizio 2
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b  # Aggiorniamo i valori


def programma():
    num=int(input("inserisci un numero"))
    fibonacci(num)



programma()
    

         
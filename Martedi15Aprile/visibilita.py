n=10


def funzione_esterna():
    
    n=5
    print("numero dentro funzione esterna ",n)
    
    
    def funzione_interna():
        
        nonlocal n
        n=3
        print("numero dentro funzione",n)
        
    
    funzione_interna()
    
    
print("numero del main (globale)",n)  #stampa 10
funzione_esterna()  #stampa prima 5, poi 3
print("numero nel main dopo la chiamata",n) #stampa 10 di nuovo
    
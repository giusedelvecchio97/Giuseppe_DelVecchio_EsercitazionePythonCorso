
class Libro():
    
    
    def __init__(self,nome,autore,pagine):
        
        self.nome=nome
        self.autore=autore
        self.pagine=pagine
        
    
    def stampa_libro(self):
        
        print(f"il libro ha come nome {self.nome}, come autore {self.autore}, numero pagine {self.pagine}")






#classe Biblioteca che contiene una lista di libri con i vari metodi costruttore,aggiunta e stampa dei vari libri
class Biblioteca():
    
    def __init__ (self,lista):
        self.lista=lista
        
        
    
    def aggiungi_libro(self,L1):
        
        self.lista.append(L1)
        
    
    
    def stampa(self):
        
        print(self.lista)
        
       
                
                

#funzione per il case 1 , dell'inserimento nella bibloteca dei libri
def inserimento(Biblioteca1):
    c=True
    lista=[]
    while(c):
        nome=input("inserisci nome libro")
        autore=input("inserisci autore")
        numero=int(input("inserisci numero pagine"))
        Libro1=Libro(nome,autore,numero)
        Biblioteca1.aggiungi_libro(Libro1)
        
        r=input("vuoi continuare a inserire")
        if(r=="NO"):
            
            
            
            c=False
            
            
            
        
  #funzione del case 2 per la stampa dei libri      
def  stampa_libri(Biblioteca1):  
    
    Biblioteca1.stampa()
    
    
    
    




#main
c=True

lista=[]
B1=Biblioteca(lista)
while(c):
    
    scelta=int(input("inserisci cosa vuoi fare : \n 1.Inserire Libro\n2.Stamapare Libro"))
    
    match scelta:
        
        case 1:
            
            inserimento(B1)
            
        case 2:
            
            
            stampa_libri(B1)
            
        case _:
            
            print("addio")
            c=False
            
            
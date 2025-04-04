class Prodotto():     #classe prodotto
    quantita=0
    def __init__(self,nome,costo_prod,prezzo):
        
        self.nome
        self.costo
        self.prezzo
        
    
    def calcola_profitto(self):
        
        return self.prezzo-self.costo_prod
    
    


class Fabbrica():    #classe Fabbrica che conterra lista di tipo prodotto
    
    def __init__(self,prodotti):
        
        self.prodotti=prodotti
    
    #permette di agggiungere un prodotto alla fabbrica,ricerca il prodotto e se è già esistente, ne aumenta solo la quantità
    def aggiungi_prodotto(self,prod):
        
        for i in self.prodotti:
            
            if(i.nome==prod.nome):
                
                i.quantita+=1
            else:        
                self.prodotti.append(prod)
                i.quantita+=1
        
    #funzione di vendita del prodotto permette di ricercare il prodotto, stamparne la quantità e diminuire la quantità in base al valore acquistato, aggiorna la quantità
    def vendi_prodotto(self,nome):
        
       
            
            for i in self.prodotti:
            
                if(i.nome==nome):
                    
                    print("prodotto,trovato")
                    
                    print(i.quantita)
                
                var=int(input("inserisci  la quantità di vendita"))
                
                if(var<=i.quantita):
                    i.quantita-=var
                    break
                else:
                    print("mi dispiace quantità d'acquisto non disponibie, riprova tra 1 giorno")
                
            
             
            
            
            #aggiorna la qantità per il reso, con ricerca e incrememnto di quantità
    def reso_prodotto(self,nome):
        
        for i in self.prodotti:
            if(i.nome==nome):
                i.quantita+=1
                




#funzione di aggiunta del prodotto, inserimento valori del prodotto e agguinta nella Fabbrica
def aggiungi_prodotto(F1):
    c=True
    while(c):
        nome=input("inserisci nome")
        costo=float(input("inserisci costo"))
        prezzo=float(input("inserisci prezzo"))
        
        P1=Prodotto(nome,costo,prezzo)
        
        F1.aggiungi_prodotto(P1)
        
        risposta=input("vuoi inserire altri prodotti?")
        if(risposta=="NO"):
            c=False
    
    
    
    
#calcola il profitto di un prodotto e lo stamopa
def calcola(fabbrica):
    
    nome=("inserisci il nome di cui vuoi calcolare il profitto")
    
    for i in fabbrica:
        
        if(i.nome==nome):
            
            var=i.calcola_profitto()
            print(var)
    
    
    #funzione di vendita del prodotto
def vendi_prodotto(fabbrica) :
    
    
    nome=("inserisci il nome del prodotto da vendere")
    
    fabbrica.vendi_prodotto(nome)

#reso del prodotto funzione
def reso(fabbrica):
    
    nome=("inserisci il nome del prodotto su cui fare il reso")
    
    fabbrica.reso_prodotto(nome)
    
    

#programma con opzioni
fabbrica=[]
F1=Fabbrica(fabbrica)

c=True
while(c):
    
    scelta=int(input("inserisci la tua scelta : \n1.AGGIUNGI PRODOTTO\n2 CALCOLA PROFITTO\n3.VENDI PRODOTTO E STAMPA PROFITTO\5 RESO"))
    
    match scelta:
        
        case 1:
            
            aggiungi_prodotto(F1)
            
        case 2: 
            calcola(F1)
            
        case 3:
            
            vendi_prodotto(F1)
            
        case 4:
            
            reso(F1)
            
        case _:
            
            c=False
    
            
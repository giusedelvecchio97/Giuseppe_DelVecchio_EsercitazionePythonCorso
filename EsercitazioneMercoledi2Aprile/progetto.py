



iscritti=[]
bibloteca=[]
libri=[]
idLibro=[]



def controllo_codice(inserimento_dati):
    
    def wrapper():
        
        flag=False
        c=inserimento_dati()
        if(len(c)!=8):
            print("codice fiscale errato,riprova")
            flag=True
        return flag
    return wrapper
        
@controllo_codice
def inserimento_dati():
    
    cod=input("inserisci codice fiscale")
    
    return cod
    
    
def iscrizione():
    
    while(inserimento_dati()==True):
                print("immetti")


def registrazione(cod,iscritti):
    
    for i in iscritti:
        
        if(cod==i):
            print("utente già loggato")
            
        else:
            iscritti.append(cod)
            print("iscrizione avvenuta")
            
    
    
def ricerca_libro(libri,nome,idLibro):
    
    for i in libri:
        
        
        if(i==nome):
            
            for j in idLibro:
            
                if(j[2]==1):
            
            
                    print("libro trovato,ma occupato")
                else:
                    print("libro libero")
                    j[2]=1
            
        
        else:
            print("libro non presente")


def stampa_libri(libri):
    
    print(libri)           







c=True

while(c):
    
    scelta=input("inserisci la scelta\1.registrarti\2.prenotare un libro\3stampa libri")
    
    match scelta:
        
        case 1:
            
            iscrizione()
                
           
            registrazione(c,iscritti)
            
            
        
        case 2: 
            
            
            libro=input("inserisci nome del libro da ricercare");
            ricerca_libro(libri,libro,idLibro)
        
        
        case 3:
            
            stampa_libri(libri)
            
        case _:
            
            print("Arresto Sistema")
            c=False
            
            
            
            
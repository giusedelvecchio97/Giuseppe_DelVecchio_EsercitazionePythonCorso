

def Utente():
    
    
    def __init__(self,nome,password):
        
        self.nome=nome
        self.password=password
        
        
    def modifica(self,nome1,utenti):
        
        if(self.nome==nome1):
            
            self.nome=nome1
            
    def modifica_password(self,passw):
        
        
       
            
            if(self.password==passw):
            
                self.password=passw
            
    def stampa_utente(self):
        
        print(self.nome,self.password)
        
        


def login(utenti):
        
        nome=input("inserisci nome da cercare")
        
        i=0
        
        for i in utenti:
            
            if(utenti[i]==nome):
                print("utente loggato")
                return False
                
            else:
                print("mi dispece non compari nel sistema")
                return True



def registrazione(utenti):
    
    nome=input("inserisci nome")
    
    c=True
    while(c):
        password=input("inserisci una password con 8 caretteri o più")
        if(len(password)>=8):
            
            
        
    
         Utente1=Utente(nome,password)
         utenti.append(Utente1)
         print("utente registrato")
         c=False
         
         
def modifica_nome(utenti):
    
    nome=input("inserisci nuovo nome")
    
    for i in utenti:
        
        if(i.nome==nome):
            
            i.modifica(nome)
            

         
def modifica_pass(utenti):
    
    c=True
    while(c):
        
        
        
        nome=input("inserisci nome")
        
        
        
        for i in utenti:
            
            if(i.nome==nome):
                
                passw=input("inserisci nuova password")
                
                
                i.modifica_password(passw)
                
                
        
                
                
        
    
       
    
    
    
        
        
            





utenti=[]
c,t=True

while(c):
    
    while(t):
        print("CIAO, BENVENUTO NEL LOGIN")
        
        t=login(utenti)
        
        scelta=int(input("inserisci scelta=\n 1.Modifica nome\n 2.Modifica Password"))
        
        match scelta:
            
            case 1:
                
                modifica_nome(utenti)
                
            
            case 2:
                
                modifica_pass(utenti)
                
            case _:
                
                
                print("uscita dal sistema")
                t=False
                c=False
                
                
    
    
    
    
    
    scelta=int("ciao benvenuto nella registrazione: ")
    
    registrazione(utenti)
    
            
    
    


            
            
        
        
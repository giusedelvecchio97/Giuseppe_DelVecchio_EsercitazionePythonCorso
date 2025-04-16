class Persona:
    
    def __init__(self,nome,eta):
        
        self.__nome=nome
        self.__eta=eta
        
    
    def get_nome(self):
        return self.__nome
    
    def get_eta(self):
        return self.__eta
    
    
    def set_nome(self,nome):
        
        while True:
            if(isinstance(nome,str)):
                self.__nome=nome
                break
            else:
                print("valore sbagliato")
                continue
            
    
    def set_eta(self,eta):
        
        while True:
            if(eta>0 and eta.isdigit()):
                self.__nome=eta
                break
            else:
                print("valore sbagliato")
                continue
            
    def presentazione(self):
        
        print(f" {self.__nome}, {self.__eta}")
            


class Studente(Persona):
    
    def __init__(self,nome,eta,voti):
        
        super().__init(self,nome,eta)
        self.__materia=voti
     
     
     
    def get_media(self):
        
        
        return self.__calcola_media()  
    
     
    
    def __calcola_media(self):
        i=0
        for i in range(len(self.__voti)):
            
            sum+=self.__voti[i]
        
        return sum/len(self.__voti)
    
    
    
    def presentazione(self):
        super().presentazione()
        
        print(f"{self.get_media()}")
        
        


class Professore(Persona):
    
    def __init___(self,nome,eta,materia):
        
        super().__init__(self,nome,materia)
        self.__materia=materia
        
    
    
    def __controlla_materia(self,materia):
        
        while True:
            if(isinstance(materia.str)):
                   
                    break
                

            else: 
                print("valore errato")
                continue
            
        return materia
        
    
    def set_materia(self,materia):
        
        self.__materia=self.__controlla_materia(materia)
        
    
    def get_materia(self):
        
        return self.__materia
    
    def presentazione(self):
        
        super().presentazione()
        print(f"{self.__materia}")
        
    

class Scuola():
    
    def __init__(self):
        
        self.__scuola=[]
    
    def set_scuola(self,studente):
        
        self.__scuola.append(studente)
        
    
    def stampa_scuola(self):
        
        print(self.__scuola)
        
    
    def stampa_media(self):
        
        
        
        for i in range(len(self.__scuola)):
            
            nome=input("inserisci nome")
            
            if(nome==self.__scuola[i].nome):
                
                print(self.__scuola[i].get_media())
                
    
    
    def stampa_materia(self):
        
        nome=input("inserire prof")
        
        for i in range(len(self.__scuola)):
            
            if(nome==self.__scuola[i].nome):
                
                print(self.__scuola[i].get_materia())      
            
            

    
#funzioni main
def aggiungi_studente(scuola):
    
    voto=[]
    while True:
        
        nome=input("inserisci nome ")
        eta=int(input("inserisci eta"))
        c=True
        while(c):
            
            v=int(input("inserire voto"))
            voto.append(v)
            
            risp=input("vuoi inserire ancora ? Si o No")
            
            if(risp=="No"):
            
                c=False
                
        studente=Studente(nome,eta,voto)
        scuola.set(studente)
        
        risp=input("vuoi inserire ancora studenti?")
        if not risp:
            
            break
        else : 
            continue
    
    
def aggiungi_prof(scuola):
    
    while True:
        
        nome=input("inserisci nome ")
        eta=int(input("inserisci eta"))
        materia=input("inserisci materia")
        
        professore=Professore(nome,eta,materia)
        scuola.append(professore)
        
        risp=input("vuoi inserire ancora studenti?")
        
        if not risp:
            
            break
        else : 
            continue
        
        
        
        
        
    
    
    
        
        
            
            
            
            
            
            
            



#main
scuola=Scuola()
while True:
    
    scelta=int(input("Inserisci cosa vuoi fare?\n 1. Gestire studente \n 2. Gestire Professore"))
    
    match scelta:
        
        case 1:
            aggiungi_studente(scuola)
            scuola.stampa_media()
            
        case 2: 
            aggiungi_prof(scuola)
            scuola.stampa_materia()
        
        
        case _:
            
            print("uscita")
            
            break
            
     
           
        
        
    
      
    
   
        
            
            
        
        
       
    
    
        
        
        
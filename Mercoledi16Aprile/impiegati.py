from abc import ABC,abstractmethod


class Impiegato(ABC):
    
    def __unit__(self,nome,cognome,stipendio):
        self.__nome=nome
        self.__cognome=cognome
        self.__stipendio=stipendio
    
    @abstractmethod    
    def get_nome(self):
        
        pass
    
    
    @abstractmethod
    def get_cogn(self):
        
      pass
    
    @abstractmethod
    def get_stipendio(self):
        
       pass
    
    
    @abstractmethod
    def set_nome(self,nome):
        
      pass
    
    @abstractmethod
    def set_cognome(self,cognome):
        
      pass
    
    @abstractmethod
    def set_stipendio(self,stipendio):
        
        pass
    
    
    
    @abstractmethod
    def calcola_stipendio():
        pass
    
    
    @abstractmethod
    def stampa():
        pass
    



class ImpegatoFisso(Impiegato):
    
    
    
    
         
    def get_nome(self):
        
        return self.__nome
    
    def get_cogn(self):
        
        return self.__cognome
    
    def calcola_stipendio(self):
        
        return self.__stipendio
    
    
    def set_nome(self,nome):
        
        while True:
        
            if isinstance(nome,str):
                
                self.__nome=nome
                break
            
            else: print("valore errato")
            continue
            
    
    def set_cognome(self,cognome):
        
        while True:
        
            if isinstance(cognome,str):
                
                self.__nome=cognome
                break
            
            else: print("valore errato")
            continue
    
    
    def set_stipendio(self,stipendio):
        
        
        
            if stipendio >0 :
                
                self.__stipendio=stipendio
                
            
            else: print("valore errato")
            
    
    
    def calcola_stipendio():
        return super().get_stipendio()
    
    
    def stampa(self):
        print(f" {self.__nome},{self.__cognome},{self.__stipendio}")
    
    
    

class ImpiegatoAprovvigione(Impiegato):
    
    
    def __init__(self,nome,cognome,stipendio,vendite):
        
        super().__init__(nome,cognome,stipendio)
        self.__vendite=vendite
        
        
    def get_nome(self):
        
        return self.__nome
    
    def get_cogn(self):
        
        return self.__cognome
    
    def calcola_stipendio(self):
        return self.calcola_stipendio()
    
    def set_nome(self,nome):
        
        while True:
        
            if isinstance(nome,str):
                
                self.__nome=nome
                break
            
            else: print("valore errato")
            continue
            
    
    def set_cognome(self,cognome):
        
        while True:
        
            if isinstance(cognome,str):
                
                self.__nome=cognome
                break
            
            else: print("valore errato")
            continue
    
    
    def set_stipendio(self,stipendio):
        
        while True:
        
            if stipendio >0 :
                
                self.__stipendio=stipendio
                break
            
            else: print("valore errato")
            continue
        
    
    def aggiungi_vendita(self,id):
        
        self.__vendite.append(id)
        
    def get_vendita(self):
        
        return self.__vendite
    
    
    def calcola_stipendio(self):
        
        if len(self.__vendite )%4==0:
            
            self.__stipendio+= (len(self.__vendite/4)*self.__stipendio/10)
            
         
        return self.__stipendio   
    
    
    def stampa(self):
        
      
          print(f" {self.__nome},{self.__cognome},{self.__stipendio},{self.__vendite}")
    
            
     
     




def funzione_main():
    
    stip=0
    vendite=["12345","45678","5678","26758"]

    impiegato=Impiegato("Marco","Delio",2567) 
    impiegApp=ImpiegatoAprovvigione("Andrea","De Carolis",2886,vendite) 
        
    scelta=int(input("Ciao, cosa vuoi fare ?\n 1. Stampa info impegato\n2.stampa info impiegato Approvvigionamento"))
        
    match scelta:
            case 1:
                
                stip=impiegato.calcola_stipendio()
                print(stip)
                impiegato.stampa()
                
            
            case 2:
                while True:
                
                    scelta1=input("vuoi aggiungere una vendita?")
                    
                    
                
                    if scelta1=="Si":
                            
                            vend=input("inserisci id vendita")
                            
                            impiegApp.aggiungi_vendita(vend)
                            continue
                        
                    else :
                        break
                        
                
                stip=impiegApp.calcola_stipendio()
                print(stip)
                impiegApp.stampa()
            
            
            case _:
                print("ciao")
                
                

                
                
            
        
    
    

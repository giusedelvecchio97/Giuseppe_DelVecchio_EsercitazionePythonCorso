from abc import ABC,abstractmethod

class Animale(ABC):
    @abstractmethod
    def muovi(self):
        pass
    
class Cane(Animale):
    
    def muoi(self):
        print("corro")
        
class Gatto(Animale):
    
    def muovi(self):
        
        print("salto")
    
    
    
#esempio pratico
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
    

class Rettangolo(Forma):
    
    def __init__(self,larghezza,altezza):
        self.larghezza=larghezza
        self.altezza=altezza
        
    
    def area(self):
        return self.altezza*self.larghezza
    
    def perimetro(self):
        return 2*(self.larghezza + self.altezza)
    
    



class Veicolo():
    
    def __init__(self,marca,modello):
        
        self.marca=marcaself.modello=modello
        
        
    def mostra_info(self):
        
        print(f"Veicolo marca {self.marca}, modello{self.modello}")
        
        

class DotazioniSpeciali():
    
    def __init__(self,dotazioni):
        
        self.dotazioni=dotazioni
        
    
    def mostra_dotazioni(self):
        print(f"Dotazioi speciali: {self.dotazioni}")
        
        


class AutomobileSportiva(Veicolo,DotazioniSpeciali):
    
    def __init__(self,marca,modello,dotazioni,cavalli):
        
        Veicolo.__init__(self,marca,modello)
        DotazioniSpeciali.__init__(self,dotazioni)
        self.cavalli=cavalli
        
        
    
    def mostra_informazioni(self):
        
        super.mostra_info()
        print(f" Potenza:{self.cavali}")
        
        self.mostra_dotazioni
        
        



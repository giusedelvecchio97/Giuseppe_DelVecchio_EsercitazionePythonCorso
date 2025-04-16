class Animale():
    
    def __inti__(self,nome):
        self.nome=nome
        
    def parla(self):
        print(f" {self.nome} fa un suono generico")
        
    
class Cane(Animale):
    
    
    def parla(self):
        print(f"{self.nome} abbaia!")
        
        
animale_gen=Animale("animale generico")

cane=Cane("Fido")

animale_gen.parla()
cane.parla()
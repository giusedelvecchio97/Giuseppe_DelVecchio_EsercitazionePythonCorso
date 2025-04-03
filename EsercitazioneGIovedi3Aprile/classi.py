
class Automobile():
    
    num_ruote=4
    
    def _init_(self,marca,modello):
        
        self.marca=marca
        self.modello=modello
        
        
    def stampa(self):
        print("automobile è una",self.marca,self.modello)
        


Auto=Automobile("FIAT","a benzina")
print(Auto.marca)
print(Auto.modello)
Auto.stampa



#metodo statico

class Calcolatore():
    numero=0
    
    def _init_(self):
        
        Calcolatore.numero+=1
    
    @staticmethod
    def somma(a,b):
        return a+b
    
    
    @classmethod
    def numero_istanze(cls):
        
        print(f"sono state create {cls.numero} istanze")
        
    

r=Calcolatore.somma(5,3)
print(r)

C=Calcolatore()
Calcolatore.numero_istanze()
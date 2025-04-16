class Animale:
    
    def emetti_suono(self):
        print("Questo animale fa ")
        
class Cane(Animale):
    def emetti_suono(self):     #overriding del metodo
        print("Bau")
        
class Gatto(Animale):
    def emetti_suono(self):   #overriding del metodo 
        
        print("Miao")
        


def fai_parlare(animale):
    
    print(animale.emetti_suono())


cane=Cane()
gatto=Gatto()

fai_parlare(gatto)
fai_parlare(cane)




#metodi variadici

class Stampa:
    def mostr(self, a=None,b=None):
        
        if a is not None and b is not None:
            print(a+b)
        elif a is not None:
            print(a)
            
        else:
            print("Niente da mostrare")
            
            

class Cerchio:
    
    def disegna(self):
        
        print("Disegna un cerchio")
        
class Rettangolo:
        def disegna(self):
            print("disegna")


  
def fai(a):
    
    a.disegna()
  
            
rettangolo=Rettangolo()
cerchio=Cerchio()


fai(rettangolo)
fai(cerchio)



        
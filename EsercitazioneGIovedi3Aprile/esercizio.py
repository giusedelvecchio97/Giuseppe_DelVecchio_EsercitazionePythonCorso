
class Punto():
    
    
    def _init_ (self,x,y):
        self.x
        self.y
        
    
    def muovi(self,dx,dy):
        self.x=dx
        self.y=dy
        
    
    def calcola_distanza(self,dx,dy):
        
        coord=[]
        coord[0]=dx-self.x
        coord[1]=dy-self.y
        
        
        return coord
    
    
dx=6
dy=9
P=Punto(6,9)

t=10
r=12

P.muovi(2,5)
lista= P.calcola_distanza(t,r)
print(lista)




#extra 

class Piano():
    
    def _init_ (self,lista):
        self.lista=lista
        
    
    
    def ricerca(self,Punto):
        
        for v in lista:
            
            if(Punto in lista):
                
                print("Punto presente")
            else:
                
                lista.append(Punto)
                print("oggetto salvato")
        


i=0
for i in range(10):
    
   x=int(input("inserisci coordinate x"))
   y=int(input("inserisci coordinate y"))
   lista[i]=Punto(x,y) 
    

Cartesiano=Piano(lista)


print("adesso ricerca un punto")
x=int(input("inserisci coordinate x"))
y=int(input("inserisci coordinate y"))
P1=Punto(x,y)
Cartesiano.ricerca(P1)
                
            
                



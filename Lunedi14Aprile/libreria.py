
import libro as l
Libro=l.Libro()

titolo=Libro.titolo
autore=Libro.autore
isbn=Libro.isbn



class Libreria():
    catalogo=[] 
    
    def __unit__(self):
        
        self.catalogo=[]
        
    def aggiungi_libro(self, Libro):
        i=0
        
        for i in range(len(self.catalogo)):
            
            if(Libro.isbn==self.catalogo[i].nome):
                print("libro già esistente")
                break
            
        else: 
            
            self.catalogo.append(Libro)
            print("libro inserito")
            
            
    
    
    def cerca_titolo(self,titolo):
        
        lista=[]
        i=0
        for i in range(len(self.catalogo)):
            
            if(titolo==self.catalogo[i]):
                
                lista.append(self.catalogo[i])
        
        
        print(lista)
        
    
    
    def rimuovi_libro(self,isbn):
        
        
         i=0
         
         for i in range(len(self.catalogo)):
             
             if(isbn==self.catalogo[i].isbn):
                 
                 self.catalogo.remove(isbn)
                 
                 print("libro eliminato")
                 
                 
    def stampa_libro(self):
        
        i=0
        [i.stampa_libro for i in self.catalogo]
        
        
    
    
    
                 
            
        
        
            
        
        
            
            
        
        
        
        
        
        
        
        
            
        
        
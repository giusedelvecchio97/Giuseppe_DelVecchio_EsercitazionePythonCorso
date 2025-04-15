class ContoBancario:
    
    def __init__(self):
        self.__titolare
        self.__saldo
        
    
    def set_conto(self,titolare,saldo):
        
        c=True
        
        while(c):
            if(isinstance(titolare,str) and saldo>0):
                
                self.__titolare=titolare
                self.__saòdo=saldo
                c=False
            
            else: print("valori inseriti non corretti")
            
    
    
    def deposita(self,saldo):
        
        if(saldo>0):
            
            self.__saldo=self.__saldo+saldo
            
    
    def get_conto(self):
        
        return self.__conto
    
    
    
    def preleva(self,conto):
        
         return get_conto()
            
    
    
    
                
            
        
        
        
        
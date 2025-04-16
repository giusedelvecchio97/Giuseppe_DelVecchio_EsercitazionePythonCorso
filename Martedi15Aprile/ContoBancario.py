class ContoBancario:
    
    def __init__(self):
        self.__titolare="null"
        self.__saldo="null"
        
    
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
            
    
    def get_titolare(self):
        
        return self.__titolare
    
    def get_conto(self):
        
        return self.__saldo
    
    
    
    def preleva(self,conto):
        c=True
        while(c):
            if(conto>0):
                
                self.__conto-=conto
                c=False
                
            
            else:
                print("importo inserito non corretto")
                
                
    
        
    
    
   
            
    
    
    
                
            
        
        
        
        
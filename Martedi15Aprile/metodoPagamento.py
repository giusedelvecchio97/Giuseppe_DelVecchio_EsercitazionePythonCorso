class MetodoPagamento():
    
    
    def __init__(self,iban,saldo):
        
        self.__iban=iban
        self.saldo=saldo
        
            
        
    
    def effetua_pagamento(self,importo):
        
        self.__saldo-=importo
        
    
    
class CartaDiCredito(MetodoPagamento):
    
    def __init__(self,iban,saldo,codice):
         super().__init__(self,iban,saldo)
         self.__codice=codice
         
    
    def effettua_pagamento(self,importo,codice):
        
        if(codice==self.__codice):
            self.saldo-=importo
        else:
            print("codice errato")


class Paypal(MetodoPagamento):
    
    def __init__(self,iban,saldo,email,password):
         super().__init__(self,iban,saldo)
         self.__email=email
         self.__password=password
         
    
    def effettua_pagamento(self,importo,email,password):
        
        if email==self.__email and password==self.__passsword:
            self.saldo-=importo
        else:
            print("credenziali errate")
    
    


class Bonifico(MetodoPagamento):
    
    def __init__(self,iban,saldo,codice,password):
         super().__init__(self,iban,saldo)
         self.__codice=codice
         self.__password=password
         
    
    def effettua_pagamento(self,importo,codice,password):
        
        if codice==self.__codice and password==self.__passsword:
            self.saldo-=importo
        else:
            print("credenziali errate")
            




class GestorePagamenti:
    def __init__(self, carta, paypal, bonifico):
        self.carta = carta
        self.paypal = paypal
        self.bonifico = bonifico

    def paga_con_carta(self, importo, codice):
        self.carta.effettua_pagamento(importo, codice)

    def paga_con_paypal(self, importo, email, password):
        self.paypal.effettua_pagamento(importo, email, password)

    def paga_con_bonifico(self, importo, codice, password):
        self.bonifico.effettua_pagamento(importo, codice, password)
        
        
       
    
    
    
    
    
 
    
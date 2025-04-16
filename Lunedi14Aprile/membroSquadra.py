class MembroSquadra():
    
    
    def __init__(self,nome,eta):
        
        self.nome=nome 
        self.eta=eta
        
        
        
    def descrivi(self):
        
        print(f"nome={self.nome}, eta={self.eta}")
        
        


class Giocatore(MembroSquadra):
    
    def __init__(self,nome,eta,num,ruolo,rate):
        
        super().__init__(self,nome,eta)
        self.num=num
        self.ruolo=ruolo
        self.rate=rate
        
    
    def gioca_partita(self):
        
        match(self.ruolo):
            
            case "attaccante":
                
                print("il giocatore può attaccare la profondità, inserirsi, calciare in porta e far goal")
            
            case "centrocampista":
                print("il giocatore deve aiutare in difesa e nella fase offensiva,aiutando gli attaccanti")
            
            case "difensore":
                
                print("il giocatore deve marcare gli attcanti e difendere la porta")
            case "portiere":
                
                print("il giocatore deve proteggere la porta ")
            case _:
                
                print("errore")
        
    


class Allenatore(MembroSquadra):
    
    def __init__(self,nome,eta,esperienza,rate):
        
        super().__init__(self,nome,eta)
        self.esperienza=esperienza
        self.rate=rate
        
    
    
    def dirige_allenamento(self):
        
        match(self.rate):
            
            case 1:
                print("l'allenatore conduce gli allenamenti in maniera più fisica e poco tecnica")
            
            case 2:
                print(" conduce l'allenamento in maniera perfetta , tattica e tecnica ")
                
            case _:
                print("errore")
                
                
class Assistente(MembroSquadra):
    
    
    def __init__(self,nome,eta,esperienza,rate):
        
        super.__init__(self,nome,eta)
        self.esperienza=esperienza
        self.rate=rate
        
    
    def supporta_team(self):
        
        print(f"contribuisce con le sue qualità e le sue competenze a far salire il livello della squadra ")
        


class Fisioterapista(Assistente):
    
    def __init__(self, nome, eta, esperienza, rate,laurea):
        super().__init__(nome, eta, esperienza, rate)
        self.laurea=laurea
        
    
    
    def supporta_team(self):
         super().supporta_team()
         print(f" grazie alle sue lauree {self.laurea} ed esperienza {self.esperienza}")
        
        
        
        

class Analista(Assistente):
    
    def __init__(self, nome, eta, esperienza, rate,laurea,storico):
        super().__init__(nome, eta, esperienza, rate)
        self.laurea=laurea
        self.storico=storico
        self.final_rate=self.rate+self.storico
        self.rate=rate+self.final_rate
    
    
    def supporta_team(self):
         super().supporta_team()
         print(f" grazie alle sue lauree {self.laurea} ed esperienza {self.esperienza}")
         









                
                
            
            
        
        
        
    
                
                
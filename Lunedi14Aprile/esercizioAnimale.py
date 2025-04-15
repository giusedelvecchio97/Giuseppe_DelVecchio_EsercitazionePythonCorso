class Animale():
    
    def __init__(self,nome,eta):
        
        self.nome=nome
        self.eta=eta
        
    def fai_suono(self):
        
        print(f"{self.nome} fa un suono")
        
        

class Leone(Animale):
    
    def __init__(self,nome,eta,tipo,spess_artigli):
        
        Animale.__init__(self,nome,eta)
        self.tipo=tipo
        self.spess_artigli=spess_artigli
        
    def fai_suono(self):
        
        super.fai_suono()
        print(f"grrr")
        
    
    def caccia(self):
        
        print(f" il {self.nome} si abbassa per poi cacciare")
        
    
    def mostra_artigli(self):
        
        print(self.spess_artigli)    
        



class Pinguino(Animale):
    
    def __init__(self,nome,eta,tipo,lung_collo):
        
        Animale.__init__(self,nome,eta)
        self.tipo=tipo
        self.lung_collo=lung_collo
        
    def fai_suono(self):
        
        super.fai_suono()
        print(f" BEEE")
        
    
    def  mostra_lunghezza(self):
        
        print(f" la lunghezza è {self.lung_collo}")
        



class Giraffa(Animale):
    
    def __init__(self,nome,eta,tipo,lung_pinne):
        
        Animale.__init__(self,nome,eta)
        self.tipo=tipo
        self.lung_pinne=lung_pinne
        
    def fai_suono(self):
        
        super.fai_suono()
        print(f" aaaaaaaaaaaa")
        
    
    def  lung_pinne(self):
        
        print(f" la lunghezza è {self.lung_pinne}")    
    
    


leone=Leone(Animale("King","8","mammifero","7 cm"))       
pin=Pinguino(Animale("Marco","8","mammifero","30 cm")) 
giraffa=Giraffa(Animale("Elsa","8","mammifero","10 cm"))  






  
 
conn = mysql.connector.connect(
    host="localhost",
    user="tuo_utente",
    password="Zanett44C!",
    
)


cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS zoo_db")

print(" Database 'zoo_db' creato o già esistente.")

# Chiudi la connessione iniziale
cursor.close()
conn.close()   


conn = mysql.connector.connect(
    host="localhost",
    user="tuo_utente",
    password="Zanett44C!",
    databse="zoo_db"
    
)


cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS animali (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    eta INT,
    tipo VARCHAR(50)
)
""")

# Leone
cursor.execute("""
CREATE TABLE IF NOT EXISTS leoni (
    id INT AUTO_INCREMENT PRIMARY KEY,
    animale_id INT,
    spess_artigli VARCHAR(50),
    FOREIGN KEY (animale_id) REFERENCES animali(id)
)
""")

# Pinguino
cursor.execute("""
CREATE TABLE IF NOT EXISTS pinguini (
    id INT AUTO_INCREMENT PRIMARY KEY,
    animale_id INT,
    lung_collo VARCHAR(50),
    FOREIGN KEY (animale_id) REFERENCES animali(id)
)
""")

# Giraffa
cursor.execute("""
CREATE TABLE IF NOT EXISTS giraffe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    animale_id INT,
    lung_pinne VARCHAR(50),
    FOREIGN KEY (animale_id) REFERENCES animali(id)
)
""")

conn.commit()


def inserisci_animale(animale, specifica_valore, tabella_secondaria, colonna_secondaria):
    # Inserisci nella tabella animali
    cursor.execute(
        "INSERT INTO animali (nome, eta, tipo) VALUES (%s, %s, %s)",
        (animale.nome, animale.eta, animale.tipo)
    )
    animale_id = cursor.lastrowid

    # Inserisci nella tabella specifica
    query = f"INSERT INTO {tabella_secondaria} (animale_id, {colonna_secondaria}) VALUES (%s, %s)"
    cursor.execute(query, (animale_id, specifica_valore))
    conn.commit()

# Inserisci tutti
inserisci_animale(leone, leone.spess_artigli, "leoni", "spess_artigli")
inserisci_animale(pinguino, pinguino.lung_collo, "pinguini", "lung_collo")
inserisci_animale(giraffa, giraffa.lung_pinne, "giraffe", "lung_pinne")



    






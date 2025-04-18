from abc import ABC, abstractmethod

# Classe astratta per una Forma geometrica
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

# Classe per il Cerchio
class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return 3.14159 * self.raggio ** 2  

    def perimetro(self):
        return 2 * 3.14159 * self.raggio  

# Classe per il Rettangolo
class Rettangolo(Forma):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza

    def perimetro(self):
        return 2 * (self.base + self.altezza)

# Classe per il Triangolo
class Triangolo(Forma):
    def __init__(self, base, altezza, lato1, lato2, lato3):
        self.base = base
        self.altezza = altezza
        self.lato1 = lato1
        self.lato2 = lato2
        self.lato3 = lato3

    def area(self):
        return 0.5 * self.base * self.altezza

    def perimetro(self):
        return self.lato1 + self.lato2 + self.lato3

# Funzione per trovare la forma con area/perimetro maggiore
def confronta_forme(forme, tipo="area"):
    forma_max = None
    valore_max = None

    for forma in forme:
        if tipo == "area":
            valore = forma.area()
        elif tipo == "perimetro":
            valore = forma.perimetro()
        else:
            print("Tipo non valido")
            return

        # Confronta il valore corrente con il valore massimo
        if valore_max is None or valore > valore_max:
            valore_max = valore
            forma_max = forma

    if tipo == "area":
        print(f"La forma con l'area maggiore è: {forma_max.__class__.__name__}")   #semplicità per il ritorno del nome della classe nella stampa 
        print(f"Area: {forma_max.area()}")
    elif tipo == "perimetro":
        print(f"La forma con il perimetro maggiore è: {forma_max.__class__.__name__}")
        print(f"Perimetro: {forma_max.perimetro()}")


# Menu per l'utente
def menu():
    forme = []
    
    while True:
        print("\nMenu:")
        print("1. Aggiungi un Cerchio")
        print("2. Aggiungi un Rettangolo")
        print("3. Aggiungi un Triangolo")
        print("4. Confronta le forme per Area")
        print("5. Confronta le forme per Perimetro")
        print("6. Esci")
        
        scelta = input("Scegli un'opzione: ")

        match scelta:
            case "1":
                raggio = float(input("Inserisci il raggio del cerchio: "))
                cerchio = Cerchio(raggio)
                forme.append(cerchio)
                print(f"Cerchio aggiunto con area: {cerchio.area()} e perimetro: {cerchio.perimetro()}")
            
            case "2":
                base = float(input("Inserisci la base del rettangolo: "))
                altezza = float(input("Inserisci l'altezza del rettangolo: "))
                rettangolo = Rettangolo(base, altezza)
                forme.append(rettangolo)
                print(f"Rettangolo aggiunto con area: {rettangolo.area()} e perimetro: {rettangolo.perimetro()}")
            
            case "3":
                base = float(input("Inserisci la base del triangolo: "))
                altezza = float(input("Inserisci l'altezza del triangolo: "))
                lato1 = float(input("Inserisci il primo lato del triangolo: "))
                lato2 = float(input("Inserisci il secondo lato del triangolo: "))
                lato3 = float(input("Inserisci il terzo lato del triangolo: "))
                triangolo = Triangolo(base, altezza, lato1, lato2, lato3)
                forme.append(triangolo)
                print(f"Triangolo aggiunto con area: {triangolo.area()} e perimetro: {triangolo.perimetro()}")
            
            case "4":
                confronta_forme(forme, tipo="area")
            
            case "5":
                confronta_forme(forme, tipo="perimetro")
            
            case "6":
                print("Uscita in corso...")
                break

            case _:
                print("Opzione non valida. Riprova.")

# Avvio del programma
menu()

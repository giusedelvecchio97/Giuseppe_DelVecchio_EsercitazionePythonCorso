class Veicolo:
    def __init__(self, marca, anno, targa, revisione):   #costruttore della classe veicolo, con relativo passaggio di parametri di inizializzazione
        self._marca = marca
        self._anno = anno
        self._targa = targa
        self._revisione = revisione

    # Getter e Setter , per accedere e settare i vari attributi della classe
    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_anno(self):
        return self._anno

    def set_anno(self, anno):
        self._anno = anno

    def get_targa(self):
        return self._targa

    def set_targa(self, targa):
        self._targa = targa

    def get_revisione(self):
        return self._revisione

    def set_revisione(self, revisione):
        self._revisione = revisione

    def descrivi(self):
        return f"Marca: {self._marca}, Anno: {self._anno}, Targa: {self._targa}, Revisione: {self._revisione}"


# === Sottoclassi ===

class Auto(Veicolo):
    def __init__(self, marca, anno, targa, revisione, numero_porte):
        super().__init__(marca, anno, targa, revisione)           #super() --> metodo che permette di richiamare il costruttore del padre per ampliarlo
        self.numero_porte = numero_porte

    def descrivi(self):
        return f"[AUTO] {super().descrivi()}, Porte: {self.numero_porte}"


class Moto(Veicolo):
    def __init__(self, marca, anno, targa, revisione, cilindrata):
        super().__init__(marca, anno, targa, revisione)
        self.cilindrata = cilindrata

    def descrivi(self):
        return f"[MOTO] {super().descrivi()}, Cilindrata: {self.cilindrata} cc"


class Camion(Veicolo):
    def __init__(self, marca, anno, targa, revisione, capacita_carico):
        super().__init__(marca, anno, targa, revisione)
        self.capacita_carico = capacita_carico

    def descrivi(self):
        return f"[CAMION] {super().descrivi()}, Carico massimo: {self.capacita_carico} kg"


# === Funzione per il menu ===

def crea_veicolo():       #funzione del programma, permette di creare e istanziare i vari oggetti in base alla scelta del menu interno
    print("\nSeleziona tipo di veicolo:")
    print("1. Auto")
    print("2. Moto")
    print("3. Camion")
    scelta = input("Scelta (1/2/3): ")

    marca = input("Marca: ")
    while True:
        try:
            anno = int(input("Anno di immatricolazione: "))        #gestione delle eccezioni, ci permettono di ciclare col while in base alla correttezza dell'input e di getsire anomalie in base all'input inserito
            break
        except ValueError:
            print("Inserisci un numero valido.")
    targa = input("Targa: ")
    revisione = input("Revisione effettuata? (s/n): ").lower() == 's'

    if scelta == "1":
        numero_porte = int(input("Numero porte: "))
        return Auto(marca, anno, targa, revisione, numero_porte)
    elif scelta == "2":
        cilindrata = int(input("Cilindrata (cc): "))
        return Moto(marca, anno, targa, revisione, cilindrata)
    elif scelta == "3":
        capacita = int(input("Capacità di carico (kg): "))
        return Camion(marca, anno, targa, revisione, capacita)
    else:
        print("Scelta non valida.")
        return None


# === Programma principale ===

def main():
    veicoli = []

    while True:
        print("\n--- Menu ---")
        print("1. Aggiungi veicolo")
        print("2. Mostra veicoli")
        print("3. Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            veicolo = crea_veicolo()
            if veicolo:
                veicoli.append(veicolo)
                print("Veicolo aggiunto con successo!")
        elif scelta == "2":
            print("\n--- Elenco Veicoli ---")
            for v in veicoli:
                print(v.descrivi())  # Metodo polimorfico
        elif scelta == "3":
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida. Riprova.")


#avvio del programma
main()

# Classe base
class UnitaMilitare:
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati

    def muovi(self):
        print(f"{self.nome} si sta muovendo con {self.numero_soldati} soldati.")

    def attacca(self):
        print(f"{self.nome} attacca il nemico!")

    def ritira(self):
        print(f"{self.nome} si sta ritirando strategicamente.")


# Classi derivate con override
class Fanteria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def muovi(self):
        super().muovi()
        print(f"{self.nome} si muove a piedi in formazione.")

    def attacca(self):
        super().attacca()
        print(f"{self.nome} usa fucili e baionette nell’attacco.")

    def ritira(self):
        super().ritira()
        print(f"{self.nome} si ritira coprendosi con fumo o trincee.")

    def costruisci_trincea(self):
        print(f"{self.nome} costruisce trincee per la difesa temporanea.")


class Artiglieria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def muovi(self):
        super().muovi()
        print(f"{self.nome} si muove trascinando i pezzi di artiglieria.")

    def attacca(self):
        super().attacca()
        print(f"{self.nome} spara colpi a lunga distanza.")

    def ritira(self):
        super().ritira()
        print(f"{self.nome} ritira l'artiglieria verso una nuova posizione.")

    def calibra_artiglieria(self):
        print(f"{self.nome} calibra i pezzi di artiglieria per maggiore precisione.")


class Cavalleria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def muovi(self):
        super().muovi()
        print(f"{self.nome} si muove rapidamente a cavallo.")

    def attacca(self):
        super().attacca()
        print(f"{self.nome} carica il nemico con velocità e sorpresa.")

    def ritira(self):
        super().ritira()
        print(f"{self.nome} si ritira a cavallo velocemente.")

    def esplora_terreno(self):
        print(f"{self.nome} esplora il terreno per raccogliere informazioni.")


class SupportoLogistico(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def muovi(self):
        super().muovi()
        print(f"{self.nome} trasporta i rifornimenti.")

    def attacca(self):
        super().attacca()
        print(f"{self.nome} difende i rifornimenti in caso di attacco.")

    def ritira(self):
        super().ritira()
        print(f"{self.nome} evacua l’equipaggiamento in sicurezza.")

    def rifornisci_unita(self):
        print(f"{self.nome} si occupa del rifornimento e della manutenzione delle truppe.")


class Ricognizione(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def muovi(self):
        super().muovi()
        print(f"{self.nome} si muove silenziosamente per osservare il nemico.")

    def attacca(self):
        super().attacca()
        print(f"{self.nome} ingaggia solo se strettamente necessario.")

    def ritira(self):
        super().ritira()
        print(f"{self.nome} si ritira rapidamente senza farsi notare.")

    def conduci_ricognizione(self):
        print(f"{self.nome} conduce una missione di sorveglianza.")


# ControlloMilitare
class ControlloMilitare:
    def __init__(self):
        self.unita_registrate = {}  # chiave: nome unità, valore: oggetto

    def registra_unita(self, unita):
        self.unita_registrate[unita.nome] = unita
        print(f"Registrata unità: {unita.nome}")

    def mostra_unita(self):
        print("Unità registrate:")
        for unita in self.unita_registrate.values():
            print(f"- {unita.nome})")

    def dettagli_unita(self, nome_unita):
        unita = self.unita_registrate.get(nome_unita)
        if unita:
            print(f"Dettagli per {nome_unita}:")
           
            print(f"  Numero soldati: {unita.numero_soldati}")
        else:
            print(f"Nessuna unità trovata con il nome '{nome_unita}'.")


# Esercito
class Esercito:
    def __init__(self):
        self.controlli = {}
        self.id_counter = 0

    def registra_esercito(self, controllo):
        self.controlli[self.id_counter] = controllo
        print(f"Registrato controllo con ID: {self.id_counter}")
        self.id_counter += 1

    def mostra_eserciti(self):
        print("Eserciti registrati:")
        for id, controllo in self.controlli.items():
            print(f"- Controllo ID {id} con {len(controllo.unita_registrate)} unità.")


# Creazione unità
f = Fanteria("Fanteria Alfa", 100)
a = Artiglieria("Artiglieria Bravo", 50)
c = Cavalleria("Cavalleria Charlie", 30)

# Controllo militare
cm = ControlloMilitare()
cm.registra_unita(f)
cm.registra_unita(a)
cm.registra_unita(c)

cm.mostra_unita()
cm.dettagli_unita("Artiglieria Bravo")

# Azioni
f.muovi()
a.attacca()
c.ritira()
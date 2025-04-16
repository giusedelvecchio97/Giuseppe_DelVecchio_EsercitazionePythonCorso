stringa = "che bella giornata"
diz = {}

for var in stringa:
    if var in diz:
        diz[var] += 1
    else:
        diz[var] = 1

print(diz)




stringa = "banana"
lista = list(stringa)
dizi = {}

for i in lista:
    dizi.setdefault(i, lista.count(i))

print(dizi)






registro={} 




def stampa_medie(dizionario_alunni):
    for nome, voti in dizionario_alunni.items():
        if voti:  
            media = sum(voti) / len(voti)
            print(f"{nome}: media = {media:.2f}")
        else:
            print(f"{nome}: nessun voto inserito")


alunni = {}
c=True

while(c):
    nome = input("Inserisci il nome dell'alunno: ")
    voti_input = input("Inserisci i voti separati da spazio: ")  
    voti = [float(voto) for voto in voti_input.split()]
    alunni[nome] = voti
    
    risp=input("vuoi inserire ancora")
    if risp=="NO":
        c=False

print("\nDizionario degli alunni e voti:")
print(alunni)

stampa_medie(alunni)



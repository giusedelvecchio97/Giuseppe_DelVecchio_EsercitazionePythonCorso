import numpy as np

matrice1 = np.random.randint(10, 51, size=(4, 4))
print("Matrice 4x4:")
print(matrice1)



righe = [0, 1, 2, 3]
colonne = [1, 3, 2, 0]

# Fancy indexing
elementi_selezionati = matrice1[righe, colonne]
print("\nElementi selezionati con fancy indexing:")
print(elementi_selezionati)



elementi3 = matrice1[1::2]
print(" matrice con righe dispari")
print(elementi3)


print("elementi incrementati per scalare 10")
elementi_10=matrice1+10
print(elementi_10)
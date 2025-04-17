import numpy as np


matrice = np.arange(1, 26).reshape(5, 5)
colonna_2 = matrice[:, 1]
print("Colonna 2:", colonna_2)

riga_3 = matrice[2, :]
print("Riga 3:", riga_3)
diag=np.diag(matrice)
print(sum(diag))





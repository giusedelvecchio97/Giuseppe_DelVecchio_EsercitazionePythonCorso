import numpy as np

#inversa
matrice=np.array([2,3],[5,6])

inversa=np.linalg.inv(matrice)
print(inversa)

#norma
v=np.array([3,4])

norm_v=np.linalig.norm(v)
print(norm_v)



#broadcasting
arr=np.array([1,2,3,4])  #aggiunge 10 ad ogni elemento
scalar=10

result=arr+scalar
print(result)
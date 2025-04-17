import numpy as np


arr=np.array([1,2,7,8])

print("Forma dell'array",arr.shape)
print("Dimensione dell'array", arr.ndim)
print("Tipo dati", arr.dtype)
print("Numero elementi", arr.size)
print("somma degli elementi",arr.sum())
print("media degli elementi",arr.mean())
print("valore massimo ", arr.max())
print("Indice del valore massimo",arr.argmax())



#dtype
arr=np.array([1,3,4], dtype='int32') #obbligo di assegnare il tipo int32
print(arr.type)  #otuput= int32


#shape
print(np.shape)   #output (2,3)

#arange
arr=np.arange(10)

print(arr)  #output [0,1,2,3,....9]


#reshape 
arr=np.arange(6)

reshaped_arr=arr.reshape((2,3))
print(reshaped_arr)      #output  [[0,1,2]  [3 4 5]]


#indexing
print(arr[0])

#slicing
print(arr[1:3])   #siccome è monodimensionale fa dalla colonna 1 alla 2

#boolean indexing
print(arr[arr>1])


#slicing multidimensionale
arr2d=np.array([1,3,4,5],[3,4,5,8])

print(arr2d[1:3])  #slicing sulle righe, stampera dalla riga 1 alla 2

#slicing sullle colonne

print(arr2d[:, 1:3])   #stampera le colonne con indice colonna da 1 a 2


#slicing misto
print(arr2d[1:,1:3])    # dalla 1 a n-1 quindi 2


#slicing con passo
print(arr[1:3:2])



#omettere start and stop
print(arr[:3])    # andrà da indice 0 a 2

print(arr[1:])  #andrà da indice 1 a n-1

#indici negativi
print(arr[-5:])  
print(arr[:-5]) #parte dall'inizio e ne prende 5



#fancy indexing

indici=np.array([1,3])   # scelgo io quale elementi stampare in base agli indici
print(arr[indici])

indici=[0,5]
print(arr[indici])   


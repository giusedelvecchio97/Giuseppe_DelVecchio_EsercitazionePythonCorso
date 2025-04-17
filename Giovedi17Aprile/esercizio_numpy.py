import numpy as np

arr=np.arange(10,50)
print(arr.dtype)
arr=arr.astype(dtype='float64')

print(arr.ndim)




arr1d=np.random(10,51)

print(arr1d[0:10])
print(arr1d[-5:])
print(arr1d[5:15])
print(arr1d[:51:3])

copia=arr1d
copia[5:9]=99

print(copia)










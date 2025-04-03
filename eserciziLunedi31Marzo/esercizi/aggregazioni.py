
#creazione tupla
punto=(3,4)
valori=(1,4,"Carla")


print(punto[0])
punto=(6,7)   #posso inizializzarla completamente 
punto=() 

x,y=punto
print(x,y)

#INSIEMI

set={1,3,4,5}
set2={1,1,3,4,4}
print(set2)

print(set.union(set2))
print(set.intersection(set2))
print(set.difference(set2))
print(set.symmetric_difference(set2))
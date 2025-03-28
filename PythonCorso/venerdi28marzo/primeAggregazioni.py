nomi=["Alice","Marco","Giuseppe"]
num=[1,5,9,8]
misto=[8, 9 ,"Alice",6.8,"Guido",True]
num[2]=10

print(nomi[2])
print(misto[3])
print(num)

nomi.append("Guido")
num.remove(8)
nomi.sort()
misto.insert(2,7)
nomi.reverse()
print(nomi)
print(misto)
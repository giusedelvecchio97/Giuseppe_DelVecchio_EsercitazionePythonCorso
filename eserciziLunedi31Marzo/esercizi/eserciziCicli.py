

controller=True


while(controller):           #il controller serve per verificare se si immetta un numero positivo o meno,così da ciclare finquando il valore inserito non sia corretto
    num=int(input("inserirsci un numero"))
    if(num>0):
        if (num%2==0):
             print("numero Pari")
        else: 
            print("numero disperi")
        controller=False
    else:
        print("numero inserito negativo riprova")
    
    
    
#esercizio2

num=int(input("inserisci un numero"))

for num in range(num,-1,-1):
    
         print(num)
         


while(num>=0):
    
    print(num)
    num=num-1
    


#esercizio3

controller=True
lista=[]

while(controller):
    
    lista.append(int(input("inserisci valore"))**2)
    
    scelta=print("vuoi inserire altri numeri? SI or No")
    
    if (scelta=="NO"):
        controller=False

 
   
print(lista)    





#esercizio 4

lista=[]
controller=True
while(controller):
    
    lista.append(int(input("inserisci valore"))**2)
    if (scelta=="NO"):
        controller=False
  
  #trovo il massimo con un for      
massimo=lista[0]
for numero in lista:
    if numero > massimo:
        massimo = numero  # Aggiorniamo il massimo se troviamo un valore maggiore

print(massimo)

#conto gli elementi nella lista
i=0
count=0
while(i<len(lista)):   #ci permette di scorrere sulla lista e count serve per contare gli elemnti
    count+=1
    
 
print(count)   


#punto3

if(len(lista==0)):

    print("la lista è vuota")
else:
    print(massimo)
    print(count)





    
    
    
    



    
    
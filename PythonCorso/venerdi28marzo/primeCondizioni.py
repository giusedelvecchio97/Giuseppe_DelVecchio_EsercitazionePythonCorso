num=-2
if(num>0):
    print("valore positivo")

else:
    print("valore non accettabile")
    
    
    
    
string=input("inserisci scelta")

match string:
    case "A":
        print("pluto")
    
    case "B":
        print("Pippo")
    case _ :
        print("scelta non accettabie")

def decoratore(funzione):
    def wrapper():
        print("prima dell'esecuzione della funzione")
        funzione()
        print("dopo l'esecuzione della funzione")
    return wrapper


@decoratore
def saluta():
    print("ciao")

saluta()
# Declarar funciones en python

def saludar():
    print("hola mundo")

def saludarNombre(nombre):
    print("hola mundo {}".format(nombre.title()))

def saludarDeBuenas(nombre, estas_de_buenas=False):
    if(estas_de_buenas):
        print("hola mundo {}".format(nombre.title()))
    else:
        print("No me hables!!!")
saludar()
saludarNombre("jonas brother")
saludarDeBuenas("jonas brother",estas_de_buenas=True)

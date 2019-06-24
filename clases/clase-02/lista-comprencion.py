mi_lista = [10,15,20,25]
#sumar 10 a cada elemento
#nueva_lista = [x + 10 for x in mi_lista]

def voltearDigitos(x):
    valor = str(x)
    valor = list(valor)
    valor.reverse()
    return ''.join(valor)

nueva_lista = [voltearDigitos(x) for x in mi_lista]

#primero se ejecuta la condicion y despues realiza la operacion
pares = [x + 10 for x in mi_lista if x % 2 == 0]

print(nueva_lista)

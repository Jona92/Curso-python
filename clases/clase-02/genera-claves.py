import string
import random

letras = string.ascii_letters
num = string.digits
valores_posibles = letras + num

total_claves = input("Dame el número de claves: ")
total_claves = int(total_claves)
long_claves = input("Longitud de las claves (8): ")
long_claves = int(long_claves)

for i in range(long_claves):
    clave = []
    for i in range(long_claves):
        clave.append(random.choice(valores_posibles))
    password = ''.join(clave)
    print(password)

auto = tuple(['auto', 15000])
bici = tuple(['bici', 1000])
bici_2 = tuple(['bici', 1000])
cham = tuple(['chamarra', 3000])

productos = [auto,bici,cham,bici_2]

#ordenamiento de listas
productos.sort(key=lambda x: x[1])
print(productos)

#los conjuntos eliminan los valores duplicados de una tupla 
conjunto = set(productos)
print(conjunto)

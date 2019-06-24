auto = ['auto', 15000]
bici = ['bici', 3000]
cham = ['chamarra', 3000]

productos = [auto,bici,cham]

productos[2][1] = productos[2][1] * 1.1

plantilla = '{} \t\t| {:.2f}'
for producto in productos:
    print(plantilla.format(producto[0].title(), producto[1]))

user_product = input("Dame el nombre un producto: ")
user_price = input("Dame el precio del producto: ")
user_price = float(user_price)
nuevo_producto = [user_product,user_price]

productos.append(nuevo_producto)

plantilla = '{} \t\t| {:.2f}'
for producto in productos:
    print(plantilla.format(producto[0].title(), producto[1]))

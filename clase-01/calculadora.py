valor_a = input("Dame el valor A: ")
valor_b = input("Dame el valor B: ")

valor_a = int(valor_a)
valor_b = int(valor_b)

menu = """
1. suma
2. resta
3. multiplicacion
4. division
5. salir
"""
print(menu)

opcion = input("Dame una opcion numerica: ")

while opcion != '5':

    if opcion == "1":
        print("{a} + {b} = {res}".format(res=valor_a+valor_b,
                                         a=valor_a,
                                         b=valor_b))
        print(menu)
        opcion = input("Dame una opcion numerica: ")
    elif opcion == "2":
        print("{a} - {b} = {res}".format(res=valor_a-valor_b,
                                         a=valor_a,
                                         b=valor_b))
        print(menu)
        opcion = input("Dame una opcion numerica: ")
    elif opcion == "3":
        print("{a} * {b} = {res}".format(res=valor_a*valor_b,
                                         a=valor_a,
                                         b=valor_b))
        print(menu)
        opcion = input("Dame una opcion numerica: ")
    elif opcion == "4":
        print("{a} / {b} = {res}".format(res=valor_a/valor_b,
                                         a=valor_a,
                                         b=valor_b))
        print(menu)
        opcion = input("Dame una opcion numerica: ")
    else:
        print('"{}" no es una opcion valida'.format(opcion))
        print(menu)
        opcion = input("Dame una opcion numerica: ")
print("Hasta pronto!!!")

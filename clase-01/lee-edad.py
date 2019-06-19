edad = input("Dame tu edad: ")

if edad.isdecimal():
    if edad>=18:
        print("Eres mayor de edad, ya puedes tomar una gaseosa")
    elif edad<=17:
        print("Eres menor de edad, puedes tomar malteada")
else:
    print("Error: {} no es valor para una edad".format(edad))

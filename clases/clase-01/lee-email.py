correo  = "correo@prueba.com"
correo1 = "correo-prueba.com"
correo2 = "correo@prueba"

lista_correo = [correo,correo1,correo2]

for email in lista_correo:
    print(email)
    if ("@" in email) and (".com" in email):
        print("Email correcto")
    else:
        print("Email incorrecto")
    print("=============\n")

info_usuario = []

nombre = input("Dame tu nombre: ")
info_usuario.append(nombre)
apellido = input("Dame tu apellido: ")
info_usuario.append(apellido)
nacionalidad = input("Dame tu nacionalidad: ")
info_usuario.append(nacionalidad)

plantilla = "El ciudadano {} {} tienen nacionalidad {},"
plantilla = plantilla.format(info_usuario[0],info_usuario[1],info_usuario[2])
print(plantilla)

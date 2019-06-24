nombre = input('Dame tu nombre: ')

# comentar con print
print('hola_mundo, ',nombre.title())
print('hola_mundo, ',nombre.capitalize())

# comentar texto con +
texto = 'hola mundo, '+nombre
print(texto)

# generar una plantilla
plantilla = "Hola Mundo, {}"
plantilla = plantilla.format(nombre)
print(plantilla)

#!/usr/bin/env python
# coding=utf-8
class Persona(object):
    """docstring for Personas."""

    def __init__(self, nombre,a_paterno,edad):
        self.nombre = nombre
        self.a_paterno = a_paterno
        self.edad = edad

    @property
    def edad_real(self):
        return int(self.edad) + 5

def obteber_personas():
     nombre = input("Dame el nombre: ")
     a_paterno = input("Dame el apellido: ")
     edad = input("Dame la edad: ")

     return Persona(nombre,a_paterno,edad)

def imprimir_personas(lista_personas):
    print("Nombre\tApellido\tEdad\tEdad_real")
    print("----------------------")
    for persona in lista_personas:
        texto = "{}\t{}\t{}\t{}".format(persona.nombre,persona.a_paterno,persona.edad,persona.edad_real)
        print(texto)
    print("----------------------")

def guardarEnArchivo(lista_personas):
    file_name = 'personas.txt'
    with open(file_name,'w') as f:
        f.write("Nombre\tApellido\tEdad\tEdad_real\n")
        f.write("----------------------\n")
        for persona in lista_personas:
            texto = "{}\t{}\t{}\t{}".format(persona.nombre,
                                            persona.a_paterno,
                                            persona.edad,
                                            persona.edad_real)
            f.write(texto)
        f.write("----------------------\n")

def main():
    lista_personas = []
    for i in range(3):
        persona = obteber_personas()
        lista_personas.append(persona)
    guardarEnArchivo(lista_personas)

if __name__ == '__main__':
    main()

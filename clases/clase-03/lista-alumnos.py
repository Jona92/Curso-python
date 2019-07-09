#!/usr/bin/env python
# coding=utf-8

class Persona(object):
    """docstring for Personas."""

    def __init__(self, nombre,a_paterno,edad):
        self.nombre = nombre
        self.a_paterno = a_paterno
        self.edad = edad

class Alumno(Persona):
    """docstring for Alumno."""

    def __init__(self, nombre,a_paterno,edad,materia,calificacion):
        Persona.__init__(self,nombre,a_paterno,edad)
        self.materia = materia
        self.calificacion = calificacion

def main():
    alumno = Alumno('jhon','alvarez',26,'python',99.9)
    print(alumno.nombre)
    print(alumno.materia)
if __name__ == '__main__':
    main()

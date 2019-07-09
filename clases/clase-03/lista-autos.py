#!/usr/bin/env python
# coding=utf-8
class Producto(object):
    """docstring for Producto."""
    def __init__(self, nombre,cantidad,precio):
        self.nombre = nombre
        self.cantdad = cantidad
        self.precio = precio

    def __str__(self):
        texto = "{}\t{}\t{}\t{}".format(self.nombre,
                                        self.cantidad,
                                        self.precio,
                                        self.subtotal)
        return texto

    @property
    def subtotal(self):
        return int(self.cantdad) * float(self.precio)

class Auto(Producto):
    """docstring for Auto."""
    def __init__(self, nombre,cantidad,precio,marca,modelo):
        Producto.__init__(self,nombre,cantidad,precio)
        self.marca = marca
        self.modelo = modelo

def imprimir_autos(lista_autos):
    print("Nombre\tCantidad\tPrecio\tSubtotal")
    print("----------------------")
    for auto in lista_autos:
        texto = "{}\t{}\t{}\t{}".format(auto.nombre,
                                        auto.cantidad,
                                        auto.precio,
                                        auto.subtotal)
        print(texto)
    print("----------------------")

def main():
    auto_1 = Auto("jetta",2,2000000,'vw',2018)
    auto_2 = Auto("ibiza",2,1000000,'seat',2018)
    auto_3 = Auto("a1",2,1300000,'audi',2011)

    print(auto_1)
    print(auto_2)
    print(auto_3)

    # lista_autos = [auto_1,auto_2,auto_3]
    # imprimir_autos(lista_autos)

if __name__ == '__main__':
    main()

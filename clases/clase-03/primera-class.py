#!/usr/bin/env python
# coding=utf-8

class A(object):
    """docstring for A."""

    def __init__(self, cantidad):
        self.cantidad = cantidad

    def porciento(self,p):
        return self.cantidad * (p/100)

def main():
    a = A(100)
    print(a.cantidad)
    print(a.porciento(85))

if __name__ == '__main__':
    main()

decimal = input('Valor decimal: ')

if decimal.isdecimal():
    entero  = int(decimal)
    binario = bin(entero)
    print('valor en binario: ',binario)
else:
    print('El valor {} no es decimal'.format(decimal))

base = input("Dame el tamaño de la base: ")

if (base.isnumeric()):
    base = int(base)
    if(base % 2 != 0):
        for i in range(1,base+1,2):
            print((i*"#").center(20))
    else:
        print("No es numero impar!")
else:
    print("No es numerico")

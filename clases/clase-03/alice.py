# fa = open('text.txt','r')
#
# palabras_novela = []
# for line in fa:
#     palabras = line.split(' ')
#     palabras_novela.extend(palabras)
#
# fa.close()
#
# sanitizar = lambda s: s.replace('\n','').replace('.','')
# palabras_novela = [sanitizar(x) for x in palabras_novela]
# palabras_novela = [x for x in palabras_novela if x != '']
#
# print(palabras_novela)

with open('alice.txt','r') as f:
    texto = f.read()

print(texto)

import csv
import os

linea_1 = ['nombre','apellido','edad']
linea_2 = ['jose','perez',35]
linea_3 = ['jose1','perez1',25]
linea_4 = ['jose2','perez2',15]

with open('personas.csv','w') as f:
    csv_writer = csv.writer(f)
    for line in [linea_1,linea_2,linea_3,linea_4]:
        csv_writer.writerow(line)

os.system("open personas.csv")

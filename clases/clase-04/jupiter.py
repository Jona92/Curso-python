file = open('somthing','w')
file.write('somthing')
file.close()
#-----------------------------------
with open('text.txt','w') as f:
    f.write('something')
#----------------------------------
import csv

fruta = [['nombre','color'],['manzana','roja'],['platano','amarillo']]

with open('futa_file.csv',mode='w') as fruta_file:
    file = csv.writer(fruta_file,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for item in fruta:
        file.writerow(item)

fruts_dic = [{ 'nombre':'manzana' , 'color':'roja'} , {'nombre':'amarillo', 'color': 'amarillo'}]

with open('fruts_dic', mode='w') as fruts_file:
  file = csv.DictWriter(fruts_file, fieldnames=fruts_dic[0].keys())
  file.writeheader()
  for item in fruts_dic:
    file.writerow(item)

#----------------------------------
import pandas

def = pandas.read_csv('fruts_file.csv')

with open('fruts_file.csv',mode='r') as fruts_file:
    rows = csv.reader(fruts_file)
    for item in rows:
        print(item)

#----------------------------------

import xlsxwriter

workbook = xlsxwriter.Workbook('hello_world.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello world')

workbook.close()

#----------------------------------
data = {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}

print(data)

import json
with open('data.json','w') as f:
    json.dump(data,f,indent=4)

with open('data.json','w') as f:
    data2 = json.load(f)

print(data2)

#-----------------------------------
import requests

r = requests.get('https://pokeapi.co/api/v2/pokemon/ditto/')
data = r.json()
data

#----------------------------------
import requests
import json
count = 0
for pokemon in [1,2,3,4,5,6,7,8,9,10]:
    count += 1
    r = requests.get('https://pokeapi.co/api/v2/pokemon/ditto/')
    data = r.json()
    with open('data%s.json'% count,'w') as f:
        json.dump(data,f,indent=4)

#-------------------------------

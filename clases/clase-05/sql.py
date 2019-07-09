import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('somthing.db')

c = conn.cursor()

sql = '''CREATE TABLE IF NOT EXISTS projects (
    id integer PRIMARY KEY,
    name text NOT NULL
);'''

#-------------------------
import pandas as pa

data = pa.read_csv('movie_metadata.csv')

#---para ver los datos en una tabla----#
data.head()

data.columns

sql_genero = '''CREATE TABLE IF NOT EXISTS genero (
    id integer PRIMARY KEY,
    name text NOT NULL
);'''

sql_actor = '''CREATE TABLE IF NOT EXISTS actor (
    id integer PRIMARY KEY,
    name text NOT NULL
);'''

sql_director = '''CREATE TABLE IF NOT EXISTS director (
    id integer PRIMARY KEY,
    name text NOT NULL
);'''

sql_pelicula = '''CREATE TABLE IF NOT EXISTS pelicula (
    id integer PRIMARY KEY,
    name text NOT NULL,
    year integer NOT NULL,
    duration integer NOT NULL,
    country text NOT NULL
);'''

c.execute(sql_genero)
c.execute(sql_actor)
c.execute(sql_director)
c.execute(sql_pelicula)

sql_genero_pelicula = '''CREATE TABLE IF NOT EXISTS genero_pelicula (
    id_genero integer NOT NULL,
    id_pelicula integer NOT NULL,
    FOREIGN KEY (id_genero) REFERENCES genero(id),
    FOREIGN KEY (id_pelicula) REFERENCES pelicula(id)
);'''

sql_actor_pelicula = '''CREATE TABLE IF NOT EXISTS actor_pelicula (
    id_actor integer NOT NULL,
    id_pelicula integer NOT NULL,
    FOREIGN KEY (id_actor) REFERENCES actor(id),
    FOREIGN KEY (id_pelicula) REFERENCES pelicula(id)
);'''

sql_director_pelicula = '''CREATE TABLE IF NOT EXISTS director_pelicula (
    id_director integer NOT NULL,
    id_pelicula integer NOT NULL,
    FOREIGN KEY (id_director) REFERENCES director(id),
    FOREIGN KEY (id_pelicula) REFERENCES pelicula(id)
);'''

c.execute(sql_genero_pelicula)
c.execute(sql_actor_pelicula)
c.execute(sql_director_pelicula)

c.execute('INSERT INTO actor(name) VALUES ("PRUEBA");')

rows =  c.execute('SELECT * FROM actor;')
for row in rows.fetchall():
    print(row)

actores = set(list(data['actor_1_name']) + list(data['actor_2_name']) + list(data['actor_3_name']))
directores = set(list(data['director_name']))
len(actores)

actores

generos = []
for genero in data['genres']:
    for item in genero.split('|'):
        if item not in generos:
            generos.append(item)

for actor in actores:
    c.execute('INSERT INTO actor(name) VALUES ("%s");'% actor)

for genero in generos:
    c.execute('INSERT INTO genero(name) VALUES ("%s");'% genero)

for director in directores:
    c.execute('INSERT INTO director(name) VALUES ("%s");'% director)

rows = list(data.iterrows())

#pendiente por terminar de completar el codigo
for row in rows:
    title = row[1]['movie_title']
    year = row[1]['title_year']
    duration = row[1]['duration']
    country = row[1]['duration']
    director = row[1]['duration']
    act = row[1]['duration']

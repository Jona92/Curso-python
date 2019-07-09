from bottle import route, run, template

# @route('/hello/<name>')
# def index(name):
#     return template('<b>Hello {{name}}</b>!', name=name)

@route('/hello')
@route('/hello/<name>')
def hello(name='World'):
    return template('hello_template', name=name)

run(host='localhost', port=8080)

# sudo apt install python-virtualenv
#
# mkdir something
# cd something
# virtualenv . --python=python3
# source bin/activate

#INSTALACION DE DJANGO
# pip install django
# django-admin startproject project_bedu
# cd project_bedu
# python manage.py runserver

#CREA UNA APP DE DJANGO 
#python manage.py startapp home

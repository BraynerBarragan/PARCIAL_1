from flask import render_template, request, redirect, url_for
from src.config.db import CONEXION_PATH,createDB,databases,tablas,especifica
from src import app
import src.config.globals as globals
import json


@app.route('/')
def index():
    if (globals.DB == False):
        return render_template('instalacion.html')
    
    return render_template('index.html')

@app.route('/iniciando', methods=['GET','POST'])
def iniciando():
    if request.method == 'GET':
        return render_template('instalacion.html')

    
    host = request.form.get('host')
    port = request.form.get('port')
    user = request.form.get('user')
    password = request.form.get('password')
    config = {
    'host': host,
    'port': int(port),
    'user': user,
    'password': password
    }
    
    archivo=open(CONEXION_PATH,"w")
    archivo.write(json.dumps(config))
    archivo.close()

    createDB()
    db = databases()
    print(databases())
    return render_template('listadbs.html', dbs = db)
    
@app.route('/db/tablas<base>', methods=['GET','POST'])
def tables(base):
    nombre = ''
    nombre = base

    lista = tablas(nombre)
    print(lista)
    
    return render_template('listatablas.html', lista = lista, base= base)

@app.route('/db/tablas/especificar<tabla>', methods=['GET','POST'])
def especificarTabla(tabla):

    especificar = especifica(tabla)
    
    return render_template('especificar.html', especificacion = especificar, tabla= tabla)

    


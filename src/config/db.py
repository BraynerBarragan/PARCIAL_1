import mariadb
from os import path
import json
import src.config.globals as globals
CONEXION_PATH = path.abspath('src/config/conexion.json')

def databases():
    cursor = globals.DB.cursor()
    cursor.execute('show databases;')
    db = cursor.fetchall()
    cursor.close()

    return db

def tablas(b):
    cursor = globals.DB.cursor()
    cursor.execute("use {}".format(b))
    cursor.execute('show tables;')
    tablas = cursor.fetchall()
    cursor.close()
    return tablas

def especifica(tabla):
    cursor = globals.DB.cursor()
    #cursor.execute("use {}".format(b))
    cursor.execute("show create table {};".format(tabla))
    datos = cursor.fetchall()
    cursor.close()
    return datos



def createDB():
    if path.exists(CONEXION_PATH):
        file_conexion = open(CONEXION_PATH, 'r')
        config = json.loads(file_conexion.read())
        globals.DB = mariadb.connect(**config)
        globals.DB.autocommit = True
        
    else:
        globals.DB = False
        
createDB()
#try:
#    DB = mariadb.connect(**config)
#    DB.autocommit = True
#except:
#    DB = False
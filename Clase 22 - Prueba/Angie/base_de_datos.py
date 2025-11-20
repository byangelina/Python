# Crear un tabla con los atributos necesarios para guardar un producto(código PK, descripción, stock y ubicación)

import sqlite3

# Base de datos de producto
conectar = sqlite3.connect('Basededatos.db')
ejecutar = conectar.cursor() 

ejecutar.execute("""CREATE TABLE producto (
        codigo integer primary key,
        descripcion text,
        stock integer,
        ubicacion text         
        )""") 

ejecutar.execute("INSERT INTO producto VALUES ('', '', '' )")

ejecutar.execute("SELECT * FROM empleados WHERE =''")



conectar.commit()
conectar.close()



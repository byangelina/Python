"""
Para crear cualquier base de datos conectada a Python, primero:

1. Importar la librería sqlite3 
import sqlite3 

2. Crear la variable que genere la coneccion con la base de datos y darle un nombre a la base de datos
variable_conexion = sqlite3.connect('nombre_base_de_datos.db')

3. Crear otra vable que permita guardar a "cursor" y acceder a los comandos de sql
variable_cursor = variable_conexion.cursor() 

"""


# Base del código

import sqlite3

conectar = sqlite3.connect('Basededatos.db') # creo la variable conectar y entre parentesis con comilla simple va el nombre de la base de datos 

# ahora que ya esta creada la base de datos, hay que crear un "cursor" de comandos,
# que permita ejecutar comandos de sql, para eso se crea otra variable.

c = conectar.cursor() # cree la variable c y la conecté a la variable de la base de datos "conectar"



#-----------------------------------------------------------------------------------------------------------------

# Quiero crear una tabla de empleados que contenga (nombre, apellido, salario):
# Cada vez que corra un codigo y no se vea nada en la terminal es porque se guardó correctamente
# Comentar el codigo corrido para que no se ejecute de nuevo o dará error

"""
PASOS:
1. Crear la tabla: create table
2. crear el nombre de la columna: nombre text, apellido text, pago integer
3. insertar datos de la tabla: INSERT INTO nombre_tabla VALUES ('')
"""



#c.execute("""CREATE TABLE empleados (
#          nombre text,
#          apellido text,
#          pago integer
#          )""") 

# c.execute("INSERT INTO empleados VALUES ('Benjita', 'Olate', 4000000 )")

c.execute("SELECT * FROM empleados WHERE apellido='Olate'")

print(c.fetchone())

conectar.commit()
conectar.close()


"""
--------------------------------------------------------------------------------------------------------------------------------------
APUNTES:

- las 3 comillas se llaman docstring
- c.fetchmany(5) --> fetch___ se utiliza para devolver en la consola una cantidad de filas como lista, si pongo (5), se verán 5.
- c.fetchone --> significa que se mostrará una fila, fetch "one"...
- c.fetchall --> solo imprime las filas restantes...
- IF NOT EXISTS: evita el error “table already exists”, ejemplo: CREATE TABLE IF NOT EXISTS empleados
- Usar DDL: CREATE TABLE
- Usar DML: INSERT, DELETE, UPDATE, SELECT
- Ejemplo DML: c.execute("INSERT INTO empleados (nombre, apellido, pago) VALUES (?, ?, ?)"...
- Mostrar datos: c.execute("SELECT * FROM empleados")
- Borrar: c.execute("DELETE FROM empleados WHERE id = ?", (3,))
- Actualizar: c.execute("UPDATE empleados SET pago = ? WHERE id = ?", (650000, 1))
- commit() guarda los cambios en el archivo .db, Si no haces commit, los cambios quedan “en el aire” y se pierden cuando termina el programa.
- try: intenta ejecutar esto. Si funciona, genial. Si da error, pasa al except.
- except: Si ocurre alguna excepción, guárdala en la variable x.”
- finally: “finally” es el cierre obligatorio del programa, siempre se ejecuta.





COMO USAR TRY: “Voy a intentar hacer estas líneas de código. Si algo falla, salto al except.”

try:
    print("Intento dividir...")
    x = 10 / 0

except Exception as x:
    print("Hubo un error:", e)

finally:
    print("Esto siempre se ejecuta.")

"""
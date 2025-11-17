

import sqlite3 # importar una librería

print("Conectando a la base de datos...")

# Abrir o crear una archivo SQlite:
try: # para capturar el error
    with sqlite3.connect("BDPrueba.db") as conn:
        c = conn.cursor()
        #DDL -> Definición, estructura de una tabla, vista, etc
        c.execute("Create table if not exists Usuarios (id Intenger Primary Key, nombre Text)")
        conn.commit()

        print("Base de datos conectada y tabla creada...")

        #DML -> Manipulación de datos (Insert, Update, Delete, Select)
        c.execute("Insert into Usuarios (id, nombre) values (1, 'Juan Perez')")
        conn.commit()

        """
        # ejemplo, no hacer esto porque es complicado, pero se si se puede hacer bien, primero invertigar.
        for x in range(10,1000000):
            c.execute("Insert into Usuarios (id, nombre) values(" + str(x))"""

        # jflkdsjfkljfljksd <---- si tengo esto y da error, da el error en except,
        # pero tabién pasa por el "finally". 
        print("\nRegistro ingresado...")

except sqlite3.Error as e: # para mostrar el error al usuario
    print("!!!....Error base de datos -> ", e, "...!!!")

finally:
    conn.close() # finally quiere decir que este paso se cumplirá si o si, el codigo pasa
    # por aqui si está correcto o si da error, caulquiera de las dos formas.

print("Fin del sistema.")




# codigo exacto del profe  -------------------------------------------------------------------------------------------------------
"""
import sqlite3

print("Conectando a la base de datos...")

try:
    #Abrir o crear una archivo SQlite 
    with sqlite3.connect("BDPrueba.db") as conn:
        c = conn.cursor()
        #DDL -> Definición, estructura de una tabla, vista, etc
        c.execute("Create table if not exists Usuarios (id Intenger Primary Key, nombre Text)")
        conn.commit()

        print("Base de datos conectada y tabla creada...")

        c.execute("Delete from Usuarios")
        #DML -> Manipulación de datos (Insert, Update, Delete, Select)
        c.execute("Insert into Usuarios (id, nombre) values (2, 'Emilia Ulloa')")
        conn.commit()

        for x in range(10,1000000):
            c.execute("Insert into Usuarios (id, nombre) values(" + str(x) + ", 'usuario" + str(x) + "')")

        conn.commit()

        print("\nRegistro ingresado...")
except sqlite3.Error as e:  
    print("!!!....Error base de datos -> ", e, "...!!!")
finally:
    conn.close()


print("Fin del sistema")"""
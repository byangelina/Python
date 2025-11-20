"""
EJERCICIO TIPO PRUEBA:

SQLite3
try / except / finally
funciones
recorrido de strings
ord() y chr()
encriptación simple
DDL y DML
insert, select, update
crear tabla
trabajar con cursor()
with sqlite3.connect()
"""


# CONTEXTO DEL CASO

# Una pequeña empresa quiere guardar información de sus empleados en una base de datos SQLite y,
# además, necesita un sistema de encriptación simple para proteger los nombres antes de
# guardarlos. Te piden desarrollar un programa en Python que haga lo siguiente.


# PASOS ------------------------------------------------------------------------------------------------------------------------------
# 1. Crear o abrir la base de datos
# 2. Encriptación, se peuden definir funciones aqui
# 2.2. encriptar(texto)
# 2.3. desencriptar(texto)
# 3. insertar tabla empleados con sus atributos, tipos de datos y usar try/except para capturar errores SQL.
# 4. Mostrar empleados desencriptados. Consulta todos los registros: c.execute("SELECT * FROM empleados")
# 5. Actualizar sueldo con el código de a continuación...
"""
try:
    with sqlite3.connect("empresa.db") as conn:
        c = conn.cursor()

        id_buscar = int(input("Ingrese el ID del empleado a actualizar: "))
        nuevo_sueldo = int(input("Ingrese el nuevo sueldo: "))

        c.execute("UPDATE empleados SET sueldo = ? WHERE id = ?", (nuevo_sueldo, id_buscar))
        conn.commit()

        if c.rowcount > 0:
            print("Sueldo actualizado correctamente.")
        else:
            print("No existe un empleado con ese ID.")

except sqlite3.Error as e:
    print("Error en la base de datos:", e)
"""
# 6. Cerrar la conexión, usar finally
# ------------------------------------------------------------------------------------------------------------------------------



# SOLUCIÓN DEL CASO

import sqlite3

def crear_tabla():
    try:
        with sqlite3.connect("empresa.db") as conn:
            c = conn.cursor()
            c.execute("""
                CREATE TABLE IF NOT EXISTS empleados (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    apellido TEXT,
                    sueldo INTEGER
                )
            """)
            conn.commit()
            print("Tabla lista.")
    except sqlite3.Error as e:
        print("Error al crear tabla:", e)

def insertar_empleado():
    try:
        with sqlite3.connect("empresa.db") as conn:
            c = conn.cursor()

            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            sueldo = int(input("Sueldo: "))

            c.execute("INSERT INTO empleados (nombre, apellido, sueldo) VALUES (?, ?, ?)",
                (nombre, apellido, sueldo))
            conn.commit()

            print("Empleado registrado.")
    except sqlite3.Error as e:
        print("Error al insertar:", e)

def mostrar_empleados():
    try:
        with sqlite3.connect("empresa.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM empleados")
            lista = c.fetchall()

            print("\n--- Empleados ---")
            for emp in lista:
                print(emp)
            print("-----------------\n")

    except sqlite3.Error as e:
        print("Error al mostrar:", e)

def actualizar_sueldo():
    try:
        with sqlite3.connect("empresa.db") as conn:
            c = conn.cursor()

            id_buscar = int(input("ID del empleado a actualizar: "))
            nuevo_sueldo = int(input("Nuevo sueldo: "))

            c.execute("UPDATE empleados SET sueldo = ? WHERE id = ?", (nuevo_sueldo, id_buscar))
            conn.commit()

            if c.rowcount > 0:
                print("Sueldo actualizado.")
            else:
                print("No existe un empleado con ese ID.")

    except sqlite3.Error as e:
        print("Error al actualizar:", e)

def eliminar_empleado():
    try:
        with sqlite3.connect("empresa.db") as conn:
            c = conn.cursor()

            id_eliminar = int(input("ID del empleado a eliminar: "))

            c.execute("DELETE FROM empleados WHERE id = ?", (id_eliminar,))
            conn.commit()

            if c.rowcount > 0:
                print("Empleado eliminado.")
            else:
                print("No existe un empleado con ese ID.")

    except sqlite3.Error as e:
        print("Error al eliminar:", e)

# ------------------------------
#        MENÚ PRINCIPAL
# ------------------------------

crear_tabla()

while True:
    print("""
    --- MENÚ ---
    1. Insertar empleado
    2. Mostrar empleados
    3. Actualizar sueldo
    4. Eliminar empleado
    5. Salir
    """)

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        insertar_empleado()
    elif opcion == "2":
        mostrar_empleados()
    elif opcion == "3":
        actualizar_sueldo()
    elif opcion == "4":
        eliminar_empleado()
    elif opcion == "5":
        print("Adiós!")
        break
    else:
        print("Opción inválida, intente nuevamente.")














# TAREA
# Crear un CRUD de usuarios que se conecte a una base de datos SQLite
"""
• Create → crear
• Read → leer/buscar
• Update → actualizar
• Delete → eliminar
"""

# Ejercicio de la pizarra (crear usuario, eliminar, actualizar, buscar, salir) debe hacerse guardando los datos
# en una tabla llamada Usuarios, con encriptación básica para el correo y la clave.

# CONSIDERACIONES:
# - clave única para el correo
# - Implementa CRUD completo
# - Manejar errores con try/except
# - Menú funcional desde consola

# CREAR TABLA USUARIOS
# id (entero, autoincremental)
# correo (texto encriptado) 
# perfil (texto)

# MENU CON OPCIONES
# 1. Crear usuario
# 2. Eliminar usuario
# 3. Actualizar usuario
# 4. Buscar usuarios
# 5. Salir


import sqlite3

# --- Encriptar y desencriptar sin hashlib ---
def encriptar(texto):
    resultado = ""
    for caracter in texto:
        resultado += chr(ord(caracter) + 5)
    return resultado

def desencriptar(texto):
    resultado = ""
    for caracter in texto:
        resultado += chr(ord(caracter) - 5)
    return resultado


# --- Crear tabla si no existe ---
def crear_tabla():
    try:
        with sqlite3.connect("Usuarios.db") as conn:
            c = conn.cursor()
            c.execute("""
                CREATE TABLE IF NOT EXISTS Usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    correo TEXT UNIQUE,
                    clave TEXT,
                    perfil TEXT
                )
            """)
            conn.commit()
        print("Tabla 'Usuarios' lista.")
    except sqlite3.Error as e:
        print("Error al crear la tabla:", e)


# --- CRUD ---

def crear_usuario():
    correo = input("Correo: ")
    clave = input("Clave: ")
    perfil = input("Perfil (admin/usuario): ")

    correo_enc = encriptar(correo)
    clave_enc = encriptar(clave)

    try:
        with sqlite3.connect("Usuarios.db") as conn:
            c = conn.cursor()
            c.execute("INSERT INTO Usuarios (correo, clave, perfil) VALUES (?, ?, ?)",
                (correo_enc, clave_enc, perfil))
            conn.commit()
            print("✅ Usuario creado con éxito.")
    except sqlite3.IntegrityError:
        print("Ese correo ya existe (clave única).")
    except sqlite3.Error as e:
        print("Error al crear usuario:", e)

def eliminar_usuario():
    id_usuario = input("ID del usuario a eliminar: ")
    try:
        with sqlite3.connect("Usuarios.db") as conn:
            c = conn.cursor()
            c.execute("DELETE FROM Usuarios WHERE id = ?", (id_usuario,))
            conn.commit()
            if c.rowcount > 0:
                print("Usuario eliminado.")
            else:
                print("ID no encontrado.")
    except sqlite3.Error as e:
        print("Error al eliminar usuario:", e)

def actualizar_usuario():
    id_usuario = input("ID del usuario a actualizar: ")
    nuevo_perfil = input("Nuevo perfil: ")
    try:
        with sqlite3.connect("Usuarios.db") as conn:
            c = conn.cursor()
            c.execute("UPDATE Usuarios SET perfil = ? WHERE id = ?", (nuevo_perfil, id_usuario))
            conn.commit()
            if c.rowcount > 0:
                print("Usuario actualizado.")
            else:
                print("ID no encontrado.")
    except sqlite3.Error as e:
        print("Error al actualizar usuario:", e)

def buscar_usuarios():
    try:
        with sqlite3.connect("Usuarios.db") as conn:
            c = conn.cursor()
            c.execute("SELECT id, correo, clave, perfil FROM Usuarios")
            usuarios = c.fetchall()
            print("\n--- LISTADO DE USUARIOS ---")
            for u in usuarios:
                print(f"ID: {u[0]} | Correo: {desencriptar(u[1])} | Clave: {desencriptar(u[2])} | Perfil: {u[3]}")
    except sqlite3.Error as e:
        print("Error al buscar usuarios:", e)

# --- MENÚ PRINCIPAL ---
def menu():
    crear_tabla()
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Crear usuario")
        print("2. Eliminar usuario")
        print("3. Actualizar usuario")
        print("4. Buscar usuarios")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            eliminar_usuario()
        elif opcion == "3":
            actualizar_usuario()
        elif opcion == "4":
            buscar_usuarios()
        elif opcion == "5":
            print("👋 Fin del sistema.")
            break
        else:
            print("Opción no válida, intenta otra vez.")

# --- EJECUTAR PROGRAMA ---
menu()

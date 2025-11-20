import sqlite3

DB_NAME = "inventario.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def crear_tabla():
    try:
        with conectar() as conn:
            c = conn.cursor()
            c.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    codigo TEXT PRIMARY KEY,
                    descripcion TEXT,
                    precio INTEGER,
                    stock INTEGER
                )
            """)
            conn.commit()
    except sqlite3.Error as e:
        print("Error al crear tabla:", e)

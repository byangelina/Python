# Crear un tabla con los atributos necesarios para guardar un producto(código PK, descripción, stock y ubicación)
import sqlite3

def conexion():
        return sqlite3.connect("producto.db")


def tabla_producto():
        try:
                conn = sqlite3.connect("producto.db")
                cursor = conn.cursor()

                cursor.execute("""
                        CREATE TABLE IF NOT EXISTS producto (
                                codigo INTEGER PRIMARY KEY,
                                descripcion TEXT,
                                stock INTEGER,
                                ubicacion TEXT
                        )
                """)
                conn.commit()

        except sqlite3.Error as x:
                print("Error al crear tabla:", x)

        finally:
                conn.close()

import sqlite3

def conectar(): sqlite3.connect('Basededatos.db')

def crear_tabla():
    cont= conectar
    try:
        c = cont.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            codigo TEXT PRIMARY KEY,
            descripcion TEXT,
            stock INTEGER,
            ubicacion TEXT
        )
        """)
        cont.commit()
    except Exception as e:
        print("Error al crear tabla:", e)
    finally:
        cont.close()
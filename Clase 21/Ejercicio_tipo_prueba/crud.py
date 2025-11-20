from db import conectar
from producto import Producto
from seguridad import validar_entero

def ingresar_producto():
    codigo = input("Código: ")
    descripcion = input("Descripción: ")
    precio = validar_entero(input("Precio: "))
    stock = validar_entero(input("Stock: "))

    if precio is None or stock is None:
        print("Datos inválidos, no se guardó.")
        return

    try:
        with conectar() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO productos (codigo, descripcion, precio, stock) VALUES (?, ?, ?, ?)",
                      (codigo, descripcion, precio, stock))
            conn.commit()
            print("Producto ingresado.")
    except Exception as e:
        print("Error al ingresar:", e)


def modificar_producto():
    codigo = input("Código del producto a modificar: ")

    try:
        with conectar() as conn:
            c = conn.cursor()

            c.execute("SELECT * FROM productos WHERE codigo = ?", (codigo,))
            prod = c.fetchone()

            if not prod:
                print("Producto no encontrado.")
                return

            print("Ingrese nuevos datos (ENTER para dejar igual):")

            nueva_desc = input(f"Descripción [{prod[1]}]: ") or prod[1]
            nuevo_precio = input(f"Precio [{prod[2]}]: ")
            nuevo_stock = input(f"Stock [{prod[3]}]: ")

            nuevo_precio = int(nuevo_precio) if nuevo_precio else prod[2]
            nuevo_stock = int(nuevo_stock) if nuevo_stock else prod[3]

            c.execute("""
                UPDATE productos
                SET descripcion=?, precio=?, stock=?
                WHERE codigo=?
            """, (nueva_desc, nuevo_precio, nuevo_stock, codigo))
            conn.commit()

            print("Producto modificado.")
    except Exception as e:
        print("Error en modificar:", e)


def eliminar_producto():
    codigo = input("Código del producto a eliminar: ")
    try:
        with conectar() as conn:
            c = conn.cursor()
            c.execute("DELETE FROM productos WHERE codigo = ?", (codigo,))
            conn.commit()

            if c.rowcount > 0:
                print("Producto eliminado.")
            else:
                print("No existe un producto con ese código.")
    except Exception as e:
        print("Error al eliminar:", e)


def buscar_codigo():
    codigo = input("Código a buscar: ")

    try:
        with conectar() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM productos WHERE codigo = ?", (codigo,))
            prod = c.fetchone()

            if prod:
                p = Producto(*prod)
                print(p)
            else:
                print("No encontrado.")
    except Exception as e:
        print("Error en la búsqueda:", e)


def buscar_descripcion():
    texto = input("Buscar texto en descripción: ")

    try:
        with conectar() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM productos WHERE descripcion LIKE ?", (f"%{texto}%",))
            lista = c.fetchall()

            if lista:
                for p in lista:
                    print(Producto(*p))
            else:
                print("No hay coincidencias.")
    except Exception as e:
        print("Error en la búsqueda:", e)


def listar():
    try:
        with conectar() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM productos")
            lista = c.fetchall()

            print("\n--- Inventario ---")
            for p in lista:
                print(Producto(*p))
            print("------------------\n")

    except Exception as e:
        print("Error al listar:", e)

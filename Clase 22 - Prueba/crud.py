
import sqlite3
from base_de_datos import conexion
from encriptacion import encriptar, desencriptar
from producto import Producto


# 1. INGRESAR PRODUCTO ------------------------------------------------------------------------------------------------
def ingresar_producto():
    try:
        codigo = int(input("Código: "))
        descripcion = input("Descripción: ")
        stock = int(input("Stock: "))
        ubicacion = input("Ubicación: ")

        # Crear objeto Producto
        p = Producto(codigo, descripcion, stock, ubicacion)

        # Llamar a insertar
        if insertar(p):
            print("Producto ingresado correctamente.\n")
        else:
            print("No se pudo ingresar el producto.\n")

    except Exception as e:
        print("Error al ingresar producto:", e)


# 1. INSERTAR PRODUCTO ------------------------------------------------------------------------------------------------
def insertar(producto: Producto):
    try:
        conn = conexion()
        c = conn.cursor()

        desc_cifrada = encriptar(producto.descripcion)

        c.execute("""
            INSERT INTO producto (codigo, descripcion, stock, ubicacion)
            VALUES (?, ?, ?, ?)
        """, (producto.codigo, desc_cifrada, producto.stock, producto.ubicacion))

        conn.commit()
        return True

    except Exception as e:
        print("Error en insertar():", e)
        return False

    finally:
        conn.close()


# 2. ACTUALIZAR ----------------------------------------------------------------------------------------
def actualizar(producto: Producto):
    try:
        conn = conexion()
        c = conn.cursor()

        desc_cifrada = encriptar(producto.descripcion)

        c.execute("""
            UPDATE producto
            SET descripcion=?, stock=?, ubicacion=?
            WHERE codigo=?
        """, (desc_cifrada, producto.stock, producto.ubicacion, producto.codigo))

        conn.commit()
        return True

    except Exception as e:
        print("Error en actualizar():", e)
        return False

    finally:
        conn.close()





# 2. BUSCAR POR CODIGO ----------------------------------------------------------------------------------------
def buscar_por_codigo(codigo):
    try:
        conn = conexion()
        c = conn.cursor()

        c.execute("SELECT * FROM producto WHERE codigo = ?", (codigo,))
        fila = c.fetchone()

        if fila:
            desc = desencriptar(fila[1])
            return Producto(fila[0], desc, fila[2], fila[3])
        return None

    finally:
        conn.close()




# 2. BUSCAR CODIGO ----------------------------------------------------------------------------------------
def buscar_codigo():
    codigo = int(input("Código a buscar: "))
    p = buscar_por_codigo(codigo)

    if p:
        print(f"\nCódigo: {p.codigo}")
        print(f"Descripción: {p.descripcion}")
        print(f"Stock: {p.stock}")
        print(f"Ubicación: {p.ubicacion}\n")
    else:
        print("Producto no encontrado.\n")




# 3. MODIFICAR PRODUCTO -------------------------------------------------------------------------------------------------
def modificar_producto():
    try:
        codigo = int(input("Código del producto a modificar: "))

        existente = buscar_por_codigo(codigo)
        if not existente:
            print("Producto no encontrado.\n")
            return False

        print(f"Descripción actual: {existente.descripcion}")
        nueva_desc = input("Nueva descripción (enter para no cambiar): ")
        if nueva_desc.strip():
            existente.descripcion = nueva_desc

        print(f"Stock actual: {existente.stock}")
        nuevo_stock = input("Nuevo stock (enter para no cambiar): ")
        if nuevo_stock.strip():
            existente.stock = int(nuevo_stock)

        print(f"Ubicación actual: {existente.ubicacion}")
        nueva_ubicacion = input("Nueva ubicación (enter para no cambiar): ")
        if nueva_ubicacion.strip():
            existente.ubicacion = nueva_ubicacion

        # Llamar a actualizar
        if actualizar(existente):
            print("Producto modificado correctamente.\n")
        else:
            print("No se pudo modificar el producto.\n")

    except Exception as e:
        print("Error al modificar:", e)
        return False




# 4. ELIMINAR ------------------------------------------------------------------------------------------------
def eliminar_producto():
    try:
        codigo = int(input("Código a eliminar: "))

        conn = conexion()
        c = conn.cursor()

        c.execute("DELETE FROM producto WHERE codigo = ?", (codigo,))
        conn.commit()

        if c.rowcount > 0:
            print("Producto eliminado.\n")
            return True
        else:
            print("No existe un producto con ese código.\n")
            return False

    except Exception as e:
        print("Error al eliminar:", e)
        return False

    finally:
        conn.close()


# 5. BUSCAR POR DESCRIPCION ----------------------------------------------------------------------
def buscar_descripcion():
    texto = input("Buscar texto: ").lower()

    conn = conexion()
    c = conn.cursor()
    filas = c.execute("SELECT * FROM producto").fetchall()
    conn.close()

    resultados = []
    for fila in filas:
        desc = desencriptar(fila[1])
        if texto in desc.lower():
            resultados.append(Producto(fila[0], desc, fila[2], fila[3]))

    if not resultados:
        print("No se encontraron coincidencias.\n")
    else:
        print("\nResultados:")
        for p in resultados:
            print(f"{p.codigo} - {p.descripcion} - {p.stock} - {p.ubicacion}")

    return resultados



# 6. LISTAR INVENTARIO -----------------------------------------------------------------------------------------------------
def listar():
    conn = conexion()
    c = conn.cursor()

    filas = c.execute("""
        SELECT * FROM producto
        ORDER BY ubicacion ASC, descripcion ASC
    """).fetchall()

    conn.close()

    print("\nInventario:\n")

    productos = []

    for fila in filas:
        desc = desencriptar(fila[1])
        print(f"{fila[0]} | {desc} | Stock: {fila[2]} | Ubicación: {fila[3]}")
        productos.append((fila[0], desc, fila[2], fila[3]))

    return productos
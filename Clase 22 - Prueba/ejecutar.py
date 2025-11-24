
from base_de_datos import tabla_producto
tabla_producto()

import crud

while True:
    print("""
Menu de productos
1. Ingresar producto
2. Modificar producto
3. Eliminar producto
4. Buscar por código
5. Buscar por descripción
6. Listar inventario
7. Salir
""")

    opcion = input("Seleccione opción: ")

    if opcion == "1":
        crud.ingresar_producto()

    elif opcion == "2":
        crud.modificar_producto()

    elif opcion == "3":
        crud.eliminar_producto()

    elif opcion == "4":
        try:
            codigo = int(input("Ingrese código a buscar: "))
            producto = crud.buscar_por_codigo(codigo)
            if producto:
                print(f"{producto.codigo} | {producto.descripcion} | {producto.stock} | {producto.ubicacion}")
            else:
                print("No encontrado.\n")
        except ValueError:
            print("Código inválido.\n")

    elif opcion == "5":
        texto = input("Ingrese texto a buscar en la descripción: ")
        productos = crud.buscar_descripcion()  # usa tu función real
        # (la función ya imprime resultados por sí misma)

    elif opcion == "6":
        crud.listar()  # no necesita más, listar imprime todo

    elif opcion == "7":
        print("Adiós!")
        break

    else:
        print("Opción inválida\n")

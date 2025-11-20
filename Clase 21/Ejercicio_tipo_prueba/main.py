from db import crear_tabla
import crud

crear_tabla()

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
        crud.buscar_codigo()
    elif opcion == "5":
        crud.buscar_descripcion()
    elif opcion == "6":
        crud.listar()
    elif opcion == "7":
        print("Adiós!")
        break
    else:
        print("Opción inválida\n")

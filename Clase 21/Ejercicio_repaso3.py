"""
APUNTES:

- def: Una función es un bloque de código que haces una vez y puedes llamar muchas veces.
EJEMPLO:
def saludar(nombre):
    mensaje = "Hola, " + nombre + "!"
    return mensaje
print(saludar("Manzanita"))  # → Hola, Manzanita!

- ord(caracter): convierte un carácter (como 'A', 'b', 'á') en su número Unicode.
- chr(numero): convierte un número (código Unicode) en el carácter

EJEMPLO:
def encriptar(mensaje):
    mensaje_encriptado = ""
    for caracter in mensaje:
        numero = ord(caracter) + 5
        nuevo_caracter = chr(numero)
        mensaje_encriptado += nuevo_caracter
    return mensaje_encriptado





-
-
-
-

"""
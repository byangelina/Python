

import sqlite3 # Esto importa la librería SQLite3, que sirve para trabajar con bases de datos

def encriptar(mensaje): # define una función que recibe un texto
    mensajeEncriptadojejeje = "" # "" → empieza con un texto vacío
    for caracter in mensaje: # recorre cada letra del mensaje
        numero = ord(caracter) + 5 # convierte cada letra en su número Unicode y despues le suma 5 al número.
        # Es como mover la letra 5 posiciones adelante en la tabla de caracteres

        nuevoCaracter = chr(numero)
        # chr(numero) → convierte el número nuevamente en una letra.

        mensajeEncriptadojejeje += nuevoCaracter # va construyendo el mensaje letra por letra.



# Esta función hace lo contrario de encriptar...
# Resta 5 en vez de sumar 5. Así, recupera el mensaje original.
# Si el mensaje encriptado es "Mtqf",
# cada letra retrocede 5 lugares en la tabla de caracteres, y vuelve a ser "Hola"


def desencriptar(mensaje):
    mensajedesEncriptado = ""
    for caracter in mensaje:
        numero = ord(caracter) - 5
        nuevoCaracter = chr(numero)
        mensajedesEncriptado = mensajedesEncriptado + nuevoCaracter

    return mensajedesEncriptado


print(desencriptar("Mtqf%hthmnstsf"))
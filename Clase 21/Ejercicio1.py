# Ejemplo 1

"""
import rsa

(clave_publica, clave_privada) = rsa.newkeys(512)

print("Clave pública: ", clave_publica)
print("Clave privada: ", clave_privada)

msj = "Hola inframundo"
msj_byte = msj.encode('utf8')

print("Mensaje en byte: ", msj_byte)

# msj_cifrado = rsa.encrypt(msj_byte, )
"""



# Ejemplo 2

import rsa

(clave_publica, clave_privada) = rsa.newkeys(512)

print("Clave pública: ", clave_publica)
print("Clave privada: ", clave_privada)

msj = "Hola inframundo"
msj_byte = msj.encode('utf8')

print("Mensaje en byte: ", msj_byte)

msj_cifrado = rsa.encrypt(msj_byte, clave_publica)

print("Cifrado: ", msj_cifrado)

msj_descifrado = rsa.decrypt(msj_cifrado,clave_privada)






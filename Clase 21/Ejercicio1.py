# aprender a usar base64: caracteres que no tienen caracteres que no son universales
"""
se codifica en Base64 como sigue:

TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlz
IHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2Yg
dGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGlu
dWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRo
ZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4=
En la cita de arriba el valor codificado de Man es TWFu. Codificadas en ASCII, las letras: M, a y n son almacenadas como los bytes 77, 97 y 110, es decir, 01001101, 01100001, 01101110 en base 2.

"""





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




# Ejemplo 3

import rsa

(clave_publica, clave_privada) = rsa.newkeys(512)

print("Clave pública: ", clave_publica)
print("Clave privada: ", clave_privada)

msj = "Hola inframundo"
msj_byte = msj.encode('utf8')

print("Mensaje en byte: ", msj_byte)

msj_cifrado = rsa.encrypt(msj_byte, clave_publica)

print("---------------------------------Encriptado")
print("Cifrado: ",msj_cifrado)

msj_descifrado_byte = rsa.decrypt(msj_cifrado,clave_privada)
msj_descifrado = msj_descifrado_byte.decode("utf8")


print("---------------------------------Desencriptar")
print("Decifrado: ", msj_descifrado)







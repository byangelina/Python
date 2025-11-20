
# Repaso de criptografía y cifrado RSA

import rsa

clave_publica, clave_privada = rsa.newkeys(1024)

print(clave_privada)

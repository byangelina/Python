
def encriptar(texto):
    nuevo = ""
    for letra in texto:
        nuevo += chr(ord(letra) + 3)
    return nuevo



def desencriptar(texto):
    nuevo = ""
    for letra in texto:
        nuevo += chr(ord(letra) - 3)
    return nuevo
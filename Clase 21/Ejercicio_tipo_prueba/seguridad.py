def validar_entero(texto):
    try:
        return int(texto)
    except:
        print("Debe ingresar un número válido.")
        return None

def validar_codigo(codigo):
    if codigo.strip() == "":
        print("El código no puede estar vacío.")
        return None
    return codigo

def validar_texto(texto):
    if texto.strip() == "":
        print("El texto no puede estar vacío.")
        return None
    return texto



# ENUNCIADO:
# Se desea crear una empresa cuyo servicio es gestión de estacionamientos, para ello se ha modelado
# el siguiente diagrama de clases


# DATOS DE LA TABLA:
# - Arriba = datos que tiene la clase (atributos).
# - Abajo = acciones que puede hacer (métodos).

"""
DIAGRAMA DE CLASES

Tipo 1 Vehiculo 0
Estacionamiento 1 Vehiculo 0

-------------------------
|  Vehiculo             |
|-----------------------|
| - patente             |
| - minutosEstacionado  |
| - tipoVehiculo        |
|-----------------------|
| + totalPagar()        |
| + mostrarDatos()      |
-------------------------
-------------------------
|  Estacionamiento      |
|-----------------------|
| - codigo (get)        |
| - direccion (get, set)|
| - capacidad (get, set)|
|-----------------------|
| + entradaVehiculo()   |
| + salidaVehiculo()    |
| + disponibles()       |
| + ocupados()          |
| + obtenerPorTipo()    |
| + Estacionamiento()   |
| + Estacionamiento()   |
-------------------------
-------------------------
|  Tipo                 |
|-----------------------|
| - ruedas (get, set)   |
| - tipoVehiculo (get)  |
| - valorMinuto (get)   |
|-----------------------|
| + totalPagar()        |
| + mostrarDatos()      |
-------------------------

"""



class Estacionamiento:
    def __init__(self,codigo,direccion,capacidad):
        self.__codigo = codigo
        self.__direccion = direccion
        self.__capacidad = capacidad

# ---- Getters ----
    @property # Getter codigo
    def codigo(self):
        return self.__codigo

    @property # Getter direccion
    def direccion(self):
        return self.__direccion
    
    @property # Getter capacidad
    def capacidad(self):
        return self.__capacidad
    
# ---- Setters ----
    @direccion.setter # Setter direccion
    def direccion(self,nuevaDireccion):
        if isinstance(nuevaDireccion,str) and len(nuevaDireccion) >3: # valida que el valor sea un texto (str) y que tenga más de 3 caracteres
            self.__direccion = nuevaDireccion
        else:
            raise ValueError("La direccion debe ser válida (más de 3 caracteres).")
            # para detener la ejecución cuando algo no cumple las condiciones definidas

    @capacidad.setter # Setter capacidad
    def capacidad(self,nuevaCapacidad):
        if isinstance(nuevaCapacidad, int) and nuevaCapacidad > 0:
            self.__capacidad = nuevaCapacidad
        else:
            raise ValueError("La dirección debe ser mayor a 1.")




class Vehiculo:
    def __init__(self,patente,tipoVehiculo,minutosEstacionado):
        self.__patente = patente
        self.__tipoVehiculo = tipoVehiculo # objeto de la clase Tipo
        self.__minutosEstacionado = minutosEstacionado

# ---- Getters ----
    @property # Getter patente
    def patente(self):
        return self.__patente

    @property # Getter tipoVehiculo
    def tipoVehiculo(self):
        return self.__tipoVehiculo

    @property # Getter minutosEstacionado
    def minutosEstacinado(self):
        return self.__minutosEstacionado

# ---- Setters ----

    @minutosEstacionado.setter
    def minutosEstacionado(self,nuevosMinutos):
        if isinstance(nuevosMinutos, int) and nuevosMinutos >=0:
            self.minutosEstacionado = nuevosMinutos
        else:
            raise ValueError("Los miuntos estacionados deben ser mayor a 0.")



#clase heredada
class Tipo:
    def __init__(self,ruedas):
        self.__ruedas = ruedas
        if ruedas == 2:
            self.__tipoVehiculo = "Motocicleta"

    lista_tipos = [[2, "Motocicleta", 300],[3, "Trimoto", 600],[4, "Automóvil", 900],[5, "Camión", 1500]]  # 5 para más de 4 ruedas

    # por si no se encuentra el tipo
    self.__tipoVehiculo = "Desconocido"
    self.__valorMinuto = 0
        
    # Buscar tipo en la lista de forma sencilla
    for tipo in lista_tipos:
        ruedas_tipo = tipo[0]
        nombre = tipo[1]
        valor = tipo[2]
            
    if ruedas == ruedas_tipo or (ruedas > 4 and ruedas_tipo == 5):
        self.__tipoVehiculo = nombre
        self.__valorMinuto = valor

    @property
    def ruedas(self):
        return self.__ruedas

    @property
    def tipoVehiculo(self):
        return self.__tipoVehiculo

    @property
    def valorMinuto(self):
        return self.__valorMinuto






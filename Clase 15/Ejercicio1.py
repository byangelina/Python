

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
        if isinstance(nuevaDireccion,str) and len(nuevaDireccion) >3: # valida que el valor sea un texto más de 3 caracteres
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


    def totalPagar(self):
        tarifaPorMinuto = {
            "Motocicleta": 30,
            "Trimoto": 60,
            "Automóvil": 90,
            "N/A": 150
        }



  # def mostrarDatos(self):












#clase heredada
class Tipo():
    def __init__(self,ruedas,tipoVehiculo,valorMinuto):
        self.__ruedas = ruedas
        if ruedas == 2:
            self.__tipoVehiculo = "Motocicleta"
        elif ruedas == 3:
            self.__tipoVehiculo = "Trimoto"
        elif ruedas == 4:
            self.__tipoVehiculo = "Automóvil"
        elif ruedas == 5:
            raise ValueError ("Error, vehiculo no identificado (no puede tener 5 ruedas)")
        elif ruedas == 6:
            self.__tipoVehiculo = "Camión"
        else:
            raise ValueError("")

        
    @property # Getter ruedas
    def ruedas(self):
        return self.__ruedas
      # raise self.__tipoVehiculo > 4

    @ruedas.setter
    def ruedas(self,nuevasRuedas):
        if isinstance(nuevasRuedas, int) and nuevasRuedas <= 6:
            self.ruedas = nuevasRuedas
        else:
            raise ValueError("Error, el vehículo tiene más de 6 ruedas, vuelva a ingresar.")

    @property # Getter tipoVehiculo
    def tipoVehiculo(self):
        return self.__tipoVehiculo

    @property # Getter valorMinuto
    def valorMinuto(self):
        return self.__valorMinuto






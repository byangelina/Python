

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
class Tipo(Vehiculo):
    def __init__(self,ruedas,tipoVehiculo,valorMinuto):
        self.__ruedas = ruedas
        self.__tipoVehiculo = tipoVehiculo
        self.__valorMinuto = valorMinuto

    @property
    def ruedas(self): # Getter ruedas
        return self.__ruedas
    
    @property # Getter tipoVehiculo
    def tipoVehiculo(self):
        return self.__tipoVehiculo

    @property # Getter valorMinuto
    def valorMinuto(self):
        return self.valorMinuto

    @ruedas.setter # Setter ruedas
    def ruedas(self,ruedas):

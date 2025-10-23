
class Tipo: # Tipo tiene un constructor para crear una rueda, tipoVehiculo (get)
    # no todos los atributos de una clase van a estar en el constructor. el constructor es el que permite crear un obejto.
    motor = "100cc" # esto no tiene self, es decir no le pertenece a la instancia ese valor. los que estan en def si le corresponden.
    def __init__(self, ruedas:int): # intancia (son los atributos del objeto)
        self.__ruedas = ruedas # ruedas es privado, se privatiza con "self.__"
        # en los parametros pongo que el dato va a ser int

        # agregar en el ciclo los valores por minuto
        if ruedas == 2:
            self.__valorMinuto = 30 # esto califica como int, que se definió en los parametros del __init__
            self.__tipoVehiculo = "Moto" # estos califican como string
        elif ruedas == 3:
            self.__valorMinuto = 60
            self.__tipoVehiculo = "Trimoto"
        elif ruedas == 4:
            self.__valorMinuto = 90
            self.__tipoVehiculo = "Auto"
        elif ruedas > 4:
            self.__valorMinuto = 150
            self.__tipoVehiculo = "Camión"
        else:
            self.__valorMinuto = 0
            self.__tipoVehiculo = "N/C"
            # raise ValueError("Tipo erro, la cantidad de ruedas no corresponde") 
            # ojo, a veces no es recomentable usa raise en ciertas partes del programa. Raise hace que se caiga el programa.


    @property
    def ruedas(self):
        return self.__ruedas

    @property
    def tipoVehiculo(self):
        return self.__tipoVehiculo
    
    @property
    def valorMinuto(self):
        return self.__valorMinuto




class Vehiculo:
    def __init__(self, patente, ruedas):
        self.__patente = patente
        self.__queVehiculoSoy = Tipo(ruedas) # esto es un atributo y a la vez un objeto de la otra clase de arriba en Tipo
        self.__minutosEstacionado = 0
        

    @property
    def patente(self):
        return self.__patente


    @property
    def ruedas(self):
        return self.__ruedas
    
    @property
    def minutosEstacionado(self):
        return self.__minutosEstacionado
    
    @minutosEstacionado.setter
    def minutosEstacionado(self, minutos):
        if minutos >= 0:
            self.__minutosEstacionado = minutos

    def tipoVehiculo(self):
        #return self.__tipoVehiculo.tipoVehiculo # aqui estamos llamando a la asociacion
        return self.__queVehiculoSoy.tipoVehiculo

    def totalPagar(self):
        return self.__minutosEstacionado * self.__queVehiculoSoy.valorMinuto
    














    # def __conexionBDD(self): # esto significa que la conexión es privada
    # pass

    # metodos y variables son privadas.



# ----------------------------------

v1 = Vehiculo("AAAA-11", 8)
# v1.minutosEstacionado = 1 # un minuto
v1.minutosEstacionado = 5


print("Patente :", v1.patente, "->", v1.tipoVehiculo(), ", total pagar -> ", v1.totalPagar())
print("Minutos estacionados -> " , v1.minutosEstacionado, "Pagar -> ", v1.totalPagar())




#t = Tipo(4)
#print(t.tipoVehiculo, " valor x minuto", t.valorMinuto)


# t = Tipo(ruedas = -7)
# print(t.tipoVehiculo)
# salida N/C


# t = Tipo(ruedas = 8)
# print(t.tipoVehiculo)
# salida Camión





















# buscar que son las normas por convesión.


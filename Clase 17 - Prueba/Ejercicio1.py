
# clase cliente -------------------------------------------------------------------------------------
class Cliente:
    def __init__(self, rut: str):
        if len(rut) != 13:
            raise ValueError("El rut debe tener 13 digitos. Además debe duplicar el ultimo digito de su guión, ejemplo: 12.345.678-99")
        self._rut = rut
        self._correo = None

# ------ getters -------
    @property
    def rut(self):
        return self._rut

    @property
    def correo(self):
        return self._correo

# ------ setters -------
    @correo.setter
    def correo(self, valor):
        if valor is None or valor == "":
            raise ValueError("El correo no puede estar vacío")
        if "@" not in valor:
            raise ValueError("EL correo no es válido. Debe tener un @")
        self._correo = valor


# clase empresa -------------------------------------------------------------------------------------
class Empresa(Cliente): # viene desde la clase cliente
    def __init__(self, rut: str, razonSocial: str):
        Cliente.__init__(self, rut) 
        self._razonSocial = razonSocial
        self._giro = None
        self._direccionComercial = None
        self._repLegal = None

# ------ getters ------
    @property
    def razonSocial(self):
        return self._razonSocial

    @property
    def giro(self):
        return self._giro

    @giro.setter
    def giro(self, valor):
        self._giro = valor

    @property
    def direccionComercial(self):
        return self._direccionComercial

# ------ setters -------
    @direccionComercial.setter
    def direccionComercial(self, valor):
        self._direccionComercial = valor

    @property
    def repLegal(self):
        return self._repLegal

    @repLegal.setter
    def repLegal(self, valor):
        self._repLegal = valor




# clase persona -----------------------------------------------------------------------------------
class Persona(Cliente): # viene desde la clase cliente
    def __init__(self, rut: str, nombre: str):
        Cliente.__init__(self, rut) 
        self._nombre = nombre
        self._direccionParticular = None
        self.celulares = []  # relacion 1 a muchos, porque empieza la lista vacia y se pude llenar con muchos celulares
        
    def agregar_celular(self, celular):
        self.celulares.append(celular)

# ----- getters -------
    @property
    def nombre(self):
        return self._nombre

    @property
    def direccionParticular(self):
        return self._direccionParticular

# ------ setters ------
    @direccionParticular.setter
    def direccionParticular(self, valor):
        self._direccionParticular = valor





# clase telefono ----------------------------------------------------------------------------------
class Telefono:
    def __init__(self, numero: str):
        self._numero = numero

    def llamar(self, fecha: str, hora: str, numero: str, minutosHablados: int) -> bool:
        print(f"Llamando a {numero} el {fecha} a las {hora} por {minutosHablados} minutos.")
        return True
    

# ----- getter -------
    @property
    def numero(self):
        return self._numero



# clase celular prepago --------------------------------------------------------------------------
# heredada de telefono
class CelularPrepago(Telefono): # viene desde la clase telefono
    def __init__(self, numero: str, imei: str):
        Telefono.__init__(self, numero) 
        self._imei = imei
        self._fechaCompra = None
        self._minutos = 0
        self._saldo = 0
        self._megas = 0
        self._detalleLlamados = []

    def navegar(self, megas: int) -> int:
        if megas <= 0:
            print("La cantidad de megas debe ser mayor a 0")
            return False
        
        # cada mega cuesta 10 pesos
        costo = megas * 10  
        if costo > self._saldo:
            print(f"No tienes suficiente saldo, saldo actual: ${self._saldo}")
            return False
        
        self._saldo -= costo
        self._megas += megas  
        print(f"Navegaste {megas} megas, gastando ${costo} pesos. Saldo restante: ${self._saldo}")
        return True

    def cargar(self, monto: float) -> bool:
        if monto < 1500:
            print(f"Monto cargado: ${monto} pesos, (el monto mínimo debe ser $1500 pesos)")
            return False
        self._saldo += monto
        print(f"Se cargaron: ${monto}. Saldo actual: ${self._saldo}")
        return True

    def llamar(self, fecha: str, hora: str, numero: str, minutosHablados: int) -> bool:
            # Debe restar 30 pesos al saldo por cada minuto hablado
            costo = minutosHablados * 30 
            if costo > self._saldo:
                print(f"No tienes saldo suficiente para llamar: {minutosHablados} minutos. Saldo: ${self._saldo} pesos, costo: ${costo} pesos")
                return False
            self._saldo -= costo
            self._minutos += minutosHablados
            self._detalleLlamados.append({
                "fecha": fecha,
                "hora": hora,
                "numero": numero,
                "minutosHablados": minutosHablados
            })
            print(f"Llamada realizada a {numero} por {minutosHablados} minutos. Saldo restante: ${self._saldo}")
            return True


    def reiniciar(self) -> bool:
        self._minutos = 0
        self._megas = 0
        self._saldo = 0
        self._detalleLlamados = []
        print("Celular reiniciado.")
        return True
    

# ----- getter -------
    @property
    def imei(self):
        return self._imei

    @property
    def fechaCompra(self):
        return self._fechaCompra
    
    @property
    def minutos(self):
        return self._minutos

    @property
    def saldo(self):
        return self._saldo

    @property
    def megas(self):
        return self._megas
    
    @property
    def detalleLlamados(self):
        return self._detalleLlamados

# ----- setter -------
    @fechaCompra.setter
    def fechaCompra(self, valor):
        if valor is not None and len(valor) >= 10:
            self._fechaCompra = valor




# probando codigo  ----------------------------------------------------------------------------------------------
print("\n-------------------- Datos ---------------------------")

# persona 1

p1 = Persona("12.345.678-11", "Manzanita")
print("Usuario:",p1.nombre)
p1.correo = "manzanita@gmail.com"
p1.direccionParticular = "Manuel Rodriguez"
cel1 = CelularPrepago("987654321", "IMEI12345")
cel1.cargar(10000)
cel1.navegar(150)
cel1.llamar("2025-10-28", "10:00", "912345678", 20)  
cel1.llamar("2025-10-28", "11:00", "923456789", 50) 

print("\n")

# persona 2
p2 = Persona("12.345.678-99", "Juan")
print("Usuario:",p2.nombre)
p2.correo = "Juanj@gmail.com"
p2.direccionParticular = "Las rejas sur"
cel2 = CelularPrepago("987654321", "IMEI12345")
cel2.cargar(1000)
cel2.navegar(50)
cel2.llamar("2025-10-28", "12:30", "945678901", 30)  



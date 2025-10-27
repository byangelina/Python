

class Personaje:

# crear el método
    # el def __init__ es nuestro constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida): # self es un argumento que hace referencia a si mismo (al objeto "Personaje")
        self.nombre = nombre # a través del def haré que todos los atributos creados arriba guarden el valor que reciban a través de lo que pida imprimir, nombre en vez de ser Default, será el nombre que le asigne al imprimir, y así con todos los atributos.
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print("-----", self.nombre, "-----", sep="")
        print("Fuerza:",self.fuerza)
        print("Inteligencia:",self.inteligencia)
        print("Defensa:",self.defensa)
        print("Vida:",self.vida)
        
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    # aqui vamos a evaluar si nuestro personaje está vivo o muerto
    def esta_vivo(self):
        return self.vida > 0  # si esta vivo devolverá True, si está muerto devolverá False

    def morir(self):
        self.vida <= 0 
        print(self.nombre,"ha muerto")

    # aqui vamos a crear cuando daño le hace nuestro personaje a otro personaje
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("La vida de", enemigo.nombre, "es", enemigo.vida,"\n")

mi_personaje = Personaje("\nAngela", 100, 70, 50, -10) # lo que hay aca adento son los argumentos
mi_enemigo = Personaje("Enemy Stando", 8, 5, 3, -5)
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()

mi_personaje.atributos()
mi_personaje.subir_nivel(1,2,0)
mi_personaje.atributos()


#-----------------------------------------------------------------------

# print("El nombre de mi personaje es:",mi_personaje.nombre)
# print("La fuerza de mi personaje es:",mi_personaje.fuerza)

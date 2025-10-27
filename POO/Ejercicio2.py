
# calculadora


import math 

class Calculadora:

    def __init__(self):
        print("\nCalculadora")

    def sumar(self,a,b): # 1
        return a + b

    def restar(self,a,b): # 2
        return a - b

    def multiplicar (self,a,b): # 3
        return a * b

    def dividir(self,a,b): # 4
        if b == 0:
            return "Error, no se puede dividir por cero"
        return a / b
    
    def promediar(self,a,b): # 5
        return (a + b) / 2

    def porcentuar(self,a,b): # 6
        return (a * b) / 100
    
    def trigonometria(self, angulo): # 7
        seno = math.sin(math.radians(angulo))
        coseno = math.cos(math.radians(angulo))
        tangente = math.tan(math.radians(angulo))
        return f"Seno: {seno:.4f}, Coseno: {coseno:.4f}, Tangente: {tangente:.4f}"


# --------------------------------------------------------------------

calc = Calculadora()
print("""
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Promediar
6. Porcentaje
7. Trigonometría
""")

operacion = int(input("Elige la operación que deseas hacer (1-7): "))
if operacion in [1,2,3,4,5,6,7]: 
    a = float(input("Ingresa el primer numero: "))
    b = float(input("Ingresa el segundo número: "))

if operacion == 1:
    resultado = calc.sumar(a,b)
elif operacion == 2:
    resultado = calc.restar(a,b)
elif operacion == 3:
    resultado = calc.multiplicar(a,b)
elif operacion == 4:
    resultado = calc.dividir(a,b)
elif operacion == 5:
    resultado = calc.porcentuar(a,b)
elif operacion == 6:
    resultado = calc.promediar(a,b)
elif operacion == 7:
    angulo = float(input("Ingresa el ángulo en grados: "))
    resultado = calc.trigonometria(angulo)
else:
    resultado = "Operación no válida, intente nuevamente."

print("resultado: ",resultado)

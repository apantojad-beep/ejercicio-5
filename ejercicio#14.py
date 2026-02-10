class Numero:
    def __init__(self, valor):
        self.valor = valor
        self.cuadrado = 0
        self.cubo = 0

    def calcular(self):
        self.cuadrado = self.valor ** 2
        self.cubo = self.valor ** 3

    def mostrar_resultados(self):
        print("NÚMERO:", self.valor)
        print("CUADRADO:", self.cuadrado)
        print("CUBO:", self.cubo)


numero_ingresado = float(input("Ingrese un número: "))

num = Numero(numero_ingresado)
num.calcular()
num.mostrar_resultados()

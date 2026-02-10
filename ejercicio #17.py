import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.area = 0
        self.circunferencia = 0

    def calcular(self):
        self.area = round(math.pi * self.radio ** 2, 2)
        self.circunferencia = round(2 * math.pi * self.radio, 2)

    def mostrar_resultados(self):
        print("RADIO:", self.radio)
        print("ÁREA DEL CÍRCULO:", self.area)
        print("LONGITUD DE LA CIRCUNFERENCIA:", self.circunferencia)


radio_ingresado = float(input("Ingrese el radio del círculo: "))

circulo = Circulo(radio_ingresado)
circulo.calcular()
circulo.mostrar_resultados()

class Empleado:
    def __init__(self, horas_trabajadas, valor_hora):
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.salario_bruto = 0
        self.retencion = 0
        self.salario_neto = 0

    def calcular_salarios(self):
        self.salario_bruto = self.horas_trabajadas * self.valor_hora
        self.retencion = self.salario_bruto * 0.125
        self.salario_neto = self.salario_bruto - self.retencion

    def mostrar_resultados(self):
        print("SALARIO BRUTO:", self.salario_bruto)
        print("RETENCIÓN EN LA FUENTE:", self.retencion)
        print("SALARIO NETO:", self.salario_neto)


empleado = Empleado(48, 5000)
empleado.calcular_salarios()
empleado.mostrar_resultados()

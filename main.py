class CuentaBancaria:
    def __init__(self):
        self.saldo = 0.0

    def ingresar_datos(self):
        self.saldo = float(input("Ingrese el saldo inicial de la cuenta: "))

    def calcular_interes_anual(self):
        if self.saldo < 10000.00:
            interes = 0.03
        else:
            interes = 0.04
        self.saldo *= (1 + interes)

    def mostrar_saldo_final(self):
        print(f"El saldo final después de un año es: ${self.saldo:.2f}")


# Ejemplo de uso
cuenta = CuentaBancaria()
cuenta.ingresar_datos()
cuenta.calcular_interes_anual()
cuenta.mostrar_saldo_final()


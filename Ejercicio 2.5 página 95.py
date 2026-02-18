from enum import Enum


class TipoCuenta(Enum):
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"


class CuentaBancaria:

    def __init__(self, nombresTitular, apellidosTitular, numeroCuenta, tipoCuenta, interesMensual):
        self.nombresTitular = nombresTitular
        self.apellidosTitular = apellidosTitular
        self.numeroCuenta = numeroCuenta
        self.tipoCuenta = tipoCuenta
        self.interesMensual = interesMensual 
        self.saldo = 0 

    def imprimir(self):
        print("Nombres del titular =", self.nombresTitular)
        print("Apellidos del titular =", self.apellidosTitular)
        print("Número de cuenta =", self.numeroCuenta)
        print("Tipo de cuenta =", self.tipoCuenta.value)
        print("Interés mensual =", self.interesMensual, "%")
        print("Saldo =", self.saldo)

    def consultarSaldo(self):
        print("El saldo actual es =", self.saldo)

    def consignar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            print("Se ha consignado $", valor, ". El nuevo saldo es $", self.saldo)
            return True
        else:
            print("El valor a consignar debe ser mayor que cero.")
            return False

    def retirar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo = self.saldo - valor
            print("Se ha retirado $", valor, ". El nuevo saldo es $", self.saldo)
            return True
        else:
            print("El valor a retirar debe ser menor o igual al saldo actual.")
            return False

    def aplicarInteres(self):
        interes = self.saldo * (self.interesMensual / 100)
        self.saldo = self.saldo + interes
        print("Interés aplicado $", interes)
        print("Saldo con interés $", self.saldo)



if __name__ == "__main__":

    cuenta = CuentaBancaria(
        "Pedro",
        "Pérez",
        123456789,
        TipoCuenta.AHORROS,
        2.5
    )

    cuenta.imprimir()
    cuenta.consignar(200000)
    cuenta.consignar(300000)
    cuenta.aplicarInteres()
    cuenta.retirar(400000)

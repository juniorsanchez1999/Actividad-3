class Cuenta:
    def __init__(self, saldo, tasa_anual):
        self.saldo = saldo
        self.numero_consignaciones = 0
        self.numero_retiros = 0
        self.tasa_anual = tasa_anual
        self.comision_mensual = 0

    def consignar(self, cantidad):
        self.saldo += cantidad
        self.numero_consignaciones += 1

    def retirar(self, cantidad):
        nuevo_saldo = self.saldo - cantidad
        if nuevo_saldo >= 0:
            self.saldo = nuevo_saldo
            self.numero_retiros += 1
        else:
            print("La cantidad a retirar excede el saldo actual.")

    def calcular_interes(self):
        tasa_mensual = self.tasa_anual / 12
        interes_mensual = self.saldo * tasa_mensual
        self.saldo += interes_mensual

    def extracto_mensual(self):
        self.saldo -= self.comision_mensual
        self.calcular_interes()


class CuentaAhorros(Cuenta):
    def __init__(self, saldo, tasa):
        super().__init__(saldo, tasa)
        self.activa = saldo >= 10000

    def retirar(self, cantidad):
        if self.activa:
            super().retirar(cantidad)

    def consignar(self, cantidad):
        if self.activa:
            super().consignar(cantidad)

    def extracto_mensual(self):
        if self.numero_retiros > 4:
            self.comision_mensual += (self.numero_retiros - 4) * 1000
        super().extracto_mensual()
        if self.saldo < 10000:
            self.activa = False

    def imprimir(self):
        print(f"Saldo = ${self.saldo:.3f}")
        print(f"Comisión mensual = ${self.comision_mensual:.3f}")
        print(f"Número de transacciones = {self.numero_consignaciones + self.numero_retiros}")
        print()


class CuentaCorriente(Cuenta):
    def __init__(self, saldo, tasa):
        super().__init__(saldo, tasa)
        self.sobregiro = 0

    def retirar(self, cantidad):
        resultado = self.saldo - cantidad
        if resultado < 0:
            self.sobregiro -= resultado
            self.saldo = 0
        else:
            super().retirar(cantidad)

    def consignar(self, cantidad):
        if self.sobregiro > 0:
            residuo = self.sobregiro - cantidad
            if residuo > 0:
                self.sobregiro = 0
                self.saldo = residuo
            else:
                self.sobregiro = -residuo
                self.saldo = 0
        else:
            super().consignar(cantidad)

    def imprimir(self):
        print(f"Saldo = ${self.saldo:.3f}")
        print(f"Cargo mensual = ${self.comision_mensual:.3f}")
        print(f"Número de transacciones = {self.numero_consignaciones + self.numero_retiros}")
        print(f"Valor de sobregiro = ${self.sobregiro:.3f}")
        print()


class PruebaCuenta:
    @staticmethod
    def main():
        print("Cuenta de ahorros")
        saldo_inicial = float(input("Ingrese saldo inicial: $"))
        tasa = float(input("Ingrese tasa de interés: "))
        cuenta = CuentaAhorros(saldo_inicial, tasa)
        
        cantidad = float(input("Ingrese cantidad a consignar: $"))
        cuenta.consignar(cantidad)
        
        cantidad = float(input("Ingrese cantidad a retirar: $"))
        cuenta.retirar(cantidad)
        
        cuenta.extracto_mensual()
        cuenta.imprimir()

if __name__ == "__main__":
    PruebaCuenta.main()
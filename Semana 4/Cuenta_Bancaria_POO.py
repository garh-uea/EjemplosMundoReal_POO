class CuentaBancaria:
    def __init__(self, titular, saldo):  # Inicializa la cuenta bancaria con un titular y un saldo inicial.
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, monto):  # Realiza un depósito en la cuenta.
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso. Saldo actual: {self.__saldo:.2f}")
        else:
            print("El monto debe ser mayor a 0.")

    def retirar(self, monto):  # Realiza un retiro de la cuenta.
        if monto > self.__saldo:
            print("Saldo insuficiente. Retire un monto menor.")
        elif monto > 0:
            self.__saldo -= monto
            print(f"Retiro exitoso de {monto:.2f}. Saldo actual: {self.__saldo:.2f}")
        else:
            print("El monto debe ser mayor a 0.")

    def mostrar_saldo(self):  # Muestra el saldo actual.
        print(f"Titular: {self.titular} | Saldo: {self.__saldo:.2f}")


class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular, saldo, tasa_interes):  # Inicializa una cuenta de ahorros con una tasa de interés.
        super().__init__(titular, saldo)
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):  # Aplica intereses al saldo actual.
        self.depositar(self._CuentaBancaria__saldo * self.tasa_interes)


# Pruebas del programa.
# Prueba de creación y uso del objeto CuentaBancaria.
cuenta_bancaria = CuentaBancaria("Gustavo Rodríguez", 800.0)
cuenta_bancaria.depositar(100.0)
cuenta_bancaria.retirar(500.0)
cuenta_bancaria.mostrar_saldo()

print("\n============ CUENTA DE AHORROS ============")

# Prueba de creación y uso del objeto CuentaAhorros
cuenta_ahorros = CuentaAhorros("Mariuxi Zambrano", 800.0, tasa_interes=0.2)
cuenta_ahorros.mostrar_saldo()
cuenta_ahorros.aplicar_interes()
cuenta_ahorros.mostrar_saldo()

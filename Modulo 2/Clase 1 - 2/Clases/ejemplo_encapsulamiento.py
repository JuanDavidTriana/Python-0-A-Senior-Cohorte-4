# Ejemplo de encapsulamiento en Python

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular        # Público
        self._saldo = saldo           # Protegido (convención)
        self.__clave = "1234"        # Privado (name mangling)

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto

    def retirar(self, monto):
        if 0 < monto <= self._saldo:
            self._saldo -= monto

    # Getter y setter para el atributo privado
    def get_clave(self):
        return self.__clave
    def set_clave(self, nueva_clave):
        if len(nueva_clave) == 4:
            self.__clave = nueva_clave

# Ejemplo de uso
cuenta = CuentaBancaria("Juan", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
print(cuenta.titular)      # Juan
print(cuenta._saldo)       # 1300 (acceso posible, pero no recomendado)
print(cuenta.get_clave())  # 1234
cuenta.set_clave("5678")
print(cuenta.get_clave())  # 5678 
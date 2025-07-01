# Ejemplo de uso de constructores (__init__) en Python

class Producto:
    def __init__(self, nombre, precio=0.0):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        print(f"Producto: {self.nombre} - Precio: ${self.precio}")

# Ejemplo de uso
p1 = Producto("Mouse", 10.5)
p2 = Producto("Teclado")
p1.mostrar_info()  # Producto: Mouse - Precio: $10.5
p2.mostrar_info()  # Producto: Teclado - Precio: $0.0 
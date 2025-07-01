# Ejemplo simple de clase y objeto en Python

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Ejemplo de uso
persona1 = Persona("Ana", 25)
persona1.saludar()  # Salida: Hola, soy Ana y tengo 25 años. 
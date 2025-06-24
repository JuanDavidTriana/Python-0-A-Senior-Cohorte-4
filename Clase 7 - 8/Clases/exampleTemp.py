class Forma:
    def calcular_area(self):
        raise NotImplementedError("La subclase debe implementar este metodo")

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado
    
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * self.radio * self.radio
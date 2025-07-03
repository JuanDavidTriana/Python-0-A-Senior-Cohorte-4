
class Persona:

    def __init__(self, nombre: str, edad: int, ciudad: str = "Bogota"):

        self._nombre = nombre  # Publicos
        self._edad = edad      # Privado
        self._ciudad = ciudad  # Protegido

    @property
    def edad(self):
        return self.edad
        
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("La edad debe ser positiva")
    
    def saludo(self):
        print(f"Hola mi nombre es {self._nombre} y mi edad es {self._edad} años y vivo en {self._ciudad}")



persona1 = Persona("Juan", 25, "Ibague")
persona1.saludo()
persona1._edad = -5
persona1.saludo()



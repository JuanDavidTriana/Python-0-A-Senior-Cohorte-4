
class Persona:

    def __init__(self, nombre: str, edad: int, ciudad: str = "Bogota"):

        self.nombre = nombre  # Publicos
        self.edad = edad      # Publico
        self._ciudad = ciudad  # Protegido
        self.__password = "12345" # Privado
        
    @property
    def saludo(self):
        print(f"Hola mi nombre es {self.nombre} y mi edad es {self._edad} años y vivo en {self.ciudad}")

    def cumplir_anios(self):
        self.edad += 1

    def cambiar_ciudad(self, nueva_ciudad:str):
        self.ciudad = nueva_ciudad
        print("Se cambio la ciudad")   

    def get_password(self):
        return self.__password

persona1 = Persona("Juan", 25, "Ibague")

print(persona1.get_password())
#print(persona1.__password)
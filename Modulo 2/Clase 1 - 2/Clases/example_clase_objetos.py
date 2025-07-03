class Persona:

    def __init__(self, nombre: str, edad: int, ciudad: str):

        self.nombre = nombre  # Atributo
        self.edad = edad      # Atributo
        self.ciudad = ciudad  # Atributo
        self.saludo()
        
    def saludo(self):
        print(f"Hola mi nombre es {self.nombre} y mi edad es {self.edad} años y vivo en {self.ciudad}")

class Persona2:

    def __init__(self, nombre: str, edad: int):

        self.nombre = nombre  # Atributo
        self.edad = edad      # Atributo
        self.ciudad = "Bogota" 
        
    def saludo(self):

        print(f"Hola mi nombre es {self.nombre} y mi edad es {self.edad} años y vivo en {self.ciudad}")

class Persona3:

    def __init__(self, nombre: str, edad: int, ciudad: str = "Bogota"):

        self.nombre = nombre  # Atributo
        self.edad = edad      # Atributo
        self.ciudad = ciudad 
        
    def saludo(self):
        print(f"Hola mi nombre es {self.nombre} y mi edad es {self.edad} años y vivo en {self.ciudad}")

    def cumplir_anios(self):
        self.edad += 1

    def cambiar_ciudad(self, nueva_ciudad:str):
        self.ciudad = nueva_ciudad
        print("Se cambio la ciudad")   

persona1 = Persona("Juan", 25, "Ibague")
persona1.saludo()

persona2 = Persona2("Ruben", 26)
persona2.saludo()

#persona3 = Persona3("Alejandra", 24, "Cali")
persona3 = Persona3("Alejandra", 24)
persona3.saludo()
persona3.cumplir_anios()
persona3.saludo()
persona3.cambiar_ciudad("Cali")
persona3.saludo()

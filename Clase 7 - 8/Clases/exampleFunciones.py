# Ejemplo de Funciones en Python - Clase 7
# ======================================

# 1. Función básica sin parámetros
def saludar():
    """Función que imprime un saludo"""
    print("¡Hola! Bienvenido a Python")

# 2. Función con parámetros
def saludar_persona(nombre):
    """Función que saluda a una persona específica"""
    print(f"¡Hola {nombre}! ¿Cómo estás?")

# 3. Función con múltiples parámetros
def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo"""
    area = base * altura
    return area

# 4. Función con parámetros por defecto
def saludar_con_edad(nombre, edad=25):
    """Saluda a una persona con su edad (edad por defecto: 25)"""
    print(f"¡Hola {nombre}! Tienes {edad} años")

# 5. Función que retorna múltiples valores
def obtener_info_circulo(radio):
    """Calcula el área y perímetro de un círculo"""
    import math
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    return area, perimetro

# 6. Función con argumentos arbitrarios (*args)
def sumar_numeros(*numeros):
    """Suma una cantidad variable de números"""
    total = 0
    for numero in numeros:
        total += numero
    return total

# 7. Función con argumentos de palabras clave (**kwargs)
def crear_perfil(**datos):
    """Crea un perfil con datos variables"""
    perfil = {}
    for clave, valor in datos.items():
        perfil[clave] = valor
    return perfil

# Ejemplos de uso
if __name__ == "__main__":
    print("=== EJEMPLOS DE FUNCIONES ===\n")
    
    # Llamada a función básica
    print("1. Función básica:")
    saludar()
    print()
    
    # Llamada a función con parámetro
    print("2. Función con parámetro:")
    saludar_persona("Juan")
    print()
    
    # Llamada a función con múltiples parámetros
    print("3. Función con múltiples parámetros:")
    area = calcular_area_rectangulo(5, 3)
    print(f"El área del rectángulo es: {area}")
    print()
    
    # Llamada a función con parámetro por defecto
    print("4. Función con parámetro por defecto:")
    saludar_con_edad("María")
    saludar_con_edad("Carlos", 30)
    print()
    
    # Llamada a función que retorna múltiples valores
    print("5. Función que retorna múltiples valores:")
    area_circulo, perimetro_circulo = obtener_info_circulo(3)
    print(f"Área del círculo: {area_circulo:.2f}")
    print(f"Perímetro del círculo: {perimetro_circulo:.2f}")
    print()
    
    # Llamada a función con argumentos arbitrarios
    print("6. Función con argumentos arbitrarios:")
    suma1 = sumar_numeros(1, 2, 3)
    suma2 = sumar_numeros(10, 20, 30, 40, 50)
    print(f"Suma de 1, 2, 3: {suma1}")
    print(f"Suma de 10, 20, 30, 40, 50: {suma2}")
    print()
    
    # Llamada a función con argumentos de palabras clave
    print("7. Función con argumentos de palabras clave:")
    perfil = crear_perfil(nombre="Ana", edad=28, ciudad="Madrid", profesion="Desarrolladora")
    print(f"Perfil creado: {perfil}")
    print()
    
    print("=== FIN DE EJEMPLOS ===") 
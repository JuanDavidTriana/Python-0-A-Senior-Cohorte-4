# ========================================
# EJEMPLO: Variables y Tipos de Datos
# Clase 1 - 2: Fundamentos Básicos
# ========================================

# ========================================
# 1. STRINGS (Texto)
# ========================================

print("=== STRINGS ===")

# Strings con comillas simples
nombre = 'Juan David'
ciudad = 'Bogotá'

# Strings con comillas dobles
mensaje = "¡Hola mundo!"
frase = "Python es genial"

# Strings multilínea
texto_largo = """Este es un texto
que puede ocupar
múltiples líneas"""

# Concatenación de strings
nombre_completo = nombre + " " + "Triana"
print("Nombre completo:", nombre_completo)

# Formateo de strings (f-strings)
edad = 25
altura = 1.75
print(f"Me llamo {nombre} y tengo {edad} años")
print(f"Mi altura es {altura} metros")

# Métodos de strings
texto = "  Python es genial  "
print("Texto original:", texto)
print("En mayúsculas:", texto.upper())
print("En minúsculas:", texto.lower())
print("Sin espacios:", texto.strip())
print("Longitud:", len(texto))

# ========================================
# 2. NÚMEROS ENTEROS (int)
# ========================================

print("\n=== NÚMEROS ENTEROS ===")

edad = 25
año = 2024
temperatura = -5
poblacion = 8000000

print("Edad:", edad, type(edad))
print("Año:", año, type(año))
print("Temperatura:", temperatura, type(temperatura))
print("Población:", poblacion, type(poblacion))

# Operaciones con enteros
a = 10
b = 3
print(f"a = {a}, b = {b}")
print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
print(f"División: {a / b}")  # Resultado es float
print(f"División entera: {a // b}")
print(f"Módulo: {a % b}")
print(f"Potencia: {a ** b}")

# ========================================
# 3. NÚMEROS DE PUNTO FLOTANTE (float)
# ========================================

print("\n=== NÚMEROS FLOTANTES ===")

altura = 1.75
peso = 70.5
pi = 3.14159
temperatura = -2.5

print("Altura:", altura, type(altura))
print("Peso:", peso, type(peso))
print("Pi:", pi, type(pi))
print("Temperatura:", temperatura, type(temperatura))

# Operaciones con flotantes
x = 10.5
y = 3.2
print(f"x = {x}, y = {y}")
print(f"Suma: {x + y}")
print(f"Resta: {x - y}")
print(f"Multiplicación: {x * y}")
print(f"División: {x / y}")

# ========================================
# 4. BOOLEANOS (bool)
# ========================================

print("\n=== BOOLEANOS ===")

es_estudiante = True
es_profesor = False
mayor_de_edad = True

print("¿Es estudiante?", es_estudiante, type(es_estudiante))
print("¿Es profesor?", es_profesor, type(es_profesor))
print("¿Es mayor de edad?", mayor_de_edad, type(mayor_de_edad))

# Operaciones con booleanos
print("\nOperaciones lógicas:")
print("True and True:", True and True)
print("True and False:", True and False)
print("True or False:", True or False)
print("False or False:", False or False)
print("not True:", not True)
print("not False:", not False)

# ========================================
# 5. VERIFICACIÓN DE TIPOS
# ========================================

print("\n=== VERIFICACIÓN DE TIPOS ===")

# Crear variables de diferentes tipos
texto = "Hola"
numero_entero = 42
numero_decimal = 3.14
es_verdadero = True

# Verificar tipos
print("texto:", texto, "->", type(texto))
print("numero_entero:", numero_entero, "->", type(numero_entero))
print("numero_decimal:", numero_decimal, "->", type(numero_decimal))
print("es_verdadero:", es_verdadero, "->", type(es_verdadero))

# ========================================
# 6. CONVERSIÓN DE TIPOS
# ========================================

print("\n=== CONVERSIÓN DE TIPOS ===")

# String a número
numero_texto = "42"
numero = int(numero_texto)
decimal = float(numero_texto)

print("Texto original:", numero_texto, type(numero_texto))
print("Convertido a int:", numero, type(numero))
print("Convertido a float:", decimal, type(decimal))

# Número a string
numero = 123
texto = str(numero)
print("Número original:", numero, type(numero))
print("Convertido a string:", texto, type(texto))

# Booleanos
print("bool(0):", bool(0))      # False
print("bool(1):", bool(1))      # True
print("bool(''):", bool(''))    # False
print("bool('Hola'):", bool('Hola'))  # True

# ========================================
# 7. EJEMPLOS PRÁCTICOS
# ========================================

print("\n=== EJEMPLOS PRÁCTICOS ===")

# Ejemplo 1: Calculadora de edad
año_nacimiento = 1995
año_actual = 2024
edad = año_actual - año_nacimiento

print(f"Naciste en {año_nacimiento}")
print(f"El año actual es {año_actual}")
print(f"Tienes {edad} años")

# Ejemplo 2: Información personal
nombre = "María"
apellido = "García"
altura = 1.65
es_programadora = True

print(f"Nombre: {nombre} {apellido}")
print(f"Altura: {altura} metros")
print(f"¿Es programadora? {es_programadora}")

# Ejemplo 3: Cálculos matemáticos
radio = 5.0
pi = 3.14159
area_circulo = pi * radio ** 2
perimetro_circulo = 2 * pi * radio

print(f"Radio del círculo: {radio}")
print(f"Área del círculo: {area_circulo}")
print(f"Perímetro del círculo: {perimetro_circulo}")

# Ejemplo 4: Verificación de datos
temperatura = 25.5
es_alta = temperatura > 30
es_baja = temperatura < 10
es_normal = not es_alta and not es_baja

print(f"Temperatura: {temperatura}°C")
print(f"¿Es alta? {es_alta}")
print(f"¿Es baja? {es_baja}")
print(f"¿Es normal? {es_normal}")

print("\n¡Fin del ejemplo de variables y tipos de datos!") 
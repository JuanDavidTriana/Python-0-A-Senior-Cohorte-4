# ========================================
# EJEMPLO: Introducción a Python
# Clase 1 - 2: Fundamentos Básicos
# ========================================

# Este es tu primer programa en Python
print("¡Hola Mundo!")
print("Bienvenido a Python 0 a Senior")

# Comentarios en Python
# Los comentarios comienzan con # y no se ejecutan
# Son útiles para explicar el código

"""
Este es un comentario multilínea
Puedes escribir varias líneas
entre comillas triples
"""

# Variables básicas
nombre = "Juan David"
edad = 25
altura = 1.75
es_estudiante = True

# Mostrar información
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura, "metros")
print("¿Es estudiante?", es_estudiante)

# Verificar tipos de datos
print("\nTipos de datos:")
print("nombre:", type(nombre))
print("edad:", type(edad))
print("altura:", type(altura))
print("es_estudiante:", type(es_estudiante))

# Operaciones básicas
print("\nOperaciones básicas:")
a = 10
b = 3

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Módulo:", a % b)
print("Potencia:", a ** b)

# Comparaciones
print("\nComparaciones:")
print("¿a es mayor que b?", a > b)
print("¿a es igual a b?", a == b)
print("¿a es diferente de b?", a != b)

# Operadores lógicos
print("\nOperadores lógicos:")
x = True
y = False

print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# Conversión de tipos
print("\nConversión de tipos:")
numero_texto = "42"
numero = int(numero_texto)
decimal = float(numero_texto)

print("Texto original:", numero_texto, type(numero_texto))
print("Convertido a int:", numero, type(numero))
print("Convertido a float:", decimal, type(decimal))

# Ejemplo práctico: Calculadora simple
print("\n=== Calculadora Simple ===")
base = 5
altura = 3
area = base * altura

print(f"Base: {base}")
print(f"Altura: {altura}")
print(f"Área del rectángulo: {area}")

# Ejemplo: Información personal
print("\n=== Información Personal ===")
nombre_completo = "María García"
profesion = "Desarrolladora"
años_experiencia = 2
domina_python = True

print(f"Nombre: {nombre_completo}")
print(f"Profesión: {profesion}")
print(f"Años de experiencia: {años_experiencia}")
print(f"¿Domina Python? {domina_python}")

print("\n¡Fin del ejemplo de introducción!") 
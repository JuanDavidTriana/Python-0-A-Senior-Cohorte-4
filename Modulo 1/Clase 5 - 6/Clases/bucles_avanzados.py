# ========================================
# EJEMPLOS DE BUCLES AVANZADOS
# ========================================

print("=== BUCLES AVANZADOS ===\n")

# Ejemplo 1: Bucles anidados - Tabla de multiplicar
print("1. Tabla de multiplicar completa:")
for i in range(1, 6):
    print(f"  Tabla del {i}:")
    for j in range(1, 11):
        print(f"    {i} x {j} = {i * j}")
    print()

print("="*50 + "\n")

# Ejemplo 2: List comprehension
print("2. List comprehensions:")
# Cuadrados de números del 1 al 10
cuadrados = [x**2 for x in range(1, 11)]
print(f"  Cuadrados: {cuadrados}")

# Números pares del 1 al 20
pares = [x for x in range(1, 21) if x % 2 == 0]
print(f"  Pares: {pares}")

# Vocales en una palabra
palabra = "Python Programming"
vocales = [letra for letra in palabra if letra.lower() in 'aeiou']
print(f"  Vocales en '{palabra}': {vocales}")

print("\n" + "="*50 + "\n")

# Ejemplo 3: Bucle con enumerate y zip
print("3. Enumerate y zip:")
estudiantes = ["Ana", "Carlos", "María", "Juan"]
notas = [85, 92, 78, 95]

print("  Notas de estudiantes:")
for i, (estudiante, nota) in enumerate(zip(estudiantes, notas), 1):
    print(f"    {i}. {estudiante}: {nota}")

print("\n" + "="*50 + "\n")

# Ejemplo 4: Bucle while con break y continue
print("4. Bucle while con control de flujo:")
contador = 0
suma = 0

while True:
    contador += 1
    
    if contador > 10:
        break
    
    if contador % 2 == 0:
        continue
    
    suma += contador
    print(f"  Número impar: {contador}, Suma acumulada: {suma}")

print(f"  Suma final de impares: {suma}")

print("\n" + "="*50 + "\n")

# Ejemplo 5: Bucle con diccionarios
print("5. Iterando diccionarios:")
persona = {
    "nombre": "Juan",
    "edad": 25,
    "profesion": "Desarrollador",
    "lenguajes": ["Python", "JavaScript", "Java"]
}

print("  Información de la persona:")
for clave, valor in persona.items():
    if isinstance(valor, list):
        print(f"    {clave}: {', '.join(valor)}")
    else:
        print(f"    {clave}: {valor}")

print("\n" + "="*50 + "\n")

# Ejemplo 6: Bucle con range y step
print("6. Rangos con diferentes pasos:")
print("  Contando de 10 en 10:")
for i in range(0, 101, 10):
    print(f"    {i}")

print("\n  Contando hacia atrás:")
for i in range(10, 0, -1):
    print(f"    {i}")

print("\n" + "="*50 + "\n")

# Ejemplo 7: Bucle con filtros
print("7. Filtros en bucles:")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Números mayores a 5
mayores_5 = [num for num in numeros if num > 5]
print(f"  Números mayores a 5: {mayores_5}")

# Números que son múltiplos de 3
multiplos_3 = [num for num in numeros if num % 3 == 0]
print(f"  Múltiplos de 3: {multiplos_3}")

print("\n" + "="*50 + "\n")

# Ejemplo 8: Bucle con matrices (listas anidadas)
print("8. Trabajando con matrices:")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("  Matriz:")
for fila in matriz:
    print(f"    {fila}")

print("\n  Suma de cada fila:")
for i, fila in enumerate(matriz):
    suma_fila = sum(fila)
    print(f"    Fila {i+1}: {suma_fila}")

print("\n" + "="*50 + "\n")

# Ejemplo 9: Bucle con generadores
print("9. Generadores:")
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("  Secuencia de Fibonacci (primeros 10 números):")
for num in fibonacci(10):
    print(f"    {num}")

print("\n" + "="*50 + "\n")

# Ejemplo 10: Bucle con try-except
print("10. Bucle con manejo de errores:")
datos = ["1", "2", "abc", "4", "5"]
suma = 0

for dato in datos:
    try:
        numero = int(dato)
        suma += numero
        print(f"    Sumando: {numero}")
    except ValueError:
        print(f"    Error: '{dato}' no es un número válido")

print(f"  Suma total: {suma}")

print("\n" + "="*50 + "\n")

# Ejemplo 11: Bucle con else
print("11. Bucle con cláusula else:")
for i in range(5):
    if i == 3:
        print(f"    Encontrado el número 3")
        break
    print(f"    Número: {i}")
else:
    print("    No se encontró el número 3")

print("\n" + "="*50 + "\n")

# Ejemplo 12: Bucle con funciones lambda
print("12. Funciones lambda en bucles:")
numeros = [1, 2, 3, 4, 5]

# Aplicar función lambda a cada número
resultados = list(map(lambda x: x**2 + 1, numeros))
print(f"  Números originales: {numeros}")
print(f"  Después de x² + 1: {resultados}")

# Filtrar con lambda
mayores_2 = list(filter(lambda x: x > 2, numeros))
print(f"  Números mayores a 2: {mayores_2}")

print("\n=== FIN DE BUCLES AVANZADOS ===") 
# ========================================
# EJERCICIOS PRÁCTICOS - CONDICIONALES Y BUCLES
# ========================================

print("=== EJERCICIOS PRÁCTICOS ===\n")

# Ejercicio 1: Contador de números pares e impares
print("EJERCICIO 1: Contador de números pares e impares")
print("-" * 50)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = 0
impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")

print("\n" + "="*60 + "\n")

# Ejercicio 2: Calculadora de calificaciones
print("EJERCICIO 2: Calculadora de calificaciones")
print("-" * 50)

notas = [85, 92, 78, 95, 88, 76, 90, 87]
suma = 0
aprobados = 0
reprobados = 0

for nota in notas:
    suma += nota
    if nota >= 70:
        aprobados += 1
    else:
        reprobados += 1

promedio = suma / len(notas)
print(f"Promedio: {promedio:.2f}")
print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")

print("\n" + "="*60 + "\n")

# Ejercicio 3: Buscador de números primos
print("EJERCICIO 3: Buscador de números primos")
print("-" * 50)

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numeros_prueba = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
primos = []

for numero in numeros_prueba:
    if es_primo(numero):
        primos.append(numero)

print(f"Números primos encontrados: {primos}")

print("\n" + "="*60 + "\n")

# Ejercicio 4: Analizador de texto
print("EJERCICIO 4: Analizador de texto")
print("-" * 50)

texto = "Python es un lenguaje de programación increíble"
vocales = 0
consonantes = 0
espacios = 0

for caracter in texto.lower():
    if caracter in 'aeiou':
        vocales += 1
    elif caracter.isalpha():
        consonantes += 1
    elif caracter == ' ':
        espacios += 1

print(f"Texto: '{texto}'")
print(f"Vocales: {vocales}")
print(f"Consonantes: {consonantes}")
print(f"Espacios: {espacios}")

print("\n" + "="*60 + "\n")

# Ejercicio 5: Generador de patrones
print("EJERCICIO 5: Generador de patrones")
print("-" * 50)

# Patrón de asteriscos
for i in range(1, 6):
    print("*" * i)

print()

# Patrón de números
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n" + "="*60 + "\n")

# Ejercicio 6: Calculadora de factorial
print("EJERCICIO 6: Calculadora de factorial")
print("-" * 50)

def factorial(n):
    if n < 0:
        return "No definido para números negativos"
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

numeros_factorial = [0, 1, 5, 7, 10]
for numero in numeros_factorial:
    print(f"Factorial de {numero}: {factorial(numero)}")

print("\n" + "="*60 + "\n")

# Ejercicio 7: Juego de adivinanza
print("EJERCICIO 7: Juego de adivinanza")
print("-" * 50)

import random

numero_secreto = random.randint(1, 100)
intentos = 0
max_intentos = 7

print("Adivina el número entre 1 y 100")
print(f"Tienes {max_intentos} intentos")

while intentos < max_intentos:
    intentos += 1
    try:
        adivinanza = int(input(f"Intento {intentos}: "))
        
        if adivinanza < numero_secreto:
            print("El número es mayor")
        elif adivinanza > numero_secreto:
            print("El número es menor")
        else:
            print(f"¡Correcto! El número era {numero_secreto}")
            print(f"Lo lograste en {intentos} intentos")
            break
    except ValueError:
        print("Por favor ingresa un número válido")
        intentos -= 1
else:
    print(f"Se acabaron los intentos. El número era {numero_secreto}")

print("\n" + "="*60 + "\n")

# Ejercicio 8: Ordenador de listas
print("EJERCICIO 8: Ordenador de listas")
print("-" * 50)

def ordenar_lista(lista):
    # Algoritmo de burbuja simple
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

numeros_desordenados = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {numeros_desordenados}")
lista_ordenada = ordenar_lista(numeros_desordenados.copy())
print(f"Lista ordenada: {lista_ordenada}")

print("\n" + "="*60 + "\n")

# Ejercicio 9: Calculadora de estadísticas
print("EJERCICIO 9: Calculadora de estadísticas")
print("-" * 50)

datos = [12, 15, 18, 22, 25, 28, 30, 35, 40, 45]

if datos:
    suma = sum(datos)
    promedio = suma / len(datos)
    minimo = min(datos)
    maximo = max(datos)
    
    # Mediana
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    if n % 2 == 0:
        mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
    else:
        mediana = datos_ordenados[n//2]
    
    print(f"Datos: {datos}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Mínimo: {minimo}")
    print(f"Máximo: {maximo}")
    print(f"Mediana: {mediana}")

print("\n" + "="*60 + "\n")

# Ejercicio 10: Validador de contraseñas
print("EJERCICIO 10: Validador de contraseñas")
print("-" * 50)

def validar_password(password):
    errores = []
    
    if len(password) < 8:
        errores.append("Debe tener al menos 8 caracteres")
    
    if not any(c.isupper() for c in password):
        errores.append("Debe tener al menos una mayúscula")
    
    if not any(c.islower() for c in password):
        errores.append("Debe tener al menos una minúscula")
    
    if not any(c.isdigit() for c in password):
        errores.append("Debe tener al menos un número")
    
    if not any(c in "!@#$%^&*" for c in password):
        errores.append("Debe tener al menos un carácter especial (!@#$%^&*)")
    
    return len(errores) == 0, errores

passwords_prueba = ["abc123", "Password123", "MyPass123!", "weak"]
for password in passwords_prueba:
    es_valida, errores = validar_password(password)
    print(f"Contraseña: '{password}'")
    if es_valida:
        print("  ✅ Válida")
    else:
        print("  ❌ Inválida:")
        for error in errores:
            print(f"    - {error}")
    print()

print("=== FIN DE EJERCICIOS PRÁCTICOS ===") 
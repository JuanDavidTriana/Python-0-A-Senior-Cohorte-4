# ========================================
# EJEMPLOS DE BUCLES BÁSICOS
# ========================================

print("=== BUCLES BÁSICOS ===\n")

# Ejemplo 1: Bucle for con range
print("1. Contando del 1 al 5:")
for i in range(1, 6):
    print(f"  Número: {i}")

print("\n" + "="*50 + "\n")

# Ejemplo 2: Bucle for con lista
frutas = ["manzana", "banana", "naranja", "uva"]
print("2. Lista de frutas:")
for fruta in frutas:
    print(f"  - {fruta}")

print("\n" + "="*50 + "\n")

# Ejemplo 3: Bucle for con enumerate
print("3. Frutas con índice:")
for indice, fruta in enumerate(frutas):
    print(f"  {indice + 1}. {fruta}")

print("\n" + "="*50 + "\n")

# Ejemplo 4: Bucle while básico
print("4. Contando con while:")
contador = 1
while contador <= 5:
    print(f"  Contador: {contador}")
    contador += 1

print("\n" + "="*50 + "\n")

# Ejemplo 5: Bucle for con step (pasos)
print("5. Números pares del 2 al 10:")
for numero in range(2, 11, 2):
    print(f"  {numero}")

print("\n" + "="*50 + "\n")

# Ejemplo 6: Bucle for con string
palabra = "Python"
print(f"6. Letras de '{palabra}':")
for letra in palabra:
    print(f"  - {letra}")

print("\n" + "="*50 + "\n")

# Ejemplo 7: Bucle while con condición
print("7. Adivinando un número:")
numero_secreto = 7
intento = 0
max_intentos = 3

while intento < max_intentos:
    intento += 1
    print(f"  Intento {intento}/{max_intentos}")
    if intento == numero_secreto:
        print("  ¡Correcto! El número era 7")
        break
    else:
        print("  Incorrecto, sigue intentando...")
else:
    print("  Se acabaron los intentos")

print("\n" + "="*50 + "\n")

# Ejemplo 8: Bucle for con diccionario
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Bogotá"
}
print("8. Información de la persona:")
for clave, valor in persona.items():
    print(f"  {clave}: {valor}")

print("\n" + "="*50 + "\n")

# Ejemplo 9: Bucle for con continue
print("9. Números del 1 al 10 (saltando el 5):")
for numero in range(1, 11):
    if numero == 5:
        continue
    print(f"  {numero}")

print("\n" + "="*50 + "\n")

# Ejemplo 10: Bucle anidado
print("10. Tabla de multiplicar del 5:")
for i in range(1, 6):
    resultado = 5 * i
    print(f"  5 x {i} = {resultado}")

print("\n" + "="*50 + "\n")

# Ejemplo 11: Bucle while con input
print("11. Suma de números (ingresa 0 para terminar):")
suma = 0
while True:
    numero = int(input("  Ingresa un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
    print(f"  Suma actual: {suma}")

print(f"  Suma final: {suma}")

print("\n" + "="*50 + "\n")

# Ejemplo 12: Bucle for con zip
nombres = ["Ana", "Carlos", "María"]
edades = [25, 30, 28]
print("12. Nombres y edades:")
for nombre, edad in zip(nombres, edades):
    print(f"  {nombre} tiene {edad} años")

print("\n=== FIN DE BUCLES BÁSICOS ===") 
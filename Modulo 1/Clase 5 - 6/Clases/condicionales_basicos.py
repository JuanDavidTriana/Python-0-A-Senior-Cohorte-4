# ========================================
# EJEMPLOS DE CONDICIONALES BÁSICOS
# ========================================

print("=== CONDICIONALES BÁSICOS ===\n")

# Ejemplo 1: Verificar si un número es positivo, negativo o cero
numero = 15
print(f"Número: {numero}")

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")

print("\n" + "="*50 + "\n")

# Ejemplo 2: Verificar la edad para diferentes categorías
edad = 25
print(f"Edad: {edad} años")

if edad < 13:
    print("Eres un niño")
elif edad < 18:
    print("Eres un adolescente")
elif edad < 65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")

print("\n" + "="*50 + "\n")

# Ejemplo 3: Verificar si un número es par o impar
numero = 7
print(f"Número: {numero}")

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

print("\n" + "="*50 + "\n")

# Ejemplo 4: Comparar dos números
a = 10
b = 20
print(f"a = {a}, b = {b}")

if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else:
    print("a es igual a b")

print("\n" + "="*50 + "\n")

# Ejemplo 5: Verificar si un string está vacío
texto = "Hola Python"
print(f"Texto: '{texto}'")

if texto:
    print("El texto no está vacío")
else:
    print("El texto está vacío")

print("\n" + "="*50 + "\n")

# Ejemplo 6: Verificar múltiples condiciones
temperatura = 25
humedad = 60
print(f"Temperatura: {temperatura}°C, Humedad: {humedad}%")

if temperatura > 30 and humedad > 70:
    print("¡Hace mucho calor y humedad!")
elif temperatura > 25 and humedad > 50:
    print("Hace calor moderado")
elif temperatura < 10:
    print("Hace frío")
else:
    print("El clima está agradable")

print("\n" + "="*50 + "\n")

# Ejemplo 7: Verificar si un número está en un rango
numero = 15
print(f"Número: {numero}")

if 0 <= numero <= 10:
    print("El número está entre 0 y 10")
elif 11 <= numero <= 20:
    print("El número está entre 11 y 20")
elif 21 <= numero <= 30:
    print("El número está entre 21 y 30")
else:
    print("El número está fuera del rango 0-30")

print("\n" + "="*50 + "\n")

# Ejemplo 8: Verificar el tipo de día según la hora
hora = 14
print(f"Hora: {hora}:00")

if 6 <= hora < 12:
    print("Buenos días")
elif 12 <= hora < 18:
    print("Buenas tardes")
elif 18 <= hora < 22:
    print("Buenas noches")
else:
    print("¡Hora de dormir!")

print("\n=== FIN DE CONDICIONALES BÁSICOS ===") 
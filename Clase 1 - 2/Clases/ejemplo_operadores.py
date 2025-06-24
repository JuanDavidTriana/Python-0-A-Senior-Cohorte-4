# ========================================
# EJEMPLO: Operadores en Python
# Clase 1 - 2: Fundamentos Básicos
# ========================================

# ========================================
# 1. OPERADORES ARITMÉTICOS
# ========================================

print("=== OPERADORES ARITMÉTICOS ===")

# Definir variables para operaciones
a = 15
b = 4

print(f"a = {a}, b = {b}")
print("-" * 30)

# Suma
resultado = a + b
print(f"Suma: {a} + {b} = {resultado}")

# Resta
resultado = a - b
print(f"Resta: {a} - {b} = {resultado}")

# Multiplicación
resultado = a * b
print(f"Multiplicación: {a} * {b} = {resultado}")

# División (siempre devuelve float)
resultado = a / b
print(f"División: {a} / {b} = {resultado}")

# División entera
resultado = a // b
print(f"División entera: {a} // {b} = {resultado}")

# Módulo (resto de la división)
resultado = a % b
print(f"Módulo: {a} % {b} = {resultado}")

# Potencia
resultado = a ** b
print(f"Potencia: {a} ** {b} = {resultado}")

# ========================================
# 2. OPERADORES DE ASIGNACIÓN
# ========================================

print("\n=== OPERADORES DE ASIGNACIÓN ===")

x = 10
print(f"Valor inicial: x = {x}")

# Suma y asignación
x += 5  # Equivale a: x = x + 5
print(f"Después de x += 5: x = {x}")

# Resta y asignación
x -= 3  # Equivale a: x = x - 3
print(f"Después de x -= 3: x = {x}")

# Multiplicación y asignación
x *= 2  # Equivale a: x = x * 2
print(f"Después de x *= 2: x = {x}")

# División y asignación
x /= 4  # Equivale a: x = x / 4
print(f"Después de x /= 4: x = {x}")

# Módulo y asignación
x %= 2  # Equivale a: x = x % 2
print(f"Después de x %= 2: x = {x}")

# Potencia y asignación
x = 3
x **= 3  # Equivale a: x = x ** 3
print(f"Después de x **= 3: x = {x}")

# ========================================
# 3. OPERADORES DE COMPARACIÓN
# ========================================

print("\n=== OPERADORES DE COMPARACIÓN ===")

# Definir variables para comparaciones
edad = 18
altura = 1.75
nombre = "Juan"

print(f"edad = {edad}, altura = {altura}, nombre = 'Juan'")
print("-" * 50)

# Igual a
print(f"¿edad == 18? {edad == 18}")
print(f"¿nombre == 'Juan'? {nombre == 'Juan'}")
print(f"¿altura == 1.80? {altura == 1.80}")

# Diferente de
print(f"¿edad != 20? {edad != 20}")
print(f"¿nombre != 'María'? {nombre != 'María'}")

# Mayor que
print(f"¿edad > 16? {edad > 16}")
print(f"¿altura > 1.80? {altura > 1.80}")

# Menor que
print(f"¿edad < 21? {edad < 21}")
print(f"¿altura < 1.70? {altura < 1.70}")

# Mayor o igual que
print(f"¿edad >= 18? {edad >= 18}")
print(f"¿altura >= 1.75? {altura >= 1.75}")

# Menor o igual que
print(f"¿edad <= 18? {edad <= 18}")
print(f"¿altura <= 1.80? {altura <= 1.80}")

# ========================================
# 4. OPERADORES LÓGICOS
# ========================================

print("\n=== OPERADORES LÓGICOS ===")

# Definir variables booleanas
es_estudiante = True
es_mayor_de_edad = True
tiene_experiencia = False
es_programador = True

print(f"es_estudiante = {es_estudiante}")
print(f"es_mayor_de_edad = {es_mayor_de_edad}")
print(f"tiene_experiencia = {tiene_experiencia}")
print(f"es_programador = {es_programador}")
print("-" * 50)

# AND (Y lógico)
print("Operador AND:")
print(f"es_estudiante and es_mayor_de_edad: {es_estudiante and es_mayor_de_edad}")
print(f"es_estudiante and tiene_experiencia: {es_estudiante and tiene_experiencia}")
print(f"tiene_experiencia and es_programador: {tiene_experiencia and es_programador}")

# OR (O lógico)
print("\nOperador OR:")
print(f"es_estudiante or es_mayor_de_edad: {es_estudiante or es_mayor_de_edad}")
print(f"es_estudiante or tiene_experiencia: {es_estudiante or tiene_experiencia}")
print(f"tiene_experiencia or es_programador: {tiene_experiencia or es_programador}")

# NOT (NO lógico)
print("\nOperador NOT:")
print(f"not es_estudiante: {not es_estudiante}")
print(f"not tiene_experiencia: {not tiene_experiencia}")
print(f"not es_programador: {not es_programador}")

# Combinaciones complejas
print("\nCombinaciones complejas:")
puede_trabajar = es_mayor_de_edad and (es_estudiante or tiene_experiencia)
print(f"¿Puede trabajar? {puede_trabajar}")

es_calificado = (es_estudiante or tiene_experiencia) and es_programador
print(f"¿Está calificado? {es_calificado}")

# ========================================
# 5. PRECEDENCIA DE OPERADORES
# ========================================

print("\n=== PRECEDENCIA DE OPERADORES ===")

# Ejemplo 1: Sin paréntesis
resultado1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {resultado1} (sin paréntesis)")

# Ejemplo 2: Con paréntesis
resultado2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {resultado2} (con paréntesis)")

# Ejemplo 3: Operaciones complejas
a = 10
b = 5
c = 2

resultado3 = a + b * c ** 2
print(f"{a} + {b} * {c} ** 2 = {resultado3}")

resultado4 = (a + b) * c ** 2
print(f"({a} + {b}) * {c} ** 2 = {resultado4}")

# ========================================
# 6. EJEMPLOS PRÁCTICOS
# ========================================

print("\n=== EJEMPLOS PRÁCTICOS ===")

# Ejemplo 1: Calculadora de descuento
precio_original = 100
porcentaje_descuento = 20

descuento = precio_original * (porcentaje_descuento / 100)
precio_final = precio_original - descuento

print(f"Precio original: ${precio_original}")
print(f"Descuento ({porcentaje_descuento}%): ${descuento}")
print(f"Precio final: ${precio_final}")

# Ejemplo 2: Verificación de contraseña
contraseña = "Python123"
longitud_minima = 8
tiene_mayuscula = "P" in contraseña
tiene_numero = "1" in contraseña

es_valida = (len(contraseña) >= longitud_minima and 
             tiene_mayuscula and tiene_numero)

print(f"\nContraseña: {contraseña}")
print(f"¿Tiene longitud mínima? {len(contraseña) >= longitud_minima}")
print(f"¿Tiene mayúscula? {tiene_mayuscula}")
print(f"¿Tiene número? {tiene_numero}")
print(f"¿La contraseña es válida? {es_valida}")

# Ejemplo 3: Verificación de edad para conducir
edad = 17
tiene_licencia = False

puede_conducir = edad >= 18 and tiene_licencia
necesita_licencia = edad >= 18 and not tiene_licencia
es_menor = edad < 18

print(f"\nEdad: {edad}")
print(f"¿Tiene licencia? {tiene_licencia}")
print(f"¿Puede conducir? {puede_conducir}")
print(f"¿Necesita licencia? {necesita_licencia}")
print(f"¿Es menor de edad? {es_menor}")

# Ejemplo 4: Cálculos matemáticos
radio = 5.0
pi = 3.14159

area_circulo = pi * radio ** 2
perimetro_circulo = 2 * pi * radio

print(f"\nRadio del círculo: {radio}")
print(f"Área del círculo: {area_circulo}")
print(f"Perímetro del círculo: {perimetro_circulo}")

# Ejemplo 5: Verificación de temperatura
temperatura = 25.5
es_alta = temperatura > 30
es_baja = temperatura < 10
es_normal = not es_alta and not es_baja

print(f"\nTemperatura: {temperatura}°C")
print(f"¿Es alta? {es_alta}")
print(f"¿Es baja? {es_baja}")
print(f"¿Es normal? {es_normal}")

# ========================================
# 7. OPERADORES DE IDENTIDAD Y PERTENENCIA
# ========================================

print("\n=== OPERADORES DE IDENTIDAD Y PERTENENCIA ===")

# Operador is (identidad)
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"¿a is b? {a is b}")  # False (objetos diferentes)
print(f"¿a is c? {a is c}")  # True (mismo objeto)

# Operador in (pertenencia)
frutas = ["manzana", "banana", "naranja"]
print(f"frutas = {frutas}")
print(f"'manzana' in frutas: {'manzana' in frutas}")
print(f"'pera' in frutas: {'pera' in frutas}")

texto = "Python es genial"
print(f"texto = '{texto}'")
print(f"'Python' in texto: {'Python' in texto}")
print(f"'Java' in texto: {'Java' in texto}")

print("\n¡Fin del ejemplo de operadores!") 
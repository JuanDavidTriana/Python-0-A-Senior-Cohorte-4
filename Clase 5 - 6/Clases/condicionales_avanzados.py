# ========================================
# EJEMPLOS DE CONDICIONALES AVANZADOS
# ========================================

print("=== CONDICIONALES AVANZADOS ===\n")

# Ejemplo 1: Condicionales anidados
print("1. Sistema de calificaciones:")
nota = 85
asistencia = 90

if nota >= 80:
    if asistencia >= 80:
        print("  Excelente - Aprobado con honores")
    else:
        print("  Bueno - Aprobado")
elif nota >= 60:
    if asistencia >= 70:
        print("  Regular - Aprobado")
    else:
        print("  Regular - En riesgo")
else:
    print("  Reprobado")

print("\n" + "="*50 + "\n")

# Ejemplo 2: Operadores lógicos complejos
print("2. Verificación de contraseña:")
password = "Python123"
longitud_ok = len(password) >= 8
tiene_mayuscula = any(c.isupper() for c in password)
tiene_minuscula = any(c.islower() for c in password)
tiene_numero = any(c.isdigit() for c in password)

if longitud_ok and tiene_mayuscula and tiene_minuscula and tiene_numero:
    print("  Contraseña válida")
else:
    print("  Contraseña inválida")
    if not longitud_ok:
        print("    - Debe tener al menos 8 caracteres")
    if not tiene_mayuscula:
        print("    - Debe tener al menos una mayúscula")
    if not tiene_minuscula:
        print("    - Debe tener al menos una minúscula")
    if not tiene_numero:
        print("    - Debe tener al menos un número")

print("\n" + "="*50 + "\n")

# Ejemplo 3: Condicional con múltiples variables
print("3. Sistema de descuentos:")
precio = 150
es_cliente_vip = True
es_primera_compra = False
cantidad = 3

descuento = 0

if es_cliente_vip:
    if cantidad >= 5:
        descuento = 20
    elif cantidad >= 3:
        descuento = 15
    else:
        descuento = 10
elif es_primera_compra:
    descuento = 5
elif cantidad >= 10:
    descuento = 8

precio_final = precio * (1 - descuento / 100)
print(f"  Precio original: ${precio}")
print(f"  Descuento: {descuento}%")
print(f"  Precio final: ${precio_final:.2f}")

print("\n" + "="*50 + "\n")

# Ejemplo 4: Condicional con in y not in
print("4. Verificación de acceso:")
usuarios_autorizados = ["admin", "usuario1", "usuario2"]
usuario_actual = "admin"
funcion = "eliminar"

if usuario_actual in usuarios_autorizados:
    if funcion in ["leer", "escribir"]:
        print("  Acceso permitido")
    elif funcion == "eliminar" and usuario_actual == "admin":
        print("  Acceso permitido (solo admin)")
    else:
        print("  Acceso denegado")
else:
    print("  Usuario no autorizado")

print("\n" + "="*50 + "\n")

# Ejemplo 5: Condicional con operador ternario
print("5. Operador ternario:")
edad = 18
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(f"  {mensaje}")

# Múltiples operadores ternarios
nota = 85
calificacion = "A" if nota >= 90 else "B" if nota >= 80 else "C" if nota >= 70 else "D"
print(f"  Calificación: {calificacion}")

print("\n" + "="*50 + "\n")

# Ejemplo 6: Condicional con is y is not
print("6. Verificación de tipos:")
valor1 = None
valor2 = []
valor3 = ""

if valor1 is None:
    print("  valor1 es None")

if valor2 is not None:
    print("  valor2 no es None")

if valor3 == "":
    print("  valor3 es una cadena vacía")

print("\n" + "="*50 + "\n")

# Ejemplo 7: Condicional con any() y all()
print("7. Verificación de listas:")
numeros = [2, 4, 6, 8, 10]
todos_pares = all(num % 2 == 0 for num in numeros)
alguno_mayor_5 = any(num > 5 for num in numeros)

if todos_pares:
    print("  Todos los números son pares")
else:
    print("  No todos los números son pares")

if alguno_mayor_5:
    print("  Al menos un número es mayor a 5")
else:
    print("  Ningún número es mayor a 5")

print("\n" + "="*50 + "\n")

# Ejemplo 8: Condicional con match (Python 3.10+)
print("8. Estructura match (Python 3.10+):")
comando = "guardar"

# Simulación de match con if-elif
if comando == "crear":
    print("  Creando nuevo archivo...")
elif comando == "abrir":
    print("  Abriendo archivo...")
elif comando == "guardar":
    print("  Guardando archivo...")
elif comando == "eliminar":
    print("  Eliminando archivo...")
else:
    print("  Comando no reconocido")

print("\n" + "="*50 + "\n")

# Ejemplo 9: Condicional con excepciones
print("9. Manejo de errores con condicionales:")
try:
    numero = int("abc")
except ValueError:
    print("  Error: No se pudo convertir a número")
    numero = 0

if numero > 0:
    print(f"  El número es: {numero}")
else:
    print("  El número no es válido")

print("\n" + "="*50 + "\n")

# Ejemplo 10: Condicional complejo con múltiples condiciones
print("10. Sistema de recomendación de películas:")
edad = 25
genero_preferido = "acción"
es_fin_de_semana = True
hora = 20

if edad >= 18:
    if genero_preferido == "acción" and es_fin_de_semana:
        if 18 <= hora <= 23:
            print("  Recomendación: Película de acción para adultos")
        else:
            print("  Recomendación: Película de acción (horario limitado)")
    elif genero_preferido == "comedia":
        print("  Recomendación: Comedia para adultos")
    else:
        print("  Recomendación: Drama o documental")
else:
    if edad >= 13:
        print("  Recomendación: Película para adolescentes")
    else:
        print("  Recomendación: Película familiar")

print("\n=== FIN DE CONDICIONALES AVANZADOS ===") 
# Ejemplo de Listas y Diccionarios en Python - Clase 7
# ===================================================

# 1. Listas - Colecciones ordenadas y mutables
print("=== LISTAS ===")

# Crear listas
frutas = ["manzana", "banana", "naranja", "uva"]
numeros = [1, 2, 3, 4, 5]
mezclada = [1, "hola", 3.14, True]

print(f"Lista de frutas: {frutas}")
print(f"Lista de números: {numeros}")
print(f"Lista mezclada: {mezclada}")

# Acceder a elementos
print(f"Primera fruta: {frutas[0]}")
print(f"Última fruta: {frutas[-1]}")
print(f"Fruta en posición 2: {frutas[2]}")

# Modificar elementos
frutas[1] = "pera"
print(f"Después de modificar: {frutas}")

# Agregar elementos
frutas.append("kiwi")
frutas.insert(1, "fresa")
print(f"Después de agregar: {frutas}")

# Eliminar elementos
frutas.remove("naranja")
ultima = frutas.pop()
print(f"Después de eliminar: {frutas}")
print(f"Elemento eliminado: {ultima}")

# Operaciones con listas
print(f"Longitud de la lista: {len(frutas)}")
print(f"¿'manzana' está en la lista? {'manzana' in frutas}")
print(f"Índice de 'uva': {frutas.index('uva')}")

# Slicing (rebanadas)
print(f"Primeras 3 frutas: {frutas[:3]}")
print(f"Últimas 2 frutas: {frutas[-2:]}")
print(f"Frutas del medio: {frutas[1:3]}")

# Ordenar listas
numeros_desordenados = [3, 1, 4, 1, 5, 9, 2, 6]
numeros_desordenados.sort()
print(f"Números ordenados: {numeros_desordenados}")

frutas.sort(reverse=True)
print(f"Frutas ordenadas al revés: {frutas}")

# List comprehension
cuadrados = [x**2 for x in range(1, 6)]
print(f"Cuadrados del 1 al 5: {cuadrados}")

pares = [x for x in range(10) if x % 2 == 0]
print(f"Números pares del 0 al 9: {pares}")

print("\n" + "="*50 + "\n")

# 2. Diccionarios - Colecciones de pares clave-valor
print("=== DICCIONARIOS ===")

# Crear diccionarios
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid",
    "profesion": "Desarrollador"
}

estudiante = dict(nombre="Ana", edad=20, carrera="Informática")

print(f"Persona: {persona}")
print(f"Estudiante: {estudiante}")

# Acceder a valores
print(f"Nombre de la persona: {persona['nombre']}")
print(f"Edad de la persona: {persona.get('edad')}")
print(f"Email (con valor por defecto): {persona.get('email', 'No especificado')}")

# Modificar y agregar elementos
persona["edad"] = 26
persona["email"] = "juan@email.com"
print(f"Después de modificar: {persona}")

# Eliminar elementos
del persona["profesion"]
email_eliminado = persona.pop("email", None)
print(f"Después de eliminar: {persona}")
print(f"Email eliminado: {email_eliminado}")

# Operaciones con diccionarios
print(f"Claves del diccionario: {list(persona.keys())}")
print(f"Valores del diccionario: {list(persona.values())}")
print(f"Pares clave-valor: {list(persona.items())}")

# Verificar existencia
print(f"¿Tiene 'nombre'? {'nombre' in persona}")
print(f"¿Tiene 'telefono'? {'telefono' in persona}")

# Diccionarios anidados
biblioteca = {
    "libros": [
        {
            "titulo": "El Señor de los Anillos",
            "autor": "J.R.R. Tolkien",
            "año": 1954,
            "genero": "Fantasía"
        },
        {
            "titulo": "1984",
            "autor": "George Orwell",
            "año": 1949,
            "genero": "Ciencia Ficción"
        }
    ],
    "usuarios": {
        "admin": {
            "nombre": "Administrador",
            "rol": "admin",
            "activo": True
        },
        "usuario1": {
            "nombre": "Juan Pérez",
            "rol": "usuario",
            "activo": True
        }
    }
}

print(f"Primer libro: {biblioteca['libros'][0]['titulo']}")
print(f"Admin activo: {biblioteca['usuarios']['admin']['activo']}")

# Dictionary comprehension
cuadrados_dict = {x: x**2 for x in range(1, 6)}
print(f"Cuadrados como diccionario: {cuadrados_dict}")

# Combinar diccionarios
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
combinado = {**dict1, **dict2}
print(f"Diccionarios combinados: {combinado}")

print("\n" + "="*50 + "\n")

# 3. Ejemplos prácticos combinando listas y diccionarios
print("=== EJEMPLOS PRÁCTICOS ===")

# Sistema de calificaciones
estudiantes = [
    {"nombre": "Ana", "calificaciones": [85, 90, 78, 92]},
    {"nombre": "Carlos", "calificaciones": [72, 88, 95, 81]},
    {"nombre": "María", "calificaciones": [90, 85, 88, 94]}
]

# Calcular promedio de cada estudiante
for estudiante in estudiantes:
    promedio = sum(estudiante["calificaciones"]) / len(estudiante["calificaciones"])
    estudiante["promedio"] = round(promedio, 2)
    print(f"{estudiante['nombre']}: {estudiante['promedio']}")

# Encontrar el estudiante con mejor promedio
mejor_estudiante = max(estudiantes, key=lambda x: x["promedio"])
print(f"Mejor estudiante: {mejor_estudiante['nombre']} con {mejor_estudiante['promedio']}")

# Sistema de inventario
inventario = {
    "productos": [
        {"id": 1, "nombre": "Laptop", "precio": 999.99, "stock": 5},
        {"id": 2, "nombre": "Mouse", "precio": 25.50, "stock": 20},
        {"id": 3, "nombre": "Teclado", "precio": 45.00, "stock": 15},
        {"id": 4, "nombre": "Monitor", "precio": 299.99, "stock": 8}
    ]
}

# Filtrar productos con stock bajo
productos_stock_bajo = [p for p in inventario["productos"] if p["stock"] < 10]
print(f"Productos con stock bajo: {[p['nombre'] for p in productos_stock_bajo]}")

# Calcular valor total del inventario
valor_total = sum(p["precio"] * p["stock"] for p in inventario["productos"])
print(f"Valor total del inventario: ${valor_total:.2f}")

# Buscar producto por nombre
def buscar_producto(nombre):
    for producto in inventario["productos"]:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None

producto_encontrado = buscar_producto("laptop")
if producto_encontrado:
    print(f"Producto encontrado: {producto_encontrado}")
else:
    print("Producto no encontrado")

print("\n=== FIN DE EJEMPLOS ===") 
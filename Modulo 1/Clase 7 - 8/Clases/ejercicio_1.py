def saludar_persona(nombre, hora):
    if hora < 12:
        print(f"Buenos dias, {nombre}")
    elif hora < 18:
        print(f"Buenas tardes, {nombre}")
    else:
        print(f"Buenas noches, {nombre} ")

# prueba
saludar_persona("Juan David", 9)
saludar_persona("Alberto", 17)
saludar_persona("Angie", 20)
def validar_password(password):
    if len(password) <= 8:
        return False
    
    tiene_mayusculas = False

    for caracter in password:
        if caracter.isupper():
            tiene_mayusculas = True

        if tiene_mayusculas:
            break

    return tiene_mayusculas

    
password = "hola mundo"

verificador = validar_password(password)

if verificador:
    print("Inicio session")
else:
    print("Error")

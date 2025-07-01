# Funcion con retorno
def calcular_area_rectangulo(base: float, altura:float) -> float:
    '''
    Calcula el área de un rectángulo

    param: base: float
    param: altura: float
    return: float
    '''
    return base * altura

# Funcion con retorno
def calcular_area_rectanguloB(base, altura):
    # Calcula el área de un rectángulo
    return base * altura

# Funcion sin retorno
def calcular_area_rectanguloC(base, altura):
    # Calcula el área de un rectángulo
    print(base * altura)

area1 = calcular_area_rectangulo(5.0 , 3.0)
area2 = calcular_area_rectanguloB(10.0, 2.0)

print(area1)
print(area2)

calcular_area_rectanguloC(5.0, 3.0)

def mostar_memu():
    print("Menu")
    print("1. Opcion 1")
    print("2. Opcion 2")
    print("3. Opcion 3")
    print("4. Opcion 4")
    print("5. Opcion 5")
    print("6. Opcion 6")

def menu():    
    mostar_memu()
    opcion = int(input("Ingrese una opcion: "))
    return opcion

#menu()

def manejar(edad, licencia=False):
    if edad >= 18 and licencia:
        print("Puedes conducir")
    elif edad >= 18 and not licencia:
        print("Necesitas obtener una licencia")
    else:
        print("Eres menor de edad")

manejar(18)
manejar(18, True)

#Funcion lambda(Anonimas)
calcularAreaRectangulo = lambda base, altura: base * altura #Calcula el área de un rectángulo 

area3 = calcularAreaRectangulo(5, 3)
print(area3)

def operar(f, x, y):
    return f(x, y)

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

resultado = operar(dividir, 4, 5) 

print(resultado)

def areaCuadrado(lado):
    return lado * lado

def areaRectangulo(base, altura):
    return base * altura

def areaTriangulo(base, altura):
    return (base * altura) / 2

print (areaCuadrado(5))
print (areaRectangulo(5, 3))
print (areaTriangulo(5, 3))


def mayusculas(f):
    def envoltura(*args, **kwargs):
        resultado = f(*args, **kwargs)
        return resultado.upper()
    return envoltura

@mayusculas
def saludo():
    return "hola mundo"

print(saludo())

session = {
    "usuario_logeado": True
}

def login_required(f):
    def wrapper(*args, **kwargs):
        # ver_panel_de_control("panel de control")
        if session["usuario_logeado"]:
            print("Acceso concedido para", session["usuario_logeado"])
            return f(*args, **kwargs)
        else:
            print("Acceso denegado")
            return None
    return wrapper

@login_required
def ver_panel_de_control():
    print("Panel de control")


ver_panel_de_control()
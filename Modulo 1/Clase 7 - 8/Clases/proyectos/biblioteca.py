from prettytable import PrettyTable

# base de datos en memoria
libros = [
    {
        'isbn': '1',
        'titulo': 'Cien años de soledad',
        'autor': 'Gabriel García Márquez',
        'estado': 'Disponible',
        'socio_prestado': None
    },
    {
        'isbn': '2',
        'titulo': 'Rayuela',
        'autor': 'Julio Cortázar',
        'estado': 'Disponible',
        'socio_prestado': None
    },
    {
        'isbn': '3',
        'titulo': 'La sombra del viento',
        'autor': 'Carlos Ruiz Zafón',
        'estado': 'Disponible',
        'socio_prestado': None
    },
    {
        'isbn': '4',
        'titulo': 'El nombre del viento',
        'autor': 'Patrick Rothfuss',
        'estado': 'Disponible',
        'socio_prestado': None
    },
    {
        'isbn': '5',
        'titulo': 'Ficciones',
        'autor': 'Jorge Luis Borges',
        'estado': 'Disponible',
        'socio_prestado': None
    }
]
socios = []
axuContador = 1

def mostar_menu():
    '''Muestra las opciones de menu'''
    print(" MINIBIBLIOTECA ")
    print("1. Regristar Libro")
    print("2. Registrar un Socio")
    print("3. Prestar Libro")
    print("4. Devolver Libro")
    print("5. Ver libros Pestados")
    print("6. Ver todos los Libros")
    print("7. Ver todos los Socios")
    print("0. Salir")

def registar_libro():
    global libros

    print("================================================================")
    print("Registrar Libros 📖")
    print("================================================================")
    print("Digite 0 si quiere cancelar la creacion")

    titulo = input("Título del libro: ").strip().lower()
    
    if titulo == "0":  return

    if not titulo:
        print("❌ El Título no puede estar vacío ❌")
        return

    autor = input("Autor del Libro: ").strip().lower()

    if autor == "0": return

    if not autor:
        print("❌ El Autor no puede estar vacío ❌")
        return

    isbn = input("ISBN del Libro: ").strip().lower()

    if isbn == "0": return

    if not isbn:
        print("❌ El ISBN no puede estar vacío ❌")
        return
    
    for libro in libros:
        if libro['isbn'] == isbn:
            print(f"❌ Ya existe un libro con el ISBN {isbn} ❌")

    #Crear el nuevo libro
    nuevo_libro = {
        'isbn': isbn,
        'titulo': titulo,
        'autor': autor,
        'estado': 'Disponible',
        'socio_prestado': None
    }

    # nuevo_libro_lista = [isbn,titulo,autor,'Disponible',None]

    libros.append(nuevo_libro)
    print("✅ Libro Registrado Exitosamente 📖")
    print(f"📚 {titulo} - {autor}")
    print(f"ISBN: {isbn}")

    print("================================================================")
    
    

def registar_socio():
    global socios, axuContador

    print("================================================================")
    print("Registrar Socio 👤")
    print("================================================================")
    print("Digite 0 si quiere cancelar la creacion")

    nombre = input("Nombre del socio: ").strip().lower()
    
    if nombre == "0": return

    if not nombre:
        print("❌ El nombre no puede estar vacío ❌")
        return

    apellido = input("Apellido del socio: ").strip().lower()

    if apellido == "0": return

    if not apellido:
        print("❌ El apellido no puede estar vacío ❌")
        return

    email = input("Email del socio: ").strip().lower()

    if email == "0": return

    if not email:
        print("❌ El email no puede estar vacío ❌")
        return
    
    # Verificar si ya existe un socio con ese email
    for socio in socios:
        if socio['email'] == email:
            print(f"❌ Ya existe un socio con el email {email} ❌")
            return

    # Crear el nuevo socio
    nuevo_socio = {
        'id': f"{axuContador}",
        'nombre': nombre,
        'apellido': apellido,
        'email': email,
        'libros_prestados': []
    }

    socios.append(nuevo_socio)
    axuContador += 1
    
    print("✅ Socio Registrado Exitosamente 👤")
    print(f"👤 {nombre} {apellido}")
    print(f"📧 Email: {email}")
    print(f"🆔 ID: {nuevo_socio['id']}")

    print("================================================================")

def prestar_libro():
    '''Prestra un libro a un socio'''
    global libros, socios

    print("📖 Prestamo de Libros 📖")

    # Pedir ISBN del libro
    isbn = input("ISBN del libro a presta: ").strip()

    if not isbn:
        print(" El ISBN no puede estar vacio")
        return
    
    #Buscar el libro
    libro_encontrado = None
    for libro in libros:
        if libro['isbn'] == isbn:
            libro_encontrado = libro
            break

    if not libro_encontrado:
        print(f"No se encontro un libro con el ISBN {isbn}")
        return
    
     # Pedir ID del socio
    id_socio = input("ID del socio: ").strip()

    print(id_socio)

    if not id_socio:
        print(" El id no puede estar vacio")
        return
    
    #Buscar el libro
    id_socio_encontrado = None
    for socio in socios:
        if socio['id'] == id_socio:
            id_socio_encontrado = socio
            break

    if not id_socio_encontrado:
        print(f"No se encontro un usuario con el id {id_socio}")
        return
    
    #Verificar que el libro este disponible
    disponible_libro = None
    for libro in libros:
        if libro['estado'] == 'Disponible':
            disponible_libro = True
            break

    if not disponible_libro:
        print("Actualemente el libro solicitado no esta disponible")
        return
    
    libro_encontrado['estado'] = 'Prestado'
    libro_encontrado['socio_prestado'] = id_socio

    print("Libro prestad con exito")
    print({libro_encontrado['titulo']})
    print(f"Pestado a: {id_socio_encontrado['nombre']}")



def devolver_libro():
    global libros

    # Pedir ISBN del libro
    isbn = input("ISBN del libro a presta: ").strip()

    if not isbn:
        print(" El ISBN no puede estar vacio")
        return
    
    #Buscar el libro
    libro_encontrado = None
    for libro in libros:
        if libro['isbn'] == isbn:
            libro_encontrado = libro
            break

    if not libro_encontrado:
        print(f"No se encontro un libro con el ISBN {isbn}")
        return
    
    libro_encontrado['estado'] = 'Disponible'
    libro_encontrado['socio_prestado'] = None

    print("Libro devuleto exitosamente")



def ver_libro_prestado():


    #TAREA: OPCION QUE MUESTRE QUE NO HAY LIBROS PRESTADOS
    table = PrettyTable()

    table.field_names = ["titulo", "autor", "isbn", "id_socio"]

    table.title = "📖 Mostrando Libros Prestados 📖"

    for i, libro in enumerate(libros, 1):
        if libro['estado'] == 'Prestado':
            table.add_row([libro["titulo"], libro["autor"], libro["isbn"], libro["socio_prestado"]])

    print(table)

def ver_todos_libros():

    table = PrettyTable()

    table.field_names = ["titulo", "autor", "isbn", "estado"]

    table.title = "📖 Mostrando Libros 📖"

    for i, libro in enumerate(libros, 1):
        table.add_row([libro["titulo"], libro["autor"], libro["isbn"], libro["estado"]])

    print(table)


    """
    print("================================================================")
    print("Mostrando todo los libros")
    print("================================================================")

    if not libros:
        print("No hay libros registrados en la biblioteca")
        return
    
    for i, libro in enumerate(libros, 1):
        print("================================================================")
        print(f"{i}. Nombre del Libro: {libro["titulo"]}")
        print(f"     Autor: {libro["autor"]}")
        print(f"     ISBN: {libro["isbn"]}")
        print(f"     Estado: {libro["estado"]}")
        print("================================================================")
    """

    

def ver_todo_socios():
    table = PrettyTable()

    table.field_names = ["ID", "Nombre", "Apellido", "Email", "Libros Prestados"]

    table.title = "👤 Mostrando Socios 👤"

    if not socios:
        print("================================================================")
        print("No hay socios registrados en la biblioteca")
        print("================================================================")
        return

    for socio in socios:
        libros_prestados = len(socio["libros_prestados"])
        table.add_row([socio["id"], socio["nombre"], socio["apellido"], socio["email"], libros_prestados])

    print(table)

    """
    print("================================================================")
    print("Mostrando todos los socios")
    print("================================================================")

    if not socios:
        print("No hay socios registrados en la biblioteca")
        return
    
    for i, socio in enumerate(socios, 1):
        print("================================================================")
        print(f"{i}. ID: {socio["id"]}")
        print(f"     Nombre: {socio["nombre"]} {socio["apellido"]}")
        print(f"     Email: {socio["email"]}")
        print(f"     Libros Prestados: {len(socio["libros_prestados"])}")
        print("================================================================")
    """

def main():
    '''Funcion principal del programa'''
    while True:
        mostar_menu()

        opcion = input("Seleccion una opción(0-7): ").strip()
        
        match opcion:
            case '1':
                registar_libro()
            case '2':
                registar_socio()
            case '3':
                prestar_libro()
            case '4':
                devolver_libro()
            case '5':
                ver_libro_prestado()
            case '6':
                ver_todos_libros()
            case '7':
                ver_todo_socios()
            case '0':
                print("📚 Gracias por usar MiniBiblio! 📚")
                print("📚 Hasta Luego 📚")
                break
            case _:
                print("Opcion no válida. Por favor, selecion una opción dek 0 al 7")

main()
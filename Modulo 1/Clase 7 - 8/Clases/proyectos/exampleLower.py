libros = [
    {
        'isbn': "1",
        'titulo': "El principito",
        'autor': "Antoine",
        'estado': 'Disponible',
        'socio_prestado': None
    },
    {
        'isbn': "2",
        'titulo': "El principito 2",
        'autor': "Antoine",
        'estado': 'Disponible',
        'socio_prestado': None
    },
    {
        'isbn': "3",
        'titulo': "El principito 3",
        'autor': "Antoine",
        'estado': 'Disponible',
        'socio_prestado': None
    }

]

isbn = "3"


for l in libros:
    if l['isbn'] == isbn:
        print(f"❌ Ya existe un libro con el ISBN ❌")
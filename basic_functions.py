def create_json_libros():
    titulo = input("Titulo: ")
    editorial = input("Editorial: ")
    autor = input("Autor: ")
    genero = input("Genero: ")
    paisautor = input("Pais del autor: ")
    npaginas = input("Numero de paginas: ")
    aedicion = input("Año de edicion: ")
    precio = input("Precio: ")

    libros = {
        "titulo": titulo,
        "editorial":editorial,
        "autor":autor,
        "genero":genero,
        "paisautor":paisautor,
        "npaginas":npaginas,
        "aedicion":aedicion,
        "precio":precio
    }
    return libros

def create_json_update():
    print("Menu de opciones")
    print("1. Modificar todos los datos del documento")
    print("2. Modificar un elemento del documento")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        titulo = input("Titulo: ")
        editorial = input("Editorial: ")
        autor = input("Autor: ")
        genero = input("Genero: ")
        paisautor = input("Pais del autor: ")
        npaginas = input("Numero de paginas: ")
        aedicion = input("Año de edicion: ")
        precio = input("Precio: ")

        libros = {
            "titulo": titulo,
            "editorial": editorial,
            "autor": autor,
            "genero": genero,
            "paisautor": paisautor,
            "npaginas": npaginas,
            "aedicion": aedicion,
            "precio": precio
        }
        return libros
    elif opcion == "2":
        indice = input("Ingrese el indice")
        valor = input("Ingrese el valor a modificar")
        libros = {indice: valor}
        return libros
    else:
        print("Dato ingresado no valido")
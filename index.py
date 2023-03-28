from crud import *
from basic_functions import *
while True:
    print("Menu de opciones")
    print("1. Ver todos los registros")
    print("2. Buscar un registro")
    print("3. Agregar un registro")
    print("4. Modificar un registro")
    print("5. Salir del sistema")
    opcion = input("Ingrese un opcion: ")
    if opcion == "1":
        read_libros()
    elif opcion == "2":
        id = int(input("Ingres el ID a buscar: "))
        read_libros(id)
    elif opcion == "3":
        libros = create_json_libros()
        create_libros(libros)
    elif opcion == "4":
        id = int(input("Ingres el ID a modificar: "))
        libros = create_json_update()
        update_libros(id, libros)
    elif opcion == "5":
        exit()
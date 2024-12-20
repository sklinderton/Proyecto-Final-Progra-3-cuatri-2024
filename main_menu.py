from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario

def menu():
    biblioteca = Biblioteca()
    biblioteca.cargar_datos()

    while True:
        print("\n--- Menu ---")
        print("1. Registrar libro")
        print("2. Registrar usuario")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Ver libros disponibles")
        print("6. Ver usuarios registrados")
        print("7. Salir")
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            anio_publicacion = int(input("Annio de publicacion: "))
            numero_de_volumen = int(input("Numero de volumen: "))
            libro = Libro(titulo, autor, anio_publicacion, True, numero_de_volumen)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            nombre = input("Nombre del usuario: ")
            id_usuario = int(input("ID del usuario: "))
            usuario = Usuario(id_usuario, nombre)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "3":
            titulo = input("Titulo del libro a prestar: ")
            id_usuario = int(input("ID del usuario que solicita el prestamo: "))
            biblioteca.prestar_libro(titulo, id_usuario)

        elif opcion == "4":
            titulo = input("Titulo del libro a devolver: ")
            id_usuario = int(input("ID del usuario que devuelve el libro: "))
            biblioteca.devolver_libro(titulo, id_usuario)

        elif opcion == "5":
            biblioteca.mostrar_libros_disponibles()

        elif opcion == "6":
            biblioteca.mostrar_usuarios()

        elif opcion == "7":
            biblioteca.guardar_datos()
            print("Datos guardados. ¡Hasta luego!")
            break

        else:
            print("Opcion no valida. Intenta nuevamente.")

if __name__ == "__main__":
    menu()

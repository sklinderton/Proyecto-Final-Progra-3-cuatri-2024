from libro import Libro
from usuario import Usuario

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def prestar_libro(self, titulo, id_usuario):
        usuario = next((u for u in self.usuarios if u._Usuario__id_usuario == id_usuario), None)
        libro = next((l for l in self.libros if l._Libro__titulo == titulo and l._Libro__disponible), None)

        if usuario and libro:
            libro._Libro__disponible = False
            usuario.agregar_libro_prestado(libro)
            print(f"El libro '{titulo}' ha sido prestado a {usuario._Usuario__nombre}.")
        elif not usuario:
            print(f"El usuario con ID {id_usuario}NO fue encontrado.")
        elif not libro:
            print(f"El libro '{titulo}' no se encuentra disponible en estos momentos.")

    def devolver_libro(self, titulo, id_usuario):
        usuario = next((u for u in self.usuarios if u._Usuario__id_usuario == id_usuario), None)
        libro = next((l for l in usuario._Usuario__libros_prestados if l._Libro__titulo == titulo), None) if usuario else None

        if usuario and libro:
            libro._Libro__disponible = True
            usuario._Usuario__libros_prestados.remove(libro)
            print(f"El libro '{titulo}' ha sido devuelto por {usuario._Usuario__nombre}.")
        elif not usuario:
            print(f"El usuario con ID {id_usuario}NO fue encontrado.")
        elif not libro:
            print(f"El libro '{titulo}' no se encuentra en los libros prestados de {usuario._Usuario__nombre}.")

    def mostrar_libros_disponibles(self):
        print("Libros disponibles:")
        for libro in self.libros:
            if libro._Libro__disponible:
                print(libro)

    def mostrar_usuarios(self):
        print("Usuarios registrados:")
        for usuario in self.usuarios:
            print(usuario)

    def cargar_datos(self):
        self.libros = Libro.cargar_libros()
        self.usuarios = Usuario.cargar_usuarios(self.libros)

    def guardar_datos(self):
        Libro.guardar_libros(self.libros)
        Usuario.guardar_usuarios(self.usuarios)

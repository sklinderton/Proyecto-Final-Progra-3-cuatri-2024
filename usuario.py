class Usuario:
    def __init__(self, id_usuario, nombre):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__libros_prestados = []

    def __str__(self):
        return f"ID: {self.__id_usuario}, Nombre: {self.__nombre}, Libros Prestados: {self.__libros_prestados}"

    def agregar_libro_prestado(self, libro):
        self.__libros_prestados.append(libro)

    @classmethod
    def cargar_usuarios(cls, libros):
        usuarios = []
        try:
            with open('usuarios.txt', 'r') as f:
                for line in f:
                    datos = line.strip().split(',')
                    if len(datos) == 3:
                        id_usuario, nombre, libros_prestados = datos
                        usuario = Usuario(int(id_usuario), nombre)
                        if libros_prestados:
                            libros_ids = libros_prestados.split(',')
                            for libro_id in libros_ids:
                                libro = next((l for l in libros if l._Libro__consecutivo == int(libro_id)), None)
                                if libro:
                                    usuario.agregar_libro_prestado(libro)
                        usuarios.append(usuario)
        except FileNotFoundError:
            print(f"El archivo 'usuarios.txt' no se encuentra.")
        return usuarios

    @staticmethod
    def guardar_usuarios(usuarios):
        try:
            with open('usuarios.txt', 'w') as f:
                for usuario in usuarios:
                    libros_prestados = ','.join([str(libro._Libro__consecutivo) for libro in usuario._Usuario__libros_prestados])
                    f.write(f"{usuario._Usuario__id_usuario},{usuario._Usuario__nombre},{libros_prestados}\n")
        except Exception as e:
            print(f"Error al guardar los usuarios: {e}")

class Libro:
    consecutivo = 1

    def __init__(self, titulo, autor, anio_publicacion, disponible, numero_de_volumen):
        self.__consecutivo = Libro.consecutivo
        self.__titulo = titulo
        self.__autor = autor
        self.__anio_publicacion = anio_publicacion
        self.__disponible = disponible
        self.__numero_de_volumen = numero_de_volumen
        Libro.consecutivo += 1  

    def __str__(self):
        return f"Consecutivo: {self.__consecutivo}, Titulo: {self.__titulo}, Autor: {self.__autor}, Annio: {self.__anio_publicacion}, Disponible: {self.__disponible}, Volumen: {self.__numero_de_volumen}"

    @classmethod
    def cargar_libros(cls):
        libros = []
        try:
            with open('libros.txt', 'r') as f:
                for line in f:
                    datos = line.strip().split(',')
                    if len(datos) == 6:
                        consecutivo, titulo, autor, anio_publicacion, disponible, numero_de_volumen = datos
                        disponible = True if disponible == 'True' else False
                        libro = Libro(titulo, autor, int(anio_publicacion), disponible, int(numero_de_volumen))
                        libros.append(libro)
        except FileNotFoundError:
            print(f"El archivo 'libros.txt' no se encuentra.")
        return libros

    @staticmethod
    def guardar_libros(libros):
        try:
            with open('libros.txt', 'w') as f:
                for libro in libros:
                    f.write(f"{libro.__consecutivo},{libro.__titulo},{libro.__autor},{libro.__anio_publicacion},{libro.__disponible},{libro.__numero_de_volumen}\n")
        except Exception as e:
            print(f"Error al guardar los libros: {e}")

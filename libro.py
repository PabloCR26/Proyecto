import uuid


class Libro:

    def __init__(self, titulo, autor, year, genero, descripcion):
        self.id = uuid.uuid4()
        self.titulo = titulo
        self.autor = autor
        self.year = year
        self.genero = genero
        self.descripcion = descripcion
        self.disponible = True
        self.reservado = False
        self.inicio_prestamo = ""
        self.fin_prestamo = ""

    def __str__(self):
        return f'{self.id},{self.titulo}, {self.autor}, {self.year}, {self.genero}, {self.descripcion}'

    def prestar(self, fecha_inicio, fecha_fin):
        self.disponible = False
        self.inicio_prestamo = fecha_inicio
        self.fin_prestamo = fecha_fin          

    def reservar(self, fecha_inicio, fecha_fin):
        self.reservado = True
        self.inicio_prestamo = fecha_inicio
        self.fin_prestamo = fecha_fin

    def devolver(self):
        self.disponible = True
        self.inicio_prestamo = ""
        self.fin_prestamo = ""
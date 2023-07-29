import uuid



class Libro:

    def __init__(self,titulo,autor,year,genero,descripcion):
        self.id= uuid.uuid4()
        self.titulo=titulo
        self.autor=autor
        self.year=year
        self.genero=genero
        self.descripcion=descripcion





    '''Pseudocodigo'''
    #1. Solicitar título del libro al usuario.
    #2. Buscar el título en la lista de libros.
    #3. Imprimir el libro si se encuentra.



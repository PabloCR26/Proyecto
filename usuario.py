from persona import Persona

class Usuario(Persona):
    def __init__(self,cedula,nombre,apellido1,apellido2,direccion,telefono):
        super().__init__(cedula,nombre,apellido1,apellido2)
        self.direccion=direccion
        self.telefono=telefono

    def __str__(self):
        return f'{self.cedula},{self.nombre}, {self.apellido1}, {self.apellido2}, {self.telefono}, {self.direccion}'
from persona import Persona


class Empleado(Persona):
    def __init__(self,cedula,nombre,apellido1,apellido2,codigo_empleado,puesto):
        super().__init__(cedula,nombre,apellido1,apellido2)
        self.codigo_empleado=codigo_empleado
        self.puesto=puesto



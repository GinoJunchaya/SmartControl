from abc import ABCMeta

class Persona(metaclass=ABCMeta):
    def __init__(self):
        self.nombre = ''
        self.apellido = ''
        self.documento = ''
        self.fecha_nacimiento = ''
        self.contacto = ''

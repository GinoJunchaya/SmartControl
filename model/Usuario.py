from model.Persona import Persona
class Usuario(Persona):
    def __init__(self, idUsuario, datosPersonales, username=None, password=None, idRol=3):
        self.idUsuario = idUsuario
        self.datosPersonales = datosPersonales
        self.username = username
        self.password = password
        self.idRol = idRol
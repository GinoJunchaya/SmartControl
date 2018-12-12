import Persona
class Cliente(Persona):
    def __init__(self, idCliente, datosPersonales):
        self.idCliente = idCliente
        self.datosPersonales = datosPersonales
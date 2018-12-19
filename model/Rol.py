class Rol:
    def __init__(self, idRol=None, descripcion=None, codRol=3):
        self.idRol = idRol
        self.descripcion = descripcion
        self.codRol = codRol
    
    def __str__(self):
        return "id: " + str(self.idRol) + " descripcion: " + self.descripcion + " codigoRol: " + str(self.codRol)
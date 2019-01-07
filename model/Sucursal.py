class Sucursal:
    def __init__(self, idSucursal=None, nombreSucursal=None, contacto=None, image=None, extension=None):
        self.idSucursal = idSucursal
        self.nombreSucursal = nombreSucursal
        self.contacto = contacto
        self.image = image
        self.extension = extension
    
    def __str__(self):
        return str(self.idSucursal) + " " + self.nombreSucursal + " " + self.contacto 
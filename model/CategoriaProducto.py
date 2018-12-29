class CategoriaProducto:
    def __init__(self, idCategoria=None, descripcion=None):
        self.idCategoria = idCategoria
        self.descripcion = descripcion
    
    def __str__(self):
        return "id: " + str(self.idCategoria) + " descripcion: " + self.descripcion
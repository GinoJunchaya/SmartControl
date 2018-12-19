class Producto:

    def __init__(self, idProducto=None, descripcion='', idCategoria=None, precio=0, stockMinimo=0, stockActual=0, idSucursal=None):
        self.idProducto = idProducto
        self.descripcion = descripcion
        self.idCategoria = idCategoria
        self.precio = precio
        self.stockMinimo = stockMinimo
        self.stockActual = stockActual
        self.idSucursal = idSucursal

    def __str__(self):
        return "idProducto: " + str(self.idProducto) + " descripcion: " + self.descripcion +\
                " idCategoria: " + str(self.idCategoria) + " precio: " + str(self.precio) +\
                " stockMinimo: " + str(self.stockMinimo) + " stockActual: " + str(self.stockActual) +\
                " idSucursal: " + str(self.idSucursal)
class Producto:
    def __init__(self, idProducto=None, descripcion='', stock_minimo=0, stock_actual=0, idCategoria=None, precio=0):
        self.idProducto = idProducto
        self.descripcion = descripcion
        self.stock_minimo = stock_minimo
        self.stock_actual = stock_actual
        self.idCategoria = idCategoria
        self.precio = precio

class Factura:
    def __init__(self, idFactura='', total=0, iva=0, idCliente=None, idUsuarioCarga=None, items=None):
        self.idFactura = idFactura
        self.total = total
        self.iva = iva
        self.idCliente = idCliente
        self.idUsuarioCarga = idUsuarioCarga
        self.items = items
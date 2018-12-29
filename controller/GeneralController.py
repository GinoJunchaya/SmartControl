from view.View import View
from model.Sucursal import Sucursal
from dataManager.Manager import Manager

class GeneralController:
    def __init__(self, exit):
        self.sucursal = Sucursal()
        self.exit = exit
        self.manager = Manager()
        self.manager.iniciar()
    
    def iniciarVista(self):
        vista = View(self)
        vista.iniciarVista()
    
    def listarProductos(self):
        return self.manager.listarProductos()
    
    def listarCategoriasProducto(self):
        return self.manager.listarCategoriasProducto()
    
    def crearProducto(self, producto):
        return self.manager.crearProducto(producto)

    def buscarCategoriaPorId(self, idCategoria):
        return self.manager.buscarCategoriaPorId(idCategoria)
    
    def buscarSucursalPorId(self, idSucursal):
        return self.manager.buscarSucursalPorId(idSucursal)
    
    
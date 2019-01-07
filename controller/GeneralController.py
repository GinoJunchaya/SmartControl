from view.View import View
from model.Sucursal import Sucursal
from dataManager.Manager import Manager
import shutil
import os

class GeneralController:
    def __init__(self, exit):
        self.sucursal = Sucursal()
        self.exit = exit
        self.manager = Manager()
        self.manager.iniciar()
        shutil.rmtree("./resources")
        pathResources = r"./resources"
        if not os.path.exists(pathResources): os.makedirs(pathResources)        
    
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
    
    def iniciarSesion(self, username, password):
        usuario = self.manager.iniciarSesion(username, password)
        if usuario is None:
            return False
        self.usuarioSesion = usuario
        return True
    
    def buscarSucursalesDeUsuario(self):
        if self.usuarioSesion is not None:
            return self.manager.buscarSucursalesDeUsuario(self.usuarioSesion.idUsuario)
        return None
    
    def seleccionarSucursal(self, sucursal):
        self.sucursal = sucursal


        
        

    
    
from view.Login import Login
from view.SucursalSelect import SucursalSelect
from view.Home import Home
from PyQt5.QtWidgets import QApplication

class View:
    def __init__(self, generalController):
        self.generalController = generalController
    
    def iniciarVista(self):
        self.app = QApplication([])
        self.loginView = Login(self)
        self.loginView.iniciar()
    
    def mostrarSeleccionSucursal(self):
        self.sucursalSelectView = SucursalSelect(self)
        self.sucursalSelectView.iniciar()

    def mostrarInicio(self):
        self.homeView = Home(self)
        self.homeView.iniciar()
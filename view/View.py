from view import Login
from view import SucursalSelect
from view import Home
from PyQt5.QtWidgets import QApplication

class View:
    def __init__(self, generalController):
        self.generalController = generalController
    
    def iniciarVista(self):
        self.app = QApplication([])
        self.loginView = Login.Login(self)
        self.loginView.iniciar()
    
    def mostrarSeleccionSucursal(self):
        self.sucursalSelectView = SucursalSelect.SucursalSelect(self)
        self.sucursalSelectView.iniciar()

    def mostrarInicio(self):
        self.homeView = Home.Home(self)
        self.homeView.iniciar()
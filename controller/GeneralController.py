from view.View import View
from model.Sucursal import Sucursal

class GeneralController:
    def __init__(self, exit):
        self.sucursal = Sucursal()
        self.exit = exit
    
    def iniciarVista(self):
        vista = View(self)
        vista.iniciarVista()
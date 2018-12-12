from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class SucursalSelect:
    def __init__(self, view):
        self.view = view
        self.title = 'Sucursales | SmartControl'

    def construir(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
        self.createGridLayout()
    
    def iniciar(self):
        self.construir()
        self.window.show()

    def createGridLayout(self):
        self.layout = QGridLayout()
        self.layout.setColumnStretch(0,1)
        self.layout.setColumnStretch(1,1)
        sucursal1 = QPushButton("Sucursal 1")
        sucursal2 = QPushButton("Sucursal 2")
        sucursal3 = QPushButton("Sucursal 3")
        sucursal4 = QPushButton("Sucursal 4")
        self.layout.addWidget(sucursal1,0,0)
        self.layout.addWidget(sucursal2,0,1)         
        self.layout.addWidget(sucursal3,1,0)
        self.layout.addWidget(sucursal4,1,1) 
        self.window.setLayout(self.layout)
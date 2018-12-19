from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from util.styles import primaryButton, controlLabel, pageHeader

class RegistrarAsistencia:

    def __init__(self, view):
        self.view = view

    def constriur(self):
        self.widget = QWidget()
        self.layoutRegistrarAsistencia = QGridLayout()
        self.layoutRegistrarAsistencia.setColumnStretch(0,9)
        self.layoutRegistrarAsistencia.setColumnStretch(1,9)        
        self.layoutRegistrarAsistencia.setColumnStretch(2,9)
        self.layoutRegistrarAsistencia.setColumnStretch(3,9)

        bigTitleLabel = QLabel("Registrar existencia")
        bigTitleLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)        
        bigTitleLabel.setStyleSheet(pageHeader)

        precioLabel = QLabel("Precio : ")
        precioLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        precioLabel.setStyleSheet(controlLabel) 

        vtoLabel = QLabel("Vencimiento : ")
        vtoLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        vtoLabel.setStyleSheet(controlLabel) 

        cantidadLabel = QLabel("Cantidad : ")
        cantidadLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        cantidadLabel.setStyleSheet(controlLabel) 

        productoLabel = QLabel("Producto : ")
        productoLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        productoLabel.setStyleSheet(controlLabel)         

        self.inputProducto = QComboBox()
        self.inputPrecio = QLineEdit()
        self.inputCantidad = QLineEdit()
        self.inputVencimiento = QLineEdit()
        self.registrarButton = QPushButton("Registrar")
        self.limpiarButton = QPushButton("Limpiar")

        self.layoutRegistrarAsistencia.addWidget(bigTitleLabel,0,0,1,10)        

        self.layoutRegistrarAsistencia.addWidget(productoLabel,1,0,1,1)
        self.layoutRegistrarAsistencia.addWidget(self.inputProducto,1,1,1,2)

        self.layoutRegistrarAsistencia.addWidget(precioLabel,1,3,1,1)
        self.layoutRegistrarAsistencia.addWidget(self.inputPrecio,1,4,1,2)

        self.layoutRegistrarAsistencia.addWidget(vtoLabel,2,0,1,1)
        self.layoutRegistrarAsistencia.addWidget(self.inputVencimiento,2,1,1,2)

        self.layoutRegistrarAsistencia.addWidget(cantidadLabel,2,3,1,1)
        self.layoutRegistrarAsistencia.addWidget(self.inputCantidad,2,4,1,2)

        self.layoutRegistrarAsistencia.addWidget(self.registrarButton,3,4,1,1)
        self.layoutRegistrarAsistencia.addWidget(self.limpiarButton,3,5,1,1)

        self.layoutRegistrarAsistencia.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.widget.setLayout(self.layoutRegistrarAsistencia)
    
    def getWidgetBuilded(self):
        self.constriur()
        return self.widget
        



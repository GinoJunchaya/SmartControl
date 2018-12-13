from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from util.styles import primaryButton, controlLabel, pageHeader

class CrearProducto:

    def __init__(self, view):
        self.view = view

    def constriur(self):
        self.widget = QWidget()

        self.layoutCrearProducto = QGridLayout()
        self.layoutCrearProducto.setColumnStretch(0,9)
        self.layoutCrearProducto.setColumnStretch(1,9)        
        self.layoutCrearProducto.setColumnStretch(2,9)
        self.layoutCrearProducto.setColumnStretch(3,9)
        self.layoutCrearProducto.setColumnStretch(4,9)

        bigTitleLabel = QLabel("Crear producto")
        bigTitleLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        bigTitleLabel.setStyleSheet(pageHeader)

        descripcionLabel = QLabel("Descripción : ")
        descripcionLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        descripcionLabel.setStyleSheet(controlLabel)

        categoriaLabel = QLabel("Categoría : ")
        categoriaLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        categoriaLabel.setStyleSheet(controlLabel)         

        precioLabel = QLabel("Precio : ")
        precioLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        precioLabel.setStyleSheet(controlLabel)           

        self.addPhotoButton = QPushButton("Agregar imagen")
        self.addPhotoButton.setStyleSheet("height: 100%")

        self.createButton = QPushButton("Crear")
        self.createButton.setStyleSheet(primaryButton)        

        self.cleanButton = QPushButton("Limpiar")
        self.cleanButton.setStyleSheet(primaryButton)

        self.inputDescripcion = QLineEdit()
        self.inputPrecio = QLineEdit()
        self.inputCategoria = QComboBox()

        self.layoutCrearProducto.addWidget(bigTitleLabel,0,0,1,10)

        self.layoutCrearProducto.addWidget(descripcionLabel,1,0,1,1)
        self.layoutCrearProducto.addWidget(categoriaLabel,2,0,1,1)
        self.layoutCrearProducto.addWidget(precioLabel,3,0,1,1)

        self.layoutCrearProducto.addWidget(self.inputDescripcion,1,1,1,6)
        self.layoutCrearProducto.addWidget(self.inputCategoria,2,1,1,6)
        self.layoutCrearProducto.addWidget(self.inputPrecio,3,1,1,6)

        self.layoutCrearProducto.addWidget(self.addPhotoButton,1,7,3,2)

        self.layoutCrearProducto.addWidget(self.createButton,4,7)
        self.layoutCrearProducto.addWidget(self.cleanButton,4,8)

        self.layoutCrearProducto.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.widget.setLayout(self.layoutCrearProducto)
    
    def getWidgetBuilded(self):
        self.constriur()
        return self.widget
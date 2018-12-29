from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from util.styles import primaryButton, controlLabel, pageHeader
from model.Producto import Producto

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
        self.layoutCrearProducto.setColumnStretch(5,9)

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

        stockMinimoLabel = QLabel("Stock minimo : ")
        stockMinimoLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        stockMinimoLabel.setStyleSheet(controlLabel)

        self.addPhotoButton = QPushButton("Agregar imagen")
        self.addPhotoButton.setStyleSheet("height: 100%")
        self.addPhotoButton.clicked.connect(self.seleccionarImagen)

        self.createButton = QPushButton("Crear")
        self.createButton.setStyleSheet(primaryButton)
        self.createButton.clicked.connect(self.handlerInsertarProducto)

        self.cleanButton = QPushButton("Limpiar")
        self.cleanButton.setStyleSheet(primaryButton)

        self.inputDescripcion = QLineEdit()
        self.inputPrecio = QLineEdit()
        self.inputCategoria = QComboBox()
        self.inputStockMinimo = QLineEdit()

        categoriasProducto = self.view.generalController.listarCategoriasProducto()
        for i in categoriasProducto:
            self.inputCategoria.addItem(i.descripcion, i)

        self.layoutCrearProducto.addWidget(bigTitleLabel,0,0,1,10)

        self.layoutCrearProducto.addWidget(descripcionLabel,1,0,1,1)
        self.layoutCrearProducto.addWidget(categoriaLabel,2,0,1,1)
        self.layoutCrearProducto.addWidget(precioLabel,3,0,1,1)
        self.layoutCrearProducto.addWidget(stockMinimoLabel,4,0,1,1)
        self.layoutCrearProducto.addWidget(self.inputDescripcion,1,1,1,6)
        self.layoutCrearProducto.addWidget(self.inputCategoria,2,1,1,6)
        self.layoutCrearProducto.addWidget(self.inputPrecio,3,1,1,6)
        self.layoutCrearProducto.addWidget(self.inputStockMinimo,4,1,1,6)
        self.layoutCrearProducto.addWidget(self.addPhotoButton,1,7,4,2)
        self.layoutCrearProducto.addWidget(self.createButton,5,7)
        self.layoutCrearProducto.addWidget(self.cleanButton,5,8)
        self.layoutCrearProducto.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.widget.setLayout(self.layoutCrearProducto)
    
    def getWidgetBuilded(self):
        self.constriur()
        return self.widget

    def handlerInsertarProducto(self):
        descripcion = self.inputDescripcion.text()
        precio = int(self.inputPrecio.text())
        categoria = self.inputCategoria.itemData(self.inputCategoria.currentIndex())
        print(categoria.idCategoria)
        stockMinimo = int(self.inputStockMinimo.text())
        producto = Producto(descripcion=descripcion, idCategoria=categoria.idCategoria, precio=precio,\
        stockMinimo=stockMinimo, stockActual=0, idSucursal=3)
        self.view.generalController.crearProducto(producto)

    def seleccionarImagen(self):
        imagenFile = QFileDialog.getOpenFileName()
        self.addPhotoButton.setIcon(QIcon(imagenFile[0]))
        self.addPhotoButton.setIconSize(QSize(100,150))
        self.addPhotoButton.setText("")
        self.addPhotoButton.setStyleSheet("border: 0px solid;")

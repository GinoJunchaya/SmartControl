from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from util.styles import primaryButton, controlLabel, pageHeader

class RegistrarExistencia:

    def __init__(self, view):
        self.view = view
        self.productos = self.view.generalController.listarProductos()

    def constriur(self):
        self.widget = QWidget()
        self.layoutRegistrarExistencia = QGridLayout()
        self.layoutRegistrarExistencia.setColumnStretch(0,9)
        self.layoutRegistrarExistencia.setColumnStretch(1,9)        
        self.layoutRegistrarExistencia.setColumnStretch(2,9)
        self.layoutRegistrarExistencia.setColumnStretch(3,9)

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
        self.inputProducto.currentIndexChanged[int].connect(self.changeProducto)
        self.inputProducto.addItem(" - Seleccione producto - ")
        for i in self.productos:
            self.inputProducto.addItem(i.descripcion, i)

        self.inputPrecio = QLabel("")
        self.inputCantidad = QLineEdit()
        self.inputVencimiento = QDateEdit(QDate.currentDate())
        self.inputVencimiento.setDisplayFormat("dd/MM/yyyy")
        self.registrarButton = QPushButton("Registrar")
        self.limpiarButton = QPushButton("Limpiar")

        self.layoutRegistrarExistencia.addWidget(bigTitleLabel,0,0,1,10)        

        self.layoutRegistrarExistencia.addWidget(productoLabel,1,0,1,1)
        self.layoutRegistrarExistencia.addWidget(self.inputProducto,1,1,1,2)

        self.layoutRegistrarExistencia.addWidget(precioLabel,1,3,1,1)
        self.layoutRegistrarExistencia.addWidget(self.inputPrecio,1,4,1,2)

        self.layoutRegistrarExistencia.addWidget(vtoLabel,2,0,1,1)
        self.layoutRegistrarExistencia.addWidget(self.inputVencimiento,2,1,1,2)

        self.layoutRegistrarExistencia.addWidget(cantidadLabel,2,3,1,1)
        self.layoutRegistrarExistencia.addWidget(self.inputCantidad,2,4,1,2)

        self.layoutRegistrarExistencia.addWidget(self.registrarButton,3,4,1,1)
        self.layoutRegistrarExistencia.addWidget(self.limpiarButton,3,5,1,1)

        self.layoutRegistrarExistencia.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.widget.setLayout(self.layoutRegistrarExistencia)
    
    def getWidgetBuilded(self):
        self.constriur()
        return self.widget

    def changeProducto(self, index):
        data = self.inputProducto.itemData(index)
        if data is not None or data != '':
            precio = "{:,}".format(data.precio).replace(',','.')
            self.inputPrecio.setText(precio)
            self.inputCantidad.setText(str(data.stockActual))



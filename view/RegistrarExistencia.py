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
        precioLabel.setObjectName("controlLabel")
        with open("./view/styles.css") as f:
            precioLabel.setStyleSheet(f.read())

        vtoLabel = QLabel("Vencimiento : ")
        vtoLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        vtoLabel.setObjectName("controlLabel")
        with open("./view/styles.css") as f:
            vtoLabel.setStyleSheet(f.read())

        cantidadLabel = QLabel("Cantidad : ")
        cantidadLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        cantidadLabel.setObjectName("controlLabel")
        with open("./view/styles.css") as f:
            cantidadLabel.setStyleSheet(f.read())

        productoLabel = QLabel("Producto : ")
        productoLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        productoLabel.setObjectName("controlLabel")
        with open("./view/styles.css") as f:
            productoLabel.setStyleSheet(f.read())

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
        self.registrarButton.setObjectName("botonPrimario")
        with open("./view/styles.css") as f:
            self.registrarButton.setStyleSheet(f.read())

        self.limpiarButton = QPushButton("Limpiar")
        self.limpiarButton.setObjectName("botonPrimario")
        with open("./view/styles.css") as f:
            self.limpiarButton.setStyleSheet(f.read())

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



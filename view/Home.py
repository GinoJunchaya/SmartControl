from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from view.RegistrarExistencia import RegistrarExistencia
from view.CrearProducto import CrearProducto
from view.Existencias import Existencias
from util.styles import primaryButton, controlLabel, pageHeader

class Home:
    def __init__(self, view):
        self.view = view
        self.title = 'Inicio | SmartControl'

    def construir(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
        self.window.setWindowIcon(QIcon("icon.ico"))
        self.layout = QGridLayout()
        self.createBarraBotones()
        self.createTitlePage()
        self.createTabSector()
    
    def iniciar(self):
        self.construir()
        self.window.setLayout(self.layout)
        self.window.show()

    def createBarraBotones(self):
        self.layout.setColumnStretch(0,11)
        self.layoutBarraBotones = QHBoxLayout()
        self.layoutBarraBotones.setAlignment(Qt.AlignLeft)

        stockButton = QPushButton("Stock")
        stockButton.setObjectName("botonModulo")
        with open("./view/styles.css") as f:
            stockButton.setStyleSheet(f.read())

        ventasButton = QPushButton("Ventas")
        ventasButton.setObjectName("botonModulo")
        with open("./view/styles.css") as f:
            ventasButton.setStyleSheet(f.read())

        reporteStockButton = QPushButton("Reporte stock")
        reporteStockButton.setObjectName("botonModulo")
        with open("./view/styles.css") as f:
            reporteStockButton.setStyleSheet(f.read())
        
        reporteVentasButton = QPushButton("Reporte ventas")
        reporteVentasButton.setObjectName("botonModulo")
        with open("./view/styles.css") as f:
            reporteVentasButton.setStyleSheet(f.read())

        ayudaButton = QPushButton("Ayuda")
        ayudaButton.setObjectName("botonModulo")
        with open("./view/styles.css") as f:
            ayudaButton.setStyleSheet(f.read())

        self.layoutBarraBotones.addWidget(stockButton)
        self.layoutBarraBotones.addWidget(ventasButton)        
        self.layoutBarraBotones.addWidget(reporteStockButton)
        self.layoutBarraBotones.addWidget(reporteVentasButton)
        self.layoutBarraBotones.addWidget(ayudaButton)
        self.layout.addLayout(self.layoutBarraBotones,0,0,1,12)
        self.window.setStyleSheet("width: 150px")

    def createTitlePage(self):
        self.layout.setColumnStretch(1,12)
        bigTitleLabel = QLabel("Control de Stock")
        bigTitleLabel.setObjectName("tituloPrincipal")
        with open("./view/styles.css") as f:
            bigTitleLabel.setStyleSheet(f.read())
        self.layout.addWidget(bigTitleLabel,1,0,1,12)

    def createTabSector(self):
        self.layout.setColumnStretch(2,12)
        self.tabsView = QTabWidget()
        registrarExistencia = RegistrarExistencia(self.view)
        crearProductoWidget = CrearProducto(self.view)
        existenciasWidget = Existencias(self.view)
        self.tabVerExistencias = existenciasWidget.getWidgetBuilded()
        self.tabRegExistencia = registrarExistencia.getWidgetBuilded()
        self.tabCrearProducto = crearProductoWidget.getWidgetBuilded()
        self.tabsView.addTab(self.tabVerExistencias, "Ver existencias")       
        self.tabsView.addTab(self.tabRegExistencia, "Registrar existencia")
        self.tabsView.addTab(self.tabCrearProducto, "Crear producto")
        self.layout.addWidget(self.tabsView,2,0,1,12)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from view import RegistrarAsistencia
from view import CrearProducto
from util.styles import primaryButton, controlLabel, pageHeader

class Home:
    def __init__(self, view):
        self.view = view
        self.title = 'Inicio | SmartControl'

    def construir(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
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
        ventasButton = QPushButton("Ventas")
        reporteStockButton = QPushButton("Reporte stock")
        reporteVentasButton = QPushButton("Reporte ventas")
        ayudaButton = QPushButton("Ayuda")
        self.layoutBarraBotones.addWidget(stockButton)
        self.layoutBarraBotones.addWidget(ventasButton)        
        self.layoutBarraBotones.addWidget(reporteStockButton)
        self.layoutBarraBotones.addWidget(reporteVentasButton)
        self.layoutBarraBotones.addWidget(ayudaButton)
        self.layout.addLayout(self.layoutBarraBotones,0,0,1,12)

    def createTitlePage(self):
        self.layout.setColumnStretch(1,12)
        bigTitleLabel = QLabel("Control de Stock")
        bigTitleLabel.setStyleSheet(pageHeader)
        self.layout.addWidget(bigTitleLabel,1,0,1,12)

    def createTabSector(self):
        self.layout.setColumnStretch(2,12)
        self.tabsView = QTabWidget()
        registrarAsistenciaWidget = RegistrarAsistencia.RegistrarAsistencia(self.view)
        crearProductoWidget = CrearProducto.CrearProducto(self.view)
        self.tabRegExistencia = registrarAsistenciaWidget.getWidgetBuilded()
        self.tabCrearProducto = crearProductoWidget.getWidgetBuilded()
        self.tabVerExistencias = QWidget()
        self.tabsView.addTab(self.tabRegExistencia, "Registrar existencia")
        self.tabsView.addTab(self.tabCrearProducto, "Crear producto")
        self.tabsView.addTab(self.tabVerExistencias, "Ver existencias")
        self.layout.addWidget(self.tabsView,2,0,1,12)



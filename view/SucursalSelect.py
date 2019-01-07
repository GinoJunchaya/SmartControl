from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from view.Popup import Popup
from PIL import Image
import time

class SucursalSelect:
    def __init__(self, view):
        self.view = view
        self.title = 'Sucursales | SmartControl'

    def construir(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
        self.window.setWindowIcon(QIcon("icon.ico"))
        self.createGridLayout()
    
    def iniciar(self):
        self.sucursales = self.view.generalController.buscarSucursalesDeUsuario()
        if self.sucursales is None:
            popup = Popup()
            popup.showCriticalBasic("Error en sucursales")
            return
        self.construir()
        self.window.show()

    def createGridLayout(self):
        self.layout = QVBoxLayout()
        groupBoxList = []
        for sucursal in self.sucursales:
            groupBox = QGroupBox("")
            layoutBox = QVBoxLayout()
            sucursalNombreLabel = QLabel(sucursal.nombreSucursal)
            sucursalNombreLabel.setObjectName("tituloGroupSucursal")
            with open("./view/styles.css") as f:
                sucursalNombreLabel.setStyleSheet(f.read())  
            contactoLabel = QLabel(sucursal.contacto)
            contactoLabel.setObjectName("subtituloGroupSucursal")
            with open("./view/styles.css") as f:
                contactoLabel.setStyleSheet(f.read())
            self.btnSeleccionar = QPushButton("Seleccionar")
            self.btnSeleccionar.setObjectName("botonPrimario")
            self.btnSeleccionar.my_own_data = sucursal
            with open("./view/styles.css") as f:
                self.btnSeleccionar.setStyleSheet(f.read())
            ts = str(time.time()).replace(".", "")
            fileName = "./resources/" + ts + "." + sucursal.extension
            open(fileName, "wb").write(sucursal.image)
            self.changeBrightness(fileName)
            groupStyle = "border: 1px solid silver; border-radius: 5px; background-image: url(" + fileName + ");"
            groupBox.setStyleSheet(groupStyle)
            self.btnSeleccionar.clicked.connect(self.seleccionarSucursal)
            layoutBox.addWidget(sucursalNombreLabel)
            layoutBox.addWidget(contactoLabel)
            layoutBox.addWidget(self.btnSeleccionar)
            groupBox.setLayout(layoutBox)
            groupBoxList.append(groupBox)
        for gb in groupBoxList:
            self.layout.addWidget(gb)
        self.window.setLayout(self.layout)
        self.window.setStyleSheet("width: 500px")

    def seleccionarSucursal(self):
        target = self.btnSeleccionar.sender()
        self.view.generalController.seleccionarSucursal(target.my_own_data)
        self.window.hide()
        self.view.mostrarInicio()        
    
    def changeBrightness(self, fileName):
        original_image = Image.open(fileName, 'r')
        pixels = original_image.getdata()
        new_image = Image.new('RGB', original_image.size)
        new_image_list = []
        brightness_multiplier = 0.4
        for pixel in pixels:
            new_pixel = (int(pixel[0] * brightness_multiplier), int(pixel[1] * brightness_multiplier), int(pixel[2] * brightness_multiplier))
            for pixel in new_pixel:
                if pixel > 255:
                    pixel = 255
                elif pixel < 0:
                    pixel = 0
            new_image_list.append(new_pixel)
        new_image.putdata(new_image_list)
        new_image.save(fileName)

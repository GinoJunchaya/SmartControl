from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from util.styles import primaryButton, controlLabel, pageHeader

class RegistrarAsistencia:

    def __init__(self, view):
        self.view = view

    def constriur(self):
        self.widget = QWidget()
        self.layoutRegistrarAsistencia = QGridLayout()
        self.layoutRegistrarAsistencia.setColumnStretch(0,12)
        self.layoutRegistrarAsistencia.setColumnStretch(1,12)        

        bigTitleLabel = QLabel("Registrar existencia")
        bigTitleLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)        
        bigTitleLabel.setStyleSheet(pageHeader)
        self.layoutRegistrarAsistencia.addWidget(bigTitleLabel,0,0,1,12)

        self.inputProducto = QLineEdit()
        self.layoutRegistrarAsistencia.addWidget(self.inputProducto,1,0,1,3)

        self.buscarButton = QPushButton("Buscar")
        self.layoutRegistrarAsistencia.addWidget(self.buscarButton,1,4,1,7)

        self.widget.setLayout(self.layoutRegistrarAsistencia)
    
    def getWidgetBuilded(self):
        self.constriur()
        return self.widget
        



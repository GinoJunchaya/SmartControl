from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Login:
    def __init__(self, view):
        self.view = view
        self.title = 'Login | SmartControl'

    def construir(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
        self.createGridLayout()
    
    def iniciar(self):
        self.construir()
        self.window.show()
        self.view.app.exec_()

    def createGridLayout(self):
        self.layout = QGridLayout()
        self.layout.setColumnStretch(0,2)
        self.layout.setColumnStretch(1,2)
        self.layout.setColumnStretch(2,2)
        labelUsername = QLabel("Nombre de usuario: ")
        labelUsername.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        labelUsername.setStyleSheet("font-weight: bold")
        labelPassword = QLabel("Contraseña: ")
        labelPassword.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        labelPassword.setStyleSheet("font-weight: bold")
        self.inputUsername = QLineEdit()
        self.inputPassword = QLineEdit()
        okButton = QPushButton("Iniciar")
        okButton.clicked.connect(self.handleLogin)
        cancelButton = QPushButton("Salir")
        self.layout.addWidget(labelUsername,0,0) 
        self.layout.addWidget(self.inputUsername,0,1,1,2) 
        self.layout.addWidget(labelPassword,1,0) 
        self.layout.addWidget(self.inputPassword,1,1,1,2)
        self.layout.addWidget(okButton,2,1)
        self.layout.addWidget(cancelButton,2,2)
        self.window.setLayout(self.layout)

    def handleLogin(self):
        #username = self.inputUsername.getText()
        #password = self.inputPassword.getText()
        #llamada al controller
        self.window.hide()        
        self.view.mostrarSeleccionSucursal()
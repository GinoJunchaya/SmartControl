from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from view.Popup import Popup

class Login:
    def __init__(self, view):
        self.view = view
        self.title = 'Login | SmartControl'

    def construir(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
        self.window.setWindowIcon(QIcon("icon.ico"))
        self.createGridLayout()
    
    def iniciar(self):
        self.construir()
        self.window.show()
        self.view.app.exec_()

    def createGridLayout(self):
        self.layout = QGridLayout()
        self.layout.setColumnStretch(0,3)
        self.layout.setColumnStretch(1,3)
        self.layout.setColumnStretch(2,3)
        self.layout.setColumnStretch(3,3)        
        self.layout.setColumnStretch(4,3)        

        labelUsername = QLabel("Nombre de usuario")
        labelUsername.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        labelUsername.setStyleSheet("font-weight: bold")

        labelPassword = QLabel("Contraseña")
        labelPassword.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        labelPassword.setStyleSheet("font-weight: bold")

        self.inputUsername = QLineEdit()
        self.inputUsername.setObjectName("entradaTexto")
        with open("./view/styles.css") as f:
            self.inputUsername.setStyleSheet(f.read())

        self.inputPassword = QLineEdit()
        self.inputPassword.setEchoMode(QLineEdit.Password)        
        self.inputPassword.setObjectName("entradaTexto")
        with open("./view/styles.css") as f:
            self.inputPassword.setStyleSheet(f.read())
            
        okButton = QPushButton("Iniciar")
        okButton.setObjectName("botonPrimario")
        with open("./view/styles.css") as f:
            okButton.setStyleSheet(f.read())        
        okButton.clicked.connect(self.handleLogin)

        registroButton = QPushButton("Registrarse")
        registroButton.setObjectName("botonPrimario")
        with open("./view/styles.css") as f:
            registroButton.setStyleSheet(f.read())        

        self.layout.addWidget(labelUsername,0,0,1,3) 
        self.layout.addWidget(self.inputUsername,1,0,1,3)
        self.layout.addWidget(labelPassword,2,0,1,3)
        self.layout.addWidget(self.inputPassword,3,0,1,3)
        self.layout.addWidget(okButton,4,1)
        self.layout.addWidget(registroButton,4,2)
        self.window.setLayout(self.layout)
        self.window.setStyleSheet("width: 150px")

    def handleLogin(self):
        username = self.inputUsername.text()
        password = self.inputPassword.text()
        if self.view.generalController.iniciarSesion(username, password):
            self.window.hide()        
            self.view.mostrarSeleccionSucursal()
        else:
            popup = Popup()
            popup.showCriticalBasic("Credenciales inválidas")
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from util.styles import primaryButton, controlLabel, pageHeader
from model.CategoriaProducto import CategoriaProducto

class Existencias:

    def __init__(self, view):
        self.view = view
        self.productos = self.view.generalController.listarProductos()

    def constriur(self):
        self.widget = QWidget()
        self.layoutExistencias = QGridLayout()
        self.layoutExistencias.setColumnStretch(0,9)
        bigTitleLabel = QLabel("Existencias")
        self.tablaExistencias = QTableWidget()
        self.tablaExistencias.setRowCount(len(self.productos))
        self.tablaExistencias.setColumnCount(6)
        header = self.tablaExistencias.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tablaExistencias.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.tablaExistencias.setHorizontalHeaderItem(1, QTableWidgetItem("DESCRIPCION"))
        self.tablaExistencias.setHorizontalHeaderItem(2, QTableWidgetItem("CATEGORIA"))
        self.tablaExistencias.setHorizontalHeaderItem(3, QTableWidgetItem("STOCK MINIMO"))
        self.tablaExistencias.setHorizontalHeaderItem(4, QTableWidgetItem("STOCK ACTUAL"))
        self.tablaExistencias.setHorizontalHeaderItem(5, QTableWidgetItem("PRECIO"))
        self.tablaExistencias.horizontalHeader().setStyleSheet("QHeaderView::section {background: #337ab7; color: white; font-weight: bold; border: 1px solid silver; padding: 5px}")
        self.tablaExistencias.verticalHeader().setStyleSheet("QHeaderView::section {background: #337ab7; color: white; font-weight: bold; border: 1px solid silver; padding: 5px}")        
        self.tablaExistencias.setStyleSheet("border-top: 0px solid transparent; border-left: 0px solid transparent")
        count = 0
        for i in self.productos:
            if count > 0:
                header.setSectionResizeMode(count, QHeaderView.Stretch)
            categoria = self.view.generalController.buscarCategoriaPorId(i.idCategoria)
            self.tablaExistencias.setItem(count,0,QTableWidgetItem(str(i.idProducto)))
            self.tablaExistencias.setItem(count,1,QTableWidgetItem(i.descripcion))
            self.tablaExistencias.setItem(count,2,QTableWidgetItem(categoria.descripcion))
            self.tablaExistencias.setItem(count,3,QTableWidgetItem(str(i.stockMinimo)))
            self.tablaExistencias.setItem(count,4,QTableWidgetItem(str(i.stockActual)))
            self.tablaExistencias.setItem(count,5,QTableWidgetItem("{:,}".format(i.precio).replace(',','.') + " GS."))
            count = count + 1
        self.tablaExistencias.move(0,0)
        bigTitleLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        bigTitleLabel.setStyleSheet(pageHeader)
        self.layoutExistencias.addWidget(bigTitleLabel,0,0,1,10)        
        self.layoutExistencias.addWidget(self.tablaExistencias,1,0,1,10)
        self.layoutExistencias.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.widget.setLayout(self.layoutExistencias)
    
    def getWidgetBuilded(self):
        self.constriur()
        return self.widget
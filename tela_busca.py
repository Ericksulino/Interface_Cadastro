# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'busc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_busca(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640,480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ResNome = QtWidgets.QLabel(self.centralwidget)
        self.ResNome.setGeometry(QtCore.QRect(120, 170, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ResNome.setFont(font)
        self.ResNome.setObjectName("ResNome")
        self.OutNa = QtWidgets.QLineEdit(self.centralwidget)
        self.OutNa.setGeometry(QtCore.QRect(270, 270, 111, 20))
        self.OutNa.setObjectName("OutNa")
        self.BUSCA = QtWidgets.QLabel(self.centralwidget)
        self.BUSCA.setGeometry(QtCore.QRect(260, 90, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BUSCA.setFont(font)
        self.BUSCA.setObjectName("BUSCA")
        self.ResNasci = QtWidgets.QLabel(self.centralwidget)
        self.ResNasci.setGeometry(QtCore.QRect(120, 270, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ResNasci.setFont(font)
        self.ResNasci.setObjectName("ResNasci")
        self.ButBus = QtWidgets.QPushButton(self.centralwidget)
        self.ButBus.setGeometry(QtCore.QRect(280, 130, 71, 23))
        self.ButBus.setObjectName("ButBus")
        self.CPF_Bu = QtWidgets.QLabel(self.centralwidget)
        self.CPF_Bu.setGeometry(QtCore.QRect(120, 130, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.CPF_Bu.setFont(font)
        self.CPF_Bu.setObjectName("CPF_Bu")
        self.InputBus = QtWidgets.QLineEdit(self.centralwidget)
        self.InputBus.setGeometry(QtCore.QRect(170, 130, 91, 20))
        self.InputBus.setObjectName("InputBus")
        self.OutEn = QtWidgets.QLineEdit(self.centralwidget)
        self.OutEn.setGeometry(QtCore.QRect(190, 220, 311, 20))
        self.OutEn.setObjectName("OutEn")
        self.OutNm = QtWidgets.QLineEdit(self.centralwidget)
        self.OutNm.setGeometry(QtCore.QRect(190, 170, 311, 20))
        self.OutNm.setObjectName("OutNm")
        self.ResEndereco = QtWidgets.QLabel(self.centralwidget)
        self.ResEndereco.setGeometry(QtCore.QRect(120, 220, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ResEndereco.setFont(font)
        self.ResEndereco.setObjectName("ResEndereco")
        self.ButHome = QtWidgets.QPushButton(self.centralwidget)
        self.ButHome.setGeometry(QtCore.QRect(470, 40, 75, 23))
        self.ButHome.setObjectName("ButHome")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ResNome.setText(_translate("MainWindow", "Nome"))
        self.BUSCA.setText(_translate("MainWindow", "BUSCA"))
        self.ResNasci.setText(_translate("MainWindow", "Data de Nascimento"))
        self.ButBus.setText(_translate("MainWindow", "Buscar"))
        self.CPF_Bu.setText(_translate("MainWindow", "CPF"))
        self.ResEndereco.setText(_translate("MainWindow", "Endere??o"))
        self.ButHome.setText(_translate("MainWindow", "HOME"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_busca()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
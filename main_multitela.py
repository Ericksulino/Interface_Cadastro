import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QMainWindow,QApplication,QFileDialog
from PyQt5.QtCore import QCoreApplication


from pessoa import Pessoa
from cadastro import Cadastro
from tela_inicio import Tela_inicio
from tela_cadastro import Tela_cadastro
from tela_busca import Tela_busca

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640,480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.tela_inicio = Tela_inicio()
        self.tela_inicio.setupUi(self.stack0)

        self.tela_cadastro = Tela_cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_busca = Tela_busca()
        self.tela_busca.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)

class Main(QMainWindow,Ui_Main):
    def __init__(self,parent=None):
        super(Main,self).__init(parent)
        self.setupUi(self)

        self.cad = Cadastro()
        self.tela_inicio.BtBus.clicked.connect(self.abrirTelaCadas)
        self.tela_inicio.BtCad.clicked.connect(self.abrirTelaBusc)

        self.tela_cadastro.ButCad.clicked.connect(self.botaoCadast)
        self.tela_busca.ButBus.clicked.connect(self.botaoBusc)
        self.tela_busca.ButHome.clicked.connect(self.abrirTelaIni)

    def botaoCadast(self):
        nome = self.tela_cadastro.InputNm.text()
        cpf = self.tela_cadastro.InputCp.text()
        endereco = self.tela_cadastro.InputEn.text()
        nascimento = self.tela_cadastro.InputNa.text()
        if not(nome == '' or cpf == '' or endereco == '' or nascimento == ''):
            p = Pessoa(nome,endereco,cpf,nascimento)
            if(self.cad.cadastra(p)):
                QMessageBox.information(None,'POOII','Cadastro realizado com sucesso!')
                self.tela_cadastro.InputNm.setText('')
                self.tela_cadastro.InputCp.setText('')
                self.tela_cadastro.InputEn.setText('')
                self.tela_cadastro.InputNa.setText('')
            else:
                QMessageBox.information(None,'POOII','O CPF informado já se encontra cadastrado!')
        else:
            QMessageBox.information(None,'POOII','Todos os campos devem ser preeecidos!')
        self.abrirTelaIni()


    def botaoBusc(self):
        cpf = self.tela_busca.InputBus.text()
        pessoa = self.cad.busca(cpf)
        if(pessoa!=None):
            self.tela_busca.OutNm.setText(pessoa.nome)
            self.tela_busca.OutCp.setText(pessoa.cpf)
            self.tela_busca.OutEn.setText(pessoa.endereco)
            self.tela_busca.OutNa.setText(pessoa.data_nascimento)
        else:
            QMessageBox.information(None,'POOII','CPF não cadastrado!')

    def abrirTelaIni(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaCadas(self):
        self.QtStack.setCurrentIndex(1)
    
    def abrirTelaBusc(self):
        self.QtStack.setCurrentIndex(2)


        



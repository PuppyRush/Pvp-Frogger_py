# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

import sys

class EventedQPushButton(QtWidgets.QPushButton):

    def __init__(self, *args, **kwargs):
        QtWidgets.QPushButton.__init__(self,*args,**kwargs)
        

    def mousePressEvent(self, QMouseEvent):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("sd")
        msg.exec_()
        #QMessageBox.Close(self, "alert", "Click between buttons neccssarly", QMessageBox.Ok)
        return super().mousePressEvent(QMouseEvent)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 200)
        Dialog.setMaximumSize(QtCore.QSize(300, 200))
        
        self.okButton = EventedQPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(60, 160, 75, 23))
        self.okButton.setObjectName("okButton")
        
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(160, 160, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 231, 51))
        self.groupBox.setObjectName("groupBox")
        self.serverButton = QtWidgets.QRadioButton(self.groupBox)
        self.serverButton.setGeometry(QtCore.QRect(40, 20, 90, 16))
        self.serverButton.setChecked(False)
        self.serverButton.setAutoRepeat(True)
        self.serverButton.setObjectName("serverButton")
        self.clientButton = QtWidgets.QRadioButton(self.groupBox)
        self.clientButton.setGeometry(QtCore.QRect(130, 20, 90, 16))
        self.clientButton.setChecked(True)
        self.clientButton.setAutoRepeat(True)
        self.clientButton.setObjectName("clientButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 90, 56, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 56, 12))
        self.label_2.setObjectName("label_2")
        self.ipEdit = QtWidgets.QLineEdit(Dialog)
        self.ipEdit.setGeometry(QtCore.QRect(100, 90, 113, 20))
        self.ipEdit.setObjectName("ipEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 120, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

     

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.okButton.setText(_translate("Dialog", "OK"))
        self.cancelButton.setText(_translate("Dialog", "CANCEL"))
        self.groupBox.setTitle(_translate("Dialog", "Server / Client"))
        self.serverButton.setText(_translate("Dialog", "Server"))
        self.clientButton.setText(_translate("Dialog", "Client"))
        self.label.setText(_translate("Dialog", "아이피"))
        self.label_2.setText(_translate("Dialog", "닉네임"))
        self.ipEdit.setText(_translate("Dialog", "192.168.0.1"))
        self.ipEdit.setPlaceholderText(_translate("Dialog", "write ip of someone pc"))
        self.lineEdit_2.setText(_translate("Dialog", "Frogger"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "write your nickname"))

    def event_clickedOkButton(self):
        if(self.serverButton.isChecked == False and self.clientButton.isChecked == False):
            reply = QMessageBox.Close(self, "alert", "Click between buttons neccssarly", QMessageBox.Ok)
            return



def beginUI():
    
    
    
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec_()
    

   
            

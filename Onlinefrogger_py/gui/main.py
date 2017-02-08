# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from copy import deepcopy

import sys

class InfoStruct(object):

    def __init__(self):
        self.myIp =""
        self.memorizeIp =""
        self.isServer = True
        self.nickname =""
    

class EventedQPushButton(QtWidgets.QPushButton):

    def __init__(self, *args, **kwargs):
        QtWidgets.QPushButton.__init__(self,*args,**kwargs)
        
    def mousePressEvent(self, QMouseEvent):

        if(self.objectName()=="okButton"):

            if((ui.serverButton.isChecked()== False and ui.clientButton.isChecked()==False )or
                (ui.clientButton.isChecked()==True and ui.nicknameEdit.text().count==0 or ui.ipEdit.text().count==0) or
                (ui.serverButton.isChecked()==True and ui.nicknameEdit.text().count==0)):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("write your information necessarly")
                msg.exec_()
                
                return
            else:
                info.nickname = ui.nicknameEdit.text()
                if(ui.serverButton.isChecked()):
                    info.isServer = True

                else:
                    info.isServer = False
                    info.myIp = ui.ipEdit.text()
                    
                ui.closeWidget()
            

        elif(self.objectName()=="cancelButton"):

            return

        return super().mousePressEvent(QMouseEvent)

class EventedQRadioButton(QtWidgets.QRadioButton):


    def __init__(self, *args, **kwargs):     
        QtWidgets.QRadioButton.__init__(self,*args,**kwargs)
          
    def mousePressEvent(self, QMouseEvent):
        
        self.setChecked(not self.isChecked())
        if(self.objectName() == "serverButton"):
            
            info.memorizeIp = ui.ipEdit.text()
            ui.ipEdit.setReadOnly(True)
            ui.ipEdit.setText(info.myIp)
            
        elif(self.objectName()=="clientButton"):

            ui.ipEdit.setReadOnly(False)
            ui.ipEdit.setText(info.memorizeIp) 
        
        return super().mousePressEvent(QMouseEvent)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 200)
        Dialog.setMaximumSize(QtCore.QSize(300, 200))
        
        self.okButton = EventedQPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(60, 160, 75, 23))
        self.okButton.setObjectName("okButton")
        
        self.cancelButton = EventedQPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(160, 160, 75, 23))
        self.cancelButton.setObjectName("cancelButton")

        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 231, 51))
        self.groupBox.setObjectName("groupBox")

        self.serverButton = EventedQRadioButton(self.groupBox)
        self.serverButton.setGeometry(QtCore.QRect(40, 20, 90, 16))
        self.serverButton.setChecked(False)
        self.serverButton.setAutoRepeat(True)
        self.serverButton.setObjectName("serverButton")

        self.clientButton = EventedQRadioButton(self.groupBox)
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
        
        self.nicknameEdit = QtWidgets.QLineEdit(Dialog)
        self.nicknameEdit.setGeometry(QtCore.QRect(100, 120, 113, 20))
        self.nicknameEdit.setObjectName("nicknameEdit")
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)   

    def closeWidget(self):
        Dialog.close()

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
        self.ipEdit.setText(_translate("Dialog", "127.0.0.1"))
        self.ipEdit.setPlaceholderText(_translate("Dialog", "write ip of someone pc"))
        self.nicknameEdit.setText(_translate("Dialog", "Frogger"))
        self.nicknameEdit.setPlaceholderText(_translate("Dialog", "write your nickname"))


info = InfoStruct()
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)

def beginUI(ip):
    info.myIp = ip
    Dialog.show()
    app.exec_()
    
    return info.isServer, info.nickname, info.myIp     
   
            

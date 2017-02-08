# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class EventedQPushButton(QtWidgets.QPushButton):

    def __init__(self, *args, **kwargs):
        QtWidgets.QPushButton.__init__(self,*args,**kwargs)
        
    def mousePressEvent(self, QMouseEvent):

        if(self.objectName() == "beginButton"):
            ui.closeWidget()

        return super().mousePressEvent(QMouseEvent)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 150)
        Dialog.setMaximumSize(QtCore.QSize(200, 150))
        self.levelComboBox = QtWidgets.QComboBox(Dialog)
        self.levelComboBox.setGeometry(QtCore.QRect(100, 20, 76, 22))
        self.levelComboBox.setObjectName("levelComboBox")
        self.levelComboBox.addItem("")
        self.levelComboBox.addItem("")
        self.levelComboBox.addItem("")
        self.levelComboBox.addItem("")
        self.levelComboBox.addItem("")
        self.levelComboBox.addItem("")
        self.levelComboBox.addItem("")
        self.levelComboBox.addItem("")
        self.levelComboBox.addItem("")
        self.levelComboBox.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 56, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_2.setObjectName("label_2")
        self.speedComboBox = QtWidgets.QComboBox(Dialog)
        self.speedComboBox.setGeometry(QtCore.QRect(100, 60, 76, 22))
        self.speedComboBox.setObjectName("speedComboBox")
        self.speedComboBox.addItem("")
        self.speedComboBox.addItem("")
        self.speedComboBox.addItem("")
        self.speedComboBox.addItem("")
        self.speedComboBox.addItem("")
        self.speedComboBox.addItem("")
        self.speedComboBox.addItem("")
        self.speedComboBox.addItem("")
        self.speedComboBox.addItem("")
        self.speedComboBox.addItem("")
        self.beginButton = EventedQPushButton(Dialog)
        self.beginButton.setGeometry(QtCore.QRect(60, 110, 75, 23))
        self.beginButton.setObjectName("beginButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def closeWidget(self):
        Dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ServerDialog"))
        self.levelComboBox.setItemText(0, _translate("Dialog", "1"))
        self.levelComboBox.setItemText(1, _translate("Dialog", "2"))
        self.levelComboBox.setItemText(2, _translate("Dialog", "3"))
        self.levelComboBox.setItemText(3, _translate("Dialog", "4"))
        self.levelComboBox.setItemText(4, _translate("Dialog", "5"))
        self.levelComboBox.setItemText(5, _translate("Dialog", "6"))
        self.levelComboBox.setItemText(6, _translate("Dialog", "7"))
        self.levelComboBox.setItemText(7, _translate("Dialog", "8"))
        self.levelComboBox.setItemText(8, _translate("Dialog", "9"))
        self.levelComboBox.setItemText(9, _translate("Dialog", "10"))
        self.label.setText(_translate("Dialog", "난이도"))
        self.label_2.setText(_translate("Dialog", "스크롤 속도"))
        self.speedComboBox.setItemText(0, _translate("Dialog", "1"))
        self.speedComboBox.setItemText(1, _translate("Dialog", "2"))
        self.speedComboBox.setItemText(2, _translate("Dialog", "3"))
        self.speedComboBox.setItemText(3, _translate("Dialog", "4"))
        self.speedComboBox.setItemText(4, _translate("Dialog", "5"))
        self.speedComboBox.setItemText(5, _translate("Dialog", "6"))
        self.speedComboBox.setItemText(6, _translate("Dialog", "7"))
        self.speedComboBox.setItemText(7, _translate("Dialog", "8"))
        self.speedComboBox.setItemText(8, _translate("Dialog", "9"))
        self.speedComboBox.setItemText(9, _translate("Dialog", "10"))
        self.beginButton.setText(_translate("Dialog", "시작하기"))



import sys
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)

def beginUI():
  
    Dialog.show()
    app.exec_()

    return ui.levelComboBox.currentText(), ui.speedComboBox.currentText()
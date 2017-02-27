# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wating.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

import threading
import time

class WattingThread(threading.Thread):

    def run(self):
        while True:
            if(self.isConnect):
                break
            else:
                time.sleep(1)    
                if(self.isConnect):
                    break

                if(len(ui.postfix)>6):
                    ui.postfix =""
                ui.postfix = ui.postfix + "."
                ui.connectingEdit.setText(ui.wattingContext + ui.postfix)



class EventedQPushButton(QtWidgets.QPushButton):

    def __init__(self, *args, **kwargs):
        QtWidgets.QPushButton.__init__(self,*args,**kwargs)
        QtCore.QThread
    def mousePressEvent(self, QMouseEvent):

        if(self.objectName() == "beginButton"):
            ui.closeWidget()

        return super().mousePressEvent(QMouseEvent)


class Ui_Dialog(object):

    def setupUi(self, dialog):
        
                
        self.wattingContext = "상대방의 접속을 대기중입니다"
        self.postfix = ""
        
        dialog.setObjectName("Dialog")
        dialog.resize(200, 146)
        dialog.setMaximumSize(QtCore.QSize(200, 150))

        self.connectingEdit = QtWidgets.QLineEdit(dialog)
        self.connectingEdit.setGeometry(QtCore.QRect(0, 50, 201, 20))
        self.connectingEdit.setObjectName("connectingEdit")
        self.beginButton = EventedQPushButton(dialog)
        self.beginButton.setGeometry(QtCore.QRect(60, 110, 75, 23))
        self.beginButton.setObjectName("beginButton")
        self.beginButton.setEnabled(False)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def closeWidget(self):
        dialog.close()

    def retranslateUi(self,dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.connectingEdit.setText(_translate("Dialog", self.wattingContext))
        self.beginButton.setText(_translate("Dialog", "대기중"))



import sys
app = QtWidgets.QApplication(sys.argv)
wattingThread = WattingThread()

dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(dialog)

def beginUI():
 
    wattingThread.isConnect = False
    wattingThread.start()
  
    dialog.show()
    app.exec_()
    

    
   
        


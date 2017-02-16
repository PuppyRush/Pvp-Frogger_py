# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wating.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

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

        if(self.objectName == "beginButton"):
            ui.closeWidget()

        return super().mousePressEvent(QMouseEvent)


class Ui_Dialog(QtWidgets.QDialog):

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setModal(False)
        
        self.wattingContext = "상대방의 접속을 대기중입니다"
        self.postfix = ""
        
        self.setObjectName("Dialog")
        self.resize(200, 146)
        self.setMaximumSize(QtCore.QSize(200, 150))
        self.connectingEdit = QtWidgets.QLineEdit(self)
        self.connectingEdit.setGeometry(QtCore.QRect(0, 50, 201, 20))
        self.connectingEdit.setObjectName("connectingEdit")
        self.beginButton = QtWidgets.QPushButton(self)
        self.beginButton.setGeometry(QtCore.QRect(60, 110, 75, 23))
        self.beginButton.setObjectName("beginButton")
        self.beginButton.setEnabled(False)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.connectingEdit.setText(_translate("Dialog", self.wattingContext))
        self.beginButton.setText(_translate("Dialog", "대기중"))



import sys
app = QtWidgets.QApplication(sys.argv)
wattingThread = WattingThread()
ui = Ui_Dialog()

def beginUI():
 
    wattingThread.isConnect = False
    wattingThread.start()
  
    ui.show()
    app.exec_()
    

    
   
        


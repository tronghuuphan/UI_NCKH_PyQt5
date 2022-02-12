# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Name = QtWidgets.QTextEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(810, 380, 71, 31))
        self.Name.setFrameShape(QtWidgets.QFrame.VLine)
        self.Name.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Name.setObjectName("Name")
        self.Dayofbirth = QtWidgets.QTextEdit(self.centralwidget)
        self.Dayofbirth.setGeometry(QtCore.QRect(810, 420, 111, 31))
        self.Dayofbirth.setFrameShape(QtWidgets.QFrame.HLine)
        self.Dayofbirth.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Dayofbirth.setObjectName("Dayofbirth")
        self.inforCCCD = QtWidgets.QLabel(self.centralwidget)
        self.inforCCCD.setGeometry(QtCore.QRect(890, 340, 121, 31))
        self.inforCCCD.setText("")
        self.inforCCCD.setObjectName("inforCCCD")
        self.inforName = QtWidgets.QLabel(self.centralwidget)
        self.inforName.setGeometry(QtCore.QRect(890, 380, 121, 31))
        self.inforName.setText("")
        self.inforName.setObjectName("inforName")
        self.inforDoB = QtWidgets.QLabel(self.centralwidget)
        self.inforDoB.setGeometry(QtCore.QRect(930, 420, 91, 31))
        self.inforDoB.setText("")
        self.inforDoB.setObjectName("inforDoB")
        self.CCCD = QtWidgets.QTextEdit(self.centralwidget)
        self.CCCD.setGeometry(QtCore.QRect(810, 340, 71, 31))
        self.CCCD.setFrameShape(QtWidgets.QFrame.VLine)
        self.CCCD.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.CCCD.setObjectName("CCCD")
        self.logoclb = QtWidgets.QLabel(self.centralwidget)
        self.logoclb.setEnabled(True)
        self.logoclb.setGeometry(QtCore.QRect(930, 40, 71, 71))
        self.logoclb.setStyleSheet("image: url(:/logo/bkmaker.png);\n"
"")
        self.logoclb.setText("")
        self.logoclb.setScaledContents(True)
        self.logoclb.setObjectName("logoclb")
        self.logokhoa = QtWidgets.QLabel(self.centralwidget)
        self.logokhoa.setEnabled(True)
        self.logokhoa.setGeometry(QtCore.QRect(820, 40, 75, 71))
        self.logokhoa.setStyleSheet("image: url(:/logo2/khoadien.png);\n"
"\n"
"")
        self.logokhoa.setText("")
        self.logokhoa.setScaledContents(True)
        self.logokhoa.setObjectName("logokhoa")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(800, 0, 231, 601))
        self.background.setStyleSheet("background-image: url(:/background1/background.jpg);\n"
"")
        self.background.setText("")
        self.background.setObjectName("background")
        self.cam = QtWidgets.QLabel(self.centralwidget)
        self.cam.setGeometry(QtCore.QRect(-10, 0, 811, 601))
        self.cam.setFrameShape(QtWidgets.QFrame.Box)
        self.cam.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cam.setLineWidth(3)
        self.cam.setText("")
        self.cam.setObjectName("cam")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(830, 160, 161, 151))
        self.image.setFrameShape(QtWidgets.QFrame.Box)
        self.image.setLineWidth(1)
        self.image.setText("")
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.Name_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.Name_2.setGeometry(QtCore.QRect(810, 460, 71, 31))
        self.Name_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.Name_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Name_2.setObjectName("Name_2")
        self.inforClass = QtWidgets.QLabel(self.centralwidget)
        self.inforClass.setGeometry(QtCore.QRect(890, 460, 121, 31))
        self.inforClass.setText("")
        self.inforClass.setObjectName("inforClass")
        self.background.raise_()
        self.Name.raise_()
        self.Dayofbirth.raise_()
        self.inforCCCD.raise_()
        self.inforName.raise_()
        self.inforDoB.raise_()
        self.CCCD.raise_()
        self.logoclb.raise_()
        self.cam.raise_()
        self.logokhoa.raise_()
        self.image.raise_()
        self.Name_2.raise_()
        self.inforClass.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Name :</span></p></body></html>"))
        self.Dayofbirth.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Date of birth :</span></p></body></html>"))
        self.CCCD.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">CCCD :</span></p></body></html>"))
        self.Name_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Class :</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

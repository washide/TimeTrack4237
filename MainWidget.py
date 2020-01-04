# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(1024, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(MainWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QtWidgets.QLabel(MainWidget)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/TimeTrackLogo.png"))
        self.logo.setObjectName("logo")
        self.verticalLayout.addWidget(self.logo, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label = QtWidgets.QLabel(MainWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.message = QtWidgets.QLabel(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.message.setFont(font)
        self.message.setScaledContents(False)
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setObjectName("message")
        self.verticalLayout.addWidget(self.message, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.barcode = QtWidgets.QLineEdit(MainWidget)
        self.barcode.setText("")
        self.barcode.setAlignment(QtCore.Qt.AlignCenter)
        self.barcode.setObjectName("barcode")
        self.verticalLayout.addWidget(self.barcode)

        self.retranslateUi(MainWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "TimeTrack4237"))
        self.label.setText(_translate("MainWidget", "Scan Your Barcode"))
        self.message.setText(_translate("MainWidget", "This is a label"))

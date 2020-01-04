# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\InOutWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InOutWidget(object):
    def setupUi(self, InOutWidget):
        InOutWidget.setObjectName("InOutWidget")
        InOutWidget.resize(1024, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(InOutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QtWidgets.QLabel(InOutWidget)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/TimeTrackLogo.png"))
        self.logo.setObjectName("logo")
        self.verticalLayout.addWidget(self.logo, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.checkinButton = QtWidgets.QPushButton(InOutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkinButton.sizePolicy().hasHeightForWidth())
        self.checkinButton.setSizePolicy(sizePolicy)
        self.checkinButton.setMinimumSize(QtCore.QSize(300, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.checkinButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/checkin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkinButton.setIcon(icon)
        self.checkinButton.setIconSize(QtCore.QSize(32, 32))
        self.checkinButton.setObjectName("checkinButton")
        self.horizontalLayout.addWidget(self.checkinButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.checkoutButton = QtWidgets.QPushButton(InOutWidget)
        self.checkoutButton.setMinimumSize(QtCore.QSize(300, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.checkoutButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/checkout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkoutButton.setIcon(icon1)
        self.checkoutButton.setIconSize(QtCore.QSize(32, 32))
        self.checkoutButton.setObjectName("checkoutButton")
        self.horizontalLayout.addWidget(self.checkoutButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.cancelButton = QtWidgets.QPushButton(InOutWidget)
        self.cancelButton.setMinimumSize(QtCore.QSize(150, 100))
        self.cancelButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.verticalLayout.addWidget(self.cancelButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)

        self.retranslateUi(InOutWidget)
        QtCore.QMetaObject.connectSlotsByName(InOutWidget)

    def retranslateUi(self, InOutWidget):
        _translate = QtCore.QCoreApplication.translate
        InOutWidget.setWindowTitle(_translate("InOutWidget", "Form"))
        self.checkinButton.setText(_translate("InOutWidget", "Check In"))
        self.checkoutButton.setText(_translate("InOutWidget", "Check Out"))
        self.cancelButton.setText(_translate("InOutWidget", "Cancel"))

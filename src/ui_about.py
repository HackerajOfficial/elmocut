# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kelmo\Desktop\OLD DESKTOP\-Python\CODE\elmocut\exe\ui_about.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        MainWindow.setToolTip("")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(100, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lblFacebook = QtWidgets.QLabel(self.centralwidget)
        self.lblFacebook.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblFacebook.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFacebook.setObjectName("lblFacebook")
        self.gridLayout.addWidget(self.lblFacebook, 5, 0, 1, 1)
        self.lblTwitter = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTwitter.sizePolicy().hasHeightForWidth())
        self.lblTwitter.setSizePolicy(sizePolicy)
        self.lblTwitter.setMinimumSize(QtCore.QSize(0, 90))
        self.lblTwitter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblTwitter.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTwitter.setObjectName("lblTwitter")
        self.gridLayout.addWidget(self.lblTwitter, 5, 1, 1, 1)
        self.lblLinkedIn = QtWidgets.QLabel(self.centralwidget)
        self.lblLinkedIn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblLinkedIn.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLinkedIn.setObjectName("lblLinkedIn")
        self.gridLayout.addWidget(self.lblLinkedIn, 5, 2, 1, 1)
        self.lblGitHub = QtWidgets.QLabel(self.centralwidget)
        self.lblGitHub.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblGitHub.setAlignment(QtCore.Qt.AlignCenter)
        self.lblGitHub.setObjectName("lblGitHub")
        self.gridLayout.addWidget(self.lblGitHub, 5, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(5)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.lblAppIcon = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblAppIcon.sizePolicy().hasHeightForWidth())
        self.lblAppIcon.setSizePolicy(sizePolicy)
        self.lblAppIcon.setMinimumSize(QtCore.QSize(0, 154))
        self.lblAppIcon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblAppIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAppIcon.setObjectName("lblAppIcon")
        self.gridLayout.addWidget(self.lblAppIcon, 1, 0, 1, 4)
        self.lblAppName = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblAppName.sizePolicy().hasHeightForWidth())
        self.lblAppName.setSizePolicy(sizePolicy)
        self.lblAppName.setMinimumSize(QtCore.QSize(0, 47))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lblAppName.setFont(font)
        self.lblAppName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAppName.setObjectName("lblAppName")
        self.gridLayout.addWidget(self.lblAppName, 2, 0, 1, 4)
        self.lblMyName = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblMyName.sizePolicy().hasHeightForWidth())
        self.lblMyName.setSizePolicy(sizePolicy)
        self.lblMyName.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lblMyName.setFont(font)
        self.lblMyName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMyName.setObjectName("lblMyName")
        self.gridLayout.addWidget(self.lblMyName, 3, 0, 1, 4)
        self.lblNickName = QtWidgets.QLabel(self.centralwidget)
        self.lblNickName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNickName.setObjectName("lblNickName")
        self.gridLayout.addWidget(self.lblNickName, 4, 0, 1, 4)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "About"))
        self.lblFacebook.setText(_translate("MainWindow", "Facebook"))
        self.lblTwitter.setText(_translate("MainWindow", "Twitter"))
        self.lblLinkedIn.setText(_translate("MainWindow", "LinkedIn"))
        self.lblGitHub.setText(_translate("MainWindow", "GitHub"))
        self.lblAppIcon.setText(_translate("MainWindow", "App Icon"))
        self.lblAppName.setText(_translate("MainWindow", "App Name + Version"))
        self.lblMyName.setText(_translate("MainWindow", "My Name"))
        self.lblNickName.setText(_translate("MainWindow", "My Nick Name"))
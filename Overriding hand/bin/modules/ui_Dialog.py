# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogdvLBzv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(344, 161)
        Dialog.setStyleSheet(u"*{\n"
"color: white;\n"
"}\n"
"")
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(24,24,36);\n"
"border: 4px solid rgb(230,5,64);\n"
"border-radius: 8px")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border:none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.vboxLayout = QVBoxLayout(self.frame_2)
        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.gripFrame = QFrame(self.frame_2)
        self.gripFrame.setObjectName(u"gripFrame")
        self.gripFrame.setMinimumSize(QSize(0, 25))
        self.gripFrame.setStyleSheet(u"background-color: rgb(24,24,36);")
        self.gripFrame.setFrameShape(QFrame.StyledPanel)
        self.gripFrame.setFrameShadow(QFrame.Raised)

        self.vboxLayout.addWidget(self.gripFrame)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet(u"background-color: rgb(24,24,36);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.messageHeader = QLabel(self.frame_4)
        self.messageHeader.setObjectName(u"messageHeader")
        font = QFont()
        font.setFamily(u"Bahnschrift")
        font.setPointSize(24)
        self.messageHeader.setFont(font)
        self.messageHeader.setStyleSheet(u"color:rgb(230,5,64);")
        self.messageHeader.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.messageHeader)


        self.vboxLayout.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"background-color: rgb(24,24,36);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.messageText = QLabel(self.frame_3)
        self.messageText.setObjectName(u"messageText")
        font1 = QFont()
        font1.setFamily(u"Bahnschrift")
        font1.setPointSize(11)
        self.messageText.setFont(font1)
        self.messageText.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.messageText)

        self.messageButton = QPushButton(self.frame_3)
        self.messageButton.setObjectName(u"messageButton")
        self.messageButton.setFont(font1)
        self.messageButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.messageButton.setStyleSheet(u"QPushButton{\n"
"border:3px solid  rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.messageButton)


        self.vboxLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.messageHeader.setText(QCoreApplication.translate("Dialog", u"HeaderText", None))
        self.messageText.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.messageButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u041a", None))
    # retranslateUi


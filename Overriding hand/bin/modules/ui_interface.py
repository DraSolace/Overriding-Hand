# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceLuOSXL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1035, 615)
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icons/TryToSave.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background:transparent;")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border:none;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainframe = QFrame(self.centralwidget)
        self.mainframe.setObjectName(u"mainframe")
        self.mainframe.setFrameShape(QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.mainframe)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(3, 3, 3, 3)
        self.slideContainer = QFrame(self.mainframe)
        self.slideContainer.setObjectName(u"slideContainer")
        self.slideContainer.setMinimumSize(QSize(0, 0))
        self.slideContainer.setMaximumSize(QSize(0, 16777215))
        self.slideContainer.setStyleSheet(u"color: white;\n"
"background-color: rgb(9,5,13);\n"
"font: Bahnschrift;\n"
"outline: none;\n"
" QPushButton#pushButton:hover {\n"
"     background-color: rgb(224, 255, 0);\n"
" }")
        self.slideContainer.setFrameShape(QFrame.StyledPanel)
        self.slideContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.slideContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slidmenu = QFrame(self.slideContainer)
        self.slidmenu.setObjectName(u"slidmenu")
        self.slidmenu.setMinimumSize(QSize(198, 0))
        self.slidmenu.setStyleSheet(u"*{\n"
"font: Bahnschrift;\n"
"}\n"
"QPushButton{\n"
"border:3px solid rgb(9,5,13);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"}")
        self.slidmenu.setFrameShape(QFrame.StyledPanel)
        self.slidmenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.slidmenu)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.slidmenu)
        self.frame_8.setObjectName(u"frame_8")
        font1 = QFont()
        font1.setFamily(u"Bahnschrift")
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.frame_8.setFont(font1)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"\n"
"border-left: 3px solid rgb(230,5,64);\n"
"\n"
"border-radius: 5px;\n"
"bacground-color: rgb(17,16,26);")

        self.horizontalLayout_7.addWidget(self.label_2)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.slidmenu)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}QToolBox{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(24,24,36);\n"
"	text-align: left;\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.createScript = QPushButton(self.frame_9)
        self.createScript.setObjectName(u"createScript")
        font2 = QFont()
        font2.setFamily(u"Bahnschrift")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.createScript.setFont(font2)
        self.createScript.setCursor(QCursor(Qt.PointingHandCursor))
        self.createScript.setStyleSheet(u"font: Bahnschrift;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.createScript.setIcon(icon1)

        self.verticalLayout_7.addWidget(self.createScript)

        self.existingScriptsBut = QPushButton(self.frame_9)
        self.existingScriptsBut.setObjectName(u"existingScriptsBut")
        self.existingScriptsBut.setFont(font2)
        self.existingScriptsBut.setCursor(QCursor(Qt.PointingHandCursor))
        self.existingScriptsBut.setStyleSheet(u"font: Bahnschrift;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.existingScriptsBut.setIcon(icon2)

        self.verticalLayout_7.addWidget(self.existingScriptsBut)

        self.editScriptButton = QPushButton(self.frame_9)
        self.editScriptButton.setObjectName(u"editScriptButton")
        self.editScriptButton.setFont(font2)
        self.editScriptButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.editScriptButton.setIcon(icon3)

        self.verticalLayout_7.addWidget(self.editScriptButton)

        self.toolBox = QToolBox(self.frame_9)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setFont(font2)
        self.toolBox.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}QToolBox{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(24,24,36);\n"
"	text-align: left;\n"
"}\n"
"QToolBox::tab{\n"
"	border-radius: 5px;\n"
"	bacground-color: rgb(17,16,26);\n"
"	text-align: left;\n"
"}\n"
"QPushButton{\n"
"border:3px solid rgb(9,5,13);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:horizontal {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: mar"
                        "gin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}")
        self.doc = QWidget()
        self.doc.setObjectName(u"doc")
        self.doc.setGeometry(QRect(0, 0, 180, 350))
        self.doc.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.doc)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.doc)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(6, 0, 6, 0)
        self.introBut = QPushButton(self.frame_10)
        self.introBut.setObjectName(u"introBut")
        self.introBut.setFont(font2)
        self.introBut.setCursor(QCursor(Qt.PointingHandCursor))
        self.introBut.setStyleSheet(u"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/terminal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.introBut.setIcon(icon4)

        self.verticalLayout_9.addWidget(self.introBut)

        self.toolBox_2 = QToolBox(self.frame_10)
        self.toolBox_2.setObjectName(u"toolBox_2")
        self.toolBox_2.setFont(font2)
        self.Overscript = QWidget()
        self.Overscript.setObjectName(u"Overscript")
        self.Overscript.setGeometry(QRect(0, 0, 165, 194))
        self.horizontalLayout_20 = QHBoxLayout(self.Overscript)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.Overscript)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_26)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(6, 0, 6, 0)
        self.structureBut = QPushButton(self.frame_26)
        self.structureBut.setObjectName(u"structureBut")
        self.structureBut.setFont(font2)
        self.structureBut.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/layers.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.structureBut.setIcon(icon5)

        self.verticalLayout_20.addWidget(self.structureBut)

        self.toolBox_3 = QToolBox(self.frame_26)
        self.toolBox_3.setObjectName(u"toolBox_3")
        self.toolBox_3.setFont(font2)
        self.toolBox_3.setStyleSheet(u"")
        self.keyboard = QWidget()
        self.keyboard.setObjectName(u"keyboard")
        self.keyboard.setGeometry(QRect(0, 0, 121, 72))
        self.horizontalLayout_52 = QHBoxLayout(self.keyboard)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.keyboard)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFont(font1)
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_27)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.sendButton = QPushButton(self.frame_27)
        self.sendButton.setObjectName(u"sendButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy1)
        self.sendButton.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamily(u"Bahnschrift")
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setWeight(50)
        self.sendButton.setFont(font3)
        self.sendButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.sendButton.setStyleSheet(u"QPushButton{\n"
"border-left:3px solid rgb(230,5,64);\n"
"}")

        self.verticalLayout_22.addWidget(self.sendButton)

        self.writeButton = QPushButton(self.frame_27)
        self.writeButton.setObjectName(u"writeButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(100)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.writeButton.sizePolicy().hasHeightForWidth())
        self.writeButton.setSizePolicy(sizePolicy2)
        self.writeButton.setMaximumSize(QSize(16777215, 30))
        self.writeButton.setFont(font2)
        self.writeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.writeButton.setStyleSheet(u"QPushButton{\n"
"border-left:3px solid rgb(230,5,64);\n"
"}")

        self.verticalLayout_22.addWidget(self.writeButton)

        self.kPRButton = QPushButton(self.frame_27)
        self.kPRButton.setObjectName(u"kPRButton")
        sizePolicy1.setHeightForWidth(self.kPRButton.sizePolicy().hasHeightForWidth())
        self.kPRButton.setSizePolicy(sizePolicy1)
        self.kPRButton.setMaximumSize(QSize(16777215, 30))
        self.kPRButton.setFont(font2)
        self.kPRButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.kPRButton.setStyleSheet(u"QPushButton{\n"
"border-left:3px solid rgb(230,5,64);\n"
"}")

        self.verticalLayout_22.addWidget(self.kPRButton)


        self.horizontalLayout_52.addWidget(self.frame_27)

        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/codesandbox.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox_3.addItem(self.keyboard, icon6, u"\u041a\u043b\u0430\u0432\u0438\u0430\u0442\u0443\u0440\u0430")
        self.mouse = QWidget()
        self.mouse.setObjectName(u"mouse")
        self.mouse.setGeometry(QRect(0, 0, 129, 120))
        self.horizontalLayout_39 = QHBoxLayout(self.mouse)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_48 = QFrame(self.mouse)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_48)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.moveButton = QPushButton(self.frame_48)
        self.moveButton.setObjectName(u"moveButton")
        sizePolicy1.setHeightForWidth(self.moveButton.sizePolicy().hasHeightForWidth())
        self.moveButton.setSizePolicy(sizePolicy1)
        self.moveButton.setMaximumSize(QSize(16777215, 30))
        self.moveButton.setFont(font2)
        self.moveButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.moveButton.setStyleSheet(u"QPushButton{\n"
"border-left:3px solid rgb(230,5,64);\n"
"}")

        self.verticalLayout_29.addWidget(self.moveButton)

        self.PosButton = QPushButton(self.frame_48)
        self.PosButton.setObjectName(u"PosButton")
        sizePolicy1.setHeightForWidth(self.PosButton.sizePolicy().hasHeightForWidth())
        self.PosButton.setSizePolicy(sizePolicy1)
        self.PosButton.setMaximumSize(QSize(16777215, 30))
        self.PosButton.setFont(font2)
        self.PosButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.PosButton.setStyleSheet(u"QPushButton{\n"
"border-left:3px solid rgb(230,5,64);\n"
"}")

        self.verticalLayout_29.addWidget(self.PosButton)

        self.clickButton = QPushButton(self.frame_48)
        self.clickButton.setObjectName(u"clickButton")
        sizePolicy1.setHeightForWidth(self.clickButton.sizePolicy().hasHeightForWidth())
        self.clickButton.setSizePolicy(sizePolicy1)
        self.clickButton.setMaximumSize(QSize(16777215, 30))
        self.clickButton.setFont(font2)
        self.clickButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.clickButton.setStyleSheet(u"QPushButton{\n"
"border-left:3px solid rgb(230,5,64);\n"
"}")

        self.verticalLayout_29.addWidget(self.clickButton)

        self.mPressButton = QPushButton(self.frame_48)
        self.mPressButton.setObjectName(u"mPressButton")
        sizePolicy1.setHeightForWidth(self.mPressButton.sizePolicy().hasHeightForWidth())
        self.mPressButton.setSizePolicy(sizePolicy1)
        self.mPressButton.setMaximumSize(QSize(16777215, 30))
        self.mPressButton.setFont(font2)
        self.mPressButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.mPressButton.setStyleSheet(u"QPushButton{\n"
"border-left:3px solid rgb(230,5,64);\n"
"}")

        self.verticalLayout_29.addWidget(self.mPressButton)

        self.wheelButton = QPushButton(self.frame_48)
        self.wheelButton.setObjectName(u"wheelButton")
        sizePolicy1.setHeightForWidth(self.wheelButton.sizePolicy().hasHeightForWidth())
        self.wheelButton.setSizePolicy(sizePolicy1)
        self.wheelButton.setMaximumSize(QSize(16777215, 30))
        self.wheelButton.setFont(font2)
        self.wheelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.wheelButton.setStyleSheet(u"QPushButton{\n"
"border-left:3px solid rgb(230,5,64);\n"
"}")

        self.verticalLayout_29.addWidget(self.wheelButton)


        self.horizontalLayout_39.addWidget(self.frame_48)

        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/mouse-pointer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox_3.addItem(self.mouse, icon7, u"\u041c\u044b\u0448\u044c")

        self.verticalLayout_20.addWidget(self.toolBox_3)

        self.waitButton = QPushButton(self.frame_26)
        self.waitButton.setObjectName(u"waitButton")
        self.waitButton.setFont(font2)
        self.waitButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/pause-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.waitButton.setIcon(icon8)

        self.verticalLayout_20.addWidget(self.waitButton)

        self.keysButton = QPushButton(self.frame_26)
        self.keysButton.setObjectName(u"keysButton")
        self.keysButton.setFont(font2)
        self.keysButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.keysButton.setIcon(icon9)

        self.verticalLayout_20.addWidget(self.keysButton)


        self.horizontalLayout_20.addWidget(self.frame_26)

        self.toolBox_2.addItem(self.Overscript, icon3, u"Overscript")
        self.Appendix = QWidget()
        self.Appendix.setObjectName(u"Appendix")
        self.Appendix.setGeometry(QRect(0, 0, 180, 262))
        self.horizontalLayout_65 = QHBoxLayout(self.Appendix)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.frame_85 = QFrame(self.Appendix)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_85)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.fileNameBut = QPushButton(self.frame_85)
        self.fileNameBut.setObjectName(u"fileNameBut")
        sizePolicy1.setHeightForWidth(self.fileNameBut.sizePolicy().hasHeightForWidth())
        self.fileNameBut.setSizePolicy(sizePolicy1)
        self.fileNameBut.setMaximumSize(QSize(16777215, 30))
        self.fileNameBut.setFont(font2)
        self.fileNameBut.setCursor(QCursor(Qt.PointingHandCursor))
        self.fileNameBut.setStyleSheet(u"QPushButton{\n"
"border-left:3px solid rgb(230,5,64);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"}")

        self.verticalLayout_49.addWidget(self.fileNameBut)

        self.NonUsedSymbolsBut = QPushButton(self.frame_85)
        self.NonUsedSymbolsBut.setObjectName(u"NonUsedSymbolsBut")
        sizePolicy1.setHeightForWidth(self.NonUsedSymbolsBut.sizePolicy().hasHeightForWidth())
        self.NonUsedSymbolsBut.setSizePolicy(sizePolicy1)
        self.NonUsedSymbolsBut.setMaximumSize(QSize(16777215, 30))
        self.NonUsedSymbolsBut.setFont(font2)
        self.NonUsedSymbolsBut.setCursor(QCursor(Qt.PointingHandCursor))
        self.NonUsedSymbolsBut.setStyleSheet(u"QPushButton{\n"
"border-left:3px solid rgb(230,5,64);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"}")
        self.NonUsedSymbolsBut.setCheckable(False)
        self.NonUsedSymbolsBut.setChecked(False)
        self.NonUsedSymbolsBut.setFlat(False)

        self.verticalLayout_49.addWidget(self.NonUsedSymbolsBut)

        self.OverLapBut = QPushButton(self.frame_85)
        self.OverLapBut.setObjectName(u"OverLapBut")
        sizePolicy1.setHeightForWidth(self.OverLapBut.sizePolicy().hasHeightForWidth())
        self.OverLapBut.setSizePolicy(sizePolicy1)
        self.OverLapBut.setMaximumSize(QSize(16777215, 30))
        self.OverLapBut.setFont(font2)
        self.OverLapBut.setCursor(QCursor(Qt.PointingHandCursor))
        self.OverLapBut.setStyleSheet(u"QPushButton{\n"
"border-left:3px solid rgb(230,5,64);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"}")

        self.verticalLayout_49.addWidget(self.OverLapBut)


        self.horizontalLayout_65.addWidget(self.frame_85, 0, Qt.AlignTop)

        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/command.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox_2.addItem(self.Appendix, icon10, u"\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435")

        self.verticalLayout_9.addWidget(self.toolBox_2)


        self.verticalLayout_8.addWidget(self.frame_10)

        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/book-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon11.addFile(u":/icons/icons/book.svg", QSize(), QIcon.Normal, QIcon.On)
        icon11.addFile(u":/icons/icons/book.svg", QSize(), QIcon.Disabled, QIcon.Off)
        icon11.addFile(u":/icons/icons/book.svg", QSize(), QIcon.Active, QIcon.Off)
        self.toolBox.addItem(self.doc, icon11, u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u044f")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 190, 350))
        self.page_2.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.page_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.page_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.oneRepeatIssueButton = QPushButton(self.frame_11)
        self.oneRepeatIssueButton.setObjectName(u"oneRepeatIssueButton")
        sizePolicy1.setHeightForWidth(self.oneRepeatIssueButton.sizePolicy().hasHeightForWidth())
        self.oneRepeatIssueButton.setSizePolicy(sizePolicy1)
        self.oneRepeatIssueButton.setMaximumSize(QSize(16777215, 39))
        self.oneRepeatIssueButton.setSizeIncrement(QSize(0, 0))
        self.oneRepeatIssueButton.setFont(font2)
        self.oneRepeatIssueButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.oneRepeatIssueButton.setStyleSheet(u"QPushButton{\n"
"border-left:3px solid rgb(230,5,64);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"}")

        self.horizontalLayout_66.addWidget(self.oneRepeatIssueButton)


        self.verticalLayout_10.addWidget(self.frame_11, 0, Qt.AlignTop)

        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/zap.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_2, icon12, u"\u0420\u0435\u0448\u0435\u043d\u0438\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c")
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.page_13.setGeometry(QRect(0, 0, 180, 350))
        self.horizontalLayout_63 = QHBoxLayout(self.page_13)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.frame_82 = QFrame(self.page_13)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_82)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.settingsBut = QPushButton(self.frame_82)
        self.settingsBut.setObjectName(u"settingsBut")
        self.settingsBut.setFont(font2)
        self.settingsBut.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/tool.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBut.setIcon(icon13)
        self.settingsBut.setIconSize(QSize(16, 16))

        self.verticalLayout_46.addWidget(self.settingsBut)

        self.gitHubBut = QPushButton(self.frame_82)
        self.gitHubBut.setObjectName(u"gitHubBut")
        self.gitHubBut.setFont(font2)
        self.gitHubBut.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/github.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.gitHubBut.setIcon(icon14)
        self.gitHubBut.setIconSize(QSize(16, 16))

        self.verticalLayout_46.addWidget(self.gitHubBut)


        self.horizontalLayout_63.addWidget(self.frame_82, 0, Qt.AlignTop)

        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/moon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_13, icon15, u"\u0420\u0430\u0437\u043d\u043e\u0435")

        self.verticalLayout_7.addWidget(self.toolBox)


        self.verticalLayout_6.addWidget(self.frame_9)

        self.frame_83 = QFrame(self.slidmenu)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.exit_button = QPushButton(self.frame_83)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setFont(font2)
        self.exit_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/external-link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon16)
        self.exit_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_8.addWidget(self.exit_button, 0, Qt.AlignBottom)


        self.verticalLayout_6.addWidget(self.frame_83)


        self.verticalLayout_2.addWidget(self.slidmenu)


        self.horizontalLayout_64.addWidget(self.slideContainer)

        self.mainbody = QFrame(self.mainframe)
        self.mainbody.setObjectName(u"mainbody")
        self.mainbody.setStyleSheet(u"*{\n"
"color: white;\n"
"}\n"
"*{\n"
"border: none;\n"
"color: white;\n"
"background-color: rgb(24,24,36);\n"
"}\n"
"")
        self.mainbody.setFrameShape(QFrame.StyledPanel)
        self.mainbody.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.mainbody)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.mainbody)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(9,5,13);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.header_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.open_close_side_bar_btn = QPushButton(self.frame_6)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        self.open_close_side_bar_btn.setBaseSize(QSize(0, 0))
        self.open_close_side_bar_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_close_side_bar_btn.setStyleSheet(u"outline: none;\n"
"border: none;\n"
"")
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon17)
        self.open_close_side_bar_btn.setIconSize(QSize(42, 42))

        self.verticalLayout_5.addWidget(self.open_close_side_bar_btn)


        self.horizontalLayout_3.addWidget(self.frame_6, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_2 = QFrame(self.header_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.quickUse = QLineEdit(self.frame_2)
        self.quickUse.setObjectName(u"quickUse")
        self.quickUse.setMinimumSize(QSize(133, 0))
        font4 = QFont()
        font4.setFamily(u"Bahnschrift")
        self.quickUse.setFont(font4)
        self.quickUse.setStyleSheet(u"border-bottom: 3px solid rgb(230,5,64)")

        self.horizontalLayout_6.addWidget(self.quickUse, 0, Qt.AlignLeft)

        self.quickUseButton = QPushButton(self.frame_2)
        self.quickUseButton.setObjectName(u"quickUseButton")
        self.quickUseButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.quickUseButton.setStyleSheet(u"outline: none;\n"
"border: none;\n"
"")
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.quickUseButton.setIcon(icon18)
        self.quickUseButton.setIconSize(QSize(20, 20))
        self.quickUseButton.setAutoDefault(False)

        self.horizontalLayout_6.addWidget(self.quickUseButton, 0, Qt.AlignLeft)


        self.horizontalLayout_3.addWidget(self.frame_2, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_3 = QFrame(self.header_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 0))
        self.pushButton_5.setStyleSheet(u"outline: none;\n"
"border: none;\n"
"")

        self.horizontalLayout_5.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"outline: none;\n"
"border: none;\n"
"")

        self.horizontalLayout_5.addWidget(self.pushButton_4)


        self.horizontalLayout_3.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_4 = QFrame(self.header_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.frame_4)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        self.minimize_window_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_window_button.setStyleSheet(u"outline: none;\n"
"border: none;\n"
"")
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/arrow-down-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon19)
        self.minimize_window_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.frame_4)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.restore_window_button.setStyleSheet(u"outline: none;\n"
"border: none;\n"
"")
        icon20 = QIcon()
        icon20.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon20)
        self.restore_window_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.frame_4)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_window_button.setStyleSheet(u"outline: none;\n"
"border: none;\n"
"")
        icon21 = QIcon()
        icon21.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon21)
        self.close_window_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.close_window_button)


        self.horizontalLayout_3.addWidget(self.frame_4, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header_frame)

        self.maincontet = QFrame(self.mainbody)
        self.maincontet.setObjectName(u"maincontet")
        sizePolicy.setHeightForWidth(self.maincontet.sizePolicy().hasHeightForWidth())
        self.maincontet.setSizePolicy(sizePolicy)
        self.maincontet.setFrameShape(QFrame.StyledPanel)
        self.maincontet.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.maincontet)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.stackedWidget = QStackedWidget(self.maincontet)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.mainmenu = QWidget()
        self.mainmenu.setObjectName(u"mainmenu")
        self.verticalLayout_13 = QVBoxLayout(self.mainmenu)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_12 = QFrame(self.mainmenu)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_6 = QLabel(self.frame_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(200, 200))
        self.label_6.setMaximumSize(QSize(200, 200))
        self.label_6.setStyleSheet(u"")
        self.label_6.setPixmap(QPixmap(u":/icons/icons/TryToSave.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_6, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_5 = QLabel(self.frame_12)
        self.label_5.setObjectName(u"label_5")
        font5 = QFont()
        font5.setFamily(u"Bahnschrift SemiBold SemiConden")
        font5.setPointSize(30)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setWeight(75)
        font5.setStrikeOut(False)
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"")

        self.verticalLayout_14.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.mainmenu)
        self.editScript = QWidget()
        self.editScript.setObjectName(u"editScript")
        self.verticalLayout_57 = QVBoxLayout(self.editScript)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.frame_98 = QFrame(self.editScript)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setStyleSheet(u"QPushButton{\n"
"border:3px solid rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontr"
                        "ol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_98)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.frame_99 = QFrame(self.frame_98)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_99)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.codeRewriteEditor = QPlainTextEdit(self.frame_99)
        self.codeRewriteEditor.setObjectName(u"codeRewriteEditor")
        font6 = QFont()
        font6.setFamily(u"Bahnschrift")
        font6.setPointSize(11)
        self.codeRewriteEditor.setFont(font6)
        self.codeRewriteEditor.setStyleSheet(u"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"text-align: left;")
        self.codeRewriteEditor.setBackgroundVisible(True)

        self.horizontalLayout_79.addWidget(self.codeRewriteEditor)


        self.horizontalLayout_78.addWidget(self.frame_99)

        self.frame_100 = QFrame(self.frame_98)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_100)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.backToEx = QPushButton(self.frame_100)
        self.backToEx.setObjectName(u"backToEx")
        self.backToEx.setFont(font6)
        self.backToEx.setCursor(QCursor(Qt.PointingHandCursor))
        self.backToEx.setStyleSheet(u"")
        self.backToEx.setIcon(icon2)

        self.verticalLayout_53.addWidget(self.backToEx)

        self.frame_103 = QFrame(self.frame_100)
        self.frame_103.setObjectName(u"frame_103")
        sizePolicy.setHeightForWidth(self.frame_103.sizePolicy().hasHeightForWidth())
        self.frame_103.setSizePolicy(sizePolicy)
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_103)
        self.verticalLayout_56.setSpacing(6)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_56.addItem(self.verticalSpacer_2)

        self.ChooseFileBut = QPushButton(self.frame_103)
        self.ChooseFileBut.setObjectName(u"ChooseFileBut")
        self.ChooseFileBut.setFont(font6)
        self.ChooseFileBut.setCursor(QCursor(Qt.PointingHandCursor))
        icon22 = QIcon()
        icon22.addFile(u":/icons/icons/navigation.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ChooseFileBut.setIcon(icon22)

        self.verticalLayout_56.addWidget(self.ChooseFileBut)

        self.editFileLine = QLineEdit(self.frame_103)
        self.editFileLine.setObjectName(u"editFileLine")
        self.editFileLine.setFont(font6)
        self.editFileLine.setStyleSheet(u"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"text-align: left;")

        self.verticalLayout_56.addWidget(self.editFileLine)

        self.RewriteBut = QPushButton(self.frame_103)
        self.RewriteBut.setObjectName(u"RewriteBut")
        self.RewriteBut.setFont(font6)
        self.RewriteBut.setCursor(QCursor(Qt.PointingHandCursor))
        self.RewriteBut.setStyleSheet(u"")
        icon23 = QIcon()
        icon23.addFile(u":/icons/icons/check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.RewriteBut.setIcon(icon23)

        self.verticalLayout_56.addWidget(self.RewriteBut, 0, Qt.AlignTop)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_56.addItem(self.verticalSpacer_3)


        self.verticalLayout_53.addWidget(self.frame_103)

        self.frame_101 = QFrame(self.frame_100)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_101)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.ChosenFileLableIsOpen = QLabel(self.frame_101)
        self.ChosenFileLableIsOpen.setObjectName(u"ChosenFileLableIsOpen")
        self.ChosenFileLableIsOpen.setFont(font6)
        self.ChosenFileLableIsOpen.setStyleSheet(u"color: rgb(230,5,64);")
        self.ChosenFileLableIsOpen.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.ChosenFileLableIsOpen)

        self.ChosenFileLableSEMEN = QLabel(self.frame_101)
        self.ChosenFileLableSEMEN.setObjectName(u"ChosenFileLableSEMEN")
        font7 = QFont()
        font7.setFamily(u"Bahnschrift")
        font7.setPointSize(12)
        self.ChosenFileLableSEMEN.setFont(font7)
        self.ChosenFileLableSEMEN.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.ChosenFileLableSEMEN)


        self.verticalLayout_53.addWidget(self.frame_101)


        self.horizontalLayout_78.addWidget(self.frame_100, 0, Qt.AlignLeft)


        self.verticalLayout_57.addWidget(self.frame_98)

        self.stackedWidget.addWidget(self.editScript)
        self.makeScript = QWidget()
        self.makeScript.setObjectName(u"makeScript")
        font8 = QFont()
        font8.setPointSize(11)
        self.makeScript.setFont(font8)
        self.makeScript.setStyleSheet(u"QPushButton:hover:!pressed\n"
"{\n"
"border-bottom: 3px solid rgb(230,5,64);\n"
"border-radius: 3px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}")
        self.horizontalLayout_12 = QHBoxLayout(self.makeScript)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_17 = QFrame(self.makeScript)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"QPushButton{\n"
"border:3px solid rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontr"
                        "ol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.codeEditor = QPlainTextEdit(self.frame_18)
        self.codeEditor.setObjectName(u"codeEditor")
        self.codeEditor.setFont(font6)
        self.codeEditor.setStyleSheet(u"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"text-align: left;")
        self.codeEditor.setBackgroundVisible(True)

        self.horizontalLayout_14.addWidget(self.codeEditor)


        self.horizontalLayout_13.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_19)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_21)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_21)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.posButton = QPushButton(self.frame)
        self.posButton.setObjectName(u"posButton")
        self.posButton.setFont(font6)
        self.posButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.posButton.setIcon(icon22)

        self.verticalLayout_47.addWidget(self.posButton, 0, Qt.AlignTop)

        self.posLable = QLabel(self.frame)
        self.posLable.setObjectName(u"posLable")
        self.posLable.setFont(font6)
        self.posLable.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.posLable)

        self.posHelpButton = QLabel(self.frame)
        self.posHelpButton.setObjectName(u"posHelpButton")
        font9 = QFont()
        font9.setFamily(u"Bahnschrift")
        font9.setPointSize(9)
        font9.setStyleStrategy(QFont.PreferDefault)
        self.posHelpButton.setFont(font9)
        self.posHelpButton.setStyleSheet(u"color: rgba(255,255,255,100);")
        self.posHelpButton.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.posHelpButton)


        self.verticalLayout_18.addWidget(self.frame, 0, Qt.AlignTop)


        self.verticalLayout_17.addWidget(self.frame_21)

        self.frame_84 = QFrame(self.frame_19)
        self.frame_84.setObjectName(u"frame_84")
        sizePolicy.setHeightForWidth(self.frame_84.sizePolicy().hasHeightForWidth())
        self.frame_84.setSizePolicy(sizePolicy)
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_84)
        self.verticalLayout_48.setSpacing(6)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_48.addItem(self.verticalSpacer_4)

        self.nameLine = QLineEdit(self.frame_84)
        self.nameLine.setObjectName(u"nameLine")
        self.nameLine.setFont(font6)
        self.nameLine.setStyleSheet(u"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"text-align: left;")

        self.verticalLayout_48.addWidget(self.nameLine, 0, Qt.AlignBottom)

        self.createButton = QPushButton(self.frame_84)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setFont(font6)
        self.createButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.createButton.setStyleSheet(u"")
        self.createButton.setIcon(icon23)

        self.verticalLayout_48.addWidget(self.createButton, 0, Qt.AlignTop)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_48.addItem(self.verticalSpacer_5)


        self.verticalLayout_17.addWidget(self.frame_84)


        self.horizontalLayout_13.addWidget(self.frame_19, 0, Qt.AlignLeft)


        self.horizontalLayout_12.addWidget(self.frame_17)

        self.stackedWidget.addWidget(self.makeScript)
        self.ExistingScript = QWidget()
        self.ExistingScript.setObjectName(u"ExistingScript")
        self.ExistingScript.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.horizontalLayout_83 = QHBoxLayout(self.ExistingScript)
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.frame_102 = QFrame(self.ExistingScript)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_102)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.frame_106 = QFrame(self.frame_102)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_106)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.frame_104 = QFrame(self.frame_106)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setFont(font6)
        self.frame_104.setStyleSheet(u"color: rgb(230,5,64);")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_85.setSpacing(6)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_104)
        self.label_4.setObjectName(u"label_4")
        font10 = QFont()
        font10.setFamily(u"Bahnschrift")
        font10.setPointSize(11)
        font10.setBold(True)
        font10.setWeight(75)
        self.label_4.setFont(font10)
        self.label_4.setStyleSheet(u"color: rgb(230,5,64);\n"
"border-right: 3px solid rgb(230,5,64);\n"
"border-left: 3px solid rgb(24,24,36);\n"
"border-radius: 7px;\n"
"border-bottom: 3px solid rgb(230,5,64);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_85.addWidget(self.label_4)

        self.label_9 = QLabel(self.frame_104)
        self.label_9.setObjectName(u"label_9")
        font11 = QFont()
        font11.setFamily(u"Bahnschrift")
        font11.setPointSize(11)
        font11.setBold(True)
        font11.setItalic(False)
        font11.setWeight(75)
        font11.setStyleStrategy(QFont.PreferDefault)
        self.label_9.setFont(font11)
        self.label_9.setStyleSheet(u"border-left: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"border-right: 3px solid rgb(24,24,36);\n"
"border-bottom: 3px solid rgb(230,5,64);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_85.addWidget(self.label_9)


        self.verticalLayout_58.addWidget(self.frame_104, 0, Qt.AlignTop)

        self.frame_105 = QFrame(self.frame_106)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_105)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.frame_107 = QFrame(self.frame_105)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_107)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_107)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QPushButton{\n"
"border:3px solid rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontr"
                        "ol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:horizontal {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7"
                        "px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 292, 30))
        self.scrollAreaWidgetContents.setStyleSheet(u"QPushButton{\n"
"border:3px solid rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontr"
                        "ol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.verticalLayout_59 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_59.setSpacing(6)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.exMacroTable = QFrame(self.scrollAreaWidgetContents)
        self.exMacroTable.setObjectName(u"exMacroTable")
        self.exMacroTable.setMaximumSize(QSize(500, 45))
        self.exMacroTable.setStyleSheet(u"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"text-align: left;\n"
"\n"
"QPushButton{\n"
"border:3px solid rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    bo"
                        "rder-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.exMacroTable.setFrameShape(QFrame.StyledPanel)
        self.exMacroTable.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.exMacroTable)
        self.horizontalLayout_84.setSpacing(3)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 3, 0)
        self.exMacroName = QLabel(self.exMacroTable)
        self.exMacroName.setObjectName(u"exMacroName")
        font12 = QFont()
        font12.setFamily(u"Bahnschrift")
        font12.setPointSize(13)
        font12.setBold(False)
        font12.setItalic(False)
        font12.setUnderline(False)
        font12.setWeight(50)
        font12.setStrikeOut(False)
        font12.setKerning(False)
        self.exMacroName.setFont(font12)
        self.exMacroName.setStyleSheet(u"border: 0px red;\n"
"color: rgb(230,5,64);")
        self.exMacroName.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_84.addWidget(self.exMacroName)

        self.exMacroRun = QPushButton(self.exMacroTable)
        self.exMacroRun.setObjectName(u"exMacroRun")
        self.exMacroRun.setFont(font6)
        self.exMacroRun.setCursor(QCursor(Qt.PointingHandCursor))
        self.exMacroRun.setStyleSheet(u"QPushButton{\n"
"border:3px solid rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}")
        self.exMacroRun.setIcon(icon23)

        self.horizontalLayout_84.addWidget(self.exMacroRun)

        self.exMacroChange = QPushButton(self.exMacroTable)
        self.exMacroChange.setObjectName(u"exMacroChange")
        self.exMacroChange.setFont(font6)
        self.exMacroChange.setCursor(QCursor(Qt.PointingHandCursor))
        self.exMacroChange.setStyleSheet(u"QPushButton{\n"
"border:3px solid rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}")
        icon24 = QIcon()
        icon24.addFile(u":/icons/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exMacroChange.setIcon(icon24)

        self.horizontalLayout_84.addWidget(self.exMacroChange)

        self.exMacroDelete = QPushButton(self.exMacroTable)
        self.exMacroDelete.setObjectName(u"exMacroDelete")
        self.exMacroDelete.setFont(font6)
        self.exMacroDelete.setCursor(QCursor(Qt.PointingHandCursor))
        self.exMacroDelete.setStyleSheet(u"QPushButton{\n"
"border:3px solid rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}")
        icon25 = QIcon()
        icon25.addFile(u":/icons/icons/file-minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exMacroDelete.setIcon(icon25)

        self.horizontalLayout_84.addWidget(self.exMacroDelete)


        self.verticalLayout_59.addWidget(self.exMacroTable)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_81.addWidget(self.scrollArea)


        self.horizontalLayout_80.addWidget(self.frame_107)

        self.frame_108 = QFrame(self.frame_105)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_108)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.frame_108)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 152, 48))
        self.verticalLayout_60 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.workMacroTable = QFrame(self.scrollAreaWidgetContents_2)
        self.workMacroTable.setObjectName(u"workMacroTable")
        self.workMacroTable.setMaximumSize(QSize(500, 45))
        self.workMacroTable.setStyleSheet(u"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"text-align: left;\n"
"\n"
"QPushButton{\n"
"border:3px solid rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    bo"
                        "rder-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.workMacroTable.setFrameShape(QFrame.StyledPanel)
        self.workMacroTable.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.workMacroTable)
        self.horizontalLayout_86.setSpacing(3)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 3, 0)
        self.workMacroName = QLabel(self.workMacroTable)
        self.workMacroName.setObjectName(u"workMacroName")
        self.workMacroName.setFont(font12)
        self.workMacroName.setStyleSheet(u"border: 0px red;\n"
"color: rgb(230,5,64);")
        self.workMacroName.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_86.addWidget(self.workMacroName)

        self.workMacroTerminate = QPushButton(self.workMacroTable)
        self.workMacroTerminate.setObjectName(u"workMacroTerminate")
        self.workMacroTerminate.setFont(font6)
        self.workMacroTerminate.setCursor(QCursor(Qt.PointingHandCursor))
        self.workMacroTerminate.setStyleSheet(u"QPushButton{\n"
"border:3px solid rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}")
        icon26 = QIcon()
        icon26.addFile(u":/icons/icons/power.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.workMacroTerminate.setIcon(icon26)

        self.horizontalLayout_86.addWidget(self.workMacroTerminate)


        self.verticalLayout_60.addWidget(self.workMacroTable)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_82.addWidget(self.scrollArea_2)


        self.horizontalLayout_80.addWidget(self.frame_108)


        self.verticalLayout_58.addWidget(self.frame_105)


        self.verticalLayout_55.addWidget(self.frame_106)


        self.horizontalLayout_83.addWidget(self.frame_102)

        self.stackedWidget.addWidget(self.ExistingScript)
        self.intro = QWidget()
        self.intro.setObjectName(u"intro")
        self.intro.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.intro)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_13 = QFrame(self.intro)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_13)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.frame_16)
        self.label_7.setObjectName(u"label_7")
        font13 = QFont()
        font13.setFamily(u"Bahnschrift")
        font13.setPointSize(24)
        font13.setBold(False)
        font13.setWeight(50)
        self.label_7.setFont(font13)
        self.label_7.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_7.setWordWrap(True)

        self.horizontalLayout_9.addWidget(self.label_7, 0, Qt.AlignVCenter)


        self.verticalLayout_16.addWidget(self.frame_16, 0, Qt.AlignTop)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")
        font14 = QFont()
        font14.setFamily(u"Bahnschrift")
        font14.setPointSize(11)
        font14.setBold(False)
        font14.setWeight(50)
        self.label_8.setFont(font14)
        self.label_8.setWordWrap(True)

        self.horizontalLayout_10.addWidget(self.label_8, 0, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.frame_14, 0, Qt.AlignTop)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.textEdit = QTextEdit(self.frame_15)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFont(font8)
        self.textEdit.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_11.addWidget(self.textEdit)


        self.verticalLayout_16.addWidget(self.frame_15)


        self.verticalLayout_15.addWidget(self.frame_13)

        self.stackedWidget.addWidget(self.intro)
        self.OverScriptStructure = QWidget()
        self.OverScriptStructure.setObjectName(u"OverScriptStructure")
        self.OverScriptStructure.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.horizontalLayout_15 = QHBoxLayout(self.OverScriptStructure)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_25 = QFrame(self.OverScriptStructure)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_20 = QFrame(self.frame_25)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_20)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_10 = QLabel(self.frame_22)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font13)
        self.label_10.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_10.setWordWrap(True)

        self.horizontalLayout_16.addWidget(self.label_10, 0, Qt.AlignVCenter)


        self.verticalLayout_19.addWidget(self.frame_22, 0, Qt.AlignTop)

        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_11 = QLabel(self.frame_23)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font14)
        self.label_11.setWordWrap(True)

        self.horizontalLayout_17.addWidget(self.label_11, 0, Qt.AlignTop)


        self.verticalLayout_19.addWidget(self.frame_23, 0, Qt.AlignTop)

        self.frame_24 = QFrame(self.frame_20)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.textBrowser = QTextBrowser(self.frame_24)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textBrowser.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.horizontalLayout_18.addWidget(self.textBrowser)


        self.verticalLayout_19.addWidget(self.frame_24)


        self.horizontalLayout_19.addWidget(self.frame_20)


        self.horizontalLayout_15.addWidget(self.frame_25)

        self.stackedWidget.addWidget(self.OverScriptStructure)
        self.send = QWidget()
        self.send.setObjectName(u"send")
        self.horizontalLayout_25 = QHBoxLayout(self.send)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.frame_28 = QFrame(self.send)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_29)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_12 = QLabel(self.frame_30)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font13)
        self.label_12.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_12.setScaledContents(False)
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_12.setWordWrap(True)

        self.horizontalLayout_22.addWidget(self.label_12, 0, Qt.AlignVCenter)


        self.verticalLayout_23.addWidget(self.frame_30, 0, Qt.AlignTop)

        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        sizePolicy.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy)
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_13 = QLabel(self.frame_31)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font14)
        self.label_13.setWordWrap(True)

        self.horizontalLayout_23.addWidget(self.label_13, 0, Qt.AlignTop)


        self.verticalLayout_23.addWidget(self.frame_31, 0, Qt.AlignTop)

        self.frame_32 = QFrame(self.frame_29)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.textBrowser_2 = QTextBrowser(self.frame_32)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.textBrowser_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textBrowser_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.horizontalLayout_24.addWidget(self.textBrowser_2)


        self.verticalLayout_23.addWidget(self.frame_32)


        self.horizontalLayout_21.addWidget(self.frame_29)


        self.horizontalLayout_25.addWidget(self.frame_28)

        self.stackedWidget.addWidget(self.send)
        self.write = QWidget()
        self.write.setObjectName(u"write")
        self.horizontalLayout_30 = QHBoxLayout(self.write)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.frame_33 = QFrame(self.write)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_34)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_14 = QLabel(self.frame_35)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font13)
        self.label_14.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_14.setScaledContents(False)
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_14.setWordWrap(True)

        self.horizontalLayout_27.addWidget(self.label_14, 0, Qt.AlignVCenter)


        self.verticalLayout_24.addWidget(self.frame_35, 0, Qt.AlignTop)

        self.frame_36 = QFrame(self.frame_34)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy)
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_15 = QLabel(self.frame_36)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font14)
        self.label_15.setWordWrap(True)

        self.horizontalLayout_28.addWidget(self.label_15, 0, Qt.AlignTop)


        self.verticalLayout_24.addWidget(self.frame_36, 0, Qt.AlignTop)

        self.frame_37 = QFrame(self.frame_34)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.textBrowser_3 = QTextBrowser(self.frame_37)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setFont(font8)
        self.textBrowser_3.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.textBrowser_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textBrowser_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.horizontalLayout_29.addWidget(self.textBrowser_3)


        self.verticalLayout_24.addWidget(self.frame_37)


        self.horizontalLayout_26.addWidget(self.frame_34)


        self.horizontalLayout_30.addWidget(self.frame_33)

        self.stackedWidget.addWidget(self.write)
        self.kPressRelease = QWidget()
        self.kPressRelease.setObjectName(u"kPressRelease")
        self.verticalLayout_26 = QVBoxLayout(self.kPressRelease)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_38 = QFrame(self.kPressRelease)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_39)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_40 = QFrame(self.frame_39)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_16 = QLabel(self.frame_40)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font13)
        self.label_16.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_16.setScaledContents(False)
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_16.setWordWrap(True)

        self.horizontalLayout_32.addWidget(self.label_16, 0, Qt.AlignVCenter)


        self.verticalLayout_25.addWidget(self.frame_40, 0, Qt.AlignTop)

        self.frame_41 = QFrame(self.frame_39)
        self.frame_41.setObjectName(u"frame_41")
        sizePolicy.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy)
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_17 = QLabel(self.frame_41)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font14)
        self.label_17.setWordWrap(True)

        self.horizontalLayout_33.addWidget(self.label_17, 0, Qt.AlignTop)


        self.verticalLayout_25.addWidget(self.frame_41, 0, Qt.AlignTop)

        self.frame_42 = QFrame(self.frame_39)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.textBrowser_4 = QTextBrowser(self.frame_42)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.textBrowser_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textBrowser_4.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.horizontalLayout_34.addWidget(self.textBrowser_4)


        self.verticalLayout_25.addWidget(self.frame_42)


        self.horizontalLayout_31.addWidget(self.frame_39)


        self.verticalLayout_26.addWidget(self.frame_38)

        self.stackedWidget.addWidget(self.kPressRelease)
        self.move = QWidget()
        self.move.setObjectName(u"move")
        self.verticalLayout_28 = QVBoxLayout(self.move)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_43 = QFrame(self.move)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:horizontal {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"    background: none;\n"
"    "
                        "\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_44)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_18 = QLabel(self.frame_45)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font13)
        self.label_18.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_18.setScaledContents(False)
        self.label_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_18.setWordWrap(True)

        self.horizontalLayout_36.addWidget(self.label_18, 0, Qt.AlignVCenter)


        self.verticalLayout_27.addWidget(self.frame_45, 0, Qt.AlignTop)

        self.frame_46 = QFrame(self.frame_44)
        self.frame_46.setObjectName(u"frame_46")
        sizePolicy.setHeightForWidth(self.frame_46.sizePolicy().hasHeightForWidth())
        self.frame_46.setSizePolicy(sizePolicy)
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_19 = QLabel(self.frame_46)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font14)
        self.label_19.setWordWrap(True)

        self.horizontalLayout_37.addWidget(self.label_19, 0, Qt.AlignTop)


        self.verticalLayout_27.addWidget(self.frame_46, 0, Qt.AlignTop)

        self.frame_47 = QFrame(self.frame_44)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.textBrowser_5 = QTextBrowser(self.frame_47)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.textBrowser_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textBrowser_5.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.horizontalLayout_38.addWidget(self.textBrowser_5)


        self.verticalLayout_27.addWidget(self.frame_47)


        self.horizontalLayout_35.addWidget(self.frame_44)


        self.verticalLayout_28.addWidget(self.frame_43)

        self.stackedWidget.addWidget(self.move)
        self.Pos = QWidget()
        self.Pos.setObjectName(u"Pos")
        self.verticalLayout_31 = QVBoxLayout(self.Pos)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_49 = QFrame(self.Pos)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.frame_50 = QFrame(self.frame_49)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_50)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_51 = QFrame(self.frame_50)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_20 = QLabel(self.frame_51)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font13)
        self.label_20.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_20.setScaledContents(False)
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_20.setWordWrap(True)

        self.horizontalLayout_41.addWidget(self.label_20, 0, Qt.AlignVCenter)


        self.verticalLayout_30.addWidget(self.frame_51, 0, Qt.AlignTop)

        self.frame_52 = QFrame(self.frame_50)
        self.frame_52.setObjectName(u"frame_52")
        sizePolicy.setHeightForWidth(self.frame_52.sizePolicy().hasHeightForWidth())
        self.frame_52.setSizePolicy(sizePolicy)
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_21 = QLabel(self.frame_52)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font14)
        self.label_21.setWordWrap(True)

        self.horizontalLayout_42.addWidget(self.label_21, 0, Qt.AlignTop)


        self.verticalLayout_30.addWidget(self.frame_52, 0, Qt.AlignTop)

        self.frame_53 = QFrame(self.frame_50)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.textBrowser_6 = QTextBrowser(self.frame_53)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.textBrowser_6.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.textBrowser_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textBrowser_6.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.horizontalLayout_43.addWidget(self.textBrowser_6)


        self.verticalLayout_30.addWidget(self.frame_53)


        self.horizontalLayout_40.addWidget(self.frame_50)


        self.verticalLayout_31.addWidget(self.frame_49)

        self.stackedWidget.addWidget(self.Pos)
        self.click = QWidget()
        self.click.setObjectName(u"click")
        self.verticalLayout_33 = QVBoxLayout(self.click)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_54 = QFrame(self.click)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.frame_55 = QFrame(self.frame_54)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_55)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_56 = QFrame(self.frame_55)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_22 = QLabel(self.frame_56)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font13)
        self.label_22.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_22.setScaledContents(False)
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_22.setWordWrap(True)

        self.horizontalLayout_45.addWidget(self.label_22, 0, Qt.AlignVCenter)


        self.verticalLayout_32.addWidget(self.frame_56, 0, Qt.AlignTop)

        self.frame_57 = QFrame(self.frame_55)
        self.frame_57.setObjectName(u"frame_57")
        sizePolicy.setHeightForWidth(self.frame_57.sizePolicy().hasHeightForWidth())
        self.frame_57.setSizePolicy(sizePolicy)
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_23 = QLabel(self.frame_57)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font14)
        self.label_23.setWordWrap(True)

        self.horizontalLayout_46.addWidget(self.label_23)


        self.verticalLayout_32.addWidget(self.frame_57, 0, Qt.AlignTop)

        self.frame_58 = QFrame(self.frame_55)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.textBrowser_7 = QTextBrowser(self.frame_58)
        self.textBrowser_7.setObjectName(u"textBrowser_7")
        self.textBrowser_7.setFont(font8)
        self.textBrowser_7.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.textBrowser_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textBrowser_7.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.horizontalLayout_47.addWidget(self.textBrowser_7)


        self.verticalLayout_32.addWidget(self.frame_58)


        self.horizontalLayout_44.addWidget(self.frame_55)


        self.verticalLayout_33.addWidget(self.frame_54)

        self.stackedWidget.addWidget(self.click)
        self.mPressRelease = QWidget()
        self.mPressRelease.setObjectName(u"mPressRelease")
        self.verticalLayout_35 = QVBoxLayout(self.mPressRelease)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_59 = QFrame(self.mPressRelease)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.frame_60 = QFrame(self.frame_59)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_60)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_61 = QFrame(self.frame_60)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_24 = QLabel(self.frame_61)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font13)
        self.label_24.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_24.setScaledContents(False)
        self.label_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_24.setWordWrap(True)

        self.horizontalLayout_49.addWidget(self.label_24, 0, Qt.AlignVCenter)


        self.verticalLayout_34.addWidget(self.frame_61, 0, Qt.AlignTop)

        self.frame_62 = QFrame(self.frame_60)
        self.frame_62.setObjectName(u"frame_62")
        sizePolicy.setHeightForWidth(self.frame_62.sizePolicy().hasHeightForWidth())
        self.frame_62.setSizePolicy(sizePolicy)
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_25 = QLabel(self.frame_62)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font14)
        self.label_25.setWordWrap(True)

        self.horizontalLayout_50.addWidget(self.label_25)


        self.verticalLayout_34.addWidget(self.frame_62, 0, Qt.AlignTop)

        self.frame_63 = QFrame(self.frame_60)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.textBrowser_8 = QTextBrowser(self.frame_63)
        self.textBrowser_8.setObjectName(u"textBrowser_8")
        self.textBrowser_8.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.textBrowser_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textBrowser_8.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.horizontalLayout_51.addWidget(self.textBrowser_8)


        self.verticalLayout_34.addWidget(self.frame_63)


        self.horizontalLayout_48.addWidget(self.frame_60)


        self.verticalLayout_35.addWidget(self.frame_59)

        self.stackedWidget.addWidget(self.mPressRelease)
        self.wheel = QWidget()
        self.wheel.setObjectName(u"wheel")
        self.verticalLayout_21 = QVBoxLayout(self.wheel)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_64 = QFrame(self.wheel)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.frame_65 = QFrame(self.frame_64)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_65)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.frame_66 = QFrame(self.frame_65)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_26 = QLabel(self.frame_66)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font13)
        self.label_26.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_26.setScaledContents(False)
        self.label_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_26.setWordWrap(True)

        self.horizontalLayout_54.addWidget(self.label_26, 0, Qt.AlignVCenter)


        self.verticalLayout_36.addWidget(self.frame_66, 0, Qt.AlignTop)

        self.frame_67 = QFrame(self.frame_65)
        self.frame_67.setObjectName(u"frame_67")
        sizePolicy.setHeightForWidth(self.frame_67.sizePolicy().hasHeightForWidth())
        self.frame_67.setSizePolicy(sizePolicy)
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_27 = QLabel(self.frame_67)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font14)
        self.label_27.setWordWrap(True)

        self.horizontalLayout_55.addWidget(self.label_27)


        self.verticalLayout_36.addWidget(self.frame_67, 0, Qt.AlignTop)

        self.frame_68 = QFrame(self.frame_65)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.textBrowser_9 = QTextBrowser(self.frame_68)
        self.textBrowser_9.setObjectName(u"textBrowser_9")
        self.textBrowser_9.setFont(font8)
        self.textBrowser_9.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.textBrowser_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textBrowser_9.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.horizontalLayout_56.addWidget(self.textBrowser_9)


        self.verticalLayout_36.addWidget(self.frame_68)


        self.horizontalLayout_53.addWidget(self.frame_65)


        self.verticalLayout_21.addWidget(self.frame_64)

        self.stackedWidget.addWidget(self.wheel)
        self.wait = QWidget()
        self.wait.setObjectName(u"wait")
        self.verticalLayout_38 = QVBoxLayout(self.wait)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.frame_69 = QFrame(self.wait)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.frame_70 = QFrame(self.frame_69)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_70)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.frame_71 = QFrame(self.frame_70)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_28 = QLabel(self.frame_71)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font13)
        self.label_28.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_28.setScaledContents(False)
        self.label_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_28.setWordWrap(True)

        self.horizontalLayout_58.addWidget(self.label_28, 0, Qt.AlignVCenter)


        self.verticalLayout_37.addWidget(self.frame_71, 0, Qt.AlignTop)

        self.frame_72 = QFrame(self.frame_70)
        self.frame_72.setObjectName(u"frame_72")
        sizePolicy.setHeightForWidth(self.frame_72.sizePolicy().hasHeightForWidth())
        self.frame_72.setSizePolicy(sizePolicy)
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_29 = QLabel(self.frame_72)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font14)
        self.label_29.setWordWrap(True)

        self.horizontalLayout_59.addWidget(self.label_29)


        self.verticalLayout_37.addWidget(self.frame_72, 0, Qt.AlignTop)

        self.frame_73 = QFrame(self.frame_70)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.textBrowser_10 = QTextBrowser(self.frame_73)
        self.textBrowser_10.setObjectName(u"textBrowser_10")
        self.textBrowser_10.setFont(font8)
        self.textBrowser_10.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.textBrowser_10.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textBrowser_10.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.horizontalLayout_60.addWidget(self.textBrowser_10)


        self.verticalLayout_37.addWidget(self.frame_73)


        self.horizontalLayout_57.addWidget(self.frame_70)


        self.verticalLayout_38.addWidget(self.frame_69)

        self.stackedWidget.addWidget(self.wait)
        self.keys = QWidget()
        self.keys.setObjectName(u"keys")
        self.verticalLayout_39 = QVBoxLayout(self.keys)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.frame_76 = QFrame(self.keys)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setStyleSheet(u"QPushButton{\n"
"border:3px solid rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontr"
                        "ol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_76)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.frame_74 = QFrame(self.frame_76)
        self.frame_74.setObjectName(u"frame_74")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_74.sizePolicy().hasHeightForWidth())
        self.frame_74.setSizePolicy(sizePolicy3)
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_74)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_79 = QFrame(self.frame_74)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_79)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_30 = QLabel(self.frame_79)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font13)
        self.label_30.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_30.setScaledContents(False)
        self.label_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_30.setWordWrap(True)

        self.verticalLayout_43.addWidget(self.label_30)


        self.verticalLayout_41.addWidget(self.frame_79)

        self.frame_77 = QFrame(self.frame_74)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_77)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_3 = QLabel(self.frame_77)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font6)

        self.verticalLayout_42.addWidget(self.label_3)


        self.verticalLayout_41.addWidget(self.frame_77)

        self.frame_78 = QFrame(self.frame_74)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_78)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.textBrowser_11 = QTextBrowser(self.frame_78)
        self.textBrowser_11.setObjectName(u"textBrowser_11")

        self.verticalLayout_44.addWidget(self.textBrowser_11)


        self.verticalLayout_41.addWidget(self.frame_78)


        self.verticalLayout_40.addWidget(self.frame_74)

        self.frame_75 = QFrame(self.frame_76)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.frame_80 = QFrame(self.frame_75)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_80)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.testLable = QLabel(self.frame_80)
        self.testLable.setObjectName(u"testLable")
        self.testLable.setFont(font7)
        self.testLable.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_62.addWidget(self.testLable, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_61.addWidget(self.frame_80)

        self.frame_81 = QFrame(self.frame_75)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_81)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.testButton = QPushButton(self.frame_81)
        self.testButton.setObjectName(u"testButton")
        self.testButton.setFont(font6)
        self.testButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon27 = QIcon()
        icon27.addFile(u":/icons/icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.testButton.setIcon(icon27)

        self.verticalLayout_45.addWidget(self.testButton)


        self.horizontalLayout_61.addWidget(self.frame_81)


        self.verticalLayout_40.addWidget(self.frame_75, 0, Qt.AlignBottom)


        self.verticalLayout_39.addWidget(self.frame_76)

        self.stackedWidget.addWidget(self.keys)
        self.fileName = QWidget()
        self.fileName.setObjectName(u"fileName")
        self.horizontalLayout_71 = QHBoxLayout(self.fileName)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.frame_86 = QFrame(self.fileName)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.frame_87 = QFrame(self.frame_86)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_87)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.frame_88 = QFrame(self.frame_87)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_88)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_31 = QLabel(self.frame_88)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font13)
        self.label_31.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_31.setScaledContents(False)
        self.label_31.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_31.setWordWrap(True)

        self.horizontalLayout_68.addWidget(self.label_31, 0, Qt.AlignVCenter)


        self.verticalLayout_50.addWidget(self.frame_88, 0, Qt.AlignTop)

        self.frame_90 = QFrame(self.frame_87)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_90)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.textBrowser_12 = QTextBrowser(self.frame_90)
        self.textBrowser_12.setObjectName(u"textBrowser_12")
        self.textBrowser_12.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.textBrowser_12.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textBrowser_12.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.horizontalLayout_70.addWidget(self.textBrowser_12)


        self.verticalLayout_50.addWidget(self.frame_90)


        self.horizontalLayout_67.addWidget(self.frame_87)


        self.horizontalLayout_71.addWidget(self.frame_86)

        self.stackedWidget.addWidget(self.fileName)
        self.nonUsedSymbols = QWidget()
        self.nonUsedSymbols.setObjectName(u"nonUsedSymbols")
        self.verticalLayout_11 = QVBoxLayout(self.nonUsedSymbols)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_89 = QFrame(self.nonUsedSymbols)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_89)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.frame_91 = QFrame(self.frame_89)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_91)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.frame_92 = QFrame(self.frame_91)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_32 = QLabel(self.frame_92)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font13)
        self.label_32.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_32.setScaledContents(False)
        self.label_32.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_32.setWordWrap(True)

        self.horizontalLayout_72.addWidget(self.label_32, 0, Qt.AlignVCenter)


        self.verticalLayout_51.addWidget(self.frame_92, 0, Qt.AlignTop)

        self.frame_93 = QFrame(self.frame_91)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_93)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.textBrowser_13 = QTextBrowser(self.frame_93)
        self.textBrowser_13.setObjectName(u"textBrowser_13")
        self.textBrowser_13.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.textBrowser_13.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textBrowser_13.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.horizontalLayout_73.addWidget(self.textBrowser_13)


        self.verticalLayout_51.addWidget(self.frame_93)


        self.horizontalLayout_69.addWidget(self.frame_91)


        self.verticalLayout_11.addWidget(self.frame_89)

        self.stackedWidget.addWidget(self.nonUsedSymbols)
        self.OverLap = QWidget()
        self.OverLap.setObjectName(u"OverLap")
        self.verticalLayout_73 = QVBoxLayout(self.OverLap)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.frame_112 = QFrame(self.OverLap)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_99 = QHBoxLayout(self.frame_112)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.frame_129 = QFrame(self.frame_112)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setFrameShape(QFrame.StyledPanel)
        self.frame_129.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_129)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.frame_130 = QFrame(self.frame_129)
        self.frame_130.setObjectName(u"frame_130")
        self.frame_130.setFrameShape(QFrame.StyledPanel)
        self.frame_130.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_100 = QHBoxLayout(self.frame_130)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.label_42 = QLabel(self.frame_130)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font13)
        self.label_42.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_42.setScaledContents(False)
        self.label_42.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_42.setWordWrap(True)

        self.horizontalLayout_100.addWidget(self.label_42, 0, Qt.AlignVCenter)


        self.verticalLayout_72.addWidget(self.frame_130, 0, Qt.AlignTop)

        self.frame_131 = QFrame(self.frame_129)
        self.frame_131.setObjectName(u"frame_131")
        self.frame_131.setFrameShape(QFrame.StyledPanel)
        self.frame_131.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_101 = QHBoxLayout(self.frame_131)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.textBrowser_17 = QTextBrowser(self.frame_131)
        self.textBrowser_17.setObjectName(u"textBrowser_17")
        self.textBrowser_17.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.textBrowser_17.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textBrowser_17.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.horizontalLayout_101.addWidget(self.textBrowser_17)


        self.verticalLayout_72.addWidget(self.frame_131)


        self.horizontalLayout_99.addWidget(self.frame_129)


        self.verticalLayout_73.addWidget(self.frame_112)

        self.stackedWidget.addWidget(self.OverLap)
        self.oneRepeatIssue = QWidget()
        self.oneRepeatIssue.setObjectName(u"oneRepeatIssue")
        self.horizontalLayout_77 = QHBoxLayout(self.oneRepeatIssue)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.frame_94 = QFrame(self.oneRepeatIssue)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_94)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.frame_95 = QFrame(self.frame_94)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_95)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.frame_96 = QFrame(self.frame_95)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_96)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_33 = QLabel(self.frame_96)
        self.label_33.setObjectName(u"label_33")
        font15 = QFont()
        font15.setFamily(u"Bahnschrift")
        font15.setPointSize(20)
        font15.setBold(False)
        font15.setWeight(50)
        self.label_33.setFont(font15)
        self.label_33.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_33.setScaledContents(False)
        self.label_33.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_33.setWordWrap(True)

        self.horizontalLayout_75.addWidget(self.label_33, 0, Qt.AlignVCenter)


        self.verticalLayout_52.addWidget(self.frame_96, 0, Qt.AlignTop)

        self.frame_97 = QFrame(self.frame_95)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_97)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.textBrowser_14 = QTextBrowser(self.frame_97)
        self.textBrowser_14.setObjectName(u"textBrowser_14")
        self.textBrowser_14.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;\n"
"}")
        self.textBrowser_14.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textBrowser_14.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.horizontalLayout_76.addWidget(self.textBrowser_14)


        self.verticalLayout_52.addWidget(self.frame_97)


        self.horizontalLayout_74.addWidget(self.frame_95)


        self.horizontalLayout_77.addWidget(self.frame_94)

        self.stackedWidget.addWidget(self.oneRepeatIssue)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.horizontalLayout_87 = QHBoxLayout(self.settingsPage)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.frame_109 = QFrame(self.settingsPage)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_109)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.frame_110 = QFrame(self.frame_109)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_110)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.PanicButBut = QPushButton(self.frame_110)
        self.PanicButBut.setObjectName(u"PanicButBut")
        self.PanicButBut.setFont(font6)
        self.PanicButBut.setCursor(QCursor(Qt.PointingHandCursor))
        self.PanicButBut.setStyleSheet(u"QPushButton{\n"
"border:3px solid rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}")
        icon28 = QIcon()
        icon28.addFile(u":/icons/icons/alert-triangle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.PanicButBut.setIcon(icon28)

        self.verticalLayout_61.addWidget(self.PanicButBut)

        self.DMSBUT = QPushButton(self.frame_110)
        self.DMSBUT.setObjectName(u"DMSBUT")
        self.DMSBUT.setFont(font6)
        self.DMSBUT.setCursor(QCursor(Qt.PointingHandCursor))
        self.DMSBUT.setStyleSheet(u"QPushButton{\n"
"border:3px solid rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}")
        self.DMSBUT.setIcon(icon27)

        self.verticalLayout_61.addWidget(self.DMSBUT)

        self.DeprecationBut = QPushButton(self.frame_110)
        self.DeprecationBut.setObjectName(u"DeprecationBut")
        self.DeprecationBut.setFont(font6)
        self.DeprecationBut.setCursor(QCursor(Qt.PointingHandCursor))
        self.DeprecationBut.setStyleSheet(u"QPushButton{\n"
"border:3px solid rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}")
        icon29 = QIcon()
        icon29.addFile(u":/icons/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.DeprecationBut.setIcon(icon29)

        self.verticalLayout_61.addWidget(self.DeprecationBut)

        self.verticalSpacer = QSpacerItem(20, 452, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_61.addItem(self.verticalSpacer)


        self.horizontalLayout_88.addWidget(self.frame_110)

        self.frame_111 = QFrame(self.frame_109)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_111)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.stackedWidget_2 = QStackedWidget(self.frame_111)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.settingsTitle = QWidget()
        self.settingsTitle.setObjectName(u"settingsTitle")
        self.verticalLayout_63 = QVBoxLayout(self.settingsTitle)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.frame_115 = QFrame(self.settingsTitle)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setStyleSheet(u"border: 3px solid rgb(230,5,64);\n"
"border-radius: 3px")
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_115)
        self.horizontalLayout_90.setSpacing(0)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.frame_116 = QFrame(self.frame_115)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setStyleSheet(u"border: none")
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_116)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.frame_116)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(200, 200))
        self.label_34.setPixmap(QPixmap(u":/icons/icons/TryToSave.png"))
        self.label_34.setScaledContents(True)
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout_65.addWidget(self.label_34)

        self.label_35 = QLabel(self.frame_116)
        self.label_35.setObjectName(u"label_35")
        font16 = QFont()
        font16.setFamily(u"Bahnschrift SemiBold SemiConden")
        font16.setPointSize(36)
        font16.setBold(True)
        font16.setWeight(75)
        self.label_35.setFont(font16)
        self.label_35.setStyleSheet(u"")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_65.addWidget(self.label_35)


        self.horizontalLayout_90.addWidget(self.frame_116, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_63.addWidget(self.frame_115)

        self.stackedWidget_2.addWidget(self.settingsTitle)
        self.panicButtpnSettings = QWidget()
        self.panicButtpnSettings.setObjectName(u"panicButtpnSettings")
        self.panicButtpnSettings.setStyleSheet(u"border: 3px solid rgb(230,5,64);\n"
"border-radius: 3px")
        self.verticalLayout_64 = QVBoxLayout(self.panicButtpnSettings)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.frame_114 = QFrame(self.panicButtpnSettings)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setStyleSheet(u"border:none;\n"
"QPushButton{\n"
"border:3px solid rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;"
                        "\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_114)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.frame_113 = QFrame(self.frame_114)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_113)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.label_36 = QLabel(self.frame_113)
        self.label_36.setObjectName(u"label_36")
        font17 = QFont()
        font17.setFamily(u"Bahnschrift")
        font17.setPointSize(20)
        self.label_36.setFont(font17)
        self.label_36.setStyleSheet(u"color:rgb(230,5,64);")

        self.horizontalLayout_93.addWidget(self.label_36)


        self.verticalLayout_66.addWidget(self.frame_113)

        self.frame_117 = QFrame(self.frame_114)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setStyleSheet(u"QPushButton{\n"
"border:3px solid rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontr"
                        "ol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.frame_117.setFrameShape(QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.frame_117)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.textBrowser_15 = QTextBrowser(self.frame_117)
        self.textBrowser_15.setObjectName(u"textBrowser_15")

        self.horizontalLayout_92.addWidget(self.textBrowser_15)


        self.verticalLayout_66.addWidget(self.frame_117)

        self.frame_118 = QFrame(self.frame_114)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setFrameShape(QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_118)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_91.addItem(self.horizontalSpacer_4)

        self.frame_119 = QFrame(self.frame_118)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setMaximumSize(QSize(500, 16777215))
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_119)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.label_37 = QLabel(self.frame_119)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font6)
        self.label_37.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.label_37)

        self.PanicbutLineEdit = QLineEdit(self.frame_119)
        self.PanicbutLineEdit.setObjectName(u"PanicbutLineEdit")
        self.PanicbutLineEdit.setFont(font6)
        self.PanicbutLineEdit.setStyleSheet(u"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"text-align: left;")
        self.PanicbutLineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.PanicbutLineEdit)


        self.horizontalLayout_91.addWidget(self.frame_119)

        self.frame_120 = QFrame(self.frame_118)
        self.frame_120.setObjectName(u"frame_120")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_120.sizePolicy().hasHeightForWidth())
        self.frame_120.setSizePolicy(sizePolicy4)
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_120)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.PanicButAccept = QPushButton(self.frame_120)
        self.PanicButAccept.setObjectName(u"PanicButAccept")
        self.PanicButAccept.setFont(font6)
        self.PanicButAccept.setCursor(QCursor(Qt.PointingHandCursor))
        self.PanicButAccept.setStyleSheet(u"QPushButton{\n"
"border:3px solid rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}")
        self.PanicButAccept.setIcon(icon23)

        self.horizontalLayout_94.addWidget(self.PanicButAccept)

        self.frame_121 = QFrame(self.frame_120)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setFrameShape(QFrame.StyledPanel)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_121)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.label_38 = QLabel(self.frame_121)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font6)
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_68.addWidget(self.label_38)

        self.currentPanicButton = QLabel(self.frame_121)
        self.currentPanicButton.setObjectName(u"currentPanicButton")
        self.currentPanicButton.setFont(font6)
        self.currentPanicButton.setStyleSheet(u"color: rgb(230,5,64);")
        self.currentPanicButton.setAlignment(Qt.AlignCenter)

        self.verticalLayout_68.addWidget(self.currentPanicButton)


        self.horizontalLayout_94.addWidget(self.frame_121)


        self.horizontalLayout_91.addWidget(self.frame_120, 0, Qt.AlignLeft)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_91.addItem(self.horizontalSpacer_3)


        self.verticalLayout_66.addWidget(self.frame_118)


        self.verticalLayout_64.addWidget(self.frame_114)

        self.stackedWidget_2.addWidget(self.panicButtpnSettings)
        self.DMSsettings = QWidget()
        self.DMSsettings.setObjectName(u"DMSsettings")
        self.DMSsettings.setStyleSheet(u"border: 3px solid rgb(230,5,64);\n"
"border-radius: 3px")
        self.horizontalLayout_89 = QHBoxLayout(self.DMSsettings)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.frame_122 = QFrame(self.DMSsettings)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setStyleSheet(u"border:none;\n"
"QPushButton{\n"
"border:3px solid rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;"
                        "\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_122)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.frame_123 = QFrame(self.frame_122)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setFrameShape(QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.frame_123)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.label_39 = QLabel(self.frame_123)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font17)
        self.label_39.setStyleSheet(u"color:rgb(230,5,64);")

        self.horizontalLayout_95.addWidget(self.label_39)


        self.verticalLayout_69.addWidget(self.frame_123)

        self.frame_124 = QFrame(self.frame_122)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setStyleSheet(u"QPushButton{\n"
"border:3px solid rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: #e60540;\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #e60540;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontr"
                        "ol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.frame_124.setFrameShape(QFrame.StyledPanel)
        self.frame_124.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.frame_124)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.textBrowser_16 = QTextBrowser(self.frame_124)
        self.textBrowser_16.setObjectName(u"textBrowser_16")

        self.horizontalLayout_96.addWidget(self.textBrowser_16)


        self.verticalLayout_69.addWidget(self.frame_124)

        self.frame_125 = QFrame(self.frame_122)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setFrameShape(QFrame.StyledPanel)
        self.frame_125.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.frame_125)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer)

        self.frame_126 = QFrame(self.frame_125)
        self.frame_126.setObjectName(u"frame_126")
        self.frame_126.setMaximumSize(QSize(500, 16777215))
        self.frame_126.setFrameShape(QFrame.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_126)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.label_40 = QLabel(self.frame_126)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font6)
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_70.addWidget(self.label_40)

        self.DMSeditLable = QLineEdit(self.frame_126)
        self.DMSeditLable.setObjectName(u"DMSeditLable")
        self.DMSeditLable.setFont(font6)
        self.DMSeditLable.setStyleSheet(u"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"text-align: left;")
        self.DMSeditLable.setAlignment(Qt.AlignCenter)

        self.verticalLayout_70.addWidget(self.DMSeditLable)


        self.horizontalLayout_97.addWidget(self.frame_126)

        self.frame_127 = QFrame(self.frame_125)
        self.frame_127.setObjectName(u"frame_127")
        sizePolicy4.setHeightForWidth(self.frame_127.sizePolicy().hasHeightForWidth())
        self.frame_127.setSizePolicy(sizePolicy4)
        self.frame_127.setFrameShape(QFrame.StyledPanel)
        self.frame_127.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.frame_127)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.DMSaccept = QPushButton(self.frame_127)
        self.DMSaccept.setObjectName(u"DMSaccept")
        self.DMSaccept.setFont(font6)
        self.DMSaccept.setCursor(QCursor(Qt.PointingHandCursor))
        self.DMSaccept.setStyleSheet(u"QPushButton{\n"
"border:3px solid rgb(24,24,36);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"border: 3px solid rgb(230,5,64);\n"
"border-radius: 7px;\n"
"bacground-color: rgb(17,16,26);\n"
"\n"
"}")
        self.DMSaccept.setIcon(icon23)

        self.horizontalLayout_98.addWidget(self.DMSaccept)

        self.frame_128 = QFrame(self.frame_127)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setFrameShape(QFrame.StyledPanel)
        self.frame_128.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_128)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.label_41 = QLabel(self.frame_128)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font6)
        self.label_41.setAlignment(Qt.AlignCenter)

        self.verticalLayout_71.addWidget(self.label_41)

        self.currentDMS = QLabel(self.frame_128)
        self.currentDMS.setObjectName(u"currentDMS")
        self.currentDMS.setFont(font6)
        self.currentDMS.setStyleSheet(u"color: rgb(230,5,64);")
        self.currentDMS.setAlignment(Qt.AlignCenter)

        self.verticalLayout_71.addWidget(self.currentDMS)


        self.horizontalLayout_98.addWidget(self.frame_128)


        self.horizontalLayout_97.addWidget(self.frame_127, 0, Qt.AlignLeft)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_2)


        self.verticalLayout_69.addWidget(self.frame_125)


        self.horizontalLayout_89.addWidget(self.frame_122)

        self.stackedWidget_2.addWidget(self.DMSsettings)

        self.verticalLayout_62.addWidget(self.stackedWidget_2)


        self.horizontalLayout_88.addWidget(self.frame_111)


        self.horizontalLayout_87.addWidget(self.frame_109)

        self.stackedWidget.addWidget(self.settingsPage)

        self.verticalLayout_12.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.maincontet)

        self.footer = QFrame(self.mainbody)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.footer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.footer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        font18 = QFont()
        font18.setFamily(u"Bahnschrift")
        font18.setPointSize(10)
        self.label.setFont(font18)

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignBottom)


        self.horizontalLayout_4.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.footer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.WhereIsBut = QPushButton(self.frame_7)
        self.WhereIsBut.setObjectName(u"WhereIsBut")
        self.WhereIsBut.setCursor(QCursor(Qt.PointingHandCursor))
        self.WhereIsBut.setStyleSheet(u"outline: none;\n"
"border: none;\n"
"")
        icon30 = QIcon()
        icon30.addFile(u":/icons/icons/box.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.WhereIsBut.setIcon(icon30)

        self.verticalLayout_3.addWidget(self.WhereIsBut)


        self.horizontalLayout_4.addWidget(self.frame_7)

        self.size_grip = QFrame(self.footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.size_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout_64.addWidget(self.mainbody)


        self.horizontalLayout.addWidget(self.mainframe)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(2)
        self.toolBox_2.setCurrentIndex(1)
        self.toolBox_3.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Overriding hand v1.0", None))
        self.createScript.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 Overscript", None))
        self.existingScriptsBut.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0442\u043e\u0432\u044b\u0435 Overscripts", None))
        self.editScriptButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c Overscript", None))
        self.introBut.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0435\u043d\u0438\u0435", None))
        self.structureBut.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430 OverScript", None))
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"send()", None))
        self.writeButton.setText(QCoreApplication.translate("MainWindow", u"write()", None))
        self.kPRButton.setText(QCoreApplication.translate("MainWindow", u"kpress()+krelease()", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.keyboard), QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0430\u0432\u0438\u0430\u0442\u0443\u0440\u0430", None))
        self.moveButton.setText(QCoreApplication.translate("MainWindow", u"move()", None))
        self.PosButton.setText(QCoreApplication.translate("MainWindow", u"Pos()", None))
        self.clickButton.setText(QCoreApplication.translate("MainWindow", u"click() + dclick()", None))
        self.mPressButton.setText(QCoreApplication.translate("MainWindow", u"mpress()+mrelease()", None))
        self.wheelButton.setText(QCoreApplication.translate("MainWindow", u"wheel()", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.mouse), QCoreApplication.translate("MainWindow", u"\u041c\u044b\u0448\u044c", None))
        self.waitButton.setText(QCoreApplication.translate("MainWindow", u"wait()", None))
        self.keysButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043b\u0430\u0432\u0438\u0448", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.Overscript), QCoreApplication.translate("MainWindow", u"Overscript", None))
        self.fileNameBut.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.NonUsedSymbolsBut.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u043c\u044b\u0435 \u0441\u0438\u043c\u0432\u043e\u043b\u044b", None))
        self.OverLapBut.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0441\u0435\u0447\u0435\u043d\u0438\u0435 HK \u0438 KS", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.Appendix), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.doc), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u044f", None))
        self.oneRepeatIssueButton.setText(QCoreApplication.translate("MainWindow", u" \"Repeat mode\" \u041f\u043e\u0432\u0442\u043e\u0440\u044f\u0435\u0442\u0441\u044f \n"
" \u043b\u0438\u0448\u044c \u0435\u0434\u0438\u043d\u043e\u0436\u0434\u044b", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0448\u0435\u043d\u0438\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c", None))
        self.settingsBut.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.gitHubBut.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_13), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043d\u043e\u0435", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.open_close_side_bar_btn.setText("")
        self.quickUse.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0411\u044b\u0441\u0442\u0440\u044b\u0439 \u0437\u0430\u043f\u0443\u0441\u043a...", None))
        self.quickUseButton.setText("")
        self.pushButton_5.setText("")
        self.pushButton_4.setText("")
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.label_6.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"OVERRIDING HAND", None))
        self.codeRewriteEditor.setDocumentTitle("")
        self.codeRewriteEditor.setPlainText("")
        self.codeRewriteEditor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u043d\u0430\u0447\u0438\u043d\u0430\u0435\u0442\u0441\u044f \u0433\u0434\u0435-\u0442\u043e \u0442\u0443\u0442...", None))
        self.backToEx.setText(QCoreApplication.translate("MainWindow", u"\u041a \u0433\u043e\u0442\u043e\u0432\u044b\u043c", None))
        self.ChooseFileBut.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.editFileLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435...", None))
        self.RewriteBut.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0437\u0430\u043f\u0438\u0441\u0430\u0442\u044c", None))
        self.ChosenFileLableIsOpen.setText("")
        self.ChosenFileLableSEMEN.setText("")
        self.codeEditor.setDocumentTitle("")
        self.codeEditor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0448 \u043a\u043e\u0434 \u043d\u0430\u0447\u0438\u043d\u0430\u0435\u0442\u0441\u044f \u0437\u0434\u0435\u0441\u044c...", None))
        self.posButton.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b", None))
        self.posLable.setText("")
        self.posHelpButton.setText("")
        self.nameLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435...", None))
        self.createButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0442\u043e\u0432\u044b\u0435 \u043a \u0440\u0430\u0431\u043e\u0442\u0435", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0435", None))
        self.exMacroName.setText(QCoreApplication.translate("MainWindow", u"Hack", None))
        self.exMacroRun.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.exMacroChange.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.exMacroDelete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.workMacroName.setText(QCoreApplication.translate("MainWindow", u"Hack", None))
        self.workMacroTerminate.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0435\u043d\u0438\u0435, \u0438\u043b\u0438 \u0447\u0442\u043e \u0442\u0430\u043a\u043e\u0435 Overriding hand", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Overriding hand \u2013 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430, \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u044e\u0449\u0430\u044f \u0441\u043e\u0437\u0434\u0430\u0432\u0430\u0442\u044c \u043c\u0430\u043a\u0440\u043e\u0441\u044b \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044f \u043a\u0430\u0441\u0442\u043e\u043c\u043d\u044b\u0439 \u044f\u0437\u044b\u043a \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \"OverScript\"", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">Overriding hand</span><span style=\" font-family:'Bahnschrift','sans-serif';\">\u201d \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0435\u0442 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0440\u0435\u043f\u0435\u0442\u0430\u0442\u0438\u0432\u043d\u044b\u0435 \u0432\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u0441"
                        " \u041f\u041a. \u0411\u0443\u0434\u044c \u0442\u043e \u0440\u0430\u0431\u043e\u0442\u0430 \u0441 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u044b\u043c\u0438 \u0442\u0430\u0431\u043b\u0438\u0446\u0430\u043c\u0438 \u0438\u043b\u0438 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u0432 \u0432\u0438\u0434\u0435\u043e\u0438\u0433\u0440\u0430\u0445.</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">OverScript</span><span style=\" font-family:'Bahnschrift','sans-serif';\">\u201d \u2013 \u044d\u0442\u043e \u0432\u044b\u0441\u043e\u043a\u043e\u0443\u0440\u043e\u0432\u043d\u0435\u0432\u044b\u0439, \u043d\u043e \u043f\u0440\u0438\u043c\u0438\u0442\u0438\u0432\u043d\u044b\u0439 \u044f\u0437\u044b\u043a \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e"
                        "\u0432\u0430\u043d\u0438\u044f, \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u043c\u044b\u0439 \u0438\u0441\u043a\u043b\u044e\u0447\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u0434\u043b\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u043c\u0430\u043a\u0440\u043e\u0441\u043e\u0432 \u0432 \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">Overriding hand</span><span style=\" font-family:'Bahnschrift','sans-serif';\">\u201d. \u0415\u0433\u043e \u043f\u0440\u0438\u043c\u0438\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c \u0441\u043e\u0437\u0434\u0430\u0435\u0442 \u043d\u0438\u0437\u043a\u0438\u0439 \u043f\u043e\u0440\u043e\u0433 \u0432\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f, \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u044f \u043e\u0441\u0432\u043e\u0438\u0442\u044c \u0435\u0433\u043e \u043b\u044e\u0431\u043e\u043c\u0443 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044e.</span> </p>\n"
"<p style=\" margin-top:12"
                        "px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u041f\u043e\u043b\u043d\u0430\u044f \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u044f \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">OverScript</span><span style=\" font-family:'Bahnschrift','sans-serif';\">\u201d \u0441 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435\u043c \u043a \u043d\u0435\u0439 \u043e\u043f\u0438\u0441\u0430\u043d\u0430 \u043d\u0438\u0436\u0435.</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439  </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">OverScript</span><span style=\" font-fami"
                        "ly:'Bahnschrift','sans-serif';\"> \u043c\u043e\u0436\u043d\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044f \u043f\u0435\u0440\u0432\u0443\u044e  \u043a\u043d\u043e\u043f\u043a\u0443 \u0432 \u043c\u0435\u043d\u044e \u0441\u043b\u0435\u0432\u0430 (&quot;\u0421\u043e\u0437\u0434\u0430\u0442\u044c </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">OverScript</span><span style=\" font-family:'Bahnschrift','sans-serif';\">&quot;. \u041f\u043e\u043c\u0438\u043c\u043e \u0440\u0435\u0434\u0430\u043a\u0442\u043e\u0440\u0430 \u043a\u043e\u0434\u0430, \u0432 \u043d\u0435\u0439 \u0435\u0441\u0442\u044c \u0444\u0443\u043d\u043a\u0446\u0438\u044f \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442 \u043a\u0443\u0440\u0441\u043e\u0440\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 \u043d\u0430 \u0441\u043e\u043e\u0442\u0432\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0443\u044e \u043a"
                        "\u043d\u043e\u043f\u043a\u0443. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u041f\u0440\u0438 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u0438 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">OverScript </span><span style=\" font-family:'Bahnschrift','sans-serif';\">\u0432\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u0437\u0430\u0433\u043b\u044f\u043d\u0443\u0442\u044c \u0432 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u044e \u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u043a \u043d\u0430\u043f\u0438\u0441\u0430\u043d\u0438\u044e \u043a\u043e\u0434\u0430 \u0431\u0435\u0437 \u043f\u043e\u0442\u0435\u0440\u0438 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0430.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-ind"
                        "ent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u0414\u043b\u044f \u0437\u0430\u043f\u0443\u0441\u043a\u0430 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0435\u0433\u043e \u043c\u0430\u043a\u0440\u043e\u0441\u0430 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u043c\u0435\u043d\u044e &quot;\u0413\u043e\u0442\u043e\u0432\u044b\u0435 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">OverScripts</span><span style=\" font-family:'Bahnschrift','sans-serif';\">&quot; \u0438\u043b\u0438 \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0435\u0433\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432 \u043f\u043e\u0438\u0441\u043a\u043e\u0432\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0435 \u0432\u044b\u0448\u0435 (\u0432 \u043d\u0435\u0439 \u043d\u0430\u043f\u0438\u0441\u0430\u043d\u043e \u201c\u0411\u044b\u0441\u0442\u0440\u044b\u0439 \u0437\u0430\u043f\u0443\u0441\u043a\u2026\u201d) \u0438 \u043d"
                        "\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u043b\u0443\u043f\u0443.</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u0412 \u043c\u0435\u043d\u044e &quot;\u0413\u043e\u0442\u043e\u0432\u044b\u0435 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">OverScripts</span><span style=\" font-family:'Bahnschrift','sans-serif';\">&quot; \u043d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f \u043f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u0432\u0441\u0435\u0445 \u0433\u043e\u0442\u043e\u0432\u044b\u0445 \u043a \u0440\u0430\u0431\u043e\u0442\u0435 \u0438 \u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0445 \u043c\u0430\u043a\u0440\u043e\u0441\u043e\u0432. \u0418\u0437 \u044d\u0442\u043e\u0433\u043e \u043c\u0435\u043d\u044e \u043c\u043e\u0436\u043d\u043e \u043e\u0442\u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432"
                        "\u0430\u0442\u044c, \u0437\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0438\u043b\u0438 \u0443\u0434\u0430\u043b\u0438\u0442\u044c \u043b\u044e\u0431\u043e\u0439 \u0438\u0437 \u043c\u0430\u043a\u0440\u043e\u0441\u043e\u0432 \u0430 \u0442\u0430\u043a \u0436\u0435 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0440\u0430\u0431\u043e\u0442\u0443 \u043b\u044e\u0431\u043e\u0433\u043e \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0433\u043e \u043c\u0430\u043a\u0440\u043e\u0441\u0430.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u0412 \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">Overriding hand</span><span style=\" font-family:'Bahnschrift','sans-serif';\">\u201d \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0442 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weig"
                        "ht:600; color:#e60540;\">Panic button</span><span style=\" font-family:'Bahnschrift','sans-serif';\"> \u0438 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">Dead man's switch</span><span style=\" font-family:'Bahnschrift','sans-serif';\">, \u0437\u0430\u0433\u043b\u044f\u043d\u0438\u0442\u0435 \u0432 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0447\u0442\u043e\u0431\u044b \u043f\u0440\u043e\u0447\u0438\u0442\u0430\u0442\u044c \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0438 \u043f\u0435\u0440\u0435\u043d\u0430\u0437\u043d\u0430\u0447\u0438\u0442\u044c \u0438\u0445 \u043a\u043b\u0430\u0432\u0438\u0448\u0438.</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430 OverScript", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u0431\u043e \u0433\u043e\u0432\u043e\u0440\u044f, \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u043a\u043e\u0434\u0430 \u0432 OverScript \u043c\u043e\u0436\u043d\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u044c \u043d\u0430 \u0442\u0440\u0438 \u0447\u0430\u0441\u0442\u0438: \u0414\u0438\u0440\u0435\u043a\u0442\u0438\u0432\u044b, \u0440\u0435\u0436\u0438\u043c \u0440\u0430\u0431\u043e\u0442\u044b \u0438 \u043a\u043e\u043c\u0430\u043d\u0434\u044b. ", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0412\u0441\u0435\u0433\u043e \u0434\u0438\u0440\u0435\u043a\u0442\u0438\u0432 4:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">HK</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> (HotKey) \u2013 \u0443\u043a\u0430\u0437"
                        "\u044b\u0432\u0430\u0435\u0442 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443, \u043f\u0440\u0438 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043c\u0430\u043a\u0440\u043e\u0441 \u0430\u043a\u0442\u0438\u0432\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u0438\u043b\u0438 \u043f\u0435\u0440\u0435\u043a\u043b\u044e\u0447\u0438\u0442\u0441\u044f \u0432 \u0441\u043b\u0443\u0447\u0430\u0435 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u201cToggleMode\u201d</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">. \u041c\u043e\u0436\u043d\u043e \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u044e \u043a\u043b\u0430\u0432\u0438\u0448 \u0447\u0435\u0440\u0435\u0437 \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">+</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d"
                        "</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">KS</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> (KillSwitch) \u2013 \u0423\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443, \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u043c\u0430\u043a\u0440\u043e\u0441 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442 \u0441\u0432\u043e\u044e \u0440\u0430\u0431\u043e\u0442\u0443 \u0438 \u0432\u044b\u0433\u0440\u0443\u0437\u0438\u0442 \u0441\u0435\u0431\u044f \u0438\u0437 \u043f\u0430\u043c\u044f\u0442\u0438. \u041c\u043e\u0436\u043d\u043e \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u043a\u043e\u043c\u0431\u0438\u043d\u0430"
                        "\u0446\u0438\u044e \u043a\u043b\u0430\u0432\u0438\u0448 \u0447\u0435\u0440\u0435\u0437 \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">+</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Delay</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u2013 \u0417\u0430\u0434\u0435\u0440\u0436\u043a\u0430 \u043c\u0435\u0436\u0434\u0443 \u043a\u0430\u0436\u0434\u043e\u0439 \u0438\u0442\u0435\u0440\u0430\u0446\u0438\u0435\u0439 \u0432 \u0440\u0435\u0436\u0438\u043c\u0435 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u201cToggleMode\u201d</span"
                        "><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">. \u0423\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445, \u043c\u043e\u0436\u0435\u0442 \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0442\u044c \u0434\u0440\u043e\u0431\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435. </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; text-decoration: underline;\">\u041d\u0410\u0421\u0422\u041e\u042f\u041b\u042c\u041d\u041e</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u0442\u0441\u044f \u043d\u0435 \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u0435\u043d\u044c\u0448\u0435 \u201c0.2\u201d. \u0414\u0440\u043e\u0431\u043d\u044b\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0442\u0441"
                        "\u044f \u0447\u0435\u0440\u0435\u0437 \u0442\u043e\u0447\u043a\u0443.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Repeats</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u2013 \u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u0439 \u0432 \u0440\u0435\u0436\u0438\u043c\u0435 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u201cRepeatMode\u201d</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">. \u041f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u0422\u041e\u041b\u042c\u041a\u041e \u0446\u0435\u043b\u044b\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f.</span><span style=\" f"
                        "ont-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0418\u0437 \u043d\u0438\u0445 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u043e\u0431\u044a\u044f\u0432\u043b\u044f\u0442\u044c \u043b\u0438\u0448\u044c \u0434\u0432\u0435: </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">KS</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0438 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">HK</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">, \u0442.\u043a. </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u201cDelay\u201d</span><span style=\" font-family:'Bahnschrift','sans-s"
                        "erif'; font-size:11pt;\"> \u0438 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u201cRepeats\u201d</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0438\u043c\u0435\u044e\u0442 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e: 1.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0414\u043b\u044f \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u044f \u0434\u0438\u0440\u0435\u043a\u0442\u0438\u0432\u044b, \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0435\u0451 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0438 \u0447\u0435\u0440\u0435\u0437 \u043e\u0440\u0434\u0438\u043d\u0430\u0440\u043d\u044b\u0439 \u043f\u0440\u043e\u0431\u0435\u043b \u0443\u043a\u0430\u0436\u0438\u0442\u0435 \u0435\u0451"
                        " \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435, \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">HK</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> t </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Delay</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> 1 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">KS</span><span style=\""
                        " font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> t+p</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0412\u0441\u0435\u0433\u043e \u0440\u0435\u0436\u0438\u043c\u043e\u0432 \u0440\u0430\u0431\u043e\u0442\u044b 3:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">PressMode</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u2013"
                        " \u041e\u0434\u043d\u043e\u043a\u0440\u0430\u0442\u043d\u043e\u0435 \u0432\u043e\u0441\u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u0435 \u043c\u0430\u043a\u0440\u043e\u0441\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u043e\u0439 \u043a </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u201cHK\u201d</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">RepeatMode</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> - \u041c\u043d\u043e\u0433\u043e\u043a\u0440\u0430\u0442\u043d\u043e\u0435 \u0432\u043e\u0441\u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434"
                        "\u0435\u043d\u0438\u0435 \u043c\u0430\u043a\u0440\u043e\u0441\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u043e\u0439 \u043a </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u201cHK\u201d</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">, \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u0432\u0442\u043e\u0440\u043e\u0432 \u0437\u0430\u0432\u0438\u0441\u0438\u0442 \u043e\u0442 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u201cRepeats\u201d</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> (\u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e 1)</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style"
                        "=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">ToggleMode</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u2013 \u0411\u0435\u0441\u043a\u043e\u043d\u0435\u0447\u043d\u043e\u0435 \u0432\u043e\u0441\u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u0435 \u043c\u0430\u043a\u0440\u043e\u0441\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u043e\u0439 \u043a </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u201cHK\u201d</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">, \u0434\u043e \u0442\u043e\u0433\u043e \u043a\u0430\u043a </span><span style=\" font-family:'Bahnschrift','sans-se"
                        "rif'; font-size:11pt; font-weight:600; color:#e60540;\">\u201cHK\u201d</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043d\u0435 \u0431\u0443\u0434\u0435\u0442 \u043d\u0430\u0436\u0430\u0442 \u0432\u043d\u043e\u0432\u044c. \u041f\u043e\u0432\u0442\u043e\u0440\u043d\u043e\u0435 \u043d\u0430\u0436\u0430\u0442\u0438\u0435 \u043d\u0430 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u201cHK\u201d</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0441\u043d\u043e\u0432\u0430 \u0437\u0430\u043f\u0443\u0441\u0442\u0438\u0442 \u043c\u0430\u043a\u0440\u043e\u0441. \u0417\u0430\u0434\u0435\u0440\u0436\u043a\u0430 \u043c\u0435\u0436\u0434\u0443 \u043a\u0430\u0436\u0434\u044b\u043c \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u0435\u043c \u0437\u0430\u0432\u0438\u0441\u0438\u0442 \u043e\u0442 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:6"
                        "00; color:#e60540;\">Delay</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> (\u041f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e 1)</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0420\u0435\u0436\u0438\u043c \u0440\u0430\u0431\u043e\u0442\u044b \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0435\u0434\u0438\u043d\u043e\u0436\u0434\u044b, \u043e\u043d \u0440\u0430\u0441\u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u044f\u0435\u0442\u0441\u044f \u043d\u0430 \u0440\u0430\u0431\u043e\u0442\u0443 \u0432\u0441\u0435\u0433\u043e \u043c\u0430\u043a\u0440\u043e\u0441\u0430.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrif"
                        "t','sans-serif'; font-size:11pt;\"><br />\u0420\u0435\u0436\u0438\u043c \u0440\u0430\u0431\u043e\u0442\u044b, \u043a\u0430\u043a \u0438 \u0434\u0438\u0440\u0435\u043a\u0442\u0438\u0432\u044b </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u201cHK\u201d</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0438 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u201cKS\u201d</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">, </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">\u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0432 \u043a\u043e\u0434\u0435</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; "
                        "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041a\u043e\u043c\u0430\u043d\u0434\u044b \u2013 \u044d\u0442\u043e \u201c\u0441\u0435\u0440\u0434\u0446\u0435\u201d \u043c\u0430\u043a\u0440\u043e\u0441\u0430. \u042d\u0442\u043e \u0443\u043a\u0430\u0437\u0430\u043d\u0438\u044f, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043c\u0430\u043a\u0440\u043e\u0441 \u0431\u0443\u0434\u0435\u0442 \u0432\u044b\u043f\u043e\u043b\u043d\u044f\u0442\u044c. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u201csend\u201d</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043d\u0430\u0436\u043c\u0435\u0442 \u043d\u0430 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u0443\u044e \u043a\u043b\u0430\u0432\u0438\u0448\u0443 \u0438\u043b\u0438 \u043a\u043e\u043c\u0431\u0438\u043d"
                        "\u0430\u0446\u0438\u044e \u043a\u043b\u0430\u0432\u0438\u0448. \u0412\u0441\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u044b \u043e\u043f\u0438\u0441\u0430\u043d\u044b \u0432 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u0438.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041f\u0440\u0438\u043c\u0435\u0440 \u043a\u043e\u0434\u0430:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">	</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">HK t</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; ma"
                        "rgin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS shift+t</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	PressMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	send(\u201ca\u201d)</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-fam"
                        "ily:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041a\u043e\u043c\u043f\u0438\u043b\u044f\u0442\u043e\u0440 \u201cOverScript\u201d \u043d\u0435\u043f\u0440\u0438\u0432\u0435\u0440\u0435\u0434\u043b\u0438\u0432 \u043a \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0435. \u041e\u043f\u0438\u0441\u044b\u0432\u0430\u0442\u044c \u0434\u0438\u0440\u0435\u043a\u0442\u0438\u0432\u044b, \u0440\u0435\u0436\u0438\u043c \u0440\u0430\u0431\u043e\u0442\u044b \u0438 \u043a\u043e\u043c\u0430\u043d\u0434\u044b \u043c\u043e\u0436\u043d\u043e \u0432 \u043b\u044e\u0431\u043e\u043c \u043f\u043e\u0440\u044f\u0434\u043a\u0435:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">	</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">send(\u201ca\u201d)</span><span style=\" font-size:11pt;"
                        " font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS shift+t</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	PressMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	HK t</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-blo"
                        "ck-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041e\u0434\u043d\u0430\u043a\u043e, \u043a\u043e\u043c\u043f\u0438\u043b\u044f\u0442\u043e\u0440 \u201cOverScript\u201d \u0447\u0443\u0432\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u0435\u043d \u043a \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0443. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u201csend\u201d</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0434\u043b\u044f \u043d\u0435\u0433\u043e \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u043a\u043e\u043c\u0430\u043d\u0434\u043d\u043e\u0439, \u0430"
                        " </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; text-decoration: underline;\">\u201cSend\u201d</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u2013 \u0443\u0436\u0435 \u0447\u0435\u043c-\u0442\u043e \u043d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b\u043c, \u043f\u043e\u044d\u0442\u043e\u043c\u0443 \u043a\u043e\u043c\u043f\u0438\u043b\u044f\u0442\u043e\u0440 \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e \u043f\u0440\u043e\u0438\u0433\u043d\u043e\u0440\u0438\u0440\u0443\u0435\u0442 \u044d\u0442\u0443 \u0441\u0442\u0440\u043e\u043a\u0443, \u0438 \u0441\u043a\u043e\u043c\u043f\u0438\u043b\u0438\u0440\u0443\u0435\u0442 \u043c\u0430\u043a\u0440\u043e\u0441 \u0431\u0435\u0437 \u043d\u0435\u0451.</span><span style=\" font-size:11pt;\"> </span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"send(\"{key}\")", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u043e\u0434\u0438\u043d \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442:\n"
"{key} - \u0441\u0438\u043c\u0432\u043e\u043b \u0438\u043b\u0438 \u0441\u0442\u0440\u043e\u043a\u0430", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">send()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043d\u0430\u0436\u0438\u043c\u0430\u0435\u0442 \u0438 \u043c\u0433\u043d\u043e\u0432\u0435\u043d\u043d\u043e \u043e\u0442\u043f\u0443\u0441\u043a\u0430\u0435\u0442 \u043a\u043b\u0430\u0432\u0438\u0448\u0443 \u0438\u043b\u0438 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u044e \u043a\u043b\u0430\u0432\u0438\u0448. </span></p>\n"
"<p style=\" margin-top:"
                        "12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0410\u0440\u0433\u0443\u043c\u0435\u043d\u0442 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">{key}</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u0441\u0438\u043c\u0432\u043e\u043b\u044c\u043d\u043e\u0435</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043b\u0438\u0431\u043e </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u0441\u0442\u0440\u043e\u0447\u043d\u043e\u0435</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0437\u043d\u0430\u0447\u0435\u043d"
                        "\u0438\u0435, \u043f\u0440\u0438 \u0435\u0433\u043e \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0438 \u043e\u043d \u0434\u043e\u043b\u0436\u0435\u043d \u0431\u044b\u0442\u044c \u0437\u0430\u043a\u043b\u044e\u0447\u0435\u043d \u0432 \u0434\u0432\u043e\u0439\u043d\u044b\u0435 \u043a\u0430\u0432\u044b\u0447\u043a\u0438 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u201c\u201d</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041f\u0440\u0438 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0438</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; color:#e60540;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\""
                        ">\u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u0438 \u043a\u043b\u0430\u0432\u0438\u0448</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">, \u0440\u0430\u0437\u0434\u0435\u043b\u044f\u0439\u0442\u0435 \u0438\u0445 \u043f\u0440\u0438 \u043f\u043e\u043c\u043e\u0449\u0438  </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; color:#ffffff;\">&quot;</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">+</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; color:#ffffff;\">&quot;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041f\u0440\u0438\u043c\u0435\u0440 \u043a\u043e\u0434\u0430:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; ma"
                        "rgin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">	</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">HK t</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS escape</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	ToggleMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inden"
                        "t:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	send(\u201ca\u201d)\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ffaaff;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff63b4;\">#\u041d\u0430\u0436\u043c\u0435\u0442 \u043d\u0430 a \u0438 \u043c\u0433\u043d\u043e\u0432\u0435\u043d\u043d\u043e \u043e\u0442\u043f\u0443\u0441\u0442\u0438\u0442 \u0430</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041f\u0440\u0438\u043c\u0435\u0440 \u043a\u043e\u0434\u0430 \u0441 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u0435\u0439 \u043a\u043b\u0430\u0432\u0438\u0448:</span"
                        "><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	HK t</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS escape</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	ToggleMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-ri"
                        "ght:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	send(\u201ca+f\u201d)\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff63b4;\">#\u0417\u0430\u0436\u043c\u0435\u0442 \u0430, \u0437\u0430\u0442\u0435\u043c f, \u043f\u043e\u0442\u043e\u043c \u043e\u0442\u043f\u0443\u0441\u0442\u0438\u0442 \u043e\u0431\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0438 \u043e\u0434\u043d\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0410\u0440\u0433\u0443\u043c\u0435\u043d\u0442</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600;\">"
                        " </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">{key}</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u0441\u0442\u0440\u043e\u0447\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043b\u0438\u0448\u044c \u0432 \u0442\u043e\u043c \u0441\u043b\u0443\u0447\u0430\u0435, \u0435\u0441\u043b\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043a\u043b\u0430\u0432\u0438\u0448\u0438:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-fa"
                        "mily:'Bahnschrift','sans-serif'; font-size:11pt;\">	</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">HK t</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS escape</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	ToggleMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11p"
                        "t; font-style:italic;\">	send(\u201cescape\u201d)\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff63b4;\">#\u041d\u0430\u0436\u043c\u0435\u0442 \u043d\u0430 escape \u0437\u0430\u0442\u0435\u043c \u043c\u0433\u043d\u043e\u0432\u0435\u043d\u043d\u043e \u043e\u0442\u043f\u0443\u0441\u0442\u0438\u0442 escape</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041f\u0440\u0438\u043c\u0435\u0440 \u0441 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u0435\u0439:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahns"
                        "chrift','sans-serif'; font-size:11pt; font-style:italic;\">	HK t</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS escape</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	ToggleMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	send(\u201calt+f4\u201d)\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0"
                        "\u00a0\u00a0\u00a0\u00a0\u00a0</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff63b4;\"> #\u0417\u0430\u0436\u043c\u0451\u0442 alt, \u0437\u0430\u0442\u0435\u043c f4, \u043f\u043e\u0442\u043e\u043c \u043e\u0442\u043f\u0443\u0441\u0442\u0438\u0442 \u043e\u0431\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0438 \u043e\u0434\u043d\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e</span><span style=\" font-size:11pt; font-style:italic; color:#ff63b4;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u043a\u043b\u0430\u0432\u0438\u0448</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0435\u0441\u0442\u044c \u0432 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u0438"
                        " \u043d\u0438\u0436\u0435.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">send()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043d\u0435\u043b\u044c\u0437\u044f \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0434\u043b\u044f \u043d\u0430\u043f\u0438\u0441\u0430\u043d\u0438\u044f \u0441\u0442\u0440\u043e\u043a:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	HK t</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-lef"
                        "t:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS escape</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	ToggleMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	send(\u201cHello World!\u201d)\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff63b4;\">#\u0421\u043a\u0440\u0438\u043f\u0442 \u043d\u0435 \u0441\u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442</span><s"
                        "pan style=\" font-size:11pt; font-style:italic; color:#ff63b4;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0414\u043b\u044f \u043d\u0430\u043f\u0438\u0441\u0430\u043d\u0438\u044f \u0441\u0442\u0440\u043e\u043a \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">write()</span><span style=\" font-size:11pt; font-weight:600; color:#e60540;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0410\u0440\u0433\u0443\u043c\u0435\u043d\u0442 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">{key}</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0431\u0435\u0440\u0451\u0442</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; color:#e60540;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">keycode</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0437\u0430\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0432 \u043d\u0435\u0433\u043e \u0441\u0438\u043c\u0432\u043e\u043b\u0430, \u0430 \u043d\u0435 \u0441\u0430\u043c \u0441\u0438\u043c\u0432\u043e\u043b. \u0422\u043e \u0435\u0441\u0442\u044c:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:"
                        "12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">	</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">HK t</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS escape</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	ToggleMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-b"
                        "lock-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	send(\u201cz\u201d)\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff63b4;\">\u00a0\u00a0 #\u0415\u0441\u043b\u0438 \u0430\u043a\u0442\u0438\u0432\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0441\u043a\u0440\u0438\u043f\u0442 \u0441 \u0440\u0443\u0441\u0441\u043a\u043e\u0439 \u0440\u0430\u0441\u043a\u043b\u0430\u0434\u043a\u043e\u0439 \u2013 \u0431\u0443\u0434\u0435\u0442 \u043d\u0430\u043f\u0435\u0447\u0430\u0442\u0430\u043d\u043e \u201c\u044f&quot;, \u0435\u0441\u043b\u0438 \u043f\u0440\u0438 \u044d\u0442\u043e\u043c \u0435\u0449\u0451 \u0438 \u0430\u043a\u0442\u0438\u0432\u0435\u043d Caps Lock - \u0431\u0443\u0434\u0435\u0442 \u043d\u0430\u043f\u0435\u0447\u0430\u0442\u0430\u043d\u043e &quot;\u042f&quot;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">send()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; color:#e60540;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0447\u0443\u0432\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u0435\u043d \u043a \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0443:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	HK t</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:it"
                        "alic;\">	KS escape</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	ToggleMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	send(\u201cZ\u201d)\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff63b4;\">#\u041d\u0430\u043f\u0435\u0447\u0430\u0442\u0430\u0435\u0442 \u0432 \u0432\u0435\u0440\u0445\u043d\u0435\u043c \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0435</span><span style=\" font-size:11pt; font-style:italic; color:#ff63b4;"
                        "\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	send(\u201cz\u201d)\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff63b4;\"> #\u041d\u0430\u043f\u0435\u0447\u0430\u0442\u0430\u0435\u0442 \u0432 \u043d\u0438\u0436\u043d\u0435\u043c \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0435</span><span style=\" font-size:11pt; font-style:italic; color:#ff63b4;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0412 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u044f\u0445 \u043c\u043e\u0436\u0435\u0442 \u0443\u0447\u0443\u0432\u0441\u0442\u0432\u043e\u0432\u0430\u0442"
                        "\u044c \u0434\u043e </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">15</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043a\u043b\u0430\u0432\u0438\u0448:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">	</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">HK t</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS escape</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bot"
                        "tom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	ToggleMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	send(\u201cq+w+e+r+t+alt+up+windows+p+y+[+m+v+c\u201d)</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438, \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f \u0432 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0435 \u043a\u043b\u0430\u0432"
                        "\u0438\u0448 \u043d\u0435\u0442, \u043d\u043e \u0443 \u0440\u0430\u0437\u043d\u044b\u0445 \u043e\u0441\u0435\u0439 \u0440\u0430\u0437\u043d\u044b\u0435 \u043f\u0440\u0435\u0434\u0435\u043b\u044b, \u0438 \u0438\u0445 \u043b\u0443\u0447\u0448\u0435 \u043d\u0435 \u0438\u0441\u043f\u044b\u0442\u044b\u0432\u0430\u0442\u044c.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"write(\"{string}\")", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u043e\u0434\u0438\u043d \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442:\n"
"{string} - \u0441\u0438\u043c\u0432\u043e\u043b \u0438\u043b\u0438 \u0441\u0442\u0440\u043e\u043a\u0430", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u041e\u0447\u0435\u043d\u044c \u043f\u043e\u0445\u043e\u0436 \u043d\u0430 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">send()</span><span style=\" font-family:'Bahnschrift','sans-serif';\">, \u043d\u043e \u0441 \u043f\u0430\u0440\u043e\u0439 \u0441\u0435\u0440\u044c\u0451\u0437\u043d\u044b\u0445 \u043e\u0442\u043b\u0438\u0447\u0438\u0439.</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">write()</span><span style=\" font-family:'Bahnschrift','sans-serif';\"> \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442</span><span style=\" font-family:'Bahnschrift','sans-serif'; color:#e60540;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">{string}</span><span style=\" font-family:'Bahnschrift','sans-serif';\">, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0432\u043e\u0441\u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u0432\u0441\u0451 \u0432\u0432\u0435\u0434\u0451\u043d\u043d\u043e\u0435 \u0432 \u043d\u0435\u0433\u043e \u043a\u0430\u043a \u0441\u0442\u0440\u043e\u043a\u0443, \u0430 \u043d\u0435 \u043d\u0430\u0431\u043e\u0440 \u043a\u043b\u0430\u0432\u0438\u0448. \u0417\u0430 \u0440\u0430\u0437 \u043e\u043d \u043c\u043e\u0436\u0435\u0442 \u043d\u0430\u043f\u0438\u0441\u0430\u0442"
                        "\u044c \u0434\u043e ~6000 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432:</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">	</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">HK alt+t</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	KS escape+shift</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	RepeatMode</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-"
                        "left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	write(\u201cescape+alt\u201d) </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic; color:#ff80ce;\">#</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic; text-decoration: underline; color:#ff80ce;\">\u041d\u0430\u043f\u0438\u0448\u0435\u0442</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic; color:#ff80ce;\"> \u201cescape+alt\u201d, \u0430 \u043d\u0435 \u043d\u0430\u0436\u043c\u0451\u0442 \u044d\u0442\u0443 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u044e \u043a\u043b\u0430\u0432\u0438\u0448.</span><span style=\" font-style:italic; color:#ff80ce;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u0421\u043e\u043e\u0442\u0432\u0435"
                        "\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e, \u043e\u043d \u043d\u0435 \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d \u043a </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">keycode</span><span style=\" font-family:'Bahnschrift','sans-serif';\">\u2019\u0430\u043c \u043a\u043b\u0430\u0432\u0438\u0448:</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	HK alt+t</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	KS escape+shift</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-i"
                        "ndent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	RepeatMode</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	write(\u201cMore dust, more ashes, more disappointment\u201d) </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic; color:#ff80ce;\">#\u041d\u0430\u043f\u0435\u0447\u0430\u0442\u0430\u0435\u0442 \u044d\u0442\u0443 \u0441\u0442\u0440\u043e\u0447\u043a\u0443 \u0432\u043d\u0435 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u043e\u0442 \u0442\u043e\u0433\u043e, \u0432\u043a\u043b\u044e\u0447\u0435\u043d \u043b\u0438 Caps Lock, \u0438\u043b\u0438 \u043a\u0430\u043a\u0430\u044f \u0440\u0430\u0441\u043a\u043b\u0430\u0434\u043a\u0430 \u0441\u0435\u0439\u0447\u0430\u0441 \u0430\u043a\u0442\u0438\u0432\u043d\u0430</spa"
                        "n><span style=\" font-style:italic; color:#ff80ce;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">write()</span><span style=\" font-family:'Bahnschrift','sans-serif';\"> \u043d\u0430\u043f\u0435\u0447\u0430\u0442\u0430\u0435\u0442 \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e \u0438\u0434\u0435\u043d\u0442\u0438\u0447\u043d\u0443\u044e \u0441\u0442\u0440\u043e\u043a\u0443 \u0438\u0437 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">{string}</span><span style=\" font-family:'Bahnschrift','sans-serif';\">, \u0435\u0441\u043b\u0438 \u0441\u0438\u043c\u0432\u043e\u043b\u044b \u0432 \u043d\u0435\u0439 \u0438\u0437 \u044e\u043d\u0438\u043a\u043e\u0434\u0430; \u043e\u0442 \u043f\u0440\u043e\u0431\u0435\u043b\u0430 \u0434\u043e \u201c</span><span style=\" font-family:'Segoe UI Symb"
                        "ol','sans-serif';\">\u2642</span><span style=\" font-family:'Bahnschrift','sans-serif';\">\u201d</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u0412 \u043e\u0441\u0442\u0430\u043b\u044c\u043d\u043e\u043c, </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">write()</span><span style=\" font-family:'Bahnschrift','sans-serif';\"> \u0438\u0434\u0435\u043d\u0442\u0438\u0447\u0435\u043d </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">send()</span><span style=\" font-weight:600; color:#e60540;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif';\">\u00a0</span> </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-b"
                        "ottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435:</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u0415\u0441\u043b\u0438 \u043e\u0431\u043e\u0431\u0449\u0430\u0442\u044c, \u0442\u043e </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">send()</span><span style=\" font-family:'Bahnschrift','sans-serif';\"> \u044d\u0442\u043e </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">\u044d\u043c\u0443\u043b\u044f\u0446\u0438\u044f</span><span style=\" font-family:'Bahnschrift','sans-serif';\"> \u043d\u0430\u0436\u0430\u0442\u0438\u044f \u043d\u0430 \u043a\u043b\u0430\u0432"
                        "\u0438\u0448\u0443, \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u0441\u0438\u0441\u0442\u0435\u043c\u0430 \u0437\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u0443\u0435\u0442 \u0438 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442; </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">write()</span><span style=\" font-family:'Bahnschrift','sans-serif';\"> \u0436\u0435 \u0441\u043b\u043e\u0432\u043d\u043e </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">\u0432\u0441\u0442\u0430\u0432\u043a\u0430</span><span style=\" font-family:'Bahnschrift','sans-serif'; color:#e60540;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">\u0438\u0437</span><span style=\" font-family:'Bahnschrift','sans-serif'; color:#e60540;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">\u0431\u0443\u0444\u0435\u0440\u0430 \u043e\u0431"
                        "\u043c\u0435\u043d\u0430</span><span style=\" font-family:'Bahnschrift','sans-serif';\">, \u0441\u0440\u0430\u0432\u043d\u0438\u043c\u0430\u044f \u0441 \u043d\u0430\u0436\u0430\u0442\u0438\u0435\u043c \u043d\u0430 ctrl+v.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u00a0</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u00a0</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u00a0</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\""
                        ">\u00a0</span> </p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"kpress(\"{key}\")+krelease (\"{key}\")", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u043e\u0434\u0438\u043d \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442:\n"
"{key} - \u0441\u0438\u043c\u0432\u043e\u043b \u0438\u043b\u0438 \u0441\u0442\u0440\u043e\u043a\u0430", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0424\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438, \u044d\u0442\u0438 \u0434\u0432\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u044b - </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">send()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">, \u0440\u0430\u0437\u0431\u0438\u0442\u044b\u0439 \u043d\u0430 \u0434\u0432\u0435 \u0447\u0430\u0441\u0442\u0438.</span><span style=\" font-s"
                        "ize:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">kpress()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043d\u0430\u0436\u0438\u043c\u0430\u0435\u0442 \u0438 \u0443\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442 \u043a\u043b\u0430\u0432\u0438\u0448\u0443 \u043f\u043e\u043a\u0430 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">krelease()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; color:#e60540;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u043d\u0435 \u0431\u0443\u0434\u0435\u0442 \u0432\u044b\u0437\u0432\u0430\u043d \u0441 \u0442\u043e\u0447\u043d\u043e \u0442\u0430\u043a\u043e\u0439 \u0436\u0435 \u043a\u043b\u0430\u0432\u0438\u0448"
                        "\u0435\u0439:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">	</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">HK p+o</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS p+escape</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" mar"
                        "gin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	PressMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	kpress(\u201ca+alt\u201d) \u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff63b4;\"> #\u041d\u0430\u0436\u0438\u043c\u0430\u0435\u0442 \u0438 \u0443\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442 \u044d\u0442\u0443 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u044e \u043a\u043b\u0430\u0432\u0438\u0448</span><span style=\" font-size:11pt; font-style:italic; color:#ff63b4;\"> </span></p>\n"
"<p "
                        "style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	wait(3)</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	krelease(\u201ca+alt\u201d) \u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff63b4;\">#\u0412\u044b\u0441\u0432\u043e\u0431\u043e\u0436\u0434\u0430\u0435\u0442 \u044d\u0442\u0443 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u044e</span><span style=\" font-size:11pt; font-style:italic; color:#ff63b4;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-bl"
                        "ock-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0415\u0441\u043b\u0438 \u0432\u043e \u0432\u0440\u0435\u043c\u044f \u0440\u0430\u0431\u043e\u0442\u044b </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">kpress()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u043d\u0430\u0436\u043c\u0451\u0442 \u043d\u0430</span><span style=\" font-size:11pt;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0443\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u043c\u0443\u044e \u043a\u043b\u0430\u0432\u0438\u0448\u0443"
                        " -</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">kpress()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043f\u0440\u0438\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442 \u0441\u0432\u043e\u044e \u0440\u0430\u0431\u043e\u0442\u0443. \u041a\u043e\u0433\u0434\u0430 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u043e\u0442\u043f\u0443\u0441\u0442\u0438\u0442 \u043d\u0430\u0436\u0430\u0442\u0443\u044e \u043a\u043b\u0430\u0432\u0438\u0448\u0443, </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">kpress()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0432\u044b\u0441\u0432\u043e\u0431\u043e\u0434\u0438\u0442 \u0441\u0435\u0431\u044f \u0438\u0437 \u043a\u043e\u0440\u0442\u0435\u0436\u0430.</spa"
                        "n><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">kpress()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0432\u043e\u0441\u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u0438 \u043a\u043b\u0430\u0432\u0438\u0448 \u043a\u0430\u043a \u0440\u0430\u0437\u0434\u0435\u043b\u044c\u043d\u044b\u0435 \u043f\u043e\u0434\u043f\u0440\u043e\u0446\u0435\u0441\u0441\u044b \u0441\u0430\u043c\u043e\u0433\u043e \u0441\u0435\u0431\u044f. \u0422\u043e \u0435\u0441\u0442\u044c, \u0435\u0441\u043b\u0438 \u0432 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">kpress()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0438"
                        "\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u044f \u043a\u043b\u0430\u0432\u0438\u0448 (\u0434\u043e\u043f\u0443\u0441\u0442\u0438\u043c \u201calt+f4\u201d), \u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u043d\u0430\u0436\u043c\u0451\u0442 \u043d\u0430 \u043e\u0434\u043d\u0443 \u0438\u0437 \u043a\u043b\u0430\u0432\u0438\u0448 (\u0434\u043e\u043f\u0443\u0441\u0442\u0438\u043c \u201calt\u201d), </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">kpress()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; color:#e60540;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u043f\u0435\u0440\u0435\u0441\u0442\u0430\u043d\u0435\u0442 \u0443\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0442\u044c \u0435\u0451 (\u201calt\u201d), \u043d\u043e \u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442"
                        " \u0443\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0442\u044c \u0434\u0440\u0443\u0433\u0438\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0438, \u0443\u0447\u0430\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435 \u0432 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u0438 (\u0432 \u043d\u0430\u0448\u0435\u043c \u0441\u043b\u0443\u0447\u0430\u0435 \u0442\u043e\u043b\u044c\u043a\u043e \u201cf4\u201d)</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0424\u0443\u043d\u043a\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">kpress()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> +</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; color:#"
                        "e60540;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">krelease()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043d\u0435 \u043e\u0442\u043b\u0438\u0447\u0430\u044e\u0442\u0441\u044f \u043e\u0442</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; color:#e60540;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">send()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">, \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e, \u0440\u0430\u0431\u043e\u0442\u0430\u044e\u0442 \u043e\u043d\u0438 \u043f\u043e \u0442\u0430\u043a\u0438\u043c \u0436\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u0430\u043c.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-ind"
                        "ent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"move({x},{y},[mode],[speed])", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u0434\u0432\u0430 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u0438 \u0434\u0432\u0430 \u043d\u0435\u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442\u0430:\n"
"{x} - \u0446\u0435\u043b\u043e\u0447\u0438\u0441\u043b\u0435\u043d\u043d\u043e\u0435/\u0434\u0440\u043e\u0431\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 |&| {y} - \u0446\u0435\u043b\u043e\u0447\u0438\u0441\u043b\u0435\u043d\u043d\u043e\u0435/\u0434\u0440\u043e\u0431\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435\n"
"[mode] - \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 Abs \u043b\u0438\u0431\u043e Add |&| [speed] - \u0446\u0435\u043b\u043e\u0447\u0438\u0441\u043b\u0435\u043d\u043d\u043e\u0435/\u0434\u0440\u043e\u0431\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435  ", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">\u0412\u0441\u0435 \u0434\u0440\u043e\u0431\u043d\u044b\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0437\u0430\u043f\u0438\u0441\u044b\u0432\u0430\u044e\u0442\u0441\u044f \u0447\u0435\u0440\u0435\u0437 \u0442\u043e\u0447\u043a\u0443. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight"
                        ":600; color:#e60540;\">move()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043f\u0435\u0440\u0435\u0434\u0432\u0438\u0433\u0430\u0435\u0442\u043a\u0443\u0440\u0441\u043e\u0440 \u043d\u0430 \u0437\u0430\u0434\u0430\u043d\u043d\u044b\u0435 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">{x}</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; color:#e60540;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0438 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">{y}</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b. </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">{x}</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\""
                        "> \u0438 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">{y}</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043c\u043e\u0433\u0443\u0442 \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0442\u044c \u0434\u0440\u043e\u0431\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435, \u0437\u0430\u043f\u0438\u0441\u0430\u043d\u043d\u043e\u0435 \u0447\u0435\u0440\u0435\u0437 \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">.</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	HK [</span><span style=\" font-size:11pt; font-style:italic;\"> </span"
                        "></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS ]</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	PressMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	move(100, 105.15)\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 \u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font"
                        "-style:italic; color:#ff63b4;\"> #\u041a\u0443\u0440\u0441\u043e\u0440 \u043e\u043a\u0430\u0436\u0435\u0442\u0441\u044f \u043d\u0430 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0430\u0445 {100, 105.15}</span><span style=\" font-size:11pt; font-style:italic; color:#ff63b4;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0410\u0440\u0433\u0443\u043c\u0435\u043d\u0442 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">[mode]</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043f\u043e \u0443"
                        "\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e \u0438\u043c\u0435\u0435\u0442 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u201cAbs\u201d</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">. \u0412 \u0440\u0435\u0436\u0438\u043c\u0435 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Abs</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043a\u0443\u0440\u0441\u043e\u0440 \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u0430\u0431\u0441\u043e\u043b\u044e\u0442\u043d\u044b\u0435 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b, \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0435 \u0432 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">{x}</span><span style=\" fo"
                        "nt-family:'Bahnschrift','sans-serif'; font-size:11pt; color:#e60540;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0438 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">{y}</span><span style=\" font-size:11pt; color:#e60540;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	HK [</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS ]</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	PressMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	move(10, 160, Abs)\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff63b4;\">#\u041a\u0443\u0440\u0441\u043e\u0440 \u043e\u043a\u0430\u0436\u0435\u0442\u0441\u044f \u043d\u0430 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0430\u0445 {10, 160}</span><span style=\" font-size:11pt; font-style:italic; color:#ff63b4;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-inden"
                        "t:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0412 \u0440\u0435\u0436\u0438\u043c\u0435 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Add</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043a \u0442\u0435\u043a\u0443\u0449\u0438\u043c \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0430\u043c \u043a\u0443\u0440\u0441\u043e\u0440\u0430 \u043f\u0440\u0438\u0431\u0430\u0432\u044f\u0442\u0441\u044f \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">{x}</span><span style=\" font-famil"
                        "y:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0438 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">{y}</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">, \u0438 \u043a\u0443\u0440\u0441\u043e\u0440 \u043f\u0435\u0440\u0435\u043c\u0435\u0441\u0442\u0438\u0442\u0441\u044f \u043d\u0430 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0438\u0440\u0443\u044e\u0449\u0438\u0435 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	HK [</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-"
                        "family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS ]</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	PressMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	move(10, 160, Add)\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff80ce;\">#\u041a \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0430\u043c \u043a\u0443\u0440\u0441\u043e\u0440\u0430 \u043f\u0440"
                        "\u0438\u0431\u0430\u0432\u0438\u0442\u044c\u0441\u044f {10, 160}</span><span style=\" font-size:11pt; font-style:italic; color:#ff80ce;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0421\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e, \u0432 \u0440\u0435\u0436\u0438\u043c\u0435 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Add</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043c\u043e\u0436\u043d\u043e \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c </s"
                        "pan><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u043e\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0435</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">	</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">HK [</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS ]</span><span style=\" font-size:11pt; font-"
                        "style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	PressMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	move(10, -160, Add)\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff80ce;\">#\u041a \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0430\u043c \u201cx\u201d \u043a\u0443\u0440\u0441\u043e\u0440\u0430 \u043f\u0440\u0438\u0431\u0430\u0432\u0438\u0442\u0441\u044f 10, \u0430 \u043e\u0442 \u043a\u043e\u043e\u0440\u0434\u0438\u043d"
                        "\u0430\u0442 \u201cy\u201d \u043a\u0443\u0440\u0441\u043e\u0440\u0430 \u043e\u0442\u043d\u0438\u043c\u0435\u0442\u0441\u044f 160 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0410\u0440\u0433\u0443\u043c\u0435\u043d\u0442 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">[speed]</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e \u0438\u043c\u0435\u0435\u0442 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 </span><span style=\" font-f"
                        "amily:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u201c0\u201d</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">. \u042d\u0442\u043e\u0442 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442 \u043e\u0442\u0432\u0435\u0447\u0430\u0435\u0442 \u0437\u0430 \u0442\u043e, \u0441 \u043a\u0430\u043a\u043e\u0439 \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c\u044e \u043a\u0443\u0440\u0441\u043e\u0440 \u043f\u0435\u0440\u0435\u043c\u0435\u0441\u0442\u0438\u0442\u0441\u044f \u043f\u043e \u0437\u0430\u0434\u0430\u043d\u043d\u044b\u043c \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0430\u043c \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	HK [</span><span style=\" font-size"
                        ":11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS ]</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	PressMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	move(10, 160, Abs, 1.5)\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><spa"
                        "n style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff80ce;\">#\u041f\u0435\u0440\u0435\u043c\u0435\u0441\u0442\u0438\u0442 \u043a\u0443\u0440\u0441\u043e\u0440 \u043d\u0430 \u0430\u0431\u0441\u043e\u043b\u044e\u0442\u043d\u044b\u0435 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b {10,160} \u0437\u0430 \u043f\u043e\u043b\u0442\u043e\u0440\u044b \u0441\u0435\u043a\u0443\u043d\u0434\u044b</span><span style=\" font-size:11pt; font-style:italic; color:#ff80ce;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0410\u0440\u0433\u0443\u043c\u0435"
                        "\u043d\u0442\u044b \u0434\u043e\u043b\u0436\u043d\u044b \u043e\u043f\u0438\u0441\u044b\u0432\u0430\u0442\u044c\u0441\u044f \u0432 \u0447\u0451\u0442\u043a\u043e\u0439 \u043f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438:</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; color:#e60540;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">move</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">(</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">{x}</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">,</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">{y}</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">,</span><span style=\" font-family:'Bahnschrift','sans-serif'; fo"
                        "nt-size:11pt; font-weight:600; color:#e60540;\">[mode]</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">,</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">[speed]</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">), \u0432\u043d\u043e\u0441\u0438\u0442\u044c \u043e\u0434\u0438\u043d \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442, \u0438\u0433\u043d\u043e\u0440\u0438\u0440\u0443\u044f \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0438\u0439 \u043d\u0435 \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u0441\u044f:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	HK [</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; marg"
                        "in-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS ]</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	PressMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	move(10, 160, 1) \u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 \u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff80ce;\""
                        ">#\u041d\u0430 \u0442\u0440\u0435\u0442\u044c\u0435\u0439 \u043f\u043e\u0437\u0438\u0446\u0438\u0438 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442\u0430 \u043e\u0436\u0438\u0434\u0430\u0435\u0442\u0441\u044f \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0434\u043b\u044f [mode] \u2013 Abs \u0438\u043b\u0438 Add, \u043d\u043e \u0431\u044b\u043b\u043e \u0434\u0430\u043d\u043e \u0446\u0435\u043b\u043e\u0447\u0438\u0441\u043b\u0435\u043d\u043d\u043e\u0435 \u0434\u043b\u044f [speed] \u2013 \u0441\u043a\u0440\u0438\u043f\u0442 \u043d\u0435 \u0441\u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442.</span><span style=\" font-size:11pt; font-style:italic; color:#ff80ce;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">\u00a0</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin"
                        "-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:1"
                        "2px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Pos({axis})", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u043e\u0434\u0438\u043d \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442: \n"
"{axis} - \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \"x\" \u043b\u0438\u0431\u043e \"y\"", None))
        self.textBrowser_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Pos() </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0444\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u201c\u043f\u044f\u0442\u043e\u0439\u201d \u0434\u0438\u0440\u0435\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u2013 \u043f\u0440\u0438 \u0432\u044b\u0437\u043e\u0432\u0435 \u043e\u043d\u0430 \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u0442 \u0437"
                        "\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442 \u043a\u0443\u0440\u0441\u043e\u0440\u0430 \u043d\u0430 \u043e\u0441\u0438, \u0432\u0432\u0435\u0434\u0435\u043d\u043d\u043e\u0439 \u0432 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">{axis}</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">	</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">HK &lt;</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bah"
                        "nschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS &gt;</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	PressMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	move(Pos(x), Pos(y), Add)\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff80ce;\">#\u041f\u0440\u0438\u0431\u0430\u0432\u0438\u0442 \u043a \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0430\u043c \u043a\u0443"
                        "\u0440\u0441\u043e\u0440\u0430 \u0435\u0433\u043e \u0442\u0435\u043a\u0443\u0449\u0438\u0435 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b</span><span style=\" font-size:11pt; font-style:italic; color:#ff80ce;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0414\u043b\u044f \u0431\u043e\u043b\u044c\u0448\u0435\u0433\u043e \u043f\u043e\u043d\u0438\u043c\u0430\u043d\u0438\u044f \u0440\u0430\u0437\u0431\u0435\u0440\u0451\u043c \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u044b\u0439 \u043f\u0440\u0438\u043c\u0435\u0440. \u0414\u043e\u043f\u0443\u0441\u0442\u0438\u043c \u043a"
                        "\u0443\u0440\u0441\u043e\u0440 \u043d\u0430 \u043c\u043e\u043c\u0435\u043d\u0442 \u0437\u0430\u043f\u0443\u0441\u043a\u0430 \u044d\u0442\u043e\u0433\u043e </span><span style=\" font-size:11pt; font-weight:600; color:#e60540;\">\u2193</span><span style=\" font-family:'Arial','sans-serif'; font-size:11pt;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0441\u043a\u0440\u0438\u043f\u0442\u0430 \u043d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f \u043d\u0430 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0430\u0445 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">{1065, 768}</span><span style=\" font-size:11pt; font-weight:600;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">	</span><span style=\" font-family:'Bahnschrift','sans-serif'; fon"
                        "t-size:11pt; font-style:italic;\">HK &lt;</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS &gt;</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	PressMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	move(Pos(x)+10, Pos(y)+10, Add) </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:1"
                        "2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0414\u043b\u044f </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u043a\u043e\u043c\u043f\u0438\u043b\u044f\u0442\u043e\u0440\u0430</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u044d\u0442\u043e \u0442\u043e\u0436\u0435 \u0441\u0430\u043c\u043e\u0435, \u0447\u0442\u043e \u0438:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">	</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">HK &lt;</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-l"
                        "eft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS &gt;</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	PressMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	move(1065+10, 768+10, Add) </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\""
                        " font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0421 \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u043c\u044b\u043c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435\u043c </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Pos()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043c\u043e\u0436\u043d\u043e \u0441\u0442\u0440\u043e\u0438\u0442\u044c \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0441\u043d\u044b\u0435 \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u044f:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        "><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">	</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">HK &lt;</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS &gt;</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	PressMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','san"
                        "s-serif'; font-size:11pt; font-style:italic;\">	move(((30+5)/(Pos(x)*10))-500+(Pos(y)/2), Pos(y), Add, 1) </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"click(\"[key]\") + dclick(\"[key]\")", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u043e\u0434\u0438\u043d \u043d\u0435\u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442: \n"
"[key] - \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \"left\", \"right\" \u043b\u0438\u0431\u043e \"middle\"", None))
        self.textBrowser_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">click()</span><span style=\" font-family:'Bahnschrift','sans-serif';\"> \u043d\u0430\u0436\u0438\u043c\u0430\u0435\u0442 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 \u043c\u044b\u0448\u0438, \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u0443\u044e \u0432 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">{key}</span><span style=\" font-family:'Bahnschrift','sans-serif';\">. </span><span style=\" font-family:'Bahnschrif"
                        "t','sans-serif'; font-weight:600; color:#e60540;\">dclick()</span><span style=\" font-family:'Bahnschrift','sans-serif';\"> \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u044f\u0435\u0442 \u0434\u0432\u043e\u0439\u043d\u043e\u0435 \u043d\u0430\u0436\u0430\u0442\u0438\u0435 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443, \u043e\u043f\u0438\u0441\u0430\u043d\u043d\u0443\u044e \u0432 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">{key}</span><span style=\" font-family:'Bahnschrift','sans-serif';\">. </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">{key}</span><span style=\" font-family:'Bahnschrift','sans-serif';\"> \u0438\u043c\u0435\u0435\u0442 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e - </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">\u201cleft\u201d</span><span style=\" font-family:'Bahnschrift"
                        "','sans-serif';\">:</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	HK l</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	KS o</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	ToggleMode</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:it"
                        "alic;\">	dclick()\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic; color:#ff80ce;\">#\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442 \u0434\u0432\u043e\u0439\u043d\u043e\u0439 \u043a\u043b\u0438\u043a \u043d\u0430 \u041b\u041a\u041c</span><span style=\" font-style:italic; color:#ff80ce;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u00a0</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u00a0</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-fami"
                        "ly:'Bahnschrift','sans-serif'; font-style:italic;\">	HK l</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	KS o</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	ToggleMode</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	click(\u201cright\u201d)\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; fon"
                        "t-style:italic; color:#ff80ce;\">#\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442 \u043a\u043b\u0438\u043a \u043d\u0430 \u041f\u041a\u041c</span><span style=\" font-style:italic; color:#ff80ce;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u00a0</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u00a0</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u00a0</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u00a0</span> </p></bo"
                        "dy></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"mpress({key}) + mrelease({key})", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u043e\u0434\u0438\u043d \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442: \n"
"{key} - \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \"left\", \"right\" \u043b\u0438\u0431\u043e \"middle\"", None))
        self.textBrowser_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0424\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438, \u044d\u0442\u0438 \u0434\u0432\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u044b - </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">click()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">, \u0440\u0430\u0437\u0431\u0438\u0442\u044b\u0439 \u043d\u0430 \u0434\u0432\u0435 \u0447\u0430\u0441\u0442\u0438.</span><span style=\" font-si"
                        "ze:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">mpress()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043d\u0430\u0436\u0438\u043c\u0430\u0435\u0442 \u0438 \u0443\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043f\u043e\u043a\u0430 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">mrelease()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; color:#e60540;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u043d\u0435 \u0431\u0443\u0434\u0435\u0442 \u0432\u044b\u0437\u0432\u0430\u043d \u0441 \u0442\u043e\u0447\u043d\u043e \u0442\u0430\u043a\u043e\u0439 \u0436\u0435 \u043a\u043d\u043e\u043f\u043a\u043e\u0439"
                        ":</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">	</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">HK c</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS </span><span style=\" font-size:11pt; font-style:italic;\">u</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	PressMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin"
                        "-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	mpress(\u201cleft\u201d) \u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff63b4;\"> #\u041d\u0430\u0436\u0438\u043c\u0430\u0435\u0442 \u0438 \u0443\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442 \u041b\u041a\u041c</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	wait(3)</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	mre"
                        "lease(\u201cleft\u201d) \u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff63b4;\">#\u0412\u044b\u0441\u0432\u043e\u0431\u043e\u0436\u0434\u0430\u0435\u0442 \u041b\u041a\u041c</span><span style=\" font-size:11pt; font-style:italic; color:#ff63b4;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0415\u0441\u043b\u0438 \u0432\u043e \u0432\u0440\u0435\u043c\u044f \u0440\u0430\u0431\u043e\u0442\u044b </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e605"
                        "40;\">mpress()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u043d\u0430\u0436\u043c\u0451\u0442 \u043d\u0430</span><span style=\" font-size:11pt;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0443\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u043c\u0443\u044e \u043a\u043d\u043e\u043f\u043a\u0443 - </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">mpress()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043f\u0440\u0438\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442 \u0441\u0432\u043e\u044e \u0440\u0430\u0431\u043e\u0442\u0443. \u041a\u043e\u0433\u0434\u0430 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u043e\u0442\u043f\u0443\u0441\u0442\u0438\u0442 \u043d\u0430\u0436\u0430\u0442\u0443\u044e \u043a\u043d\u043e\u043f\u043a\u0443, </sp"
                        "an><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">mpress()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0432\u044b\u0441\u0432\u043e\u0431\u043e\u0434\u0438\u0442 \u0441\u0435\u0431\u044f \u0438\u0437 \u043a\u043e\u0440\u0442\u0435\u0436\u0430.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0424\u0443\u043d\u043a\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">mpress()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> +</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; color:#e60540;\"> </span><span style=\" font-family:'Bahnschrift','sans-se"
                        "rif'; font-size:11pt; font-weight:600; color:#e60540;\">mrelease()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043d\u0435 \u043e\u0442\u043b\u0438\u0447\u0430\u044e\u0442\u0441\u044f \u043e\u0442</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; color:#e60540;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">click()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">, \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e, \u0440\u0430\u0431\u043e\u0442\u0430\u044e\u0442 \u043e\u043d\u0438 \u043f\u043e \u0442\u0430\u043a\u0438\u043c \u0436\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u0430\u043c.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; "
                        "font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"wheel([delta])", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u043e\u0434\u0438\u043d \u043d\u0435\u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442: \n"
"[delta] - \u0446\u0435\u043b\u043e\u0447\u0438\u0441\u043b\u0435\u043d\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0432 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u0435 [-3000; 3000]", None))
        self.textBrowser_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">wheel()</span><span style=\" font-family:'Bahnschrift','sans-serif';\"> \u043f\u0440\u043e\u043a\u0440\u0443\u0447\u0438\u0432\u0430\u0435\u0442 \u043a\u043e\u043b\u0435\u0441\u043e \u043c\u044b\u0448\u0438 \u043d\u0430 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u201c\u0449\u0435\u043b\u0447\u043a\u043e\u0432\u201d, \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0445 \u0432 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weigh"
                        "t:600; color:#e60540;\">[delta]</span><span style=\" font-family:'Bahnschrift','sans-serif';\">. \u0417\u043d\u0430\u043a </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">[delta]</span><span style=\" font-family:'Bahnschrift','sans-serif';\"> \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0435\u0442 \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435. </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">[delta]</span><span style=\" font-family:'Bahnschrift','sans-serif';\"> \u0438\u043c\u0435\u0435\u0442 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e: 1:</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	KS i</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p sty"
                        "le=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	HK m</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	PressMode</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	wheel()\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic; color:#ff80ce;\">#\u041e\u0434\u0438\u043d \u201c\u0449\u0435\u043b\u0447\u043e"
                        "\u043a\u201d \u0432\u0432\u0435\u0440\u0445</span><span style=\" font-style:italic; color:#ff80ce;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	wheel(10)\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic; color:#ff80ce;\">#\u0414\u0435\u0441\u044f\u0442\u044c \u201c\u0449\u0435\u043b\u0447\u043a\u043e\u0432\u201d \u0432\u0432\u0435\u0440\u0445</span><span style=\" font-style:italic; color:#ff80ce;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	wheel(-11)\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 \u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0"
                        "\u00a0\u00a0\u00a0</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic; color:#ff80ce;\">\u00a0 #\u041e\u0434\u0438\u043d\u043d\u0430\u0434\u0446\u0430\u0442\u044c \u201c\u0449\u0435\u043b\u0447\u043a\u043e\u0432\u201d \u0432\u043d\u0438\u0437</span><span style=\" font-style:italic; color:#ff80ce;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u00a0</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u00a0</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u00a0</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margi"
                        "n-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u00a0</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif';\">\u00a0</span> </p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"wait({time})", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u043e\u0434\u0438\u043d \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442: \n"
"{time} - \u0446\u0435\u043b\u043e\u0447\u0438\u0441\u043b\u0435\u043d\u043d\u043e\u0435/\u0434\u0440\u043e\u0431\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435.", None))
        self.textBrowser_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">wait() </span><span style=\" font-family:'Bahnschrift','sans-serif';\">\u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e \u043f\u0440\u0438\u043e\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0440\u0430\u0431\u043e\u0442\u0443 \u043c\u0430\u043a\u0440\u043e\u0441\u0430 \u043d\u0430 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\""
                        ">\u0441\u0435\u043a\u0443\u043d\u0434</span><span style=\" font-family:'Bahnschrift','sans-serif';\">, \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u0435 \u0432 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">{time}</span><span style=\" font-family:'Bahnschrift','sans-serif';\">. \u0414\u0440\u043e\u0431\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">{time}</span><span style=\" font-family:'Bahnschrift','sans-serif';\"> \u0437\u0430\u043f\u0438\u0441\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0447\u0435\u0440\u0435\u0437 \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-weight:600; color:#e60540;\">.</span><span style=\" font-family:'Bahnschrift','sans-serif';\">\u201d:</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                        "font-family:'Bahnschrift','sans-serif';\">	</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">KS t</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	HK b</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	PressMode</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	send(\u201cwindows+r\u201d)</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p style=\" mar"
                        "gin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	wait(0.3) \u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic; color:#ff80ce;\">#\u041c\u0430\u043a\u0440\u043e\u0441 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0441\u044f \u043d\u0430 0.3 \u0441\u0435\u043a\u0443\u043d\u0434\u044b</span><span style=\" font-style:italic; color:#ff80ce;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	send(\u201center\u201d)</span><span style=\" font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-i"
                        "ndent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic;\">	wait(1)\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-style:italic; color:#ff80ce;\">#\u041c\u0430\u043a\u0440\u043e\u0441 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0441\u044f \u043d\u0430 1 \u0441\u0435\u043a\u0443\u043d\u0434\u0443</span><span style=\" font-style:italic; color:#ff80ce;\"> </span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0430\u0432\u0438\u0448\u0438", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043d\u0438\u0437\u0443 \u0435\u0441\u0442\u044c \u0444\u0443\u043d\u043a\u0446\u0438\u044f, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u043f\u043e\u043c\u043e\u0436\u0435\u0442 \u0441\u0432\u0435\u0440\u0438\u0442\u044c\u0441\u044f \u0441 \u043a\u043b\u0430\u0432\u0438\u0448\u0430\u043c\u0438", None))
        self.textBrowser_11.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u0441\u0435\u0445 \u043a\u043b\u0430\u0432\u0438\u0448 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0442</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0438\u0445 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f\u043c \u0432 \u043e\u0444\u0438\u0446\u0438"
                        "\u0430\u043b\u044c\u043d\u043e\u0439 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u0438, \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">alt, shift, windows, escape, enter, backspace, f5, page up, end \u0438 \u0442.\u0434.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0422\u0430\u043a \u0436\u0435 \u0440\u0430\u0431\u043e\u0442\u0430\u044e\u0442 \u0438 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u043c\u043e\u0434\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b</"
                        "span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">right alt, left shift, right windows \u0438 \u0442.\u0434.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0412\u043c\u0435\u0441\u0442\u043e \u043f\u0435\u0440\u0435\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u044f \u0432\u0441\u0435\u0445 \u043a\u043b\u0430\u0432\u0438\u0448\u0438 \u043f\u043e \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438, \u0441\u043d\u0438\u0437\u0443 \u0432\u044b \u0441\u043c\u043e\u0436\u0435\u0442\u0435 \u043d\u0430\u0439\u0442\u0438 \u0444"
                        "\u0443\u043d\u043a\u0446\u0438\u044e, \u0447\u0442\u043e \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u0442 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043d\u0430\u0436\u0430\u0442\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438:<br />1. \u041d\u0430\u0436\u0430\u0442\u044c \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 &quot;\u041d\u0430\u0447\u0430\u0442\u044c&quot;, \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043f\u0440\u0438\u0441\u043e\u0442\u0430\u043d\u043e\u0432\u0438\u0442 \u0441\u0432\u043e\u044e \u0440\u0430\u0431\u043e\u0442\u0443 \u0434\u043e \u043c\u043e\u043c\u0435\u043d\u0442\u0430 \u043d\u0430\u0436\u0430\u0442\u0438\u044f \u043d\u0430 \u043a\u043b\u0430\u0432\u0438\u0448\u0443<br />2.\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u043b\u044e\u0431\u0443\u044e \u043a\u043b\u0430\u0432\u0438\u0448\u0443 \u043d\u0430 \u043a\u043b\u0430\u0432\u0438\u0430\u0442\u0443\u0440\u0435<br />3.\u0421\u043b\u0435\u0432\u0430 \u043f\u043e\u044f\u0432\u0438\u0442\u0441"
                        "\u044f \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0438, \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u043c\u043e\u0436\u043d\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0432 \u043a\u043e\u0434\u0435.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p></body></html>", None))
        self.testLable.setText("")
        self.testButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.textBrowser_12.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041f\u0440\u0438 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0438 \u043d\u043e\u0432\u043e\u0433\u043e </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">OverScript</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043c\u043e\u0436\u043d\u043e \u043f\u0440\u0438\u043c\u0435\u043d\u044f\u0442\u044c \u043b\u044e\u0431\u044b\u0435 \u0441\u0438\u043c\u0432\u043e\u043b\u044b \u044e\u043d\u0438"
                        "\u043a\u043e\u0434\u0430 \u043a\u0440\u043e\u043c\u0435 \u0442\u0435\u0445, \u0447\u0442\u043e \u043d\u0435\u0434\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u044b \u0432 \u0444\u0430\u0439\u043b\u043e\u0432\u043e\u0439 \u0441\u0438\u0441\u0442\u0435\u043c\u0435 \u041e\u0421. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440 \u0434\u043b\u044f </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">windows</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">: / \\ : * ? \u00a0\u201c &lt; &gt; |</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041d\u0430\u0437\u044b\u0432\u0430\u044f \u0441\u043a\u0440\u0438\u043f\u0442 \u0443\u0436\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0435\u043c \u0438\u043c\u0435\u043d"
                        "\u0435\u043c,</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\"> Overriding Hand</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043f\u0440\u043e\u0441\u0442\u043e </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">\u043f\u0435\u0440\u0435\u0437\u0430\u043f\u0438\u0448\u0435\u0442</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0444\u0430\u0439\u043b, \u043d\u0435 \u0441\u043e\u0437\u0434\u0430\u0432\u0430\u044f \u043a\u043e\u043f\u0438\u044e.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin"
                        "-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u043c\u044b\u0435 \u0441\u0438\u043c\u0432\u043e\u043b\u044b", None))
        self.textBrowser_13.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041d\u0435\u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0441\u0438\u043c\u0432\u043e\u043b\u044b \u0431\u044b\u043b\u0438 \u0437\u0430\u0440\u0435\u0437\u0435\u0440\u0432\u0438\u0440\u043e\u0432\u0430\u043d\u044b \u0434\u043b\u044f \u043e\u0442\u043b\u0430\u0434\u043a\u0438 \u0438 \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0435\u0433\u043e \u0432\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f </span><span style=\" font-family:'Bahnschrift','s"
                        "ans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Overriding hand</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">. \u0412 \u044d\u0442\u043e\u0442 \u0441\u043f\u0438\u0441\u043e\u043a \u0432\u0445\u043e\u0434\u044f\u0442:<br />&quot;</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">{</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">&quot;   &quot;</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">}</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">&quot;   &quot;</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">[</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">&quot;   &quot;</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">]</span><spa"
                        "n style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">&quot;\u00a0  &quot;</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">*</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">&quot;  &quot;</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">-</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">&quot;</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0422\u0430\u043a \u0436\u0435 \u0432 \u0441\u043f\u0438\u0441\u043e\u043a \u0437\u0430\u0440\u0435\u0437\u0435\u0440\u0432\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432 \u0432\u0445\u043e\u0434\u044f\u0442 \u0433\u043e"
                        "\u0440\u044f\u0447\u0438\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0438 \u0434\u043b\u044f </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Panic button</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> (\u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">home</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d) \u0438 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">DMS</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> (\u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e &quot;</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">end</span><span style=\" font-family:'Bahnschrift','sans-s"
                        "erif'; font-size:11pt;\">&quot;).</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041f\u0440\u0438 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0438 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">KS</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0438\u043b\u0438 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">HK</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; text-decoration: underline;\">\u043d\u0435\u043b\u044c\u0437\u044f</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0438\u0441\u043f\u043e\u043b\u044c\u0437"
                        "\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u0440\u0435\u0437\u0435\u0440\u0432\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0441\u0438\u043c\u0432\u043e\u043b\u044b \u0438\u043b\u0438 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u0438 \u0441 \u0443\u0447\u0430\u0441\u0442\u0438\u0435\u043c \u0437\u0430\u0440\u0435\u0437\u0435\u0440\u0432\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0412 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442\u0430 \u0434\u043b\u044f </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">send()</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> </span><span style"
                        "=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; text-decoration: underline;\">\u043d\u0435\u043b\u044c\u0437\u044f</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u0440\u0435\u0437\u0435\u0440\u0432\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0441\u0438\u043c\u0432\u043e\u043b\u044b, \u043d\u043e \u0438\u0445 \u0443\u0447\u0430\u0441\u0442\u0438\u0435 \u0432 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u0438 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; text-decoration: underline;\">\u0434\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u043e</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> (\u041d\u043e \u0432\u0441\u0451 \u0436\u0435 \u043d\u0435\u0436\u0435\u043b\u0430\u0442\u0435\u043b\u044c\u043d\u043e, \u043e\u0441\u043e\u0431\u0435\u043d\u043d\u043e \u0434\u043b\u044f \u043f\u043e\u043b\u044c\u0437"
                        "\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439 Linux). </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p></body></html>", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0441\u0435\u0447\u0435\u043d\u0438\u0435 HK \u0438 KS", None))
        self.textBrowser_17.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041a\u043e\u0433\u0434\u0430 \u043c\u0430\u043a\u0440\u043e\u0441 \u0432\u044b\u0441\u0432\u043e\u0431\u043e\u0436\u0434\u0430\u0435\u0442 \u0441\u0435\u0431\u044f \u0438\u0437 \u043f\u0430\u043c\u044f\u0442\u0438, \u043e\u043d \u0442\u0430\u043a \u0436\u0435 \u0432\u044b\u0441\u0432\u043e\u0431\u043e\u0436\u0434\u0430\u0435\u0442 \u0432\u0441\u0435 \u0433\u043e\u0440\u044f\u0447\u0438\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0438, \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d"
                        "\u043d\u044b\u0435 \u043a \u043d\u0435\u043c\u0443.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0418\u0437-\u0437\u0430 \u044d\u0442\u043e\u0439 \u043e\u0441\u043e\u0431\u0435\u043d\u043d\u043e\u0441\u0442\u0438 \u043c\u043e\u0433\u0443\u0442 \u0432\u043e\u0437\u043d\u0438\u043a\u043d\u0443\u0442\u044c \u043f\u0435\u0440\u0435\u0441\u0435\u0447\u0435\u043d\u0438\u044f </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">HK</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0438 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">KS</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0443 \u0440\u0430\u0437\u043d\u044b\u0445 \u043c"
                        "\u0430\u043a\u0440\u043e\u0441\u043e\u0432.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0443 \u043d\u0430\u0441 \u0435\u0441\u0442\u044c \u0441\u043a\u0440\u0438\u043f\u0442 \u043f\u043e\u0434 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435\u043c \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; color:#ff80ce;\">Hello</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">	</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size"
                        ":11pt; font-style:italic; color:#ff80ce;\">#Hello</span><span style=\" font-size:11pt; font-style:italic; color:#ff80ce;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	HK t\u00a0\u00a0\u00a0\u00a0 \u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff80ce;\">#\u0422\u0430\u043a\u0430\u044f \u0436\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0430, \u043a\u0430\u043a \u0438 \u0432 KS \u0443 \u201cWorld\u201d</span><span style=\" font-size:11pt; font-style:italic; color:#ff80ce;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS "
                        "i</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	PressMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	send(\u201cescape\u201d)</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0418 \u0442\u0430\u043a \u0436\u0435 \u0441\u043a\u0440\u0438\u043f\u0442 \u201c</span><span style=\" font-family:'Bahnschrift','sans"
                        "-serif'; font-size:11pt; color:#ff80ce;\">World</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">	</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff80ce;\">#World</span><span style=\" font-size:11pt; font-style:italic; color:#ff80ce;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	HK j</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span st"
                        "yle=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS t\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff80ce;\">#\u0422\u0430\u043a\u0430\u044f \u0436\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0430, \u043a\u0430\u043a \u0438 \u0432 HK \u0443 \u201cHello\u201d</span><span style=\" font-size:11pt; font-style:italic; color:#ff80ce;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	PressMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-s"
                        "ize:11pt; font-style:italic;\">	send(\u201center\u201d)</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041f\u0440\u043e\u0431\u043b\u0435\u043c\u0430 \u0432 \u0442\u043e\u043c, \u0447\u0442\u043e \u0435\u0441\u043b\u0438 \u0430\u043a\u0442\u0438\u0432\u0438\u0440\u043e\u0432\u0430\u0442\u044c </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">KillSwitch</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0443 \u201c</span><span style=\" font-fam"
                        "ily:'Bahnschrift','sans-serif'; font-size:11pt; color:#ff80ce;\">World</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d, \u043e\u043d \u0432\u044b\u0441\u0432\u043e\u0431\u043e\u0434\u0438\u0442 \u0432\u0441\u0435 \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0435 \u043a \u043d\u0435\u043c\u0443 \u0433\u043e\u0440\u044f\u0447\u0438\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0438, \u0432\u043a\u043b\u044e\u0447\u0430\u044f </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">HK</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0439 \u043a \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; color:#ff80ce;\">Hello</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d. \u041a\u0430\u043a \u0438\u0442\u043e\u0433 \u2013 \u201c</span><span style=\" fon"
                        "t-family:'Bahnschrift','sans-serif'; font-size:11pt; color:#ff80ce;\">Hello</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d \u0431\u043e\u043b\u044c\u0448\u0435 \u043d\u0435 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u0432\u044b\u0437\u0432\u0430\u043d\u0430, \u0435\u0451 \u043f\u0440\u0438\u0434\u0435\u0442\u0441\u044f \u0432\u044b\u043a\u043b\u044e\u0447\u0430\u0442\u044c \u0438 \u0437\u0430\u043f\u0443\u0441\u043a\u0430\u0442\u044c \u0437\u0430\u043d\u043e\u0432\u043e.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0412\u043e \u0438\u0437\u0431\u0435\u0436\u0430\u043d\u0438\u0435 \u043f\u0435\u0440\u0435\u0441\u0435\u0447\u0435\u043d\u0438\u044f, \u043d\u0430\u0437\u043d\u0430\u0447\u0430\u0439\u0442\u0435 </span><span style=\" font-family:'Bahnschrift'"
                        ",'sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">HK</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0438 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">KS</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043d\u0430 \u0440\u0430\u0437\u043d\u044b\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0438 \u0443 \u043c\u0430\u043a\u0440\u043e\u0441\u043e\u0432, \u0447\u0442\u043e \u0441\u043e\u0431\u0438\u0440\u0430\u0435\u0442\u0435\u0441\u044c \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0432\u043c\u0435\u0441\u0442\u0435.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0441\u043e\u0437\u0434\u0430"
                        "\u0432\u0430\u0439\u0442\u0435 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u0438:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">	</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff80ce;\">#Hello</span><span style=\" font-size:11pt; font-style:italic; color:#ff80ce;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	HK ctrl+t\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 \u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff80ce;\">#\u041f\u0435"
                        "\u0440\u0435\u0441\u0435\u0447\u0435\u043d\u0438\u0435 \u0431\u043e\u043b\u044c\u0448\u0435 \u043d\u0435 \u0432\u043e\u0437\u043d\u0438\u043a\u0430\u0435\u0442</span><span style=\" font-size:11pt; font-style:italic; color:#ff80ce;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS i</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	PressMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; "
                        "font-size:11pt; font-style:italic;\">	send(\u201cescape\u201d)</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0418 \u0432 \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; color:#ff80ce;\">World</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff80ce;\">#World</span><span style=\" font-size:11pt; font-style:italic; color:#ff80ce;\"> </span></p>\n"
""
                        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	HK j</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS t\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic; color:#ff80ce;\"># \u041f\u0435\u0440\u0435\u0441\u0435\u0447\u0435\u043d\u0438\u0435 \u0431\u043e\u043b\u044c\u0448\u0435 \u043d\u0435 \u0432\u043e\u0437\u043d\u0438\u043a\u0430\u0435\u0442</span><span style=\" font-size:11pt; font-style:italic; color:#ff80ce;\"> </span></p>\n"
"<p style=\""
                        " margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	PressMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	send(\u201center\u201d)</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">\u00a0</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                        "<span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u0435\u0435 \u0432\u0441\u0435\u0433\u043e, \"Repeats\" \u0443\u043a\u0430\u0437\u0430\u043d\u0430 \u043d\u0435\u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e", None))
        self.textBrowser_14.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u044d\u0442\u043e\u0442 \u0441\u043a\u0440\u0438\u043f\u0442 \u0432 \u043b\u044e\u0431\u043e\u043c \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u043e\u043c \u0440\u0435\u0434\u0430\u043a\u0442\u043e\u0440\u0435:</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnsc"
                        "hrift','sans-serif'; font-size:11pt;\">	</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">HK t</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	KS p</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	RepeatMode</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:ita"
                        "lic;\">	Repeats 3</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	write(\u201chello world!\u201d)</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	send(\u201center\u201d)</span><span style=\" font-size:11pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-style:italic;\">	wait(0.1)</span><span style=\" font-size:11pt; font-style:italic;\"> </span></"
                        "p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0412\u044b \u0434\u043e\u043b\u0436\u043d\u044b \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0442\u0440\u0438 \u0441\u0442\u0440\u043e\u0447\u043a\u0438 \u0441 \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">hello world!</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d. \u0415\u0441\u043b\u0438 \u044d\u0442\u043e\u0433\u043e \u043d\u0435 \u043f\u0440\u043e\u0438\u0437\u043e\u0448\u043b\u043e, \u043f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u043f\u0435\u0440\u0435\u0441\u043e\u0431\u0440\u0430\u0442\u044c </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Overriding hand</span><span style=\" font-family:'Bahnschrift','sans-se"
                        "rif'; font-size:11pt;\"> \u0438\u0437 \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u0433\u043e \u043a\u043e\u0434\u0430. \u0412 \u0441\u043b\u0443\u0447\u0430\u0435, \u0435\u0441\u043b\u0438 \u0440\u0435\u0434\u0435\u043f\u043b\u043e\u0439 \u043f\u0440\u043e\u0435\u043a\u0442\u0430 \u043d\u0435 \u043f\u043e\u043c\u043e\u0433 \u2013 \u0437\u0430\u0440\u0435\u043f\u043e\u0440\u0442\u0438\u0442\u0435 \u0431\u0430\u0433, \u043f\u0440\u0438\u043b\u043e\u0436\u0438\u0432 \u0441\u043f\u0435\u0446\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044e \u0432\u0430\u0448\u0435\u0433\u043e \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u0430 \u0438 \u041e\u0421. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-bl"
                        "ock-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p></body></html>", None))
        self.PanicButBut.setText(QCoreApplication.translate("MainWindow", u"Panic button", None))
        self.DMSBUT.setText(QCoreApplication.translate("MainWindow", u"DMS", None))
        self.DeprecationBut.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043f\u0440\u0435\u043a\u0430\u0446\u0438\u044f", None))
        self.label_34.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Panic button", None))
        self.textBrowser_15.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Panic button</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u044d\u043a\u0441\u0442\u0440\u0435\u043d\u043d\u043e \u0437\u0430\u0432\u0435\u0440\u0448\u0430\u0435\u0442 \u0432\u0441\u0435 \u0440\u0430\u0431\u043e\u0442\u0430\u044e\u0449\u0438\u0435 \u043c\u0430\u043a\u0440\u043e\u0441\u044b \u0438 \u0432\u044b\u0441\u0432\u043e\u0431\u043e\u0436\u0434\u0430\u0435\u0442 \u0438\u0445 \u0438\u0437 \u043a\u043e\u0440\u0442"
                        "\u0435\u0436\u0430.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041a </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Panic button</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043f\u0440\u0438\u0441\u0432\u0430\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u0437\u0430\u0440\u0435\u0437\u0435\u0440\u0432\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u0430\u044f \u043a\u043b\u0430\u0432\u0438\u0448\u0430, \u0447\u0442\u043e \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u0430 \u043e\u0434\u043d\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e \u0438 \u043a </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">keycode\u2019\u0443</span><span style=\" f"
                        "ont-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043a\u043b\u0430\u0432\u0438\u0448\u0438 \u0438 \u043a</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\"> \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044e</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043a\u043b\u0430\u0432\u0438\u0448\u0438, \u0434\u043b\u044f \u0442\u043e\u0433\u043e \u0447\u0442\u043e \u0431\u044b \u043d\u0430\u0436\u0430\u0442\u0438\u0435 \u043d\u0430 \u043d\u0435\u0451 \u0431\u044b\u043b\u043e \u0437\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043e \u0441\u043a\u0432\u043e\u0437\u044c \u043b\u044e\u0431\u044b\u0435 \u0438\u043d\u044b\u0435 \u0441\u0438\u0433\u043d\u0430\u043b\u044b. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0422"
                        "\u043e \u0435\u0441\u0442\u044c, \u0435\u0441\u043b\u0438 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Panic button</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0431\u044b\u043b \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d \u043a, \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">U</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d, \u0442\u043e \u043d\u0430\u0436\u0430\u0442\u0438\u044f \u043d\u0430 \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#ff80ce;\">\u0413</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d \u043d\u0435 \u0430\u043a\u0442\u0438\u0432\u0438\u0440\u0443\u044e\u0442 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11p"
                        "t; font-weight:600; color:#e60540;\">Panic button</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">. \u0425\u043e\u0442\u044c \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">U</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d \u0438 \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; color:#ff80ce;\">\u0413</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d \u0440\u0430\u0437\u0434\u0435\u043b\u044f\u044e\u0442 \u043e\u0434\u0438\u043d \u0438 \u0442\u043e\u0442 \u0436\u0435 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">keycode</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">, \u0438\u0445 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043d\u0430 \u0440\u0430\u0437\u043d\u044b\u0445 \u0440\u0430\u0441\u043a\u043b"
                        "\u0430\u0434\u043a\u0430\u0445 \u0440\u0430\u0437\u043d\u043e\u0435. \u0421\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e, \u0435\u0441\u043b\u0438 \u043a </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Panic button</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u0430 \u043a\u043b\u0430\u0432\u0438\u0448\u0430 \u043d\u0430 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u043e\u0439 \u0440\u0430\u0441\u043a\u043b\u0430\u0434\u043a\u0435, \u0442\u043e \u0438 \u0430\u043a\u0442\u0438\u0432\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0435\u0451 \u043c\u043e\u0436\u043d\u043e \u043b\u0438\u0448\u044c \u043d\u0430 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u043e\u0439 \u0440\u0430\u0441\u043a\u043b\u0430\u0434\u043a\u0435. \u042d\u0442\u043e \u043d\u0435 \u043a\u0430\u0441\u0430\u0435\u0442\u0441\u044f \u0444\u0443\u043d\u043a\u0446\u0438"
                        "\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0445 \u043a\u043b\u0430\u0432\u0438\u0448, \u0432\u0440\u043e\u0434\u0435 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">shift</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">, </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">scroll lock</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">,</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\"> end</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0438 \u0442\u0430\u043a \u0434\u0430\u043b\u0435\u0435, \u0442.\u043a. \u043d\u0430 \u043b\u044e\u0431\u043e\u0439 \u0440\u0430\u0441\u043a\u043b\u0430\u0434\u043a\u0435 \u043a \u044d\u0442\u0438\u043c </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e"
                        "60540;\">keycode\u2019\u0430\u043c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043e \u043e\u0434\u043d\u043e \u0438 \u0442\u043e \u0436\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u0442\u0441\u044f \u043f\u0440\u0438\u0432\u044f\u0437\u044b\u0432\u0430\u0442\u044c \u043a</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\"> Panic button</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043b\u0430\u0442\u0438\u043d\u0441\u043a\u0438\u0435 \u0441\u0438\u043c\u0432\u043e\u043b\u044b.</span><span style=\" font-size:11pt;\""
                        "> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041a </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Panic button</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; text-decoration: underline;\">\u041d\u0415\u041b\u042c\u0417\u042f</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043f\u0440\u0438\u0432\u044f\u0437\u044b\u0432\u0430\u0442\u044c \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">+</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; ma"
                        "rgin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041a </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Panic button</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; text-decoration: underline;\">\u041d\u0415\u041b\u042c\u0417\u042f</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043f\u0440\u0438\u0432\u044f\u0437\u044b\u0432\u0430\u0442\u044c \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u044e \u043a\u043b\u0430\u0432\u0438\u0448 \u0447\u0435\u0440\u0435\u0437 \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">+</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d.</span></p>\n"
"<p style=\" margin-top:12"
                        "px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0438 \u0434\u043b\u044f </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Panic button </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u043f\u0440\u0438\u0439\u0434\u0443 \u0432 \u0441\u0438\u043b\u0443 \u043b\u0438\u0448\u044c \u043f\u043e\u0441\u043b\u0435 \u043f\u0435\u0440\u0435\u0437\u0430\u043f\u0443\u0441\u043a\u0430.</span><span style=\" font-size:11pt;\"> </span></p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0443/\u0438 \u043d\u0438\u0436\u0435", None))
        self.PanicButAccept.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0435\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435:", None))
        self.currentPanicButton.setText(QCoreApplication.translate("MainWindow", u"scroll lock", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Dead man's switch", None))
        self.textBrowser_16.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Dead man\u2019s switch</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> (</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">DMS</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">), \u0441\u043b\u043e\u0432\u043d\u043e \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540"
                        ";\">BSOD</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d, \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u043c \u043e\u043f\u043b\u043e\u0442\u043e\u043c, \u0447\u0442\u043e \u043d\u0430\u0441\u0438\u043b\u044c\u043d\u043e \u043f\u0440\u0435\u0440\u044b\u0432\u0430\u0435\u0442 \u043f\u0440\u043e\u0446\u0435\u0441\u0441 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Overriding hand</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0438 \u0432\u0441\u0435 \u0441\u043e\u043f\u0440\u044f\u0436\u0435\u043d\u043d\u044b\u0435 \u043f\u043e\u0434\u043f\u0440\u043e\u0446\u0435\u0441\u0441\u044b \u0432\u043e \u0438\u0437\u0431\u0435\u0436\u0430\u043d\u0438\u0435 \u043f\u0435\u0440\u0435\u0433\u0440\u0443\u0437\u0430 \u0441\u0438\u0441\u0442\u0435\u043c\u044b - \u0432\u0441\u0435 \u0447\u0442\u043e \u0441\u0432\u044f\u0437\u0430\u043d\u043e"
                        " \u0441</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\"> Overriding hand</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0431\u0443\u0434\u0435\u0442 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">\u043d\u0430\u0441\u0438\u043b\u044c\u043d\u043e</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0432\u044b\u0441\u0432\u043e\u0431\u043e\u0436\u0434\u0435\u043d\u043e \u0438\u0437 \u043f\u0430\u043c\u044f\u0442\u0438 \u0432\u043d\u0435 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u043e\u0442 \u0442\u0435\u043a\u0443\u0449\u0435\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0438\u043b\u0438 \u0435\u0433\u043e \u043f\u043e\u0434\u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0432.</span></p>\n"
"<p style=\" margin-"
                        "top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041e\u0431\u044b\u0447\u043d\u043e, </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">DMS</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0430\u043a\u0442\u0438\u0432\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u0441\u0430\u043c\u043e\u0441\u0442\u043e\u044f\u0442\u0435\u043b\u044c\u043d\u043e, \u0435\u0441\u043b\u0438 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Overriding hand</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043d\u0430\u0447\u043d\u0435\u0442 \u043f\u043e\u0442\u0440\u0435\u0431\u043b\u044f\u0442\u044c \u0430\u043d\u043e\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0440"
                        "\u0435\u0441\u0443\u0440\u0441\u043e\u0432.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041a </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">DMS</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043f\u0440\u0438\u0441\u0432\u0430\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u0437\u0430\u0440\u0435\u0437\u0435\u0440\u0432\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u0430\u044f \u043a\u043b\u0430\u0432\u0438\u0448\u0430, \u0447\u0442\u043e \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u0430 \u043e\u0434\u043d\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e \u0438 \u043a </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">keycode\u2019\u0443</span><"
                        "span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043a\u043b\u0430\u0432\u0438\u0448\u0438 \u0438 \u043a \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044e \u043a\u043b\u0430\u0432\u0438\u0448\u0438, \u0434\u043b\u044f \u0442\u043e\u0433\u043e \u0447\u0442\u043e \u0431\u044b \u043d\u0430\u0436\u0430\u0442\u0438\u0435 \u043d\u0430 \u043d\u0435\u0451 \u0431\u044b\u043b\u043e \u0437\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043e \u0441\u043a\u0432\u043e\u0437\u044c \u043b\u044e\u0431\u044b\u0435 \u0438\u043d\u044b\u0435 \u0441\u0438\u0433\u043d\u0430\u043b\u044b. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0422\u043e \u0435\u0441\u0442\u044c, \u0435\u0441\u043b\u0438 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">Dead"
                        " man\u2019s switch</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0431\u044b\u043b \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d \u043a, \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">U</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d, \u0442\u043e \u043d\u0430\u0436\u0430\u0442\u0438\u044f \u043d\u0430 \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#ff80ce;\">\u0413</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d \u043d\u0435 \u0430\u043a\u0442\u0438\u0432\u0438\u0440\u0443\u044e\u0442 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">DMS</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">. \u0425\u043e\u0442\u044c \u201c</span><spa"
                        "n style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">U</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d \u0438 \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#ff80ce;\">\u0413</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d \u0440\u0430\u0437\u0434\u0435\u043b\u044f\u044e\u0442 \u043e\u0434\u0438\u043d \u0438 \u0442\u043e\u0442 \u0436\u0435 keycode, \u0438\u0445 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043d\u0430 \u0440\u0430\u0437\u043d\u044b\u0445 \u0440\u0430\u0441\u043a\u043b\u0430\u0434\u043a\u0430\u0445 \u0440\u0430\u0437\u043d\u043e\u0435. \u0421\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e, \u0435\u0441\u043b\u0438 \u043a </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">DMS</span><span style=\" font-family:'Bahnschrift"
                        "','sans-serif'; font-size:11pt;\"> \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u0430 \u043a\u043b\u0430\u0432\u0438\u0448\u0430 \u043d\u0430 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u043e\u0439 \u0440\u0430\u0441\u043a\u043b\u0430\u0434\u043a\u0435, \u0442\u043e \u0438 \u0430\u043a\u0442\u0438\u0432\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0435\u0451 \u043c\u043e\u0436\u043d\u043e \u043b\u0438\u0448\u044c \u043d\u0430 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u043e\u0439 \u0440\u0430\u0441\u043a\u043b\u0430\u0434\u043a\u0435. \u042d\u0442\u043e \u043d\u0435 \u043a\u0430\u0441\u0430\u0435\u0442\u0441\u044f \u0444\u0443\u043d\u043a\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0445 \u043a\u043b\u0430\u0432\u0438\u0448, \u0432\u0440\u043e\u0434\u0435 </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">shift</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">, </span><span style=\" font-family:'B"
                        "ahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">scroll lock</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">, </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">end</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0438 \u0442\u0430\u043a \u0434\u0430\u043b\u0435\u0435, \u0442.\u043a. \u043d\u0430 \u043b\u044e\u0431\u043e\u0439 \u0440\u0430\u0441\u043a\u043b\u0430\u0434\u043a\u0435 \u043a \u044d\u0442\u0438\u043c </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">keycode\u2019\u0430\u043c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043e \u043e\u0434\u043d\u043e \u0438 \u0442\u043e \u0436\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-"
                        "top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u0442\u0441\u044f \u043f\u0440\u0438\u0432\u044f\u0437\u044b\u0432\u0430\u0442\u044c \u043a </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">DMS</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u0444\u0443\u043d\u043a\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u043c \u043a\u043b\u0430\u0432\u0438\u0448\u0430\u043c.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041a </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60"
                        "540;\">DMS</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; text-decoration: underline;\">\u041d\u0415\u041b\u042c\u0417\u042f</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043f\u0440\u0438\u0432\u044f\u0437\u044b\u0432\u0430\u0442\u044c \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">+</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u041a </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">DMS</span><span style=\" font-family:'Bahnschri"
                        "ft','sans-serif'; font-size:11pt;\"> </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; text-decoration: underline;\">\u041d\u0415\u041b\u042c\u0417\u042f</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\"> \u043f\u0440\u0438\u0432\u044f\u0437\u044b\u0432\u0430\u0442\u044c \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u044e \u043a\u043b\u0430\u0432\u0438\u0448 \u0447\u0435\u0440\u0435\u0437 \u201c</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">+</span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u201d.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043a\u043b\u0430\u0432\u0438\u0448"
                        "\u0438 \u0434\u043b\u044f </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt; font-weight:600; color:#e60540;\">DMS </span><span style=\" font-family:'Bahnschrift','sans-serif'; font-size:11pt;\">\u043f\u0440\u0438\u0439\u0434\u0443 \u0432 \u0441\u0438\u043b\u0443 \u043b\u0438\u0448\u044c \u043f\u043e\u0441\u043b\u0435 \u043f\u0435\u0440\u0435\u0437\u0430\u043f\u0443\u0441\u043a\u0430.</span><span style=\" font-size:11pt;\"> </span></p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0443/\u0438 \u043d\u0438\u0436\u0435", None))
        self.DMSaccept.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0435\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435:", None))
        self.currentDMS.setText(QCoreApplication.translate("MainWindow", u"scroll lock", None))
        self.label.setText("")
        self.WhereIsBut.setText("")
    # retranslateUi


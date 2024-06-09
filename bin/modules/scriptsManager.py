import os
import keyboard
import mouse
from PyQt5 import QtCore, QtWidgets, QtGui
from ReCode import baseconstructing
import codecs
from ui_interface import *
from ui_Dialog import *

#Создание таблиц с работающими скриптами
# ////////////////////////////////////////////////////////////////////////////////////////////
def createWorkScriptTables(self, name, macroslist):
    File = open(os.path.abspath(f"../O-Hands/{name}.manual"), "r")
    readedManual = File.readlines()
    for each in readedManual:
        if (each.find("KS") != -1):
            KillSwitch = (each.replace("KS ", "")[:-1])
            break
    File.close()
    font6 = QFont()
    font6.setFamily(u"Bahnschrift")
    font6.setPointSize(11)
    font12 = QFont()
    font12.setFamily(u"Bahnschrift")
    font12.setPointSize(13)
    font12.setBold(False)
    font12.setItalic(False)
    font12.setUnderline(False)
    font12.setWeight(50)
    font12.setStrikeOut(False)
    font12.setKerning(False)
    fileNamed = name
    newName = str(fileNamed) + "exMacroTable"
    self.ui.workMacroTable = QFrame(self.ui.scrollAreaWidgetContents_2)
    self.ui.workMacroTable.setObjectName(newName)
    self.ui.workMacroTable.setMaximumSize(QSize(500, 45))
    setattr(self.ui, newName, self.ui.workMacroTable)
    self.ui.workMacroTable.setStyleSheet(u"border: 3px solid rgb(230,5,64);\n"
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
    self.ui.workMacroTable.setFrameShape(QFrame.StyledPanel)
    self.ui.workMacroTable.setFrameShadow(QFrame.Raised)
    self.ui.horizontalLayout_86 = QHBoxLayout(self.ui.workMacroTable)
    self.ui.horizontalLayout_86.setSpacing(3)
    self.ui.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
    self.ui.horizontalLayout_86.setContentsMargins(0, 0, 3, 0)
    newName = str(fileNamed) + "workMacroName"
    self.ui.workMacroName = QLabel(self.ui.workMacroTable)
    self.ui.workMacroName.setObjectName(newName)
    self.ui.workMacroName.setText(fileNamed)
    self.ui.workMacroName.setFont(font12)
    setattr(self.ui, newName, self.ui.workMacroName)
    self.ui.workMacroName.setStyleSheet(u"border: 0px red;\n"
                                     "color: rgb(230,5,64);")
    self.ui.workMacroName.setAlignment(Qt.AlignCenter)

    self.ui.horizontalLayout_86.addWidget(self.ui.workMacroName)
    newName = str(fileNamed) + "workMacroTerminate"
    self.ui.workMacroTerminate = QPushButton(self.ui.workMacroTable)
    self.ui.workMacroTerminate.setObjectName(fileNamed)
    self.ui.workMacroTerminate.setFont(font6)
    setattr(self.ui, newName, self.ui.workMacroTerminate)
    self.ui.workMacroTerminate.setText("Отключить")
    def terminateIt():
        temp = fileNamed
        for i in range(len(macroslist)):
            if macroslist[i][0] == temp:
                macroslist[i][1].kill()
                macroslist.pop(i)
                try:
                    keyboard.remove_hotkey(f"{KillSwitch}")
                except:
                    pass
                return 1
    self.ui.workMacroTerminate.setCursor(QCursor(Qt.PointingHandCursor))
    self.ui.workMacroTerminate.clicked.connect(lambda:[terminateIt(), self.updateExistingScripts()])
    self.ui.workMacroTerminate.setStyleSheet(u"QPushButton{\n"
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
    icon28.addFile(u":/icons/icons/power.svg", QSize(), QIcon.Normal, QIcon.Off)
    self.ui.workMacroTerminate.setIcon(icon28)

    self.ui.horizontalLayout_86.addWidget(self.ui.workMacroTerminate)

    self.ui.verticalLayout_60.addWidget(self.ui.workMacroTable)

#Создание таблиц с готовыми к работе скриптами
# ////////////////////////////////////////////////////////////////////////////////////////////
def createExScriptTables(self, name):
    icon25 = QIcon()
    icon25.addFile(u":/icons/icons/check.svg", QSize(), QIcon.Normal, QIcon.Off)
    font6 = QFont()
    font6.setFamily(u"Bahnschrift")
    font6.setPointSize(11)
    fileNamed = name
    newName = str(fileNamed[:-7]) + "exMacroTable"
    self.ui.exMacroTable = QFrame(self.ui.scrollAreaWidgetContents)
    self.ui.exMacroTable.setObjectName(newName)
    setattr(self.ui, newName, self.ui.exMacroTable)
    self.ui.exMacroTable.setMaximumSize(QSize(500, 45))
    self.ui.exMacroTable.setStyleSheet(u"border: 3px solid rgb(230,5,64);\n"
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
    self.ui.exMacroTable.setFrameShape(QFrame.StyledPanel)
    self.ui.exMacroTable.setFrameShadow(QFrame.Raised)
    self.ui.horizontalLayout_84 = QHBoxLayout(self.ui.exMacroTable)
    self.ui.horizontalLayout_84.setSpacing(3)
    self.ui.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
    self.ui.horizontalLayout_84.setContentsMargins(0, 0, 3, 0)
    newName = str(fileNamed[:-7]) + "exMacroName"
    self.ui.exMacroName = QLabel(self.ui.exMacroTable)
    self.ui.exMacroName.setObjectName(newName)
    self.ui.exMacroName.setText(str(fileNamed[:-7]))
    setattr(self.ui, newName, self.ui.exMacroName)
    font10 = QFont()
    font10.setFamily(u"Bahnschrift")
    font10.setPointSize(13)
    font10.setBold(False)
    font10.setItalic(False)
    font10.setUnderline(False)
    font10.setWeight(50)
    font10.setStrikeOut(False)
    font10.setKerning(False)
    self.ui.exMacroName.setFont(font10)
    self.ui.exMacroName.setStyleSheet(u"border: 0px red;\n"
                                      "color: rgb(230,5,64);")
    self.ui.exMacroName.setAlignment(Qt.AlignCenter)

    self.ui.horizontalLayout_84.addWidget(self.ui.exMacroName)
    newName = str(fileNamed[:-7]) + "exMacroRun"
    self.ui.exMacroRun = QPushButton(self.ui.exMacroTable)
    self.ui.exMacroRun.setText("Запустить")
    self.ui.exMacroRun.setObjectName(newName)
    self.ui.exMacroRun.setFont(font6)
    self.ui.exMacroRun.setCursor(QCursor(Qt.PointingHandCursor))
    setattr(self.ui, newName, self.ui.exMacroRun)
    self.ui.exMacroRun.clicked.connect(lambda: [self.usemacro(str(fileNamed[:-7]))])
    self.ui.exMacroRun.setStyleSheet(u"QPushButton{\n"
                                     "border:3px solid rgb(24,24,36);\n"
                                     "}\n"
                                     "QPushButton:hover:!pressed\n"
                                     "{\n"
                                     "border: 3px solid rgb(230,5,64);\n"
                                     "border-radius: 7px;\n"
                                     "bacground-color: rgb(17,16,26);\n"
                                     "\n"
                                     "}")
    self.ui.exMacroRun.setIcon(icon25)

    self.ui.horizontalLayout_84.addWidget(self.ui.exMacroRun)

    newName = str(fileNamed[:-7]) + "exMacroChange"
    self.ui.exMacroChange = QPushButton(self.ui.exMacroTable)
    self.ui.exMacroChange.setText("Изменить")
    self.ui.exMacroChange.setObjectName(newName)
    setattr(self.ui, newName, self.ui.exMacroChange)
    self.ui.exMacroChange.clicked.connect(
        lambda: [self.ChooseFile(fileNamed[:-7]), self.ui.stackedWidget.setCurrentWidget(self.ui.editScript)])

    self.ui.exMacroChange.setFont(font6)
    self.ui.exMacroChange.setCursor(QCursor(Qt.PointingHandCursor))

    self.ui.exMacroChange.setStyleSheet(u"QPushButton{\n"
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
    icon26.addFile(u":/icons/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
    self.ui.exMacroChange.setIcon(icon26)

    self.ui.horizontalLayout_84.addWidget(self.ui.exMacroChange)

    newName = str(fileNamed[:-7]) + "exMacroDelete"
    self.ui.exMacroDelete = QPushButton(self.ui.exMacroTable)
    self.ui.exMacroDelete.setText("Удалить")
    self.ui.exMacroDelete.setObjectName(newName)
    self.ui.exMacroDelete.setFont(font6)
    self.ui.exMacroDelete.setCursor(QCursor(Qt.PointingHandCursor))
    setattr(self.ui, newName, self.ui.exMacroDelete)
    temp = os.path.abspath(f"../O-Hands/{name}")
    temp2 = os.path.abspath(f"../O-Hands/Compiled/{name[:-7]}.py")
    self.ui.exMacroDelete.clicked.connect( lambda: [os.remove(temp),os.remove(temp2),self.updateExistingScripts(),self.DBManager.action(f"Удалил {name[:-7]}")])
    self.ui.exMacroDelete.setStyleSheet(u"QPushButton{\n"
                                        "border:3px solid rgb(24,24,36);\n"
                                        "}\n"
                                        "QPushButton:hover:!pressed\n"
                                        "{\n"
                                        "border: 3px solid rgb(230,5,64);\n"
                                        "border-radius: 7px;\n"
                                        "bacground-color: rgb(17,16,26);\n"
                                        "\n"
                                        "}")
    icon27 = QIcon()
    icon27.addFile(u":/icons/icons/file-minus.svg", QSize(), QIcon.Normal, QIcon.Off)
    self.ui.exMacroDelete.setIcon(icon27)

    self.ui.horizontalLayout_84.addWidget(self.ui.exMacroDelete)

    self.ui.verticalLayout_59.addWidget(self.ui.exMacroTable)

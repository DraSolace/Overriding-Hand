# coding=utf-8           # -*- coding: utf-8 -*
# -*- coding: UTF-8 -*
import sys
import os
import time
import subprocess
import keyboard
import mouse
from PySide2 import QtCore, QtWidgets, QtGui
from ReCode import baseconstructing
import codecs
from ui_interface import *
from ui_Dialog import *
#Класс главного окна
class MainWindow(QMainWindow):
    global isRedacted, listofmacros, posFlag, current_edited
    current_edited = None
    listofmacros = []
    posFlag = True
    isRedacted = False
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Отцентровка окна
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        #Убрать тайтл, сделать прозрачный фон для корректной работы тени
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #Эффект Тени
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 5, 64,150))

        #И применить его к центру
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        #Обозначаем ту маленькую штуковину в левом нижнем углу как грип-поинт
        QSizeGrip(self.ui.size_grip)

        #Минимизировать окно
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())

        #Закрыть окно
        self.ui.close_window_button.clicked.connect(lambda: self.closeOverridingHand())
        self.ui.exit_button.clicked.connect(lambda: [self.slideLeftMenu(),self.ui.stackedWidget.setCurrentWidget(self.ui.mainmenu)])

        #Восстановить\максимизировать окно
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())

        #Перетаскивание всего окна мышкой, если она на шапке
        def moveWindow(e):
            if self.isMaximized() == False:  # Не максимизировано
                # Двигать окно можно лишь когда оно "нормального" размера

                # Если нажат (только) ЛКМ:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        #Mouse event для функции
        self.ui.header_frame.mouseMoveEvent = moveWindow

        # Присваивание функций ко всем кнопкам на GUI
        # ////////////////////////////////////////////////////////////////////////////////////////////
        self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.introBut.clicked.connect(lambda:  self.ui.stackedWidget.setCurrentWidget(self.ui.intro))
        self.ui.createScript.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.makeScript))
        self.ui.structureBut.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.OverScriptStructure))
        self.ui.sendButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.send))
        self.ui.writeButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.write))
        self.ui.kPRButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.kPressRelease))
        self.ui.moveButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.move))
        self.ui.PosButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Pos))
        self.ui.clickButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.click))
        self.ui.mPressButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.mPressRelease))
        self.ui.wheelButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.wheel))
        self.ui.waitButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.wait))
        self.ui.keysButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.keys))
        self.ui.fileNameBut.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.fileName))
        self.ui.OverLapBut.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.OverLap))
        self.ui.NonUsedSymbolsBut.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.nonUsedSymbols))
        self.ui.settingsBut.clicked.connect(lambda: [self.ui.stackedWidget_2.setCurrentWidget(self.ui.settingsTitle), self.ui.stackedWidget.setCurrentWidget(self.ui.settingsPage)])
        self.ui.PanicButBut.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.panicButtpnSettings))
        self.ui.DMSBUT.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.DMSsettings))
        self.ui.DeprecationBut.clicked.connect(lambda: self.showPopUp("Не-а", "Лишь для опытных пользователей\nАктивируйте режим отладки"))
        self.ui.gitHubBut.clicked.connect(lambda: os.system("start \"\" https://github.com/DraSolace/Overriding-Hand"))
        self.ui.oneRepeatIssueButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.oneRepeatIssue))
        self.ui.ChooseFileBut.clicked.connect(lambda: self.ChooseFile())
        self.ui.DMSaccept.clicked.connect(lambda: self.rebindPBorDMS(False))
        self.ui.PanicButAccept.clicked.connect(lambda: self.rebindPBorDMS(True))
        self.ui.testButton.clicked.connect(lambda: [self.buttonTest()])
        self.ui.editScriptButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.editScript))
        self.ui.posButton.clicked.connect(lambda: self.showPos())
        self.ui.WhereIsBut.clicked.connect(lambda: os.startfile(os.path.abspath(f"../")))
        self.ui.existingScriptsBut.clicked.connect(lambda: [self.ui.stackedWidget.setCurrentWidget(self.ui.ExistingScript), self.updateExistingScripts()] )
        self.ui.backToEx.clicked.connect(lambda: [self.ui.stackedWidget.setCurrentWidget(self.ui.ExistingScript), self.updateExistingScripts()])
        self.ui.createButton.clicked.connect(lambda: self.makeOverScript(self.ui.nameLine.text(), True))

        #global current_edited
        self.ui.RewriteBut.clicked.connect(lambda: [self.ChooseFile(),self.makeOverScript(current_edited, False)])
        self.ui.quickUseButton.clicked.connect(lambda: [self.usemacro(self.ui.quickUse.text())])

        #Чтение UNI файла и присваивание Panic button с Dead man's switch

        oFile = open(os.path.abspath("uni.cfg"), "r")
        lines = oFile.readlines()
        oFile.close()
        self.ui.currentPanicButton.setText((lines[0])[:-1])
        keyboard.add_hotkey(f"{(lines[0])[:-1]}", self.PanicButton)
        self.ui.currentDMS.setText((lines[1])[:-1])
        keyboard.add_hotkey(f"{(lines[1])[:-1]}", lambda: self.DeadMansSwitch())

        #Отображение окна
        self.show()

        #Анимация открытия окна
        self.animation = QPropertyAnimation(self.ui.mainframe, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1024)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        self.animation.finished.connect(lambda: self.ui.mainframe.setMaximumWidth(16777215))
        self.updateExistingScripts()

    #Перебиндовка Panic button и Dead man's switch На другие клавиши
    # ////////////////////////////////////////////////////////////////////////////////////////////
    def rebindPBorDMS(self, isPBorDMs):
        if isPBorDMs == True:
            inLineEdit =self.ui.PanicbutLineEdit.text()
            try:
                keyboard.add_hotkey(f"{inLineEdit}", lambda: keyboard.remove_hotkey(f"{inLineEdit}"))
            except:
                self.showPopUp("Ошибка", "Этой клавиши не существует")
                return 0
            if inLineEdit == "+":
                self.showPopUp("НАПИСАНО БЫЛО", "\'+\' привязывать НЕЛЬЗЯ")
                return 0
            elif inLineEdit.find("+") != -1:
                self.showPopUp("НАПИСАНО БЫЛО", "Комбинацию клавиш привязывать НЕЛЬЗЯ")
                return 0
            oFile = open("uni.cfg", "r")
            lines = oFile.readlines()
            oFile.close()
            lines[0] = inLineEdit + '\n'
            oFile = open("uni.cfg", "w")
            for each in lines:
                oFile.write(each)
            oFile.close()
            self.ui.PanicbutLineEdit.setEnabled(False)
            self.ui.PanicButAccept.setEnabled(False)
            self.ui.PanicbutLineEdit.setStyleSheet("border: none; \ncolor: rgb(230,5,64)")
            self.showPopUp("Перезаписано", "Перезапустите Overriding hand")
        else:
            inLineEdit = self.ui.DMSeditLable.text()
            try:
                keyboard.add_hotkey(f"{inLineEdit}", lambda: keyboard.remove_hotkey(f"{inLineEdit}"))
            except:
                self.showPopUp("Ошибка", "Этой клавиши не существует")
                return 0
            if inLineEdit == "+":
                self.showPopUp("НАПИСАНО БЫЛО", "\'+\' привязывать НЕЛЬЗЯ")
                return 0
            elif inLineEdit.find("+") != -1:
                self.showPopUp("НАПИСАНО БЫЛО", "Комбинацию клавиш привязывать НЕЛЬЗЯ")
                return 0
            oFile = open("uni.cfg", "r")
            lines = oFile.readlines()
            oFile.close()
            lines[1] = inLineEdit + '\n'

            oFile = open("uni.cfg", "w")
            for each in lines:
                oFile.write(each)
            oFile.close()
            self.ui.DMSeditLable.setEnabled(False)
            self.ui.DMSeditLable.setStyleSheet("border: none; \ncolor: rgb(230,5,64)")
            self.ui.DMSaccept.setEnabled(False)
            self.showPopUp("Перезаписано", "Перезапустите Overriding hand")

    #Функция для привязки к Panic button
    # ////////////////////////////////////////////////////////////////////////////////////////////
    def PanicButton(self):
        temp = (len(listofmacros) -1 )
        for i in range(len(listofmacros)):
            listofmacros[temp][1].kill()
            listofmacros.pop(temp)
            temp -= 1
        self.updateExistingScripts()
        self.ui.stackedWidget.setCurrentWidget(self.ui.mainmenu)

    #Функция для привязки к Dead man's switch
    # ////////////////////////////////////////////////////////////////////////////////////////////
    def DeadMansSwitch(self):
        self.PanicButton()
        try:
            self.DialogWindow.close()
        except AttributeError:
            pass
        self.close()


    #Обновление готовых и работающих скриптов во вкладке "Готовые OverScripts"
    #////////////////////////////////////////////////////////////////////////////////////////////
    def updateExistingScripts(self):
        #Перебор всех существующих таблиц с работащим скриптами и их удаление
        for child in self.ui.scrollAreaWidgetContents_2.findChildren(QtWidgets.QFrame):
            child.setParent(None)
        tempArr = []
        #Создание новых таблиц из макросов, находящихся в listofmacros
        for item in range(len(listofmacros)):
            tempArr.append(listofmacros[item][0])
        for macro in tempArr:
            self.createWorkScriptTables(macro)

        # Перебор всех существующих таблиц с готовыми скриптами и их удаление
        for child in self.ui.scrollAreaWidgetContents.findChildren(QtWidgets.QFrame):
            child.setParent(None)
        tempArr =[]
        # Создание новых таблиц из макросов, находящихся в ../O-Hands/{название}.manual
        for file in os.listdir(os.path.abspath(f"../O-Hands")):
            if file.endswith(".manual"):
                tempArr.append(file)
        for fileNamed in tempArr:
            self.createExScriptTables(fileNamed)

    #Создание таблиц с работающими скриптами
    # ////////////////////////////////////////////////////////////////////////////////////////////
    def createWorkScriptTables(self, name):
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
            for i in range(len(listofmacros)):
                if listofmacros[i][0] == temp:
                    listofmacros[i][1].kill()
                    listofmacros.pop(i)
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
        self.ui.exMacroDelete.clicked.connect( lambda: [os.remove(temp),os.remove(temp2),self.updateExistingScripts()])
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

    #Функция для выбора файла во вкладке "Изменить Overscript"
    # ////////////////////////////////////////////////////////////////////////////////////////////
    def ChooseFile(self, temp = "none"):
        global current_edited
        if temp != "none":
            temptxt = temp
        else:
            temptxt = self.ui.editFileLine.text()
        pathToManual = os.path.abspath(f"../O-Hands/{temptxt}.manual")
        if os.path.exists(pathToManual):
            oFile = open(pathToManual, "r")
            lines = oFile.read()
            oFile.close()
            self.ui.codeRewriteEditor.clear()
            self.ui.codeRewriteEditor.insertPlainText(lines)
            self.ui.ChosenFileLableSEMEN.setText(f"{temptxt}")
            self.ui.ChosenFileLableIsOpen.setText(f"Открыт:")
            self.ui.editFileLine.clear()
            current_edited = temptxt
        else:
            self.showPopUp("Ой...", "Такого макроса не существует")

    #Показ координат курсора при нажатии на "-" в меню с созданием нового OverScript
    # ////////////////////////////////////////////////////////////////////////////////////////////
    def showPos(self):
        global posFlag
        if posFlag == True:
            self.animation = QPropertyAnimation(self.ui.posHelpButton, b"maximumWidth")
            self.animation.setDuration(250)
            self.animation.setStartValue(0)
            self.animation.setEndValue(230)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
            self.ui.posHelpButton.setText("Нажатия на \"-\" \nВыведут текущие координаты курсора")
            keyboard.add_hotkey("-", lambda : self.ui.posLable.setText(str(mouse.get_position())))
            posFlag = not posFlag
        else:
            self.animation = QPropertyAnimation(self.ui.posHelpButton, b"maximumWidth")
            self.animation.setDuration(250)
            self.animation.setStartValue(self.ui.posHelpButton.width())
            self.animation.setEndValue(0)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
            #self.animation.finished.connect(self.ui.posHelpButton.setText(""))
            self.ui.posLable.setText("")
            keyboard.remove_hotkey("-")
            posFlag = not posFlag

    #Функция, закрывающая Overriding hand с анимацией
    # ////////////////////////////////////////////////////////////////////////////////////////////
    def closeOverridingHand(self):
        self.PanicButton()
        self.ui.slideContainer.setMaximumWidth(0)
        self.shadow.setBlurRadius(0)
        try:
            self.DialogWindow.close()
        except AttributeError:
            pass
        self.animation = QPropertyAnimation(self.ui.mainbody, b"maximumHeight")
        self.animation.setDuration(250)
        self.animation.setStartValue(self.ui.mainbody.height())
        self.animation.setEndValue(0)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        self.animation.finished.connect(lambda: self.close())

    #Функция для создания и отображение Поп-апа
    # ////////////////////////////////////////////////////////////////////////////////////////////
    def showPopUp(self, header, text):
        self.DialogWindow = QtWidgets.QDialog()
        self.Dialog = Ui_Dialog()
        self.Dialog.setupUi(self.DialogWindow)
        self.Dialog.messageHeader.setText(header)
        self.Dialog.messageText.setText(text)
        self.Dialog.messageButton.clicked.connect(lambda:closePopUp())
        self.DialogWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.DialogWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.DialogWindow.show()
        self.DialogWindow.animation = QPropertyAnimation(self.Dialog.frame, b"maximumHeight")
        self.DialogWindow.animation.setDuration(200)
        self.DialogWindow.animation.setStartValue(0)
        self.DialogWindow.animation.setEndValue(160)
        self.DialogWindow.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.DialogWindow.animation.start()
        def closePopUp():
            self.DialogWindow.animation = QPropertyAnimation(self.Dialog.frame, b"maximumHeight")
            self.DialogWindow.animation.setDuration(200)
            self.DialogWindow.animation.setStartValue(160)
            self.DialogWindow.animation.setEndValue(0)
            self.DialogWindow.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.DialogWindow.animation.start()
            self.DialogWindow.animation.finished.connect(lambda: self.DialogWindow.close())

    #Функция для проверки клавиш
    # ////////////////////////////////////////////////////////////////////////////////////////////
    def buttonTest(self):
        self.ui.testLable.setText("Нажмите на любую клавишу")
        temp = keyboard.read_key()
        self.ui.testLable.setText(temp)

    #Функция запускающая макросы
    # ////////////////////////////////////////////////////////////////////////////////////////////
    # Использование макросов в Overriding hand вращается вокруг "listofmacros"
    # listofmacros это список с подсписками. Каждый элемент в listofmacros это подсписок из двух элементов -
    # Название макроса и ссылки на подпроцесс, привязанной к исполняемому скрипту.
    # Все манипуляции проводятся отталкиваясь от информации из listofmacros, привязка кнопок в GUI и клавиш на клавиатуре
    def usemacro(self, name):
        global listofmacros

        #Если макрос уже существует, прервать запуск
        for i in range (len(listofmacros)):
            if listofmacros[i][0] == name:
                self.showPopUp("Ой...", f" \'{name}\' уже запущен")
                return 1

        #Создание пути для каждого из возможных файлов ассоциирующиеся с названием {name}
        pathToMacro = os.path.abspath(f"../O-Hands/Compiled/{name}.py")
        pathToManual = os.path.abspath(f"../O-Hands/{name}.manual")

        #Проверка на существование подобного "manual" файла
        if os.path.exists(pathToManual):
            #Попытаться инициализировать скрипт
            try:
                #Открытие manual файла для нахождения KillSwitch
                File = open(pathToManual, "r")
                readedManual = File.readlines()
                File.close()
                for each in readedManual:
                    if (each.find("KS") != -1):
                        KillSwitch = (each.replace("KS ", "")[:-1])
                        break

                #Инициализировать скрипт и добавить к listofmacros его название и ссылку на подпроцесс
                si = subprocess.STARTUPINFO()
                si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                listofmacros.append([f"{name}",subprocess.Popen(["python.exe", pathToMacro], startupinfo=si)])

                #Для привязки к KillSwitch. Индекс текущего макроса в listofmacros. "-1" из-за индексации с 0
                temp = len(listofmacros)-1

                #Привязать к клавише по keycode'у KillSwitch отвязку самой себя, прекращение работы скрипта,
                #Выггрузка элемента этого скрипта из listofmacros и обновление страницы "Готовые OverScripts"
                keyboard.add_hotkey(f"{KillSwitch}",lambda :[keyboard.remove_hotkey(f"{KillSwitch}"), listofmacros[temp][1].kill(), listofmacros.pop(temp), self.updateExistingScripts])
                self.ui.quickUse.clear()
                self.showPopUp("Готово", "Макрос успешно включен")
                self.updateExistingScripts()
            except:

            #Неудача означает, что manual файл существует, но его скомплированная версия - нет
                self.showPopUp("Ой...", "Макроса не может быть запущен или он не существует.\nПересоздайте его.")
        else:

            #Файла просто не существует
            self.showPopUp("Ой...", "Макроса с таким названием не существует")

    # использовать baseconstruck из ReCode, создать manual и py файлы
    def makeOverScript(self, filename, EditOrCreate):
        global current_edited, isRedacted
        if filename == "":
            self.showPopUp("Ой...", "Имя скрипта не указано")
            return 0
        if EditOrCreate == False:
            if current_edited == None:
                self.showPopUp("Ой...", "Скрипт не выбран")
                return 0
        if(filename != ""):
            sour = os.path.abspath(f"../O-Hands/{filename}.manual")
            File = codecs.open(sour, 'w', encoding= "utf-8")
            if EditOrCreate == True:
                temp = self.ui.codeEditor.toPlainText()
            else:
                temp = self.ui.codeRewriteEditor.toPlainText()
            File.write(u"{temp}".format(temp = temp))
            File.write("\n")
            File.close()
            baseconstructing(sour, filename)
            sour = os.path.abspath(f"../compiled/Compiling.report")
            File = open(sour, 'r')
            Checker= File.readline()
            if Checker == "!KS or HK is not defined":
                self.showPopUp("Ой...", "KS или HK не определены")
            elif Checker == "!Mode is not defined":
                self.showPopUp("Ой...", "Режим работы не определен")
            elif Checker == "!Cannot be compiled":
                self.showPopUp("Ой...", "В коде пристуствуют синтаксические ошибки\nCкрипт не может быть скомпилирован")
            elif Checker == "!Symbol in HK or KS":
                self.showPopUp("Ой...", "Использован зарезервированный символ\nпри описании HK или KS")
            elif Checker == "!Symbol in send":
                self.showPopUp("Ой...", "Использован зарезервированный символ\nв команде \'send()\'")
            elif Checker == "Successful:)":
                if EditOrCreate == True:
                    self.showPopUp("Отлично!", "Макрос готов к использованию")
                    self.ui.codeEditor.clear()
                    self.ui.nameLine.clear()
                    current_edited = None
                    self.ui.ChosenFileLableSEMEN.setText(f"")
                    self.ui.ChosenFileLableIsOpen.setText(f"")
                else:
                    isRedacted = not isRedacted
                    self.showPopUp("Отлично!", "Макрос успешно перезаписан")
                    self.ui.codeRewriteEditor.clear()
                    self.ui.editFileLine.clear()
                    current_edited = None
                    self.ui.ChosenFileLableSEMEN.setText(f"")
                    self.ui.ChosenFileLableIsOpen.setText(f"")

            File.close()


    #Выдвижение меню слева
    def slideLeftMenu(self):
        width = self.ui.slideContainer.width()

        if width == 0:
            newWidth = 230
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-left.svg"))
        else:
            newWidth = 0
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/align-left.svg"))


        # Анимирование этого перехода
        self.animation = QPropertyAnimation(self.ui.slideContainer, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()




    #######################################################################


    #Добавить к окну хук на MouseEvent
    def mousePressEvent(self, event):
        # Получить текущую позицию мыши
        self.clickPosition = event.globalPos()
        # это значение используем при движении окна

    #Изменение размера окна и его иконки при максимизации\минимизации окна
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/icons/minimize-2.svg"))





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

# coding=utf-8
# -*- coding: utf-8 -*
# -*- coding: UTF-8 -*


import os
import subprocess
import keyboard
import mouse
from PyQt5 import QtCore, QtWidgets, QtGui
from ReCode import baseconstructing
import codecs
from ui_interface import *
from ui_Dialog import *
from DataBaseManager import DBMRoutine
from scriptsManager import createExScriptTables, createWorkScriptTables
from initializeGuiButtonsBound import BoundGuiButtons

#Класс главного окна
class MainWindow(QMainWindow):
    global isRedacted, listofmacros, posFlag, current_edited
    current_edited = None
    listofmacros = []
    posFlag = True
    isRedacted = False
    def __init__(self):
        self.DBManager = DBMRoutine()
        QMainWindow.__init__(self)
        self.setWindowTitle("Overriding Hands")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Overriding Hand")
        self.setWindowIcon(QtGui.QIcon('HandLogo.ico'))

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
            # Двигать окно можно лишь когда оно не максимизированно
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        #Mouse event для функции
        self.ui.header_frame.mouseMoveEvent = moveWindow
        #Инициализация всех биндов для кнопок на GUI
        BoundGuiButtons(self)

        #Один отдельный байнд на кнопку в GUI из-за обращения к локальному атрибуту
        self.ui.RewriteBut.clicked.connect(lambda: [self.ChooseFile(), self.ChangeScript(current_edited)])

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
            self.DBManager.action(f"Изменил Panic button на {self.ui.PanicbutLineEdit.text()}")
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
            self.DBManager.action(f"Изменил DMS на {self.ui.DMSeditLable.text()}")

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
        self.DBManager.action("Использовал DMS")
        self.PanicButton()
        try:
            self.DialogWindow.close()
        except AttributeError:
            pass
        self.close()


    #Обновление готовых и работающих скриптов во вкладке "Готовые OverScripts"
    #Колдунство с динамическим созданием экземпляров по атрибутам, за это отвечает createWorkScriptTables
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
            createWorkScriptTables(self, macro, listofmacros)

        # Перебор всех существующих таблиц с готовыми скриптами и их удаление
        for child in self.ui.scrollAreaWidgetContents.findChildren(QtWidgets.QFrame):
            child.setParent(None)
        tempArr =[]
        # Создание новых таблиц из макросов, находящихся в ../O-Hands/{название}.manual
        for file in os.listdir(os.path.abspath(f"../O-Hands")):
            if file.endswith(".manual"):
                tempArr.append(file)
        for fileNamed in tempArr:
            createExScriptTables(self, fileNamed)


    #Функция для выбора файла во вкладке "Изменить Overscript"
    # ////////////////////////////////////////////////////////////////////////////////////////////
    def ChooseFile(self, temp = None):
        global current_edited
        if temp == None:
            self.showPopUp("Ой...","Скрипт не выбран")
            return
        temptxt = temp
        pathToManual = os.path.abspath(f"../O-Hands/{temptxt}.manual")
        if os.path.exists(pathToManual):
            oFile = open(pathToManual, "r")
            lines = oFile.read()
            oFile.close()
            self.ui.codeRewriteEditor.clear()
            self.ui.codeRewriteEditor.insertPlainText(lines)
            self.ui.ChosenFileLableSEMEN.setText(f"{temptxt}")
            self.ui.ChosenFileLableIsOpen.setText(f"Открыт:")
            current_edited = temptxt

    
    #Показ координат курсора при нажатии на "-" в меню с созданием нового OverScript
    # ////////////////////////////////////////////////////////////////////////////////////////////
    def showPos(self):
        global posFlag
        if posFlag == True:
            keyboard.add_hotkey("-", lambda: [self.ui.posLable.setText(str(mouse.get_position())), self.ui.posLable_2.setText(str(mouse.get_position()))])

            self.animation = QPropertyAnimation(self.ui.posHelpButton, b"maximumWidth")
            self.animation.setDuration(250)
            self.animation.setStartValue(0)
            self.animation.setEndValue(230)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
            self.ui.posHelpButton.setText("Нажатия на \"-\" \nВыведут текущие координаты курсора")
            self.animation1 = QPropertyAnimation(self.ui.posHelpButton_2, b"maximumWidth")
            self.animation1.setDuration(250)
            self.animation1.setStartValue(0)
            self.animation1.setEndValue(230)
            self.animation1.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation1.start()
            self.ui.posHelpButton_2.setText("Нажатия на \"-\" \nВыведут текущие координаты курсора")
            posFlag = not posFlag
        else:
            self.animation = QPropertyAnimation(self.ui.posHelpButton, b"maximumWidth")
            self.animation.setDuration(250)
            self.animation.setStartValue(self.ui.posLable.width())
            self.animation.setEndValue(0)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
            #self.animation.finished.connect(self.ui.posHelpButton.setText(""))
            self.animation1 = QPropertyAnimation(self.ui.posHelpButton_2, b"maximumWidth")
            self.animation1.setDuration(250)
            self.animation1.setStartValue(self.ui.posLable.width())
            self.animation1.setEndValue(0)
            self.animation1.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation1.start()
            self.ui.posLable.setText("")
            self.ui.posLable_2.setText("")
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

        #Создание пути для каждого из возможных файлов ассоциирующихся с названием {name}
        pathToMacro = os.path.abspath(f"../O-Hands/Compiled/{name}.py")
        pathToManual = os.path.abspath(f"../O-Hands/{name}.manual")

        #Проверка на существование подобного "manual" файла
        if os.path.exists(pathToManual):

            if not os.path.exists(pathToMacro):
                self.showPopUp("Запуск прерван", "Макрос имеет ошибки, исправь их :)")
                return
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
            
            #вызов подпроцесса, присвоенного чему-либо не вызывает исключение, except никогда не сработает
            #Я ебло
            
            #Неудача означает, что manual файл существует, но его скомплированная версия - нет
                self.showPopUp("Ой...", "Макроса не может быть запущен или он не существует.\nПересоздайте его.")
        else:

            #Файла просто не существует
            self.showPopUp("Ой...", "Макроса с таким названием не существует")

    #Используя BaseConstruct изменить скрипт
    def ChangeScript(self, filename):
        global current_edited
        if filename == None:
            self.showPopUp("Ой...","Макрос не выбран")
            return
        else:
            source = os.path.abspath(f"../O-Hands/{filename}.manual")
            temp = self.ui.codeRewriteEditor.toPlainText()
            File = codecs.open(source, 'r', encoding="utf-8")
            BeforeTheChange = File.read()
            File.close()
            File = codecs.open(source, 'w', encoding="utf-8")
            File.write(u"{temp}".format(temp = temp))
            File.write("\n")
            File.close()
            baseconstructing(source, filename)
            source = os.path.abspath(f"../compiled/Compiling.report")
            File = open(source, 'r')
            Checker= File.readline()
            if Checker == "!KS or HK is not defined":
                self.showPopUp("Сохранено, но...", "KS или HK не определены")
            elif Checker == "!Mode is not defined":
                self.showPopUp("Сохранено, но...", "Режим работы не определен")
            elif Checker == "!Cannot be compiled":
                self.showPopUp("Сохранено, но...", "В коде пристуствуют синтаксические ошибки\nCкрипт не может быть скомпилирован")
            elif Checker == "!Symbol in HK or KS":
                self.showPopUp("Сохранено, но...", "Использован зарезервированный символ в HK или KS")
            elif Checker == "!Symbol in send":
                self.showPopUp("Сохранено, но...", "Использован зарезервированный символ в командах")
            elif Checker == "!No Quotes":
                self.showPopUp("Сохранено, но...", "Cимвольные или строчные значения\n отсуствуют или не обернуты в ковычки")
            elif Checker == "!Mouse TypeError":
                self.showPopUp("Сохранено, но...", "Неправильный аргумент в команде(ах) с мышью")
            elif Checker == "Successful:)":
                    self.DBManager.change(filename, BeforeTheChange, temp)
                    self.showPopUp("Отлично!", "Макрос успешно перезаписан")
                    self.ui.codeRewriteEditor.clear()
                    self.ui.ChosenFileLableSEMEN.setText(f"")
                    self.ui.ChosenFileLableIsOpen.setText(f"")
                    current_edited = None

            File.close()

    # Используя BaseConstruct создать скрипт
    def CreateScript(self, filename):
        global current_edited, isRedacted
        if filename == "":
            self.showPopUp("Ой...", "Имя скрипта не указано")
            return
        else:
            source = os.path.abspath(f"../O-Hands/{filename}.manual")
            temp = self.ui.codeEditor.toPlainText()
            File = codecs.open(source, 'w', encoding="utf-8")
            File.write(u"{temp}".format(temp = temp))
            File.write("\n")
            File.close()
            baseconstructing(source, filename)
            source = os.path.abspath(f"../compiled/Compiling.report")
            File = open(source, 'r')
            Checker= File.readline()
            if Checker == "!KS or HK is not defined":
                self.showPopUp("Сохранено, но...", "KS или HK не определены")
            elif Checker == "!Mode is not defined":
                self.showPopUp("Сохранено, но...", "Режим работы не определен")
            elif Checker == "!Cannot be compiled":
                self.showPopUp("Сохранено, но...", "В коде пристуствуют синтаксические ошибки\nCкрипт не может быть скомпилирован")
            elif Checker == "!Symbol in HK or KS":
                self.showPopUp("Сохранено, но...", "Использован зарезервированный символ в HK или KS")
            elif Checker == "!Symbol in send":
                self.showPopUp("Сохранено, но...", "Использован зарезервированный символ в командах")
            elif Checker == "!No Quotes":
                self.showPopUp("Сохранено, но...", "Cимвольные или строчные значения\n отсуствуют или не обернуты в ковычки")
            elif Checker == "Successful:)":
                self.DBManager.action(f"Создал {self.ui.nameLine.text()}")
                self.showPopUp("Отлично!", "Макрос готов к использованию")
                self.ui.codeEditor.clear()
                self.ui.nameLine.clear()
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


    def closeEvent(self, event):
        self.closeOverridingHand()
        event.accept()
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




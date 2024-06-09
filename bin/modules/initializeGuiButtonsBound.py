import os

import urllib
import subprocess
import keyboard
import mouse
from PySide2 import QtCore, QtWidgets, QtGui
from ReCode import baseconstructing
import codecs
from ui_interface import *
from ui_Dialog import *

def BoundGuiButtons(self):


    # Присваивание функций ко всем кнопкам на GUI
    # ////////////////////////////////////////////////////////////////////////////////////////////
    self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())
    self.ui.introBut.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.intro))
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
    self.ui.settingsBut.clicked.connect(lambda: [self.ui.stackedWidget_2.setCurrentWidget(self.ui.settingsTitle),
                                                 self.ui.stackedWidget.setCurrentWidget(self.ui.settingsPage)])
    self.ui.PanicButBut.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.panicButtpnSettings))
    self.ui.DMSBUT.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.DMSsettings))
    self.ui.DeprecationBut.clicked.connect(
        lambda: self.showPopUp("Не-а", "Лишь для опытных пользователей\nАктивируйте режим отладки"))
    self.ui.gitHubBut.clicked.connect(lambda: os.system("start \"\" https://github.com/DraSolace/Overriding-Handv1.1"))
    self.ui.oneRepeatIssueButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.oneRepeatIssue))
    self.ui.DMSaccept.clicked.connect(lambda: self.rebindPBorDMS(False))
    self.ui.PanicButAccept.clicked.connect(lambda: self.rebindPBorDMS(True))
    self.ui.testButton.clicked.connect(lambda: [self.buttonTest()])
    self.ui.editScriptButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.editScript))
    self.ui.posButton.clicked.connect(lambda: self.showPos())
    self.ui.posButton_2.clicked.connect(lambda: self.showPos())
    self.ui.WhereIsBut.clicked.connect(lambda: os.startfile(os.path.abspath(f"/")))
    self.ui.existingScriptsBut.clicked.connect(
        lambda: [self.ui.stackedWidget.setCurrentWidget(self.ui.ExistingScript), self.updateExistingScripts()])
    self.ui.createButton.clicked.connect(lambda: self.CreateScript(self.ui.nameLine.text()))


    self.ui.quickUseButton.clicked.connect(lambda: [self.usemacro(self.ui.quickUse.text())])

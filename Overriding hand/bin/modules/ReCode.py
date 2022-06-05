# coding=utf-8
# -*- coding: utf-8 -*
import os.path
import ast
import time
import codecs
global HotKey, KillSwitch, Delay, Repeats, mode, HKflag, KSflag
def baseconstructing(source, name):
    '''
    "source" - адрес с исходным "кодом" макроса
    "name" - название файла, что будет сделан по итогу
    (TM)ToggleMode; (PM)PressMode; (RM)RepeatMode
    (!!!THM!!!)ThreadMode; - Кривой, полурабочий
    '''

    #Ебаный костыль, открытие файла в начале и поиск всех кейвордов
    sourceFile = codecs.open(source, 'r',encoding="utf-8")
    readed = sourceFile.readlines()
    file = open("uni.cfg", "r")
    lines = file.readlines()
    file.close()
    Symbols = ['[', ']', '-', '{', '}', '*']
    Symbols.append((lines[0])[:-1])
    Symbols.append((lines[1])[:-1])
    def findall():
        global HotKey, KillSwitch, Delay, Repeats, mode, HKFlag, KSFlag
        #даже если delay с repeats не будут найдены, у них должно быть дефолтное значение
        SymbolFlag = True
        DelayFlag = True
        RepeatFlag = True
        HKFlag = True
        KSFlag = True
        ModeFlag = True
        for each in readed:

            if (each.find("HK") != -1):
                HotKey = (each.replace("HK ", ""))
                HKFlag = False
                for symbol in Symbols:
                    if (each.find(f"{symbol}") != -1):
                        SymbolFlag = False
            if (each.find("KS") != -1):
                KillSwitch = (each.replace("KS ", ""))
                KSFlag = False
                for symbol in Symbols:
                    if (each.find(f"{symbol}") != -1):
                        SymbolFlag = False
            if (each.find("ToggleMode") != -1):
                mode = "TM"
                ModeFlag = False
            elif (each.find("PressMode") != -1):
                mode = "PM"
                ModeFlag = False
            elif (each.find("RepeatMode") != -1):
                mode = "RM"
                ModeFlag = False
            if (each.find("Repeats") != -1):
                Repeats = (each.replace("Repeats ", ""))
                RepeatFlag = False
            if (each.find("Delay") != -1):
                Delay = (each.replace("Delay ", ""))
                DelayFlag = False
        if(DelayFlag):
            Delay = "1"
        if(RepeatFlag):
            Repeats = "1"
        if HKFlag == True or KSFlag == True:
            return("HKKS")
        if ModeFlag == True:
            return("mode")
        if SymbolFlag == False:
            return("symbol")
        return(0)

    pizdec = os.path.abspath(f"../compiled/Compiling.report")
    ReportFile = open(pizdec, 'w',encoding="utf-8")
    returnedValue = findall()
    if returnedValue == "HKKS":
        ReportFile.write("!KS or HK is not defined")
        ReportFile.close()
        sourceFile.close()
        os.remove(os.path.abspath(f"../O-Hands/{name}.manual"))
        return("No KS or HK")
    elif returnedValue == "mode":
        ReportFile.write("!Mode is not defined")
        ReportFile.close()
        sourceFile.close()
        os.remove(os.path.abspath(f"../O-Hands/{name}.manual"))
        return("Mode is not defined")
    elif returnedValue == "symbol":
        ReportFile.write("!Symbol in HK or KS")
        ReportFile.close()
        sourceFile.close()
        os.remove(os.path.abspath(f"../O-Hands/{name}.manual"))
        return ("Symbol in HK or KS")
    else:
        ReportFile.write("Successful:)")
        ReportFile.close()

    #Поиск нужных шаблонов
    if(mode == "TM"):
        template = os.path.abspath("../compiled/Templates/TM.manual")
        eoftemplate = os.path.abspath("../compiled/Templates/EOFTM.manual")
    elif (mode == "PM"):
        template = os.path.abspath("../compiled/Templates/PM.manual")
        eoftemplate = os.path.abspath("../compiled/Templates/EOFPM.manual")
    elif (mode == "RM"):
        template = os.path.abspath("../compiled/Templates/RM.manual")
        eoftemplate = os.path.abspath("../compiled/Templates/EOFRM.manual")

    #Создание пути макроса
    AbPathToMacro = os.path.abspath(f"../O-Hands/Compiled/{name}.py")

    #Открытие (создание, в случае макроса) каждого файла
    macroFile = open(AbPathToMacro, 'w+')
    templateFile = open(template, 'r')
    eoftemplateFile = open(eoftemplate, 'r')
    sourceFile = open(source, 'r', encoding="utf-8")

    #Перенос первичного шаблона в макрос и его закрытие
    readed = templateFile.readlines()
    for each in readed:
        macroFile.write(each)
    templateFile.close()

    #И вновь, чтение файла с исходным кодом, самый пиздец лишь начинается ;)
    readed = sourceFile.readlines()

    macroFile.write('\n')
    #Самая хуёвая часть - так называемая '""ИНТРЕПРИТАЦИЯ\КОМПИЛЯЦИЯ""', в  Ж И Р Н Ю Щ И Х  ковычках
    SymbolFlag = True
    for each in readed:
        if (each.find("send") != -1):
            for symbol in Symbols:
                if (each.find(f"\"{symbol}\"") != -1):
                    SymbolFlag = False
                    break
            macroFile.write((each.replace("send", "\n\t\t\t\t\tkeyboard.send")))
        if (each.find("write") != -1):
            macroFile.write((each.replace("write", "\n\t\t\t\t\tkeyboard.write")))
        if (each.find("kpress") != -1):
            macroFile.write((each.replace("kpress", "\n\t\t\t\t\tkeyboard.press")))
        if (each.find("krelease") != -1):
            macroFile.write((each.replace("krelease", "\n\t\t\t\t\tkeyboard.release")))
        if (each.find("move") != -1):
            macroFile.write((each.replace("move", "\n\t\t\t\t\tmouse.move")))
        if (each.find("drag") != -1):
            macroFile.write((each.replace("drag", "\n\t\t\t\t\tmouse.drag")))
        if (each.find("click") != -1):
            macroFile.write((each.replace("click", "\n\t\t\t\t\tmouse.click")))
        if (each.find("dclick") != -1):
            macroFile.write((each.replace("dclick", "\n\t\t\t\t\tmouse.double_click")))
        if (each.find("wheel") != -1):
            macroFile.write((each.replace("wheel", "\n\t\t\t\t\tmouse.wheel")))
        if (each.find("mpress") != -1):
            macroFile.write((each.replace("mpress", "\n\t\t\t\t\tmouse.press")))
        if (each.find("mrelease") != -1):
            macroFile.write((each.replace("mrelease", "\n\t\t\t\t\tmouse.release")))
        if (each.find("wait") != -1):
            macroFile.write((each.replace("wait", "\n\t\t\t\t\ttime.sleep")))
    sourceFile.close()

    if SymbolFlag == False:
        ReportFile = open(pizdec, 'w', encoding="utf-8")
        ReportFile.write("!Symbol in send")
        ReportFile.close()
        sourceFile.close()
        os.remove(os.path.abspath(f"../O-Hands/{name}.manual"))
        ReportFile.close
        return ("Symbol in send")
    #Вставка второй части шаблона
    readed = eoftemplateFile.readlines()
    for each in readed:
        macroFile.write(each)
    eoftemplateFile.close()

    #Замена всех переменных на реальные
    macroFile.close()
    macroFile = open(AbPathToMacro, "r")
    readed = macroFile.read()
    macroFile.close()



    readed = readed.replace("Pos(x)", f"mouse.get_position()[0]")
    readed = readed.replace("Pos(y)", f"mouse.get_position()[1]")
    readed = readed.replace("Abs", f"True")
    readed = readed.replace("Add", f"False")
    readed = readed.replace("KS", f"{KillSwitch[:-1]}")
    readed = readed.replace("HK", f"{HotKey[:-1]}")
    print(Delay)
    readed = readed.replace("Delay", f"{Delay}")
    readed = readed.replace("Repeats", f"{Repeats}")
    macroFile = open(AbPathToMacro, "w")
    macroFile.write(readed)
    macroFile.close()


    with open(AbPathToMacro) as f:
        source = f.read()
    valid = True
    try:
        ast.parse(source)
    except SyntaxError:
        valid = False

    if valid == True:
        return 0;
    else:
        pizdec = os.path.abspath(f"../compiled/Compiling.report")
        ReportFile = open(pizdec, 'w', encoding="utf-8")
        ReportFile.write("!Cannot be compiled")
        pizdec = os.path.abspath(f"../O-Hands/Compiled/{name}.py")
        os.remove(os.path.abspath(f"../O-Hands/{name}.manual"))
        os.remove(pizdec)
        ReportFile.close()
    f.close()







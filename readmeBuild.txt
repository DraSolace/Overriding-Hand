Является portable

Для сборки билда при помощи pyinstaller, в файле setup.xlkm скопируйте вторую строчку и исполните её в папке modules
Потом вытащите main.exe из папки dist и переместити в modules. main.exe - рабочий Overriding hand

(необязательно)
Что бы вытащить ярлык Overriding hand в любое другое место, выполните ту же самую строчку в папке modules, но не с main.py а с RecreateItself.py
Вытащите из dist, поместите в папку modules, нажмите ПКМ по RecreateItself.exe -> создать ярлык. Этот ярлык может быть помещен где угодно.
Даже если переместить директорию с Overriding hand, ярлык будет исправно работать.

в setup.xlkm так же перечислены все необходимые библиотеки для работы Overriding hand


Уже собраный билд: https://drive.google.com/file/d/1CMnqu5KiroXd8gDOk9xb_gy4mtlYaOH-/view?usp=sharing
# В процессе импорта модуля, он исполняется целиком. А те имена, которые останутся в пространстве имен, связанные с
# исполнением этого модуля, мы затем сможем использовать. Они доступны в качестве атрибутов импортируемого модуля.
# Внутри модуля всегда доступно глобальное имя __name__. Оно показывает текущее имя модуля.
# Когда модуль запускается с помощью интерпретатора, он носит имя __main__
# Если же модуль импортируется, то __name__ будет содержать название самого модуля.
# def fib(k):
#     if k ==0 or k ==1:
#         return 1
#     else:
#         return fib(k - 1) + fib(k - 2)
# if __name__ == '__main__':
#     print(__name__)
#     print(fib(31))
# если запускать модуль - выполнится все. Если импортировать - выполнится до if __name__ == '__main__'
# Исполнения модуля происходит только при первом его импорте. Если повторно вызвать импорт этого модуля, то он не будет
# заново исполнен, а будут переиспользованы старые объекты нашего модуля.
# Имена модулей хранятся в словаре sys.modules
# Если интерпретатор не находит запрашиваемого модуля в словаре sys.modules, он будет искать его в папках, указанных
# в списке sys.path
# import sys
# print(type(sys.modules))
# print(sys.modules)
# Если интерпретатор не находит запрашиваемого модуля в словаре sys.modules, он будет искать его в папках, указанных в
# списке sys.path
# import sys
# for path in sys.path:
#     print(path)
# Сначала он ищет в локальной директории модуля. Затем перебирает внешние библиотеки.
# В PyCharm мы можем тоже увидеть все библиотеки Python:
# В библиотеке Python39 содержатся модули, которые являются стандартной библиотекой языка Python.
# В свою очередь, библиотека site-packages содержит в себе модули, которые являются дополнительно установленными.
# Внутри библиотеки почти все модули представлены папками. Они называются пакеты.
# Пакет - это удобный способ представления некоторого числа файлов в качестве одного модуля. Пакеты тоже могут вести себя
# как модули, которые тоже можно импортировать.
# Интерпретатор умеет определять по папке является ли она пакетом по наличию файла __init__.py внутри: Именно этот файл
# исполняется при импорте.  в папке-пакете может быть больше модулей, чем указано в ините, например незавершённые
# разработки. и они не импортируются. при импорте интерпретатор прочтет файл инит и возьмёт только то, что указано в
# нем, а остальное пропустит.
# Также мы можем импортировать не весь модуль целиком, а только определенные имена из него
# Если в данном модуле уже существует функция с аналогичным именем, произойдет следующее (пример на скрине ниже):
# ●	сначала мы в локальное имя greet записываем функцию из модуля exceptions
# ●	затем, когда мы определяем функцию greet() внутри своего файла, то мы перезаписываем это локальное имя
# Таким образом, мы теряем ссылку на функцию из модуля exceptions
# from exception import BadName, greet
# def greet();
#     pass
# greet()
# Для того, чтобы это избежать, мы можем явно указать то локальное имя, которое мы бы хотели использовать. Мы можем даже
# импортировать целиком модуль, используя для него другое локальное имя:
# from exception import BadName as bad, greet as exc_greet
# import exception as exc
# def greet();
#     pass
# greet()
# В языке Python возможно импортировать все имена из какого-либо модуля. Для этого достаточно использовать *
# Однако, такая практика не рекомендуется. Так как если модуль большой и в нем много имен, то какие-то из них могут
# пересекаться с теми, которые вы используете.
# При этом в самом модуле с помощью конструкции __all__ можно явно указать какие имена будут импортироваться, если
# использовать *
# GREETING = 'Hello'
# class BadName(Exception):
#     pass
# def greet(name):
#     if name[0].isupper():
#         return GREETING + name
#     else:
#         raise BadName(name + ' error')
# __all__ = ['BadName', 'greet']
# Также не будут импортироваться любые имена, начинающиеся с нижнего подчеркивания _ - _GREETING
# Python Package Index
# https://pypi.org/
# https://docs.python.org/3.5/distutils/packageindex.html

# Значит при втором и последующих импортах не удастся произвести импорт других функций этого модуля, т.к. sys.modules уже
# будет содержаться наш импортируемый модуль после первого импорта?
# Не совсем. Если второй импорт делать вида "import mymodule",  то код модуля выполнен не будет и все НЕ импортированные
# до этого функции действительно не будут импортированы, однако если второй импорт будет иметь вид
# "from mymodule import bar", тогда bar станет доступна, хотя код всего модуля исполнен так же не будет.

# Подскажите пожалуйста, чем отличается import exceptions от from exceptions import * ?
# Да ничем по сути, единственное что когда вы импортируете всё со звёздочкой - у вас импортируются все имена из модуля
# (который импортируете) и это может приводить к конфликтам: ну например у вас есть функция с именем f, в модуле есть
# одноименная функция - возникает путаница. В общем лучше import module_name или module_name as mn (или что-то похожее)
# и потом пользоваться через точку ну или from module_name import f1, f2, f3 - то есть что-то конкретное, вообще вопрос
# вкуса/удобства, но на мой взгляд - так читабельнее и меньше потенциальных багов


# Алиса зашифровала свою информацию с помощью библиотеки simple-crypt. Она представила информацию в виде строки,
# и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.
# Вам необходимо установить библиотеку simple-crypt при установке - внизу поставить галочку options с "--no-deps" (для
# работы этого модуля установите модуль pycryptodome), и с помощью метода simplecrypt.decrypt узнать, какой из паролей
# служит ключом для расшифровки файла с интересной информацией.
#
# from simplecrypt import decrypt, DecryptionException
#
# with open("D:\\encrypted.bin", "rb") as inp:
#     encrypted = inp.read().strip()
# with open("D:\\passwords.txt", "r") as inf:
#     passwords = inf.read().strip().split('\n')
#
# for password in passwords:
#     try:
#         print(decrypt(password, encrypted).decode('utf8'))
#         break
#     except DecryptionException:
#         continue
#
# encrypted = open("encrypted.bin", "rb").read()
# passwords = open("passwords.txt").readlines()
# for p in passwords:
#     p = p.strip()
#     try:
#         s = simplecrypt.decrypt(p, encrypted)
#     except simplecrypt.DecryptionException:
#         continue
#     print(s.decode("utf-8"))
#
# import os
# import urllib.request
# from multiprocessing import Process
#
# import simplecrypt
#
# def decryptor(passw,text):
#     try:
#         print("Пробуем " + passw)
#         result = simplecrypt.decrypt(passw.strip(), text)
#         proc = os.getpid()
#         print('Пароль {0} подошел. Результат: {1}. id процесса: {2}'.format(
#             passw, result, proc))
#     except:
#         print(passw + " Не подошел :(")
#
# urllib.request.urlretrieve('https://stepik.org/media/attachments/lesson/24466/encrypted.bin', 'encrypted.bin')
# urllib.request.urlretrieve("https://stepik.org/media/attachments/lesson/24466/passwords.txt", 'passwords.txt')
#
# if __name__ == '__main__':
#     encrypted = ""
#     with open("encrypted.bin", "rb") as inp:
#         encrypted = inp.read()
#
#     with open('passwords.txt') as f:
#         lineList = f.readlines()
#         procs = []
#
#         for i in lineList:
#             proc = Process(target=decryptor, args=(i.strip(), encrypted,))
#             procs.append(proc)
#             proc.start()
#
#         for proc in procs:
#             proc.join()

# bkl = urllib.request.urlopen('https://stepic.org/media/attachments/lesson/24466/encrypted.bin').read()
# passwords = urllib.request.urlopen('https://stepic.org/media/attachments/lesson/24466/passwords.txt').read().strip().split()
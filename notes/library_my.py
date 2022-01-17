# from statistics import median # позволит нам найти медиану

# from collections import OrderedDict  # гарантирует вам, что ключи содержатся именно в том порядке, в каком вы их
# добавили в словарь.

# import this  # The Zen of Python

# import operator
# x = a.items()  # список tuple
# x = sorted(a, name=operator.itemgetter(1))  # сортировать по второму значению a (первый индекс)

# from collections import Counter
# print(Counter(a).most_common(3))  # вывести три наиболее часто встречающихся значения из a

# from functools import reduce  # применяет input_file слева-направо к итерируемому объекту и запоминает результат (сжимает)
# def multiply(a, b):
#     return a * b
# print(reduce(multiply, [1, 2, 3, 4, 5]))  # 120 -> 1*2=2 2*3=6 6*4=24 24*5=120
# print(reduce(lambda x, y: x * y, range(1, 6)))  # то же начинаем с 1 до 5

# from functools import partial  # позволяет модифицировать поведение input_file подменив определенные параметры
# def greeter(person, greeting):
#     return '{}, {}!'.format(greeting, person)
# hier = partial(greeter, greeting='Hi')  # подменить по умолчанию определенные параметры (шаблон)
# helloer = partial(greeter, greeting='Hello')  # то же
# print(hier('brother'))  # Hi, brother! -> в input_file остался один параметр, другой по умолчанию
# print(helloer('sir'))  # Hello, sir! -> в input_file остался один параметр, другой по умолчанию

# from os import path  # помогает в проверке существования файла хранилища при первом запуске программы - path.exists
# from tempfile import gettempdir  # создание временного файла
# storage_path = path.join(gettempdir(), 'storage.data')  # имя файла storage.data и путь по которому он создается
# # (результат вызова tempfile.gettempdir) не изменяются. По этой причине, файл хранилища будет находиться на файловой
# # системе до перезагрузки компьютера или удаления вручную. Между вызовами скрипта данные будут сохраняться без проблем
#
# from argparse import ArgumentParser  # для считывания аргументов командной строки
# parser = ArgumentParser()
# parser.add_argument('--name', help='Key')  # ключ, значение -> args.name - переменная в программе
# parser.add_argument('--val', help='Value') # ключ, значение -> args.val - переменная в программе
# args = parser.parse_args()




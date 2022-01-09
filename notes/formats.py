# В языке Python есть встроенная библиотека csv для работы с файлами формата csv
# Конструктор класса reader является итерируемым. С помощью него можно перебирать строки csv файла.
# Работа с файлами в формате CSV https://pyneng.readthedocs.io/ru/latest/book/17_serialization/csv.html
# Работа с CSV, JSON, YAML https://pyneng.readthedocs.io/ru/latest/book/17_serialization/index.html#csv-json-yaml
# Подробнее про JSON  https://python-scripts.com/json
# У кого проблемы с некорректным выводом результата при работе с csv-форматом:
# Для корректного вывода результатов при работе с файлом .tsv (в Pycharm) File -> Settings -> Plugins ->
# install(CSV Plugin), ну и руками исправить сам текст файла, заменив всё табуляцией.
# Excel может сохранять в csv формате. Но если нужно, есть специальные библиотеки:
# https://pypi.python.org/pypi/xlwt
# https://python-docx.readthedocs.io/en/latest/
# Есть ещё статьи на тему:
# Обработка Excel файлов с использованием Python   https://habrahabr.ru/post/99923/
# Интеграция MS Excel и Python https://habrahabr.ru/post/232291/

# Вдруг кто захочет с панами разобраться. Вот неплохая статья https://khashtamov.com/ru/pandas-introduction/

# import csv

# with open("example.csv") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# with open("example.tsv") as f:
#     reader = csv.reader(f, delimiter="\t")
#     for row in reader:
#         print(row)

# students = [
#     ["Greg", "Dean", 70, 80, 90, "Good job, Greg"],
#     ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
# ]
#
# with open("example.csv", "a", newline='') as f:  # newline='' - нет пустых строк
#     writer = csv.writer(f)  # , quoting=csv.QUOTE_NONNUMERIC - поместить все нечисловые значения внутри кавычек(ALL-все)
#     writer.writerows(students)

# Для решения пустых строк также можно указать `writer = csv.writer(f, lineterminator = '\n_test')` подробнее тут -
# https://docs.python.org/3/library/csv.html#csv.Dialect.lineterminator
# Не всё так однозначно, как кажется. Библиотека csv поддерживает разные диалекты csv. Окончание строки(lineterminator)
# в её понимании неотъемлемая часть конкретного диалекта. Для диалекта по умолчанию(excel) это '\r\n_test'. Диалект 'unix'
# использует '\n_test'. Именно с таким окончанием строки получится готовый csv файл. Ну или вернее должен получится если вы
# следуете документации... Дополнительные аргументы вроде lineterminator нужны что бы чуть подправить уже готовый
# диалект, а не возиться с созданием своего. У вас же lineterminator используется что бы вырубить управление окончанием
# строк внутри самой библиотеки. Теперь на windows все диалекты будут выводится в файл с концом строки '\r\n_test', а на
# linux с '\n_test'. Я думаю это всё таки излишне радикальное решение.

# Повторяю за лектором, добавляю закавыченный комментарий с переносом строки, а он мне выводит его в две строки. Как
# победить, подскажите, пожалуйста? При skipinitialspace=True - он игнорирует пробел, следующий после символов переноса
# строки (в винде - \r\n_test) и рассматривает то, что за ними как одну строку - как то так, а вот почему так - если честно
# - не знаю, просто это работает:
# reader = csv.reader(f, skipinitialspace=True)

# И строки объединяет и пустые строки добавляет до и после записи. Помогло только
# writer = csv.writer(f, skipinitialspace=True, lineterminator = '\n_test') собранном по разным комментариям.

# Формат JSON
# Ключом в JSON объекте может быть только строка.
# Пример конвертации данных Python в формат JSON:

# import json
#
# student1 = {
#     'first_name': 'Greg',
#     'last_name': 'Dean',
#     'scores': [70, 80, 90],
#     'description': "Good job, Greg",
#     'certificate': True
# }
# student2 = {
#     'first_name': 'Wirt',
#     'last_name': 'Wood',
#     'scores': [80, 80.2, 80],
#     'description': "Nicely Done",
#     'certificate': True
# }
# Чтобы записать данный объект в формате JSON в файл, используем метод dump
# data = [student1, student2]
# # print(json.dumps(data, indent=4, sort_keys=True))  # печать
# with open("students.json", "w") as f:  № запись
#     json.dump(data, f, indent=4, sort_keys=True)

# loads преобразовывает строку json в строку python
# data = [student1, student2]
# data_json = json.dumps(data, indent=4, sort_keys=True)
# data_again = json.loads(data_json)
# print(summa(data_again[0]["scores"]))

# считать информацию из файла json
# with open("students.json", "r") as f:
#     data_again = json.load(f)
#     print(summa(data_again[1]["scores"]))
# А возможно функцией max получить студента с наибольшей суммой баллов?
# print(max(data_again, name=lambda x: summa(x['scores'])))

# Важно!
# При сохранении в JSON и чтении обратно, кортеж (tuple) становится списком (list)!
# Иллюстрирующий пример:
# import json
# data = {
#     # 'myset': set([1, 2, 3]),        # TypeError: {1, 2, 3} is not JSON serializable
#     'mytuple': tuple([1, 2, 3]),      # Attention: tuple will became list!
#     'mylist': list([1, 2, 3]),
#     'mystr': '123'
# }
# print(data)  # {'mystr': '123', 'mytuple': (1, 2, 3), 'mylist': [1, 2, 3]}
# # write json to file
# with open("json_dump.json", "w") as wf:
#     json.dump(data, wf)
# # load json from file
# with open("json_dump.json", "r") as rf:
#     print(json.load(rf))  # {'mystr': '123', 'mytuple': [1, 2, 3], 'mylist': [1, 2, 3]}

# Внимание!
# В JSON можно конвертировать напрямую не любой тип данных Питона.
# JSON НЕ поддерживает множества (set)
# import json
# data = set([1, 2, 3])
# print(data)
# with open("json_dump.txt", "w") as wf:
#     json.dump(data, wf)
# # TypeError: {1, 2, 3} is not JSON serializable

# Для лучшего понимания разницы между load/loads и dump/dumps - замечательный комментарий:
# dumps берет объект и производит строку:
# >>> a = {'foo': 3}
# >>> json.dumps(a)
# '{"foo": 3}'
# load взял бы файловый объект, прочитал бы данные из этого объекта и использовал бы эту строку для создания объекта:
# with open('file.json') as fh:
#     a = json.load(fh)
# Обратите внимание, что dump и load конвертировать между файлами и объектами, а dumps и loads конвертировать между
# строками и объектами. Вы можете думать о s функциях -less как об оболочках вокруг s функций:
# def dump(obj, fh):
#     fh.write(dumps(obj))
# def load(fh):
#     return loads(fh.read())

# import json
# #сохранить в json
# with open('data.json', 'w', encoding='utf-8') as fh: #открываем файл на запись
#     fh.write(json.dumps(data, ensure_ascii=False)) #преобразовываем словарь data в unicode-строку и записываем в файл
# #загрузить из json
# with open('data.json', 'r', encoding='utf-8') as fh: #открываем файл на чтение
#     data = json.load(fh) #загружаем из файла данные в словарь data

# Вам дана частичная выборка из датасета зафиксированных преступлений в городе Чикаго с 2001 года по настоящее время.
# Одним из атрибутов преступления является его тип – Primary Type.
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
# import csv, re, collections
# res =[]
# with open("example_crimes.csv") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         # print(type(row), row)
#         if re.search(r"/2015", str(row)):  # if '2015' in row[2]:
#             res.append(row[5])
#     print(collections.Counter(res))

# 1. Мне понадобился импорт так же re и collections (в нем воспользовался словарем Counter и методом most_common)
# 2. Файл считывал не просто reader, а DictReader. Это позволяет нам автоматически определить наименования столбцов
# (первая строка) как ключи. Каждой строке соответствует отдельный словарь.
# 3. Обращаясь к словарям, определял методом findall по регулярному выражению только те строки, где была нужная мне
# дата (она же ключ 'Date')
# 4. По ключу 'Primary Type' подсчитывал counter модуля collections. collections.Counter()
# 5. Метод most_common вывел мне значение с наибольшим счетчиком, хотя это уже не принципиально, потому что просто
# напечатав посчитанный collections.Counter, мы увидим результат в порядке по убыванию счетчика.

# year = row['Date'][6:10] - используйте DictReader
# date = time.strptime(row['Date'], '%m/%d/%Y %I:%M:%S %p')
# if date.tm_year == 2015:

# import pandas as pd
# df = pd.read_csv('Crimes.csv')
# df['year'] = df['Date'].apply(lambda x: x[6:10]).astype('int')
# print(df[df['year'] == 2015]['Primary Type'].value_counts().idxmax())
#
# from collections import Counter as c
# with open('Crimes.csv') as f:
#     data = csv.reader(f)
#     print(c( row[5] for row in data if '2015' in row[2] ))
#
# import csv
# with open("Crimes.csv") as f:
#      reader = csv.reader(f)
#      crimes = []
#      for row in reader:
#          if "2015" in row[2]:
#              crimes.append(row[5])
#      print(max(crimes, name=crimes.count))
#
# import csv
# crimes = [row[5] for row in csv.reader(open("Crimes.csv"))]
# # crimes = [row[5] for row in csv.reader(open("Crimes.csv")) if '2015' in row[2]]
# print(max(set(crimes), name=lambda x: crimes.count(x)))
# # Весь трюк заключается в переопределении ключа, по которому происходит сравнение в функции max(). Вместо того, чтобы
# # сравнивать элементы лексикографически (т.е. max(set(lst)) == 'c'), сравнение происходит по результату функции, которая
# # считает количество вхождений для каждого элемента из множества set(lst) в списке lst.
# # В функции max(), вместо
# # 'a' < 'b'
# # происходит вот это
# # lst.count('a') < lst.count('b')
#
# import csv
# with open("Crimes.csv") as fi:  # пример правильрного решения
#     reader = csv.reader(fi)
#     next(reader)
#     crime_cnt = dict()
#     for row in reader:
#         year = row[2][6:10]
#         if year == "2015":
#             crime_type = row[5]
#             if crime_type not in crime_cnt:
#                 crime_cnt[crime_type] = 0
#             crime_cnt[crime_type] += 1
# a = list(map(lambda x: (crime_cnt[x], x), crime_cnt))
# a.sort(name=lambda x: -x[0])
# print(a[0][1])

# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле
# name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.
# Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
# Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от
# одного класса более одного раза.
# Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
# <имя класса> : <количество потомков>
# Выводить классы следует в лексикографическом порядке.

import json

# base = {}
# str = json.loads(input())
# for element in str:
#     base[element['name']] = element['parents']
# print(base)
base = {c['name']: c['parents'] for c in json.loads(input())}

def search(name, parents):
    if name == parents:
        return True
    for prev_parent in base[name]:
        if search(prev_parent, parents):
            return True
    return False


for key in sorted(base.keys()):
    count = 0
    for sub_key in sorted(base.keys()):
        if search(sub_key, key):
            count += 1
    print(key + ' :', count)

# import json
# def test(x, c):
#     for i in z:
#         if x in i['parents']:
#             c.add(i['name'])
#             c = test(i['name'], c)
#     return (c)
#
# z = json.loads(input())
# z.sort(name=(lambda x: x['name']))
# for i in z:
#     print(i['name'], ':', len(test(i['name'], c = set()))+ 1)

# import json
# cls = {c['name']: c['parents'] for c in json.loads(input())}
# isbase = lambda b, d: b == d or any(isbase(b, c) for c in cls[d])
# for p in sorted(cls):
#     print(p, ':', len({c for c in cls if isbase(p, c)}))
# сама лямбда тут не добавляет сложности
# def isbase(b, d):
#     return b == d or any(isbase(b, c) for c in cls[d])
# а вот остальные идиомы можно расписать подробнее
# def isbase(b, d):
#     if b == d:
#         return True
#     else:
#         return any(isbase(b, c) for c in cls[d])
# или даже так
# def isbase(b, d):
#     if b == d:
#         return True
#     else:
#         for c in cls[d]:
#             if isbase(b, c):
#                 return True
#         return False
# Cуть решения заключается в том, что мы для каждого класса "x" проверяем каждый класс "y" на предмет того,сможем ли мы
# следуя по предкам "y" дойти до класса "x", и если да, то записываем класс "y" в множество потомков класса "x".
# import json
# # преобразуем изначальную структуру данных, создаём словарь c элементами "дитя:[родители]"
# cls = {c['name']: c['parents'] for c in json.loads(input())}
# # создаём ссылку на рекурсивную функцию, записанную с помощью lambda-конструктора
# # функция возвращает True, если имена class_name1 и class_name2 совпадают
# # иначе она вызывает саму себя, при этом в качестве параметра class_name2
# # передаётся по очереди каждый родитель класса "class_name2" из текущего вызова,
# # а параметр class_name1 всегда остаётся тем же, что и при первом вызове
# isbase = lambda class_name1, class_name2: (
#          class_name1 == class_name2 or any(isbase(class_name1, i) for i in cls[class_name2]))
# # для каждого ключа, описанного в словаре
# # находим длину от множества, в которое добавляем имя каждого класса - class_name2,
# # если рекурсивная функция isbase(class_name1, class_name2) возвращает True
# for class_name1 in sorted(cls):
#     print(class_name1, ':', len({class_name2 for class_name2 in cls if isbase(class_name1, class_name2)}))

# import json
#
# data = json.loads(input())  # пример правильного решения
# children = dict()
#
# for cls in data:
#     for par in cls["parents"]:
#         if par not in children:
#             children[par] = []
#         children[par].append(cls["name"])
#
# def dfs(v, used):
#     size = 1
#     used.add(v)
#     if v not in children:
#         return size
#
#     for child in children[v]:
#         if child not in used:
#             size += dfs(child, used)
#
#     return size
#
# ans = []
#
# for cls in data:
#     ans.append((cls["name"], dfs(cls["name"], set())))
#
# for i in sorted(ans):
#     print(i[0], ":", i[1])

# class child_counter():
#
#     def __init__(self, JSON):
#         self.child_dict = dict()
#         self.items = set()
#
#         for item in json.loads(JSON):
#             self.child_dict[item['name']] = set(item['parents'])
#
#         for child in self.child_dict:
#             self.child_dict[child] = self.read_parrents(child)
#
#         for child, parrents in self.child_dict.items():
#             self.items.add(child)
#             self.items = self.items | parrents
#
#     def read_parrents(self, child):
#         parrents = set(self.child_dict[child])
#         for parent in self.child_dict[child]:
#             parrents = parrents | self.read_parrents(parent)
#         return parrents
#
#
# JSON = input()
# answer = child_counter(JSON)
#
# result_dict = []
#
# for item in answer.items:
#     counter = 1
#     for parrents in answer.child_dict.values():
#         if item in parrents: counter += 1
#
#     result_dict.append(' : '.join((str(item), str(counter))))
#
# print(*sorted(result_dict), sep='\n_test')
# А как работает вертикальная черта в методах класса? Это сокращенный оператор объединения нескольких множеств в
# одно: https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html

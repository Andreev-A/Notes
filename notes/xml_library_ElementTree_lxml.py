# Отличие HTML и XML заключается в том, что HTML используется для того, чтобы данные отображать, а XML - для того,
# чтобы данные хранить.
# Элементы в XML объявляются с помощью тегов.
# Есть 2 вида тегов: парные и одиночные: <tag> ... </tag> и <tag/>
# Все что находится между парными тегами, является содержимым элемента: <tag id="1"> текст элемента </tag>
# Внутри элемента также хранятся атрибуты.
# Атрибуты - это пара ключ-значение, которые разделены символом =
# Значение хранится в кавычках.
# Атрибуты объявляются в открывающем теге.
# В XML формате мы сами придумываем себе придумываем себе формат, теги и имена для атрибутов. Важно придумывать понятные
# имена для тегов, чтобы другие люди, которые будут пользоваться этими данными в XML формате, смогли легко в нем
# разобраться.
# Предпочтительнее всего использовать понятные слова, которые хорошо раскрывают сущность тех данных, которые вы храните.
# Из-за того, что элементы в XML могут также содержать в себе другие элементы или текст, то нам проще всего отображать
# данные в XML формате с помощью деревьев.
# Формат XML требует от нас наличие выделенного корня, который содержит в себе все остальные элементы.
# Поэтому все стандартные библиотеки, которые разбирают формат XML, так или иначе хранят его в виде дерева.
#
# from xml.etree import ElementTree
#
# tree = ElementTree.parse("example.xml")
# root = tree.getroot()

# use root = ElementTree.fromstring(string_xml_data)  # из строки

# print(root)  # <Element 'studentsList' at 0x000001FF00EFE770>
# print(root.tag, root.attrib)  # studentsList {}

# Можно использовать индексацию через числа, для того, чтобы обращаться к детям и к детям детей:
# print(root[0][0].text)  # Greg

# Мы можем перебрать детей нашего корня, например, используя цикл for
# for child in root:
#     print(child.tag, child.attrib)  # student {'id': '1'}  student {'id': '2'}

# Все элементы дерева имеют один и тот же класс Element. Поэтому все имена методов и атрибутов у данных объектов будут
# одинаковые.
#
# С помощью метода iter() мы можем перебрать все элементы с заданным тегом:
# for element in root.iter("scores"):  # все элементы в поддереве, то .findall (только среди детей)
#     score_sum = 0
#     for child in element:
#         score_sum += float(child.text)
#     print(score_sum)  # 240.0  240.2
# С помощью методов Element.find() и Element.findall() можно найти дочерние элементы, принадлежащие конкретному элементу:

# Данные, хранящиеся в элементах xml можно модифицировать и затем записывать в файл с помощью метода write():
# tree.write("example_modified.xml")  # запись в файл

# greg = root[0]
# module1 = next(greg.iter("module1"))
# print(module1, module1.text)  # <Element 'module1' at 0x0000017E4AE57D60> 70 <-значение баллов для Грега в модуле 1
# module1.text = str(float(module1.text) + 30)  # измеили в модуле 1 значение с 70 на 100
# tree.write("example_modified.xml")
# При этом не забываем, что числа хранятся в xml в виде строк.

# Теперь создадим новый атрибут для элемента certificate с помощью метода set() и укажем, что тип сертификата - с отличием:
# from xml.etree import ElementTree
# tree = ElementTree.parse("example_modified.xml")
# root = tree.getroot()
# greg = root[0]
# certificate = greg[2]
# certificate.set("type", "with distinction")  # добавили в сертификат
# tree.write("example_modified.xml")

# Создадим новый элемент description для элемента greg:
# from xml.etree import ElementTree
# tree = ElementTree.parse("example_modified.xml")
# root = tree.getroot()
# greg = root[0]
# description = ElementTree.Element("description")  # создать элемент
# description.text = "Showed excellent skills during the course"  # добавить значение
# greg.append(description)
# tree.write("example_modified.xml")
# Для этого воспользуемся конструктором класса Element, который находится внутри библиотеки ElementTree. В качестве
# аргумента указываем имя тега, который мы хотим создать - "description".
# Затем у нового элемента определим текстовое значение с помощью атрибута text.
# После чего добавляем новый тег с описанием внутрь элемента greg с помощью метода append().

# С помощью метода remove() мы сможем удалить ненужный элемент:
# from xml.etree import ElementTree
# tree = ElementTree.parse("example_modified.xml")
# root = tree.getroot()
# greg = root[0]
# description = greg.find("description")  # найдем как ребенка Грега
# greg.remove(description)  # удалим
# tree.write("example_modified.xml")

# С помощью конструктора SubElement() мы легко можем создать все дерево XML документа с полного нуля. В параметрах
# SubElement() мы указываем родителя и название нового тега :
# from xml.etree import ElementTree
# root = ElementTree.Element("student")
# first_name = ElementTree.SubElement(root, "firstName")
# first_name.text = "Greg"
# second_name = ElementTree.SubElement(root, "secondName")
# second_name.text = "Dean"
# scores = ElementTree.SubElement(root, "scores")
# module1 = ElementTree.SubElement(scores, "module1")
# module1.text = "100"
# module2 = ElementTree.SubElement(scores, "module2")
# module2.text = "80"
# module3 = ElementTree.SubElement(scores, "module3")
# module3.text = "90"
# tree = ElementTree.ElementTree(root)
# tree.write("student.xml")
# На финальном шаге с помощью конструктора ElementTree() мы создаем дерево. В параметрах конструктора указываем корень
# дерева.

# print(ElementTree.ElementTree.__doc__)

# Как лучше всего (или существуют разные способы) красиво распечатать XML на Python?
# import xml.dom.minidom
# dom = xml.dom.minidom.parse(xml_fname) # or xml.dom.minidom.parseString(xml_string)
# pretty_xml_as_string = dom.toprettyxml()
#
# lxml является недавним, обновленным и включает красивую функцию печати
# import lxml.etree as etree
# x = etree.parse("filename")
# print etree.tostring(x, pretty_print=True)


# Если мы используем стандартную конструкцию шагания по итерируемому объекту, то он шагает только по невложенным
# объектам. По именам и сертификату. А вложенный объект scores не воспринимает. Не совсем так. Просто Вы во втором
# print запрашиваете text. А его нет в scores.
# for element in root:
#     print(element)
#     score_sum=0
#     for child in element:
#         print(child.tag)  # print(child.text)


# Библиотека lxml
# Первым делом импортируем из lxml библиотеку etree.
# from lxml import etree
# Это связано с тем, что библиотека lxml пытается вести себя в точности также, как встроенная в Python библиотека
# ElementTree.

# from lxml import etree
# import requests
#
# res = requests.get("https://docs.python.org/3/")
# print(res.status_code)
# print(res.headers["Content-Type"])
#
# parser = etree.HTMLParser()
# root = etree.fromstring(res.text, parser)
#
# # print(root)
# for element in root.iter("a"):
#     print(element, element.attrib)
# Именно парсер HTMLParser, который находится внутри библиотеке lxml, является той самой умной частью библиотеке lxml,
# которая отличает его от стандартной библиотеки языка Python. Он позволяет нам работать даже с данными в формате HTML,
# которые являются плохо сформированными.

# Можно было немного рассказать о xpath, который есть в lxml, например, то, что можно получить из страницы все ссылки
# из тега a с помощью такого запроса:
# for a in root.xpath('//a/@href'):
#     print(a)

# Вам дано описание пирамиды из кубиков в формате XML. Кубики могут быть трех цветов: красный (red), зеленый (green) и
# синий (blue).  Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.
# Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1.
# Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками,
# имеют ценность 3. И т. д. Ценность цвета равна сумме ценностей всех кубиков этого цвета.
# Выведите через пробел три числа: ценности красного, зеленого и синего цветов.

# from xml.etree import ElementTree
# <cube color="blue"><cube color="red"><cube color="green"><cube color="green"><cube color="green"><cube color="blue">
# </cube><cube color="green"></cube><cube color="red"></cube></cube></cube></cube></cube><cube color="red">
# <cube color="blue"></cube></cube></cube>
# root = ElementTree.fromstring(input())
# memory = {'red': 0, 'green': 0, 'blue': 0}
# count, run = 1, 'cube'
# memory[root.attrib['color']] += count
# while True:
#     count += 1
#     stop = 0
#     for element in root.findall(run):
#         stop += len(element)
#         memory[element.attrib['color']] += count
#     if not stop:
#         break
#     run = run + '/cube'
# print(memory['red'], memory['green'], memory['blue'])
# red = 10(2, 6, 2)
# green = 18(3, 4, 5, 6)
# blue = 10(1, 6, 3)
# root.findall(".//cube[@color='xxx']")  # список всех узлов cube цвета xxx любого уровня вложенности в корень
# root.findall("./cube/[@color='xxx']")           # список узлов cube 2го уровня цвета xxx
# root.findall("./cube/cube[@color='xxx']")       # список 3го уровня
# root.findall("./cube/cube/cube[@color='xxx']")  # список 4го уровня и т.д.

# from xml.etree import ElementTree
# root = ElementTree.fromstring('<cube color="blue"><cube color="red"><cube color="green"><cube color="green">'
#                               '<cube color="green"><cube color="blue"></cube><cube color="green"></cube>'
#                               '<cube color="red"></cube></cube></cube></cube></cube><cube color="red">'
#                               '<cube color="blue"></cube></cube></cube>')
# colors = {'red': 0, 'green': 0, 'blue': 0}
# def count_colors(root, count):
#     colors[root.attrib['color']] += count
#     for child in root.findall('cube'):
#         count_colors(child, count + 1)
# count_colors(root, 1)
# print(colors['red'], colors['green'], colors['blue'])
#
# import re
# x = input()
# y = re.findall(r'(red|blue|green|\/)', x)
# n_test = 0
# d = {"red":0, "green":0, "blue":0}
# for i in y:
#     if i != '/':
#         n_test += 1
#         d[i] += n_test
#     else:
#         n_test-=1
# print(d['red'], d['green'], d['blue'])

# import xml.etree.ElementTree as ET
# tree = ET.fromstring(input())  # пример правильного решения
# ans = {"red": 0, "green": 0, "blue": 0}
# def dfs(cube, res, depth):
#     res[cube.attrib["color"]] += depth
#     for i in cube.findall("cube"):
#         dfs(i, res, depth + 1)
# dfs(tree, ans, 1)
# print(ans["red"], ans["green"], ans["blue"])

##################################################################################
# from xml.etree.ElementTree import XMLParser
#
#
# class MaxDepth:  # The target object of the parser
#     maxDepth = 0
#     depth = 0
#
#     def start(self, tag, attrib):  # Called for each opening tag.
#         self.depth += 1
#         if self.depth > self.maxDepth:
#             self.maxDepth = self.depth
#
#     def end(self, tag):  # Called for each closing tag.
#         self.depth -= 1
#
#     def data(self, data):
#         pass  # We do not need to do anything with data.
#
#     def close(self):  # Called when all data has been parsed.
#         return self.maxDepth
#
# target = MaxDepth()
# parser = XMLParser(target=target)
# parser.feed(exampleXml)
# parser.close()
# Вариант взят из документации по xml.etree.ElementTree:
# https://docs.python.org/3/library/xml.etree.elementtree.html#xmlparser-objects. Ниже нример решения на этом варианте:
# from xml.etree.ElementTree import XMLParser
#
# class CubeScore:
#     depth = 0
#     red_score = 0
#     green_score = 0
#     blue_score = 0
#
#     def start(self, tag, attrib):
#         '''Вызывается для каждого открывающегося тега'''
#         self.depth += 1
#         if attrib['color'] == 'red':
#             self.red_score += self.depth
#         elif attrib['color'] == 'green':
#             self.green_score += self.depth
#         elif attrib['color'] == 'blue':
#             self.blue_score += self.depth
#
#     def end(self, tag):
#         '''Вызывается для каждого закрывающегося тега'''
#         self.depth -= 1
#
#     def close(self):
#         '''Вызывется этот метод при завершении разбора XML'''
#         return str(self.red_score) + ' ' + str(self.green_score) \
#             + ' ' + str(self.blue_score)
#
# target = CubeScore()
# parser = XMLParser(target=target)
# parser.feed(input())
# print(parser.close())
#######################################################################################

# from xml.etree import ElementTree
# colors = {"red": 0, "green": 0, "blue": 0}  # словарь ключ=цвет
# def finder(root, count=1):
#     colors[root.attrib["color"]] += count  # нашли цвет добавили к счётчику
#     [finder(child, count + 1) for child in root]  # поиск во вложениях
# finder(ElementTree.fromstring(input()))  # считываем xml-строку
# print(colors["red"], colors["green"], colors["blue"])  # выдаём ответ

# from html.parser import HTMLParser
# d = {"red":0, "blue":0, "green":0}
# class MyParser(HTMLParser):
#
#     def __init__(self):
#         HTMLParser.__init__(self)
#         self.price = 0
#
#     def handle_starttag(self, tag, attrs):
#         self.price += 1
#         d[attrs[0][1]] += self.price
#
#     def handle_endtag(self, tag):
#         self.price -= 1
#
#     def handle_data(self, data):
#         d[data] += self.price
# s = input()
# parser = MyParser()
# parser.feed(s)
# parser.close()
# print(d["red"], d["green"], d["blue"])


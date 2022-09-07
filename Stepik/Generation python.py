# a = int(input())
# b = int(input())
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print((a ** 10 + b ** 10) ** 0.5)

##################################################################################################################
# Напишите программу для вычисления и оценки индекса массы тела (ИМТ) человека.

# weight, growth = float(input()), float(input())
#
# imt = weight / growth ** 2
#
# if imt < 18.5:
#     print("Недостаточная масса")
# elif imt > 25:
#     print("Избыточная масса")
# else:
#     print("Оптимальная масса")
#
#
# class Human():
#     def __init__(self, height, weight):
#         self.height = height
#         self.weight = weight
#
#     @staticmethod
#     def check(value):
#         if not isinstance(value, (int, float)) or value < 0:
#             raise TypeError("Значение роста и веса человека должно быть неотрицательным числом")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, height_value):
#         self.check(height_value)
#         self.__height = height_value
#         self.__body_mass_index = None
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight_value):
#         self.check(weight_value)
#         self.__weight = weight_value
#         self.__body_mass_index = None
#
#     @property
#     def body_mass_index(self):
#         if self.__body_mass_index is None:
#             self.__body_mass_index = self.weight / self.height ** 2
#         return self.__body_mass_index
#
#     def display_bmi(self):
#         if self.body_mass_index < 18.5:
#             print("Недостаточная масса")
#         elif self.body_mass_index > 25:
#             print("Избыточная масса")
#         else:
#             print("Оптимальная масса")
#
#
# weight, height = float(input()), float(input())
# Human(height, weight).display_bmi()

#######################################################################################################################
# Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ
# (в том числе пробел) стоит 60 копеек.

# string = str(input())
# price = 0
# for el in string:
#     price += 60
# print(price // 100, 'р.', price % 100, 'коп.')
#
# l =sum( [60 for i in input()])
# print(f'{l//100} р. { l%100} коп.')
#
# string = input()
# price = 60 * len(string)
# print(f'{price // 100} р. {price % 100} коп.')
#
# print(*divmod(len(input()) * 60, 100), sep='р. ', end='коп.')

# Синтаксис: divmod(divident, divisor)
# Параметры:
# divident - делимое, число, которое вы хотите разделить
# divisor - делитель, число, на которое вы хотите делить
# Возвращаемое значение: tuple - кортеж вида (частное, остаток)
# Описание:
# Функция divmod() возвращает кортеж, содержащий частное и остаток. Не поддерживает комплексные числа. Со смешанными
# типами операндов применяются правила для двоичных арифметических операторов.
# Для целых результат аналогичен (a // b, a % b).
# Для чисел с плавающей запятой результат аналогичен (q, a % b), где q обычно равен math.floor(a / b), однако может может
# быть и на единицу меньше. Так или иначе, q * b + a % b приближено к a, если a % b не нуль, то имеет тот же знак,
# что и b, и 0 <= abs(a % b) < abs(b).

######################################################################################################################
# Дана строка, состоящая из слов, разделенных пробелами. Напишите программу, которая подсчитывает количество слов в
# этой строке.

# string = input().split()  # .split() != .split(' ')
# print(len(string))

# В Python можно использовать даже несколько разделителей. Для этого просто требуется передать несколько символов в
# качестве разделителей функции split.
# import re
# my_st = "Я\nучу; язык,программирования\nPython"
# print(re.split(";|,|\n", my_st))

#####################################################################################################################
# Китайский гороскоп назначает животным годы в 12-летнем цикле. Один 12-летний цикл показан в таблице ниже.
# 2000	Дракон
# 2001	Змея
# 2002	Лошадь
# 2003	Овца
# 2004	Обезьяна
# 2005	Петух
# 2006	Собака
# 2007	Свинья
# 2008	Крыса
# 2009	Бык
# 2010	Тигр
# 2011	Заяц
# Напишите программу, которая считывает год и отображает название связанного с ним животного. Ваша программа должна
# корректно работать с любым годом, не только теми, что перечислены в таблице.

# number = int(input()) % 12
# name = ['Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь', 'Овца']
# print(name[number])

# import requests
# import unicodedata
#
# link = 'https://stepik.org/api/steps?ids[]=1612731'
# page = requests.get(link)
# js = page.json()
# text = js["steps"][0]["block"]["text"]
#
# def noneTags(string):
#     flag = True
#     resultString = ''
#     for i in string:
#         if i == '<':
#             flag = False
#         elif i == '>':
#             flag = True
#             continue
#         if flag:
#             resultString += i
#     return resultString
#
#
# s = noneTags(text).replace("\n", '')
# result = s.split()[25:49]
#
# x = list(map(lambda n: int(n[1:-1])%12 if n[0] == "$" else n, result))
# adict = {x[i]: x[i+1] for i in range(0, len(x), 2)}
#
# print(adict[int(input()) % 12])

####################################################################################################################
# Дано пятизначное или шестизначное натуральное число. Напишите программу, которая изменит порядок его последних пяти
# цифр на обратный.
# Формат входных данных - На вход программе подается одно натуральное пятизначное или шестизначное число.
# Формат выходных данных - Программа должна вывести число, которое получится в результате разворота, указанного в
# условии задачи. Число нужно выводить без незначащих нулей.

# number = input()
# a = ''
# if len(number) == 6:
#     a += number[0]
# for i in reversed(number[-5:]):
#     a += i
# print(int(a))

# n = input()
# n = n[:-5] + n[:-6:-1]
# print(int(n))

# (lambda x: print(int(x[:-5] + x[-5:][::-1])))(input())

#####################################################################################################################
# На вход программе подаётся натуральное число. Напишите программу, которая вставляет в заданное число запятые в
# соответствии со стандартным американским соглашением о запятых в больших числах.

# print('{:,}'.format(1234567890))

# num = int(input())
# print(f'{num:,}')

number = input()
out = number[:len(number) % 3]
for index in range(len(number) % 3, len(number), 3):
    if out:
        out += ','
    out += number[index: index + 3]
print(out)

num = input()
for idx in range(len(num) - 3, 0, -3):
    num = num[:idx] + ',' + num[idx:]
print(num)
# len(num) - 3 # отсекаются последние три знака
# (len(num) - 3, 0, -3) # перебор от последних трёх знаков до первого значения с интервалом в -3 знака
# num = num[:idx] + ',' + num[idx:] # после каждых трёх последних знаков вставляется "," (при вставке списки и строки
# смещаются вправо, и поэтому не включается в счётчик следующего перебора)

#####################################################################################################################





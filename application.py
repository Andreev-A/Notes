# def factorial(n):
#     if n == 1:
#         return 1
#     factorial_n_minus_1 = factorial(n=n - 1)
#     return n * factorial_n_minus_1
#
#
# print(factorial(9))

# Выведите одно число – сумму данных n чисел
# n = int(input())
# out = 0
# for _ in range(n):
#     out += int(input())
# print(out)
#
# print(sum(int(input()) for _ in range(int(input()))))


# Реализуйте программу, которая будет вычислять количество различных объектов в списке.
# Два объекта a и b считаются различными, если a is b равно False.
# Вашей программе доступна переменная с названием objects, которая ссылается на список, содержащий не более
# 100 объектов. Выведите количество различных объектов в этом списке.
# objects = [1, 2, 1, 2, 3, True]
# objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]
# ans, set_objects = 0, []
# for obj in objects:  # доступная переменная objects
#     for set_obj in set_objects:
#         if obj is set_obj:
#             break
#     else:
#         set_objects.append(obj)
#         ans += 1
# print(ans)
#
# n = len(objects)
# ans = n
# for i in range(n):
#     for j in range(i):
#         if id(objects[i]) == id(objects[j]):
#             ans -= 1
#             break
# print(ans)
#
# print(len(set(map(id, objects))))
# print(len(set(id(i) for i in objects)))
#
# Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x
# и возвращающую самое маленькое целое число y, такое что:
# y больше или равно x
# y делится нацело на 5
# def closest_mod_5(x):
#     while x % 5 != 0:
#         x +=1
#     return x
# def closest_mod_5(x):
#     return (x + 4) // 5 * 5
# def closest_mod_5(x):
#     return x if x % 5 == 0 else closest_mod_5(x + 1)
# def closest_mod_5(x):
#     return [x + i for i in range(5) if (x + i) % 5 == 0][0]

# Пусть n = 3, т. е. есть три элемента (1, 2, 3). Пусть k = 2. Все различные сочетания из 3 элементов по 2:
# (1, 2), (1, 3), (2, 3). Различных сочетаний три, поэтому C(3, 2) = 3.
# При C(n, 0) = 1, так как из n элементов выбрать 0 можно единственным образом, а именно, ничего не выбрать.
# Также несложно понять, что если k > n, то C(n, k) = 0, так как невозможно, например, из трех элементов выбрать пять.
# Для вычисления C(n, k) в других случаях используется следующая рекуррентная формула:
# C(n, k) = C(n - 1, k) + C(n - 1, k - 1).
# Реализуйте программу, которая для заданных n и k вычисляет C(n, k).
# Вашей программе на вход подается строка, содержащая два целых числа n и k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10).
# Ваша программа должна вывести единственное число: C(n, k).
# def C(n, k):
#     if k == 0:
#         return 1
#     elif k > n:
#         return 0
#     else:
#         return C(n - 1, k) + C(n - 1, k - 1)
#
# n, k = map(int, input().split())
# print(C(n, k))
# print(C(*map(int, input().split())))
# print(C(*(int(i)for i in input().split())))
#
# n, k = map(int, input().split())
# sz = max(n, k) + 1
# c = [[0] * sz for _ in range(sz)]
# c[0][0] = 1
# for i in range(1, sz):
#     for j in range(i + 1):
#         c[i][j] = c[i - 1][j] + c[i - 1][j - 1]
# print(c[n][k])
#
# Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку
# создания пространств имен и добавление в них переменных.
# В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.
# Вашей программе на вход подаются следующие запросы:
# create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
# add <namespace> <var> – добавить в пространство <namespace> переменную <var>
# get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из
# пространства <namespace>, или None, если такого пространства не существует
# Для каждого запроса get выведите в отдельной строке его результат
#
# memory = {'global': [None, []]}
#
# def search(a, b):
#     if a is None or b in memory[a][1]:
#         print(a)
#     else:
#         search(memory[a][0], b)
#
# for command, namespace, parent_var in [input().split() for i in range(int(input()))]:
#     if command == 'create':
#         memory[namespace] = [parent_var, []]
#     elif command == 'add':
#         memory[namespace][1].append(parent_var)
#     else:
#         search(namespace, parent_var)
#
# memory = {'global': [None, []]}
#
# for command, namespace, parent_var in [input().split() for i in range(int(input()))]:
#     if command == 'create':
#         memory[namespace] = [parent_var, []]
#     elif command == 'add':
#         memory[namespace][1].append(parent_var)
#     else:
#         while namespace is not None:
#             if parent_var in memory[namespace][1]:
#                 break
#             namespace = memory[namespace][0]
#         print(namespace)

# dct = {'global': ['None']}  # словарь списков(родитель,переменные)
# for ops, nms, v in [input().split() for i in range(int(input()))]:
#     if ops == 'create':
#         dct[nms] = [v]  # создать пространство-новый список в словаре
#     elif ops == 'add':
#         dct[nms].append(v)  # новая переменная-добавить в список
#     elif ops == 'get':  # поиск переменной (циклом)
#         while nms != 'None' and v not in dct[nms]:  # если нет в пространстве-меняем на родителя(пока не None)
#             nms = dct[nms][0]
#         print(nms)
#
# n = int(input())
# parent = {"global": None}
# vs = {"global": set()}
# for _ in range(n):
#     t, fst, snd = input().split()
#     if t == "create":
#         parent[fst] = snd
#         vs[fst] = set()
#     elif t == "add":
#         vs[fst].add(snd)
#     else:  # t == get
#         while fst is not None:
#             if snd in vs[fst]:
#                 break
#             fst = parent[fst]
#         print(fst)

# Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
# Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно
# положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность
# добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее
# вместимость.
# class MoneyBox:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.there_is = 0
#         # конструктор с аргументом – вместимость копилки
#
#     def can_add(self, v):
#         return self.capacity - self.there_is >= v
#         # True, если можно добавить v монет, False иначе.
#
#     def add(self, v):
#         if self.can_add(v):
#             self.there_is += v
#             # положить v монет в копилку

# Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки чисел из
# этой последовательности, затем сумму второй пятерки, и т. д.
# Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её последовательные части.
# Например, сначала первые три элемента, потом следующие шесть, потом следующие два и т. д.
# Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить сумму пятерок
# последовательных элементов по мере их накопления.
# Одним из требований к классу является то, что он не должен хранить в себе больше элементов, чем ему действительно
# необходимо, т. е. он не должен хранить элементы, которые уже вошли в пятерку, для которой была выведена сумма.
#
# class Buffer:
#     def __init__(self):
#         self.my_list = []
#         # конструктор без аргументов
#
#     def add(self, *a):
#         self.my_list.extend(a)
#         while len(self.my_list) >= 5:
#             print(sum(self.my_list[:5]))
#             del(self.my_list[:5])
#         # добавить следующую часть последовательности
#
#     def get_current_part(self):
#         return self.my_list
#         # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
#         # добавлены
#
# class Buffer:
#     def __init__(self):
#         self.part = []
#
#     def add(self, *a):
#         for i in a:
#             self.part.append(i)
#             if len(self.part) == 5:
#                 print(sum(self.part))
#                 self.part.clear()
#
#     def get_current_part(self):
#         return self.part

# for k, v in словарь.items():
#     for k2, v2 in словарь.items():
# На первом уровне мы последовательно перебираем пары ключ(класс наследник) - значения(классы предки) в словаре.\
# На втором уровне для каждого значения(предка) из пары проверяем содержится ли он в ключах словаря(т.е.является
# ли предок в свою очередь чьим - то наследником).И если да, то добавляем предков предка в значения.
# Естественно перед этим надо каким - то образом заполнить словарь. Ну а в самом конце просто проверяем, есть ли
# соответствующее значение(предок) у запрошенного ключа(наследника).

# Вам необходимо отвечать на запросы, является ли один класс предком другого класса
# Важное примечание: Создавать классы не требуется.
# Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов.
# В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется
# i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется
# сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.
# В следующей строке содержится число q - количество запросов.
# В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
# Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.
# Формат выходных данных
# Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2,
# и "No", если не является.
#
# def search(child, parent):
#     if child == parent:
#         return 'Yes'
#     #if child not in base or not base[child]:
#         #return 'No'
#     for prev_parent in base[child]:
#         if search(prev_parent, parent):
#             return 'Yes'
#     return 'No'
#
# base = {}
# for _ in range(int(input())):
#     child, *parents = input().replace(":", " ").split()
#     base[child] = parents
# for _ in range(int(input())):
#     end, start = input().split()
#     print(search(start, end))
#
# Пример изящной реализации функции is_parent с использованием стандартной библиотеки языка Python
# n = int(input())
# parents = {}
# for _ in range(n):
#     a = input().split()
#     parents[a[0]] = [] if len(a) == 1 else a[2:]
#
# def is_parent(child, parent):
#     return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))
#
#
# q = int(input())
# for _ in range(q):
#     a, b = input().split()
#     print("Yes" if is_parent(b, a) else "No")
#
# n = int(input())
# parents = {}
# for _ in range(n):
#     a = input().split()
#     parents[a[0]] = [] if len(a) == 1 else a[2:]
#
# def is_parent(child, parent):
#     if child == parent:
#         return True
#
#     for p in parents[child]:
#         if is_parent(p, parent):
#             return True
#
#     return False
#
# q = int(input())
# for _ in range(q):
#     a, b = input().split()
#     print("Yes" if is_parent(b, a) else "No")
#
# def test(parent, child):
#     if parent == child or parent in base[child]:
#         return 'Yes'
#     for i in base[child]:
#         if test(parent, i) == 'Yes':
#             return 'Yes'
#     return 'No'
#
# base = {}
# for com in [input().split(' ') for i in range(int(input()))]:
#     base[com[0]] = com[2:len(com)]
# for com in [input().split(' ') for i in range(int(input()))]:
#     print (test(com[0], com[1]))

# Реализуйте структуру данных, представляющую собой расширенную структуру стек. Необходимо поддерживать добавление
# элемента на вершину стека, удаление с вершины стека, и необходимо поддерживать операции сложения, вычитания,
# умножения и целочисленного деления.
#
# class ExtendedStack(list):
#     def sum(self):
#         self.append(self.pop() + self.pop())
#         # операция сложения
#
#     def sub(self):
#         self.append(self.pop() - self.pop())
#         # операция вычитания
#
#     def mul(self):
#         self.append(self.pop() * self.pop())
#         # операция умножения
#
#     def div(self):
#         self.append(self.pop() // self.pop())
#         # операция целочисленного деления

# Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом, чтобы при добавлении
# элемента в список с помощью метода append в лог отправлялось сообщение, состоящее из только что добавленного элемента.
# import time
# class Loggable:
#     def log(self, msg):
#         print(str(time.ctime()) + ": " + str(msg))
#
#
# class LoggableList(list, Loggable):
#     def append(self, s):
#         super(LoggableList, self).append(s)
#         self.log(s)
#
#
# # Пример правильного решения
# class LoggableList(list, Loggable):
#     def append(self, x):
#         list.append(self, x)
#         self.log(x)
#
# class LoggableList(list, Loggable):
#     def append(self, msg):
#         super().append(msg)
#         self.log(msg)




########################################################################################################################




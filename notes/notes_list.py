# создание списка  #####################################################################################################
# a = [2, 3, 4]
# a = list([1, 2, 3])
# list(range(10))  # генератор списка

# методы списка  #######################################################################################################

# .append()  # добавить в конец (один элемент)
# .extend([5, 5])  # добавить в конец (несколько элементов)
# .insert(3, 'a')  # вставить в определенное место
# .index('i', 5, 7)  # индекс элемента  (необязат. (5-нач., 7-кон.), возвращает первое вхождение, нет элемента - ошибка)
# .pop(0) - получить элемент по индексу [0], удаляя его из последовательности (по умолчанию () - последний)
# my_list[1] = 200  # заменить в списке
# del my_list[5]  # удалить элемент (с конкретного места)
# my_list.remove('s')  # удаляет первый по порядку элемент 's'
# my_list.count('d')  # количество элементов в списке
# min(my_list), max(my_list), summa(my_list)  # найти мин, макс, сумму (для списка чисел)
# my_list.sort()  # сортировать список
# sorted(my_list)  # если не надо изменить сам список (создает в памяти отсортированную копию)

#   zip() - profit = [100, 20]
#   days = ['пн', 'вт']
#   res = zip(profit, days)
#   print(list(res)) или res = list(zip(profit, days)) или print(dict(zip(days, profit)))
# ___сортировка по второму элементу: work_list.sort(name=lambda x: x[1]) или lst.sort(name=itemgetter(1)) с
# from operator import itemgetter
# ___получить элемент по индексу удаляя его из последовательности: dots = [segments.pop(0)[1]] for l, r in segments:

# Метод isupper() проверяет, все ли символы в строке находятся в верхнем регистре.
# Метод не принимает никаких параметров
# Метод в Python возвращает: Истинно, если все символы в строке являются прописными. False, если какие-либо символы в
# строке являются строчными.
# a = 'sdf'
# a.isupper()
# print(a)
# В python-е все функции/методы что-то возвращают - либо значение, либо None. reverse() изменяет сам объект и ничего не
# возвращает - только и всего

# Хранение в памяти
# При создании списка, в памяти резервируется пустая область. С одной стороны, это ничем не отличается от создания
# любого другого типа данных, но разница в том, что содержимое list может меняться:
# numbers = [1, 2]
# numbers[1] = 3
# # обновлённый список: [1, 3]
# До замены элемента последовательности print(numbers[1]) выведет 2, а после замены — 3.
# Создание списка в Python
# Это можно сделать несколькими способами, например перечислением элементов списка в квадратных скобках:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# При этом единица будет на позиции 0, то есть print(numbers[0]) выведет 1.
# Также можно использовать обработку итерируемого объекта функцией list(). Пусть у нас будет некоторая строка, тогда:
# list('tproger')
# # ['t', 'p', 'r', 'o', 'g', 'e', 'r']
# Также существуют генераторы списков, которые позволяют применить заданное выражение к каждому элементу
# последовательности. Допустим, необходимо создать list, состоящий из чисел от 1 до 5 включительно:
# numbers = [i for i in range(1,6)]
# # [1, 2, 3, 4, 5]
# Срезы (slice) списка
# Срезы позволяют получить некое подмножество значений. Следующий код вернёт список с элементами, начиная индексом 0 и
# не включая при этом индекс 2 и выше:
# numbers = [1, 5, 9, 6]
# print(numbers[0:2])
# # вывод [1, 5]
# Далее выведем всё, за исключением элемента на позиции 3:
# print(numbers[:3])
# # вывод [1, 5, 9]
# А теперь начиная с индекса 1 и до конца:
# print(numbers[1:])
# # вывод [5, 9, 6]
# Операции над списками Python
# x in l — true, если элемент x есть в списке l;
# x not in l — true, если элемент x отсутствует в l;
# l1 + l2 — объединение двух списков;
# l * n_test , n_test * l — копирует список n_test раз;
# len(l) — количество элементов в l;
# min(l) — наименьший элемент;
# max(l) — наибольший элемент;
# sum(l) — сумма чисел списка;
# for i in list() — перебирает элементы слева направо.
# Методы списков Python
# Index
# Возвращает положение первого совпавшего элемента. Поиск совпадения происходит слева направо. Пример:
# numbers = [1, 5, 9, 6, 1, 2, 1]
# print(numbers.index(1))
# # вывод 0: первая найденная единица на позиции 0
# Count
# Данный метод считает, сколько раз указанное значение появляется в списке Python:
# numbers = [1, 5, 9, 6, 1, 2, 1]
# print(numbers.count(1))
# # вывод 3, потому что единица встречается 3 раза
# Append
# Добавляет указанное значение в конец:
# numbers = [1, 5, 9, 6]
# numbers.append(3)
# # обновлённый список: [1, 5, 9, 6, 3]
# Sort
# Сортирует список в Пайтоне. По умолчанию от меньшего к большему:
# numbers = [1, 5, 9, 6]
# numbers.sort()
# # обновлённый список: [1, 5, 6, 9]
# Также можно сортировать последовательность элементов от большего к меньшему:
# numbers = [1, 5, 9, 6]
# numbers.sort(reverse = true)
# # обновлённый список: [9, 6, 5, 1]
# Insert
# Вставляет элемент перед указанным индексом:
# numbers = [1, 5, 9, 6]
# numbers.insert(3, [2, 3])
# # обновлённый список: [1, 5, 9, [2, 3], 6]
# Remove
# Удаляет первое попавшееся вхождение элемента в списке Python:
# numbers = [1, 5, 9, 6, 1, 2, 1]
# numbers.remove(1)
# # обновлённый список: [5, 9, 6, 1, 2, 1]
# Extend
# Подобно методу append(), добавляет элементы, но преимущество метода extend() в том, что он также позволяет добавлять
# списки:
# numbers = [1, 5, 9, 6]
# numbers.extend([2, 3])
# # обновлённый список: [1, 5, 9, 6, 2, 3]
# Pop
# Данный метод удаляет элемент в конкретно указанном индексе, а также выводит удалённый элемент. Если индекс не указан,
# метод по умолчанию удалит последний элемент:
# numbers = [1, 5, 9, 6]
# numbers.pop(1)
# # получаем:
# # 5
# # [1, 9, 6]
# Join
# Преобразовывает список в строку. Разделитель элементов пишут в кавычках перед методом, а сам список Питона должен
# состоять из строк:
# mylist = ['сайт', 'типичный', 'программист']
# print(', '.join(mylist))
# # вывод 'сайт, типичный, программист'

# x = ['abc', 'a', 'ab', 'abcd']
# # Сортировка элементов списка по возрастанию:
# # 1
# x.sort(name=len)
# print(x)
# # ['a', 'ab', 'abc', 'abcd']
# # 2
# new_x = sorted(x, name=len)
# print(new_x)
# # ['a', 'ab', 'abc', 'abcd']
# # В обратном порядке:
# # 1
# x.sort(name=len, reverse=True)
# print(x)
# # ['abcd', 'abc', 'ab', 'a']
# # 2
# new_x = sorted(x, name=len, reverse=True)
# print(new_x)
# # ['abcd', 'abc', 'ab', 'a']
# # Разница между sort() и sorted() в том, что первый - сортирует список на месте, возвращая None. Второй - возвращает
# # новый отсортированный список.

# Для преобразования листа листов в лист можно использовать вот такую функцию:
# def flatten(lst):
#     return [y for x in lst for y in x]
# Пример:
# lst = [[1, 2, 3], [4, 5, 6]]
# print(flatten(lst))
# [1, 2, 3, 4, 5, 6]

# lst.sort(key = lambda x: (x[0], x[1]))  # отсортирует по первому элементу туплей, с учётом второго, если первые совпадают

# l.sort(key=lambda x: (-x[0], x[1]), reverse=True)  # в порядке убывания 0, 1 - по алфавиту

# Python-код для преобразования списка кортежей в список
# Список инициализации кортежа
lt = [('Geeks', 2), ('For', 4), ('geek', '6')]
# использование списка понимания
out = [item for t in lt for item in t]
# вывод на печать
print(out)

# Импорт
import itertools
# Список инициализации кортежа
tuple = [(1, 2), (3, 4), (5, 6)]
# Использование itertools
out = list(itertools.chain(*tuple))
# вывод на печать
print(out)

# Добавление элемента в множество осуществляется с помощью метода add,
# Чтобы удалить элемент из множества, можно воспользоваться одним из двух методов: discard или remove. Если удаляемого
# элемента в множестве не было, то discard не изменит состояния множества, а remove выпадет с ошибкой.

# Вместо этого вы можете распаковать кортеж вручную, что будет работать как на Python 2.x, так и на 3.x:
# foo = lambda xy: (xy[1],xy[0])
# Или:
# def foo(xy):
#     x,y = xy
#     return (y,x)

# как транспонировать матрицу в питоне
# [*zip(*theArray)]
#
# >>> theArray = [['a','b','c'],['d','e','f'],['g','h','i']]
# >>> [list(i) for i in zip(*theArray)]
# [['a', 'd', 'g'], ['b', 'e', 'h'], ['c', 'f', 'i']]
# генератор списков создает новый 2d-массив с элементами списка вместо кортежей.
#
# в Python 3 функциональность map изменен, itertools.zip_longest можно использовать вместо:
# Источник:Что нового в Python 3.0
# >>> import itertools
# >>> uneven = [['a','b','c'],['d','e'],['g','h','i']]
# >>> list(itertools.zip_longest(*uneven))
# [('a', 'd', 'g'), ('b', 'e', 'h'), ('c', None, 'i')]


# Многие слышали о функции zip в Python, а кто-то даже регулярно ей пользуется. Сегодня мы (из интереса и для общего
# развития) опишем, как можно реализовать её самому с помощью list comprehensions.
# Для начала поясню, что вообще делает функция zip, для тех, кто с ней раньше не сталкивался:
# >>> s = 'abc'
# >>> t = (10, 20, 30)
# >>> zip(s,t)
# [('a', 10), ('b', 20), ('c', 30)]
# То есть функция берёт на вход несколько списков и создаёт из них список (в Python 3 создаётся не list, а специальный
# zip-объект) кортежей, такой, что первый элемент полученного списка содержит кортеж из первых элементов всех
# списков-аргументов. Таким образом, если ей передать три списка, то она отработает следующим образом:
# >>> s = 'abc'
# >>> t = (10, 20, 30)
# >>> u = (-5, -10, -15)
# >>> list(zip(s,t,u))
# [('a', 10, -5), ('b', 20, -10), ('c', 30, -15)]
# В общем-то, функция отработает даже для одного iterable-объекта, результатом будет последовательность из кортежей, в
# каждом из которых будет по одному элементу. Но это, пожалуй, не самый распространенный способ применения zip. Я часто
# использую zip, например, для создания словарей:
# >>> names = ['Tom', 'Dick', 'Harry']
# >>> ages = [50, 35, 60]
# >>> dict(zip(names, ages))
# {'Harry': 60, 'Dick': 35, 'Tom': 50}
# Это весьма удобно, не находите? Каждый раз, когда я рассказываю о zip на своих уроках, у меня спрашивают о том, что
# будет, если в функцию передать массивы разной длины. Ответ простой — победит более короткий:
# >>> s = 'abc'
# >>> t = (10, 20, 30, 40)
# >>> list(zip(s,t))
# [('a', 10), ('b', 20), ('c', 30)]
# Однако, если вам необходимо, чтобы для каждого из элементов более длинного массива в результирующем списке был создан
# кортеж из одного элемента, вы можете использовать zip_longest из пакета itertools.
# Есть одна возможность в Python, которая мне нравится даже больше, чем zip. Это списковое включение
# (англ. list comprehension). Именно поэтому, когда один из студентов недавно спросил меня, можем ли мы реализовать zip
# сами с помощью списковых включений, я просто не смог устоять.
# Как же нам этого добиться? Начнём с первого, что приходит на ум:
# [(s[i], t[i])              # создаём кортеж из двух элементов
#  for i in range(len(s))]   # для индексов от 0 до len(s) - 1
# В общем-то всё! Это работает. Но есть несколько моментов, которые всё же стоит доработать в этом методе.
# Во-первых, оригинальная функция могла работать с массивами разной длины. Поэтому вместо range(len(s)) нам стоит
# использовать range(len(x)), где x — наиболее короткая последовательность. Для этого достаточно поместить все
# последовательности в один список, отсортировать этот список по длине элементов и выяснить длину элемента, оказавшегося
# под нулевым индексом:
# >>> s = 'abcd'
# >>> t = (10, 20, 30)
# >>> sorted((s,t), key=len)
# [(10, 20, 30), 'abcd']
# Совмещаем это с предыдущим кодом:
# >>> s = 'abcd'
# >>> t = (10, 20, 30)
# >>> sorted((s,t), key=len)
# [(10, 20, 30), 'abcd']
# Это ещё не все доработки, а выражение уже получается слишком длинным. Пожалуй, выяснение наименьшей длины стоит
# вынести в отдельную функцию (заодно сделаем так, чтобы она вычисляла наикратчайшую последовательность из
# неограниченного количества аргументов):
# >>> def shortest_sequence_range(*args):
#         return range(len(sorted(args, key=len)[0]))
# >>> [(s[i], t[i])
#     for i in shortest_sequence_range(s,t) ]
# Что осталось теперь? Как уже говорилось выше, Python 3 создаёт не список, а специальный zip-объект, возвращая итератор
# от него. Это сделано для того, чтобы код не ломался при обработке исключительно длинных последовательностей. Это можно
# реализовать, но уже не с помощью спискового включения (которое всегда возвращает список), а с помощью генератора. К
# счастью, для этого достаточно поменять квадратные скобки на круглые:
# >>> def shortest_sequence_range(*args):
#       return range(len(sorted(args, key=len)[0]))
# >>> g = ((s[i], t[i])
#          for i in shortest_sequence_range(s,t) )
# >>> for item in g:
#         print(item)
# ('a', 10)
# ('b', 20)
# ('c', 30)
# Готово! Мы реализовали свой полностью рабочий zip. Вы можете потренироваться и самостоятельно подумать, как ещё можно
# улучшить этот алгоритм.
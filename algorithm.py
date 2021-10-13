# Дано целое число 1 ≤ n ≤ 40, необходимо вычислить n-е число Фибоначчи
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
#
# def fib(n):
#     if 1 <= n <= 40:
#         a, b = 0, 1
#         for _ in range(n):
#             a, b = b, a + b
#         return a
#
# def fib(num):
#     prev, cur = 0, 1
#     for i in range(1, num):
#         prev, cur = cur, prev + cur
#     return cur

# Дано число 1 <= n <= 10^7, необходимо найти последнюю цифру n-го числа Фибоначчи.
# Как мы помним, числа Фибоначчи растут очень быстро, поэтому при их вычислении нужно быть аккуратным с переполнением.
# В данной задаче, впрочем, этой проблемы можно избежать, поскольку нас интересует только последняя цифра числа
# Фибоначчи: если 0 <= a,b <= 9 — последние цифры чисел F_i и F_i+1 соответственно, то (a+b) mod10 — последняя цифра
# числа F_i+2. Используем период Пизано.
#
# def fib_digit(n):
#     if 1 <= n <= 10 ** 7:
#         a, b = 0, 1
#         for _ in range(n):
#             a, b = b, (a + b) % 10
#         return a

# Даны целые числа 1 <= n <= 10^18 и 2 <= m <= 10^5 , необходимо найти остаток от деления n-го числа Фибоначчи на m
#
# def fib_mod(n, m):
#     list = [0, 1, 1]
#     for i in range(2, n + 2):
#         if list[i - 1] == 0 and list[i] == 1:
#             break
#         list.append((list[i - 1] + list[i]) % m)
#     out = list[n % (len(list) - 2)]
#     return out

# По данным двум числам 1 <= a, b <= 2*10^9 найдите их наибольший общий делитель.

# def gcd(a, b):
#     list, i = [a, b], 1
#     for i in range(1, max(a, b)):
#         if not list[i] and list[i - 1]:
#             break
#         list.append(list[i - 1] % list[i])
#     return max(list[i], list[i - 1])

# def gcd(a, b):
#     return gcd(b, a % b) if b else a

# a, b = map(int, input().split())
# while b:     # while b != 0
#     a, b = b, a % b
# print(a)

# По данным n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит
# хотя бы одну из точек.
# В первой строке дано число 1<=n<=100 отрезков. Каждая из последующих n строк содержит по два числа 0<=l<=r<=10^9,
# задающих начало и конец отрезка. Выведите оптимальное число m точек и сами m точек. Если таких множеств точек
# несколько, выведите любое из них.

# 4
# 4 7
# 1 3
# 2 5
# 5 6
# work_list = [list(map(int, input().split())) for i in range(int(input()))]
# work_list.sort(key=lambda x: x[1])
# point_list = [work_list[0][1]]
# for i in range(len(work_list) - 1):
#     if not work_list[i + 1][0] <= point_list[-1]:
#         point_list.append(work_list[i + 1][1])
# print(len(point_list))
# print(*point_list)
#
# segments = sorted([sorted(map(int,input().split())) for i in range(int(input()))], key=lambda x: x[1])
# dots = [segments.pop(0)[1]]
# for l, r in segments:
#     if l > dots[-1]:
#         dots.append(r)
# print(str(len(dots)) + '\n' + ' '.join(map(str, dots)))
#
# points = [list(map(int, input().split())) for i in range(int(input()))]
# out = []
# for p in reversed(sorted(points)):
#     if not out or out[-1] > p[1]:
#         out.append(p[0])
# print(len(out))
# print(*out)
#
# segs = sorted([[int(i) for i in input().split()] for j in range(int(input()))])
# dots = []
# while segs:
#     dots.append(segs[-1][0])
#     while segs and dots[-1] <= segs[-1][1]:
#         segs.pop()
# print(str(len(dots))+'\n'+' '.join(map(str, dots)))

# По данному числу 1 <= n <= 10^9 найдите максимальное число k, для которого n можно представить как сумму
# k различных натуральных слагаемых. Выведите в первой строке число k, во второй — k слагаемых.
#
# entered_number = int(input())
# difference_entered_number = entered_number
# summand_of_numbers = []
# for next_summand_of_number in range(1, entered_number + 1):
#     difference_entered_number -= next_summand_of_number
#     if difference_entered_number <= next_summand_of_number:
#         summand_of_numbers.append(next_summand_of_number + difference_entered_number)
#         break
#     summand_of_numbers.append(next_summand_of_number)
# print(len(summand_of_numbers))
# print(*summand_of_numbers)

# a = int(input())
# b = []
# for i in range(1, a + 1):
#     a -= i
#     if a <= i:
#         b.append(i + a)
#         break
#     b.append(i)
# print(len(b))
# print(*b)

# Первая строка содержит количество предметов 1 <= n <= 10^3 и вместимость рюкзака 0 <= W <= 2 * 10^6. Каждая из
# следующих n строк задаёт стоимость 0 <= c_i <= 2 * 10^6 и объём 0 <= w_i <= 2 * 10^6 предмета (n, W, c_i, w_i  —
# целые числа). Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть,
# стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх
# знаков после запятой.

# 3 50
# 60 20
# 100 50
# 120 30
# number_of_items, backpack_capacity = map(int, input().split())
# work_list, maximum_cost = [], 0
# for _ in range(number_of_items):
#     cost, volume = map(int, input().split())
#     work_list.append([cost / volume, cost, volume])
# for segment in reversed(sorted(work_list)):
#     if backpack_capacity >= segment[2]:
#         backpack_capacity -= segment[2]
#         maximum_cost += segment[1]
#     else:
#         maximum_cost += backpack_capacity / segment[2] * segment[1]
#         break
# print(round(maximum_cost, 3))
#
#  алгоритм с практики (задача выше)
import sys
import heapq


# решение сортировкой
def fractional_knapsack(capacity, values_and_weights):
    # список пар удельная стоимость и количество
    order = [(v / w, w) for v, w in values_and_weights]
    # пары сравниваются лексиграфически, если первые равны - то берется по второй большей
    order.sort(reverse=True)
    #  заведем аккумулятор - стоимость рюкзака на данный момент и обойдем получившийся список
    acc = 0
    for v_per_w, w in order:
        # если помещается в рюкзак, то берем весь, емкость убывает
        if w < capacity:
            acc += v_per_w * w
            capacity -= w
        # не помещается - то берем сколько сможем
        else:
            acc += v_per_w * capacity
            break
    return acc


# # решение двоичной кучей, добавляем модуль heapq
# def fractional_knapsack(capacity, values_and_weights):
#     # список пар удельная стоимость и количество
#     order = [(-v / w, w) for v, w in values_and_weights]
#     # построим кучу на списке пар, удельная ценность как приоритет, строим по наименьшему приоритету преобразуя список
#     # чтобы инвертировать это поведение добавим '-' в первый компонент пары выше в строке order
#     heapq.heapify(order)
#     #  заведем аккумулятор - будем вытаскивать из списка элемент с большей удельной ценность с помощью функции heappop
#     acc = 0
#     # while order:
#     #     v_per_w, w = heapq.heappop(order)
#     #     # если помещается в рюкзак, то берем весь, емкость убывает, ставим '-' т.к в куче с минусом
#     #     if w < capacity:
#     #         acc += -v_per_w * w
#     #         capacity -= w
#     #     # не помещается - то берем сколько сможем, ставим '-' т.к в куче с минусом
#     #     else:
#     #         acc += -v_per_w * capacity
#     #         break
#     # или через переменную, добавляем условие остановки по полному рюкзаку - and capacity
#     while order and capacity:
#         v_per_w, w = heapq.heappop(order)
#         can_take = min(w, capacity)
#         # '-' заменяем сложение, чтобы не было -v_per_w
#         acc -= v_per_w * can_take
#         capacity -= can_take
#
#     return acc


def main():
    # для каждой строки а потоке ввода разбивает ее на кусочки и каждый кусочек приводит к целому числу,
    # map - функция-генератор, приводим все к кортежу - чтобы все было явно
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    # прочитаем элементы, попросив следующий элемент с генератора
    n, capacity = next(reader)
    # читаем остальные элементы в потоке в список парами
    values_and_weights = list(reader)
    # не используем n явно просто проверим что правильно считали
    assert len(values_and_weights) == n
    # вызовем функцию для решения и выведем ответ
    opt_value = fractional_knapsack(capacity, values_and_weights)
    print('{:.3f}'.format(opt_value))


def test():
    # рюкзак ноль - его нет
    assert fractional_knapsack(0, [(60, 20)]) == 0.0
    # предмета меньше, чем рюкзак может вместить - то есть взяли сколько есть
    assert fractional_knapsack(25, [(60, 20)]) == 60.0
    # есть предметы нулевой стоимости и они не повлияли на итог
    assert fractional_knapsack(25, [(60, 20), (0, 100)]) == 60.0
    # если предметов больше, то возьмем оптимальное решение
    assert fractional_knapsack(25, [(60, 20), (50, 50)]) == 60.0 + 5.0
    # пример со страницы задания
    assert fractional_knapsack(50, [(60, 20), (100, 50), (120, 30)]) == 180.0

    import time

    def timed(f, *args, n_iter=100):
        acc = float('inf')
        for i in range(n_iter):
            t0 = time.perf_counter()
            f(*args)
            t1 = time.perf_counter()
            acc = min(acc, t1 - t0)
        return acc

    from random import randint
    # from timing import timed
    for attempt in range(100):
        n = randint(1, 1000)
        capacity = randint(0, 2 * 10 ** 6)
        values_and_weights = []
        for i in range(n):
            values_and_weights.append((randint(0, 2 * 10 ** 6), randint(1, 2 * 10 ** 6)))

        t = timed(fractional_knapsack, capacity, values_and_weights)
        print(t)
        assert t < 5


#  вызов функции main, на время проверки меняем на test
if __name__ == '__main__':
    test()

#
# Постройте алгоритм, который получает на вход натуральное число n и за время O(n) находит минимальное число монет
# def num_coin_opt(price: int):
#     coins = [10, 25, 1]
#     coins.sort(reverse=True)
#     amount_coins = [0] * (len(coins))
#
#     for i in range(len(coins)):
#         working_price = priceabacabad
#         for coin in coins[i:]:
#             amount_coins[i] += working_price // coin
#             working_price %= coin
#     return min(amount_coins)

# По данной непустой строке ss длины не более 10^4, состоящей из строчных букв латинского алфавита, постройте
# оптимальный беспрефиксный код. В первой строке выведите количество различных букв k, встречающихся в строке,
# и размер получившейся закодированной строки. В следующих k строках запишите коды букв в формате "letter: code".
# В последней строке выведите закодированную строку.
# abacabad   01001100100111
#
# string = input()
# work_list, letters_in_binary, binary_code = [], {}, ''
# for letter in set(string):
#     work_list.append([letter, string.count(letter)])
# number_of_letters = len(work_list)
# while len(work_list) > 1:
#     work_list.sort(key=lambda x: x[1])
#     work_list.append([work_list[0][0] + work_list[1][0], work_list[0][1] + work_list[1][1]])
#     for i in range(2):
#         for j in work_list.pop(0)[0]:
#             if j in letters_in_binary:
#                 letters_in_binary[j] = str(i) + letters_in_binary[j]
#             else:
#                 letters_in_binary.setdefault(j, str(i))
# for letter in string:
#     if number_of_letters == 1:
#         binary_code = str(0) * work_list[0][1]
#         letters_in_binary[letter] = str(0)
#     else:
#         binary_code += letters_in_binary[letter]
# print(number_of_letters, len(binary_code))
# [print('{}: {}'.format(k, letters_in_binary[k])) for k in sorted(letters_in_binary)]
# print(binary_code)
#
# import collections
#
#
# def popmin(tree, codes, num):
#     el = tree.pop(tree.index(min(tree)))
#     for s in el[1]:
#         codes[s] = num + codes[s]
#     return el[0], el[1]
#
#
# def main():
#     sss = input().strip()
#     count = collections.Counter(sss)
#     codes = dict.fromkeys(count, '0' if len(count) == 1 else '')
#     tree = [[count[key], key] for key in count]
#     while len(tree) > 1:
#         val1, s1 = popmin(tree, codes, '0')
#         val2, s2 = popmin(tree, codes, '1')
#         tree.append([val1 + val2, s1 + s2])
#     word = ''.join(codes[s] for s in sss)
#     print(len(count), len(word))
#     [print('{}: {}'.format(k, codes[k])) for k in sorted(codes)]
#     print(word)
#
#
# from heapq import heappush, heappop
# from collections import Counter
#
# prefix = lambda a, p: [(k, p + v) for k, v in a]
# merge  = lambda a, b: (a[0] + b[0], prefix(a[1], '0') + prefix(b[1], '1'))
#
# string = input()
# heap = [(v, [(k, '')]) for k, v in reversed(Counter(string).most_common())]
#
# while len(heap) > 1:
#     heappush(heap, merge(heappop(heap), heappop(heap)))
#
# table = heap[0][1] if len(heap[0][1]) > 1 else prefix(heap[0][1], '0')
# encoded = string.translate(str.maketrans(dict(table)))
#
# print(len(table), len(encoded))
# print(*map('{0[0]}: {0[1]}'.format, table), encoded, sep='\n')
#
# from collections import Counter
#
# line = input()
# count = Counter(line)
# d = {key:"" for key in set(count)}
# if len(d) > 1:
#     while len(count) > 1:
#         a, b = count.most_common()[:-3:-1]
#         count[a[0] + b[0]] = count.pop(a[0]) + count.pop(b[0])
#         for c in a[0]:
#             d[c] = '0' + d[c]
#         for c in b[0]:
#             d[c] = '1' + d[c]
# elif len(d) == 1:
#     d[line[0]] = '0'
#
# cod_line = ''.join(d[k] for k in line)
#
# print(len(d), len(cod_line))
# print(*[f'{k}: {d[k]}' for k, z in Counter(line).most_common()], sep='\n')
# print(cod_line)

# Восстановите строку по её коду и беспрефиксному коду символов. В первой строке входного файла заданы два целых числа k
# и l через пробел — количество различных букв, встречающихся в строке, и размер получившейся закодированной строки,
# соответственно. В следующих k строках записаны коды букв в формате "letter: code". Ни один код не является префиксом
# другого. Буквы могут быть перечислены в любом порядке. В качестве букв могут встречаться лишь строчные буквы
# латинского алфавита; каждая из этих букв встречается в строке хотя бы один раз. Наконец, в последней строке записана
# закодированная строка. Исходная строка и коды всех букв непусты. Заданный код таков, что закодированная строка имеет
# минимальный возможный размер.
# В первой строке выходного файла выведите строку s. Она должна состоять из строчных букв латинского алфавита.
# Гарантируется, что длина правильного ответа не превосходит 10^4 символов.
#
# 4 14
# a: 0
# b: 10
# c: 110
# d: 111
# 01001100100111
# number_of_letters, encoded_string_size = map(int, input().split())
# letters_in_binary = dict({map(str, input().split(': ')[::-1]) for _ in range(number_of_letters)})
# encoded_string, decoded_string, letter = input(), '', ''
# for i in encoded_string:
#     letter += i
#     if letter not in letters_in_binary:
#         continue
#     decoded_string += letters_in_binary[letter]
#     letter = ''
# print(decoded_string)

# Первая строка входа содержит число операций 1 <= n <= 10^5. Каждая из последующих n строк задают операцию одного из
# следующих двух типов:
# Insert x, где 0 <= n <= 10^9 — целое число
# ExtractMax
# Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает максимальное число и выводит его.
#
# priority_list, extract_max = [], []
# for _ in range(int(input())):
#     string = input()
#     if priority_list and string == 'ExtractMax':
#         extract_max.append(priority_list.pop(0))
#         if len(priority_list) > 1:
#             priority_list.insert(0, priority_list.pop(- 1))
#             index = 0
#             while 2 * index + 1 < len(priority_list):
#                 index_1 = 2 * index + 1
#                 index_2 = 2 * index + 2
#                 if index_2 > len(priority_list) - 1:
#                     index_2 = index_1
#                 if priority_list[index] >= (priority_list[index_1] and priority_list[index_2]):
#                     break
#                 next_index = index_1 if priority_list[index_1] >= priority_list[index_2] else index_2
#                 priority_list[index], priority_list[next_index] = priority_list[next_index], priority_list[index]
#                 index = next_index
#     elif string != 'ExtractMax':
#         priority_list.append(int(string.split()[1]))
#         index = len(priority_list) - 1
#         while index:
#             prev_index = (index - 1) // 2
#             if priority_list[index] > priority_list[prev_index]:
#                 priority_list[index], priority_list[prev_index] = priority_list[prev_index], priority_list[index]
#                 index = prev_index
#             else:
#                 break
# print(*extract_max, sep='\n')
#
# def up(i):
#     while i > 0 and a[(i - 1)//2] < a[i]:
#         a[(i - 1)//2], a[i] = a[i], a[(i - 1)//2]
#         i = (i - 1) // 2
#
# def down(i):
#     while 2 * i + 1 <= len(a) - 1:
#         j = i
#         if a[2 * i + 1] > a[i]:
#             j = 2 * i + 1
#         if 2 * i + 2 <= len(a) - 1 and a[2 * i + 2] > a[j]:
#             j = 2 * i + 2
#         if i == j:
#             break
#         else:
#             a[i], a[j] = a[j], a[i]
#             i = j
#
# a = []
# for _ in range(int(input())):
#     s = (input().split())
#     if len(s) == 2:
#         a.append(int(s[1]))
#         up(len(a) - 1)
#     else:
#         print(a[0])
#         a[0] = a[-1]
#         a.pop()
#         down(0)

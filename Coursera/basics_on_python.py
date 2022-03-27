

###################################################################################################################

# Для подсчета модуля числа в Питоне существует функция abs, которая избавляет от необходимости каждый раз писать
# подсчет модуля вручную.



###############3######################################################################################################

# В отличие от целых чисел, вещественные числа в языке Питон имеют ограниченную длину.
# Подумаем, как хранить десятичную дробь в памяти. Поскольку вещественных чисел бесконечно много (даже больше, чем
# натуральных), то нам придется ограничить точность. Например, мы можем хранить только несколько первых значащих цифр,
# не храня незначащие нули. Будем отдельно хранить целое число с первыми значащими цифрами и отдельно хранить
# числа 10, на которую нужно умножить это число.
# Например, число 5.972*10**24 (это масса Земли в килограммах) можно сохранить как 5972 (цифры числа, мантисса) и 21
# (на какую степень 10 нужно умножить число, экспонента). С помощью такого представления можно хранить вещественные
# числа любой размерности.
# Примерно так и хранятся числа в памяти компьютера, однако вместо десятичной системы используется двоичные. На
# большинстве аппаратных систем в языке Питон для хранения float используется 64 бита, из которых 1 бит уходит на знак,
# 52 бита - на мантиссу и 11 бит - на экспоненту. Это не совсем правда, но достаточно неплохо описывает реальность.
# 52 бита дают около 15-16 десятичных знаков, которые будут храниться точно. 11 бит на экспоненту также накладывает
# ограничения на размерность хранимых чисел (примерно от -1000 до 1000 степени числа 10).
# Любое вещественное число на языке Питон представимо в виде дроби, где в числителе хранится целое число, а в
# знаменателе находится какая-либо степень двойки. Например, 0.125 представимо как 1/8, а 0.1 как
# 3602879701896397/36028797018963968. Несложно заметить, что эта дробь не равно 0.1, т. е. хранение числа 0.1 точно в
# типе float невозможно, как и многих других "красивых" десятичных дробей.
# В целом будет полезно представлять себе вещественное число X как отрезок [X - epsilon; X + epsilon]. Как же определить
# величину epsilon?
# Для этого нужно понять, что погрешность не является абсолютной, т. е. одинаковой для всех чисел, а является
# относительной. Упрощенно, аппаратную погрешность хранения числа X можно оценить как X*2**(-54).
# Чаще всего в задачах входные данные имеют определенную точность. Рассмотрим на примере: заданы два числа X и Y с
# точностью 6 знаков после точки (значит epsilon=5*10**(-7)) и по модулю не превосходящие 10**9. Оценить абсолютную
# погрешность вычисления X * Y. Рассмотрим худший случай, когда X и Y равны 10**9 и отклонились на максимально возможное
# значение epsilon в одну сторону. Тогда результат вычисления будет выглядеть так:
# (X + epsilon) * (Y + epsilon) = XY + (X + Y) * epsilon + epsilon**2
# Величина epsilon**2 пренебрежимо мала, XY - это правильный ответ, а (X + Y) * epsilon - искомое значение абсолютной
# погрешности. Подставим числа и получим:
# 2 * 10**9 * 5 * 10**(-7) = 10**3                               |X - Y| < epsilon
# Абсолютная погрешность вычисления составила 1000 (одну тысячу). Что довольно неожиданно и грустно.
# Таким образом, становится понятно, что нужно аккуратно вычислять значение погрешности для сравнения вещественных чисел
# print(0.1.as_integer_ratio()) - вывод дроби
# Для записи констант или при вводе-выводе может использоваться как привычное представление в виде десятичной дроби,
# например 123.456, так и "инженерная" запись числа, где мантисса записывается в виде вещественного числа с одной цифрой
# до точки и некоторым количеством цифр после точки, затем следует буква ''e'' (или ''E'') и экспонента. Число 123.456 в
# инженерной записи будет выглядеть как 1.23456e2, что означает, что 1.23456 нужно умножить на 10**2. И мантисса и
# экспонента могут быть отрицательными и записываются в десятичной системе.
# Такая запись чисел может применяться при создании вещественных констант, а также при вводе и выводе. Инженерная запись
# удобна для хранения очень больших или очень маленьких чисел, чтобы не считать количество нулей в начале или конце
# числа.
# Если хочется вывести число не в инженерной записи, а с фиксированным количеством знаков после точки, то следует
# воспользоваться методом format, который имеет массу возможностей. Нам нужен только вывод фиксированного количества
# знаков, поэтому воспользуемся готовым рецептом для вывода 25 знаков после десятичной точки у числа 0.1:
# x = 0.1
# print('{0:.25f}'.format(x))
# Если запустить эту программу, то можно легко убедиться в том, что 0.1 + 0.2 не равно 0.3. Хотя можно было надеятся,
# что несмотря на неточное представление, оно окажется одинаково неточным для всех чисел.
# Поэтому при использовании вещественных чисел нужно следовать нескольким простым правилам:
# 1) Если можно обойтись без использования вещественных чисел - нужно это сделать. Вещественные числа проблемные,
# неточные и медленные.
# 2) Два вещественных числа равны между собой, если они отличаются не более чем на epsilon. Число X меньше числа Y,
# если X < Y - epsilon.
# Код для сравнения двух чисел, заданных с точностью 6 знаков после точки, выглядит так:
# x = float(input())
# y = float(input())
# epsilon = 10 ** -6
# if abs(x - y) < epsilon:
#     print('Equal')
# else:
#     print('Not equal')
# При использовании целых и вещественных чисел в одном выражении вычисления производятся в вещественных числах. Тем не
# менее, иногда возникает необходимость преобразовать вещественное число в целое. Для этого можно использовать несколько
# видов функций округления:
# int - округляет в сторону нуля и отрицательные также в сторону нуля (отбрасывет дробную часть)
# round - округляет до ближайшего целого, если ближайших целых несколько (дробная часть равно 0.5), то к чётному
# floor - округляет в меньшую сторону
# ceil - округляет в большую сторону
# Функции floor и ceil находятся в библиотеке math.
# В библиотеке math также есть функция округления trunc, которая работает аналогично int.




#######################################4########################################################33

# Вызовы функций из функции
# Функцию подсчета факториала можно использовать для подсчета биномиальных коэффициентов (числа сочетаний). Формула для
# подсчета числа сочетаний выглядит так: n! / (k! * (n - k)!).
# Если бы мы не пользовались функциями, то нам потребовалось бы три раза записать почти одно и то же. С помощью функций
# вычисление выглядит намного проще:
# def factorial(num):
#     fact = 1
#     i = 2
#     while i <= num:
#         fact *= i
#         i += 1
#     return fact
# def binomial(n, k):
#     return factorial(n) // (factorial(k) * factorial(n - k))
# n, k = int(input()), int(input())  # n > k
# print(binomial(n, k))






###################################5#############################################################################


####



#######################6#################################


####################################7########################################################



##############8########################################################################

# Дан список чисел, который может содержать до 100000 чисел.Определите, сколько в нем встречается различных чисел.
# Формат ввода - Вводится список целых чисел. Все числа списка находятся на одной строке.
# Формат вывода - Выведите ответ на задачу.
# неразвернутое - print(len(set(map(int, input().split()))))
# print(
#     len(
#         set(
#             map(
#                 int,
#                 input().split()
#             )
#         )
#     )
# )

# Во входном файле (вы можете читать данные из sys.stdin, подключив библиотеку sys) записан текст. Словом считается
# последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами
# конца строки. Определите, сколько различных слов содержится в этом тексте.
# Формат ввода - Вводится текст.
# Формат вывода - Выведите ответ на задачу.
# import sys
# print(
#     len(
#         set(
#             map(
#                 str,
#                 sys.stdin.read().split()
#             )
#         )
#     )
# )

# Выведите значение наименьшего нечетного элемента списка, гарантируется, что хотя бы один нечётный элемент в списке есть.
# Формат ввода - Вводится список чисел. Все числа списка находятся на одной строке.
# Формат вывода - Выведите ответ на задачу.
# print(
#     min(
#         filter(
#             lambda x: x % 2 == 1,
#             map(
#                 int,
#                 input().split()
#             )
#         )
#     )
# )

# Проверьте, есть ли среди данных N чисел нули.
# Формат ввода - Вводится число N, а затем N чисел.
# Формат вывода - Выведите True, если среди введенных чисел есть хотя бы один нуль, или False в противном случае.
# неразвернутое - print(any(map(lambda x: x == 0, map(lambda x: int(input()), range(int(input()))))))
# print(
#     any(
#         map(
#             lambda x: x == 0,
#             map(
#                 lambda x: int(input()),
#                 range(int(input()))
#             )
#         )
#     )
# )

# print(any(map(lambda x: int(x) == 0, (open('input.txt', 'r', encoding='utf8').read()).split())))
# print('0' in set(open('input.txt').read().split()))
# print(any(map(lambda x: x == '0', map(lambda x: input(), range(int(input()))))))

# На вход подаётся последовательность натуральных чисел длины n≤1000.Посчитайте произведение пятых степеней чисел в
# последовательности.
# Формат ввода - Вводится последовательность чисел
# Формат вывода - Выведите ответ на задачу
# Примечания - Для решения задачи используйте функцию reduce из модуля functools
# неразвернутое - print(reduce(lambda x, y: x * y, map(lambda x: x ** 5, map(int, input().split()))))
# from functools import reduce
# print(
#     reduce(
#         lambda x, y: x * y,
#         map(
#             lambda x: x ** 5,
#             map(
#                 int,
#                 input().split()
#             )
#         )
#     )
# )

# Булева функция XOR (сложение по модулю два) задаётся следующей таблицей истинности:
# xor(0,0)=0
# xor(0,1)=1
# xor(1,0)=1
# xor(1,1)=0
# На вход подаются две последовательности (a₁,…,an) и (b₁,…,bn) из 0 и 1.
# Вычислите последовательность из (c₁,…,cn), где каждая cᵢ=xor(aᵢ,bᵢ).
# Формат ввода - На вход подаются две строки из 0 и 1, разделённых пробелами.
# Первая строка  —  это последовательность (a₁,…,an).
# Вторая строка  —  это последовательность (b₁,…,bn).
# Формат вывода - Выведите последовательность (c₁,…,cn), разделяя каждый элемент пробелом
# Примечания
# Для решения задачи можете использовать функцию zip.
# неразвернутое - print(*map(lambda xy: xy[0] ^ xy[1], zip(map(int, input().split()), map(int, (input().split())))))
# print(
#     *map(
#         lambda xy: xy[0] ^ xy[1],
#         zip(
#             map(
#                 int,
#                 input().split()
#             ),
#             map(
#                 int,
#                 input().split()
#             )
#         )
#     )
# )

# По заданной последовательности: (a₁,…,an)
# посчитайте последовательность частичных сумм: (S₁,…,Sn), где Sk=a₁+a₂+…+ak.
# Формат ввода - Вводится последовательность чисел (a₁,…,an), разделённая пробелами.
# Формат вывода - Выведите последовательность (S₁,…,Sn), разделяя числа пробелами.
# Примечания
# Для решения задачи можно воспользоваться функцией accumulate из модуля itertools.
# неразвернутое - print(*accumulate(map(int, input().split())))
# from itertools import accumulate
# print(
#     *accumulate(
#         map(
#             int,
#             input().split()
#         )
#     )
# )

# По заданному на входе числу 0≤n≤2000 выведите последовательность факториалов: 0!,1!,2!,…,n!
# Формат ввода - Вводится число n.
# Формат вывода - Выведите последовательность факториалов, разделяя числа пробелами
# from itertools import accumulate
# print(
#     *accumulate(
#         map(
#             lambda x: max(x, 1),
#             range(int(input()) + 1)
#         ),
#         lambda x, y: x * y
#     )
# )

# a = [0, 1, 2, 3, 4, 5, 6]
# a = map(lambda x: max(x,1), a)
# print(*accumulate(a, lambda x, y: x * y))
# print(*a)

# По данному числу N выведите все перестановки чисел от 1 до N в лексикографическом порядке.
# Формат ввода - Задано 1 число: N (0<N<10).
# Формат вывода - Необходимо вывести все перестановки чисел от 1 до N в лексикографическом порядке. Перестановки
# выводятся по одной в строке, числа в перестановке выводятся без пробелов.
# неразвернутое - print(*map(lambda xyz: ''.join(map(str, xyz)), permutations(range(1, int(input()) + 1))), sep='\n')
# from itertools import permutations
# print(
#     *map(
#         lambda xyz: ''.join(map(str, xyz)),
#         permutations(
#             range(
#                 1,
#                 int(input()) + 1)
#         )
#     ),
#     sep='\n'
# )

# XOR для произвольного числа аргументов определяется следующим образом:
# xor(a₁,a₂,…,an)= xor(a₁, xor(a₂, xor(a₃,… xor(an))…)
# XOR от n последовательностей A₁,…,An (Aᵢ=Aᵢ₁,…,Aᵢk) равных длин k  —  это последовательность C=xor(A₁,…,An),такая, что:
# cᵢ=xor(A₁ᵢ,…Anᵢ)
# Посчитайте XOR от n последовательностей равной длины k.
# Формат ввода - На первой строке записано число 2≤n≤1000  —  количество последовательностей.
# На последующих n строках записаны последовательности A₁,…,An из 0 и 1, разделённых пробелами равной длины 1≤k≤1000.
# Формат вывода - Выведите последовательность C=xor(A₁,…,An), разделяя числа последовательности пробелами.
# from functools import reduce
# print(
#     *map(
#         lambda x: (
#             reduce(
#                 lambda a, b: (a ^ b),
#                 x
#             )
#         ),
#         zip(
#             *map(
#                 lambda x: map(
#                     int,
#                     input().split()
#                 ),
#                 range(int(input()))
#             )
#         )
#     )
# )

# print(
#     *map(
#         lambda x: (reduce(lambda a, b: (a ^ b), x)),
#         zip(*map(lambda x: map(int, input().split()), range(int(input()))))
#     )
# )
# У нас списки с содержимым строк, а для xor от последовательности нужно бы получить списки столбцов. Похоже, самый
# простой способ это сделать - zip. При чём на вход ему нужно отправить не список строк, а список списков чисел в
# строках: lambda x: map(int, x.split()). Не забываем распаковать map звёздочкой, всё это в zip, красота.
# Ну а теперь список столбцов превращаем в финальный список: lambda x: reduce(lambda a, b: a ^ b, x). Перед принтом
# снова распаковываем map звёздочкой.
# Помогло разобраться, как работает map. В качестве lambda функции можно передавать другой map, в качестве параметров
# несколько списков.
# from sys import stdin
# from functools import reduce
# from operator import xor
#
# print(
#     *reduce(
#         lambda a, b: map(xor, a, b),
#         list(
#             map(
#                 lambda _: map(
#                     int, stdin.readline().strip().split()
#                 ), range(
#                     int(
#                         stdin.readline()
#                     )
#                 )
#             )
#         )
#     )
# )

# Выведите все простые на отрезке [2;n].
# Формат ввода - Вводится число 2≤n≤100000.
# Формат вывода - Выведите все простые числа из отрезка [2,n] в порядке возрастания
# Примечания
# Напомним, что проверить число на то, простое ли оно можно за количество операций порядка √(N). Также напомним, что
# функция math.sqrt работает значительно быстрее, чем (x ** 1/2).
# from math import sqrt
# print(
#     2,
#     *filter(
#         lambda i: all(
#             map(
#                 lambda x: i % x,
#                 range(2, int(sqrt(i)) + 1)
#             )
#         ),
#         range(3, int(input()) + 1, 2)
#     )
# )

################################################################################################################
# Перед началом тараканьих бегов всем болельщикам было предложено сделать по две ставки на результаты бегов. Каждая
# ставка имеет вид "Таракан №A придет раньше, чем таракан №B". Организаторы бегов решили выяснить, могут ли тараканы
# прийти в таком порядке, чтобы у каждого болельщика сыграла ровно одна ставка из двух (то есть чтобы ровно одно из двух
# утверждений каждого болельщика оказалось верным). Считается, что никакие два таракана не могут прийти к финишу
# одновременно.
# Формат ввода
# В первой строке входных данных содержатся два разделенных пробелом натуральных числа: число K, не превосходящее 10,
# - количество тараканов и число N, не превосходящее 100, - количество болельщиков. Все тараканы пронумерованы числами
# от 1 до K. Каждая из следующих N строк содержит 4 натуральных числа A, B, C, D, не превосходящих K, разделенных
# пробелами. Они соответствуют ставкам болельщика "Таракан №A придет раньше, чем таракан №B" и "Таракан №C придет
# раньше, чем таракан №D".
# Формат вывода
# Если завершить бега так, чтобы у каждого из болельщиков сыграла ровно одна из двух ставок, можно, то следует вывести
# номера тараканов в том порядке, в котором они окажутся в итоговой таблице результатов (сначала номер таракана,
# пришедшего первым, затем номер таракана, пришедшего вторым и т. д.) в одну строку через пробел. Если таких вариантов
# несколько, выведите любой из них. Если требуемого результата добиться нельзя, выведите одно число 0.
# Тест 1
# Входные данные:
# 3 2
# 2 1 2 3
# 1 2 3 2
# Вывод программы:
# 3 2 1
#
# Тест 2
# Входные данные:
# 3 4
# 1 2 1 3
# 1 2 3 1
# 1 2 2 3
# 1 2 3 2
# Вывод программы:
# 0
# import itertools
# import operator
#
# print(next(map(lambda a:
#                ' '.join(map(str, a[0])),
#                filter(lambda a: all(map(lambda b: operator.xor(
#                    *map(lambda c: c in itertools.combinations(a[0], 2), b, )),
#                                         a[1])), (
#                           lambda a, b: zip(itertools.permutations(a),
#                                            itertools.repeat(b)))(
#                    *(lambda k, n: (range(1, k + 1),
#                                    tuple(map(lambda i: (i[:2], i[2:]),
#                                              map(lambda _: tuple(
#                                                  map(int, input().split())),
#                                                  range(n)))))
#                      )(*map(int, input().split()))))), 0))

# from itertools import permutations
# from sys import stdin
# from operator import xor
#
# print(
#     *next(
#         map(
#             lambda d:
#             next(
#                 filter(
#                     lambda y:
#                     all(
#                         map(
#                             lambda x:
#                             xor(y.index(x[0]) < y.index(x[1]), y.index(x[2]) < y.index(x[3])),
#                             d[-1])
#                     ),
#                     d[:-1]
#                 ),
#                 [0, ]
#             ),
#
#             map(
#                 lambda j: [
#                     *permutations(range(j, 0, -1), j),
#                     list(map(lambda z: tuple(map(int, z.split())),
#                              stdin.readlines()))
#                 ],
#                 map(int, input().split())
#             )
#
#         ),
#         [0, ]
#     )
# )
# Т.к. во входных данных через map(int, input().split()) идёт и K и N, то у нас будет считаться два permutations. Чтобы
# не использовать второй мы используем next. Следовательно у Вас ошибка в последовательности. next на 9-й строке должен
# быть перед map на 7-й, а lambda d это filter.
#
# И посмотрите на то, что выдаёт map на 23-й строке (кстати не пойму зачем * на 25-й строке). Вы неправильно берёте из
# неё данные.
#
# И по поводу xor, не факт что грейдер импортирует библиотеку operator. Есть встроенный логический оператор, который
# подходит для наших нужд - ^. Используется как обычно: a ^ b.
#####################99999999999999###############################################################################################

# Реализуйте класс Matrix. Он должен содержать:
# Конструктор от списка списков. Гарантируется, что списки состоят из чисел, не пусты и все имеют одинаковый размер.
# Конструктор должен копировать содержимое списка списков, т. е. при изменении списков, от которых была сконструирована
# матрица, содержимое матрицы изменяться не должно.
# Метод __str__, переводящий матрицу в строку. При этом элементы внутри одной строки должны быть разделены знаками
# табуляции, а строки  —  переносами строк. После каждой строки не должно быть символа табуляции и в конце не должно
# быть переноса строки.
# Метод size без аргументов, возвращающий кортеж вида (число строк, число столбцов). Пример теста с участием этого
# метода есть в следующей задаче этой недели.
# from sys import stdin
# class Matrix:
#     def __init__(self, cls):
#         self._cls = [lst[:] for lst in cls]
#
#     def __str__(self):
#         s = ''
#         for i in self._cls:
#             if s:
#                 s += '\n'
#             s += '\t'.join(map(str, i))
#         return s
#
#     def size(self):
#         return len(self._cls), len(self._cls[0])
# exec(stdin.read())
######################################################################################################################

# Добавьте в предыдущий класс следующие методы:
#  __add__, принимающий вторую матрицу того же размера и возвращающий сумму матриц.
#  __mul__, принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр.
#  __rmul__, делающий то же самое, что и __mul__. Этот метод будет вызван в том случае, аргумент находится справа. Для
# реализации этого метода в коде класса достаточно написать __rmul__ = __mul__.
# Иллюстрация:
#  В следующем случае вызовется __mul__: Matrix([[0, 1], [1, 0]) * 10.
#  В следующем случае вызовется __rmul__ (так как у int не определен __mul__ для матрицы справа):
#  10 * Matrix([[0, 1], [1, 0]).
# Разумеется, данные методы не должны менять содержимое матрицы.
# Формат ввода - Как в предыдущей задаче.
# Формат вывода - Как в предыдущей задаче.
# from sys import stdin
# class Matrix:
#     def __init__(self, cls):
#         self.cls = [lst[:] for lst in cls]
#
#     def __str__(self):
#         s = ''
#         for i in self.cls:
#             if s:
#                 s += '\n'
#             s += '\t'.join(map(str, i))
#         return s
#
#     def __add__(self, other):
#         return Matrix([[num + other.cls[j][i] for i, num in enumerate(number)]
#                        for j, number in enumerate(self.cls)])
#
#     def __mul__(self, other):
#         return Matrix([[num * other for num in number]
#                        for number in self.cls])
#
#     __rmul__ = __mul__
#
#     def size(self):
#         return len(self.cls), len(self.cls[0])
# exec(stdin.read())

# from sys import stdin
# from copy import deepcopy
# class Matrix:
#     def __init__(self, matrix):
#         self.matrix = deepcopy(matrix)
#
#     def __str__(self):  # без аргументов
#         return '\n'.join(['\t'.join(map(str, list)) for list in self.matrix])
#
#     def __add__(self, other):
#         return Matrix()
#
#     def size(self):  # без аргументов!
#         return (len(self.matrix), len(self.matrix[0]))
#
#     def __add__(self, other):
#         return Matrix(list(map(
#             lambda x, y: list(map(lambda z, w: z + w, x, y)),
#             self.matrix, other.matrix)))
#
#     def __mul__(self, other):
#         return Matrix([[i * other for i in list] for list in self.matrix])
#
#     __rmul__ = __mul__
# # exec(stdin.read())
# m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
# print(m1 + m2)
# m = Matrix([[1, 1, 0], [0, 2, 10], [10, 15, 30]])
# alpha = 15
# print(m * alpha)
# print(alpha * m)
####################################################################################################################

# Добавьте в программу из предыдущей задачи класс MatrixError, содержащий внутри self поля matrix1 и matrix2 — ссылки на
# матрицы.
# В класс Matrix внесите следующие изменения:
# Добавьте в метод __add__ проверку на ошибки в размере входных данных, чтобы при попытке сложить матрицы разных
# размеров было выброшено исключение MatrixError таким образом, чтобы matrix1 поле MatrixError стало первым аргументом
# __add__ (просто self), а matrix2  —  вторым (второй операнд для сложения).
# Реализуйте метод transpose, транспонирующий матрицу и возвращающую результат (данный метод модифицирует экземпляр
# класса Matrix)
# Реализуйте статический метод transposed, принимающий Matrix и возвращающий транспонированную матрицу. Пример
# статического метода.
# Формат ввода - Как в предыдущей задаче.
# Формат вывода - Как в предыдущей задаче.

# from sys import stdin
#
# class MatrixError(BaseException):
#     def __init__(self, cls, other):
#         self.matrix1 = cls
#         self.matrix2 = other
#
#
# class Matrix:
#     def __init__(self, cls):
#         self.cls = [lst[:] for lst in cls]
#
#     def __str__(self):
#         s = ''
#         for i in self.cls:
#             if s:
#                 s += '\n'
#             s += '\t'.join(map(str, i))
#         return s
#
#     def __add__(self, other):
#         if len(self.cls) == len(other.cls):
#             return Matrix(
#                 [[num + other.cls[j][i] for i, num in enumerate(number)]
#                  for j, number in enumerate(self.cls)])
#
#         else:
#             raise MatrixError(self, other)
#
#     def __mul__(self, other):
#         return Matrix([[num * other for num in number]
#                        for number in self.cls])
#
#     __rmul__ = __mul__
#
#     def size(self):
#         return len(self.cls), len(self.cls[0])
#
#     def transpose(self):
#         if isinstance(self, Matrix):
#             self.cls = [*zip(*self.cls)]
#             return Matrix(self.cls)
#
#     @staticmethod
#     def transposed(cls):
#         return Matrix([*zip(*cls.cls)])
#
# exec(stdin.read())


#
# from sys import stdin
#
# class MatrixError(BaseException):
#     def __init__(self, cls, other):
#         self.matrix1 = cls
#         self.matrix2 = other
#
#
# class Matrix:
#     def __init__(self, cls):
#         self.cls = [lst[:] for lst in cls]
#
#     def __str__(self):
#         s = ''
#         for i in self.cls:
#             if s:
#                 s += '\n'
#             s += '\t'.join(map(str, i))
#         return s
#
#     def __add__(self, other):
#         if len(self.cls) == len(other.cls):
#             return Matrix(
#                 [[num + other.cls[j][i] for i, num in enumerate(number)]
#                  for j, number in enumerate(self.cls)])
#
#         else:
#             raise MatrixError(self, other)
#
#     def __mul__(self, other):
#         return Matrix([[num * other for num in number]
#                        for number in self.cls])
#
#     __rmul__ = __mul__
#
#     def size(self):
#         return len(self.cls), len(self.cls[0])
#
#     def transpose(self):
#         if isinstance(self, Matrix):
#             self.cls = [*zip(*self.cls)]  #  list(map(list, zip(*self.matrix)))
#             return Matrix(self.cls)
#
#     @staticmethod
#     def transposed(cls):
#         return Matrix([*zip(*cls.cls)])
#
# exec(stdin.read())
#######################################################################################################################

# Внесите следующие изменение в предыдущую программу:
# Измените метод __mul__ таким образом, чтобы матрицы можно было умножать как на скаляры, так и на другие матрицы. В
# случае, если две матрицы перемножить невозможно, то тогда выбросьте ошибку MatrixError. Первая матрице в ошибке  —
# это self, вторая  —  это второй операнд умножения.
# Формат ввода - Как в предыдущей задаче.
# Формат вывода - Как в предыдущей задаче.

# from sys import stdin
#
# class MatrixError(BaseException):
#     def __init__(self, cls, other):
#         self.matrix1 = cls
#         self.matrix2 = other
#
#
# class Matrix:
#     def __init__(self, cls):
#         self.cls = [lst[:] for lst in cls]
#
#     def __str__(self):
#         s = ''
#         for i in self.cls:
#             if s:
#                 s += '\n'
#             s += '\t'.join(map(str, i))
#         return s
#
#     def __add__(self, other):
#         if len(self.cls) == len(other.cls):
#             return Matrix(
#                 [[num + other.cls[j][i] for i, num in enumerate(number)]
#                  for j, number in enumerate(self.cls)])
#
#         else:
#             raise MatrixError(self, other)
#
#     def __mul__(self, other):
#         if isinstance(other, int) or isinstance(other, float):
#             return Matrix([[num * other for num in number]
#                            for number in self.cls])
#         elif isinstance(other, Matrix):
#             if self.size()[1] != other.size()[0]:
#                 raise MatrixError(self, other)
#             return Matrix(
#                 list(map(
#                     lambda x: list(
#                         map(
#                             lambda y: sum(map(
#                                 lambda z: z[0] * z[1],
#                                 zip(x, y))
#                             ),
#                             zip(*other.cls))),
#                     zip(*Matrix.transposed(self).cls))
#                 )
#             )
#
#     __rmul__ = __mul__
#
#     def size(self):
#         return len(self.cls), len(self.cls[0])
#
#     def transpose(self):
#         if isinstance(self, Matrix):
#             self.cls = [*zip(*self.cls)]
#             return Matrix(self.cls)
#
#     @staticmethod
#     def transposed(cls):
#         return Matrix([*zip(*cls.cls)])
#
# exec(stdin.read())

# Тест 1
# Входные данные:
# # Task 4 check 1
# mid = Matrix([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
# m1 = Matrix([[3, 2], [-10, 0], [14, 5]])
# m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
# print(mid * m1)
# print(mid * m2)
# print(m2 * m1)
# try:
#     m = m1 * m2
#     print("WA It should be error")
# except MatrixError as e:
#     print(e.matrix1)
#     print(e.matrix2)
#
# Вывод программы:
# 3	2
# -10	0
# 14	5
# 5.0	2.0	10.0
# -0.5	-0.25	18.0
# -22.0	-2.5	-0.125
# 135	60
# 253.0	89.0
# -42.75	-44.625
# 3	2
# -10	0
# 14	5
# 5	2	10
# -0.5	-0.25	18
# -22	-2.5	-0.125
#
#
#
# Тест 2
# Входные данные:
# # Task 4 check 2
# mid = Matrix([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
# m1 = Matrix([[3, 2], [-10, 0], [14, 5]])
# m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
# print(0.5 * m2)
# print(m2 * (0.5 * mid * m1))
#
# Вывод программы:
# 2.5	1.0	5.0
# -0.25	-0.125	9.0
# -11.0	-1.25	-0.0625
# 67.5	30.0
# 126.5	44.5
# -21.375	-22.3125
#
#
#
# Тест 3
# Входные данные:
# # Task 4 check 3
# mid = Matrix([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
# m1 = Matrix([[3, 2], [-10, 0], [14, 5]])
# m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
# print(5 * m2)
# print(m2 * (120 * mid * m1))
#
# Вывод программы:
# 25	10	50
# -2.5	-1.25	90
# -110	-12.5	-0.625
# 16200	7200
# 30360.0	10680.0
# -5130.0	-5355.0

# Тест 5
# Task 4 check 5
# m1 = Matrix([[3, 2], [-10, 0], [14, 5]])
# m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
# print(m2 * m1)
# print(Matrix.transposed(m2 * m1))
# print(m1.transpose() * m2.transpose())
# Ответ:
# 135	60
# 253.0	89.0
# -42.75	-44.625
# 135	253.0	-42.75
# 60	89.0	-44.625
# 135	253.0	-42.75
# 60	89.0	-44.625

#
# from sys import stdin
#
# class MatrixError(BaseException):
#     def __init__(self, Mtx, other):
#         self.matrix1 = Mtx
#         self.matrix2 = other
#
#
# class Matrix:
#     def __init__(self, l4l):
#         self.Mtx = [_.copy() for _ in l4l]
#
#     def __str__(self):
#         return '\n'.join(['\t'.join(map(str, self.Mtx[i]))
#                           for i in range(len(self.Mtx))])
#
#     def size(self):
#         return len(self.Mtx), len(self.Mtx[0])
#
#     def __add__(self, other):
#         if self.size() != other.size():
#             raise MatrixError(self, other)
#         return Matrix(list(map(
#             lambda a, b: list(map(
#                 lambda x, y: x + y, a, b)), self.Mtx, other.Mtx)))
#
#     def __mul__(self, other):
#         if isinstance(other, int) or isinstance(other, float):
#             return Matrix([list(map(
#                 lambda x: x * other, self.Mtx[i]))
#                 for i in range(len(self.Mtx))])
#         elif isinstance(other, Matrix):
#             if self.size()[1] != other.size()[0]:
#                 raise MatrixError(self, other)
#             return Matrix(
#                 list(map(
#                         lambda x: list(
#                             map(
#                                 lambda y: sum(map(
#                                     lambda z: z[0] * z[1],
#                                     zip(x, y))
#                                 ),
#                             zip(*other.Mtx))),
#                     zip(*Matrix.transposed(self).Mtx))
#                 )
#             )
#
#     __rmul__ = __mul__
#
#     def transpose(self):
#         self.Mtx = list(map(lambda *args: list(args), *self.Mtx))
#         return Matrix(self.Mtx)
#
#     @staticmethod
#     def transposed(M):
#         return Matrix(list(map(lambda *args: list(args), *M.Mtx)))
#
# exec(stdin.read())
#
#
# def __mul__(self, n):
#     if isinstance(n, list):
#         if len(self.l[0]) != len(n):
#             return MatrixError
#         else:
#             tmp, res = [], [] * len(self.l)
#             for i in range(len(self.l)):
#                 for j in range(len(n[0])):
#                     s = 0
#                     for k in range(len(self.l[0])):
#                         s += self.l[i][k] * n[k][j]
#                     tmp.append(s)
#                 res.append(tmp)
#                 tmp = []
#             return Matrix(res)
#     else:
#         return ([n * j for j in i] for i in self.l)
#######################################################################################################################

# Пусть экземпляр класса Matrix задаёт систему линейных алгебраических уравнений.
# Тогда добавьте в класс метод solve, принимающий вектор-строку свободных членов и возвращающий строку-список, состоящую
# из float  —  решение системы, если оно единственно. Если решений нет или оно не единственно  — выдайте какую-нибудь
# ошибку.
# Формат ввода - Как в предыдущей задаче.
# Формат вывода - Как в предыдущей задаче.

# def solve(self, vector):
#     if self.size()[1] != self.size()[0]:
#         raise Exception("The Matrix is not square!")
#     elif self.size()[1] != len(vector):
#         raise Exception("The Matrix and vector have different length!")
#     helperD = []
#     for i in range(len(vector)):
#         M = Matrix(self.cls)
#         for j in range(len(vector)):
#             M.cls[j][i] = vector[j]
#         helperD.append(Matrix.determinator(M))
#     return list(map(lambda x: x / Matrix.determinator(self), helperD))
#
#
# @staticmethod
# def determinator(M):
#     if M.size()[0] == 2:
#         return M.cls[0][0] * M.cls[1][1] - M.cls[0][1] * M.cls[1][0]
#     elif M.size()[0] == 3:
#         return \
#             M.cls[0][0] * M.cls[1][1] * M.cls[2][2] \
#             + M.cls[2][0] * M.cls[0][1] * M.cls[1][2] \
#             + M.cls[1][0] * M.cls[2][1] * M.cls[0][2] \
#             - M.cls[2][0] * M.cls[1][1] * M.cls[0][2] \
#             - M.cls[0][0] * M.cls[2][1] * M.cls[1][2] \
#             - M.cls[1][0] * M.cls[0][1] * M.cls[2][2]
#     else:
#         raise Exception("Matrix's range more than 3")

# Тест 1
# Входные данные:
# # Task 5 check 1
# m = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# print(m.solve([1,1,1]))
# Вывод программы:
# [1.0, 1.0, 1.0]
#
# Тест 2
# Входные данные:
# # Task 5 check 2
# m = Matrix([[1, 1, 1], [0, 2, 0], [0, 0, 4]])
# print(m.solve([1,1,1]))
# Вывод программы:
# [0.25, 0.5, 0.25]
#
# Тест 3
# Входные данные:
# # Task 5 check 3
# m = Matrix([[1, 1, 1], [0, 1, 2], [0.5, 1, 1.5]])
# try:
#     s = m.solve([1,1,1])
#     print('WA No solution')
# except Exception as e:
#     print('OK')
# Вывод программы:
# OK
#####################################################################################################################

# К программе в предыдущей задаче добавьте класс SquareMatrix  —  наследник Matrix с операцией возведения в степень
# __pow__, принимающей натуральную степень (включая ноль), в которую нужно возвести матрицу. Используйте быстрое
# возведение в степень.
# Формат ввода - Как в предыдущей задаче.
# Формат вывода - Как в предыдущей задаче.
# Возводить в степень можно гораздо быстрее, чем за n умножений! Для этого нужно воспользоваться следующими
# рекуррентными соотношениями: aⁿ = (a²)ⁿ/² при четном n, aⁿ=a⋅aⁿ⁻¹ при нечетном n. Реализуйте алгоритм быстрого
# возведения в степень. Если вы все сделаете правильно,то сложность вашего алгоритма будет O(logn).
# def power(a, n):
#     if n == 0:
#         return 1
#     if n % 2 == 0:
#         return power(a, n/2)**2
#     else:
#         return a*power(a, n-1)
# a = int(input())
# n = int(input())
# print(power(a, n))

# class SquareMatrix(Matrix):
#     def __mul__(self, other):
#         return SquareMatrix(super().__mul__(other).cls)
#
#     def __pow__(self, n):
#         if n in [0, 1]:
#             return self
#         elif n == 2:
#             return self * self
#         if n % 2 != 0:
#             return self * (self ** (n - 1))
#         else:
#             return (self * self) ** (n // 2)
#
# m = SquareMatrix([[1, 1, 0, 0, 0, 0],
#                   [0, 1, 1, 0, 0, 0],
#                   [0, 0, 1, 1, 0, 0],
#                   [0, 0, 0, 1, 1, 0],
#                   [0, 0, 0, 0, 1, 1],
#                   [0, 0, 0, 0, 0, 1]]
#                 )
# print(m)
# print('----------')
# print(m ** 1)
# print('----------')
# print(m ** 2)
# print('----------')
# print(m ** 3)
# print('----------')
# print(m ** 4)
# print('----------')
# print(m ** 5)

# класс полностью ###############################################################################################
from sys import stdin


class MatrixError(BaseException):
    def __init__(self, cls, other):
        self.matrix1 = cls
        self.matrix2 = other


class Matrix:
    def __init__(self, cls):
        self.cls = [lst[:] for lst in cls]

    def __str__(self):
        s = ''
        for i in self.cls:
            if s:
                s += '\n'
            s += '\t'.join(map(str, i))
        return s

    def __add__(self, other):
        if len(self.cls) == len(other.cls):
            return Matrix(
                [[num + other.cls[j][i] for i, num in enumerate(number)]
                 for j, number in enumerate(self.cls)])

        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Matrix([[num * other for num in number]
                           for number in self.cls])
        elif isinstance(other, Matrix):
            if self.size()[1] != other.size()[0]:
                raise MatrixError(self, other)
            return Matrix(
                list(map(
                    lambda x: list(
                        map(
                            lambda y: sum(map(
                                lambda z: z[0] * z[1],
                                zip(x, y))
                            ),
                            zip(*other.cls))),
                    zip(*Matrix.transposed(self).cls))
                )
            )

    __rmul__ = __mul__

    def size(self):
        return len(self.cls), len(self.cls[0])

    def transpose(self):
        if isinstance(self, Matrix):
            self.cls = [*zip(*self.cls)]
            return Matrix(self.cls)

    @staticmethod
    def transposed(cls):
        return Matrix([*zip(*cls.cls)])

    def solve(self, vector):
        if self.size()[1] != self.size()[0]:
            raise Exception("The Matrix is not square!")
        elif self.size()[1] != len(vector):
            raise Exception("The Matrix and vector have different length!")
        helperD = []
        for i in range(len(vector)):
            M = Matrix(self.cls)
            for j in range(len(vector)):
                M.cls[j][i] = vector[j]
            helperD.append(Matrix.determinator(M))
        return list(map(lambda x: x / Matrix.determinator(self), helperD))

    @staticmethod
    def determinator(M):
        if M.size()[0] == 2:
            return M.cls[0][0] * M.cls[1][1] - M.cls[0][1] * M.cls[1][0]
        elif M.size()[0] == 3:
            return \
                M.cls[0][0] * M.cls[1][1] * M.cls[2][2] \
                + M.cls[2][0] * M.cls[0][1] * M.cls[1][2] \
                + M.cls[1][0] * M.cls[2][1] * M.cls[0][2] \
                - M.cls[2][0] * M.cls[1][1] * M.cls[0][2] \
                - M.cls[0][0] * M.cls[2][1] * M.cls[1][2] \
                - M.cls[1][0] * M.cls[0][1] * M.cls[2][2]
        else:
            raise Exception("Matrix's range more than 3")


class SquareMatrix(Matrix):
    def __mul__(self, other):
        return SquareMatrix(super().__mul__(other).cls)

    def __pow__(self, n):
        if n in [0, 1]:
            return self
        elif n == 2:
            return self * self
        if n % 2 != 0:
            return self * (self ** (n - 1))
        else:
            return (self * self) ** (n // 2)


exec(stdin.read())

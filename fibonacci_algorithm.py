# from PIL import Image
# from rcviz import CallGraph, viz
#
# cg = CallGraph(filename="sort.png")
cache = {}


# @viz(cg)
# Самый долгий алгоритм - рекурсивная функция (вычисляем все заново)
def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)

# Средний алгоритм (храним вычисленное в глобальной переменной - cache)

# @viz(cg)
def fib2(n):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fib2(n - 1) + fib2(n - 2)
    return cache[n]

# строка - n_test if n_test <= 1 else fib2(n_test - 1) + fib2(n_test - 2)
# if n_test <= 1:
#     cache[n_test] = n_test
# else:
#     cache[n_test] = fib2(n_test - 1) + fib2(n_test - 2)

# Декоратор (без глобальной переменной)
# def memo(f):
#     cache = {}
#     def inner(n_test):  # функция "обертка" принимает один аргумент - n_test
#         if n_test not in cache:
#             cache[n_test] = f(n_test)
#         return cache[n_test]
#     return inner
#
# fib1 = memo(fib1)
#
# from functools import lru_cache  # такая функция памяти из библиотеки
# fib1 = lru_cache(maxsize=None)(fib1)  # maxsize=None - сохранить все числа или набрать нужное значение

# # Чтобы случайно не наплодить багов и не ломать впоследствии голову над тем, почему что-то не работает,
# # лучше декорировать функцию заранее, перед объявлением, например, так:
#
# from functools import lru_cache
#
# def memo(f):
#     cache = {}
#     def inner(n_test):
#         if n_test not in cache:
#             cache[n_test] = f(n_test)
#         return cache[n_test]
#     return inner
#
# @memo # ИЛИ также можно заменить эту строчку на @lru_cache(maxsize=None)
# def fib1(n_test):
#     assert n_test >= 0
#     return n_test if n_test <= 1 else fib1(n_test - 1) + fib1(n_test - 2)

# На этом этапе у некоторых (меня в том числе) возникла путаница с именами функций, что привело к тому, что
# кэширование не заработало. Это неприятно, когда что-то не работает.
# Посмотрим, как именно мы меняем поведение функции с помощью декоратора

# def fib(n_test):
#     return n_test if n_test < 2 else fib(n_test - 1) + fib(n_test - 2)
#
# def memo(f):
#     cache = {}
#     def wrap(n_test):
#         if n_test not in cache:
#             cache[n_test] = f(n_test)
#         return cache[n_test]
#     return wrap
#
# fib = memo(f=fib)

# Разберём самую интересную запись справа налево
# fib = memo(f=fib)
# ПРАВО - передаем функции memo аргумент f, который ссылается на ту же функцию, на которую ссылается функция
# fib -> получаем функцию wrap
# ЛЕВО - определяем, что теперь fib будет ссылаться на функцию справа т.е. wrap
# В ИТОГЕ мы поменяли не только поведение, но и зону видимости функции fib (теперь она видит cache и новую функцию f)
# Для лучшего понимаю, можно записать.
# cache = {}
#
# def f(n_test):
#     return n_test if n_test < 2 else fib(n_test - 1) + fib(n_test - 2)
#
# def fib(n_test):
#     if n_test not in cache:
#         cache[n_test] = f(n_test)
#     return cache[n_test]
# Такая функция будет работать быстро и верно. Следовательно называя новую функцию как попало и затем вызывая её
# random_name = memo(f=fib)
# random_name(80)
# мы обрекаем себя на вызов рекурсивной неоптимизированной функции fib
# cache = {}
# def f(n_test): #2
#     return n_test if n_test < 2 else fib(n_test - 1) + fib(n_test - 2)
#
# def fib(n_test): #3,.. n_test
#     return n_test if n_test < 2 else fib(n_test - 1) + fib(n_test - 2)
#
# def random_name(n_test): #1
#     if n_test not in cache:
#         cache[n_test] = f(n_test)
#     return cache[n_test]

# Есть ограничение на кол-во вызовов рекурсивных функций. Пишем функцию использующую итерацию вместо рекурсии.
def fib3(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1

# print(fib3(1185))

# Измерение времени работы функции
import time

def timed(f, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc

print(timed(fib3, 800))

from matplotlib import pyplot as plt

def compare(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
        plt.legend()
        plt.grid(True)

compare([fib1, fib3], list(range(20)))

plt.show()

compare([fib3], list(range(200)))

plt.show()

# cg.render()
# Image.open('./sort.png').show()

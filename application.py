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

# command, namespace, parent_var = (str(input().split()) for i in range(int(input())))
# command, namespace, parent_var = (input().split() for i in range(int(input())))
# print(command)
# a, b = (int(i) for i in input().split())
command, namespace, parent_var = map(str, input().split())
print(command, namespace, parent_var)
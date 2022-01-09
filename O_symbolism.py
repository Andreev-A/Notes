
# Сложение больших чисел имеет сложность О(n_test), отсюда n_test итераций цикла можно оценить как O(n_test*n_test)

# from sympy import *
#
#
# def l_rule(t, g, n_test):
#     res = str(limit(t / g, n_test, oo))
#     if res == '0':
#         return str(t) + ' имеет меньший порядок роста, чем ' + str(g)
#     elif res == 'oo':
#         return str(t) + ' имеет больший порядок роста, чем ' + str(g)
#     else:
#         return str(t) + ' имеет тот же порядок роста, что и ' + str(g)
#
#
# n_test = Symbol('n_test')
#
# funcs = {
#     n_test ** 0.5: 5 ** log(n_test),
#     n_test * log(n_test): n_test,
#     sqrt(n_test): log(n_test) ** 3,
#     100 * n_test * log(n_test): n_test + (log(n_test) ** 2),
#     factorial(n_test): 2 ** n_test,
#     2 ** n_test: 2 ** (n_test + 1),
#     10 * log(n_test): log(n_test) ** 2
# }
#
# for func1, func2 in funcs.items():
#     print(l_rule(func1, func2, n_test))


# import math
# n_test=1550
# # print(math.log(math.log(n_test, 2)))
# # print(math.sqrt(math.log(n_test, 4)))
# # print(math.log(n_test, 3))
# # print(math.log(n_test, 2) ** 2)
# # print(math.sqrt(n_test))
# # print(n_test / math.log(n_test, 5))
# # print(math.log(math.factorial(n_test),2))
# # print(3 ** math.log(n_test, 2))
# # print(n_test ** 2)
# # print(7 ** (math.log(n_test, 2)))
# # print(math.log(n_test, 2) ** (math.log(n_test, 2)))
# print(n_test ** (math.log(n_test, 2)))
# print(n_test ** (math.sqrt(n_test)))
# # print(2 ** n_test)
# # print(4 ** n_test)
# # print(2 ** (3 * n_test))
# # print(math.factorial(n_test))
# # print(2 ** (2 ** n_test))

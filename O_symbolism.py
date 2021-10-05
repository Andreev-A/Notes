# from __future__ import print_function
#
# from sympy import *
#
#
# def l_rule(t, g, n):
#     res = str(limit(t / g, n, oo))
#     if res == '0':
#         return str(t) + ' имеет меньший порядок роста, чем ' + str(g)
#     elif res == 'oo':
#         return str(t) + ' имеет больший порядок роста, чем ' + str(g)
#     else:
#         return str(t) + ' имеет тот же порядок роста, что и ' + str(g)
#
#
# n = Symbol('n')
#
# funcs = {
#     n ** 0.5: 5 ** log(n),
#     n * log(n): n,
#     sqrt(n): log(n) ** 3,
#     100 * n * log(n): n + (log(n) ** 2),
#     factorial(n): 2 ** n,
#     2 ** n: 2 ** (n + 1),
#     10 * log(n): log(n) ** 2
# }
#
# for func1, func2 in funcs.items():
#     print(l_rule(func1, func2, n))


# import math
# n=1550
# # print(math.log(math.log(n, 2)))
# # print(math.sqrt(math.log(n, 4)))
# # print(math.log(n, 3))
# # print(math.log(n, 2) ** 2)
# # print(math.sqrt(n))
# # print(n / math.log(n, 5))
# # print(math.log(math.factorial(n),2))
# # print(3 ** math.log(n, 2))
# # print(n ** 2)
# # print(7 ** (math.log(n, 2)))
# # print(math.log(n, 2) ** (math.log(n, 2)))
# print(n ** (math.log(n, 2)))
# print(n ** (math.sqrt(n)))
# # print(2 ** n)
# # print(4 ** n)
# # print(2 ** (3 * n))
# # print(math.factorial(n))
# # print(2 ** (2 ** n))


from PIL import Image
from rcviz import CallGraph, viz

cg = CallGraph(filename="sort.png")


@viz(cg)
def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


fib1(8)

cg.render()

Image.open('./sort.png').show()

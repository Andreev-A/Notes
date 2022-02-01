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

from itertools import permutations
from sys import stdin
from operator import xor

print(
    *next(
        map(
            lambda d:
            next(
                filter(
                    lambda y:
                    all(
                        map(
                            lambda x:
                            xor(y.index(x[0]) < y.index(x[1]), y.index(x[2]) < y.index(x[3])),
                            d[-1])
                    ),
                    d[:-1]
                ),
                [0, ]
            ),

            map(
                lambda j: [
                    *permutations(range(j, 0, -1), j),
                    list(map(lambda z: tuple(map(int, z.split())),
                             stdin.readlines()))
                ],
                map(int, input().split())
            )

        ),
        [0, ]
    )
)
# Т.к. во входных данных через map(int, input().split()) идёт и K и N, то у нас будет считаться два permutations. Чтобы
# не использовать второй мы используем next. Следовательно у Вас ошибка в последовательности. next на 9-й строке должен
# быть перед map на 7-й, а lambda d это filter.
#
# И посмотрите на то, что выдаёт map на 23-й строке (кстати не пойму зачем * на 25-й строке). Вы неправильно берёте из
# неё данные.
#
# И по поводу xor, не факт что грейдер импортирует библиотеку operator. Есть встроенный логический оператор, который
# подходит для наших нужд - ^. Используется как обычно: a ^ b.


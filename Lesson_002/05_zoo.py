#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
zoo.insert(1, 'bear')
print(*zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO здесь ваш код
zoo += birds
print(*zoo)

# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код
zoo.remove('elephant')
print(*zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
if 'lion' in zoo:
    lion_cage_number = zoo.index('lion')
    print('Лев в клетке -', lion_cage_number, end=' ')
if 'lark' in zoo:
    lark_cage_number = zoo.index('lark')
    print('Жаворонок в клетке -', lark_cage_number)

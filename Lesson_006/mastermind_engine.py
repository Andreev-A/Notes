import random

_hidden_number = ''


def number_generator():
    """a four-digit number, all digits of which are different, the first digit of the number is nonzero"""
    global _hidden_number
    _hidden_number = ''
    digits_list = random.sample("1234567890", 4)
    if digits_list[0] == '0':
        digits_list.append(digits_list.pop(0))
    _hidden_number = ''.join(digits_list)
    # return _hidden_number  # uncomment for debugging


def check_the_number(number):
    """report the number of "bulls" and "cows" in the named number"""
    result_of_checking = {'bulls': 0, 'cows': 0}
    for i in range(4):
        if number[i] == _hidden_number[i]:
            result_of_checking['bulls'] += 1
        else:
            if _hidden_number[i] in number:
                result_of_checking['cows'] += 1
    return result_of_checking

# def get_random_value():
#     # Берём 4 уникальные случайные цифры из набора
#     value = random.sample("1234567890", 4)
#
#     # Перемешиваем последовательность до тех пор пока не будет нуля в начале
#     # while value[0] == '0':
#     #     random.shuffle(value)
#
#     # Ну или можно просто переставить 0 в конец последовательности
#     if value[0] == '0':
#        value.append(value.pop(0))
#
#     # Склеиваем последовательность в строку и преобразуем её в число
#     return int(''.join(value))
#
# print(get_random_value())

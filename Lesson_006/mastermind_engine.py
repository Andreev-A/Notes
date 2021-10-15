import random

_hidden_number = ''


def number_generator():
    """a four-digit number, all digits of which are different, the first digit of the number is nonzero"""
    global _hidden_number
    _hidden_number = ''
    digits_list = list(map(str, range(10)))
    b = ''.join(random.sample(digits_list, 4))
    if b[0] == '0':
        b = b[1] + '0' + b[2:]
    _hidden_number = b
    return b

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
